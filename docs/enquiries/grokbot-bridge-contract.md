# GrokBot Bridge — Integration Contract
**Version:** Stage D / 2026-10-13  
**Status:** Specification and implementation complete; live integration pending operator approval  
**Endpoint:** `GET /api/agent-intake`

---

## Purpose

Provide a narrow, read-only, authenticated feed of new enquiries to an authorised intake agent (GrokBot). GrokBot prepares draft responses and handover summaries for human review — it does not send, decide, or act autonomously.

---

## Authentication

**Method:** Bearer token  
**Header:** `Authorization: Bearer <AGENT_INTAKE_TOKEN>`  
**Token source:** `AGENT_INTAKE_TOKEN` environment variable (Vercel Production)  
**Generate:** `openssl rand -hex 32`  
**Revocation:** Remove or rotate the env var and redeploy.

GrokBot must store the token as a secret, never in browser JS, logs, or version control.

---

## Endpoint

```
GET /api/agent-intake
Authorization: Bearer <token>
```

### Query parameters

| Param | Type | Default | Notes |
|---|---|---|---|
| `cursor` | ISO 8601 timestamp | last 24 hours | Returns records `submitted_at > cursor` (exclusive, ascending) |
| `limit` | integer 1–50 | 20 | Max 50 per request |

### Rate limit

60 requests per hour. `429` response if exceeded.

---

## Response format

```json
{
  "items": [...],
  "next_cursor": "2026-10-13T10:45:00.000Z",
  "restricted_count": 1,
  "count": 5
}
```

`next_cursor` is the `submitted_at` of the last item — pass as `cursor` in the next request.  
`restricted_count` shows how many items in this page are restricted (HUMAN_REVIEW).  
`next_cursor` is `null` when there are no more records in this window.

---

## Item shapes

### Non-restricted lead

```json
{
  "submission_id": "7535cab5-9201-4184-b6b6-193e3e5dfca4",
  "reference": "MA-ENQ-7535CAB5",
  "operational_queue": "PRIORITY_INTAKE",
  "matter_category": "family_parenting",
  "timing": "flexible",
  "delivery_preference": "either",
  "safe_email": true,
  "safe_voicemail": true,
  "safe_phone": false,
  "preferred_contact_time": null,
  "formspree_notified": true,
  "notification_attempts": 1,
  "notification_last_error": null,
  "tags": [],
  "submitted_at": "2026-10-13T00:33:00.000Z"
}
```

### HUMAN_REVIEW or safety-flagged lead

```json
{
  "submission_id": "abcd1234-...",
  "reference": "MA-ENQ-ABCD1234",
  "operational_queue": "HUMAN_REVIEW",
  "restricted": true,
  "submitted_at": "2026-10-13T01:00:00.000Z"
}
```

**No name, email, phone, message, category, or safety detail is returned for restricted leads.**

---

## What GrokBot may do with this data

| Action | Permitted | Notes |
|---|---|---|
| Deduplicate by `submission_id` | ✅ | Use as idempotency key |
| Prepare Farley handover summary | ✅ | Non-restricted fields only |
| Prepare acknowledgement **draft** | ✅ | Draft only; human must approve before sending |
| Use `safe_email`/`safe_voicemail`/`safe_phone` to choose draft channel | ✅ | |
| Send any email or message automatically | ❌ | Never |
| Contact Party B | ❌ | Never |
| Access contact details (name, email, phone) | ❌ | Not returned by this endpoint |
| Access HUMAN_REVIEW narrative | ❌ | Restricted item returns reference only |
| Make routing or suitability decisions | ❌ | Server routing is authoritative |
| Schedule confirmed mediation | ❌ | Requires separate integration approval |

---

## Idempotency contract

GrokBot must track processed `submission_id` values. The cursor guarantees no item is returned twice in sequential calls, but GrokBot should deduplicate by `submission_id` as a safety net in case of retry or replay.

---

## Failure handling

| Scenario | GrokBot action |
|---|---|
| `503` database unavailable | Retry after 5 minutes; do not alert as a new enquiry |
| `429` rate limited | Back off 60 seconds; reduce polling frequency |
| `401` unauthorised | Stop and alert operator — token may have been rotated |
| Empty `items` array | No new enquiries; advance cursor and wait |
| `restricted: true` item | Log reference only; escalate to human via internal channel |

---

## Access logging

Every request is logged to `enquiry_audit_log` with `event_type: 'AGENT_INTAKE_ACCESS'` and the cursor and row count.

---

## V1 Formspree-only leads

V1 Quick Enquiry submissions are NOT available via this endpoint. GrokBot must not attempt to ingest V1 leads from Formspree directly. V1 monitoring remains a manual staff task until a unified V2-only form is confirmed.

---

## Not implemented in this stage

The following require a separate integration approval:
- Gmail draft creation
- Gmail sending
- Party B outreach
- CRM writes
- Confirmed mediation scheduling
- Privileged detail retrieval for draft generation (requires per-request staff approval)
