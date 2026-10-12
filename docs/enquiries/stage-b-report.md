# Stage B Implementation Report
**Branch:** `feature/enquiry-form-stage-b`
**Date:** 2026-10-13
**Status:** Implementation complete. Not pushed. Not deployed. Awaiting Stage C approval.

---

## Changes made

### New files (untracked — not yet committed)

| File | Purpose |
|---|---|
| `api/enquiry.mjs` | POST endpoint — validation, routing engine, rate limiting, idempotency, Formspree adapter, Neon write |
| `api/enquiry-admin.mjs` | Authenticated admin interface — GET list/detail, PATCH queue override |
| `scripts/enquiry-schema.mjs` | Neon migration — creates 4 tables + indexes; safe to re-run |
| `build/gen_enquiry.py` | Page generator — outputs V1 fallback and V2 guided form for `/book-a-consultation/` |
| `docs/enquiries/discovery.md` | Stage A discovery report |
| `docs/enquiries/architecture.md` | Stage A architecture design |
| `docs/enquiries/stage-b-report.md` | This document |

### Modified files

| File | Change |
|---|---|
| `build/templates.py` | Line 744: quiz CTA `href` changed from `/contact-us/` to `/book-a-consultation/`; added `onclick` that saves `_qd.type` to sessionStorage before navigation |
| `.env.example` | Added `ADMIN_SECRET` and `ENQUIRY_FORM_V2` documentation |

### Rebuilt files (build output)

| File | How |
|---|---|
| `book-a-consultation/index.html` | `python3 build/gen_enquiry.py` — V1 fallback confirmed built |
| `index.html` | `python3 build/gen_home.py` — picks up quiz CTA fix |

> `family-law-mediation/index.html` appears in the git diff due to pre-existing generator drift. It is not a Stage B change and should be excluded from the Stage B commit.

---

## Routing test matrix

Tests run: 21 | All correct (one test expectation corrected during review — see note)

**Correction note:** Test "Workplace + hardship" had expectation GENERAL_INTAKE but correct answer is ENGAGE_OTHER_PARTY. For `workplace_employment + standard_fee_hardship + party_b=not_asked`, the routing falls to P6 (ENGAGE_OTHER_PARTY) because the other party has not been approached — fee preference does not bypass party engagement. Only `family_* + standard_fee_hardship` bypasses to ACCESS_REVIEW at P2.

### Priority order (P1 → P7)

| P | Queue | Triggering condition |
|---|---|---|
| 1 | HUMAN_REVIEW | `safety_flag=yes/prefer_not_to_say` |
| 1 | HUMAN_REVIEW | `stage=court_date` |
| 1 | HUMAN_REVIEW | `timing=urgent AND stage∈{proceedings_started,lawyers_involved}` |
| 1 | HUMAN_REVIEW | `category=elder_family AND (capacity_concern=yes OR safeguarding=yes)` |
| 2 | ACCESS_REVIEW | `category∈{family_parenting,family_property,family_combined} AND fee=standard_fee_hardship` — no prior Access page visit required |
| 3 | PUBLIC_SERVICE_INFORMATION | `fee=need_free_service` |
| 4 | PREPARATION_NURTURE | Family property/combined with `disclosure∈{not_started,in_progress}` AND `legal_advice∈{neither,one_party}` |
| 4 | PREPARATION_NURTURE | Commercial with `settlement_proposal=no AND stage=exploring` |
| 5 | PRIORITY_INTAKE | `party_b∈{agreed,open_to_discussion,not_applicable} AND stage∈{ready_to_arrange,discussing} AND fee∈{standard_private,want_fee_information}` |
| 6 | ENGAGE_OTHER_PARTY | `party_b∈{not_asked,unsure}` — never `not_applicable` |
| 7 | GENERAL_INTAKE | Everything else (declined party, other/unsure fee, unmatched combinations) |

**Amendment 1:** `not_applicable` never routes to ENGAGE_OTHER_PARTY. Confirmed by two tests.
**Amendment 2:** Family + hardship routes to ACCESS_REVIEW without requiring `/access-mediation/` visit. Three family category variants confirmed.

### Sample payloads

**Family parenting → HUMAN_REVIEW (safety)**
```json
{ "safety_flag": "yes", "matter_category": "family_parenting",
  "stage": "ready_to_arrange", "party_b_status": "agreed", "fee_preference": "standard_private" }
→ { "operational_queue": "HUMAN_REVIEW", "professional_review_required": true,
    "review_reasons": ["safety_flag"] }
```

**Family property → ACCESS_REVIEW (hardship)**
```json
{ "safety_flag": "no", "matter_category": "family_property",
  "stage": "exploring", "party_b_status": "unsure", "fee_preference": "standard_fee_hardship" }
→ { "operational_queue": "ACCESS_REVIEW", "professional_review_required": false }
```

**Workplace → PRIORITY_INTAKE (both willing)**
```json
{ "safety_flag": "no", "matter_category": "workplace_employment",
  "stage": "discussing", "party_b_status": "open_to_discussion", "fee_preference": "want_fee_information" }
→ { "operational_queue": "PRIORITY_INTAKE", "professional_review_required": false }
```

**Estate → HUMAN_REVIEW (court date)**
```json
{ "safety_flag": "no", "matter_category": "estate_inheritance",
  "stage": "court_date", "party_b_status": "agreed", "fee_preference": "standard_private" }
→ { "operational_queue": "HUMAN_REVIEW", "professional_review_required": true,
    "review_reasons": ["urgent_deadline"], "tags": ["urgent_deadline"] }
```

**Commercial → PREPARATION_NURTURE**
```json
{ "safety_flag": "no", "matter_category": "commercial_business",
  "stage": "exploring", "party_b_status": "open_to_discussion", "fee_preference": "standard_private",
  "branch_answers": { "settlement_proposal": "no" } }
→ { "operational_queue": "PREPARATION_NURTURE", "professional_review_required": false }
```

---

## Security review

### Validation
- Required fields checked: `submission_id` (UUID format), `matter_category` (explicit allowlist), `stage` (explicit allowlist), `consent` (must be boolean true)
- Field-length limits on all string inputs
- Honeypot `_hp` (guided) and `qk-hp` (quick) — any non-empty value rejects the submission
- All enum fields validated against allowlists — no freetext category accepted
- `safety_flag` value, `free_text_message`, income/assets fields are never forwarded to Formspree or analytics

### Rate limiting
- Neon-backed: 5 submissions per IP per 15-minute sliding window
- IP stored in `enquiry_audit_log` (SUBMITTED events) — never in `enquiries` table
- **Fail-open on Neon error** — rate limit is skipped if the database is unreachable to avoid blocking genuine enquiries. This is a deliberate design choice; operator should be aware.

### Idempotency
- Client generates `submission_id` UUID on page load via `crypto.randomUUID()`
- Server checks for existing record before write — returns existing if found
- Duplicate submits (network retry, double-click) produce one lead

### Spam protection
- Honeypot fields (hidden, bots fill them)
- Server-side rate limiting
- No CAPTCHA (deliberately avoided for accessibility)

### Admin authentication
- `Authorization: Bearer <ADMIN_SECRET>` header required
- Returns 401 if `ADMIN_SECRET` is not set in env (deny-all default)
- Same pattern as existing `api/admin.mjs`
- `ADMIN_SECRET` is never committed — documented in `.env.example` only

### Formspree payload (amendment 4 compliance)
Minimal non-sensitive fields only:

| Field | Value |
|---|---|
| `submission_id` | UUID reference for staff lookup |
| `operational_queue` | Queue name |
| `professional_review_required` | Boolean |
| `form_variant` | `guided` or `quick` |
| `matter_category` | Dispute category |
| `stage` | Process stage |
| `delivery_preference` | Online/face-to-face |
| `timing` | Urgency |
| `safe_email` | Boolean |
| `safe_voicemail` | Boolean |
| `preferred_contact_time` | Time preference |
| `name` | Display name |
| `_subject` | Auto-generated subject |
| `_replyto` | Email for reply threading |

**Never included:** `safety_flag` value, `free_text_message` body, `phone` in plain text, income/assets, sensitive branch answers.

### Analytics
GA4 events: `enquiry_started`, `step_completed` (step index only), `enquiry_submitted`, `quick_enquiry_submitted`. Non-sensitive parameters only. Safety, contact details, income — never passed to GA4.

### sessionStorage (amendment 3)
Only `_qd.type` (dispute category) is written before quiz CTA navigation. Read immediately on page load and deleted. No sensitive quiz answers stored.

### Secrets
No secrets committed. `POSTGRES_URL` and `ADMIN_SECRET` are server-side env vars only. Formspree `xwvgjnve` is a public endpoint ID (not a secret).

---

## Git diff summary

```
.env.example                    |   4 +  ADMIN_SECRET + ENQUIRY_FORM_V2 docs
book-a-consultation/index.html  | 801    V2 guided form added; V1 fallback preserved
build/templates.py              |   2 ±  quiz CTA href fix + sessionStorage onclick
index.html                      |   2 ±  picks up quiz CTA fix via gen_home.py rebuild
```

Untracked new files to stage for Stage B commit:
- `api/enquiry.mjs`
- `api/enquiry-admin.mjs`
- `scripts/enquiry-schema.mjs`
- `build/gen_enquiry.py`
- `docs/enquiries/` (all three documents)

**Exclude:** `family-law-mediation/index.html` — pre-existing generator drift, not Stage B.

---

## Database schema (not yet applied)

```sql
-- enquiries: routing result, non-sensitive metadata
CREATE TABLE IF NOT EXISTS enquiries (
  submission_id UUID PRIMARY KEY,
  form_variant TEXT,
  matter_category TEXT,
  stage TEXT,
  operational_queue TEXT,
  professional_review_required BOOLEAN,
  review_reasons TEXT[],
  routing_rules_version TEXT,
  consent_version TEXT,
  delivery_preference TEXT,
  timing TEXT,
  preferred_contact_time TEXT,
  party_b_status TEXT,
  safe_email BOOLEAN,
  safe_voicemail BOOLEAN,
  submitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- enquiry_contacts: restricted PII (name, email, phone, message)
CREATE TABLE IF NOT EXISTS enquiry_contacts (
  id BIGSERIAL PRIMARY KEY,
  submission_id UUID REFERENCES enquiries(submission_id),
  name TEXT,
  email TEXT,
  phone TEXT,
  message TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- enquiry_branch_answers: conditional branch key/value answers
CREATE TABLE IF NOT EXISTS enquiry_branch_answers (
  id BIGSERIAL PRIMARY KEY,
  submission_id UUID REFERENCES enquiries(submission_id),
  answer_key TEXT,
  answer_value TEXT
);

-- enquiry_audit_log: SUBMITTED events (IP for rate limit), QUEUE_OVERRIDE events
CREATE TABLE IF NOT EXISTS enquiry_audit_log (
  id BIGSERIAL PRIMARY KEY,
  submission_id UUID,
  event_type TEXT,
  actor TEXT,
  detail JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

To apply: `POSTGRES_URL=<neon-url> node scripts/enquiry-schema.mjs`
The API returns 500 without this migration.

---

## SEO impact

- `/book-a-consultation/` URL preserved — no change
- Canonical, title, H1, schema — no change
- Feature flag `ENQUIRY_FORM_V2=0` default — existing Formspree form active by default
- Homepage quiz CTA corrected: was `/contact-us/` (broken), now `/book-a-consultation/` (correct)
- No new routes, no sitemap changes, no redirect changes

---

## Tests performed

- Routing engine: 21 test cases, all 7 queues covered, all 6 amendment conditions verified
- V1 build: `ENQUIRY_FORM_V2=0 python3 build/gen_enquiry.py` → confirmed
- V2 build: `ENQUIRY_FORM_V2=1 python3 build/gen_enquiry.py` → confirmed
- Homepage rebuild: `python3 build/gen_home.py` → quiz CTA fix confirmed in diff

**Not tested (requires Stage C — browser/live environment):**
- End-to-end submission to Formspree live endpoint
- Admin interface against real Neon data
- sessionStorage prefill across two pages in browser
- Rate limiting under repeated submission
- All conditional branch questions in browser
- Keyboard navigation, screen reader, mobile
- GA4 event firing

---

## Issues requiring approval before Stage C

### 1. Database migration authorisation (blocker)
`scripts/enquiry-schema.mjs` must be run against the Neon database before the API can function. Requires explicit operator sign-off. Command: `POSTGRES_URL=<neon-url> node scripts/enquiry-schema.mjs`

### 2. Privacy policy legal review (blocker)
New collection scope includes safety signals, financial hardship indication, and party relationship information. APPs require the privacy policy to reflect what is collected and why. Lawyer/compliance review required before any traffic is directed to the new form.

### 3. Response time SLA wording (approval)
"One business day" removed per amendment 6. Confirmation screen and email now say "we will be in touch as soon as we can." The business must approve this wording.

### 4. Access Mediation capacity integration (decision)
For ACCESS_REVIEW cases, the form shows static eligibility information. The spec mentions live capacity polling from "the existing approved source." Confirm whether static text is acceptable for Stage C or whether live capacity is required.

### 5. Operational README for admin interface (required before pilot)
`api/enquiry-admin.mjs` exposes full contact details. An operational procedure (authentication, queue override process, data handling) must be documented and approved before staff use it.

### 6. Formspree endpoint verification (required before pilot)
Confirm the existing Formspree form (`xwvgjnve`) accepts JSON payloads with `Accept: application/json` and that notifications reach the correct inbox.

### 7. GrokBot integration — Stage C scope
Deferred per amendment. No GrokBot code exists in this branch.

---

## Human/client review required

- Routing logic review by Farley/qualified mediator — do the 7 queues match operational intake practice?
- Confirmation screen wording — no suitability promises, no booking commitments
- Safety question wording (step 6) — practitioner review required
- Access Mediation eligibility text for hardship cases — Access Mediation team review
- Fee pathway descriptions — commercial accuracy confirmation

---

## What was not changed

- Access Mediation calculator (`/access-mediation/`) — untouched
- SEO architecture, canonicals, sitemap — untouched
- Navigation — untouched
- Homepage H1 — untouched
- Any existing redirects — untouched
- Production Formspree form (available as V1 fallback when `ENQUIRY_FORM_V2=0`)
- Any page other than `/book-a-consultation/` and the homepage quiz CTA link
