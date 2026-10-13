/**
 * GET  /api/lead-ack?id=<uuid>&t=<token>  — show confirm page (no DB write)
 * POST /api/lead-ack  (body: id, t)        — record receipt
 *
 * MA-OPS-003: Farley receipt acknowledgement.
 * Grok Bot embeds the URL in every lead email. Farley clicks it to log when
 * he picked the lead up. A GET shows a confirm page without writing anything —
 * this protects against Outlook Safe Links, Gmail, Mimecast and other scanners
 * that open links before the recipient does. A POST from the confirm button
 * records the timestamp atomically.
 *
 * Token: base64url(HMAC-SHA256(LEAD_ACK_SECRET, "lead-ack:v1:" + submission_id))
 *   - Input string: exactly "lead-ack:v1:" + the UUID submission_id
 *   - Encoding: standard base64url, trailing "=" stripped
 *   - Verification: crypto.timingSafeEqual (constant-time)
 *   - Same computation in Python (for Grok Bot):
 *       import hmac, hashlib, base64
 *       mac = hmac.new(secret.encode(), f"lead-ack:v1:{sid}".encode(), hashlib.sha256).digest()
 *       token = base64.urlsafe_b64encode(mac).rstrip(b"=").decode()
 *   - URL: https://www.mediationsaustralia.com.au/api/lead-ack?id=<uuid>&t=<token>
 *
 * Security:
 *   - Unknown id and bad token return 403 with the same generic page.
 *   - Constant-time comparison prevents timing oracle attacks.
 *   - HMAC token serves as CSRF protection (no cookies needed).
 *   - No PII in rendered HTML — only MA-ENQ reference and timestamps.
 *   - Cache-Control: no-store, X-Robots-Tag: noindex, Referrer-Policy: no-referrer.
 *   - Rate limit: 60 req/hour per IP.
 */

import { createHmac, timingSafeEqual } from 'crypto';
import { sql } from '@vercel/postgres';

const RATE_LIMIT_WINDOW = 60 * 60 * 1000;
const RATE_LIMIT_MAX    = 60;
const _rateMap          = new Map();

function isRateLimited(key) {
  const now  = Date.now();
  const hits = (_rateMap.get(key) ?? []).filter(t => t > now - RATE_LIMIT_WINDOW);
  _rateMap.set(key, [...hits, now]);
  return hits.length >= RATE_LIMIT_MAX;
}

function computeToken(secret, submissionId) {
  return createHmac('sha256', secret)
    .update(`lead-ack:v1:${submissionId}`)
    .digest('base64url')
    .replace(/=+$/, '');
}

function verifyToken(secret, submissionId, provided) {
  if (!provided || typeof provided !== 'string') return false;
  const expected = computeToken(secret, submissionId);
  // Pad to same length before timingSafeEqual; also check actual lengths match
  const a = Buffer.from(provided.padEnd(expected.length, '\0').slice(0, expected.length));
  const b = Buffer.from(expected);
  return a.length === b.length && timingSafeEqual(a, b) && provided.length === expected.length;
}

function makeReference(sid) {
  return `MA-ENQ-${sid.replace(/-/g, '').slice(0, 8).toUpperCase()}`;
}

function formatAEDT(date) {
  return new Intl.DateTimeFormat('en-AU', {
    timeZone:     'Australia/Sydney',
    weekday:      'short',
    day:          'numeric',
    month:        'short',
    year:         'numeric',
    hour:         'numeric',
    minute:       '2-digit',
    hour12:       true,
    timeZoneName: 'short',
  }).format(new Date(date));
}

// ── HTML pages ─────────────────────────────────────────────────────────────────

const CSS = `
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;font-size:16px;line-height:1.6;background:#f5f4f1;color:#1a1a1a;min-height:100vh}
.hdr{background:#175233;padding:20px 24px}
.hdr h1{font-family:'PT Serif',serif;color:#fff;font-size:1.2rem;font-weight:700}
.hdr p{color:#a8c4b5;font-size:.78rem;margin-top:2px}
.main{max-width:480px;margin:48px auto;padding:0 16px}
.card{background:#fff;border-radius:8px;padding:32px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
h2{font-family:'PT Serif',serif;font-size:1.3rem;font-weight:700;color:#175233;margin-bottom:12px}
p{color:#444;margin-bottom:14px}
.ref{font-family:monospace;font-size:.88rem;background:#f0ede8;padding:2px 8px;border-radius:4px;color:#175233}
.btn{display:inline-block;background:#175233;color:#fff;border:none;padding:12px 28px;border-radius:6px;font-family:'DM Sans',sans-serif;font-size:1rem;font-weight:500;cursor:pointer;margin-top:8px}
.btn:hover{background:#1f6b42}
.tstamp{font-size:.95rem;color:#175233;font-weight:500}
`.trim();

const FONTS = `<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=PT+Serif:wght@400;700&family=DM+Sans:wght@400;500&display=swap">`;

function shell(body) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Mediations Australia</title>${FONTS}<style>${CSS}</style></head><body><header class="hdr"><h1>Mediations Australia</h1><p>Intake management</p></header><main class="main">${body}</main></body></html>`;
}

function pageConfirm(ref, id, token) {
  return shell(`<div class="card"><h2>Confirm receipt</h2><p>Enquiry <span class="ref">${ref}</span> has been assigned to you.</p><p>Click below to confirm you have received and reviewed this lead.</p><form method="POST" action="/api/lead-ack"><input type="hidden" name="id" value="${id}"><input type="hidden" name="t" value="${token}"><button class="btn" type="submit">Confirm receipt</button></form></div>`);
}

function pageAlreadyAcked(ref, ackedAt) {
  return shell(`<div class="card"><h2>Already logged</h2><p>Enquiry <span class="ref">${ref}</span></p><p>Receipt was previously logged at</p><p class="tstamp">${formatAEDT(ackedAt)}</p></div>`);
}

function pageThanks(ref, ackedAt) {
  return shell(`<div class="card"><h2>Thanks Farley</h2><p>Enquiry <span class="ref">${ref}</span></p><p>Receipt logged at</p><p class="tstamp">${formatAEDT(ackedAt)}</p></div>`);
}

function pageInvalid() {
  return shell(`<div class="card"><h2>Link not valid</h2><p>This link isn't valid or has expired. Contact the intake team if you need assistance.</p></div>`);
}

// ── Handler ────────────────────────────────────────────────────────────────────

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex');
  res.setHeader('Referrer-Policy', 'no-referrer');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  if (!['GET', 'POST'].includes(req.method)) {
    res.setHeader('Allow', 'GET, POST');
    return res.status(405).end();
  }

  const ip = String(req.headers['x-forwarded-for']?.split(',')[0]?.trim() ?? 'unknown').slice(0, 45);
  if (isRateLimited(ip)) return res.status(429).end();

  const secret = process.env.LEAD_ACK_SECRET ?? '';
  if (!secret) return res.status(503).end();

  // Parse id and t from query (GET) or parsed form body (POST)
  let id, token;
  if (req.method === 'GET') {
    id    = String(req.query?.id ?? '');
    token = String(req.query?.t  ?? '');
  } else {
    const body = typeof req.body === 'object' && req.body !== null ? req.body : {};
    id    = String(body.id ?? '');
    token = String(body.t  ?? '');
  }

  const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

  // Look up enquiry — always run even if UUID is invalid, so timing is consistent
  let row = null;
  if (UUID_RE.test(id)) {
    try {
      const r = await sql.query(
        'SELECT submission_id, acknowledged_at FROM enquiries WHERE submission_id = $1::uuid LIMIT 1',
        [id]
      );
      row = r.rows[0] ?? null;
    } catch {
      return res.status(503).end();
    }
  }

  // Token verification — always run to prevent timing attacks
  const tokenOk = row !== null && verifyToken(secret, id, token);

  if (!tokenOk) {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    return res.status(403).send(pageInvalid());
  }

  const ref = makeReference(id);

  // ── GET: show confirm page or "already acked" — no DB write ───────────────
  if (req.method === 'GET') {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    return res.status(200).send(
      row.acknowledged_at ? pageAlreadyAcked(ref, row.acknowledged_at) : pageConfirm(ref, id, token)
    );
  }

  // ── POST: record receipt atomically ───────────────────────────────────────
  const ua = String(req.headers['user-agent'] ?? '').slice(0, 200);
  let finalAckedAt;

  try {
    await sql.query(
      `UPDATE enquiries
         SET acknowledged_at = now(), acknowledged_via = 'email_button', ack_user_agent = $2
       WHERE submission_id = $1::uuid AND acknowledged_at IS NULL`,
      [id, ua]
    );
    const r = await sql.query(
      'SELECT acknowledged_at FROM enquiries WHERE submission_id = $1::uuid',
      [id]
    );
    finalAckedAt = r.rows[0]?.acknowledged_at;
  } catch {
    return res.status(503).end();
  }

  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  return res.status(200).send(pageThanks(ref, finalAckedAt));
}
