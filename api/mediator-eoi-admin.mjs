/**
 * GET   /api/mediator-eoi-admin?view=list[&status=NEW][&notification=FAILED][&limit=50][&offset=0]
 * GET   /api/mediator-eoi-admin?view=detail&id=<submission_id>
 * PATCH /api/mediator-eoi-admin  { submission_id, review_status?, internal_notes?, assigned_reviewer? }
 *
 * Same Bearer auth as /api/enquiry-admin (ADMIN_USERS / ADMIN_SECRET).
 * admin: read + PATCH; viewer: read only. Status changes are always manual —
 * nothing here (or elsewhere) auto-approves a mediator.
 */

import { sql } from '@vercel/postgres';

const STATUSES = ['NEW','IN_REVIEW','MORE_INFORMATION_REQUESTED','DISCUSSION_INVITED','APPROVED_FOR_ONBOARDING','NOT_PROCEEDING'];

const _rate = new Map();
function limited(name) {
  const now = Date.now();
  const hits = (_rate.get(name) ?? []).filter(t => t > now - 60_000);
  _rate.set(name, [...hits, now]);
  return hits.length >= 30;
}

function authenticate(req) {
  const h = req.headers['authorization'] ?? '';
  if (!h.startsWith('Bearer ')) return null;
  const key = h.slice(7);
  if (process.env.ADMIN_USERS) {
    try {
      const u = JSON.parse(process.env.ADMIN_USERS).find(x => x.key && x.key === key);
      if (u) return { name: u.name ?? 'unknown', role: u.role ?? 'viewer' };
    } catch { /* malformed — fall through */ }
  }
  if (process.env.ADMIN_SECRET && key === process.env.ADMIN_SECRET) return { name: 'admin', role: 'admin' };
  return null;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  const user = authenticate(req);
  if (!user) return res.status(401).json({ error: 'Unauthorised' });
  if (limited(user.name)) return res.status(429).json({ error: 'Too many requests' });

  try {
    if (req.method === 'GET') {
      const q = req.query ?? {};
      if (q.view === 'detail') {
        if (!/^[0-9a-f-]{36}$/i.test(q.id ?? '')) return res.status(400).json({ error: 'Invalid id' });
        const r = await sql`SELECT * FROM mediator_eois WHERE submission_id = ${q.id}`;
        if (!r.rows.length) return res.status(404).json({ error: 'Not found' });
        await sql`INSERT INTO mediator_eoi_audit_log (submission_id, event_type, actor) VALUES (${q.id}, 'VIEWED', ${user.name})`;
        return res.status(200).json(r.rows[0]);
      }
      const status = STATUSES.includes(q.status) ? q.status : null;
      const notif = ['PENDING','SENT','FAILED'].includes(q.notification) ? q.notification : null;
      const limit = Math.min(Math.max(parseInt(q.limit ?? '50', 10) || 50, 1), 200);
      const offset = Math.max(parseInt(q.offset ?? '0', 10) || 0, 0);
      const r = await sql`
        SELECT submission_id, submitted_at, name, state, city, experience_band, practice_areas,
               delivery_modes, review_status, assigned_reviewer, notification_status
        FROM mediator_eois
        WHERE (${status}::text IS NULL OR review_status = ${status})
          AND (${notif}::text IS NULL OR notification_status = ${notif})
        ORDER BY submitted_at DESC LIMIT ${limit} OFFSET ${offset}`;
      return res.status(200).json({ items: r.rows, limit, offset });
    }

    if (req.method === 'PATCH') {
      if (user.role !== 'admin') return res.status(403).json({ error: 'Read-only user' });
      const b = req.body ?? {};
      if (!/^[0-9a-f-]{36}$/i.test(b.submission_id ?? '')) return res.status(400).json({ error: 'Invalid submission_id' });
      if (b.review_status !== undefined && !STATUSES.includes(b.review_status)) return res.status(400).json({ error: 'Invalid review_status' });
      const notes = typeof b.internal_notes === 'string' ? b.internal_notes.slice(0, 4000) : null;
      const reviewer = typeof b.assigned_reviewer === 'string' ? b.assigned_reviewer.slice(0, 80) : null;
      const r = await sql`
        UPDATE mediator_eois SET
          review_status     = COALESCE(${b.review_status ?? null}, review_status),
          internal_notes    = COALESCE(${notes}, internal_notes),
          assigned_reviewer = COALESCE(${reviewer}, assigned_reviewer),
          reviewed_at       = NOW()
        WHERE submission_id = ${b.submission_id}
        RETURNING submission_id, review_status`;
      if (!r.rows.length) return res.status(404).json({ error: 'Not found' });
      await sql`INSERT INTO mediator_eoi_audit_log (submission_id, event_type, actor, detail)
                VALUES (${b.submission_id}, 'UPDATED', ${user.name}, ${b.review_status ?? null})`;
      return res.status(200).json(r.rows[0]);
    }

    return res.status(405).json({ error: 'Method not allowed' });
  } catch {
    return res.status(503).json({ error: 'Database unavailable' });
  }
}
