# Staff Intake Runbook — Mediations Australia Enquiry System
**Version:** Stage D / 2026-10-13  
**Applies to:** Reception, intake coordinators, senior practitioners

---

## 1. Accessing the admin queue

**Endpoint:** `GET https://mediationsaustralia.com.au/api/enquiry-admin?view=list`  
**Auth:** `Authorization: Bearer <your-key>` (from Dan — individual per staff member)

Filter by queue:
```
?queue=HUMAN_REVIEW
?queue=PRIORITY_INTAKE
?queue=GENERAL_INTAKE
```

Retrieve full lead detail:
```
GET /api/enquiry-admin?view=detail&id=<submission_id>
```

---

## 2. Queue handling

### HUMAN_REVIEW (act within 2 hours during business hours)
- Safety flag, urgent court date, or elder capacity concern.
- **Do NOT send email or call without safe-contact check.**
- Check `safe_email`, `safe_phone`, `safe_voicemail` flags in the detail record.
- If `safe_email=false` and `safe_phone=false` — contact by post only or await their call.
- Escalate to senior practitioner before any external contact.
- Formspree notification: reference ID and "URGENT REVIEW REQUIRED" subject only — no client detail in the notification email.

### ACCESS_REVIEW
- Family matter with financial hardship indicator.
- Confirm eligibility via the existing Access Mediation pathway before quoting fees.
- Do not promise Access pricing without practitioner review.

### PUBLIC_SERVICE_INFORMATION
- Enquirer indicated need for free/community services.
- Provide referral information. Do not attempt paid intake without explicit consent.

### PREPARATION_NURTURE
- Financial disclosure or legal advice outstanding.
- Send information on preparation steps. Do not schedule mediation until preparation confirmed.

### PRIORITY_INTAKE
- Both parties willing, matter ready, standard fee. Proceed with intake call.
- Confirm details and book initial consultation.

### ENGAGE_OTHER_PARTY (internal — do not contact Party B directly)
- Party B status not confirmed.
- Contact the enquirer first to understand Party B's position before any outreach.

### GENERAL_INTAKE
- Standard triage. Review and assign within 1 business day.
- If `financial_hardship_flag` tag is present — discuss fee options before routing.

---

## 3. Safe-contact protocol for HUMAN_REVIEW

Before any contact with a HUMAN_REVIEW enquirer:
1. Retrieve full record: check `safe_email`, `safe_phone`, `safe_voicemail`, `preferred_contact_time`.
2. If `safe_email=false` — do not email to their address under any circumstances.
3. If `safe_voicemail=false` — do not leave a voicemail.
4. If `safe_phone=false` — do not call their number.
5. Use only the contact method they confirmed safe.
6. Never contact Party B without the enquirer's explicit knowledge and consent.
7. Document all contact attempts in the queue notes via PATCH override.

---

## 4. Queue override (reassign a lead)

```
PATCH /api/enquiry-admin
Content-Type: application/json
Authorization: Bearer <admin-key>

{
  "submission_id": "<uuid>",
  "queue": "PRIORITY_INTAKE",
  "notes": "Hardship confirmed — Access not applicable. Moving to standard intake."
}
```

Only `admin`-role keys can override. `viewer`-role keys return 403.  
All overrides are logged with your name and timestamp.

---

## 5. Failed notification recovery

A lead with `formspree_notified=false` in the list view means the staff email was not delivered.

Steps:
1. Identify the `submission_id` from the list (`?queue=<any>`, check `formspree_notified` field).
2. Retrieve full detail via `view=detail`.
3. Action the lead manually using the information in the detail record.
4. Optionally add a note via PATCH: `"notes": "Manual notification actioned — Formspree failed"`.

The lead is NOT lost — it is in Neon. The failure is a notification-only problem.

---

## 6. V1 Quick Enquiry reconciliation

V1 Quick Enquiry submissions (the short form above the guided form) post directly to Formspree and are NOT in the Neon admin queue.

**Current procedure (until V2 is the only active form):**
- Monitor the Formspree inbox for the original endpoint (separate from `mnpjbroe`).
- V1 leads have no reference ID — use name + email to identify.
- Log any V1 enquiry that progresses to consultation manually.
- Do not copy V1 contact details into Neon without a privacy assessment.

**Decision point for operator:** confirm whether to deactivate V1 after a defined period once V2 is established.

---

## 7. Reference ID lookup

Every V2 submission returns `MA-ENQ-XXXXXXXX` to the enquirer.  
Look up by reference: extract the 8-character hex, find the `submission_id` in the list that starts with those characters (case-insensitive).

---

## 8. End-of-day exception check

Before end of business:
1. Check `HUMAN_REVIEW` queue for any unactioned items.
2. Check `notification_attempts > 1` or `formspree_notified=false` in recent records.
3. Check `PRIORITY_INTAKE` for items older than 4 hours without an owner assigned.

---

## 9. Key management

- Individual Bearer keys are issued by Dan.
- If your key is compromised: notify Dan immediately for revocation and re-issue.
- Do not share your key with colleagues — each person must have their own.
- Do not embed keys in browser bookmarks, scripts, or shared documents.
