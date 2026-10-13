# Stage C — Form Acceptance Testing

**Branch:** `feature/enquiry-form-stage-b`  
**Environment:** Static file preview (`file://`) + code inspection  
**Date:** 2026-10-13

---

## Test matrix — guided form branches

| # | Scenario | Steps taken | Expected queue | Actual result | Status |
|---|----------|-------------|----------------|---------------|--------|
| G1 | Family parenting + court_date stage | category=family_parenting, stage=court_date | HUMAN_REVIEW | HUMAN_REVIEW | ✓ |
| G2 | Family + safety_flag=yes | category=family_parenting, safety_flag=yes | HUMAN_REVIEW | HUMAN_REVIEW | ✓ |
| G3 | Family + need_free_service | category=family_parenting, fee=need_free_service | PUBLIC_SERVICE_INFORMATION | PUBLIC_SERVICE_INFORMATION | ✓ |
| G4 | Family parenting + standard_fee_hardship | family_parenting, fee=standard_fee_hardship | ACCESS_REVIEW | ACCESS_REVIEW | ✓ |
| G5 | Family property + standard_fee_hardship | family_property, fee=standard_fee_hardship | ACCESS_REVIEW | ACCESS_REVIEW | ✓ |
| G6 | Workplace + standard_fee_hardship | workplace_employment, fee=standard_fee_hardship | GENERAL_INTAKE + financial_hardship_flag | GENERAL_INTAKE + financial_hardship_flag | ✓ |
| G7 | Commercial + standard_fee_hardship | commercial_business, fee=standard_fee_hardship | GENERAL_INTAKE + financial_hardship_flag | GENERAL_INTAKE + financial_hardship_flag | ✓ |
| G8 | Family, party agreed, discussing stage | family_parenting, party_b=agreed, stage=discussing, fee=standard_private | PRIORITY_INTAKE | PRIORITY_INTAKE | ✓ |
| G9 | Family, party not asked | family_parenting, party_b=not_asked | ENGAGE_OTHER_PARTY | ENGAGE_OTHER_PARTY | ✓ |
| G10 | Commercial, not_applicable other party | commercial_business, party_b=not_applicable, stage=ready_to_arrange | PRIORITY_INTAKE | PRIORITY_INTAKE | ✓ (not_applicable → PRIORITY_INTAKE, not ENGAGE) |
| G11 | Family, party declined | family_parenting, party_b=declined, fee=standard_private | GENERAL_INTAKE | GENERAL_INTAKE | ✓ |
| G12 | Family property, disclosure not started + no legal advice | family_property, branch_answers.disclosure_readiness=not_started, legal_advice=neither | PREPARATION_NURTURE | PREPARATION_NURTURE | ✓ (code verified) |
| G13 | Elder family + capacity_concern=yes | elder_family, branch_answers.capacity_concern=yes | HUMAN_REVIEW | HUMAN_REVIEW | ✓ (code verified) |
| G14 | Urgent timing + proceedings started | family_parenting, timing=urgent, stage=proceedings_started | HUMAN_REVIEW (urgent_deadline) | HUMAN_REVIEW | ✓ |
| G15 | General other_unsure category | other_unsure | GENERAL_INTAKE | GENERAL_INTAKE | ✓ |

All 21 routing cases (including G1–G15 plus permutations) pass deterministic routing engine.

---

## Form behaviour tests

| # | Test | Method | Expected | Actual | Status |
|---|------|--------|----------|--------|--------|
| F1 | Back button hidden on Step 0 | JS: `getComputedStyle(backBtn).display` | `none` | `none` | ✓ |
| F2 | Next without selection shows error | JS: click Next before any radio selected | "Please make a selection to continue." | "Please make a selection to continue." | ✓ |
| F3 | Multi-question step (delivery + timing) | JS: step 4 radios | Both groups present | Both groups present | ✓ |
| F4 | Safety notice on safety_flag=yes | JS: click Yes radio | `enq-safety-notice` visible | Visible, correct text | ✓ |
| F5 | Safety notice hidden on safety_flag=no | JS: click No radio | Notice hidden | Hidden | ✓ |
| F6 | GA4 `enquiry_started` fires on form open | JS: intercept gtag | `{form_variant:'guided'}` | Event captured | ✓ |
| F7 | GA4 `step_completed` fires on step advance | Code inspection | `{step_index:idx}` | Added to _renderStep | ✓ (code) |
| F8 | GA4 `enquiry_submitted` fires on submit | Code inspection | `{operational_queue:...}` | Present at line 591 | ✓ (code) |
| F9 | sessionStorage prefill: key read and cleared | Code inspection | Category pre-selected, key removed | `sessionStorage.removeItem('ma_quiz_category')` | ✓ (code, data: URL blocks live test) |
| F10 | Mobile viewport stacking | Browser resize <768px | Columns stack, no horizontal scroll | Stacked correctly | ✓ |
| F11 | Back navigation preserves step state | Manual click through | Previously selected radio re-checked | State preserved in `_state.answers` | ✓ |
| F12 | No sensitive data in URL parameters | Code inspection | Attribution from URL params only (utm_*) | Only utm_source/medium/campaign/landing captured | ✓ |
| F13 | No response-time promise in confirmation | Code inspection | No "1 business day" etc. | "A member of our team will review your enquiry and be in touch." | ✓ |
| F14 | Honeypot silent pass | JS: set _hp value | Returns 200 `{ok:true, reference:'MA-ENQ-BLOCKED'}` | Silent pass (code verified) | ✓ |
| F15 | Neon unavailable → truthful error | Code inspection | 503 with phone number, no false success | 503: "We could not save your enquiry right now. Please call us on (02) 7227 7373" | ✓ |

---

## Keyboard navigation (code inspection — requires live HTTP server for full test)

| Element | Expected behaviour | Code evidence |
|---------|-------------------|---------------|
| Radio inputs | Wrapped in `<label>` — click on label activates radio | `_radioStep()` wraps each `<input type=radio>` in `<label>` |
| Back/Next/Submit buttons | Standard `<button>` — keyboard accessible by default | Semantic `<button>` elements |
| Form inputs (name, email etc.) | Standard `<input>` with labels | `<label>` elements present in final step |
| Error messages | `role="alert"` + `aria-live="polite"` on `#enq-error` | `role="alert"` present at line 171 |
| Safety notice | Appears in DOM flow, not modal — accessible without focus trap | Standard `<div>` visibility toggle |

**Outstanding:** Full keyboard navigation test (tab order through all steps, Enter to submit) requires a running HTTP server with VoiceOver or NVDA. Not possible in `file://` preview.

---

## V1 fallback (quick enquiry)

| Test | Result |
|------|--------|
| Quick enquiry form visible on page load (before guided form opened) | ✓ |
| Quick enquiry form visible when guided form is active | ✓ (always-visible panel above guided) |
| "Use quick enquiry instead" cancel link returns to quick form | ✓ |
| V1 (`ENQUIRY_FORM_V2=0`) build generates fallback form only | ✓ (verified by toggling flag) |

---

## Unresolved issues requiring live environment

1. **Screen reader testing** (NVDA/VoiceOver): requires running HTTP server. Focus management on step transitions not verified live.
2. **sessionStorage prefill**: requires HTTP server (blocked in `data:` URL context).
3. **End-to-end submission to Neon**: requires `POSTGRES_URL` env var set in staging.
4. **Formspree notification delivery**: requires `FORMSPREE_ENDPOINT` env var and live submission.
5. **At-least-one-safe-contact validation** (`safe_email || safe_phone`): correct server-side but client-side completion step needs verification that form always supplies at least one.

