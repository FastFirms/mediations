# Stage A — Discovery Report
## Mediations Australia Intelligent Enquiry Forms

**Produced:** 2026-10-13  
**Scope:** Repository inspection only. No code changed, no files deployed.  
**Next gate:** Architecture review and approval before Stage B begins.

---

## 1. Current Forms Inventory

### 1.1 General Enquiry / Booking Form

| Property | Value |
|---|---|
| Pages | `/book-a-consultation/`, `/contact-us/`, `/workplace-mediation-lp/`, `/belbin-team-roles-training/` |
| Formspree endpoint | `https://formspree.io/f/xwvgjnve` (single shared ID across all four) |
| Method | `/book-a-consultation/` — native HTML POST; `/contact-us/` — JS fetch |
| Spam protection | `_gotcha` honeypot (hidden, off-screen), `_subject` hidden field |
| Server validation | None beyond Formspree's own; client-only `required` attributes |
| Fields collected | name (req), phone (req), email (req), matter select (req), location (opt), message (opt) |
| Matter options | Property Settlement, Parenting, Property & Parenting, Other Family Law, Workplace, Estate, Something else |
| Submission ID | None — no UUID, no schema version, no deduplication |
| Confirmation | `thank-you/index.html` (native POST) or inline status message (fetch) |
| Analytics events | None wired — GA4 present on pages but no `enquiry_submitted` event |

**Gap:** One endpoint handles all enquiry types with no structure, no routing, no idempotency.

---

### 1.2 Homepage Quick-Step Widget

| Property | Value |
|---|---|
| Location | `index.html` inline JS (`qGo`, `_qd`, `_qhist`) |
| Purpose | Pre-qualifies dispute type and stage; routes to `/book-a-consultation/` |
| Submission | Does NOT submit — collects clicks then redirects |
| Data stored | In-memory JS `_qd` object; not persisted or transmitted |
| Context carried to booking | No — dropped at redirect |

**Gap:** Pre-qualification context is discarded on redirect. The new form should accept it.

---

### 1.3 Access Mediation Calculator & Application

| Property | Value |
|---|---|
| Entry page | `/access-mediation/` |
| Calculator JS | `access-calc.js` (563 lines, client-side multi-step) |
| Calculator API | POST `/api/access-calc` — pure eligibility, no storage |
| Application API | POST `/api/access-apply` — writes to Neon, checks capacity |
| Admin panel | `/admin/` — Bearer auth, GET/PATCH `/api/admin` |
| Database | Neon (Vercel Postgres + pgvector) |
| Formspree notification | Same `xwvgjnve` — sends only matter_id, matter_type, party_a_name (no financial data) |

**Calculator steps:** income_band → dependants → assets_band → concession → hardship → matter_type → needs_60i

**Contribution bands (ex GST, 3h):** Band 1 $495 / Band 2 $695 / Band 3 $895 / Band 4 $1,095 / Band 5 $1,295 / Standard $1,500

**Capacity:** 8 units/month (`MAX_MONTHLY_UNITS = 8`). Consumed at booking, not application. Waitlist is informational.

**Privacy guardrails (confirmed in code):** Financial bands never in URLs, never to Formspree, never in analytics events.

---

### 1.4 GrokBot (Chat Widget)

| Property | Value |
|---|---|
| UI | `widget.js` — floating chat button (Dan Toombs avatar) + panel |
| API | POST `/api/chat` → `api/chat.mjs` |
| Model | Claude Haiku `claude-haiku-4-5-20251001` |
| Retrieval | OpenAI `text-embedding-3-small` + pgvector cosine (top-5 chunks) |
| Scope | General information only; draft-only; no legal advice, no sending, no suitability |
| Data stored | Stateless per request — no chat log persisted |

GrokBot is a distinct product. The enquiry form must not overlap its function.

---

## 2. Technology Stack

| Layer | Current |
|---|---|
| Site generator | Python (`build/*.py`) — static HTML |
| Hosting | Vercel — auto-deploys from `main` |
| Serverless functions | Vercel (`api/*.mjs`, Node ESM) |
| Database | Neon / Vercel Postgres + pgvector |
| Form submission | Formspree endpoint `xwvgjnve` |
| Analytics | GA4 `G-7GTTR2T25L` via gtag.js (no GTM) |
| Chat model | Claude Haiku (Anthropic SDK ^0.30.0) |
| Embeddings | OpenAI text-embedding-3-small (OpenAI SDK ^4.67.0) |
| Dependencies | @anthropic-ai/sdk, @vercel/postgres, openai |

---

## 3. Security & Privacy (Current State)

| Control | Status |
|---|---|
| HTTPS + HSTS | Pass — max-age=63072000 in vercel.json |
| X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy | Pass |
| CSP | Not present |
| CSRF | Not present on general forms (Formspree handles at their end) |
| Rate limiting | Not present on general forms |
| Admin auth | Pass — Bearer `ADMIN_SECRET` env var |
| Financial data in URLs | Pass — prevented by design |
| Financial data to analytics | Pass — step IDs and result type only |
| Consent checkbox on general form | Not present |
| Privacy policy | Exists at /privacy-policy/ — references Privacy Act 1988, APPs |
| Data retention / deletion policy | Not specified in policy |
| Access Mediation consent | Pass — `privacy_consent` + `accuracy_declaration` booleans |

---

## 4. Analytics & Attribution

- GA4 `G-7GTTR2T25L` on all pages
- No `enquiry_started`, `step_completed`, `enquiry_submitted` events in current form JS
- No UTM / attribution capture in Formspree payload
- Access Mediation: step IDs and result type only (correct)
- **Gap:** No conversion event tracking on general enquiry

---

## 5. CTA Inventory

| CTA | Destination | Coverage |
|---|---|---|
| "Book a Free Consultation" button | /book-a-consultation/ | 477+ pages |
| "Contact" nav link | /contact-us/ | All pages |
| Phone (02) 7227 7373 | tel: | All pages (header, footer) |
| Homepage quick-step widget | → /book-a-consultation/ | Homepage |
| Access Mediation CTA | /access-mediation/ | Selected family pages |
| GrokBot chat | /api/chat inline | All pages |

---

## 6. Gaps vs Specification

| Requirement | Current state | Gap |
|---|---|---|
| submission_id UUID | Not present | New |
| schema_version | Not present | New |
| Machine-readable matter category | Free-text select label | New |
| Operational queue routing | Not present | New — routing engine |
| Safety/coercion trigger → HUMAN_REVIEW | Not present | New |
| Party B status capture | Not present | New |
| Delivery preference | Location free-text only | New |
| Timing preference | Not present | New |
| Fee pathway preference | Not present | New |
| Explicit consent checkbox | Not present | New |
| Idempotency / duplicate prevention | Not present | New |
| Feature flag (restore old form) | Not present | New |
| Analytics events (step, submitted, error) | Not present | New |
| UTM / attribution fields | Not present | New |
| Safe-contact preference | Not present | New |
| Quick Enquiry fallback component | /book-a-consultation/ acts as fallback | Keep + new Quick Enquiry |

---

## 7. Readiness Assessment

| Item | Assessment |
|---|---|
| Framework | Static + Vercel serverless — new form is `api/enquiry.mjs` + inline JS. No framework change. |
| Formspree | Existing endpoint preserved. New payload is additive. |
| Access Mediation | Separate sophisticated flow. Guided form branches to /access-mediation/ — does not replicate the calculator. |
| Database | Neon already in use. New enquiry tables added alongside existing. |
| New AI/vendor | None — Anthropic SDK already present for any GrokBot draft integration. |
| New sensitive-data processor | None — Neon and Formspree already in use. No approval required on this basis. |
| Privacy policy update | Required — new fields (consent, safe-contact, routing data) need disclosure. Legal review recommended before Stage D. |
| Existing submissions | Preserved — Formspree continues; Neon Access data untouched. |

---

## 8. Approvals Required Before Stage B

1. Architecture document review and approval (this gate).
2. Confirm GrokBot integration scope for Stage B — drafts only, or deferred to Stage C?
3. Confirm Access Mediation display method — link/redirect to /access-mediation/, not a re-implementation of the calculator inside the guided form.
4. Privacy policy update — recommend legal review before Stage D launch.

---

*Stage A discovery complete. See architecture.md for design.*
