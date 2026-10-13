# Stage D Readiness Report
**Date:** 2026-10-13  
**Branch:** `feature/enquiry-stage-d`  
**Status:** READY WITH CONDITIONS

---

## Workstream A — Production configuration and notification integrity

### FORMSPREE_ENDPOINT
- **Status:** Code updated to `process.env.FORMSPREE_ENDPOINT || 'https://formspree.io/f/mnpjbroe'`
- **Required dashboard action (operator):** Set `FORMSPREE_ENDPOINT=https://formspree.io/f/mnpjbroe` in Vercel → Production environment. Command: `echo "https://formspree.io/f/mnpjbroe" | npx vercel env add FORMSPREE_ENDPOINT production`
- **Risk if not done:** Hardcoded fallback is active and correct. A future endpoint change requires a code deploy rather than an env var update.

### Notification integrity
- Write happens first; notification is attempted after successful Neon write only.
- Failed notifications: `formspree_notified=false`, `notification_last_error` populated. Admin list view exposes this — operator can identify and retry manually.
- No silent loss path: a successful Neon write with a failed Formspree call results in a record visible in the admin queue with `notification_attempts` set.
- HUMAN_REVIEW payload: reference ID and subject line only — no name, no category, no contact detail.
- Retry: 2 attempts with 1-second delay. Further retry requires staff action via admin API.

### V1 Formspree-only leads
- V1 Quick Enquiry posts directly to the original Formspree endpoint, bypassing Neon.
- These leads have no reference ID and are not in the admin queue.
- **Reconciliation procedure:** documented in `staff-intake-runbook.md` §6.
- **Operator decision required:** whether to unify V1 into Neon (requires privacy assessment) or continue dual-stream until V2 is the only active form.

---

## Workstream B — Staff access and privacy

### Admin API security
- Per-user RBAC via `ADMIN_USERS` env var (preferred) or `ADMIN_SECRET` fallback.
- Rate limiting: 30 requests per 60 seconds per authenticated user — added Stage D.
- Detail view access is now logged to `enquiry_audit_log` (event: `ADMIN_ACCESS`).
- Notes on queue override are capped at 500 characters.
- Viewer role cannot PATCH — enforced server-side.
- `ADMIN_SECRET` fallback returns `role: admin` — **retire before wider staff access** (see §3 below).

### Conditions before wider staff access
1. **Set `ADMIN_USERS`** with individual keys per staff member — eliminates shared secret.
2. **Remove `ADMIN_SECRET`** from Vercel env after `ADMIN_USERS` is set and tested.
3. **Periodic key rotation** — document rotation as a quarterly task in the runbook.

### Privacy
- Draft privacy collection notice in `privacy-review-draft.md` — **requires legal/privacy review before publication**.
- Data minimisation: contact details in separate restricted table; safety flag never forwarded externally; message text never in Formspree.

---

## Workstream C — Practitioner routing sign-off

### Routing matrix (for Farley/practitioner review)
See `staff-intake-runbook.md` §2 for exact question text and escalation criteria.

| Rule | Trigger | Queue | Notes |
|---|---|---|---|
| Safety flag | User answered Yes to safety question | HUMAN_REVIEW | No automated contact |
| Urgent court date | stage=court_date | HUMAN_REVIEW | Also urgent+proceedings/lawyers |
| Elder capacity | elder_family + capacity_concern=yes OR safeguarding=yes | HUMAN_REVIEW | Branch answer required |
| Family hardship | family_* category + fee=standard_fee_hardship | ACCESS_REVIEW | Family only |
| Free service | fee=need_free_service | PUBLIC_SERVICE_INFORMATION | All categories |
| Non-family hardship | non-family + fee=standard_fee_hardship | GENERAL_INTAKE + tag:financial_hardship_flag | Staff assess fee options |
| Prep outstanding | family property/combined + disclosure not started + no/one-party legal advice | PREPARATION_NURTURE | |
| Commercial prep | commercial + no settlement proposal + exploring | PREPARATION_NURTURE | |
| Both willing + ready | party_b agreed/open/not_applicable + stage discussing/ready + standard fee | PRIORITY_INTAKE | |
| Party B unknown | party_b not_asked or unsure | ENGAGE_OTHER_PARTY | Internal queue only |
| All other | — | GENERAL_INTAKE | |

**Practitioner sign-off required on:**
- Safety question exact wording (see form HTML)
- Court-date urgency threshold
- Elder capacity/safeguarding branch questions
- Handling of `declined` party B status
- Access mediation suitability criteria

**Status:** ⚠️ Pending Farley review — do not use routing autonomously until signed off.

---

## Workstream D — GrokBot bridge

- `GET /api/agent-intake` implemented.
- Auth: `AGENT_INTAKE_TOKEN` env var (Bearer token).
- HUMAN_REVIEW and safety-flagged leads: reference + restricted:true only.
- Non-restricted leads: operational metadata only — no name, email, phone, message, safety detail.
- Cursor-based pagination (submitted_at, exclusive, ascending).
- Rate limit: 60 requests/hour.
- All access logged to `enquiry_audit_log` (event: `AGENT_INTAKE_ACCESS`).
- **Required before activation:** Set `AGENT_INTAKE_TOKEN` in Vercel Production: `openssl rand -hex 32 | npx vercel env add AGENT_INTAKE_TOKEN production`

---

## Workstream E — Documentation

| File | Status |
|---|---|
| `docs/enquiries/stage-d-readiness.md` | ✅ This file |
| `docs/enquiries/staff-intake-runbook.md` | ✅ Complete |
| `docs/enquiries/privacy-review-draft.md` | ✅ Draft — pending legal review |
| `docs/enquiries/grokbot-bridge-contract.md` | ✅ Complete |
| `docs/enquiries/incident-and-rollback.md` | ✅ Complete |

---

## Deployment readiness decision

**READY WITH CONDITIONS**

### Before merging to production
1. Operator: Set `FORMSPREE_ENDPOINT` in Vercel Production env.
2. Operator: Set `AGENT_INTAKE_TOKEN` in Vercel Production env before activating GrokBot.
3. Operator: Set `ADMIN_USERS` with individual staff keys; remove `ADMIN_SECRET`.
4. Legal/privacy: Review and approve `privacy-review-draft.md` before updating the live privacy policy.
5. Practitioner: Farley (or equivalent) reviews and signs off the routing matrix above.

### Non-blocking (post-launch)
- V1/V2 reconciliation procedure — document decision on dual-stream vs. V2-only.
- Quarterly key rotation runbook entry.

### No blockers to code merge — all functionality is implemented and tested.
