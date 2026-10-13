# Enquiry System — Staff Operational README

> For the Mediations Australia multi-step guided enquiry form (V2).  
> Last updated: 2026-10-13 | Branch: feature/enquiry-form-stage-b

---

## 1. Operational queues

Every guided-form submission is routed deterministically to one of seven queues in this priority order:

| Priority | Queue | Who handles it | Trigger |
|----------|-------|----------------|---------|
| 1 | **HUMAN_REVIEW** | Senior mediator + admin | Active proceedings, violence flag, court date, court order, supervised-contact, urgent child safety |
| 2 | **ACCESS_REVIEW** | Rostered Access Mediation staff | Family + genuine financial hardship (need_free_service or subsidised); approved by existing Access system |
| 3 | **PUBLIC_SERVICE_INFORMATION** | Reception / info team | Need-free-service but not family (refer to NADRAC, Legal Aid, community centres) |
| 4 | **PREPARATION_NURTURE** | Email/drip sequence | Early-stage enquiry; not ready to book; no urgent flag |
| 5 | **PRIORITY_INTAKE** | Senior intake coordinator | Family matters that passed all higher gates — ready to book |
| 6 | **ENGAGE_OTHER_PARTY** | Intake coordinator | Other party has not yet been approached — support needed before booking |
| 7 | **GENERAL_INTAKE** | Standard intake | Non-family matters, or financial hardship (non-family) flagged for fee assessment |

**GENERAL_INTAKE with `financial_hardship_flag` tag** means a workplace or commercial enquiry indicated financial hardship. Do not quote standard fees without checking with senior staff.

---

## 2. Viewing submissions

### Admin API endpoint

```
GET /api/enquiry-admin?view=list
GET /api/enquiry-admin?view=list&queue=HUMAN_REVIEW
GET /api/enquiry-admin?view=detail&id=<submission_id>
```

**Authentication:** Bearer token in the `Authorization` header.  
Example with curl:
```bash
curl -H "Authorization: Bearer <your-key>" \
  "https://mediationsaustralia.com.au/api/enquiry-admin?view=list&queue=HUMAN_REVIEW"
```

### Keys and roles

Keys are set in the Vercel `ADMIN_USERS` environment variable (JSON array). Contact the system administrator to request a key.

| Role | What it can do |
|------|----------------|
| `admin` | View all queues + override queue assignment |
| `viewer` | View all queues only (read-only) |

**Keys are personal.** Do not share your key. Keys are never visible in the browser or in Formspree notifications.

---

## 3. HUMAN_REVIEW notifications

When a submission routes to HUMAN_REVIEW, Formspree sends a notification email with:
- Subject: `URGENT REVIEW REQUIRED — Ref: MA-ENQ-XXXXXXXX`
- Body: the submission reference ID and queue name only — **no personal details, no name, no email**

To retrieve the full submission (including contact details):
1. Note the reference ID from the notification subject.
2. Query the admin API: `GET /api/enquiry-admin?view=list&queue=HUMAN_REVIEW`
3. Find the matching submission and note its `submission_id`.
4. Fetch full details: `GET /api/enquiry-admin?view=detail&id=<submission_id>`

Contact details (name, email, phone) are in the `contact` object of the detail response. They are never sent via Formspree.

**Why this design?** Sensitive enquiries (proceedings, violence flags) must not transit email in identifiable form. The reference ID is enough to retrieve the full record securely.

---

## 4. Queue overrides

An admin-role user can manually move a submission to a different queue:

```bash
curl -X PATCH \
  -H "Authorization: Bearer <admin-key>" \
  -H "Content-Type: application/json" \
  -d '{"submission_id":"<uuid>","queue":"PRIORITY_INTAKE","notes":"Client confirmed ready to book"}' \
  "https://mediationsaustralia.com.au/api/enquiry-admin"
```

Every override is recorded in the audit log with your username and the reason you provided. Overrides are permanent (no undo via API) — call the endpoint again with the correct queue if you made an error.

---

## 5. Access Mediation (ACCESS_REVIEW)

The Access Mediation eligibility and capacity check is handled by the **existing approved system** — the form does not bypass it. Submissions entering ACCESS_REVIEW have indicated family matters with genuine financial hardship. Staff must still verify eligibility and capacity through the normal Access process before confirming a booking.

The enquiry system does not communicate availability or capacity to the applicant.

---

## 6. Data retention and privacy

| Table | Contents | Sensitivity |
|-------|----------|-------------|
| `enquiries` | Routing data, answers, tags, timeline | Low — no personal details |
| `enquiry_contacts` | Name, email, phone, message | **Restricted** — contact details only |
| `enquiry_branch_answers` | Detailed question answers | Medium |
| `enquiry_audit_log` | Queue changes, actors, reasons | Internal |

**Retention:** No automated deletion is currently configured. Review submissions older than 12 months periodically and delete contact records for closed matters.

**Right to erasure:** To delete a contact record without deleting the submission record, delete the row from `enquiry_contacts` where `enquiry_submission_id = <uuid>`. The `enquiries` row (routing data) can remain for operational reporting.

---

## 7. Escalation

| Situation | Action |
|-----------|--------|
| HUMAN_REVIEW notification not received within 1 hour of expected submission | Check `formspree_notified` column in `enquiries`; contact system administrator if `false` |
| Routing appears wrong | Use admin API to check the `review_reasons` and `tags` fields; override if needed |
| Database unreachable | Submissions fail with a user-facing error message; no data is silently lost |
| Rate limit hit by legitimate user | Rate limit is 5 submissions per 15-minute window per IP; contact administrator to investigate |
| Sensitive matter in wrong queue | Move to HUMAN_REVIEW via PATCH override immediately; note reason |

---

## 8. Rate limiting

The system allows 5 submissions per 15-minute window per IP address. If Neon (the database) is temporarily unavailable, an in-memory fallback rate limiter activates — responses will include the header `X-Rate-Limit-Mode: memory-fallback`. This is a degraded-service state; contact the system administrator if it persists.

---

## 9. Checking notification delivery

To find submissions where the Formspree notification was not sent:

```sql
SELECT submission_id, operational_queue, submitted_at
FROM enquiries
WHERE NOT formspree_notified
  AND operational_queue = 'HUMAN_REVIEW'
ORDER BY submitted_at DESC;
```

If `formspree_notified = false` for a HUMAN_REVIEW submission, manually retrieve the submission via the admin API and follow up directly.

---

## 10. Environment variables (for system administrator)

| Variable | Purpose | Required |
|----------|---------|----------|
| `POSTGRES_URL` | Neon database connection (Vercel Postgres) | Yes |
| `FORMSPREE_ENDPOINT` | Formspree form URL for HUMAN_REVIEW notifications | Yes |
| `ADMIN_USERS` | JSON array of per-user admin keys and roles | Recommended |
| `ADMIN_SECRET` | Legacy single shared admin key (fallback) | Optional |
| `ENQUIRY_FORM_V2` | Set to `1` at build time to enable guided form | Yes (build env) |

Variables are set in the Vercel project dashboard. Never commit these to the repository.
