/**
 * POST /api/mediator-eoi
 *
 * Mediator Network expression of interest. Recruitment only — never routed
 * into client intake queues, Access Mediation or chatbot lead feeds.
 *
 * - Server-side validation with strict enums and length caps.
 * - Honeypot (_hp), IP rate limit, submission_id idempotency, and same-email
 *   24h duplicate guard.
 * - Record is saved in Neon BEFORE notifying; a failed notification marks
 *   notification_status = FAILED and is recoverable via /api/mediator-eoi-admin.
 * - No personal data in logs, URLs or error messages.
 */

import { sql } from '@vercel/postgres';

const FORMSPREE_ENDPOINT = process.env.FORMSPREE_EOI_ENDPOINT || 'https://formspree.io/f/xoeeerjo';
const FORM_VERSION       = '2026-10-v1';
const CONSENT_VERSION    = '2026-10-v1';
const RATE_WINDOW_MS     = 15 * 60 * 1000;
const RATE_MAX           = 5;
const DUP_EMAIL_WINDOW_MS = 24 * 60 * 60 * 1000;

export const ENUMS = {
  state:          ['NSW','VIC','QLD','WA','SA','TAS','ACT','NT'],
  practice_type:  ['independent_mediator','lawyer_mediator','fdr_practitioner','workplace_hr_mediator','other'],
  credential:     ['amdras','fdrp','other_credential','working_toward','prefer_to_explain'],
  experience:     ['under_2','2_5','6_10','11_plus'],
  practice_area:  ['family_parenting','property_financial','workplace_employment','commercial_business',
                   'estate_inheritance','elder_intergenerational','neighbourhood_strata_property','other_specialist'],
  delivery:       ['in_person','online','both'],
  venue:          ['own_venue','can_arrange','depends','not_applicable'],
  capacity:       ['available','limited','future','prefer_discuss'],
};

const EMAIL_RE = /^[^\s@<>()]{1,64}@[^\s@<>()]+\.[a-z]{2,}$/i;
const URL_RE   = /^https?:\/\/[^\s<>"]+\.[^\s<>"]+$/i;

function str(v) {
  if (typeof v !== 'string') return null;
  const t = v.trim();
  return t.length ? t : null;
}

export function validate(b) {
  const errs = {};
  const out = {};
  const req = (key, max, label) => {
    const v = str(b[key]);
    if (!v) errs[key] = `${label} is required.`;
    else if (v.length > max) errs[key] = `${label} must be ${max} characters or fewer.`;
    else out[key] = v;
  };
  const opt = (key, max, label) => {
    const v = str(b[key]);
    if (v && v.length > max) errs[key] = `${label} must be ${max} characters or fewer.`;
    else out[key] = v;
  };
  const oneOf = (key, list, label, required) => {
    const v = str(b[key]);
    if (!v) { if (required) errs[key] = `Please select ${label}.`; out[key] = null; return; }
    if (!list.includes(v)) errs[key] = `Please select a valid ${label}.`;
    else out[key] = v;
  };
  const manyOf = (key, list, label) => {
    const v = Array.isArray(b[key]) ? [...new Set(b[key].filter(x => typeof x === 'string'))] : [];
    if (!v.length) errs[key] = `Please select at least one ${label}.`;
    else if (v.some(x => !list.includes(x))) errs[key] = `Please select valid ${label} options.`;
    else out[key] = v;
  };

  req('name', 120, 'Full name');
  req('email', 254, 'Email');
  if (out.email && !EMAIL_RE.test(out.email)) errs.email = 'Please enter a valid email address.';
  req('phone', 30, 'Phone');
  if (out.phone && (out.phone.replace(/\D/g, '').length < 8 || /[^\d\s()+-]/.test(out.phone))) errs.phone = 'Please enter a valid phone number.';
  req('city', 100, 'City or suburb');
  oneOf('state', ENUMS.state, 'a state or territory', true);
  opt('website', 300, 'Website');
  if (out.website && !URL_RE.test(out.website)) errs.website = 'Please enter a full web address starting with https://';
  opt('organisation', 150, 'Practice or organisation');

  oneOf('practice_type', ENUMS.practice_type, 'role', false);
  manyOf('credential_types', ENUMS.credential, 'accreditation or registration');
  opt('credential_body', 150, 'Accrediting body');
  opt('credential_identifier', 80, 'Registration number');
  oneOf('experience_band', ENUMS.experience, 'your years of experience', true);
  manyOf('practice_areas', ENUMS.practice_area, 'practice area');
  opt('background', 500, 'Professional background');

  req('regions_served', 300, 'Regions or cities you service');
  oneOf('delivery_mode', ENUMS.delivery, 'how you deliver mediation', true);
  oneOf('venue_access', ENUMS.venue, 'venue access', false);
  oneOf('capacity_band', ENUMS.capacity, 'capacity', false);
  opt('languages', 150, 'Languages');
  opt('motivation', 500, 'Your answer');

  if (b.accuracy_confirmed !== true) errs.accuracy_confirmed = 'Please confirm your information is accurate.';
  if (b.privacy_acknowledged !== true) errs.privacy_acknowledged = 'Please acknowledge the Privacy Policy.';
  out.marketing_opt_in = b.marketing_opt_in === true;

  if (out.delivery_mode) {
    out.delivery_modes = out.delivery_mode === 'both' ? ['in_person', 'online'] : [out.delivery_mode];
  }
  return { errors: errs, data: out };
}

const refFor = id => `MA-EOI-${id.replace(/-/g, '').slice(0, 8).toUpperCase()}`;

const _mem = new Map();
function memLimited(ip) {
  const now = Date.now();
  const hits = (_mem.get(ip) ?? []).filter(t => t > now - RATE_WINDOW_MS);
  _mem.set(ip, [...hits, now]);
  return hits.length >= RATE_MAX;
}

async function rateLimited(ip) {
  try {
    const since = new Date(Date.now() - RATE_WINDOW_MS).toISOString();
    const r = await sql`SELECT COUNT(*) AS c FROM mediator_eoi_audit_log
                        WHERE event_type = 'SUBMIT_ATTEMPT' AND actor = ${ip} AND created_at > ${since}`;
    await sql`INSERT INTO mediator_eoi_audit_log (event_type, actor) VALUES ('SUBMIT_ATTEMPT', ${ip})`;
    return parseInt(r.rows[0]?.c ?? '0', 10) >= RATE_MAX;
  } catch {
    return memLimited(ip);
  }
}

async function notify(id, d) {
  const payload = {
    reference:       refFor(id),
    name:            d.name,
    state:           d.state,
    regions_served:  d.regions_served,
    experience_band: d.experience_band,
    practice_areas:  d.practice_areas.join(', '),
    delivery:        d.delivery_mode,
    _subject:        `Mediator Network EOI — ${refFor(id)}`,
  };
  let attempts = 0;
  for (let i = 0; i < 2; i++) {
    attempts++;
    try {
      const r = await fetch(FORMSPREE_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload),
      });
      if (r.ok) return { ok: true, attempts };
    } catch { /* retry */ }
    if (i === 0) await new Promise(res => setTimeout(res, 800));
  }
  return { ok: false, attempts };
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const b = (req.body && typeof req.body === 'object') ? req.body : {};
  if (JSON.stringify(b).length > 12000) return res.status(413).json({ error: 'Submission too large.' });

  if (typeof b._hp === 'string' && b._hp !== '') {
    return res.status(200).json({ ok: true, reference: 'MA-EOI-RECEIVED' });
  }

  const { errors, data } = validate(b);
  if (Object.keys(errors).length) return res.status(400).json({ error: 'Please check the highlighted fields.', fields: errors });

  const ip = String(req.headers['x-forwarded-for']?.split(',')[0]?.trim() ?? 'unknown').slice(0, 45);
  if (await rateLimited(ip)) {
    return res.status(429).json({ error: 'Too many submissions. Please try again later.' });
  }

  const id = (typeof b.submission_id === 'string' && /^[0-9a-f-]{36}$/i.test(b.submission_id))
    ? b.submission_id.toLowerCase() : crypto.randomUUID();

  try {
    const since = new Date(Date.now() - DUP_EMAIL_WINDOW_MS).toISOString();
    const dup = await sql`SELECT submission_id FROM mediator_eois
                          WHERE (submission_id = ${id}) OR (lower(email) = lower(${data.email}) AND submitted_at > ${since})
                          LIMIT 1`;
    if (dup.rows.length) {
      return res.status(200).json({ ok: true, reference: refFor(dup.rows[0].submission_id), duplicate: true });
    }

    await sql`
      INSERT INTO mediator_eois (
        submission_id, form_version, name, email, phone, city, state, organisation, website,
        practice_type, credential_types, credential_body, credential_identifier, experience_band,
        practice_areas, regions_served, delivery_modes, venue_access, capacity_band, languages,
        background, motivation, accuracy_confirmed, privacy_acknowledged, consent_version, marketing_opt_in
      ) VALUES (
        ${id}, ${FORM_VERSION}, ${data.name}, ${data.email}, ${data.phone}, ${data.city}, ${data.state},
        ${data.organisation}, ${data.website}, ${data.practice_type}, ${data.credential_types},
        ${data.credential_body}, ${data.credential_identifier}, ${data.experience_band},
        ${data.practice_areas}, ${data.regions_served}, ${data.delivery_modes}, ${data.venue_access},
        ${data.capacity_band}, ${data.languages}, ${data.background}, ${data.motivation},
        true, true, ${CONSENT_VERSION}, ${data.marketing_opt_in}
      )
      ON CONFLICT (submission_id) DO NOTHING
    `;
    await sql`INSERT INTO mediator_eoi_audit_log (submission_id, event_type) VALUES (${id}, 'SUBMITTED')`;
  } catch {
    return res.status(503).json({
      error: 'We could not save your expression of interest right now. Please try again shortly or email hello@mediationsaustralia.com.au.',
    });
  }

  const n = await notify(id, data);
  try {
    await sql`UPDATE mediator_eois SET notification_status = ${n.ok ? 'SENT' : 'FAILED'},
              notification_attempts = ${n.attempts} WHERE submission_id = ${id}`;
  } catch { /* record is already saved */ }

  return res.status(200).json({ ok: true, reference: refFor(id) });
}
