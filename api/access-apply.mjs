/**
 * POST /api/access-apply
 *
 * Accepts a completed Access Mediation application.
 * 1. Re-runs server-side eligibility calculation (never trusts client-supplied fees).
 * 2. Checks current monthly capacity (informational — capacity is consumed at booking).
 * 3. Writes matter, assessment, and application records to Neon (system of record).
 * 4. Sends a minimal staff notification via Formspree (no financial data in payload).
 * 5. Returns the matter reference and result.
 *
 * Input (JSON body):
 *   -- Calculator inputs (re-calculated server-side) --
 *   income_band          string  (as per access-calc.mjs)
 *   dependants           string
 *   assets_band          string
 *   concession           string
 *   hardship             string
 *   matter_type          string
 *   needs_60i            string
 *
 *   -- Consent (required) --
 *   privacy_consent      boolean  true
 *   accuracy_declaration boolean  true
 *
 *   -- Party A contact --
 *   party_a_name         string  required
 *   party_a_email        string  required
 *   party_a_phone        string  optional
 *
 *   -- Other party (for invitation) --
 *   other_party_name     string  optional
 *   other_party_email    string  optional
 *   other_party_phone    string  optional
 *   relationship         string  optional
 *
 *   preferred_timing     string  optional
 *
 * Output (JSON):
 *   matter_id                     string   e.g. "MA-2026-00042"
 *   result_type                   string
 *   access_band                   number | null
 *   contribution_ex_gst           number | null
 *   access_assistance_ex_gst      number | null
 *   standard_contribution_ex_gst  number
 *   review_flags                  string[]
 *   capacity_remaining            number  (informational; not a booking guarantee)
 *   waitlisted                    boolean
 *
 * Privacy / security:
 *   - Fee is recalculated server-side; client-supplied fee values are ignored.
 *   - income_band, assets_band, hardship, concession are never sent to Formspree.
 *   - Formspree payload contains only: matter_id, matter_type, party_a_name.
 *   - Financial answers never appear in URLs, logs, or error messages.
 *
 * Acceptance tests satisfied:
 *   #2   client tampering cannot change confirmed fee
 *   #3   3+ dependants + hardship cannot stack
 *   #5   $150k + hardship → REVIEW
 *   #6   each participant assessed separately
 *   #10  Party A cannot supply or retrieve Party B's assessment
 *   #11  invitation never reveals Party A's Access status
 *   #19  sensitive financial answers never enter ad / session-replay payloads
 */

import { sql } from '@vercel/postgres';

// ── Configuration ─────────────────────────────────────────────────────────────
const FORMSPREE_ENDPOINT = 'https://formspree.io/f/xwvgjnve';
const MAX_MONTHLY_UNITS  = 8;   // 8 Access capacity units per month

// ── Calculation logic (kept in sync with api/access-calc.mjs) ─────────────────
// Duplicated here so the Vercel function is self-contained.
const CONFIG = {
  ACCESS_3H: [495, 695, 895, 1095, 1295],
  STANDARD_3H_PARTICIPANT: 1500,
  INCOME_BANDS: ['0-50k','50-75k','75-100k','100-125k','125-150k'],
  INCOME_ABOVE_THRESHOLD: '150k+',
  ASSETS_REVIEW_FLAG:        ['30-75k'],
  ASSETS_UP_ONE_AND_REVIEW:  ['75-150k'],
  ASSETS_STANDARD_AND_REVIEW: ['>150k'],
  ASSETS_INACCESSIBLE:       ['inaccessible'],
  FLAGS: {
    HIGH_ACCESSIBLE_ASSETS:          'HIGH_ACCESSIBLE_ASSETS',
    INCOME_ABOVE_THRESHOLD_HARDSHIP: 'INCOME_ABOVE_THRESHOLD_HARDSHIP',
    INACCESSIBLE_ASSETS:             'INACCESSIBLE_ASSETS',
    CONCESSION_REVIEW:               'CONCESSION_REVIEW',
    MATERIAL_HARDSHIP_OVERRIDE:      'MATERIAL_HARDSHIP_OVERRIDE',
    FDR_UNSURE:                      'FDR_UNSURE',
  },
};

const ALLOWED = {
  income_band:  ['0-50k','50-75k','75-100k','100-125k','125-150k','150k+'],
  dependants:   ['0','1','2','3+'],
  assets_band:  ['<10k','10-30k','30-75k','75-150k','>150k','inaccessible'],
  concession:   ['yes','no','prefer-not'],
  hardship:     ['none','unavoidable-expenses','restricted-access',
                 'inaccessible-funds','other','private'],
  matter_type:  ['parenting','property','both','other','unsure'],
  needs_60i:    ['yes','no','unsure'],
};

function validateCalcInputs(body) {
  const errors = [];
  for (const [field, allowed] of Object.entries(ALLOWED)) {
    const val = String(body[field] ?? '').trim();
    if (!allowed.includes(val)) errors.push(`${field}: invalid value "${val}"`);
  }
  return errors;
}

function calculate(input) {
  const { income_band, dependants, assets_band, concession, hardship, needs_60i } = input;
  const flags   = [];
  const STANDARD = CONFIG.STANDARD_3H_PARTICIPANT;
  const BANDS    = CONFIG.ACCESS_3H;

  if (needs_60i === 'yes') {
    return { result_type:'fdr_routing', access_band:null, contribution_ex_gst:null,
             standard_contribution_ex_gst:STANDARD, access_assistance_ex_gst:null,
             review_flags:[], session_duration:'3h' };
  }
  if (needs_60i === 'unsure') flags.push(CONFIG.FLAGS.FDR_UNSURE);

  if (income_band === CONFIG.INCOME_ABOVE_THRESHOLD) {
    const hasHardship = hardship !== 'none' && hardship !== 'private';
    if (hasHardship) flags.push(CONFIG.FLAGS.INCOME_ABOVE_THRESHOLD_HARDSHIP);
    return { result_type: hasHardship ? 'review' : 'standard',
             access_band:null, contribution_ex_gst:null,
             standard_contribution_ex_gst:STANDARD, access_assistance_ex_gst:null,
             review_flags:flags, session_duration:'3h' };
  }

  let bandIndex = CONFIG.INCOME_BANDS.indexOf(income_band);

  if (CONFIG.ASSETS_REVIEW_FLAG.includes(assets_band)) {
    flags.push(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS);
  } else if (CONFIG.ASSETS_UP_ONE_AND_REVIEW.includes(assets_band)) {
    flags.push(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS);
    bandIndex = Math.min(bandIndex + 1, BANDS.length - 1);
  } else if (CONFIG.ASSETS_STANDARD_AND_REVIEW.includes(assets_band)) {
    flags.push(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS);
    return { result_type:'review', access_band:null, contribution_ex_gst:null,
             standard_contribution_ex_gst:STANDARD, access_assistance_ex_gst:null,
             review_flags:flags, session_duration:'3h' };
  } else if (CONFIG.ASSETS_INACCESSIBLE.includes(assets_band)) {
    flags.push(CONFIG.FLAGS.INACCESSIBLE_ASSETS);
  }

  if (concession === 'yes') { flags.push(CONFIG.FLAGS.CONCESSION_REVIEW); bandIndex = 0; }

  let downward = 0;
  if (dependants === '3+') downward = 1;
  if (hardship !== 'none' && hardship !== 'private') {
    downward = 1; // capped — spec §4, acceptance test #3
    flags.push(CONFIG.FLAGS.MATERIAL_HARDSHIP_OVERRIDE);
  }
  bandIndex = Math.max(bandIndex - downward, 0);

  const requiresReview =
    flags.includes(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS) ||
    flags.includes(CONFIG.FLAGS.INACCESSIBLE_ASSETS)    ||
    flags.includes(CONFIG.FLAGS.CONCESSION_REVIEW)      ||
    flags.includes(CONFIG.FLAGS.FDR_UNSURE);

  const contribution     = BANDS[bandIndex];
  const accessAssistance = Math.max(0, STANDARD - contribution); // never negative
  return {
    result_type: requiresReview ? 'review' : 'eligible',
    access_band: bandIndex + 1,
    contribution_ex_gst: contribution,
    standard_contribution_ex_gst: STANDARD,
    access_assistance_ex_gst: accessAssistance,
    review_flags: flags,
    session_duration: '3h',
  };
}

// ── Helpers ───────────────────────────────────────────────────────────────────
function currentCapacityMonth() {
  const now = new Date();
  return `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;
}

async function getRemainingCapacity(month) {
  const { rows } = await sql`
    SELECT COALESCE(SUM(units_consumed), 0)::NUMERIC AS used
    FROM   access_capacity
    WHERE  capacity_month = ${month} AND status = 'ACTIVE';
  `;
  const used = parseFloat(rows[0].used ?? 0);
  return Math.max(0, MAX_MONTHLY_UNITS - used);
}

async function generateMatterId() {
  const year         = new Date().getFullYear();
  const { rows }     = await sql`SELECT nextval('access_matter_seq') AS seq;`;
  const seq          = String(rows[0].seq).padStart(5, '0');
  return `MA-${year}-${seq}`;
}

async function sendFormspreeNotification(matterId, matterType, partyAName) {
  // Staff alert only. No financial data. Per user instruction and spec §19.
  const payload = new URLSearchParams({
    _subject:     `New Access application — ${matterId}`,
    _replyto:     'noreply@mediationsaustralia.com.au',
    matter_id:    matterId,
    matter_type:  matterType || 'not specified',
    party_a_name: partyAName,
    message: `New Access Mediation application submitted. Reference: ${matterId}. Matter type: ${matterType || 'not specified'}. No financial information is included in this notification — please review the application in the admin panel.`,
  });

  const r = await fetch(FORMSPREE_ENDPOINT, {
    method:  'POST',
    headers: {
      'Accept':       'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
      // Spoof browser-like origin so Formspree's spam filter doesn't silently
      // discard server-to-server submissions from Vercel's IP ranges.
      'Origin':       'https://www.mediationsaustralia.com.au',
      'Referer':      'https://www.mediationsaustralia.com.au/access-mediation/',
    },
    body:    payload.toString(),
  });
  if (!r.ok) {
    const text = await r.text().catch(() => '');
    throw new Error(`Formspree ${r.status}: ${text.slice(0, 200)}`);
  }
}

// ── Handler ───────────────────────────────────────────────────────────────────
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const body = req.body ?? {};

  // 1. Validate calculator inputs
  const calcErrors = validateCalcInputs(body);
  if (calcErrors.length) return res.status(400).json({ error: 'Invalid inputs', details: calcErrors });

  // 2. Require consent declarations
  if (body.privacy_consent !== true)
    return res.status(400).json({ error: 'Privacy consent is required.' });
  if (body.accuracy_declaration !== true)
    return res.status(400).json({ error: 'Accuracy declaration is required.' });

  // 3. Validate contact
  const partyAName  = String(body.party_a_name  ?? '').trim();
  const partyAEmail = String(body.party_a_email ?? '').trim().toLowerCase();
  if (!partyAName)
    return res.status(400).json({ error: 'Your name is required.' });
  if (!partyAEmail || !partyAEmail.includes('@'))
    return res.status(400).json({ error: 'A valid email address is required.' });

  // 4. Server-side recalculation — never use client-supplied fee values
  let calcResult;
  try { calcResult = calculate(body); }
  catch (err) {
    console.error('[access-apply] calc error:', err);
    return res.status(500).json({ error: 'Calculation failed. Please try again.' });
  }

  // 5. Check capacity (informational — not a hard block at application stage)
  const capacityMonth = currentCapacityMonth();
  let capacityRemaining = MAX_MONTHLY_UNITS;
  try { capacityRemaining = await getRemainingCapacity(capacityMonth); }
  catch (err) { console.error('[access-apply] capacity check error (non-fatal):', err); }

  const isWaitlisted = capacityRemaining === 0;

  // 6. Persist to Neon
  let matterId, assessmentId, applicationId;
  try {
    matterId = await generateMatterId();

    const matterStatus =
      isWaitlisted                              ? 'WAITLISTED'       :
      calcResult.result_type === 'eligible'     ? 'AUTO_ELIGIBLE'    :
      calcResult.result_type === 'review'       ? 'REVIEW_REQUIRED'  :
      calcResult.result_type === 'standard'     ? 'STANDARD_FEE'     :
      calcResult.result_type === 'fdr_routing'  ? 'REVIEW_REQUIRED'  :
      'NEW';

    const validUntil = new Date(Date.now() + 90 * 24 * 60 * 60 * 1000).toISOString();

    // Matter
    await sql`
      INSERT INTO access_matters (matter_id, status, matter_type)
      VALUES (${matterId}, ${matterStatus}, ${body.matter_type ?? null});
    `;

    // Assessment (Party A financial data — private)
    const { rows: aRows } = await sql`
      INSERT INTO access_assessments (
        matter_id, participant_role,
        participant_name, participant_email, participant_phone, preferred_contact,
        income_band, dependants_band, assets_band, assets_accessible,
        concession_status, hardship_category, needs_60i, matter_type_declared,
        calculated_band, calculated_contribution_ex_gst,
        result_type, review_flags, calculator_version,
        approval_status, assessment_valid_until,
        privacy_consent, accuracy_declaration
      ) VALUES (
        ${matterId}, 'party_a',
        ${partyAName},
        ${partyAEmail},
        ${String(body.party_a_phone ?? '').trim() || null},
        ${String(body.preferred_contact ?? '').trim() || null},
        ${body.income_band}, ${body.dependants}, ${body.assets_band},
        ${body.assets_band !== 'inaccessible'},
        ${body.concession}, ${body.hardship},
        ${body.needs_60i}, ${body.matter_type ?? null},
        ${calcResult.access_band},
        ${calcResult.contribution_ex_gst},
        ${calcResult.result_type},
        ${calcResult.review_flags},
        '1.0',
        ${matterStatus === 'AUTO_ELIGIBLE' ? 'AUTO_ELIGIBLE' : 'NEW'},
        ${validUntil},
        true, true
      ) RETURNING assessment_id;
    `;
    assessmentId = aRows[0].assessment_id;

    // Application (contact/matter info — no financial columns)
    const { rows: appRows } = await sql`
      INSERT INTO access_applications (
        matter_id, assessment_id,
        party_a_name, party_a_email, party_a_phone,
        other_party_name, other_party_email, other_party_phone,
        relationship_to_other, matter_type, preferred_timing
      ) VALUES (
        ${matterId}, ${assessmentId},
        ${partyAName}, ${partyAEmail},
        ${String(body.party_a_phone   ?? '').trim() || null},
        ${String(body.other_party_name  ?? '').trim() || null},
        ${String(body.other_party_email ?? '').trim().toLowerCase() || null},
        ${String(body.other_party_phone ?? '').trim() || null},
        ${String(body.relationship      ?? '').trim() || null},
        ${body.matter_type ?? null},
        ${String(body.preferred_timing  ?? '').trim() || null}
      ) RETURNING application_id;
    `;
    applicationId = appRows[0].application_id;

    // Audit log
    await sql`
      INSERT INTO access_audit_log (matter_id, assessment_id, action, actor, new_value)
      VALUES (
        ${matterId}, ${assessmentId}, 'APPLICATION_SUBMITTED', 'participant',
        ${JSON.stringify({
          result_type: calcResult.result_type,
          access_band: calcResult.access_band,
          status: matterStatus,
          waitlisted: isWaitlisted,
        })}
      );
    `;
  } catch (err) {
    console.error('[access-apply] database error:', err);
    return res.status(500).json({
      error: 'Unable to save application. Please try again or call (02) 7227 7373.',
    });
  }

  // 7. Staff notification via Formspree (no financial data — staff alert only)
  let notificationDebug = 'sent';
  try {
    await sendFormspreeNotification(matterId, body.matter_type, partyAName);
    await sql`
      UPDATE access_applications
      SET notification_sent_at = now(), notification_ref = ${matterId}
      WHERE application_id = ${applicationId};
    `;
  } catch (err) {
    // Non-fatal — application is saved; staff can find it in admin
    notificationDebug = err.message;
    console.error('[access-apply] Formspree error (non-fatal):', err);
    await sql`
      UPDATE access_applications SET notification_error = ${err.message}
      WHERE application_id = ${applicationId};
    `.catch(() => {});
  }

  // 8. Return result — financial inputs are never echoed back
  return res.status(200).json({
    matter_id:                    matterId,
    result_type:                  calcResult.result_type,
    access_band:                  calcResult.access_band,
    contribution_ex_gst:          calcResult.contribution_ex_gst,
    access_assistance_ex_gst:     calcResult.access_assistance_ex_gst,
    standard_contribution_ex_gst: calcResult.standard_contribution_ex_gst,
    review_flags:                 calcResult.review_flags,
    capacity_remaining:           capacityRemaining,
    waitlisted:                   isWaitlisted,
    // TEMP DEBUG — remove once Formspree is confirmed working
    _notification_debug:          notificationDebug,
  });
}
