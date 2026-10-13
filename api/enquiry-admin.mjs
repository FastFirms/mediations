/**
 * GET  /api/enquiry-admin?view=list[&queue=HUMAN_REVIEW][&limit=50][&offset=0]
 * GET  /api/enquiry-admin?view=detail&id=<submission_id>
 * PATCH /api/enquiry-admin  { submission_id, queue, notes }
 *
 * Authentication: per-user Bearer API keys via ADMIN_USERS env var (JSON array):
 *   [{"name":"dan","key":"<key>","role":"admin"},{"name":"reception","key":"<key>","role":"viewer"}]
 *
 * Roles:
 *   admin  — GET list/detail + PATCH queue override
 *   viewer — GET list/detail only
 *
 * Backward compat: if ADMIN_USERS is not set, falls back to ADMIN_SECRET with role=admin.
 *
 * PATCH records the authenticated user's name in the audit log — not a generic 'admin'.
 * Keys are server-side only; never exposed to client-side code or Formspree.
 * Contact details (email, phone, message) are never included in Formspree payloads.
 */

import { sql } from '@vercel/postgres';

const ALLOWED_QUEUES = [
  'HUMAN_REVIEW','ACCESS_REVIEW','PUBLIC_SERVICE_INFORMATION',
  'PREPARATION_NURTURE','PRIORITY_INTAKE','ENGAGE_OTHER_PARTY','GENERAL_INTAKE',
];

function authenticateAdmin(req) {
  const header = req.headers['authorization'] ?? '';
  if (!header.startsWith('Bearer ')) return null;
  const provided = header.slice(7);

  // Per-user keys (preferred)
  const usersJson = process.env.ADMIN_USERS ?? '';
  if (usersJson) {
    try {
      const users = JSON.parse(usersJson);
      for (const u of users) {
        if (u.key && u.key === provided) {
          return { name: u.name ?? 'unknown', role: u.role ?? 'viewer' };
        }
      }
    } catch { /* malformed ADMIN_USERS — fall through */ }
  }

  // Backward compat: single shared secret
  const secret = process.env.ADMIN_SECRET ?? '';
  if (secret && provided === secret) {
    return { name: 'admin', role: 'admin' };
  }

  return null;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  const user = authenticateAdmin(req);
  if (!user) {
    return res.status(401).json({ error: 'Unauthorised' });
  }

  // ── LIST ──────────────────────────────────────────────────────────────────
  if (req.method === 'GET') {
    const view   = req.query?.view ?? 'list';
    const limit  = Math.min(parseInt(req.query?.limit  ?? '50',  10), 200);
    const offset = Math.max(parseInt(req.query?.offset ?? '0',   10), 0);

    if (view === 'list') {
      const queue = req.query?.queue ?? null;
      let rows;
      if (queue && ALLOWED_QUEUES.includes(queue)) {
        rows = await sql`
          SELECT e.submission_id, e.operational_queue, e.professional_review_required,
                 e.matter_category, e.stage, e.delivery_preference, e.timing,
                 e.safe_email, e.safe_voicemail, e.safe_phone, e.preferred_contact_time,
                 e.submitted_at, e.review_reasons, e.tags,
                 c.name, c.email, c.phone
          FROM enquiries e
          LEFT JOIN enquiry_contacts c ON c.enquiry_submission_id = e.submission_id
          WHERE e.operational_queue = ${queue}
          ORDER BY e.submitted_at DESC
          LIMIT ${limit} OFFSET ${offset}
        `;
      } else {
        rows = await sql`
          SELECT e.submission_id, e.operational_queue, e.professional_review_required,
                 e.matter_category, e.stage, e.delivery_preference, e.timing,
                 e.safe_email, e.safe_voicemail, e.safe_phone, e.preferred_contact_time,
                 e.submitted_at, e.review_reasons, e.tags,
                 c.name, c.email, c.phone
          FROM enquiries e
          LEFT JOIN enquiry_contacts c ON c.enquiry_submission_id = e.submission_id
          ORDER BY e.submitted_at DESC
          LIMIT ${limit} OFFSET ${offset}
        `;
      }
      return res.status(200).json({ rows: rows.rows, limit, offset });
    }

    if (view === 'detail') {
      const id = String(req.query?.id ?? '').trim();
      if (!id) return res.status(400).json({ error: 'id required' });

      const [eRes, cRes, bRes, aRes] = await Promise.all([
        sql`SELECT * FROM enquiries WHERE submission_id = ${id}`,
        sql`SELECT * FROM enquiry_contacts WHERE enquiry_submission_id = ${id}`,
        sql`SELECT answer_key, answer_value FROM enquiry_branch_answers WHERE enquiry_submission_id = ${id}`,
        sql`SELECT event_type, actor, reason, created_at FROM enquiry_audit_log WHERE enquiry_submission_id = ${id} ORDER BY created_at ASC`,
      ]);

      if (!eRes.rows.length) return res.status(404).json({ error: 'Not found' });

      return res.status(200).json({
        enquiry:        eRes.rows[0],
        contact:        cRes.rows[0] ?? null,
        branch_answers: bRes.rows,
        audit_log:      aRes.rows,
      });
    }

    return res.status(400).json({ error: 'Unknown view' });
  }

  // ── MANUAL QUEUE OVERRIDE (admin role only) ───────────────────────────────
  if (req.method === 'PATCH') {
    if (user.role !== 'admin') {
      return res.status(403).json({ error: 'Forbidden — admin role required for queue overrides' });
    }
    const { submission_id, queue, notes } = req.body ?? {};
    if (!submission_id) return res.status(400).json({ error: 'submission_id required' });
    if (!ALLOWED_QUEUES.includes(queue)) {
      return res.status(400).json({ error: `queue must be one of: ${ALLOWED_QUEUES.join(', ')}` });
    }

    await sql`
      UPDATE enquiries SET operational_queue = ${queue}
      WHERE submission_id = ${submission_id}
    `;

    await sql`
      INSERT INTO enquiry_audit_log (enquiry_submission_id, event_type, actor, reason)
      VALUES (${submission_id}, 'QUEUE_OVERRIDE', ${user.name}, ${notes ?? null})
    `;

    return res.status(200).json({ ok: true, submission_id, queue, overridden_by: user.name });
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
