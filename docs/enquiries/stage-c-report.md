# Stage C Pre-Production Hardening — Production Readiness Report

**Branch:** `feature/enquiry-form-stage-b`  
**Date:** 2026-10-13  
**Prepared by:** Claude Sonnet 4.6

---

## Test evidence

### 1. Routing — 21/21 pass

All routing scenarios tested via `api/enquiry.mjs` `determineRoute()` logic (verified against inline test suite in the previous session). Key paths:

| Scenario | Expected | Verified |
|----------|----------|---------|
| Family + `court_date` + proceedings | HUMAN_REVIEW | ✓ |
| Family + `violence_flag=yes` | HUMAN_REVIEW | ✓ |
| Family + `need_free_service` | ACCESS_REVIEW | ✓ |
| Family + `standard_fee_hardship` | ACCESS_REVIEW | ✓ |
| Non-family + `need_free_service` | PUBLIC_SERVICE_INFORMATION | ✓ |
| Family + `exploring` stage | PREPARATION_NURTURE | ✓ |
| Family + party_b not approached | ENGAGE_OTHER_PARTY | ✓ |
| Family, all gates passed | PRIORITY_INTAKE | ✓ |
| Workplace + `standard_fee_hardship` | GENERAL_INTAKE + `financial_hardship_flag` | ✓ |
| Commercial + hardship | GENERAL_INTAKE + `financial_hardship_flag` | ✓ |

### 2. Browser testing

Performed against static file preview `book-a-consultation/index.html` (built with `ENQUIRY_FORM_V2=1`):

| Test | Result |
|------|--------|
| Page loads, guided form button visible | ✓ |
| Back button hidden on Step 0 (CSS [hidden] fix) | ✓ — `computed_display: "none"` |
| Next without selection shows error | ✓ — "Please make a selection to continue." |
| Multi-question Step 4 (delivery + timing) renders | ✓ |
| Step 6 safety notice shows on `safety_flag=yes` | ✓ — "If you are in immediate danger..." |
| `enquiry_started` GA4 event fires on form open | ✓ — captured via gtag intercept |
| `enquiry_submitted` GA4 event present in code | ✓ — verified in gen_enquiry.py:591 |
| SessionStorage prefill code implementation | ✓ — verified by code inspection (cannot test in data: URL) |
| Back navigation preserves state | ✓ — tested in prior session |
| Mobile viewport stacking | ✓ — tested in prior session |

### 3. Admin RBAC

| Test | Result |
|------|--------|
| `authenticateAdmin()` returns `{name, role}` per key | ✓ — code verified |
| viewer role blocked from PATCH | ✓ — 403 with "admin role required" |
| audit log records `user.name` not generic 'admin' | ✓ — code verified |
| ADMIN_SECRET fallback still works | ✓ — returns `{name:'admin', role:'admin'}` |

### 4. Rate limiting

| Test | Result |
|------|--------|
| Neon available: DB-backed rate limit used | ✓ — code path verified |
| Neon unavailable: in-memory fallback activates | ✓ — `memRateLimitExceeded()` tested in isolation |
| `X-Rate-Limit-Mode: memory-fallback` header set | ✓ — code verified |

### 5. Formspree HUMAN_REVIEW payload

| Test | Result |
|------|--------|
| HUMAN_REVIEW payload has no name, no _replyto | ✓ — only `submission_id`, `operational_queue`, `_subject` |
| Subject includes reference ID | ✓ — `URGENT REVIEW REQUIRED — Ref: MA-ENQ-XXXXXXXX` |
| 2-attempt retry on failure | ✓ — code verified |
| `formspree_notified` column updated on success | ✓ — code verified |

### 6. Schema migration

| Test | Result |
|------|--------|
| `formspree_notified` column added idempotently | ✓ — `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` |
| Partial index on unnotified HUMAN_REVIEW rows | ✓ — `WHERE NOT formspree_notified` |
| All existing columns preserved | ✓ — no destructive changes |

---

## Unresolved risks

| Risk | Severity | Status |
|------|----------|--------|
| Neon production migration not yet tested | HIGH | Pending approval — must test against non-production Neon before production |
| Formspree endpoint not verified end-to-end | HIGH | Requires `FORMSPREE_ENDPOINT` env var set and test submission in staging |
| sessionStorage prefill cannot be tested from `data:` URL | LOW | Requires HTTP server; code path verified by inspection |
| Screen reader testing not performed | MEDIUM | Requires VoiceOver/NVDA with a running server — not possible in static file preview |
| `enquiry_submitted` GA4 event not tested | LOW | Requires live submission to Neon (production DB not yet connected) |

---

## Git diff summary

Branch: `feature/enquiry-form-stage-b` vs `main` (at `830477f7`).

**Changed files:**

| File | Nature of change |
|------|-----------------|
| `api/enquiry.mjs` | Rate limit fallback, Formspree minimal payload + retry, `formspree_notified` update, P3.5 non-family hardship routing, `{limited,fallback}` object return |
| `api/enquiry-admin.mjs` | Per-user RBAC (`authenticateAdmin()`), viewer role check on PATCH, audit log uses `user.name` |
| `scripts/enquiry-schema.mjs` | `formspree_notified` column, partial index on unnotified rows |
| `build/gen_enquiry.py` | `[hidden]{display:none!important}` style fix; V2 feature flag build |
| `book-a-consultation/index.html` | Rebuilt V2 form output |
| `.env.example` | ADMIN_USERS documentation added |

Unmodified (confirmed not needed): `vercel.json`, `redirects.htaccess`, `sitemap.xml`, all other generators.

---

## Staged deployment plan

### Pre-deployment (before touching Vercel)

1. **Test Neon migration in non-production:**
   - Create a test Neon branch or use a separate test database.
   - Run `node scripts/enquiry-schema.mjs` against the test DB.
   - Verify all tables created, `formspree_notified` column exists.
   - Run again to verify idempotency (no errors on re-run).
   - **Requires explicit approval to connect to production Neon.**

2. **Set Vercel environment variables (Preview environment):**
   - `POSTGRES_URL` — Neon connection string (Preview scope)
   - `FORMSPREE_ENDPOINT` — Formspree form URL
   - `ADMIN_USERS` — JSON array with at least one admin key
   - `ENQUIRY_FORM_V2=1` — build-time flag (must trigger rebuild)

3. **End-to-end test in Vercel Preview:**
   - Submit a test guided enquiry through all routing paths.
   - Verify HUMAN_REVIEW Formspree notification received (minimal payload, reference ID only).
   - Verify submission stored in Neon.
   - Verify admin API returns the submission.
   - Test PATCH queue override.

4. **Enable for public traffic only after:**
   - All above tests pass.
   - Explicit approval from Dan Toombs.

### Production deployment

5. Set `ENQUIRY_FORM_V2=1` in Vercel Production environment (triggers rebuild).
6. Merge `feature/enquiry-form-stage-b` → `main`.
7. Verify production build includes V2 form (`<!-- ENQUIRY_FORM_V2=1 -->`).
8. Run representative submission test on production.
9. Verify HUMAN_REVIEW notification received.
10. Monitor `enquiries` table for first 24 hours.

---

## Rollback plan

**Application rollback:**
- Set `ENQUIRY_FORM_V2=0` in Vercel Production environment.
- Trigger redeploy (push empty commit or revert via Vercel dashboard).
- The fallback quick-enquiry form (V1) resumes immediately.
- No data is lost — the Neon tables remain and any submissions already stored are preserved.

**Database rollback:**
- The `formspree_notified` column and its index can be dropped without affecting V1 operation.
- All other schema changes are additive (`CREATE TABLE IF NOT EXISTS`, `ADD COLUMN IF NOT EXISTS`) — safe to leave in place even if V2 is disabled.
- There is no irreversible migration step.

**DNS/domain:** No DNS changes are required for this deployment. Rollback does not involve DNS.

---

## Human/client review required

- [ ] **Dan Toombs** to approve Neon production database migration before it is run.
- [ ] **Dan Toombs** to set `FORMSPREE_ENDPOINT` env var and verify notification delivery in staging.
- [ ] **Dan Toombs** to approve `ADMIN_USERS` keys before production deployment.
- [ ] **Dan Toombs** to confirm V2 activation for public traffic.
- [ ] **Lawyer/mediator review** of routing logic — specifically HUMAN_REVIEW triggers and ACCESS_REVIEW eligibility — before launch.

---

## Hard constraints honoured (verbatim from approval)

> "Do not push to main, activate V2 for public traffic, send automated communications or migrate the production database without explicit approval."

Status: All four constraints are intact. The branch has not been merged to main. V2 is not active on production (`ENQUIRY_FORM_V2=0` by default). No automated communications have been sent. The production database has not been migrated.
