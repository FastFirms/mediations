/**
 * GET  /api/admin?view=list
 * GET  /api/admin?view=detail&matter_id=MA-2026-00001
 * PATCH /api/admin  { matter_id, status, notes }
 *
 * Protected by Authorization: Bearer <ADMIN_SECRET>.
 * Never returns financial data to unauthenticated callers.
 * Financial assessment data (income_band, assets, contributions) is
 * returned only to authenticated admins via this endpoint.
 */

import { sql } from '@vercel/postgres';

const ALLOWED_STATUSES = [
  'NEW', 'AUTO_ELIGIBLE', 'REVIEW_REQUIRED', 'STANDARD_FEE',
  'APPROVED', 'DECLINED', 'WAITLISTED', 'BOOKED', 'COMPLETED',
];

function authOk(req) {
  const header = req.headers['authorization'] ?? '';
  const secret = process.env.ADMIN_SECRET ?? '';
  if (!secret) return false; // env var not set — deny all
  return header === `Bearer ${secret}`;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');

  if (!authOk(req)) {
    return res.status(401).json({ error: 'Unauthorised' });
  }

  // ── LIST ──────────────────────────────────────────────────────────────────
  if (req.method === 'GET') {
    const view = req.query?.view ?? 'list';

    if (view === 'list') {
      const { rows } = await sql`
        SELECT
          m.matter_id,
          m.status,
          m.matter_type,
          m.created_at,
          app.party_a_name,
          app.party_a_email,
          app.submitted_at,
          app.notification_sent_at,
          app.notification_error,
          a.result_type,
          a.review_flags,
          a.calculated_band,
          a.calculated_contribution_ex_gst
        FROM access_matters m
        LEFT JOIN access_applications app ON app.matter_id = m.matter_id
        LEFT JOIN access_assessments  a   ON a.matter_id  = m.matter_id
                                          AND a.participant_role = 'party_a'
        ORDER BY m.created_at DESC
        LIMIT 200;
      `;
      return res.status(200).json({ rows });
    }

    if (view === 'detail') {
      const matterId = String(req.query?.matter_id ?? '').trim();
      if (!matterId) return res.status(400).json({ error: 'matter_id required' });

      const [matterRes, assessRes, appRes, auditRes] = await Promise.all([
        sql`SELECT * FROM access_matters WHERE matter_id = ${matterId};`,
        sql`SELECT * FROM access_assessments WHERE matter_id = ${matterId};`,
        sql`SELECT * FROM access_applications WHERE matter_id = ${matterId};`,
        sql`
          SELECT action, actor, created_at, new_value
          FROM access_audit_log
          WHERE matter_id = ${matterId}
          ORDER BY created_at ASC;
        `,
      ]);

      if (!matterRes.rows.length) return res.status(404).json({ error: 'Not found' });

      return res.status(200).json({
        matter:      matterRes.rows[0],
        assessments: assessRes.rows,
        application: appRes.rows[0] ?? null,
        audit_log:   auditRes.rows,
      });
    }

    return res.status(400).json({ error: 'Unknown view' });
  }

  // ── UPDATE STATUS ─────────────────────────────────────────────────────────
  if (req.method === 'PATCH') {
    const { matter_id, status, notes } = req.body ?? {};
    if (!matter_id) return res.status(400).json({ error: 'matter_id required' });
    if (!ALLOWED_STATUSES.includes(status))
      return res.status(400).json({ error: `status must be one of: ${ALLOWED_STATUSES.join(', ')}` });

    await sql`
      UPDATE access_matters SET status = ${status}, updated_at = now()
      WHERE matter_id = ${matter_id};
    `;

    await sql`
      INSERT INTO access_audit_log (matter_id, action, actor, new_value)
      VALUES (
        ${matter_id}, 'STATUS_UPDATED', 'admin',
        ${JSON.stringify({ status, notes: notes ?? null })}
      );
    `;

    return res.status(200).json({ ok: true, matter_id, status });
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
