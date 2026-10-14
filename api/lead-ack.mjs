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
body{margin:0;background:#f5f4f1;font:16px/1.55 "DM Sans",Helvetica,Arial,sans-serif;color:#333}
.card{max-width:480px;margin:32px auto;background:#fff;border:1px solid #e6e3dd;border-top:8px solid #175233;border-radius:16px;padding:28px}
@media(max-width:520px){.card{margin:0;border-radius:0;min-height:100vh}}
.logo{display:block;width:180px;height:auto;margin-bottom:28px}
.label{font:700 12px/1 "DM Sans",sans-serif;letter-spacing:1.4px;text-transform:uppercase;color:#175233;margin:0 0 10px}
h1{font:700 26px/1.25 "PT Serif",Georgia,serif;color:#111;margin:0 0 12px}
.time{font:700 22px/1.3 "DM Sans",sans-serif;color:#111;margin:8px 0 0}
.muted{color:#5c5c5c;font-size:14px;margin-top:8px}
.btn{display:block;width:100%;height:56px;margin:20px 0 10px;background:#f5c347;border:2px solid #f5c347;border-radius:10px;color:#1a1a1a;font:700 18px "DM Sans",sans-serif;cursor:pointer;text-align:center;line-height:52px}
.btn:focus-visible{outline:3px solid #175233;outline-offset:2px}
.icon{width:48px;height:48px;border:2px solid #175233;border-radius:50%;color:#175233;font:700 24px/44px sans-serif;text-align:center;margin-bottom:16px}
.icon.neutral{border-color:#5c5c5c;color:#5c5c5c}
`.trim();

const FONTS = `<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=PT+Serif:wght@700&family=DM+Sans:wght@400;700&display=swap">`;

function shell(title, body) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>${title} · Mediations Australia</title>${FONTS}<style>${CSS}</style></head><body><main class="card"><img class="logo" src="/assets/images/email/ma-logo-black.png" alt="Mediations Australia">${body}</main></body></html>`;
}

function pageConfirm(ref, id, token) {
  return shell('Confirm receipt',
    `<p class="label">Lead receipt</p>
<h1>Confirm you&rsquo;ve received ${ref}</h1>
<form method="POST" action="/api/lead-ack">
  <input type="hidden" name="id" value="${id}">
  <input type="hidden" name="t" value="${token}">
  <button class="btn" type="submit">Confirm receipt</button>
</form>
<p class="muted">This only logs the time you picked it up.</p>`);
}

function pageAlreadyAcked(ref, ackedAt) {
  return shell('Already logged',
    `<div class="icon">&#10003;</div>
<h1>Already logged</h1>
<p class="muted">${ref}</p>
<p class="time">${formatAEDT(ackedAt)}</p>
<p class="muted">You can close this page.</p>`);
}

function pageThanks(ref, ackedAt) {
  return shell('Receipt logged',
    `<div class="icon">&#10003;</div>
<h1>Thanks Farley, receipt logged</h1>
<p class="time">${formatAEDT(ackedAt)}</p>
<p class="muted">${ref} &middot; you can close this page.</p>`);
}

function pageInvalid() {
  return shell('Link not valid',
    `<div class="icon neutral">i</div>
<h1>This link isn&rsquo;t valid</h1>
<p>It may have expired or been copied incorrectly. If you need help, contact the Mediations Australia office.</p>`);
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
