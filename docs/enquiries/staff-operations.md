# Staff Operations — Enquiry System

**Branch:** feature/enquiry-form-stage-b
**Date:** 2026-10-13

---

## 1. Retrieving a lead by reference ID

Every submission generates a reference in the format MA-ENQ-XXXXXXXX.

Endpoints (Authorization: Bearer <your-key> required):
- GET /api/enquiry-admin?view=list
- GET /api/enquiry-admin?view=list&queue=HUMAN_REVIEW
- GET /api/enquiry-admin?view=detail&id=<submission_id>

Detail response fields:
- enquiry: routing data, category, stage, timing, safe contact preferences
- contact: name, email, phone, message (restricted)
- branch_answers: question-specific answers
- audit_log: queue changes with actor, reason, timestamp

---

## 2. Seven operational queues

HUMAN_REVIEW: Safety flag, court date, urgent deadline, elder capacity. Senior mediator. Personal contact using safe contact preferences. No auto-email.

ACCESS_REVIEW: Family + genuine hardship. Access Mediation staff. Check capacity and eligibility via existing Access system first. Do not confirm eligibility.

PUBLIC_SERVICE_INFORMATION: Needs free service (non-family). Reception. Refer to NADRAC, Legal Aid, community centres.

PREPARATION_NURTURE: Early-stage; disclosure or legal prep outstanding. Email coordinator. Nurture sequence, no booking offer yet.

PRIORITY_INTAKE: Both parties willing, ready, standard fee. Senior intake coordinator. Book initial call or send fee schedule.

ENGAGE_OTHER_PARTY: Other party not yet approached (internal queue only). Intake coordinator. Support enquirer to approach other party. Do not contact other party directly.

GENERAL_INTAKE: All other cases; non-family hardship flagged. Standard intake. Check financial_hardship_flag tag before quoting fees.

HUMAN_REVIEW safe contact protocol:
1. Check safe_email, safe_voicemail, safe_phone and preferred_contact_time in detail response.
2. Use only contact methods marked true.
3. If safe_email=false, do not send email.
4. If safe_voicemail=false, do not leave a voicemail.
5. If no safe contact method is available, escalate to senior mediator before any attempt.

---

## 3. Queue override (admin role required)

PATCH /api/enquiry-admin with JSON body:
  {"submission_id":"<uuid>","queue":"PRIORITY_INTAKE","notes":"Reviewed — parties ready"}

Every override is recorded in the audit log with your name, target queue, and reason.

---

## 4. Key management

Keys are set by the system administrator in Vercel (ADMIN_USERS environment variable).

Rotation: every 90 days or immediately when a staff member leaves.
1. Administrator generates new key: openssl rand -hex 32
2. Updates ADMIN_USERS in Vercel and redeploys
3. Old key is invalid after redeploy

Never share your key. Never put it in a URL, email, or support ticket.

---

## 5. Failed HUMAN_REVIEW notifications

If a Formspree email is not received within 30 minutes, the submission is still safe in Neon. Check via direct DB access:
- formspree_notified = false means delivery failed
- notification_attempts: how many attempts (max 2)
- notification_last_error: http_4xx, http_5xx, or network_error

Retrieve submission via admin API using any available reference ID.

---

## 6. Access Mediation scope

This system identifies ACCESS_REVIEW candidates. It does not assert eligibility, check capacity, communicate availability, or bypass the existing Access eligibility assessment. All ACCESS_REVIEW enquiries must go through the standard Access process before any booking.

---

## 7. Escalation

HUMAN_REVIEW notification missing: Check Vercel function logs; retrieve via admin API.
Submission in wrong queue: PATCH to correct queue with reason note.
Contact safety uncertain: Senior mediator to assess before any contact.
Rate limit on legitimate user: Contact system administrator.

---

## 8. Deletion and access requests

Delete contact details (direct DB access via system administrator):
  DELETE FROM enquiry_contacts WHERE enquiry_submission_id = '<uuid>';

Anonymise IP in audit log:
  UPDATE enquiry_audit_log SET actor = 'anonymised' WHERE enquiry_submission_id = '<uuid>' AND event_type = 'SUBMITTED';

The enquiries routing record may be retained for operational reporting after contact details are deleted.
