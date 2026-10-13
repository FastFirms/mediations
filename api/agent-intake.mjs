/**
 * GET /api/agent-intake
 *
 * Read-only feed of new enquiries for an authorised intake agent (GrokBot).
 * Returns non-restricted leads with minimal operational metadata.
 * HUMAN_REVIEW leads return reference + restricted-alert only — no detail.
 *
 * Auth: Authorization: Bearer <AGENT_INTAKE_TOKEN> (env var, server-side only)
 * Rate limit: 60 requests per hour per token.
 * All access is logged to enquiry_audit_log.
 *
 * Query params:
 *   cursor  — ISO timestamp; returns records submitted_at > cursor (exclusive)
 *             Omit to get the last 24 hours of records.
 *   limit   — max 50, default 20
 *
 * Response:
 *   { items: [...], next_cursor: <ISO> | null, restricted_count: <n> }
 *
 * Items (non-restricted):
 *   submission_id, reference, operational_queue, matter_category,
 *   timing, delivery_preference, safe_email, safe_voicemail, safe_phone,
 *   preferred_contact_time, formspree_notified, notification_attempts,
 *   notification_last_error, submitted_at, assigned_owner
 *
 * Items (HUMAN_REVIEW or safety-flagged):
 *   submission_id, reference, operational_queue: "HUMAN_REVIEW",
 *   restricted: true, submitted_at
 *   — no contact detail, no category, no timing
 *
 * NEVER returns: name, email, phone, message, safety_flag detail, free text,
 *                contact details, branch answers, or IP addresses.
 */

import { sql } from '@vercel/postgres';

const RATE_LIMIT_WINDOW = 60 * 60 * 1000; // 1 hour
const RATE_LIMIT_MAX    = 60;
const _rateMap          = new Map();

function isRateLimited(label) {
  const now  = Date.now();
  const hits = (_rateMap.get(label) ?? []).filter(t => t > now - RATE_LIMIT_WINDOW);
  _rateMap.set(label, [...hits, now]);
  return hits.length >= RATE_LIMIT_MAX;
}

function authenticateAgent(req) {
  const header = req.headers['authorization'] ?? '';
  if (!header.startsWith('Bearer ')) return null;
  const provided = header.slice(7);
  const token    = process.env.AGENT_INTAKE_TOKEN ?? '';
  if (!token || provided !== token) return null;
  return 'agent';
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Auth
  const agent = authenticateAgent(req);
  if (!agent) {
    return res.status(401).json({ error: 'Unauthorised' });
  }

  // Rate limit
  if (isRateLimited('agent')) {
    return res.status(429).json({ error: 'Rate limit exceeded — 60 requests per hour.' });
  }

  // Cursor and limit
  const rawCursor = req.query?.cursor ?? null;
  const cursor    = rawCursor && /^\d{4}-\d{2}-\d{2}T[\d:.Z+-]+$/.test(rawCursor)
    ? new Date(rawCursor).toISOString()
    : new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(); // default: last 24h
  const limit = Math.min(Math.max(parseInt(req.query?.limit ?? '20', 10), 1), 50);

  let rows;
  try {
    rows = await sql`
      SELECT
        submission_id,
        operational_queue,
        safety_flag,
        matter_category,
        timing,
        delivery_preference,
        safe_email,
        safe_voicemail,
        safe_phone,
        preferred_contact_time,
        formspree_notified,
        notification_attempts,
        notification_last_error,
        submitted_at,
        professional_review_required,
        review_reasons,
        tags
      FROM enquiries
      WHERE submitted_at > ${cursor}
      ORDER BY submitted_at ASC
      LIMIT ${limit}
    `;
  } catch (err) {
    return res.status(503).json({ error: 'Database temporarily unavailable. Retry shortly.' });
  }

  // Log access
  sql`
    INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor, reason)
    VALUES (NULL, 'AGENT_INTAKE_ACCESS', 'grokbot', ${'cursor=' + cursor + ' rows=' + rows.rows.length})
  `.catch(() => {});

  const items       = [];
  let restrictedCount = 0;

  for (const row of rows.rows) {
    const refShort = row.submission_id.replace(/-/g, '').slice(0, 8).toUpperCase();
    const reference = `MA-ENQ-${refShort}`;
    const isRestricted = row.operational_queue === 'HUMAN_REVIEW'
      || row.safety_flag === 'yes'
      || row.professional_review_required === true;

    if (isRestricted) {
      restrictedCount++;
      items.push({
        submission_id:     row.submission_id,
        reference,
        operational_queue: 'HUMAN_REVIEW',
        restricted:        true,
        submitted_at:      row.submitted_at,
      });
    } else {
      items.push({
        submission_id:           row.submission_id,
        reference,
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
      });
    }
  }

  const lastItem  = rows.rows[rows.rows.length - 1];
  const nextCursor = lastItem ? new Date(lastItem.submitted_at).toISOString() : null;

  return res.status(200).json({
    items,
    next_cursor:      nextCursor,
    restricted_count: restrictedCount,
    count:            items.length,
  });
}
