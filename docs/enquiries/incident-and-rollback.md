# Incident and Rollback Procedures
**Version:** Stage D / 2026-10-13  
**Applies to:** Enquiry form V2, admin API, GrokBot bridge

---

## 1. Rollback the enquiry form (revert to V1 only)

If V2 causes problems, the V1 Quick Enquiry form remains on the page and is fully operational. V2 can be disabled without a code deploy by:

1. Remove or set `ENQUIRY_FORM_V2=0` in Vercel Production env.
2. Rebuild the static site (`python3 build/gen_enquiry.py`) and push.
3. V1 Quick Enquiry continues to post to the original Formspree endpoint.
4. Neon data is not affected — records already written are preserved.

**To roll back the code entirely:**
```bash
git revert <merge-commit-sha> --no-edit
git push origin main
```
Vercel redeploys automatically. No DNS change required.

---

## 2. Neon database incident

### Enquiry form returning 503
- Expected behaviour when Neon is unreachable.
- Visitors see: "Please call (02) 7227 7373 or email hello@mediationsaustralia.com.au."
- No data is lost — no write was attempted.
- Monitor Neon status at [neon.tech/status].
- When Neon recovers, form resumes automatically.

### Data corruption or accidental deletion
- Neon provides automated daily backups. Contact Neon support to restore.
- Do not attempt manual SQL restoration without DBA involvement.
- The `enquiry_audit_log` table is the source of truth for what events occurred.

---

## 3. Formspree notification failure

- Lead is in Neon with `formspree_notified=false`.
- Lead is NOT lost.
- Staff: check admin queue for `formspree_notified=false` items daily.
- Action manually using the detail record.
- Add a note via PATCH: `"notes": "Manual action — notification failed"`.
- If Formspree is down: check [formspree.io/status].

---

## 4. Admin API key compromise

If an `ADMIN_USERS` key is compromised:
1. Notify Dan immediately.
2. Remove the compromised key from `ADMIN_USERS` in Vercel env.
3. Issue a new key: `openssl rand -hex 32`.
4. Update `ADMIN_USERS` with the new key and redeploy.
5. Check `enquiry_audit_log` for `actor=<compromised-user-name>` to audit what was accessed.

If `ADMIN_SECRET` (shared fallback) is compromised:
1. Remove `ADMIN_SECRET` from Vercel env immediately.
2. Ensure `ADMIN_USERS` is set with individual keys for all active staff.
3. Redeploy.

---

## 5. GrokBot token compromise

If `AGENT_INTAKE_TOKEN` is compromised:
1. Generate a new token: `openssl rand -hex 32`.
2. Update `AGENT_INTAKE_TOKEN` in Vercel Production env.
3. Redeploy (env var change takes effect on next invocation).
4. Provide the new token to the GrokBot operator.
5. Check `enquiry_audit_log` for `event_type=AGENT_INTAKE_ACCESS` to audit recent access.
6. The bridge returns no contact details or restricted lead content — exposure is limited to operational queue metadata.

---

## 6. HUMAN_REVIEW enquiry sent to wrong channel

If a HUMAN_REVIEW lead is exposed to an automated agent or general notification:
1. Identify the `submission_id` immediately.
2. Check what data was exposed: the bridge returns only `reference`, `operational_queue: HUMAN_REVIEW`, and `restricted: true` — no name, contact, or category.
3. If additional detail was exposed via another route (e.g., admin API misuse): notify the affected person's data contact and assess under the Privacy Act.
4. Log the incident in `enquiry_audit_log` manually via a direct database insert (contact Dan for access).
5. Review and tighten access controls.

---

## 7. Safety-flagged enquiry contacted via unsafe method

If a person with `safe_email=false` or `safe_phone=false` is contacted via that method:
1. Stop all further contact immediately.
2. Escalate to senior practitioner.
3. Assess whether the person may be at risk as a result of the unsafe contact.
4. Follow family violence safety protocols as directed by the senior practitioner.
5. Document in the audit log.

---

## 8. Known rollback constraints

- Rolling back the database schema is destructive — do not drop tables without a verified backup.
- Rolling back the code does not roll back Neon data — submitted enquiries remain.
- V1 and V2 can operate in parallel safely — disabling V2 does not affect V1.
