/**
 * GET /api/agent-intake                       — paginated feed (default: metadata only)
 * GET /api/agent-intake?detail=full           — paginated feed with full enquiry detail
 * GET /api/agent-intake?id=<uuid>             — single record, metadata only
 * GET /api/agent-intake?id=<uuid>&detail=full — single record, full detail
 *
 * Auth:       Authorization: Bearer <AGENT_INTAKE_TOKEN>
 * Rate limit: 60 requests per hour (shared across all modes)
 * Cache:      Cache-Control: no-store on every response
 *
 * MA-OPS-002 (approved Dan Toombs 2026-10-13) — interim until ResolveOS is live:
 *   ?detail=full returns contact PII (name, email, phone), free-text narrative,
 *   ordered form answers with human-readable labels, and source/attribution fields.
 *   HUMAN_REVIEW records returned in full when detail=full (restricted:true kept).
 *   Full-detail access is logged without logging bodies.
 *
 * Cursor: Opaque base64-encoded JSON { seq: "<BIGSERIAL id as string>" }
 *   MA-OPS-002 ticket requested composite (submitted_at + submission_id) cursor.
 *   BIGSERIAL id cursor (live since Stage D) is strictly superior — integer comparison,
 *   guaranteed unique, no timestamp precision edge cases. Kept as-is.
 *
 * Default (no ?detail) response — byte-for-byte unchanged from Stage D.
 */

import { sql } from '@vercel/postgres';

const RATE_LIMIT_WINDOW = 60 * 60 * 1000;
const RATE_LIMIT_MAX    = 60;
const _rateMap          = new Map();

// ── Human-readable value labels ────────────────────────────────────────────────

const VALUE_LABELS = {
  matter_category: {
    family_parenting:         'Parenting arrangements or children',
    family_property:          'Property or financial settlement',
    family_combined:          'Both parenting and property',
    workplace_employment:     'Workplace or employment',
    commercial_business:      'Business or commercial dispute',
    estate_inheritance:       'Estate or inheritance',
    elder_family:             'Elder care or family decision-making',
    neighbour_property:       'Neighbour, boundary or strata',
    construction_real_estate: 'Construction or real estate',
    other_unsure:             'Not sure / something else',
  },
  stage: {
    exploring:                     'Just exploring options',
    discussing:                    'Trying to discuss but stuck',
    ready_to_arrange:              'Ready to arrange mediation',
    lawyers_involved:              'Lawyers are involved',
    proceedings_started:           'Court proceedings have started',
    court_date:                    'There is a court date',
    agreement_needs_formalisation: 'We have an agreement that needs formalising',
    unsure:                        'Not sure',
  },
  party_b_status: {
    agreed:             'Yes, and they are willing',
    open_to_discussion: 'Yes, and they seem open',
    unsure:             'Not sure',
    not_asked:          "I haven't raised it yet",
    declined:           'They have said no',
    not_applicable:     'Not applicable',
    prefer_not_to_say:  'Prefer not to say',
  },
  delivery_preference: {
    online:       'Online (video)',
    face_to_face: 'In person',
    either:       'Either — flexible',
    unsure:       'Not sure',
  },
  timing: {
    urgent:         'As soon as possible',
    within_2_weeks: 'Within 2 weeks',
    within_month:   'Within a month',
    flexible:       'Flexible',
  },
  fee_preference: {
    standard_private:     'I will pay standard fees',
    want_fee_information: "I'd like to understand what it costs first",
    standard_fee_hardship:'Standard fee would be a genuine hardship',
    need_free_service:    'I need a free or community service',
    unsure:               'Not sure',
  },
  safety_flag: { no: 'No', yes: 'Yes' },
  preferred_contact_time: {
    morning: 'Morning', afternoon: 'Afternoon', evening: 'Evening', flexible: 'Flexible',
  },
};

// Ordered main-form questions for the answers array (guided form; form step order)
const GUIDED_QUESTIONS = [
  { id: 'matter_category',        label: 'What type of dispute is this?' },
  { id: 'stage',                  label: 'Where are things at?' },
  { id: 'party_b_status',         label: 'Does the other party know about mediation?' },
  { id: 'delivery_preference',    label: 'How would you prefer to attend?' },
  { id: 'timing',                 label: 'When are you hoping to mediate?' },
  { id: 'state',                  label: 'Your state' },
  { id: 'fee_preference',         label: 'Fees and pathway' },
  { id: 'safety_flag',            label: 'Is there a safety, pressure or deadline concern?' },
  { id: 'safe_email',             label: 'Is email safe to use?' },
  { id: 'safe_voicemail',         label: 'Is voicemail safe?' },
  { id: 'safe_phone',             label: 'Is phone safe to use?' },
  { id: 'preferred_contact_time', label: 'Best time to call' },
];

// Category-specific branch questions (stored in enquiry_branch_answers)
const BRANCH_QUESTIONS = [
  { id: 'issues',                label: 'What are the main issues?' },
  { id: 'existing_arrangements', label: 'Are there existing parenting arrangements?' },
  { id: 'disclosure_readiness',  label: 'How far along is financial disclosure?' },
  { id: 'legal_advice',          label: 'Have both parties received independent legal advice?' },
  { id: 'complexity',            label: 'How complex is the dispute?' },
  { id: 'enquirer_role_detail',  label: 'What is your role in this matter?' },
  { id: 'org_size',              label: 'Organisation size' },
  { id: 'issue_type',            label: 'Type of issue' },
  { id: 'parties_type',          label: 'Who are the parties involved?' },
  { id: 'settlement_proposal',   label: 'Has a settlement proposal been prepared?' },
  { id: 'estate_role',           label: 'Role in estate matter' },
  { id: 'estate_issue',          label: 'Estate issue type' },
  { id: 'estate_stage',          label: 'Stage of estate matter' },
  { id: 'elder_issue',           label: 'Elder care issue type' },
  { id: 'elder_role',            label: 'Role in elder matter' },
  { id: 'locality',              label: 'Local government area' },
  { id: 'council_stage',         label: 'Council dispute stage' },
  { id: 'construction_issue',    label: 'Construction issue type' },
  { id: 'construction_role',     label: 'Role in construction matter' },
  { id: 'expert_report',         label: 'Has an expert report been obtained?' },
];

const SELECT_COLS = [
  'id', 'submission_id', 'form_variant', 'schema_version', 'submitted_at',
  'matter_category', 'stage', 'party_b_status', 'delivery_preference', 'timing',
  'state', 'city', 'fee_preference', 'operational_queue', 'professional_review_required',
  'review_reasons', 'tags', 'safe_email', 'safe_voicemail', 'safe_phone',
  'preferred_contact_time', 'safety_flag', 'formspree_notified',
  'notification_attempts', 'notification_last_error',
  'attribution_landing', 'attribution_utm_source', 'attribution_utm_medium',
  'attribution_utm_campaign',
  'acknowledged_at',
].join(', ');

// ── Helpers ───────────────────────────────────────────────────────────────────

function isRateLimited(label) {
  const now  = Date.now();
  const hits = (_rateMap.get(label) ?? []).filter(t => t > now - RATE_LIMIT_WINDOW);
  _rateMap.set(label, [...hits, now]);
  return hits.length >= RATE_LIMIT_MAX;
}

function authenticateAgent(req) {
  const header = req.headers['authorization'] ?? '';
  if (!header.startsWith('Bearer ')) return null;
  const token = process.env.AGENT_INTAKE_TOKEN ?? '';
  if (!token || header.slice(7) !== token) return null;
  return 'agent';
}

function decodeCursor(raw) {
  if (!raw) return null;
  try {
    const parsed = JSON.parse(Buffer.from(raw, 'base64').toString('utf8'));
    if (typeof parsed.seq !== 'string' || !/^\d+$/.test(parsed.seq)) return null;
    return { seq: BigInt(parsed.seq) };
  } catch { return null; }
}

function encodeCursor(seq) {
  return Buffer.from(JSON.stringify({ seq: seq.toString() })).toString('base64');
}

function makeReference(sid) {
  return `MA-ENQ-${sid.replace(/-/g, '').slice(0, 8).toUpperCase()}`;
}

function checkRestricted(row) {
  return row.operational_queue === 'HUMAN_REVIEW'
    || (row.safety_flag != null && row.safety_flag !== '')
    || row.professional_review_required === true;
}

function buildAnswers(row, branchMap) {
  const answers = [];

  if (row.form_variant === 'guided') {
    for (const q of GUIDED_QUESTIONS) {
      const raw = row[q.id];
      let answer;
      if (q.id === 'safe_email' || q.id === 'safe_voicemail' || q.id === 'safe_phone') {
        answer = raw === true ? 'Yes' : raw === false ? 'No' : null;
      } else if (VALUE_LABELS[q.id]) {
        answer = raw != null ? (VALUE_LABELS[q.id][raw] ?? raw) : null;
      } else {
        answer = raw != null ? String(raw) : null;
      }
      answers.push({ question_id: q.id, question_label: q.label, answer });
    }
  }

  for (const q of BRANCH_QUESTIONS) {
    answers.push({ question_id: q.id, question_label: q.label, answer: branchMap.get(q.id) ?? null });
  }

  return answers;
}

function buildFullItem(row, contact, branchMap) {
  const restricted = checkRestricted(row);
  return {
    submission_id:       row.submission_id,
    reference:           makeReference(row.submission_id),
    submitted_at:        row.submitted_at,
    operational_queue:   restricted ? 'HUMAN_REVIEW' : row.operational_queue,
    restricted,
    matter_category:     row.matter_category ?? null,
    timing:              row.timing ?? null,
    delivery_preference: row.delivery_preference ?? null,
    contact: {
      name:                   contact?.name ?? null,
      email:                  contact?.email ?? null,
      phone:                  contact?.phone ?? null,
      preferred_contact_time: row.preferred_contact_time ?? null,
      safe_email:             row.safe_email ?? null,
      safe_phone:             row.safe_phone ?? null,
      safe_voicemail:         row.safe_voicemail ?? null,
    },
    location: {
      city:  row.city ?? null,
      state: row.state ?? null,
    },
    answers:  buildAnswers(row, branchMap),
    message:  contact?.message ?? null,
    source: {
      landing_page: row.attribution_landing ?? null,
      utm_source:   row.attribution_utm_source ?? null,
      utm_medium:   row.attribution_utm_medium ?? null,
      utm_campaign: row.attribution_utm_campaign ?? null,
      form_version: row.form_variant === 'guided'
        ? `guided-${row.schema_version ?? '1.0'}`
        : 'quick',
    },
    formspree_notified: row.formspree_notified ?? false,
    acknowledged_at:    row.acknowledged_at ?? null,
  };
}

function buildDefaultItem(row) {
  const restricted = checkRestricted(row);
  if (restricted) {
    return {
      submission_id:     row.submission_id,
      reference:         makeReference(row.submission_id),
      operational_queue: 'HUMAN_REVIEW',
      restricted:        true,
      submitted_at:      row.submitted_at,
    };
  }
  return {
    submission_id:           row.submission_id,
    reference:               makeReference(row.submission_id),
    operational_queue:       row.operational_queue,
    matter_category:         row.matter_category,
    timing:                  row.timing,
    delivery_preference:     row.delivery_preference,
    safe_email:              row.safe_email,
    safe_voicemail:          row.safe_voicemail,
    safe_phone:              row.safe_phone,
    preferred_contact_time:  row.preferred_contact_time,
    formspree_notified:      row.formspree_notified,
    notification_attempts:   row.notification_attempts,
    notification_last_error: row.notification_last_error,
    tags:                    row.tags,
    submitted_at:            row.submitted_at,
    acknowledged_at:         row.acknowledged_at ?? null,
  };
}

async function fetchDetailData(submissionIds) {
  if (!submissionIds.length) return { contacts: new Map(), branches: new Map() };

  const [cr, br] = await Promise.all([
    sql.query(
      'SELECT enquiry_submission_id, name, email, phone, message FROM enquiry_contacts WHERE enquiry_submission_id = ANY($1::uuid[])',
      [submissionIds]
    ),
    sql.query(
      'SELECT enquiry_submission_id, answer_key, answer_value FROM enquiry_branch_answers WHERE enquiry_submission_id = ANY($1::uuid[]) ORDER BY enquiry_submission_id, id ASC',
      [submissionIds]
    ),
  ]);

  const contacts = new Map();
  for (const r of cr.rows) contacts.set(r.enquiry_submission_id, r);

  const branches = new Map();
  for (const r of br.rows) {
    if (!branches.has(r.enquiry_submission_id)) branches.set(r.enquiry_submission_id, new Map());
    branches.get(r.enquiry_submission_id).set(r.answer_key, r.answer_value);
  }

  return { contacts, branches };
}

// ── Main handler ───────────────────────────────────────────────────────────────

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });
  if (!authenticateAgent(req)) return res.status(401).json({ error: 'Unauthorised' });
  if (isRateLimited('agent')) return res.status(429).json({ error: 'Rate limit exceeded — 60 requests per hour.' });

  const isFull   = req.query?.detail === 'full';
  const singleId = req.query?.id ?? null;
  const limit    = Math.min(Math.max(parseInt(req.query?.limit ?? '20', 10), 1), 50);
  const cursor   = decodeCursor(req.query?.cursor ?? null);
  const ip       = String(req.headers['x-forwarded-for']?.split(',')[0]?.trim() ?? 'unknown').slice(0, 45);

  // ── Single-record mode ─────────────────────────────────────────────────────
  if (singleId) {
    if (!/^[0-9a-f-]{36}$/.test(singleId)) {
      return res.status(400).json({ error: 'Invalid id format.' });
    }

    let rows;
    try {
      rows = await sql.query(`SELECT ${SELECT_COLS} FROM enquiries WHERE submission_id = $1::uuid LIMIT 1`, [singleId]);
    } catch {
      return res.status(503).json({ error: 'Database temporarily unavailable. Retry shortly.' });
    }

    if (!rows.rows.length) return res.status(404).json({ error: 'Not found.' });

    const row = rows.rows[0];
    let item;

    if (isFull) {
      let contacts, branches;
      try {
        ({ contacts, branches } = await fetchDetailData([row.submission_id]));
      } catch {
        return res.status(503).json({ error: 'Database temporarily unavailable. Retry shortly.' });
      }
      item = buildFullItem(row, contacts.get(row.submission_id), branches.get(row.submission_id) ?? new Map());
      sql.query(
        "INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor, reason) VALUES ($1::uuid, 'AGENT_INTAKE_FULL_ACCESS', 'grokbot', $2)",
        [row.submission_id, `single-record ip=${ip}`]
      ).catch(() => {});
    } else {
      item = buildDefaultItem(row);
    }

    return res.status(200).json({ item });
  }

  // ── List mode ──────────────────────────────────────────────────────────────
  let rows;
  try {
    if (cursor) {
      rows = await sql.query(
        `SELECT ${SELECT_COLS} FROM enquiries WHERE id > $1::bigint ORDER BY id ASC LIMIT $2`,
        [cursor.seq.toString(), limit]
      );
    } else {
      const since = new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString();
      rows = await sql.query(
        `SELECT ${SELECT_COLS} FROM enquiries WHERE submitted_at >= $1::timestamptz ORDER BY id ASC LIMIT $2`,
        [since, limit]
      );
    }
  } catch {
    return res.status(503).json({ error: 'Database temporarily unavailable. Retry shortly.' });
  }

  const dbRows      = rows.rows;
  const cursorLabel = cursor ? `seq=${cursor.seq}` : 'last24h';
  let items;
  let restrictedCount = 0;

  if (isFull) {
    let contacts = new Map(), branches = new Map();
    try {
      ({ contacts, branches } = await fetchDetailData(dbRows.map(r => r.submission_id)));
    } catch {
      return res.status(503).json({ error: 'Database temporarily unavailable. Retry shortly.' });
    }

    items = dbRows.map(row => {
      const item = buildFullItem(row, contacts.get(row.submission_id), branches.get(row.submission_id) ?? new Map());
      if (item.restricted) restrictedCount++;
      return item;
    });

    sql.query(
      "INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor, reason) VALUES (NULL, 'AGENT_INTAKE_FULL_ACCESS', 'grokbot', $1)",
      [`cursor=${cursorLabel} rows=${dbRows.length} ip=${ip}`]
    ).catch(() => {});
  } else {
    items = dbRows.map(row => {
      const item = buildDefaultItem(row);
      if (item.restricted) restrictedCount++;
      return item;
    });

    sql.query(
      "INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor, reason) VALUES (NULL, 'AGENT_INTAKE_ACCESS', 'grokbot', $1)",
      [`cursor=${cursorLabel} rows=${dbRows.length}`]
    ).catch(() => {});
  }

  const lastRow = dbRows[dbRows.length - 1];
  return res.status(200).json({
    items,
    next_cursor:      lastRow ? encodeCursor(BigInt(lastRow.id)) : null,
    restricted_count: restrictedCount,
    count:            items.length,
  });
}
