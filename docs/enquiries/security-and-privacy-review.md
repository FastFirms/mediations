# Security and Privacy Review — Enquiry System

**Branch:** `feature/enquiry-form-stage-b`  
**Date:** 2026-10-13  
**Status:** Pre-production review — not a legal sign-off

---

## 1. Authentication and access control

### Admin API (`/api/enquiry-admin`)

| Control | Implementation | Residual risk |
|---------|---------------|---------------|
| Per-user Bearer tokens | `ADMIN_USERS` JSON env var; each key is unique per staff member | Keys are long-lived — no automatic rotation. Recommend periodic rotation. |
| Role separation | `admin` (GET + PATCH) / `viewer` (GET only) | Only two roles — no finer-grained control (e.g. read-only for one queue) |
| Audit log | PATCH records `user.name` and reason in `enquiry_audit_log` | Audit log not currently surfaced in a dashboard — reviewed manually via DB |
| Revocation | Remove key from `ADMIN_USERS` env var and redeploy | Requires Vercel deployment; no instant revocation without redeploy |
| Fallback secret | `ADMIN_SECRET` backward-compatible single-key path | Shared secret has no per-user audit trail — migrate all users to `ADMIN_USERS` before launch |
| No client-side exposure | Keys server-side only; never in JS bundle, URL or Formspree | ✓ Confirmed by code review |

**Action required before production:** Remove or disable `ADMIN_SECRET` once all staff have individual keys in `ADMIN_USERS`.

### Submission API (`/api/enquiry`)

| Control | Implementation |
|---------|---------------|
| No authentication required | Public POST endpoint — protected by rate limit + honeypot + validation |
| Rate limit | 5 submissions per IP per 15 min (Neon-backed; in-memory fallback on Neon outage) |
| Honeypot | `_hp` field — silent pass, no 4xx given to bots |
| Server-side allowlist validation | All categorical fields validated against explicit Sets; free text size-limited |
| No secrets in client JS | `FORMSPREE_ENDPOINT` is hardcoded in server-side `.mjs` only |

---

## 2. Data minimisation and separation

| Data type | Where stored | Restricted? |
|-----------|-------------|-------------|
| Routing answers (category, stage, fee preference) | `enquiries` table | No — operational staff |
| Contact details (name, email, phone, message) | `enquiry_contacts` table | Yes — separate table; join required |
| Branch-specific answers | `enquiry_branch_answers` | No — operational staff |
| IP address | `enquiry_audit_log` (actor field only) | Partial — not in main enquiry record |
| Safety flag value | `enquiries.safety_flag` | No — accessible to all admin role |
| Free-text case narrative | NOT collected by this form | N/A |

**GA4:** No category, safety, hardship, contact detail or free text sent to GA4. Only: `enquiry_started`, `step_completed` (index only), `enquiry_submitted` (queue name only), `quick_enquiry_submitted`.

**Formspree (HUMAN_REVIEW):** Only `submission_id` and subject line with reference ID — no name, no contact detail, no category.

**Formspree (other queues):** Name, safe contact preferences, category, timing — no phone, no email, no message, no safety detail beyond queue name.

---

## 3. Notification delivery and sensitive data

| Queue | Formspree payload | _replyto set? |
|-------|------------------|---------------|
| HUMAN_REVIEW | Reference ID + subject only | No |
| All others (safe_email=true, safety=no) | Name, category, safe contact prefs | Yes (email) |
| All others (safety_flag=yes) | As above | No — safety-flagged enquiries never get _replyto |
| All others (safe_email=false) | As above | No |

**Automatic email to enquirer:** Not implemented. No auto-reply or acknowledgement email is sent. All outbound communication requires human action.

---

## 4. Neon (Vercel Postgres) — data location and access

- **Data location:** Neon is hosted on AWS (region: `ap-southeast-1` for Vercel Postgres by default — verify with Vercel/Neon console). Australian data residency is not confirmed.
- **Access:** Vercel project team members with production environment access can see `POSTGRES_URL`. Limit Vercel project access to authorised staff.
- **Encryption:** Neon encrypts data at rest and in transit (TLS). Connection string uses `sslmode=require`.
- **Backups:** Neon provides point-in-time recovery. Verify backup retention period meets business requirements (suggest minimum 30 days).
- **Contractual:** Verify Neon and Vercel data processing agreements are in place for Australian privacy law compliance (Privacy Act 1988, APP 8 cross-border disclosure).

**Action required before production:** Confirm data residency and obtain legal sign-off on cross-border transfer if data is stored outside Australia.

---

## 5. Formspree — data handling

- Formspree receives HUMAN_REVIEW notification payloads (reference ID + subject only).
- For other queues, Formspree receives name + safe contact prefs + category (no contact detail).
- Formspree stores submitted data on its own infrastructure. Verify Formspree's data retention and deletion policies.
- Formspree is a US-based service. APP 8 cross-border disclosure applies.
- **Action required:** Confirm whether existing Formspree account/plan permits this use, and obtain legal review of data shared with Formspree.

---

## 6. Privacy notice and consent

- The current form collects consent via `privacy_consent` checkbox (required) and `accuracy_declaration`.
- The consent version is stored (`consent_version = '2026-10-v1'`).
- **Action required before production:** Update the site's privacy policy to disclose:
  - What data is collected via the enquiry form.
  - Where it is stored (Neon/Vercel Postgres; Formspree for notifications).
  - Who can access it (mediators and admin staff; Formspree).
  - Retention periods and deletion process.
  - Right to access and erasure under the Privacy Act 1988.
  - Obtain qualified Australian privacy law review before activation.

---

## 7. Retention and deletion

**No automated retention enforcement is currently implemented.**

Proposed retention periods (for human review and approval — not legal advice):

| Data | Suggested retention | Mechanism |
|------|--------------------|----|
| Contact details (enquiry_contacts) | 12 months from submission or closure of matter | Manual delete of row |
| Routing/operational data (enquiries) | 24 months for operational reporting | Manual delete or archival |
| Audit log | 24 months | Manual delete |
| IP address (audit_log.actor) | 90 days | Manual delete or anonymise actor field |

**Action required:** Define and document retention periods with legal review; implement automated enforcement before public launch.

---

## 8. Residual risks classified

| Risk | Classification | Mitigation |
|------|---------------|------------|
| No Australian data residency confirmed | P1 | Verify with Neon/Vercel; obtain legal sign-off |
| No privacy policy update | P0 | Must be done before activation |
| ADMIN_SECRET shared key still present | P1 | Disable before launch; migrate all users to ADMIN_USERS |
| No key rotation mechanism | P2 | Implement rotation procedure in staff operations |
| Formspree contractual review not done | P1 | Legal review required |
| No automated retention enforcement | P2 | Manual process sufficient for pilot |
| Admin API keys long-lived | P2 | Rotation procedure in staff operations doc |
| No rate limiting on admin API | P2 | Admin API is key-authenticated; lower priority |

