/**
 * POST /api/enquiry
 *
 * Accepts guided or quick-enquiry form submissions.
 *
 * Security:
 *   - Server-side input validation; client payload is untrusted.
 *   - Honeypot field (_hp) must be empty.
 *   - Rate limiting: max 5 submissions per IP per 15 minutes (Neon).
 *   - Idempotency: duplicate submission_id returns 200 without double-write.
 *   - No sensitive fields (safety_flag detail, message, contact) in Formspree.
 *   - No sensitive fields in logs or error messages.
 *   - Bearer-authenticated admin endpoint for full detail retrieval.
 *
 * Privacy:
 *   - Financial/hardship answers are NOT collected by this endpoint.
 *   - Safety flag value is stored in Neon only; never forwarded externally.
 *   - Free-text message is stored in enquiry_contacts only; never in Formspree.
 *   - Contact details are in a separate restricted table.
 *
 * Routing priority (deterministic, no AI):
 *   1. HUMAN_REVIEW      — safety/coercion/child risk/capacity/urgent deadline
 *   2. ACCESS_REVIEW     — family + genuine financial hardship
 *   3. PUBLIC_SERVICE_INFORMATION — free/community service preference
 *   4. PREPARATION_NURTURE — disclosure or legal prep outstanding
 *   5. PRIORITY_INTAKE   — both parties willing + ready + standard fee
 *   6. ENGAGE_OTHER_PARTY — other party unknown/not asked (internal queue only)
 *   7. GENERAL_INTAKE    — all other cases
 *
 * note: `not_applicable` party_b_status routes to GENERAL_INTAKE or
 * PRIORITY_INTAKE (not ENGAGE_OTHER_PARTY — no other party exists).
 */

import { sql } from '@vercel/postgres';

const FORMSPREE_ENDPOINT  = process.env.FORMSPREE_ENDPOINT || 'https://formspree.io/f/mnpjbroe';
const ROUTING_RULES_VER   = '2026-10-v1';
const CONSENT_VER         = '2026-10-v1';
const RATE_LIMIT_WINDOW   = 15 * 60 * 1000;  // 15 minutes in ms
const RATE_LIMIT_MAX      = 5;                // submissions per IP per window

// In-memory fallback rate limiter (per serverless instance — imperfect but adds a
// layer when Neon is unreachable). Entries expire after RATE_LIMIT_WINDOW.
const _memRateMap = new Map(); // ip → [timestamp, ...]
function memRateLimitExceeded(ip) {
  const now = Date.now();
  const cutoff = now - RATE_LIMIT_WINDOW;
  const hits = (_memRateMap.get(ip) ?? []).filter(t => t > cutoff);
  _memRateMap.set(ip, [...hits, now]);
  return hits.length >= RATE_LIMIT_MAX;
}

// ── Validation helpers ────────────────────────────────────────────────────────

const VALID_CATEGORIES = new Set([
  'family_parenting','family_property','family_combined',
  'workplace_employment','commercial_business','estate_inheritance',
  'elder_family','neighbour_property','construction_real_estate','other_unsure',
]);
const VALID_STAGES = new Set([
  'exploring','discussing','ready_to_arrange','lawyers_involved',
  'proceedings_started','court_date','agreement_needs_formalisation','unsure',
]);
const VALID_PARTY_B = new Set([
  'agreed','open_to_discussion','unsure','not_asked','declined','not_applicable','prefer_not_to_say',
]);
const VALID_DELIVERY = new Set(['online','face_to_face','either','unsure']);
const VALID_TIMING   = new Set(['urgent','within_2_weeks','within_month','flexible']);
const VALID_FEE_PREF = new Set([
  'standard_private','want_fee_information','standard_fee_hardship','need_free_service','unsure',
]);
const VALID_SAFETY   = new Set(['no','yes']);
const VALID_VARIANTS = new Set(['guided','quick']);
const FAMILY_CATS    = new Set(['family_parenting','family_property','family_combined']);

function isNonEmpty(v) { return typeof v === 'string' && v.trim().length > 0; }
function isBool(v)     { return v === true || v === false; }

function validateGuidedPayload(b) {
  const errs = [];
  if (!VALID_CATEGORIES.has(b.matter_category))   errs.push('invalid matter_category');
  if (!VALID_STAGES.has(b.stage))                  errs.push('invalid stage');
  if (!VALID_PARTY_B.has(b.party_b_status))        errs.push('invalid party_b_status');
  if (!VALID_DELIVERY.has(b.delivery_preference))  errs.push('invalid delivery_preference');
  if (!VALID_TIMING.has(b.timing))                 errs.push('invalid timing');
  if (!VALID_FEE_PREF.has(b.fee_preference))       errs.push('invalid fee_preference');
  if (!VALID_SAFETY.has(b.safety_flag))            errs.push('invalid safety_flag');
  if (b.safe_email !== true && b.safe_phone !== true) errs.push('at_least_one_safe_contact required');
  if (!isNonEmpty(b.name))                         errs.push('name required');
  if (b.safe_email && !isNonEmpty(b.email))        errs.push('email required when safe_email');
  if (!isBool(b.privacy_consent) || !b.privacy_consent) errs.push('privacy_consent required');
  if (!isBool(b.accuracy_declaration) || !b.accuracy_declaration) errs.push('accuracy_declaration required');
  return errs;
}

function validateQuickPayload(b) {
  const errs = [];
  if (!isNonEmpty(b.name)) errs.push('name required');
  if (!isNonEmpty(b.email) && !isNonEmpty(b.phone)) errs.push('email or phone required');
  if (!isBool(b.privacy_consent) || !b.privacy_consent) errs.push('privacy_consent required');
  return errs;
}

// ── Routing engine ─────────────────────────────────────────────────────────────

function determineSafetyFlag(b) {
  if (b.safety_flag === 'yes') return true;
  return false;
}

function determineUrgentDeadline(b) {
  if (b.stage === 'court_date') return true;
  if (b.timing === 'urgent' && (b.stage === 'proceedings_started' || b.stage === 'lawyers_involved')) return true;
  return false;
}

function determineElderCapacity(b) {
  if (b.matter_category !== 'elder_family') return false;
  return b.branch_answers?.capacity_concern === 'yes' || b.branch_answers?.safeguarding === 'yes';
}

function determineRoute(b) {
  const reviewReasons = [];
  const tags = [];

  // Priority 1: HUMAN_REVIEW
  if (determineSafetyFlag(b)) reviewReasons.push('safety_flag');
  if (determineUrgentDeadline(b)) reviewReasons.push('urgent_deadline');
  if (determineElderCapacity(b)) reviewReasons.push('capacity_or_safeguarding');
  if (reviewReasons.length > 0) {
    if (determineUrgentDeadline(b)) tags.push('urgent_deadline');
    return { operational_queue: 'HUMAN_REVIEW', professional_review_required: true, review_reasons: reviewReasons, tags };
  }

  // Priority 2: ACCESS_REVIEW — family + genuine financial hardship (no prior page visit required)
  if (FAMILY_CATS.has(b.matter_category) && b.fee_preference === 'standard_fee_hardship') {
    return { operational_queue: 'ACCESS_REVIEW', professional_review_required: false, review_reasons: [], tags };
  }

  // Priority 3: PUBLIC_SERVICE_INFORMATION — free/community preference
  if (b.fee_preference === 'need_free_service') {
    return { operational_queue: 'PUBLIC_SERVICE_INFORMATION', professional_review_required: false, review_reasons: [], tags };
  }

  // Priority 3.5: Non-family hardship — staff fee assessment before routing
  // Family hardship was caught at P2 (ACCESS_REVIEW). Non-family hardship must not
  // enter ENGAGE_OTHER_PARTY; flag it so staff can assess fee options first.
  if (b.fee_preference === 'standard_fee_hardship') {
    tags.push('financial_hardship_flag');
    return { operational_queue: 'GENERAL_INTAKE', professional_review_required: false, review_reasons: [], tags };
  }

  // Priority 4: PREPARATION_NURTURE — disclosure or legal prep outstanding
  const disclosureOutstanding = (
    (b.matter_category === 'family_property' || b.matter_category === 'family_combined') &&
    (b.branch_answers?.disclosure_readiness === 'not_started' || b.branch_answers?.disclosure_readiness === 'in_progress') &&
    (b.branch_answers?.legal_advice === 'neither' || b.branch_answers?.legal_advice === 'one_party')
  );
  const commercialPrepOutstanding = (
    b.matter_category === 'commercial_business' &&
    b.branch_answers?.settlement_proposal === 'no' &&
    b.stage === 'exploring'
  );
  if (disclosureOutstanding || commercialPrepOutstanding) {
    return { operational_queue: 'PREPARATION_NURTURE', professional_review_required: false, review_reasons: [], tags };
  }

  // Priority 5: PRIORITY_INTAKE — both parties willing + ready + standard pathway
  const partyWilling = b.party_b_status === 'agreed' || b.party_b_status === 'open_to_discussion' || b.party_b_status === 'not_applicable';
  const stageReady   = b.stage === 'ready_to_arrange' || b.stage === 'discussing';
  const standardFee  = b.fee_preference === 'standard_private' || b.fee_preference === 'want_fee_information';
  if (partyWilling && stageReady && standardFee) {
    // not_applicable goes here too (no other party to engage)
    return { operational_queue: 'PRIORITY_INTAKE', professional_review_required: false, review_reasons: [], tags };
  }

  // Priority 6: ENGAGE_OTHER_PARTY — other party status unknown/not asked (internal queue only)
  // never applies to not_applicable (no other party)
  if (b.party_b_status === 'not_asked' || b.party_b_status === 'unsure') {
    return { operational_queue: 'ENGAGE_OTHER_PARTY', professional_review_required: false, review_reasons: [], tags };
  }

  // Priority 7: GENERAL_INTAKE — all other cases (including not_applicable, declined, prefer_not_to_say)
  return { operational_queue: 'GENERAL_INTAKE', professional_review_required: false, review_reasons: [], tags };
}

// ── Rate limiting (Neon-based) ────────────────────────────────────────────────

async function checkRateLimit(ip) {
  try {
    const windowStart = new Date(Date.now() - RATE_LIMIT_WINDOW).toISOString();
    const result = await sql`
      SELECT COUNT(*) AS cnt
      FROM enquiry_audit_log
      WHERE event_type = 'SUBMITTED'
        AND actor = ${ip}
        AND created_at > ${windowStart}
    `;
    return parseInt(result.rows[0]?.cnt ?? '0', 10) >= RATE_LIMIT_MAX;
  } catch {
    // Neon unavailable — fall back to in-memory limiter (per-instance; not cluster-wide)
    // Returns { limited: bool, fallback: true } to allow response header annotation
    return { limited: memRateLimitExceeded(ip), fallback: true };
  }
}

// ── Formspree notification (minimal — no sensitive data) ──────────────────────
//
// HUMAN_REVIEW: ultra-minimal payload — no name, no _replyto, no category.
//   Subject says "URGENT HUMAN REVIEW" only. Staff retrieve full detail via admin.
// All other queues: standard minimal payload (name + safe contact prefs + category).
// Retry once on transient failure. Returns true if notification was sent successfully.

async function sendFormspreeNotification(submissionId, route, b) {
  const isHumanReview = route.operational_queue === 'HUMAN_REVIEW';
  const isSafetyFlagged = b.safety_flag === 'yes';

  let payload;
  if (isHumanReview) {
    // Minimal: reference + urgency only. No name, no contact detail, no category.
    // Prevents sensitive context appearing in an email subject or notification preview.
    payload = {
      submission_id:    submissionId,
      operational_queue: 'HUMAN_REVIEW',
      professional_review_required: true,
      _subject:         `URGENT REVIEW REQUIRED — Ref: MA-ENQ-${submissionId.replace(/-/g,'').slice(0,8).toUpperCase()}`,
    };
  } else {
    payload = {
      submission_id:               submissionId,
      operational_queue:           route.operational_queue,
      professional_review_required: route.professional_review_required,
      form_variant:                b.form_variant ?? 'guided',
      matter_category:             b.matter_category ?? null,
      stage:                       b.stage ?? null,
      delivery_preference:         b.delivery_preference ?? null,
      timing:                      b.timing ?? null,
      safe_email:                  b.safe_email ?? null,
      safe_voicemail:              b.safe_voicemail ?? null,
      preferred_contact_time:      b.preferred_contact_time ?? null,
      name:                        b.name ?? null,
      _subject:                    `[${route.operational_queue}] New enquiry — Mediations Australia`,
      _replyto:                    (!isSafetyFlagged && b.email) ? b.email : undefined,
    };
  }

  let attempts = 0;
  let lastError = null;
  for (let attempt = 0; attempt < 2; attempt++) {
    attempts++;
    try {
      const r = await fetch(FORMSPREE_ENDPOINT, {
        method:  'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body:    JSON.stringify(payload),
      });
      if (r.ok) return { ok: true, attempts, lastError: null };
      lastError = `http_${r.status}`;
    } catch {
      lastError = 'network_error';
      if (attempt < 1) await new Promise(res => setTimeout(res, 1000));
    }
  }
  return { ok: false, attempts, lastError };
}

// ── Neon writes ───────────────────────────────────────────────────────────────

async function writeEnquiry({ submissionId, formVariant, b, route, ip, attribution }) {
  const result = await sql`
    INSERT INTO enquiries (
      submission_id, form_variant, schema_version, routing_rules_version,
      submitted_at, matter_category, stage, desired_outcome, party_b_status,
      enquirer_role, delivery_preference, state, city, timing, fee_preference,
      operational_queue, professional_review_required, review_reasons, tags,
      safe_email, safe_voicemail, safe_phone, preferred_contact_time, safety_flag,
      attribution_landing, attribution_referrer, attribution_utm_source,
      attribution_utm_medium, attribution_utm_campaign,
      consent_version, privacy_consent, accuracy_declaration
    ) VALUES (
      ${submissionId}, ${formVariant}, ${'1.0'}, ${ROUTING_RULES_VER},
      NOW(), ${b.matter_category ?? null}, ${b.stage ?? null},
      ${b.desired_outcome ?? null}, ${b.party_b_status ?? null},
      ${b.enquirer_role ?? null}, ${b.delivery_preference ?? null},
      ${b.state ?? null}, ${b.city ?? null}, ${b.timing ?? null},
      ${b.fee_preference ?? null},
      ${route.operational_queue}, ${route.professional_review_required},
      ${route.review_reasons}, ${route.tags},
      ${b.safe_email ?? null}, ${b.safe_voicemail ?? null},
      ${b.safe_phone ?? null}, ${b.preferred_contact_time ?? null},
      ${b.safety_flag ?? null},
      ${attribution.landing ?? null}, ${attribution.referrer ?? null},
      ${attribution.utm_source ?? null}, ${attribution.utm_medium ?? null},
      ${attribution.utm_campaign ?? null},
      ${CONSENT_VER}, ${b.privacy_consent}, ${b.accuracy_declaration ?? false}
    )
    ON CONFLICT (submission_id) DO NOTHING
  `;

  // Duplicate: ON CONFLICT fired — return existing record data
  if (result.rowCount === 0) {
    const existing = await sql`
      SELECT submission_id, operational_queue FROM enquiries WHERE submission_id = ${submissionId} LIMIT 1
    `;
    return { inserted: false, existing: existing.rows[0] ?? null };
  }

  // Contact details in separate restricted table
  await sql`
    INSERT INTO enquiry_contacts (enquiry_submission_id, name, email, phone, message)
    VALUES (
      ${submissionId},
      ${b.name ?? null},
      ${b.email ?? null},
      ${b.phone ?? null},
      ${b.message ?? null}
    )
  `;

  // Branch-specific answers (if provided)
  if (b.branch_answers && typeof b.branch_answers === 'object') {
    const safe = b.branch_answers;
    const allowed = [
      'issues','existing_arrangements','disclosure_readiness','legal_advice',
      'complexity','enquirer_role_detail','org_size','issue_type','parties_type',
      'settlement_proposal','estate_role','estate_issue','estate_stage',
      'elder_issue','elder_role','locality','council_stage',
      'construction_issue','construction_role','expert_report',
    ];
    for (const key of allowed) {
      if (safe[key] !== undefined && safe[key] !== null) {
        const val = Array.isArray(safe[key]) ? safe[key].join(',') : String(safe[key]);
        await sql`
          INSERT INTO enquiry_branch_answers (enquiry_submission_id, answer_key, answer_value)
          VALUES (${submissionId}, ${key}, ${val})
        `;
      }
    }
  }

  // Audit log (IP stored here only, not in main enquiry record)
  await sql`
    INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor)
    VALUES (${submissionId}, 'SUBMITTED', ${ip})
  `;

  return { inserted: true };
}

// ── Main handler ──────────────────────────────────────────────────────────────

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const b = req.body ?? {};

  // Honeypot check (silent — don't tip off bots)
  if (b._hp && b._hp !== '') {
    return res.status(200).json({ ok: true, submission_id: 'honeypot', reference: 'MA-ENQ-BLOCKED' });
  }

  const formVariant = VALID_VARIANTS.has(b.form_variant) ? b.form_variant : 'quick';

  // ── Validate ────────────────────────────────────────────────────────────────
  const errors = formVariant === 'guided'
    ? validateGuidedPayload(b)
    : validateQuickPayload(b);

  if (errors.length > 0) {
    return res.status(400).json({ error: 'Validation failed', details: errors });
  }

  // ── Rate limit ──────────────────────────────────────────────────────────────
  const ip = String(
    req.headers['x-forwarded-for']?.split(',')[0]?.trim() ?? 'unknown'
  ).slice(0, 45);

  const rl = await checkRateLimit(ip);
  const rateLimited = typeof rl === 'object' ? rl.limited : rl;
  const rateLimitFallback = typeof rl === 'object' ? rl.fallback : false;
  if (rateLimited) {
    return res.status(429).json({ error: 'Too many submissions. Please try again later or call (02) 7227 7373.' });
  }
  if (rateLimitFallback) {
    res.setHeader('X-Rate-Limit-Mode', 'memory-fallback');
  }

  // ── Idempotency ─────────────────────────────────────────────────────────────
  const submissionId = (typeof b.submission_id === 'string' && /^[a-f0-9-]{36}$/.test(b.submission_id))
    ? b.submission_id
    : crypto.randomUUID();

  // ── Routing ─────────────────────────────────────────────────────────────────
  const route = formVariant === 'guided'
    ? determineRoute(b)
    : { operational_queue: 'GENERAL_INTAKE', professional_review_required: false, review_reasons: [], tags: [] };

  // ── Attribution (strip sensitive params) ───────────────────────────────────
  const attribution = {
    landing:       (typeof b.attribution_landing   === 'string') ? b.attribution_landing.slice(0, 200)   : null,
    referrer:      (typeof b.attribution_referrer  === 'string') ? b.attribution_referrer.slice(0, 300)   : null,
    utm_source:    (typeof b.attribution_utm_source === 'string') ? b.attribution_utm_source.slice(0, 80)  : null,
    utm_medium:    (typeof b.attribution_utm_medium === 'string') ? b.attribution_utm_medium.slice(0, 80)  : null,
    utm_campaign:  (typeof b.attribution_utm_campaign === 'string') ? b.attribution_utm_campaign.slice(0, 100) : null,
  };

  // ── Write to Neon (atomic ON CONFLICT idempotency) ──────────────────────────
  let writeResult;
  try {
    writeResult = await writeEnquiry({ submissionId, formVariant, b, route, ip, attribution });
  } catch {
    // Neon unavailable — return truthful error with alternative contact route.
    // Do NOT tell the visitor their enquiry was received.
    return res.status(503).json({
      error: 'We could not save your enquiry right now. Please call us on (02) 7227 7373 or email hello@mediationsaustralia.com.au and we will help you directly.',
      fallback: true,
    });
  }

  // Duplicate submission_id — idempotent 200
  if (!writeResult.inserted) {
    const ex = writeResult.existing;
    const sid = ex?.submission_id ?? submissionId;
    return res.status(200).json({
      ok: true,
      submission_id: sid,
      reference: `MA-ENQ-${sid.replace(/-/g,'').slice(0,8).toUpperCase()}`,
      operational_queue: ex?.operational_queue ?? route.operational_queue,
      duplicate: true,
    });
  }

  // ── Formspree notification + attempt tracking ───────────────────────────────
  const notifResult = await sendFormspreeNotification(submissionId, route, b);
  try {
    await sql`
      UPDATE enquiries
      SET formspree_notified      = ${notifResult.ok},
          notification_attempts   = ${notifResult.attempts},
          notification_last_error = ${notifResult.lastError}
      WHERE submission_id = ${submissionId}
    `;
  } catch { /* non-fatal — submission is safe in Neon */ }

  // ── Response ────────────────────────────────────────────────────────────────
  const refShort = submissionId.replace(/-/g, '').slice(0, 8).toUpperCase();
  return res.status(200).json({
    ok: true,
    submission_id: submissionId,
    reference: `MA-ENQ-${refShort}`,
    operational_queue: route.operational_queue,
    professional_review_required: route.professional_review_required,
  });
}
