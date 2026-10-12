# Stage A — Architecture & Implementation Plan
## Mediations Australia Intelligent Enquiry Forms

**Produced:** 2026-10-13  
**Status:** For review and approval. No code written.

---

## 1. Design Principles

1. The form gathers information and routes work. A qualified human practitioner determines suitability.
2. Build behind a feature flag. The existing `/book-a-consultation/` form is the fallback at all times.
3. No AI model determines professional suitability, safety, or legal outcomes.
4. Safety concerns, coercion, family violence, child risk, capacity concerns, and urgent legal deadlines → HUMAN_REVIEW. Automated outreach is suppressed.
5. Financial assessment answers (Access Mediation) are never in URLs, analytics, or general email notifications.
6. Do not change slugs, canonicals, sitemap, navigation, or structured data.
7. No automatic push to `main`. All Stage B work on a branch.

---

## 2. Architecture Overview

```
Visitor
  │
  ├── Feature flag OFF ──────────────────────────────► /book-a-consultation/ (unchanged)
  │
  └── Feature flag ON
        │
        ├── Quick Enquiry component (name + safe contact + broad issue)
        │     └── POST /api/enquiry → Formspree + Neon → confirmation
        │
        └── Guided form (6–8 steps + 2–4 conditional)
              │
              ├── Client-side JS state machine (no page reloads)
              ├── Step completion → GA4 event (step ID only)
              │
              └── Submit → POST /api/enquiry
                    │
                    ├── Server-side validation
                    ├── Deterministic routing engine (versioned rules)
                    ├── Neon write (enquiry tables)
                    ├── Formspree notification (minimal, no sensitive data)
                    └── JSON response → confirmation screen
```

---

## 3. Feature Flag Design

**Implementation:** Single environment variable `ENQUIRY_FORM_V2=1` read by the generator at build time.

- Flag OFF (default): All CTAs point to existing `/book-a-consultation/`. No change to any page.
- Flag ON: New guided form rendered at `/book-a-consultation/` (same slug — no SEO URL change). Old form preserved in generator as fallback.
- Rollback: Set `ENQUIRY_FORM_V2=0`, rebuild, deploy. Restores old form in one build cycle.
- The Quick Enquiry component can be enabled independently of the guided form.

**Generator change:** In `build/gen_booking.py` (currently guarded — a new `gen_enquiry.py` should be created rather than running the existing `gen_booking.py` which is out of sync).

---

## 4. Universal Question Matrix

All categories answer these core steps. Branches add 2–4 additional questions only.

### Step 1 — Dispute Type
**Question:** What best describes your situation?

| Value | Label |
|---|---|
| `family_parenting` | Parenting arrangements or children |
| `family_property` | Property or financial settlement |
| `family_combined` | Both parenting and property |
| `workplace_employment` | Workplace or employment |
| `commercial_business` | Business or commercial dispute |
| `estate_inheritance` | Estate or inheritance |
| `elder_family` | Elder care or family decision-making |
| `neighbour_property` | Neighbour, boundary or strata |
| `construction_real_estate` | Construction or real estate |
| `other_unsure` | Not sure / something else |

*Pre-select from page context (URL/referrer) but permit change. Changing category clears branch-specific answers.*

---

### Step 2 — Stage & Desired Outcome
**Question:** Where are things at?

| Value | Label |
|---|---|
| `exploring` | Just exploring options |
| `discussing` | Trying to discuss but stuck |
| `ready_to_arrange` | Ready to arrange mediation |
| `lawyers_involved` | Lawyers are involved |
| `proceedings_started` | Court proceedings have started |
| `court_date` | There is a court date |
| `agreement_needs_formalisation` | We have an agreement, need it formalised |
| `unsure` | Not sure |

If `court_date`: optionally collect date and jurisdiction. Flag for urgent human review. Never suggest deadlines can be delayed.

**Desired outcome:** Short category-specific options (4–5 max). Examples:
- Family: "Reach a parenting agreement" / "Settle finances" / "Both" / "Explore options" / "Unsure"
- Workplace: "Resolve the dispute" / "Repair the relationship" / "Understand my options" / "Unsure"

---

### Step 3 — Other-Party Awareness
**Question:** Does the other party know you're looking into mediation?

| Value | Label |
|---|---|
| `agreed` | Yes, and they are willing |
| `open_to_discussion` | Yes, and they seem open |
| `unsure` | Not sure |
| `not_asked` | I haven't raised it yet |
| `declined` | They have said no |
| `not_applicable` | Not applicable |
| `prefer_not_to_say` | Prefer not to say |

**Enquirer role:**
| Value | Label |
|---|---|
| `participant` | I am a party to the dispute |
| `employer_hr` | I am an employer / HR representative |
| `adviser` | I am an authorised adviser or lawyer |

*Do not collect Party B contact details at this stage.*

---

### Step 4 — Delivery & Location
**Question:** How would you prefer to attend?

| Value | Label |
|---|---|
| `online` | Online (video) |
| `face_to_face` | In person |
| `either` | Either — flexible |
| `unsure` | Not sure |

If face-to-face or either: collect **state** (select) and **city / postcode** (optional text).

Do not promise a local office or mediator availability for any location.

**Timing:**
| Value | Label |
|---|---|
| `urgent` | As soon as possible |
| `within_2_weeks` | Within 2 weeks |
| `within_month` | Within a month |
| `flexible` | Flexible |

---

### Step 5 — Fees & Pathway
**Question:** What best describes your situation regarding fees?

| Value | Label |
|---|---|
| `standard_private` | I will pay standard fees |
| `want_fee_information` | I'd like to understand what it costs first |
| `standard_fee_hardship` | Standard fee would be a genuine hardship |
| `need_free_service` | I need a free or community service |
| `unsure` | Not sure |

If family category + `standard_fee_hardship`: show a brief neutral explanation of Access Mediation and link to `/access-mediation/` to check eligibility. Do not run the eligibility calculation inside the guided form. Do not promise Access availability. If Access capacity is closed (polled from `/api/access-calc` at this step), show a neutral message ("Access Mediation is at capacity this month — you can still apply and join the waitlist, or proceed as standard").

Price shopping (`want_fee_information`) does not equal hardship. Do not route to ACCESS_REVIEW solely on this answer.

---

### Step 6 — Safety & Contact Guardrail
**Question (plain language):** Is there anything about safety, pressure, how we contact you, or an urgent legal deadline that you want a mediator to know before we get in touch?

| Value | Label |
|---|---|
| `no` | No, nothing to flag |
| `yes` | Yes — I'd like someone to review this |
| `prefer_not_to_say` | Prefer not to say |

If `yes` or `prefer_not_to_say`:
- "If you are in immediate danger in Australia, call 000."
- Route → HUMAN_REVIEW
- Suppress automated outbound contact
- Do not ask for details or allegations

**Safe contact follow-up (all respondents):**
- Is email safe for us to contact you? yes / sometimes / no — please use phone only
- Is voicemail safe? yes / no
- Best time to call? Morning / Afternoon / Evening / No preference

---

### Step 7 — Contact & Consent
Fields:
- Name (required)
- At least one safe contact channel — email or phone (required, at least one)
- Preferred contact time (optional)
- Neutral message (optional — "anything else you'd like us to know", 500 char max)
- Privacy consent checkbox (required — links to /privacy-policy/)
- Accuracy declaration (required — "The information I've provided is accurate to the best of my knowledge")

Confirmation screen:
- Reference number (submission_id, displayed as `MA-ENQ-{date}-{short-id}`)
- "We'll be in touch within one business day"
- No suitability statements, no booking promises, no legal advice

---

## 5. Conditional Branch Questions

### Family Parenting (2–3 extra questions)
1. **Issues:** Parenting arrangements / Communication / Relocation / Schooling or holidays / Section 60I / Other
2. **Existing arrangements:** None / Parenting agreement / Court orders / Unsure
3. *(If court orders or court date): flag urgent practitioner review — do not promise certificate or legal outcome*

### Family Property / Combined (3–4 extra questions)
1. **Issues:** Family home / Superannuation / Business interests / Debts / Financial disclosure / Other
2. **Disclosure readiness:** Not started / In progress / Substantially ready / Unsure
3. **Legal advice:** Both parties have / One party has / Neither / Unsure
4. **Complexity:** Standard / Business or trust involved / Multiple properties / Overseas assets / Unsure

If `agreement_needs_formalisation`: route to information about legal process, not automatic mediation sale.

### Workplace / Employment (2–3 extra questions)
1. **Enquirer role:** Employer or HR / Employee / Manager / Adviser / Other
2. **Issue:** Interpersonal / Team / Leadership / Complaint or investigation / Post-investigation / Exit / Workers compensation / Other
3. **Organisation size:** (optional) Under 20 / 20–100 / 100–500 / 500+ / Prefer not to say

Active complaint with Fair Work / tribunal deadline → flag for timing review. No guarantee of confidentiality, privilege, or regulatory outcome.

### Commercial / Business (2–3 extra questions)
1. **Issue:** Contract / Unpaid invoice / Partnership / Shareholder / Supplier / IP / Professional services / Other
2. **Parties:** Individuals / Companies / Mixed / Unsure
3. **Settlement proposal:** Yes / No / Unsure

No contract uploads in the form.

### Estate / Inheritance (2–3 extra questions)
1. **Role:** Executor / Administrator / Beneficiary / Family member / Adviser / Other
2. **Issue:** Will / Entitlement / Executor administration / Distribution / Family disagreement / Other
3. **Stage:** Before administration / Underway / Proceedings started / Unsure

Deadline → flag for human review.

### Elder / Intergenerational (2–3 extra questions)
1. **Issue:** Care arrangements / Living arrangements / Family communication / Financial decisions / Guardianship / Other
2. **Role:** Person concerned / Family member / Professional / Other

Capacity, consent, or safeguarding concerns → mandatory HUMAN_REVIEW. Do not presume a relative can act for the person.

### Neighbour / Property Boundary (2 extra questions)
1. **Issue:** Fencing / Boundary / Noise / Access / Strata / Shared property / Other
2. **Council or tribunal stage:** Not started / Approached council or tribunal / Matter filed

### Construction / Real Estate (2–3 extra questions)
1. **Issue:** Building works / Defects / Contract / Strata / Body corporate / Property transaction / Other
2. **Role:** Owner / Builder / Agent / Body corporate / Adviser / Other
3. **Expert report:** Available / Pending / Not applicable / Unsure

### Other / Unsure
Broad issue (short text, 200 char max) and desired outcome. Minimal contact. Route to GENERAL_INTAKE for human triage.

---

## 6. Quick Enquiry Component

Always available regardless of feature flag state on guided form.

**Fields:** name, safe contact (email or phone — at least one), broad issue (short text or category select), optional message (300 char max)
**Submission:** POST `/api/enquiry` with `form_variant: "quick"`
**Routing:** GENERAL_INTAKE (no routing engine applied)
**Analytics:** `quick_enquiry_submitted` event

---

## 7. Deterministic Routing Engine

All routing is rule-based. No AI model determines suitability.

### Priority Order (first match wins)

1. **HUMAN_REVIEW** — any of:
   - Safety/coercion/family violence signal (`safety_flag: yes` or `prefer_not_to_say`)
   - Child risk or urgent safety concern (inferred from elder/capacity answer)
   - Court date within 7 days
   - Enquirer role = `adviser` for a child or incapacitated person (elder branch)
   - Suppress automated outreach. Create minimal internal escalation only.

2. **ACCESS_REVIEW** — all of:
   - Category is family (parenting, property, or combined)
   - Fee preference is `standard_fee_hardship`
   - Enquirer clicked through from Access Mediation info
   - Staff review eligibility and capacity; no automatic approval.

3. **PUBLIC_SERVICE_INFORMATION** — fee preference is `need_free_service`
   - Provide information about FRC, Legal Aid, community mediation.
   - Optionally offer human support call.

4. **PRIORITY_INTAKE** — all of:
   - Other party status is `agreed` or `open_to_discussion`
   - Stage is `ready_to_arrange` or `discussing`
   - Fee preference is `standard_private` or `want_fee_information`
   - Subject to professional screening at intake.

5. **ENGAGE_OTHER_PARTY** — other party status is `not_asked`, `unsure`, or `not_applicable`
   - Internal queue only. Does NOT trigger any contact with the other party.
   - Enquirer receives standard response about process.

6. **PREPARATION_NURTURE** — disclosure or legal preparation outstanding (family property, complex commercial)
   - Consent-based nurture sequence. Not automatic outreach.

7. **GENERAL_INTAKE** — all other cases

### Tags

- `senior_intake`: high complexity flag (business/trust, overseas assets, multiple parties). Adds tag; never overrides safety review.
- `urgent_deadline`: court date captured. Adds tag; always paired with HUMAN_REVIEW.

### Manual Override

Requires: user (staff member), reason, timestamp. Recorded in audit log.

### Payload Schema (v1.0)

```json
{
  "schema_version": "1.0",
  "submission_id": "uuid-v4",
  "form_variant": "guided | quick",
  "submitted_at": "2026-10-13T10:00:00+10:00",
  "matter_category": "family_parenting",
  "stage": "ready_to_arrange",
  "desired_outcome": "reach_parenting_agreement",
  "party_b_status": "agreed",
  "enquirer_role": "participant",
  "delivery_preference": "online",
  "state": "NSW",
  "city": "Sydney",
  "timing": "within_2_weeks",
  "commercial_pathway": "standard_private",
  "operational_queue": "PRIORITY_INTAKE",
  "professional_review_required": false,
  "review_reasons": [],
  "tags": [],
  "routing_rules_version": "2026-10-v1",
  "safe_email": true,
  "safe_voicemail": true,
  "preferred_contact_time": "morning",
  "safety_flag": "no",
  "consent_version": "2026-10-v1",
  "privacy_consent": true,
  "accuracy_declaration": true,
  "attribution": {
    "landing_page": "/family-law-mediation/",
    "referrer": "https://www.google.com.au/",
    "utm_source": "google",
    "utm_medium": "organic",
    "utm_campaign": null
  },
  "contact": {
    "name": "...",
    "email": "...",
    "phone": "..."
  }
}
```

**Formspree notification payload (minimal — no sensitive fields):**
```json
{
  "submission_id": "uuid-v4",
  "matter_category": "family_parenting",
  "stage": "ready_to_arrange",
  "operational_queue": "PRIORITY_INTAKE",
  "professional_review_required": false,
  "timing": "within_2_weeks",
  "delivery_preference": "online",
  "name": "...",
  "safe_email": true,
  "safe_voicemail": true,
  "preferred_contact_time": "morning"
}
```

*safety_flag value, free-text message, income/assets/hardship, and full contact details are NOT in the Formspree payload.*

---

## 8. Database Schema (New Tables)

New tables sit alongside existing Access Mediation tables in the Neon instance.

```sql
CREATE TABLE enquiries (
  id                     BIGSERIAL PRIMARY KEY,
  submission_id          UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),
  form_variant           TEXT NOT NULL,         -- 'guided' | 'quick'
  schema_version         TEXT NOT NULL,
  routing_rules_version  TEXT NOT NULL,
  submitted_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
  matter_category        TEXT,
  stage                  TEXT,
  desired_outcome        TEXT,
  party_b_status         TEXT,
  enquirer_role          TEXT,
  delivery_preference    TEXT,
  state                  TEXT,
  timing                 TEXT,
  commercial_pathway     TEXT,
  operational_queue      TEXT NOT NULL,
  professional_review_required BOOLEAN NOT NULL DEFAULT false,
  review_reasons         TEXT[],
  tags                   TEXT[],
  safe_email             BOOLEAN,
  safe_voicemail         BOOLEAN,
  preferred_contact_time TEXT,
  safety_flag            TEXT,
  attribution_landing    TEXT,
  attribution_referrer   TEXT,
  attribution_utm_source TEXT,
  attribution_utm_medium TEXT,
  attribution_utm_campaign TEXT,
  consent_version        TEXT,
  privacy_consent        BOOLEAN NOT NULL DEFAULT false,
  accuracy_declaration   BOOLEAN NOT NULL DEFAULT false,
  created_at             TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Separate table for contact details (restricted access)
CREATE TABLE enquiry_contacts (
  enquiry_id   BIGINT NOT NULL REFERENCES enquiries(id),
  name         TEXT NOT NULL,
  email        TEXT,
  phone        TEXT,
  message      TEXT,   -- neutral optional message only; no case details
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Branch-specific answers (separate from routing data)
CREATE TABLE enquiry_branch_answers (
  enquiry_id   BIGINT NOT NULL REFERENCES enquiries(id),
  answer_key   TEXT NOT NULL,
  answer_value TEXT NOT NULL,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Audit log
CREATE TABLE enquiry_audit_log (
  id           BIGSERIAL PRIMARY KEY,
  enquiry_id   BIGINT REFERENCES enquiries(id),
  event_type   TEXT NOT NULL,
  actor        TEXT,
  reason       TEXT,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

---

## 9. Analytics Events (Non-Sensitive Only)

| Event | Trigger | Properties |
|---|---|---|
| `enquiry_started` | User opens guided form | `form_variant` |
| `step_completed` | User completes a step | `step_id` (number only), `form_variant` |
| `enquiry_submitted` | Successful submission | `form_variant`, `operational_queue` |
| `enquiry_error` | Submission error | `error_type` (generic), `form_variant` |
| `quick_enquiry_submitted` | Quick form submitted | — |

No matter category, no safety flag value, no contact details, no financial values in any analytics event.

---

## 10. Files to Create (Stage B)

| File | Purpose |
|---|---|
| `api/enquiry.mjs` | Serverless function: validation, routing engine, Neon write, Formspree notification |
| `scripts/enquiry-schema.mjs` | Database migration: create enquiry tables |
| `build/gen_enquiry.py` | Generator: builds `/book-a-consultation/` with feature flag logic |
| `docs/enquiries/question-matrix.md` | Full question text, answer values, branch logic (this document + detail) |
| `docs/enquiries/routing-matrix.md` | Routing rules table, test cases |
| `docs/enquiries/operational-readme.md` | Staff guide: queues, overrides, escalation |

**Files NOT changed:**
- `api/chat.mjs`, `api/access-calc.mjs`, `api/access-apply.mjs`, `api/admin.mjs`
- Any existing `*/index.html` (except `/book-a-consultation/index.html` via generator)
- `vercel.json` — no SEO URL, noindex, or redirect changes
- `redirects.htaccess`
- Any generator except `gen_enquiry.py` (new file)

---

## 11. Formspree Compatibility

- Existing `xwvgjnve` endpoint continues to receive the general booking form payload as the fallback.
- New guided form sends a separate structured JSON payload to the same endpoint (Formspree accepts JSON via fetch with `Accept: application/json`).
- If a future dedicated Formspree form ID is preferred for the structured payload, that is a one-line change in `api/enquiry.mjs`.

---

## 12. GrokBot (Draft Integration — Scope Decision Required)

The spec says: "GrokBot drafts only initially." Options for Stage B:

**Option A — Defer to Stage C (recommended):** Stage B submits the structured payload to Neon only. No GrokBot draft generated at submission time. Staff triage from the admin panel. GrokBot draft integration is built and tested in Stage C with practitioner review.

**Option B — Include in Stage B (draft-only):** `api/enquiry.mjs` calls Claude Haiku post-submission to draft a triage summary. Draft stored in Neon, never sent automatically. Visible to admin panel only. Adds Anthropic API cost per submission (~$0.002 per enquiry at Haiku pricing).

**Recommendation:** Option A. Deferring reduces Stage B scope, keeps the safety review simpler, and means the draft wording goes through practitioner review (Stage C) before any enquirer sees it.

---

## 13. SEO Impact Assessment

- No slug changes. `/book-a-consultation/` retains its URL.
- No canonical, sitemap, or navigation changes.
- No new indexable pages.
- Feature flag OFF restores the original page; the new page inherits the same title/desc/schema.
- Risk: if the guided form renders content in JS only, Googlebot may not index it. Mitigation: the page's static HTML renders the Quick Enquiry form and a brief descriptive paragraph; the guided form progressively enhances that.

---

## 14. Rollback Plan

1. Set `ENQUIRY_FORM_V2=0` in Vercel environment variables.
2. Rebuild and deploy: `python3 build/gen_enquiry.py` + `git push`.
3. Old `/book-a-consultation/` form restored within one Vercel deployment cycle.
4. No data is lost — Neon tables and Formspree submissions are unaffected.
5. Formspree `xwvgjnve` continues delivering to inbox throughout.

---

## 15. Stage B Effort Estimate

| Component | Complexity |
|---|---|
| Feature flag + generator | Low |
| Client-side form state machine (JS) | Medium |
| Question matrix + conditional rendering | Medium-High |
| Routing engine (api/enquiry.mjs) | Medium |
| Database schema + migration | Low |
| Formspree adapter | Low |
| Analytics events | Low |
| Quick Enquiry component | Low |
| Tests (all branches, safety, duplicate) | Medium |
| Operational README | Low |

**Not in Stage B:** GrokBot draft, Access Mediation capacity live poll, attribution deep-dive, privacy policy rewrite.

---

*Architecture draft complete. Awaiting review and approval before Stage B begins.*
