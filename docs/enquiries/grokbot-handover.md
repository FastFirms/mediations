# GrokBot Handover — Integration Specification

**Branch:** feature/enquiry-form-stage-b
**Date:** 2026-10-13
**Status:** Specification and mocks only. GrokBot tools/permissions are not available in this repository. No live integration is implemented.

---

## 1. Purpose

GrokBot acts as a preparation layer between the enquiry routing system and human staff.
It reads structured submissions, prepares handover summaries and draft acknowledgements,
and creates follow-up tasks. It does not determine suitability, send messages autonomously,
or replace human review.

Operating principle: GrokBot prepares; humans decide and send.

---

## 2. Data feed — authenticated admin API

GrokBot polls or is triggered to call:

  GET /api/enquiry-admin?view=list&limit=50&offset=0

Authorization: Bearer <grokbot-key>   (viewer role — read-only)

GrokBot uses submission_id as its deduplication key. It must not process a submission_id
it has already handled (idempotent processing).

For full detail before preparing a handover:

  GET /api/enquiry-admin?view=detail&id=<submission_id>

---

## 3. Queue-to-action map

| Queue | GrokBot action | Restrictions |
|-------|---------------|-------------|
| HUMAN_REVIEW | Escalate via secure internal channel only. No draft email. No external action. | Never generate or send external draft for HUMAN_REVIEW. |
| ACCESS_REVIEW | Prepare Farley handover summary for Access Mediation staff. No draft email without explicit safe_email=true and safety_flag=no. | Confirm with Access staff before any contact. |
| PUBLIC_SERVICE_INFORMATION | Prepare referral summary (NADRAC, Legal Aid, community centre options by state). Draft email only if safe_email=true and safety_flag=no. | |
| PREPARATION_NURTURE | Prepare nurture sequence draft. Do not send. Hold for human review. | |
| PRIORITY_INTAKE | Prepare Farley handover + neutral acknowledgement draft (Gmail draft only). | Draft only — human approves before sending. |
| ENGAGE_OTHER_PARTY | Prepare internal handover summary. No contact with other party. | Never draft message to other party from enquirer details. |
| GENERAL_INTAKE | Standard intake handover summary. Fee hardship flag triggers staff note. | Check financial_hardship_flag tag. |

---

## 4. Farley handover format (mock)

For each permitted queue, GrokBot prepares a concise internal handover:

  Ref:        MA-ENQ-XXXXXXXX
  Category:   family_parenting
  Location:   Sydney NSW
  Delivery:   Online preferred
  Timing:     Urgent
  Party B:    Open to discussion
  Fee:        Standard private
  Stage:      Proceedings started
  Action:     PRIORITY_INTAKE — schedule initial consultation call

Fields included: submission_id, matter_category, state, city, delivery_preference,
timing, party_b_status, fee_preference, stage, operational_queue, review_reasons, tags.

Fields never included in handover: name, email, phone, message, safety_flag detail,
free-text narratives.

---

## 5. Draft acknowledgement rules

GrokBot may prepare a Gmail draft acknowledgement (not send) only when ALL of the following apply:

- operational_queue is NOT HUMAN_REVIEW
- safe_email = true
- safety_flag = no
- Email address is present in enquiry_contacts

The draft must:
- Reference the submission reference (MA-ENQ-XXXXXXXX)
- Use the enquirer's name from enquiry_contacts
- NOT include: case details, category, safety context, fee bands, legal advice, guaranteed outcomes, response time commitments
- NOT ask for information already supplied in the form
- Be neutral in tone: "We have received your enquiry and a member of our team will be in touch."

GrokBot must not send, forward, archive, delete or auto-reply. Draft creation only.

---

## 6. Follow-up task creation

For each new submission, GrokBot may create one internal follow-up task:
- Reference ID
- Queue and recommended action
- Preferred contact time (from enquiry)
- No sensitive narrative

Task must NOT be created for HUMAN_REVIEW — those are escalated through a secure internal channel only.

---

## 7. Daily summaries

GrokBot may produce daily queue summary reports (internal only):
- Unique enquiries by queue and form variant
- Enquiries with formspree_notified=false (undelivered notifications — requires attention)
- Overdue items (no queue override recorded within defined SLA per queue)

Summary must not include names, contact details or safety narratives.

---

## 8. Idempotency and failure handling

- GrokBot tracks processed submission_ids externally. Never re-process.
- If admin API returns 401/403, alert system administrator. Do not retry with different key.
- If admin API returns 503, wait and retry with exponential backoff (max 3 attempts).
- If draft creation fails, log failure and alert staff. Do not silently drop.

---

## 9. What GrokBot must never do (non-negotiable)

- Determine professional suitability for mediation.
- Issue Section 60I certificates or advise on legal rights or deadlines.
- Assess family violence risk as safe.
- Contact the other party (Party B) autonomously.
- Send, forward or archive any message without explicit human approval.
- Send automatic nurture messages after seven days.
- Create or send any draft for HUMAN_REVIEW submissions.
- Create or send any draft where safe_email=false or safety_flag=yes.
- Quote binding prices or schedule confirmed mediations.
- Forward raw sensitive narratives to Gmail or any external service.

---

## 10. Interface contract

Input: Admin API responses (viewer role). No direct database access.
Output: Internal handover documents, Gmail drafts (held), follow-up tasks, daily summaries.
Auth: Viewer-role Bearer key stored in GrokBot's secure credential store. Not hardcoded.
Frequency: On-demand or polling (suggest every 15 minutes during business hours).
Data minimisation: GrokBot works with operational metadata only. Contact details are retrieved only when needed to prepare a compliant draft and are not stored in GrokBot's own database.
