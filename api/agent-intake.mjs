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
 *   cursor  — opaque base64 token from a previous next_cursor response.
 *             Omit to get the last 24 hours of records.
 *   limit   — max 50, default 20
 *
 * Response:
 *   { items: [...], next_cursor: <string> | null, restricted_count: <n>, count: <n> }
 *
 * Items (non-restricted):
 *   submission_id, reference, operational_queue, matter_category,
 *   timing, delivery_preference, safe_email, safe_voicemail, safe_phone,
 *   preferred_contact_time, formspree_notified, notification_attempts,
 *   notification_last_error, tags, submitted_at
 *
 * Items (HUMAN_REVIEW or safety-flagged):
 *   submission_id, reference, operational_queue: "HUMAN_REVIEW",
 *   restricted: true, submitted_at
 *   — no contact detail, no category, no timing
 *
 * Cursor format: base64-encoded JSON { t: <ISO timestamp>, id: <UUID> }
 * Stable composite (submitted_at, submission_id) comparison prevents skipping
 * enquiries when multiple records share the same timestamp.
 *
 * NEVER returns: name, email, phone, message, safety_flag detail, free text,
 *                contact details, branch answers, or IP addresses.
 */

import { sql } from '@vercel/postgres';

const RATE_LIMIT_WINDOW = 60 * 60 * 1000; // 1 hour
const RATE_LIMIT_MAX    = 60;
const _rateMap          = new Map();

const NIL_UUID = '00000000-0000-0000-0000-000000000000';

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

// Decode an opaque base64 cursor into { t: ISO, id: UUID }.
// Returns null if the cursor is absent or malformed.
function decodeCursor(raw) {
  if (!raw) return null;
  try {
    const json = Buffer.from(raw, 'base64').toString('utf8');
    const parsed = JSON.parse(json);
    if (typeof parsed.t !== 'string' || typeof parsed.id !== 'string') return null;
    const ts = new Date(parsed.t);
    if (isNaN(ts.getTime())) return null;
    return { t: ts.toISOString(), id: parsed.id };
  } catch {
    return null;
  }
}

// Encode { t: ISO, id: UUID } into an opaque base64 cursor string.
function encodeCursor(t, id) {
  return Buffer.from(JSON.stringify({ t, id })).toString('base64');
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

  const limit = Math.min(Math.max(parseInt(req.query?.limit ?? '20', 10), 1), 50);
  const cursor = decodeCursor(req.query?.cursor ?? null);

  let rows;
  try {
    if (cursor) {
      // Stable composite cursor: (submitted_at, submission_id) > (cursor.t, cursor.id)
      // Postgres tuple comparison is equivalent to: submitted_at > t OR (submitted_at = t AND submission_id::text > id)
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
        WHERE (submitted_at, submission_id::text) > (${cursor.t}::timestamptz, ${cursor.id})
        ORDER BY submitted_at ASC, submission_id ASC
        LIMIT ${limit}
      `;
    } else {
      // No cursor: return last 24 hours, anchored at the nil UUID sentinel
      const since = new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString();
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
        WHERE submitted_at >= ${since}::timestamptz
        ORDER BY submitted_at ASC, submission_id ASC
        LIMIT ${limit}
      `;
    }
  } catch (err) {
    return res.status(503).json({ error: 'Database temporarily unavailable. Retry shortly.' });
  }

  const cursorLabel = cursor ? `t=${cursor.t},id=${cursor.id}` : 'last24h';
  sql`
    INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor, reason)
    VALUES (NULL, 'AGENT_INTAKE_ACCESS', 'grokbot', ${`cursor=${cursorLabel} rows=${rows.rows.length}`})
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

  const lastItem = rows.rows[rows.rows.length - 1];
  const nextCursor = lastItem
    ? encodeCursor(new Date(lastItem.submitted_at).toISOString(), lastItem.submission_id)
    : null;

  return res.status(200).json({
    items,
    next_cursor:      nextCursor,
    restricted_count: restrictedCount,
    count:            items.length,
  });
}
