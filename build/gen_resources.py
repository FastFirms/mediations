#!/usr/bin/env python3
"""Resource/guide pages + booking form. Keyword-first H1s, full schema."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build(slug,title,desc,eyebrow,h1,lede,ans,blocks,qa,crumb,cta_h,cta_p,is_article=True,tool_html=None):
    extra=article_schema(crumb,desc) if is_article else None
    schema=[org_schema(),breadcrumb_schema([("Home",""),("Resources",None if False else "preparing-for-mediation"),(crumb,slug)])]
    if extra: schema.append(extra)
    if qa: schema.append(faq_schema(qa))
    d=head(title,desc,slug,extra_schema=schema)+nav()
    d+=f"""<main id="main">
{crumb_html([("Home",""),("Resources",None),(crumb,None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
<h1>{h1}</h1><p class="lede">{lede}</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {ans}</p></div></div>
<article class="body"><div class="wrap-narrow reveal">{blocks}</div></article>"""
    if tool_html: d+=tool_html
    if qa: d+=faq_html(qa,heading=f"{crumb} — FAQs")
    d+=cta_band(cta_h,cta_p)+"</main>"+page_end()
    p=os.path.join(OUT,slug); os.makedirs(p,exist_ok=True)
    open(os.path.join(p,"index.html"),"w").write(d)
    import re; return slug,len(re.sub(r'<[^>]+>',' ',d).split())

# ---- PARENTING PLAN BUILDER TOOL (embedded on parenting-plan-template page) ----
PARENTING_BUILDER = """
<section class="sec ppb-outer" style="border-top:2px solid var(--line);padding:80px 0 96px;background:var(--sand)">
<div class="wrap" style="max-width:800px">
<div style="text-align:center;margin-bottom:52px">
  <p class="sec-tag">Free interactive tool</p>
  <h2 class="sec-title" style="margin-bottom:14px">Build Your Parenting Plan <em>Agreement</em></h2>
  <p style="color:var(--ink-soft);max-width:52ch;margin:0 auto;font-size:1.05rem;line-height:1.7">Answer the prompts across 9 steps. When you're done, download a ready-to-sign PDF agreement — free, private, and stored only on your device.</p>
</div>

<style>
/* ── Builder card ───────────────────────────────────────────── */
.ppb-card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:40px 44px;box-shadow:var(--shadow)}
/* ── Step indicator ─────────────────────────────────────────── */
.ppb-stepper{display:flex;align-items:center;justify-content:space-between;margin-bottom:36px;gap:6px}
.ppb-step{display:flex;flex-direction:column;align-items:center;gap:6px;flex:1;cursor:default}
.ppb-step-dot{width:30px;height:30px;border-radius:50%;border:2px solid var(--line);background:#fff;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;font-family:var(--sans);color:var(--ink-soft);transition:all .25s;flex-shrink:0}
.ppb-step.done .ppb-step-dot{background:var(--sage);border-color:var(--sage);color:#fff}
.ppb-step.active .ppb-step-dot{background:var(--sage);border-color:var(--sage);color:#fff;box-shadow:0 0 0 4px rgba(30,96,64,.15)}
.ppb-step-label{font-size:.68rem;font-family:var(--sans);font-weight:500;color:var(--ink-soft);text-align:center;letter-spacing:.01em;display:none}
.ppb-step.active .ppb-step-label{display:block;color:var(--sage);font-weight:600}
.ppb-step-connector{height:2px;flex:1;background:var(--line);border-radius:1px;margin-bottom:22px;transition:background .25s;min-width:8px}
.ppb-step-connector.done{background:var(--sage)}
/* ── Progress bar ───────────────────────────────────────────── */
.ppb-progress-wrap{margin-bottom:6px}
.ppb-progress-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;font-family:var(--sans);font-size:.82rem;color:var(--ink-soft)}
.ppb-progress-meta strong{color:var(--ink)}
.ppb-progress{background:var(--sand-deep);height:6px;border-radius:3px;overflow:hidden}
.ppb-progress-bar{height:100%;background:var(--sage);border-radius:3px;transition:width .35s cubic-bezier(.16,1,.3,1);width:0%}
/* ── Section ────────────────────────────────────────────────── */
.ppb-section{display:none}.ppb-section.active{display:block;animation:ppbFade .2s ease}
@keyframes ppbFade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.ppb-section-header{margin-bottom:28px;padding-bottom:20px;border-bottom:1px solid var(--line)}
.ppb-section-title{font-size:1.4rem;color:var(--ink);margin:0 0 4px;font-family:var(--serif);font-weight:500;line-height:1.25}
.ppb-section-subtitle{font-size:.9rem;color:var(--ink-soft);font-family:var(--sans);margin:0}
/* ── Form elements ──────────────────────────────────────────── */
.ppb-form-group{margin-bottom:22px}
.ppb-form-group label{display:block;margin-bottom:8px;color:var(--ink);font-weight:600;font-size:.88rem;font-family:var(--sans);letter-spacing:.01em}
.ppb-form-group input,.ppb-form-group select,.ppb-form-group textarea{width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-size:.95rem;box-sizing:border-box;font-family:var(--body-serif);transition:border-color .2s,box-shadow .2s;background:#fff;color:var(--ink)}
.ppb-form-group input:focus,.ppb-form-group select:focus,.ppb-form-group textarea:focus{outline:none;border-color:var(--sage);box-shadow:0 0 0 3px rgba(30,96,64,.1)}
.ppb-form-group select{appearance:none;background-image:url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%233d5248' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:36px}
.ppb-form-group textarea{min-height:100px;resize:vertical;line-height:1.65}
/* ── Radio as cards ─────────────────────────────────────────── */
.ppb-radio-cards{display:flex;flex-direction:column;gap:10px;margin-top:6px}
.ppb-radio-card{display:flex;align-items:center;gap:14px;padding:14px 16px;border:1.5px solid var(--line);border-radius:10px;cursor:pointer;transition:border-color .18s,background .18s;background:#fff}
.ppb-radio-card:hover{border-color:var(--sage);background:var(--sand)}
.ppb-radio-card input[type=radio]{width:18px;height:18px;accent-color:var(--sage);flex-shrink:0;cursor:pointer}
.ppb-radio-card label{color:var(--ink);font-family:var(--sans);font-size:.93rem;cursor:pointer;margin:0;font-weight:400;line-height:1.4}
.ppb-radio-card.selected{border-color:var(--sage);background:rgba(30,96,64,.04)}
/* ── Checkboxes ─────────────────────────────────────────────── */
.ppb-check-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px}
.ppb-check-card{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1.5px solid var(--line);border-radius:10px;cursor:pointer;transition:border-color .18s,background .18s;background:#fff}
.ppb-check-card:hover{border-color:var(--sage);background:var(--sand)}
.ppb-check-card input[type=checkbox]{width:17px;height:17px;accent-color:var(--sage);flex-shrink:0;cursor:pointer}
.ppb-check-card label{color:var(--ink);font-family:var(--sans);font-size:.88rem;cursor:pointer;margin:0;font-weight:400}
/* ── Two-column row ─────────────────────────────────────────── */
.ppb-row{display:grid;grid-template-columns:1fr 1fr;gap:18px}
/* ── Required marker ────────────────────────────────────────── */
.ppb-req{color:var(--sage);font-weight:700}
/* ── Help text ──────────────────────────────────────────────── */
.ppb-help{font-size:.8rem;color:var(--ink-soft);margin-top:5px;font-family:var(--sans);line-height:1.5}
/* ── Nav buttons ────────────────────────────────────────────── */
.ppb-nav{display:flex;justify-content:space-between;align-items:center;margin-top:36px;padding-top:24px;border-top:1px solid var(--line);gap:12px}
.ppb-btn-prev{display:inline-flex;align-items:center;gap:8px;padding:14px 24px;border:1.5px solid var(--line);border-radius:100px;font-size:.9rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:#fff;color:var(--ink-soft);transition:all .2s}
.ppb-btn-prev:hover:not(:disabled){border-color:var(--ink);color:var(--ink)}
.ppb-btn-prev:disabled{opacity:.35;cursor:not-allowed}
.ppb-btn-next{display:inline-flex;align-items:center;gap:8px;padding:14px 32px;border:none;border-radius:100px;font-size:.95rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:var(--sage);color:#fff;transition:all .2s;box-shadow:0 4px 14px rgba(30,96,64,.28)}
.ppb-btn-next:hover{background:var(--sage-deep);transform:translateY(-2px);box-shadow:0 8px 22px rgba(30,96,64,.32)}
/* ── Summary ────────────────────────────────────────────────── */
.ppb-summary{background:var(--sand);border:1px solid var(--line);border-radius:14px;padding:28px;margin-top:4px}
.ppb-summary-group{margin-bottom:22px;padding-bottom:22px;border-bottom:1px solid var(--line)}
.ppb-summary-group:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0}
.ppb-summary-group h4{font-family:var(--sans);font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--sage);margin:0 0 12px}
.ppb-summary-row{display:flex;gap:12px;margin-bottom:8px;font-size:.9rem}
.ppb-summary-row strong{font-family:var(--sans);font-weight:600;color:var(--ink);flex-shrink:0;min-width:140px}
.ppb-summary-row span{color:var(--ink-soft)}
/* ── Download / restart ─────────────────────────────────────── */
.ppb-actions{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}
.ppb-btn-dl{flex:1;min-width:160px;padding:16px 24px;border:none;border-radius:100px;font-size:1rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:var(--sage);color:#fff;box-shadow:0 4px 14px rgba(30,96,64,.28);transition:all .2s}
.ppb-btn-dl:hover{background:var(--sage-deep);transform:translateY(-2px)}
.ppb-btn-reset{flex:1;min-width:140px;padding:16px 24px;border:1.5px solid var(--line);border-radius:100px;font-size:.95rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:#fff;color:var(--ink-soft);transition:all .2s}
.ppb-btn-reset:hover{border-color:var(--ink);color:var(--ink)}
/* ── Disclaimer ─────────────────────────────────────────────── */
.ppb-disclaimer{font-size:.82rem;color:var(--ink-soft);background:var(--sand);border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin-top:20px;font-family:var(--sans);line-height:1.65}
.ppb-disclaimer strong{color:var(--ink)}
/* ── Error state ────────────────────────────────────────────── */
.ppb-error{border-color:var(--sage)!important;box-shadow:0 0 0 3px rgba(30,96,64,.15)!important}
.ppb-error-msg{font-size:.8rem;color:var(--sage);font-family:var(--sans);margin-top:4px;display:none}
/* ── Responsive ─────────────────────────────────────────────── */
@media(max-width:640px){
  .ppb-card{padding:24px 20px}
  .ppb-row{grid-template-columns:1fr}
  .ppb-check-grid{grid-template-columns:1fr}
  .ppb-nav{flex-direction:column-reverse}
  .ppb-btn-prev,.ppb-btn-next{width:100%;justify-content:center}
  .ppb-actions{flex-direction:column}
  .ppb-btn-dl,.ppb-btn-reset{width:100%;text-align:center}
  .ppb-step-dot{width:24px;height:24px;font-size:.65rem}
}
</style>

<div class="ppb-card">
  <!-- Step indicator -->
  <div class="ppb-stepper" id="ppbStepper" aria-label="Progress"></div>

  <!-- Progress bar -->
  <div class="ppb-progress-wrap">
    <div class="ppb-progress-meta">
      <span id="ppbStepLabel"><strong>Step 1 of 9:</strong> Parties &amp; Children</span>
      <span id="ppbStepPct" style="font-weight:600;color:var(--sage)">11%</span>
    </div>
    <div class="ppb-progress" role="progressbar" aria-valuenow="11" aria-valuemin="0" aria-valuemax="100">
      <div class="ppb-progress-bar" id="ppbProgressBar"></div>
    </div>
  </div>

  <form id="ppbForm" novalidate>

    <!-- Step 1: Parties -->
    <div class="ppb-section active" data-section="1">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Parties &amp; Children</h3>
        <p class="ppb-section-subtitle">The people this agreement is between, and the children it covers.</p>
      </div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Party 1 Full Name <span class="ppb-req">*</span></label><input type="text" name="parent1_name" autocomplete="name" required placeholder="Full legal name"></div>
        <div class="ppb-form-group"><label>Party 2 Full Name <span class="ppb-req">*</span></label><input type="text" name="parent2_name" autocomplete="off" required placeholder="Full legal name"></div>
      </div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Party 1 Address</label><input type="text" name="parent1_address" placeholder="Street address, suburb, state"></div>
        <div class="ppb-form-group"><label>Party 2 Address</label><input type="text" name="parent2_address" placeholder="Street address, suburb, state"></div>
      </div>
      <div class="ppb-form-group"><label>Child / Children <span class="ppb-req">*</span></label><textarea name="children_info" required placeholder="Full name and date of birth for each child&#10;e.g. Sarah Elizabeth Smith, born 15 March 2016"></textarea><p class="ppb-help">Include all children covered by this agreement, one per line.</p></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Agreement Date <span class="ppb-req">*</span></label><input type="date" name="agreement_date" required></div>
        <div class="ppb-form-group"><label>Review Date <span class="ppb-help" style="display:inline;font-style:normal">— optional</span></label><input type="date" name="review_date"></div>
      </div>
    </div>

    <!-- Step 2: Parental Responsibility -->
    <div class="ppb-section" data-section="2">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Parental Responsibility</h3>
        <p class="ppb-section-subtitle">Who makes major long-term decisions about the children.</p>
      </div>
      <div class="ppb-form-group">
        <label>Parental Responsibility Arrangement <span class="ppb-req">*</span></label>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="parental_responsibility" value="equal" id="ppb_r1" required><label for="ppb_r1">Equal shared parental responsibility — both parents decide together on major issues</label></div>
          <div class="ppb-radio-card"><input type="radio" name="parental_responsibility" value="sole_parent1" id="ppb_r2"><label for="ppb_r2">Sole parental responsibility to Party 1</label></div>
          <div class="ppb-radio-card"><input type="radio" name="parental_responsibility" value="sole_parent2" id="ppb_r3"><label for="ppb_r3">Sole parental responsibility to Party 2</label></div>
        </div>
      </div>
      <div class="ppb-form-group">
        <label>Major decisions requiring consultation between both parties</label>
        <div class="ppb-check-grid">
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="education" id="ppb_m1"><label for="ppb_m1">Education</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="major medical treatment" id="ppb_m2"><label for="ppb_m2">Major medical treatment</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="religious upbringing" id="ppb_m3"><label for="ppb_m3">Religious upbringing</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="relocation" id="ppb_m4"><label for="ppb_m4">Relocation</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="name changes" id="ppb_m5"><label for="ppb_m5">Name changes</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="passport applications" id="ppb_m6"><label for="ppb_m6">Passport applications</label></div>
        </div>
      </div>
    </div>

    <!-- Step 3: Living Arrangements -->
    <div class="ppb-section" data-section="3">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Living Arrangements</h3>
        <p class="ppb-section-subtitle">Where the children live and the regular care schedule.</p>
      </div>
      <div class="ppb-form-group">
        <label>The child/children shall live with <span class="ppb-req">*</span></label>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="primary_residence" value="equal" id="ppb_res1" required><label for="ppb_res1">Both parties equally — shared care arrangement</label></div>
          <div class="ppb-radio-card"><input type="radio" name="primary_residence" value="parent1" id="ppb_res2"><label for="ppb_res2">Primarily with Party 1</label></div>
          <div class="ppb-radio-card"><input type="radio" name="primary_residence" value="parent2" id="ppb_res3"><label for="ppb_res3">Primarily with Party 2</label></div>
        </div>
      </div>
      <div class="ppb-form-group">
        <label>Regular Care Schedule <span class="ppb-req">*</span></label>
        <select name="schedule_type" required>
          <option value="">Select a schedule</option>
          <option value="week about (alternating weeks)">Week about — alternating weeks</option>
          <option value="2-2-5-5 schedule">2-2-5-5 schedule</option>
          <option value="2-2-3-3 schedule">2-2-3-3 schedule</option>
          <option value="alternate weekends">Alternate weekends with one parent</option>
          <option value="custom">Custom — I'll describe it below</option>
        </select>
      </div>
      <div class="ppb-form-group"><label>Detailed Schedule</label><textarea name="schedule_details" placeholder="Specific days, times, and any weekly variations"></textarea></div>
      <div class="ppb-form-group"><label>Changeover — time and location</label><textarea name="changeover_details" placeholder="e.g. Friday at 6:00 pm at the child's school"></textarea></div>
    </div>

    <!-- Step 4: Holidays -->
    <div class="ppb-section" data-section="4">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Holidays &amp; Special Days</h3>
        <p class="ppb-section-subtitle">How school holidays and significant days are divided. Leave blank any that don't apply.</p>
      </div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Christmas &amp; New Year</label><textarea name="christmas_arrangement" placeholder="e.g. Christmas Day with Party 1 in odd years, Party 2 in even years"></textarea></div>
        <div class="ppb-form-group"><label>Easter</label><textarea name="easter_arrangement" placeholder="e.g. Easter weekend alternates each year"></textarea></div>
      </div>
      <div class="ppb-form-group"><label>School Holiday Periods</label><textarea name="school_holidays" placeholder="e.g. School holidays split equally — each party takes two weeks per term break"></textarea></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Children's Birthdays</label><textarea name="children_birthdays" placeholder="e.g. Both parents attend birthday celebrations where possible"></textarea></div>
        <div class="ppb-form-group"><label>Mother's Day &amp; Father's Day</label><textarea name="parents_day" placeholder="e.g. Children spend Mother's Day with Party 1, Father's Day with Party 2"></textarea></div>
      </div>
    </div>

    <!-- Step 5: Communication -->
    <div class="ppb-section" data-section="5">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Communication</h3>
        <p class="ppb-section-subtitle">How the parents communicate, and how the children stay in touch with the other parent.</p>
      </div>
      <div class="ppb-form-group">
        <label>Communication between parents</label>
        <div class="ppb-check-grid">
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="email" id="ppb_c1"><label for="ppb_c1">Email</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="text message" id="ppb_c2"><label for="ppb_c2">Text message</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="phone calls" id="ppb_c3"><label for="ppb_c3">Phone calls</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="parenting app" id="ppb_c4"><label for="ppb_c4">Parenting app (e.g. OurFamilyWizard)</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Child's contact with the other parent</label><textarea name="child_contact" placeholder="e.g. Daily phone or video call at 7:00 pm when staying with the other parent"></textarea></div>
    </div>

    <!-- Step 6: Education -->
    <div class="ppb-section" data-section="6">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Education</h3>
        <p class="ppb-section-subtitle">School decisions and extracurricular activities.</p>
      </div>
      <div class="ppb-form-group">
        <label>School Selection</label>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="school_selection" value="joint decision by both parties" id="ppb_s1"><label for="ppb_s1">Joint decision by both parties</label></div>
          <div class="ppb-radio-card"><input type="radio" name="school_selection" value="primary carer decides after consultation" id="ppb_s2"><label for="ppb_s2">Primary carer decides after consultation</label></div>
          <div class="ppb-radio-card"><input type="radio" name="school_selection" value="continue at current school" id="ppb_s3"><label for="ppb_s3">Continue at current school</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Extracurricular Activities</label><textarea name="extracurricular_activities" placeholder="e.g. Both parties support current activities; new activities require agreement"></textarea></div>
    </div>

    <!-- Step 7: Health -->
    <div class="ppb-section" data-section="7">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Health &amp; Medical Care</h3>
        <p class="ppb-section-subtitle">Medical decision-making and expense responsibilities.</p>
      </div>
      <div class="ppb-form-group">
        <label>Medical Decision Making</label>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="medical_decisions" value="joint decisions for all medical treatment" id="ppb_md1"><label for="ppb_md1">Joint decisions for all medical treatment</label></div>
          <div class="ppb-radio-card"><input type="radio" name="medical_decisions" value="joint for major decisions; either parent for routine and emergency care" id="ppb_md2"><label for="ppb_md2">Joint for major decisions; either parent for routine and emergency</label></div>
          <div class="ppb-radio-card"><input type="radio" name="medical_decisions" value="primary carer decides after consultation" id="ppb_md3"><label for="ppb_md3">Primary carer decides after consultation with the other</label></div>
        </div>
      </div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Health Insurance &amp; Expenses</label><textarea name="medical_expenses" placeholder="e.g. Both parties share Medicare and private health costs equally"></textarea></div>
        <div class="ppb-form-group"><label>Special Health Needs</label><textarea name="special_health_needs" placeholder="Any ongoing conditions, medications, or specialist requirements"></textarea></div>
      </div>
    </div>

    <!-- Step 8: Financial -->
    <div class="ppb-section" data-section="8">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Financial Provisions</h3>
        <p class="ppb-section-subtitle">Child support and how ongoing costs will be shared.</p>
      </div>
      <div class="ppb-form-group">
        <label>Child Support</label>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="child_support" value="Services Australia child support assessment" id="ppb_cs1"><label for="ppb_cs1">Services Australia assessment</label></div>
          <div class="ppb-radio-card"><input type="radio" name="child_support" value="private child support agreement between the parties" id="ppb_cs2"><label for="ppb_cs2">Private agreement between the parties</label></div>
          <div class="ppb-radio-card"><input type="radio" name="child_support" value="no child support payable" id="ppb_cs3"><label for="ppb_cs3">No child support payable</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Child Support Details</label><textarea name="support_details" placeholder="Amount, frequency, and payment method if private agreement"></textarea></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Education Expenses</label><textarea name="education_expenses" placeholder="e.g. School fees and uniforms shared equally"></textarea></div>
        <div class="ppb-form-group"><label>Medical &amp; Dental Expenses</label><textarea name="health_expenses" placeholder="e.g. Out-of-pocket costs shared equally after Medicare rebate"></textarea></div>
      </div>
    </div>

    <!-- Step 9: Dispute Resolution -->
    <div class="ppb-section" data-section="9">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Dispute Resolution &amp; Other Provisions</h3>
        <p class="ppb-section-subtitle">How disagreements will be handled, and any other terms you want to include.</p>
      </div>
      <div class="ppb-form-group"><label>Dispute Resolution Process</label><textarea name="dispute_process" placeholder="e.g. Direct discussion first, then Family Dispute Resolution with an accredited mediator, then legal proceedings if unresolved"></textarea></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Travel &amp; Relocation</label><textarea name="travel_relocation" placeholder="e.g. Domestic travel requires 7 days notice; international travel requires written agreement"></textarea></div>
        <div class="ppb-form-group"><label>Introduction of New Partners</label><textarea name="new_partners" placeholder="e.g. New partners introduced only after 6 months of relationship"></textarea></div>
      </div>
      <div class="ppb-form-group"><label>Additional Provisions</label><textarea name="additional_provisions" placeholder="Any other terms the parties agree to include"></textarea></div>
    </div>

    <!-- Step 10: Review -->
    <div class="ppb-section" data-section="10">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Review &amp; Download</h3>
        <p class="ppb-section-subtitle">Check your answers, then download a ready-to-sign PDF.</p>
      </div>
      <div class="ppb-summary" id="ppbPlanSummary"></div>
      <div class="ppb-disclaimer">
        <strong>Important:</strong> A parenting plan is a written agreement but is not directly enforceable by a court. To make your arrangements legally enforceable, you must apply for <a href="/consent-orders/">consent orders</a>. Independent legal advice is recommended before signing. This builder is a free tool only — it does not create a lawyer-client relationship with Mediations Australia.
      </div>
      <div class="ppb-actions">
        <button type="button" class="ppb-btn-dl" id="ppbDownloadBtn">Download PDF Agreement →</button>
        <button type="button" class="ppb-btn-reset" id="ppbRestartBtn">Start Over</button>
      </div>
    </div>

  </form>

  <div class="ppb-nav" id="ppbNav">
    <button type="button" class="ppb-btn-prev" id="ppbPrevBtn" disabled>← Previous</button>
    <button type="button" class="ppb-btn-next" id="ppbNextBtn">Next →</button>
  </div>
</div>
<div class="ppb-container">
  <div class="ppb-progress"><div class="ppb-progress-bar" id="ppbProgressBar"></div></div>
  <form id="ppbForm">

    <div class="ppb-section active" data-section="1">
      <h3 class="ppb-section-title"><span class="ppb-section-number">A</span>Agreement Parties</h3>
      <div class="ppb-row">
        <div class="ppb-col"><div class="ppb-form-group"><label>Party 1 Full Name <span class="ppb-required">*</span></label><input type="text" name="parent1_name" required></div></div>
        <div class="ppb-col"><div class="ppb-form-group"><label>Party 2 Full Name <span class="ppb-required">*</span></label><input type="text" name="parent2_name" required></div></div>
      </div>
      <div class="ppb-row">
        <div class="ppb-col"><div class="ppb-form-group"><label>Party 1 Address</label><input type="text" name="parent1_address"></div></div>
        <div class="ppb-col"><div class="ppb-form-group"><label>Party 2 Address</label><input type="text" name="parent2_address"></div></div>
      </div>
      <div class="ppb-form-group"><label>Child/Children (full name and date of birth) <span class="ppb-required">*</span></label><textarea name="children_info" placeholder="e.g., Sarah Elizabeth Smith, born 15 March 2016" required></textarea></div>
      <div class="ppb-row">
        <div class="ppb-col"><div class="ppb-form-group"><label>Agreement Date <span class="ppb-required">*</span></label><input type="date" name="agreement_date" required></div></div>
        <div class="ppb-col"><div class="ppb-form-group"><label>Review Date</label><input type="date" name="review_date"></div></div>
      </div>
    </div>

    <div class="ppb-section" data-section="2">
      <h3 class="ppb-section-title"><span class="ppb-section-number">1</span>Parental Responsibility</h3>
      <div class="ppb-subsection">
        <div class="ppb-form-group"><label>Parental Responsibility Arrangement <span class="ppb-required">*</span></label>
          <div class="ppb-radio-group">
            <div class="ppb-radio-item"><input type="radio" name="parental_responsibility" value="equal" id="ppb_resp_equal" required><label for="ppb_resp_equal">Equal shared parental responsibility</label></div>
            <div class="ppb-radio-item"><input type="radio" name="parental_responsibility" value="sole_parent1" id="ppb_resp_sole1"><label for="ppb_resp_sole1">Sole parental responsibility to Party 1</label></div>
            <div class="ppb-radio-item"><input type="radio" name="parental_responsibility" value="sole_parent2" id="ppb_resp_sole2"><label for="ppb_resp_sole2">Sole parental responsibility to Party 2</label></div>
          </div>
        </div>
      </div>
      <div class="ppb-subsection">
        <div class="ppb-subsection-title">Major long-term decisions requiring consultation</div>
        <div class="ppb-checkbox-group">
          <div class="ppb-checkbox-item"><input type="checkbox" name="major_decisions[]" value="education" id="ppb_m_ed"><label for="ppb_m_ed">Education</label></div>
          <div class="ppb-checkbox-item"><input type="checkbox" name="major_decisions[]" value="major medical treatment" id="ppb_m_med"><label for="ppb_m_med">Major medical treatment</label></div>
          <div class="ppb-checkbox-item"><input type="checkbox" name="major_decisions[]" value="religious upbringing" id="ppb_m_rel"><label for="ppb_m_rel">Religious upbringing</label></div>
          <div class="ppb-checkbox-item"><input type="checkbox" name="major_decisions[]" value="relocation" id="ppb_m_reloc"><label for="ppb_m_reloc">Relocation</label></div>
          <div class="ppb-checkbox-item"><input type="checkbox" name="major_decisions[]" value="name changes" id="ppb_m_name"><label for="ppb_m_name">Name changes</label></div>
          <div class="ppb-checkbox-item"><input type="checkbox" name="major_decisions[]" value="passport applications" id="ppb_m_pass"><label for="ppb_m_pass">Passport applications</label></div>
        </div>
      </div>
    </div>

    <div class="ppb-section" data-section="3">
      <h3 class="ppb-section-title"><span class="ppb-section-number">2</span>Living Arrangements</h3>
      <div class="ppb-subsection">
        <div class="ppb-form-group"><label>The child/children shall live with <span class="ppb-required">*</span></label>
          <div class="ppb-radio-group">
            <div class="ppb-radio-item"><input type="radio" name="primary_residence" value="equal" id="ppb_res_equal" required><label for="ppb_res_equal">Both parties equally (shared care)</label></div>
            <div class="ppb-radio-item"><input type="radio" name="primary_residence" value="parent1" id="ppb_res_p1"><label for="ppb_res_p1">Primarily with Party 1</label></div>
            <div class="ppb-radio-item"><input type="radio" name="primary_residence" value="parent2" id="ppb_res_p2"><label for="ppb_res_p2">Primarily with Party 2</label></div>
          </div>
        </div>
      </div>
      <div class="ppb-subsection">
        <div class="ppb-form-group"><label>Regular Care Schedule <span class="ppb-required">*</span></label>
          <select name="schedule_type" required>
            <option value="">Select a care schedule</option>
            <option value="week about (alternating weeks)">Week about (alternating weeks)</option>
            <option value="2-2-5-5 schedule">2-2-5-5 Schedule</option>
            <option value="2-2-3-3 schedule">2-2-3-3 Schedule</option>
            <option value="alternate weekends">Alternate weekends</option>
            <option value="custom">Custom (detailed below)</option>
          </select>
        </div>
        <div class="ppb-form-group"><label>Detailed Schedule Provisions</label><textarea name="schedule_details" placeholder="Specify exact days, times, and arrangements"></textarea></div>
        <div class="ppb-form-group"><label>Changeover Times and Locations</label><textarea name="changeover_details" placeholder="e.g., Friday 6:00 PM at the child's school"></textarea></div>
      </div>
    </div>

    <div class="ppb-section" data-section="4">
      <h3 class="ppb-section-title"><span class="ppb-section-number">3</span>Holidays and Special Occasions</h3>
      <div class="ppb-form-group"><label>Christmas and New Year</label><textarea name="christmas_arrangement"></textarea></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script>
(function(){
  var TOTAL=10;
  var STEP_NAMES=['Parties & Children','Parental Responsibility','Living Arrangements','Holidays & Special Days','Communication','Education','Health & Medical','Financial','Dispute Resolution','Review & Download'];
  var cur=1;
  var form=document.getElementById('ppbForm');
  var progBar=document.getElementById('ppbProgressBar');
  var prevBtn=document.getElementById('ppbPrevBtn');
  var nextBtn=document.getElementById('ppbNextBtn');
  var navEl=document.getElementById('ppbNav');
  var stepperEl=document.getElementById('ppbStepper');
  var stepLabelEl=document.getElementById('ppbStepLabel');
  var stepPctEl=document.getElementById('ppbStepPct');

  /* Build mini step dots */
  for(var i=1;i<=TOTAL;i++){
    var dot=document.createElement('div');
    dot.className='ppb-step'+(i===1?' active':'');
    dot.setAttribute('data-step',i);
    dot.innerHTML='<div class="ppb-step-dot">'+i+'</div><div class="ppb-step-label">'+STEP_NAMES[i-1]+'</div>';
    stepperEl.appendChild(dot);
    if(i<TOTAL){var conn=document.createElement('div');conn.className='ppb-step-connector';conn.setAttribute('data-conn',i);stepperEl.appendChild(conn);}
  }

  /* Highlight radio-cards on click */
  form.addEventListener('change',function(e){
    var el=e.target;
    if(el.type==='radio'){
      var name=el.name;
      form.querySelectorAll('[name="'+name+'"]').forEach(function(r){
        var card=r.closest('.ppb-radio-card');
        if(card) card.classList.toggle('selected',r.checked);
      });
    }
  });

  function gd(n){return(new FormData(form).get(n)||'').toString();}

  function updateUI(){
    var pct=Math.round(cur/TOTAL*100);
    progBar.style.width=pct+'%';
    progBar.parentElement.setAttribute('aria-valuenow',pct);
    stepLabelEl.innerHTML='<strong>Step '+cur+' of '+TOTAL+':</strong> '+STEP_NAMES[cur-1];
    stepPctEl.textContent=pct+'%';
    /* Stepper dots */
    stepperEl.querySelectorAll('.ppb-step').forEach(function(s){
      var n=parseInt(s.getAttribute('data-step'));
      s.classList.toggle('done',n<cur);
      s.classList.toggle('active',n===cur);
    });
    stepperEl.querySelectorAll('.ppb-step-connector').forEach(function(c){
      c.classList.toggle('done',parseInt(c.getAttribute('data-conn'))<cur);
    });
    prevBtn.disabled=(cur===1);
    if(cur===TOTAL){nextBtn.style.display='none';}
    else if(cur===TOTAL-1){nextBtn.style.display='';nextBtn.innerHTML='Review &amp; Finish →';}
    else{nextBtn.style.display='';nextBtn.innerHTML='Next →';}
  }

  function validateCurrent(){
    var curEl=form.querySelector('[data-section="'+cur+'"]');
    var ok=true;
    /* Text/select/textarea required */
    curEl.querySelectorAll('input[required],select[required],textarea[required]').forEach(function(f){
      if(f.type==='radio'){return;} /* handled below */
      if(!f.value.trim()){f.classList.add('ppb-error');ok=false;}
      else{f.classList.remove('ppb-error');}
    });
    /* Required radio groups */
    var radioNames={};
    curEl.querySelectorAll('input[type=radio][required]').forEach(function(r){radioNames[r.name]=true;});
    Object.keys(radioNames).forEach(function(n){
      var checked=curEl.querySelector('[name="'+n+'"]:checked');
      var cards=curEl.querySelectorAll('[name="'+n+'"]');
      cards.forEach(function(r){
        var card=r.closest('.ppb-radio-card');
        if(card) card.classList.toggle('ppb-error',!checked);
      });
      if(!checked) ok=false;
    });
    return ok;
  }

  function changeSection(dir){
    if(dir>0&&!validateCurrent()){
      /* Scroll to first error */
      var first=form.querySelector('[data-section="'+cur+'"] .ppb-error');
      if(first) first.scrollIntoView({behavior:'smooth',block:'center'});
      return;
    }
    form.querySelector('[data-section="'+cur+'"]').classList.remove('active');
    cur=Math.min(Math.max(cur+dir,1),TOTAL);
    form.querySelector('[data-section="'+cur+'"]').classList.add('active');
    if(cur===TOTAL) generateSummary();
    updateUI();
    /* Autosave on advance */
    autosave();
    /* Scroll builder card into view */
    document.getElementById('ppbForm').closest('.ppb-card').scrollIntoView({behavior:'smooth',block:'start'});
  }

  prevBtn.addEventListener('click',function(){changeSection(-1);});
  nextBtn.addEventListener('click',function(){changeSection(1);});

  function generateSummary(){
    var fd=new FormData(form);
    var majors=fd.getAll('major_decisions[]');
    var comms=fd.getAll('parent_communication[]');
    var row=function(label,val){return val?'<div class="ppb-summary-row"><strong>'+label+'</strong><span>'+(val||'—')+'</span></div>':'';}
    var group=function(title,rows){return'<div class="ppb-summary-group"><h4>'+title+'</h4>'+rows+'</div>';};
    var h='';
    h+=group('Parties',
      row('Party 1',gd('parent1_name'))+
      row('Party 2',gd('parent2_name'))+
      row('Children',gd('children_info').replace(/\n/g,'; '))+
      row('Agreement date',gd('agreement_date'))
    );
    h+=group('Parental Responsibility &amp; Residence',
      row('Parental responsibility',gd('parental_responsibility').replace(/_/g,' '))+
      (majors.length?row('Joint decisions',majors.join(', ')):'')+
      row('Children live with',gd('primary_residence').replace(/_/g,' '))+
      row('Schedule',gd('schedule_type'))
    );
    h+=group('Holidays &amp; Communication',
      row('Christmas',gd('christmas_arrangement'))+
      row('Easter',gd('easter_arrangement'))+
      row('School holidays',gd('school_holidays'))+
      (comms.length?row('Parent communication',comms.join(', ')):'')
    );
    h+=group('Education, Health &amp; Finance',
      row('School selection',gd('school_selection'))+
      row('Medical decisions',gd('medical_decisions'))+
      row('Child support',gd('child_support'))
    );
    document.getElementById('ppbPlanSummary').innerHTML=h;
  }

  /* ---- PDF ---- */
  document.getElementById('ppbDownloadBtn').addEventListener('click',function(){
    if(typeof window.jspdf==='undefined'){alert('PDF library loading — please wait a moment and try again.');return;}
    var jsPDF=window.jspdf.jsPDF;
    var doc=new jsPDF();
    var fd=new FormData(form);
    var g=function(n){return(fd.get(n)||'[To be specified]').toString().trim();};
    var M=20,W=170; var y=30;
    var chk=function(need){if(y+need>280){doc.addPage();y=20;}};
    var para=function(text,size,bold,gap){
      doc.setFont('helvetica',bold?'bold':'normal');doc.setFontSize(size);
      var lines=doc.splitTextToSize(text,W);
      chk(lines.length*(size*0.5));
      doc.text(lines,M,y);y+=lines.length*(size*0.5)+(gap||4);
    };
    /* Cover */
    doc.setFont('helvetica','bold');doc.setFontSize(20);
    doc.text('PARENTING PLAN AGREEMENT',105,y,{align:'center'});y+=14;
    doc.setFont('helvetica','normal');doc.setFontSize(12);
    doc.text('Dated: '+g('agreement_date'),105,y,{align:'center'});y+=8;
    doc.text('Between '+g('parent1_name')+' and '+g('parent2_name'),105,y,{align:'center'});y+=12;
    para('Concerning: '+g('children_info').replace(/\n/g,'; '),11,false,10);
    para('PREAMBLE',13,true,6);
    para('This Parenting Plan is made between '+g('parent1_name')+' and '+g('parent2_name')+' in relation to the care, welfare and development of the above-named child/children. The parties acknowledge that it is in the best interests of the child/children that both parents continue to have meaningful relationships with them, consistent with the best interests principle under the Family Law Act 1975 (Cth).',11,false,10);
    /* Clause 1 */
    para('1. PARENTAL RESPONSIBILITY',12,true,6);
    var pr=g('parental_responsibility');
    if(pr==='equal') para('1.1 The parties shall have equal shared parental responsibility for the child/children.',11,false,4);
    else if(pr==='sole_parent1') para('1.1 '+g('parent1_name')+' shall have sole parental responsibility for the child/children.',11,false,4);
    else if(pr==='sole_parent2') para('1.1 '+g('parent2_name')+' shall have sole parental responsibility for the child/children.',11,false,4);
    var majors=fd.getAll('major_decisions[]');
    if(majors.length) para('1.2 The following major long-term decisions shall require consultation between both parties: '+majors.join(', ')+'.',11,false,10);
    /* Clause 2 */
    para('2. LIVING ARRANGEMENTS',12,true,6);
    var res=g('primary_residence');
    if(res==='equal') para('2.1 The child/children shall spend equal time with both parties in a shared care arrangement.',11,false,4);
    else if(res==='parent1') para('2.1 The child/children shall live primarily with '+g('parent1_name')+' and spend time with '+g('parent2_name')+' per the schedule below.',11,false,4);
    else if(res==='parent2') para('2.1 The child/children shall live primarily with '+g('parent2_name')+' and spend time with '+g('parent1_name')+' per the schedule below.',11,false,4);
    para('2.2 Care schedule: '+g('schedule_type')+'.',11,false,4);
    if(g('schedule_details')!=='[To be specified]') para('2.3 '+g('schedule_details'),11,false,4);
    if(g('changeover_details')!=='[To be specified]') para('2.4 Changeovers: '+g('changeover_details'),11,false,10);
    /* Clause 3 */
    para('3. HOLIDAYS AND SPECIAL OCCASIONS',12,true,6);
    [['3.1 Christmas and New Year','christmas_arrangement'],['3.2 Easter','easter_arrangement'],['3.3 School holidays','school_holidays'],['3.4 Birthdays','children_birthdays'],["3.5 Mother's and Father's Day",'parents_day']].forEach(function(a){if(g(a[1])!=='[To be specified]') para(a[0]+': '+g(a[1]),11,false,4);});y+=4;
    /* Clause 4 */
    para('4. COMMUNICATION',12,true,6);
    var comms=fd.getAll('parent_communication[]');
    if(comms.length) para('4.1 Communication between parents shall be by: '+comms.join(', ')+'.',11,false,4);
    if(g('child_contact')!=='[To be specified]') para('4.2 The child/children may contact the other parent: '+g('child_contact'),11,false,10);
    /* Clause 5 */
    para('5. EDUCATION',12,true,6);
    if(g('school_selection')!=='[To be specified]') para('5.1 School selection: '+g('school_selection')+'.',11,false,4);
    if(g('extracurricular_activities')!=='[To be specified]') para('5.2 Extracurricular activities: '+g('extracurricular_activities'),11,false,10);
    /* Clause 6 */
    para('6. HEALTH AND MEDICAL CARE',12,true,6);
    if(g('medical_decisions')!=='[To be specified]') para('6.1 Medical decision making: '+g('medical_decisions')+'.',11,false,4);
    if(g('medical_expenses')!=='[To be specified]') para('6.2 Health insurance and expenses: '+g('medical_expenses'),11,false,4);
    if(g('special_health_needs')!=='[To be specified]') para('6.3 Special health needs: '+g('special_health_needs'),11,false,10);
    /* Clause 7 */
    para('7. FINANCIAL PROVISIONS',12,true,6);
    para('7.1 Child support: '+g('child_support')+'.',11,false,4);
    if(g('support_details')!=='[To be specified]') para('7.2 Details: '+g('support_details'),11,false,4);
    if(g('education_expenses')!=='[To be specified]') para('7.3 Education expenses: '+g('education_expenses'),11,false,4);
    if(g('health_expenses')!=='[To be specified]') para('7.4 Medical and dental expenses: '+g('health_expenses'),11,false,10);
    /* Clause 8 */
    para('8. DISPUTE RESOLUTION AND OTHER PROVISIONS',12,true,6);
    para('8.1 Dispute resolution: '+(g('dispute_process')!=='[To be specified]'?g('dispute_process'):'The parties agree to attempt resolution through direct discussion and, if unresolved, Family Dispute Resolution before commencing court proceedings.'),11,false,4);
    if(g('travel_relocation')!=='[To be specified]') para('8.2 Travel and relocation: '+g('travel_relocation'),11,false,4);
    if(g('new_partners')!=='[To be specified]') para('8.3 Introduction of new partners: '+g('new_partners'),11,false,4);
    if(g('additional_provisions')!=='[To be specified]') para('8.4 Additional provisions: '+g('additional_provisions'),11,false,10);
    /* Execution page */
    doc.addPage();y=20;
    para('EXECUTION',12,true,6);
    para('The parties agree to be bound by the terms of this Parenting Plan and acknowledge they have read and understood its contents. This Plan may be varied by mutual written agreement at any time.',11,false,8);
    doc.setFont('helvetica','italic');doc.setFontSize(9);
    var notice=doc.splitTextToSize('IMPORTANT: A parenting plan is not a legally enforceable agreement. If you want your agreement to be legally binding and enforceable, you must apply to the Family Court for consent orders. Seek independent legal advice before signing.',W);
    doc.text(notice,M,y);y+=notice.length*4.5+18;
    doc.setFont('helvetica','normal');doc.setFontSize(11);
    doc.text('SIGNED:',M,y);y+=6;
    doc.line(M,y+14,90,y+14);doc.text(g('parent1_name'),M,y+21);doc.text('Date: __________________',M,y+30);
    doc.line(110,y+14,180,y+14);doc.text(g('parent2_name'),110,y+21);doc.text('Date: __________________',110,y+30);
    doc.setFontSize(8);
    doc.text('Generated by Mediations Australia Parenting Plan Builder — www.mediationsaustralia.com.au',105,288,{align:'center'});
    doc.save('parenting-plan-agreement.pdf');
  });

  document.getElementById('ppbRestartBtn').addEventListener('click',function(){
    if(!confirm('Start over? All entered information will be lost.')) return;
    form.reset();
    try{sessionStorage.removeItem('ppbData');}catch(e){}
    form.querySelectorAll('.ppb-section').forEach(function(s){s.classList.remove('active');});
    form.querySelector('[data-section="1"]').classList.add('active');
    cur=1;
    updateUI();
  });

  /* Autosave */
  var saveTimer;
  form.addEventListener('input',function(){
    clearTimeout(saveTimer);
    saveTimer=setTimeout(autosave,800);
  });
  function autosave(){
    var fd=new FormData(form),data={};
    fd.forEach(function(v,k){
      if(data[k]===undefined) data[k]=v;
      else{if(!Array.isArray(data[k])) data[k]=[data[k]]; data[k].push(v);}
    });
    try{sessionStorage.setItem('ppbData',JSON.stringify(data));}catch(e){}
  }

  /* Restore */
  try{
    var saved=sessionStorage.getItem('ppbData');
    if(saved){
      var data=JSON.parse(saved);
      Object.keys(data).forEach(function(k){
        var nodes=form.querySelectorAll('[name="'+k.replace(/"/g,'')+'"]');
        nodes.forEach(function(f){
          if(f.type==='radio'||f.type==='checkbox'){
            f.checked=Array.isArray(data[k])?data[k].includes(f.value):f.value===data[k];
            if(f.checked&&f.type==='radio'){
              var card=f.closest('.ppb-radio-card');
              if(card) card.classList.add('selected');
            }
          } else { f.value=data[k]; }
        });
      });
    }
  }catch(e){}

  updateUI();
})();
</script>
</section>
"""

# ---- PARENTING PLAN TEMPLATE ----
build("parenting-plan-template",
 "Parenting Plan Template Australia | What to Include (2026)",
 "A complete guide to what belongs in a parenting plan in Australia — living arrangements, time, decisions, holidays and dispute resolution. Build yours with accredited mediators.",
 "A practical guide for separated parents",
 "Parenting Plan Template",
 "A parenting plan is the practical backbone of co-parenting after separation. This guide walks through every section a thorough Australian parenting plan should cover — with worked examples, common mistakes to avoid, and how to turn a draft into an arrangement that actually holds.",
 "A parenting plan should cover where the children live, how time is shared week to week, holidays and special occasions, how major decisions are made, communication between parents, travel arrangements, and how disputes will be handled. A mediator helps parents negotiate each section so the plan reflects the children's real needs rather than what either parent prefers.",
 """
 <h2>What is a parenting plan?</h2>
 <p>A parenting plan is a written agreement between separated parents that sets out how their children will be raised across two households. Under the <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act 1975</a>, a parenting plan must be in writing and signed and dated by both parents. It is not a court order, but a court will consider it in any later dispute — and it is far more useful than an oral agreement that each party later remembers differently.</p>
 <p>A parenting plan is different from <a href="/consent-orders/">consent orders</a>, which are court-approved and directly enforceable. Many families use a parenting plan as a starting point and later formalise it as consent orders once arrangements have settled.</p>

 <h2>The full template: what to cover section by section</h2>

 <h3>1. Living arrangements</h3>
 <p>Specify where the children primarily live and describe the week-to-week routine clearly enough that there's no room for argument. Include:</p>
 <ul>
   <li>Which parent the child lives with during the school week</li>
   <li>Which parent has time at weekends and when</li>
   <li>How transitions happen — who drops off, who collects, at what time and where</li>
   <li>What happens if one parent is late or unavailable</li>
 </ul>
 <div class="callout"><h3>Worked example: week on / week off</h3>
 <p>"[Child] will live with Parent A Sunday evening to Sunday evening in alternating weeks. Parent B will collect from school on the first day of their week and Parent A will collect at the end. If either parent is unable to collect, they will notify the other by 2pm that day and the other parent will collect instead."</p></div>

 <h3>2. Time with each parent</h3>
 <p>Detail regular time arrangements with enough specificity that both parents can follow the plan without needing to negotiate each week. Consider:</p>
 <ul>
   <li>Weekday and weekend routine during term time</li>
   <li>Before and after school arrangements</li>
   <li>How overnight stays are scheduled</li>
   <li>What happens when the child is sick</li>
 </ul>

 <h3>3. School holidays</h3>
 <p>School holidays are a common flashpoint. Set out exactly how each holiday period is divided — don't leave it as "to be agreed each time".</p>
 <figure class="tbl"><table>
 <caption>Common holiday allocation approaches</caption>
 <thead><tr><th>Holiday period</th><th>Approach A (split evenly)</th><th>Approach B (alternating years)</th></tr></thead>
 <tbody>
 <tr><td>Christmas</td><td>First half / second half alternating years</td><td>Parent A odd years, Parent B even years</td></tr>
 <tr><td>Easter</td><td>Good Friday weekend / Easter Monday weekend alternating</td><td>Opposite to Christmas allocation</td></tr>
 <tr><td>School term breaks</td><td>First week / second week each break</td><td>Alternating school holiday periods</td></tr>
 <tr><td>Winter holidays</td><td>Split evenly, parents choose halves</td><td>Alternating years</td></tr>
 </tbody></table></figure>

 <h3>4. Special occasions</h3>
 <p>Specify what happens on birthdays, Mother's Day, Father's Day, and significant cultural or religious occasions. These are predictable pressure points — plan for them in advance.</p>

 <h3>5. Major decision-making</h3>
 <p>The <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act</a> distinguishes between day-to-day decisions (each parent makes these during their time) and long-term decisions about the child's welfare. Specify how you'll handle:</p>
 <ul>
   <li><strong>Education</strong> — which school, subject choices, tutoring, extracurriculars</li>
   <li><strong>Health</strong> — routine medical appointments, elective procedures, choice of doctor or dentist</li>
   <li><strong>Religion and culture</strong> — religious upbringing and cultural practices</li>
   <li><strong>Travel</strong> — interstate and overseas holidays, passport applications</li>
   <li><strong>Name changes</strong></li>
 </ul>
 <p>Most plans provide for joint decision-making on major issues, with a process for resolving disagreement — such as mediation — before either parent can act unilaterally.</p>

 <h3>6. Communication between parents</h3>
 <p>Agree on how you'll communicate — about the children, not about each other. Many plans specify:</p>
 <ul>
   <li>Preferred channel (email, a co-parenting app, text)</li>
   <li>Expected response times for non-urgent matters</li>
   <li>How to handle urgent or emergency communication</li>
   <li>Whether a parent can contact the children during the other's time, and how</li>
 </ul>

 <h3>7. Travel and relocation</h3>
 <p>Address domestic and international travel separately. For overseas travel, specify notice periods, passport arrangements, and what documentation the travelling parent will carry. Relocation — one parent moving significantly further away — is one of the most contested issues in family law. Even if it seems unlikely now, consider including a process for how it would be handled.</p>

 <h3>8. Changeover arrangements</h3>
 <p>Specify exactly where and when changeovers happen. "At school" is clearer and lower-conflict than "at the front door". Include a fallback: what happens if a parent is more than 30 minutes late?</p>

 <h3>9. Dispute resolution</h3>
 <p>Include a clause committing both parents to return to mediation before escalating any dispute to court. This is one of the most valuable provisions in any parenting plan — it keeps minor disagreements from becoming expensive litigation.</p>

 <h3>10. Review and variation</h3>
 <p>Children's needs change. Build in a scheduled review — annually, or when a child changes school — and agree on a process for proposing changes. A plan that can be updated by agreement is far more durable than one that can only be changed through court.</p>

 <h2>Parenting plan vs consent orders: which do you need?</h2>
 <figure class="tbl"><table>
 <thead><tr><th></th><th>Parenting plan</th><th>Consent orders</th></tr></thead>
 <tbody>
 <tr><td>Legally binding</td><td>No — but courts consider it</td><td>Yes — directly enforceable</td></tr>
 <tr><td>Court involvement</td><td>None</td><td>Registered with court (no hearing)</td></tr>
 <tr><td>Flexibility to vary</td><td>High — by agreement</td><td>Lower — requires consent or court order</td></tr>
 <tr><td>Cost</td><td>Lower</td><td>Slightly higher (court filing fee)</td></tr>
 <tr><td>Best for</td><td>Early-stage, cooperative arrangements</td><td>Where you want certainty and enforceability</td></tr>
 </tbody></table></figure>

 <h2>Common mistakes in parenting plans</h2>
 <ul>
   <li><strong>Too vague</strong> — "reasonable time with each parent" sounds flexible but causes constant negotiation and disputes.</li>
   <li><strong>No holiday detail</strong> — leaving holidays as "to be agreed" is the most common source of conflict.</li>
   <li><strong>No changeover specifics</strong> — ambiguity about time and place breeds conflict at handover.</li>
   <li><strong>Forgetting the children's activities</strong> — who drives to sport, who pays for extracurriculars, what happens when activities conflict with changeover?</li>
   <li><strong>No review mechanism</strong> — a plan written when a child is 4 won't suit a teenager.</li>
 </ul>

 <h2>How mediation helps you build a better plan</h2>
 <p>A mediator doesn't draft the plan for you — they help you and the other parent work through each section together, drawing out the details that matter, surfacing disagreements early, and finding workable solutions. The result is a plan both parents have genuinely agreed to, which is what makes it last. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
 """,
 [("What should be included in a parenting plan in Australia?",
   "Living arrangements, weekly time with each parent, school holiday allocation, special occasions, major decision-making, communication between parents, travel, changeover arrangements, dispute resolution, and how the plan will be reviewed. The more specific it is, the fewer disputes arise."),
  ("Is a parenting plan legally binding in Australia?",
   "No. A parenting plan is not a court order and cannot be directly enforced. However, a court will consider it in any later dispute, and it is far more useful than a verbal agreement. To make arrangements directly enforceable, formalise them as consent orders."),
  ("Do I need a lawyer to make a parenting plan?",
   "No. A parenting plan can be made directly between parents, and a mediator can help you cover everything thoroughly. Independent legal advice is recommended before formalising anything as consent orders."),
  ("Can a parenting plan be changed later?",
   "Yes — by written agreement between both parents. The Family Law Act allows parenting plans to be varied or replaced by a later signed agreement. Build a review process into the plan itself so changes happen constructively."),
  ("What is the difference between a parenting plan and consent orders?",
   "A parenting plan is a private written agreement — flexible but not directly enforceable. Consent orders are court-approved and enforceable. Many families start with a parenting plan and convert to consent orders once arrangements are settled."),
  ("How specific should a parenting plan be?",
   "Specific enough that neither parent has to negotiate week by week. Vague terms like 'reasonable time' cause disputes. Specify days, times, locations, and fallback arrangements for common scenarios like illness or late pick-up.")],
 "Parenting Plan Template",
 "Build a parenting plan that <em>actually works</em>.",
 "Book a free initial consultation and let an accredited mediator help you create a complete, child-focused parenting plan.",
 tool_html=PARENTING_BUILDER)

# ---- BFA OR CONSENT ORDERS ----
build("bfa-or-consent-orders",
 "BFA or Consent Orders? Which Is Right for You (2026 Guide)",
 "BFA or consent orders? Compare the two ways to formalise a property settlement in Australia — cost, finality, flexibility and when each applies. Free consultation.",
 "Know which one to choose before you sign",
 "BFA or Consent Orders",
 "Once you've reached an agreement on property, you need to make it legally binding. There are two main routes: consent orders and binding financial agreements. They work differently, cost differently, and suit different situations. This guide explains which is right for you.",
 "Consent orders are approved by the Federal Circuit and Family Court — simpler, cheaper, and suitable for most separating couples. A binding financial agreement (BFA) is a private contract that offers more flexibility, can be made before or during a relationship, but requires independent legal advice from a lawyer for each party. For most people finalising a separation, consent orders are the better starting point.",
 """
 <h2>What are consent orders?</h2>
 <p><a href="/consent-orders/">Consent orders</a> are orders made by the Federal Circuit and Family Court of Australia that reflect an agreement the parties have already reached. You don't attend court — a registrar reviews the proposed orders on the papers and, if satisfied they are just and equitable, approves them. Once approved, they are binding court orders with the full force of law behind them.</p>
 <p>Consent orders can cover property (real estate, superannuation, savings, debts), parenting arrangements, and spousal maintenance. They are the most common way to formalise a property settlement after separation.</p>

 <h2>What is a binding financial agreement (BFA)?</h2>
 <p>A <a href="/financial-agreements-mediation/">binding financial agreement</a> is a private contract between two people that sets out how assets, finances and (in some cases) maintenance will be handled. Unlike consent orders, a BFA is never reviewed or approved by a court — it takes effect as a private contract once each party has received independent legal advice from a lawyer and both lawyers have signed a statement confirming that advice was given.</p>
 <p>BFAs can be made at three stages: before a marriage or de facto relationship begins (a "prenup"), during the relationship, or after separation. This flexibility is their main advantage.</p>

 <h2>Side-by-side comparison</h2>
 <figure class="tbl"><table>
 <thead><tr><th></th><th>Consent orders</th><th>Binding financial agreement</th></tr></thead>
 <tbody>
 <tr><td>Court involvement</td><td>Yes — court reviews and approves</td><td>No — private contract</td></tr>
 <tr><td>When it can be made</td><td>On or after separation</td><td>Before, during or after the relationship</td></tr>
 <tr><td>Independent legal advice required</td><td>Not mandatory, but recommended</td><td>Mandatory for both parties — agreement is void without it</td></tr>
 <tr><td>Typical cost (legal fees)</td><td>$1,500–$3,500 combined</td><td>$3,000–$8,000+ combined (each party needs own lawyer)</td></tr>
 <tr><td>What it can cover</td><td>Property, super, parenting, maintenance</td><td>Property, super, maintenance (not parenting)</td></tr>
 <tr><td>Grounds to challenge</td><td>Fraud, non-disclosure, impracticable</td><td>Non-disclosure, undue influence, no legal advice</td></tr>
 <tr><td>Suitable for prenup</td><td>No</td><td>Yes</td></tr>
 </tbody></table></figure>

 <h2>Which should you choose?</h2>
 <p>For most separating couples finalising a property split, <strong>consent orders are the better default</strong>. They are cheaper, faster, cover parenting as well as property, and carry the weight of court approval — which makes them harder to challenge. The court's "just and equitable" check is a feature, not a bureaucratic hurdle: it protects both parties.</p>
 <p>A BFA makes more sense when:</p>
 <ul>
   <li>You want to make arrangements before or during a relationship (a prenup or mid-relationship agreement)</li>
   <li>You have strong privacy reasons to keep the agreement entirely off court records</li>
   <li>Your situation is genuinely unusual in a way consent orders can't accommodate</li>
   <li>You are de facto and separated more than two years ago (outside the window for court property orders)</li>
 </ul>

 <h2>What happens if you do nothing?</h2>
 <p>Not formalising your settlement is the most common — and most costly — mistake. Without consent orders or a BFA:</p>
 <ul>
   <li>Either party can return to court to claim a share of assets years later</li>
   <li>The other person's future spouse, creditors or estate may have a claim over assets you thought were yours</li>
   <li>Time limits apply: married couples have 12 months from the date of divorce; de facto couples have 24 months from separation</li>
 </ul>
 <div class="callout"><h3>The hard part is reaching the agreement</h3>
 <p>Whichever instrument you use, the real work is negotiating a fair outcome — which is exactly what <a href="/property-settlement-mediation/">property settlement mediation</a> does in a single day. Once agreement is reached, your lawyers can draft and formalise it. <a href="/property-settlement-mediation/">See property settlement mediation →</a></p></div>

 <h2>Cost comparison: a worked example</h2>
 <p>For a typical couple with a house, super, and one shared car:</p>
 <figure class="tbl"><table>
 <thead><tr><th>Step</th><th>Via consent orders</th><th>Via BFA</th></tr></thead>
 <tbody>
 <tr><td>Mediation (property settlement)</td><td>~$3,000–$5,000 shared</td><td>~$3,000–$5,000 shared</td></tr>
 <tr><td>Legal drafting</td><td>~$1,500–$3,000 combined</td><td>~$3,000–$8,000 combined</td></tr>
 <tr><td>Court filing fee</td><td>$175 (2026)</td><td>Nil</td></tr>
 <tr><td>Total (approximate)</td><td><strong>$5,000–$8,000</strong></td><td><strong>$6,000–$13,000</strong></td></tr>
 </tbody></table></figure>
 <p>Both paths cost a fraction of contested litigation, which typically runs $30,000–$150,000 per side. <a href="/family-law-cost-estimator/">See the full cost comparison →</a></p>
 """,
 [("Is a BFA or consent orders cheaper?",
   "Consent orders are generally cheaper. A BFA requires mandatory independent legal advice from a separate lawyer for each party, which adds cost. For most separating couples, consent orders are the more cost-effective route."),
  ("Can a BFA be made before marriage?",
   "Yes. A binding financial agreement can be made before, during or after a marriage or de facto relationship. One made before is often called a prenup. Consent orders can only be made on or after separation."),
  ("Do I have to go to court for consent orders?",
   "No. Consent orders are reviewed on the papers by a registrar — there is no hearing. You submit the application and draft orders, pay the filing fee, and the court approves them without anyone attending."),
  ("Are consent orders harder to overturn than a BFA?",
   "Generally yes, because they carry court approval. A BFA can be set aside on contract-related grounds like non-disclosure or failure to obtain independent legal advice. Both are binding when properly made."),
  ("What if I miss the time limit?",
   "Married couples must apply for property orders within 12 months of their divorce becoming final. De facto couples have 24 months from the date of separation. After these deadlines, you need court permission to proceed, which adds cost and uncertainty."),
  ("Can consent orders cover both property and parenting?",
   "Yes — consent orders are the only instrument that can cover both in the same document. A BFA cannot include parenting arrangements.")],
 "BFA or Consent Orders",
 "Choose the right way to make it binding.",
 "Book a consultation and we'll help you reach agreement and formalise it the right way for your situation.")

# ---- GETTING READY FOR SEPARATION ----
build("getting-ready-for-separation",
 "Getting Ready for Separation | Practical Checklist 2026",
 "A practical guide to preparing for separation in Australia — finances, documents, children, legal steps and wellbeing. What to do first, what to avoid, and how mediation helps.",
 "The first steps you take matter most",
 "Getting Ready for Separation",
 "The decisions you make in the first weeks of separation have a disproportionate effect on the months that follow. This practical guide covers every step — financial, legal, parenting and personal — so you're prepared rather than reactive, and so the process ahead is as straightforward as it can be.",
 "To get ready for separation, record your separation date, gather all financial documents, understand the full asset pool, think carefully about parenting arrangements, and get an early understanding of your legal options. Acting early and systematically protects your interests and makes mediation — the fastest path to resolution — far more productive.",
 """
 <h2>Step 1: Record your separation date</h2>
 <p>Your separation date is more important than most people realise. It starts the clock on time limits for property applications — 12 months from divorce for married couples, 24 months from separation for de facto couples. It also affects Centrelink entitlements, tax, and how assets are valued in a property settlement.</p>
 <p>Write down the date, note it in a message to yourself, or send a brief email — something dated and retrievable. If you're separating under one roof, see our guide to <a href="/separation-under-one-roof/">separation under one roof</a> for what else you'll need to document.</p>

 <h2>Step 2: Gather your financial documents</h2>
 <p>A property settlement requires a complete and honest picture of everything you own and owe, together and separately. Start collecting:</p>
 <figure class="tbl"><table>
 <caption>Financial documents to gather</caption>
 <thead><tr><th>Category</th><th>What to collect</th></tr></thead>
 <tbody>
 <tr><td>Property</td><td>Recent valuations or sales data, mortgage statements, council rates notices</td></tr>
 <tr><td>Superannuation</td><td>Latest statements for all super funds — both yours and your partner's</td></tr>
 <tr><td>Bank accounts</td><td>Statements for all accounts — joint and individual — for the past 12–24 months</td></tr>
 <tr><td>Income</td><td>Payslips, tax returns, business financials if self-employed</td></tr>
 <tr><td>Investments</td><td>Share portfolios, managed funds, cryptocurrency holdings</td></tr>
 <tr><td>Vehicles</td><td>Registration documents, finance contracts</td></tr>
 <tr><td>Debts</td><td>Credit card statements, personal loan balances, HECS, any guarantees</td></tr>
 <tr><td>Business interests</td><td>Trust deeds, company documents, accountant valuations</td></tr>
 </tbody></table></figure>
 <p>Both parties are legally required to make full financial disclosure in any property settlement. Gathering your own documents early means you're not dependent on your former partner's cooperation later.</p>

 <h2>Step 3: Understand the full asset pool</h2>
 <p>The "asset pool" in a property settlement includes everything owned by either of you — jointly or individually — minus all liabilities. Under the <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act 1975</a>, assets acquired before the relationship, during it, and after separation may all be relevant. Make a list:</p>
 <ul>
   <li>The family home and any investment properties</li>
   <li>Superannuation for both parties (treated as a separate asset class)</li>
   <li>Bank savings and term deposits</li>
   <li>Shares, managed funds, cryptocurrency</li>
   <li>Vehicles, boats, caravans</li>
   <li>Businesses, trust interests, partnership shares</li>
   <li>Inheritances received (timing and use matters)</li>
   <li>All debts: mortgage, car loans, credit cards, personal loans</li>
 </ul>

 <h2>Step 4: Think clearly about the children</h2>
 <p>If you have children, their arrangements are the most important thing to get right — and the most emotionally charged. Before any conversations with your former partner, think through:</p>
 <ul>
   <li>Where the children would live day-to-day and who would do school drop-off and pick-up</li>
   <li>How time would be divided week to week, and over school holidays</li>
   <li>How major decisions — schooling, health, travel — would be made</li>
   <li>What the children's routines, friendships and activities are, and how to protect them</li>
 </ul>
 <p>The <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act</a> requires that the best interests of the child are the paramount consideration in any parenting arrangement. Keeping that principle front of mind — rather than what feels fair to you as a parent — produces better outcomes and reduces conflict. See our <a href="/parenting-plan-template/">parenting plan template</a> for what a thorough arrangement covers.</p>

 <h2>Step 5: Protect your immediate financial position</h2>
 <p>While you're getting organised:</p>
 <ul>
   <li><strong>Open a personal bank account</strong> in your own name if you don't already have one, and redirect your income to it</li>
   <li><strong>Don't drain joint accounts</strong> — this is treated seriously by courts and will be held against you in a property settlement</li>
   <li><strong>Update your will and superannuation beneficiary nominations</strong> — these don't change automatically on separation</li>
   <li><strong>Notify Centrelink</strong> if you receive family payments — your entitlements change from the date of separation</li>
   <li><strong>Review any joint insurances</strong> — home, contents, health — and consider your coverage going forward</li>
 </ul>

 <h2>Step 6: Understand your legal options early</h2>
 <p>Many people assume separation means lawyers and court. In most cases it doesn't have to. The options, roughly in order of cost and conflict:</p>
 <figure class="tbl"><table>
 <thead><tr><th>Option</th><th>Best for</th><th>Typical cost</th></tr></thead>
 <tbody>
 <tr><td><a href="/family-law-mediation/">Mediation</a></td><td>Most separating couples — property and parenting</td><td>$3,000–$8,000 total shared</td></tr>
 <tr><td>Collaborative law</td><td>Where both parties have lawyers but want to avoid court</td><td>$10,000–$30,000</td></tr>
 <tr><td>Negotiation via lawyers</td><td>Complex matters or where one party won't engage</td><td>$15,000–$60,000+</td></tr>
 <tr><td>Contested court proceedings</td><td>Last resort — when nothing else works</td><td>$30,000–$150,000+ per side</td></tr>
 </tbody></table></figure>
 <p>Mediation resolves over 90% of matters. Most people who try it avoid court entirely. <a href="/family-law-mediation/">Read more about family law mediation →</a></p>

 <h2>A note on safety</h2>
 <p>If your situation involves family violence or you feel unsafe, your safety comes first. Call 000 in an emergency. The <a href="https://1800respect.org.au" target="_blank" rel="noopener">1800RESPECT helpline (1800 737 732)</a> provides confidential support 24 hours a day. Mediation may not be appropriate where there is family violence — tell us about any safety concerns and we will advise the safest options, including arrangements where you and your former partner are never in the same room.</p>

 <div class="callout"><h3>You don't need to have it all sorted before you call us</h3>
 <p>Most people contact us before they've gathered everything. A free initial consultation helps you understand what comes next, what to prioritise, and what mediation can realistically achieve in your situation — no obligation.</p></div>
 """,
 [("What should I do first when separating?",
   "Record your separation date, open a personal bank account, gather your financial documents, and get an early understanding of your options. Acting early and systematically protects your interests and makes the process ahead much smoother."),
  ("What financial documents do I need for separation?",
   "Property valuations and mortgage statements, superannuation statements for both parties, bank statements for all accounts, payslips and tax returns, and details of all debts. Both parties must make full financial disclosure in any property settlement."),
  ("How do I protect my children during separation?",
   "Keep conflict away from them, maintain their routines, and focus on what works for them rather than what feels fair to you. A parenting plan negotiated through mediation gives children stability and keeps arrangements off the court's docket."),
  ("When should I update my will after separation?",
   "Immediately. Your will does not automatically change on separation, and your former partner may remain a beneficiary until it is updated. Also update your superannuation beneficiary nominations, which are separate from your will."),
  ("Do I have to go to court when I separate?",
   "No. Most separating couples resolve property and parenting matters through mediation, then formalise the agreement as consent orders. Court is a last resort, usually only needed when one party refuses to engage or there is a serious safety issue."),
  ("What happens if I miss the time limits for property settlement?",
   "Married couples have 12 months from the date of divorce to apply for property orders; de facto couples have 24 months from separation. After those dates you need the court's permission, which adds cost and uncertainty. Act before the deadline.")],
 "Getting Ready for Separation",
 "Face it prepared, not overwhelmed.",
 "Book a free initial consultation and we'll help you understand exactly what to do next — with no obligation.")

# ---- FAMILY LAW COST ESTIMATOR ----
build("family-law-cost-estimator",
 "Family Law Cost Estimator | Mediation vs Court Costs 2026",
 "How much does a family law matter cost in Australia? Real figures for mediation, lawyers and court — by dispute type. See why mediation saves tens of thousands.",
 "Know the real numbers before you decide",
 "Family Law Cost Estimator",
 "The cost of resolving a family law matter in Australia varies enormously — from a few thousand dollars through mediation to six figures in contested litigation. This guide gives you real cost figures by dispute type, explains what drives costs up, and shows how to estimate your own situation.",
 "Mediation typically costs $3,000–$8,000 total shared between the parties, regardless of complexity. A contested family law matter through court typically costs each party $30,000–$150,000+ in legal fees and takes one to three years. The path you choose — not the complexity of your matter — is the single biggest driver of cost.",
 """
 <h2>The single biggest cost driver: path choice</h2>
 <p>Most people assume family law cost is determined by how complex their matter is. It isn't. The single biggest driver is whether you resolve through mediation or through contested court proceedings. A highly complex property matter resolved through mediation costs a small fraction of a simple matter fought through court.</p>
 <p>The reason: court runs on hourly legal fees, accumulated over months or years. Mediation runs on a fixed session fee, resolved in a day.</p>

 <h2>Cost by dispute type: mediation vs court</h2>
 <figure class="tbl"><table>
 <caption>Approximate costs by dispute type (2026, Australia)</caption>
 <thead><tr><th>Dispute type</th><th>Mediation (total, shared)</th><th>Contested court (per party)</th></tr></thead>
 <tbody>
 <tr><td>Parenting arrangements</td><td>$2,500–$5,000</td><td>$25,000–$80,000</td></tr>
 <tr><td>Property settlement (straightforward)</td><td>$3,000–$6,000</td><td>$30,000–$80,000</td></tr>
 <tr><td>Property settlement (complex — business, trust)</td><td>$5,000–$10,000</td><td>$60,000–$200,000+</td></tr>
 <tr><td>Parenting + property combined</td><td>$4,000–$8,000</td><td>$40,000–$150,000+</td></tr>
 <tr><td>Spousal maintenance</td><td>$2,500–$5,000</td><td>$20,000–$60,000</td></tr>
 <tr><td>Estate dispute</td><td>$3,000–$7,000</td><td>$30,000–$120,000+</td></tr>
 <tr><td>Workplace dispute</td><td>$2,000–$5,000</td><td>$15,000–$80,000</td></tr>
 </tbody></table></figure>
 <p><em>Figures are estimates only. Actual costs depend on the number of sessions required, complexity, and whether legal advice is sought alongside mediation. Court costs include solicitor fees, barrister fees for hearings, and filing costs — and do not include the value of your own time over one to three years.</em></p>

 <h2>What's included in mediation costs</h2>
 <p>At Mediations Australia, mediation fees are fixed and transparent. They cover:</p>
 <ul>
   <li>A free initial consultation</li>
   <li>Mediator preparation and intake</li>
   <li>The mediation session (typically a full day)</li>
   <li>A written record of outcomes or heads of agreement</li>
 </ul>
 <p>Mediation fees are typically shared equally between the parties. See our <a href="/our-fee-structure/">full fee structure →</a></p>

 <h2>What's not included — and what you might also need</h2>
 <p>Mediation reaches agreement. Formalising that agreement is a separate step:</p>
 <figure class="tbl"><table>
 <thead><tr><th>Formalisation step</th><th>Approximate cost</th></tr></thead>
 <tbody>
 <tr><td>Consent orders (property + parenting)</td><td>$1,500–$3,000 combined legal drafting + $175 court fee</td></tr>
 <tr><td>Binding financial agreement (BFA)</td><td>$3,000–$8,000 combined (each party needs own lawyer)</td></tr>
 <tr><td>Section 60I certificate (parenting)</td><td>Included in mediation fee</td></tr>
 </tbody></table></figure>

 <h2>What drives costs up in court</h2>
 <p>Court costs compound over time. The typical escalation path:</p>
 <ol>
   <li><strong>Initial legal advice and letters</strong> — $3,000–$8,000</li>
   <li><strong>Interim hearings</strong> (urgent orders for parenting or property) — $5,000–$20,000 per hearing</li>
   <li><strong>Disclosure and subpoenas</strong> — $5,000–$15,000</li>
   <li><strong>Expert reports</strong> (valuations, family reports) — $3,000–$10,000</li>
   <li><strong>Final hearing preparation</strong> — $15,000–$40,000</li>
   <li><strong>Final hearing</strong> (barrister, solicitor, 2–5 days) — $20,000–$80,000</li>
 </ol>
 <p>These amounts apply to <em>each party</em>. In family law, costs are rarely awarded — meaning each side almost always bears their own legal bill regardless of outcome.</p>

 <h2>The hidden costs of litigation</h2>
 <p>The financial cost is only part of it. Contested court proceedings also cost:</p>
 <ul>
   <li><strong>Time</strong> — one to three years to a final hearing, during which nothing is resolved</li>
   <li><strong>The asset pool itself</strong> — legal fees are paid from the assets being divided. A couple with a $600,000 property can spend $150,000 in combined legal fees fighting over how to split it.</li>
   <li><strong>The co-parenting relationship</strong> — adversarial proceedings make it harder to cooperate on parenting for the years ahead</li>
   <li><strong>Wellbeing</strong> — the stress of protracted litigation has measurable effects on health and work performance</li>
 </ul>

 <h2>Worked example: the same matter, two paths</h2>
 <p>A Sydney couple separating with a $950,000 home, $280,000 combined super, and two children aged 8 and 11:</p>
 <figure class="tbl"><table>
 <thead><tr><th></th><th>Via mediation</th><th>Via contested court</th></tr></thead>
 <tbody>
 <tr><td>Time to resolution</td><td>1 day</td><td>18–30 months</td></tr>
 <tr><td>Mediation / legal fees (combined)</td><td>$7,000</td><td>$120,000–$200,000</td></tr>
 <tr><td>Asset pool preserved</td><td>~$1,223,000</td><td>~$1,023,000–$1,103,000</td></tr>
 <tr><td>Ongoing co-parenting relationship</td><td>Intact</td><td>Damaged</td></tr>
 </tbody></table></figure>

 <div class="callout"><h3>Early resolution saves the most</h3>
 <p>Costs in family law compound with time. The earlier you resolve — ideally through mediation before lawyers are deeply involved — the more of the asset pool stays with your family. <a href="/family-law-mediation/">See what mediation involves →</a></p></div>
 """,
 [("How much does family law mediation cost in Australia?",
   "Mediation typically costs $3,000–$8,000 total, shared between the parties. This covers the mediator's preparation, the session (usually a full day), and a written record of outcomes. Formalising the agreement as consent orders adds approximately $1,500–$3,000 in legal fees."),
  ("How much does a contested family law case cost?",
   "A contested family law matter typically costs each party $30,000–$150,000 in legal fees, depending on complexity and how far it runs. In most cases each side bears their own costs regardless of outcome."),
  ("Why is mediation so much cheaper than court?",
   "Mediation resolves in a single day on a fixed fee. Court runs on hourly legal billing accumulated over one to three years, with multiple hearings, disclosure processes, and expert reports — all of which compound costs significantly."),
  ("Are mediation costs split between the parties?",
   "Usually yes. Mediation fees are typically shared equally, which halves the effective cost for each party. Each party pays their own lawyers if they choose to have legal advice alongside the process."),
  ("What happens to legal costs in court — does the winner get them paid?",
   "Generally no. Family law courts rarely award costs, meaning each party almost always pays their own legal fees regardless of outcome. This is one reason mediation — where costs are low and shared — is the better financial choice for most families."),
  ("How can I get an accurate cost estimate for my situation?",
   "Book a free initial consultation. Costs depend on the specific issues in dispute, the asset pool, and the level of cooperation between parties — a short conversation gives a far more accurate picture than a generic guide.")],
 "Family Law Cost Estimator",
 "See what you could save.",
 "Book a free initial consultation for an honest estimate of what resolving your matter will cost — and how much mediation can save you.")

# ---- SEPARATION UNDER ONE ROOF ----
build("separation-under-one-roof",
 "Separation Under One Roof | How It Works in Australia",
 "Separated but still living together? Learn how separation under one roof works in Australia, what you need to show, and how mediation helps. Free consultation.",
 "Managing together until you can live apart",
 "Separation Under One Roof",
 "Many couples separate while still living in the same home — for financial reasons, for the children, or while they sort out next steps. This guide explains how 'separation under one roof' is recognised in Australia and how to handle it.",
 "Separation under one roof means a couple has separated but continues to live in the same home. It is recognised in Australia, but you may need to show that the relationship has genuinely ended — through changes in finances, sleeping arrangements, and how you present to others.",
 """
 <h2>What is separation under one roof?</h2>
 <p>"Separation under one roof" describes a couple who have decided their relationship is over but continue, at least for a time, to live in the same home. It is common and entirely valid. People stay under one roof for financial reasons — running two households is expensive — for the stability of the children, while a property settlement is sorted out, or simply because finding somewhere else to live takes time.</p>
 <p>What matters legally is not whether you share an address, but whether the relationship has genuinely ended. In Australia you can be separated for every legal purpose — divorce, property settlement, Centrelink — while still sleeping under the same roof, provided you can show the marriage or de facto relationship is over in substance.</p>

 <h2>Is separation under one roof legally recognised in Australia?</h2>
 <p>Yes. Under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, separation happens when at least one person forms the intention to end the relationship, communicates that to the other, and acts on it. Nothing in the law requires you to live at different addresses. The courts have long accepted that a couple can be "separated but living under the same roof", and the <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a> has a specific process for proving it when you apply for a divorce.</p>
 <p>This matters because a divorce in Australia requires you to be separated for at least <strong>12 months and one day</strong> before you can apply. Time spent separated under one roof counts towards that 12 months — you just need to be able to evidence it.</p>

 <h2>How do you show you've genuinely separated?</h2>
 <p>Because you're still living together, you may need to demonstrate that the relationship has actually ended rather than merely become strained. No single factor is decisive; a court or agency looks at the overall picture across several areas of life.</p>
 <figure class="tbl"><table><caption>What changes when a couple separates under one roof</caption>
 <thead><tr><th>Area of life</th><th>What genuine separation can look like</th></tr></thead>
 <tbody>
 <tr><td>Sleeping arrangements</td><td>Separate bedrooms, or one partner moving to another part of the home</td></tr>
 <tr><td>Finances</td><td>Separate bank accounts, divided bills, no longer pooling income</td></tr>
 <tr><td>Household tasks</td><td>Each person cooks, cleans and shops for themselves rather than for the couple</td></tr>
 <tr><td>Social life</td><td>Attending events separately; no longer presenting as a couple</td></tr>
 <tr><td>Others' knowledge</td><td>Family, friends and agencies such as Centrelink have been told you've separated</td></tr>
 </tbody></table></figure>
 <p>You don't need every box ticked. The point is to show a consistent pattern that the relationship has ended, not just a rough patch. Keeping a brief note of when things changed — when you moved to a separate room, when you split the accounts — makes this far easier to evidence later.</p>
 <div class="callout"><h3>The date of separation matters</h3>
 <p>Your date of separation sets the clock running on time limits for both divorce and property. It can also affect Centrelink entitlements and how assets are valued. If you're separated under one roof, pin the date down early so you understand exactly where you stand.</p></div>

 <h2>The affidavit you'll need when you apply for divorce</h2>
 <p>When you have lived under the same roof during the 12-month separation period, the court won't simply take your word for it. You will usually need to file an <strong>affidavit</strong> setting out the changes in your relationship — sleeping arrangements, finances, household duties and social life — together with a <strong>corroborating affidavit from an independent person</strong>, such as a friend or family member, who can confirm they understood you to be separated. The <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">FCFCOA divorce process</a> sets out exactly what these affidavits should cover.</p>
 <p>It sounds onerous, but in practice it is a short, factual statement. The earlier you have clarity on your separation date and the changes that followed, the simpler this step becomes.</p>

 <h2>How your separation date affects time limits</h2>
 <p>Separation isn't only about divorce. It also starts the clock on the deadlines for finalising a property settlement, and those deadlines differ for married and de facto couples.</p>
 <figure class="tbl"><table><caption>Key time limits that run from your separation or divorce date</caption>
 <thead><tr><th>Step</th><th>Married couples</th><th>De facto couples</th></tr></thead>
 <tbody>
 <tr><td>Apply for divorce</td><td>After 12 months' separation</td><td>Not applicable</td></tr>
 <tr><td>Apply for a property settlement</td><td>Within 12 months of divorce becoming final</td><td>Within 24 months of separation</td></tr>
 <tr><td>Parenting arrangements</td><td>No time limit</td><td>No time limit</td></tr>
 </tbody></table></figure>
 <p>Applying after a deadline isn't impossible, but you need the court's permission, which adds cost and uncertainty. If a deadline is approaching, it is worth formalising arrangements while everyone is still cooperating. <a href="/property-settlement-after-separation/">Read our property settlement guide →</a></p>

 <h2>Centrelink, tax and finances while under one roof</h2>
 <p>Once you separate, you may be assessed as a single person for some payments even if you still share an address. <a href="https://www.servicesaustralia.gov.au/separating" target="_blank" rel="noopener">Services Australia</a> can recognise you as separated under one roof and may ask for a separation form and supporting details. Being upfront and consistent — the same separation date you'd give the court — keeps things clean across the board and avoids problems down the track.</p>

 <h2>Living together while separated: practical tips</h2>
 <p>The arrangement works best when expectations are clear. A few things make a real difference:</p>
 <ul>
   <li><strong>Agree on space and schedules</strong> — who uses common areas when, and how you'll handle meals, laundry and the bathroom.</li>
   <li><strong>Separate your money early</strong> — open individual accounts and divide responsibility for bills so nothing falls through the cracks.</li>
   <li><strong>Keep the children's routine steady</strong> — shield them from conflict and present a united, calm front about the practical changes.</li>
   <li><strong>Document the change</strong> — note your separation date and the adjustments that followed, which helps with both divorce and Centrelink later.</li>
   <li><strong>Plan the exit</strong> — treat the shared-roof period as temporary and agree a rough timeline for one person to move on.</li>
 </ul>

 <h2>How mediation helps when you're still living together</h2>
 <p>Living together while separated can be tense, and small frictions — bills, the school run, who uses the kitchen when — can escalate quickly. <a href="/family-law-mediation/">Mediation</a> provides a structured, neutral way to agree on living arrangements, finances and parenting while you remain under the same roof, and to plan an orderly transition out of it.</p>
 <p>A mediator can help you set practical ground rules for the household, work towards a <a href="/property-settlement-mediation/">property settlement</a> and <a href="/parenting-plan-mediation/">parenting arrangements</a>, and reach agreements you can later formalise as <a href="/consent-orders-explained/">consent orders</a>. If being in the same room is difficult, mediation can be conducted in separate rooms (shuttle mediation) or online. <a href="/getting-ready-for-separation/">See getting ready for separation →</a></p>
 """,
 [("Can you be separated while living together?",
   "Yes. 'Separation under one roof' is recognised in Australia under the Family Law Act 1975. You may need to show the relationship has genuinely ended despite living in the same home."),
  ("How do you prove separation under one roof?",
   "Through factors like separate sleeping arrangements, separated finances, reduced shared activities, and informing family, friends and relevant agencies that you've separated. When applying for divorce you'll usually file an affidavit, plus a corroborating affidavit from an independent person."),
  ("Does time separated under one roof count towards the 12 months for divorce?",
   "Yes. A divorce requires 12 months and one day of separation, and time spent separated under the same roof counts — provided you can evidence that the relationship had genuinely ended."),
  ("Why does the date of separation matter?",
   "It can affect time limits for divorce and property applications, Centrelink entitlements, and how assets are valued. Getting clarity on your separation date early helps you understand your legal position."),
  ("Can you still claim Centrelink as separated if you live together?",
   "You may be assessed as single even while sharing an address. Services Australia can recognise separation under one roof and may ask for a separation form and supporting details."),
  ("Can we mediate while still living together?",
   "Yes. Mediation can help you agree on living arrangements, finances and parenting while under one roof, and can be conducted in separate rooms or online if being together is difficult.")],
 "Separation Under One Roof",
 "Living together, living apart — <em>we can help</em>.",
 "Book a free initial consultation to work out living, financial and parenting arrangements while you're separated under one roof.")

# ---- UNFAIR DISMISSAL: 21-DAY RULE ----
build("unfair-dismissal-21-day-rule",
 "Unfair Dismissal: The 21-Day Rule Explained",
 "An unfair dismissal application must be lodged within 21 calendar days. This guide explains who can claim, what happens at conciliation, what a realistic outcome looks like, and how most cases resolve without a hearing.",
 "Know your deadline — and your options",
 "Unfair Dismissal: <em>The 21-Day Rule Explained</em>",
 "If you have just lost your job and something about it feels wrong, you are probably experiencing two things at once: the shock of the dismissal itself, and a creeping worry about what to do next. This guide is written for that moment. It explains the single most important fact about unfair dismissal in Australia — the 21-day deadline — along with who can claim, what actually happens after you lodge, what a realistic outcome looks like, and how most of these disputes resolve without anyone ever setting foot in a courtroom.",
 "An unfair dismissal application must be lodged with the Fair Work Commission within 21 calendar days of the dismissal taking effect — not 21 business days. The deadline is unforgiving: extensions are only granted in exceptional circumstances. The people who protect their position best are not the ones with the strongest cases — they are the ones who act quickly.",
 """
 <h2>Why 21 days is the number that matters most</h2>
 <p><strong>An unfair dismissal application must be lodged with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> within 21 calendar days after the dismissal takes effect</strong> — not 21 business days. Weekends and public holidays included. The clock starts on the day your dismissal takes effect, which is usually your last day of employment, not the day you were told and not the day your final pay landed.</p>
 <p>This deadline is unforgiving by design. The Commission can extend it only in "exceptional circumstances," and the bar for that is genuinely high. Being upset, being unsure of your rights, or simply not getting around to it are not exceptional circumstances. Serious illness, or being actively misled about your dismissal, might be — but you cannot count on it. <strong>The safest assumption is that once 21 days pass, the door closes.</strong></p>
 <p>The people who protect their position best are not the ones with the strongest cases — they are the ones who act quickly. If you are reading this in the first few days after losing your job, you are in the best possible position. If you are reading it on day 18, you need advice today.</p>

 <h2>Are you eligible to claim?</h2>
 <p>Not everyone who is dismissed can bring an unfair dismissal claim. You generally need to pass all of these:</p>
 <ul>
   <li><strong>You were dismissed</strong> — including constructive dismissal, where your employer's conduct left you no real choice but to resign. It does not include a genuine mutual agreement, or resigning simply because you found a better job.</li>
   <li><strong>You served the minimum employment period</strong> — at least 6 months of continuous service, or 12 months if your employer is a small business employer with fewer than 15 employees.</li>
   <li><strong>You are award-covered, agreement-covered, or earn under the high-income threshold</strong> — if neither an award nor an agreement applies, you must earn below the high-income threshold (indexed each 1 July). Above that threshold without coverage, unfair dismissal is not available.</li>
   <li><strong>It was not a genuine redundancy</strong> — a genuine redundancy is a complete defence to an unfair dismissal claim. See our <a href="/redundancy-was-it-genuine/">redundancy guide</a> for the legal test.</li>
 </ul>
 <p>If you do not qualify for unfair dismissal, that is not necessarily the end of the road. A <strong>general protections claim</strong> may be open to you — and in dismissal cases, that also runs on a 21-day deadline. Choosing the wrong claim, or missing which one applies, can be costly — which is exactly why early advice matters.</p>

 <h2>What "unfair" actually means</h2>
 <p>People often assume that if their dismissal felt unfair, it legally was. The test is narrower than that. The Commission asks whether the dismissal was <strong>"harsh, unjust or unreasonable."</strong> It weighs things like: was there a valid reason connected to your capacity or conduct? Were you told about that reason and given a chance to respond? Were you warned about performance problems before being dismissed for them? Were you allowed a support person in relevant meetings?</p>
 <p>A dismissal can be substantively justified but still unfair because the process was botched — and equally, a clumsy-feeling dismissal might still be lawful if the reason was sound and the process fair. Understanding this distinction early helps you form a realistic view rather than an emotional one.</p>

 <h2>What happens after you lodge</h2>
 <p>Here is the part that surprises most people: the overwhelming majority of unfair dismissal claims never reach a hearing. After you lodge (using Form F2), the employer files a response, and the Commission then offers <strong>conciliation</strong> — an informal, private, without-prejudice discussion designed to help both sides reach their own agreement.</p>
 <p>Conciliation is typically held about five weeks after the application, runs for up to <strong>90 minutes</strong>, and is usually conducted by phone or video. It is led by an independent conciliator who does not take sides and cannot impose a decision. Their job is to help both parties understand the strengths and weaknesses of their positions and explore whether a settlement is possible.</p>
 <p>Around <strong>three in four cases settle at or before conciliation.</strong> If a matter does not settle, it moves to a Member who, like a judge, will hear evidence and make a binding decision.</p>

 <h2>How to prepare for conciliation</h2>
 <p>Preparation is where you give yourself the best chance of a good outcome. Before the day: gather your employment contract, a recent payslip, any warning letters or the dismissal letter, and copies of the application and response. Read the other side's response carefully, even if you disagree with all of it. Write down your key issues and — importantly — the outcome you want and the outcome you would accept. These are rarely the same number, and knowing your range in advance stops you being caught flat-footed.</p>
 <p>A useful mindset: conciliation is about facts and interests, not about being proven right. Coming in wanting an apology and a formal finding of wrongdoing, rather than a practical settlement, is the most common way people talk themselves out of a good outcome.</p>

 <h2>What a realistic outcome looks like</h2>
 <p>Because conciliation lets parties agree to almost anything, settlements are flexible in a way a hearing can never be. Common elements include: a payment (often measured in weeks of pay, not a windfall); an agreed statement of service or reference (often more valuable than money for your next job); a non-disparagement agreement; a mutual release; and confidentiality over the terms.</p>
 <p>Compensation, if a matter runs all the way to a Member's decision, is <strong>capped</strong> (indexed annually) and reinstatement, while technically the primary remedy, is ordered relatively rarely.</p>
 <p>If you reach agreement, you will sign a <strong>Deed of Settlement</strong> or Terms of Agreement — a binding legal contract. If unrepresented, you are usually given a short cooling-off period (commonly three days) to change your mind — a genuinely important protection, so use that window to think clearly before the agreement becomes final.</p>

 <h2>Where private mediation fits</h2>
 <p>The Commission's conciliation is not your only option. Private mediation with an accredited mediator can run <em>before</em> you lodge — sometimes resolving things without a formal claim — or <em>alongside</em> a lodged claim, with one of our own mediators focused on your specific dispute, more time, and a more tailored process than a 90-minute phone call allows. This is often the better route in more complex or higher-value matters, or where the relationship is worth preserving. See our <a href="/unfair-dismissal-termination-mediation/">unfair dismissal and termination mediation page</a> for how we approach it.</p>
 """,
 [("Does the 21 days include weekends?",
   "Yes. It is 21 calendar days from when the dismissal takes effect, not 21 business days."),
  ("What if I have already missed the 21-day deadline?",
   "You can apply for an extension, but it is only granted in exceptional circumstances such as serious illness or being actively misled. Get advice immediately — do not assume you have no options, but do not assume you will get the extension either."),
  ("What does unfair dismissal actually mean?",
   "The Fair Work Commission asks whether your dismissal was 'harsh, unjust or unreasonable.' This looks at both the reason for dismissal and the fairness of the process — including whether you were warned, consulted, and given a chance to respond."),
  ("Do I need a lawyer at conciliation?",
   "No. Many people are unrepresented, and the process is designed to be accessible. But advice beforehand — especially on what your claim is realistically worth — can significantly change the outcome."),
  ("Will I have to face my employer?",
   "Not in person. Conciliation is by phone or video, and the conciliator can keep the parties in separate virtual rooms if being in the same meeting would be difficult."),
  ("How much will I get?",
   "There is no set figure. Many settlements are measured in weeks of pay. The value depends on the strength of your case, your length of service, your loss, and how both sides weigh the risk of a hearing."),
  ("Can private mediation help with an unfair dismissal?",
   "Yes. Private mediation can run before you lodge, to try to resolve directly with your employer, or alongside a lodged claim for a more tailored process than the Commission's 90-minute conciliation call allows.")],
 "Unfair Dismissal: The 21-Day Rule",
 "The 21-day rule rewards people who move quickly.",
 "If you have been dismissed and something feels wrong, the worst thing you can do is wait and hope for clarity. Talk to us now, while you still have your full options open.")

# ---- IS MEDIATION RIGHT FOR YOUR WORKPLACE DISPUTE? ----
build("is-mediation-right-for-workplace-dispute",
 "Is Mediation Right for Your Workplace Dispute?",
 "Mediation resolves most workplace disputes faster and more privately than a tribunal — but not every situation. This honest guide helps you decide whether mediation fits your dispute.",
 "An honest guide to help you decide",
 "Is Mediation Right for Your Workplace Dispute?",
 "Mediation resolves the large majority of workplace disputes faster, more privately, and more cheaply than a tribunal or court — and we believe in it deeply. But we are not going to pretend it is the right answer for every situation, because it isn't, and being honest about that is part of taking your circumstances seriously. This guide is designed to help you work out whether mediation genuinely fits your dispute, or whether another path should come first.",
 "Mediation works best when both people can come to the table able to speak freely and safely, with a genuine aim of finding a workable outcome. It may not be the right first step where there has been violence, serious harassment, a severe power imbalance, or where serious allegations need to be independently established first. An honest initial conversation will tell you which path fits.",
 """
 <h2>What mediation actually is — and is not</h2>
 <p>A mediator is a neutral third party who helps the people in a dispute have a structured, confidential conversation and reach their own agreement. The mediator does not judge, does not take sides, does not give evidence, and cannot impose a decision on anyone. <strong>Mediation is not a watered-down court.</strong> Nobody "wins" a mediation and nobody is "found" to have done anything. It is a facilitated negotiation, and its entire power comes from the fact that the parties themselves control the outcome.</p>
 <p>That design is what makes mediation brilliant for some disputes and unsuitable for others. It works when people can come to the table able to speak and negotiate freely. It struggles when they cannot.</p>

 <h2>When mediation works well</h2>
 <p>Mediation tends to be the best available option where several of these are true:</p>
 <ul>
   <li><strong>The relationship needs to continue, or ending it well matters.</strong> Colleagues who will keep working together, a manager and report who need a functioning relationship, or business partners who share an industry even after they separate. Mediation is built to preserve working relationships; litigation is built to end them.</li>
   <li><strong>Both people can participate freely and safely.</strong> This is the single most important condition.</li>
   <li><strong>The dispute is about interests, not just proving fault.</strong> Pay, conditions, workload, recognition, a communication breakdown, or a management relationship that has soured — these are exactly the kind of interest-based problems mediation excels at.</li>
   <li><strong>You want control over the outcome.</strong> In mediation you shape the resolution — an agreed reference, a payment, a change in how things are done, a dignified exit. A tribunal offers a limited menu of remedies and imposes whichever it chooses.</li>
   <li><strong>Speed and privacy matter.</strong> Most workplace mediations resolve in a single session and stay completely confidential. Tribunal decisions are public and can take many months.</li>
 </ul>
 <p>This covers a great many disputes: <a href="/unfair-dismissal-termination-mediation/">unfair dismissal and termination</a>, <a href="/redundancy-restructure-mediation/">redundancy disagreements</a>, many <a href="/general-protections-discrimination-mediation/">general protections matters</a>, <a href="/partnership-executive-exit-mediation/">partnership and executive exits</a>, and most everyday <a href="/workplace-investigations-grievance-mediation/">grievances</a>.</p>

 <h2>When mediation may not be the right first step</h2>
 <p>Here is where we are candid, because it matters. Mediation depends on both people being able to negotiate safely and on a reasonably equal footing. When that condition is absent, mediation can be ineffective at best and harmful at worst. It may not be the right first step where:</p>
 <ul>
   <li><strong>There has been violence, serious sexual harassment, or threats.</strong> Where the conduct at issue makes a safe, direct conversation impossible, putting the parties together is inappropriate. Safety comes before process, full stop.</li>
   <li><strong>There is a serious power imbalance that cannot be managed.</strong> Some imbalance is present in almost every workplace dispute, and a skilled mediator manages it routinely — through shuttle mediation, support people, and careful process design. But where the imbalance is so severe that one party genuinely cannot advocate for themselves, mediation may not deliver a fair outcome.</li>
   <li><strong>A party feels unsafe, intimidated, or fears reprisal.</strong> If someone cannot speak honestly because they fear the consequences, the conversation is not a real negotiation.</li>
   <li><strong>The behaviour is ongoing and needs to be stopped urgently.</strong> Where bullying or harassment is continuing, a stop-bullying application or work health and safety report may need to come first. See our <a href="/workplace-bullying-harassment-mediation/">bullying and harassment guide</a> for how these fit together.</li>
   <li><strong>Serious allegations need to be independently established.</strong> Where the dispute turns on whether serious misconduct actually happened — conduct that could lead to dismissal or carry legal consequences — a proper independent investigation usually needs to come first. Our <a href="/workplace-investigations-grievance-mediation/">workplace investigations guide</a> explains the investigate-versus-mediate decision.</li>
 </ul>
 <p>Importantly, "not the right first step" does not always mean "never." Mediation frequently has a valuable role <em>later</em> — after a dispute is de-escalated, after facts are established by an investigation, or once safety is assured — to repair the workplace and agree how people will work together going forward.</p>

 <h2>Two examples, to make it concrete</h2>
 <p>Consider two disputes that look similar on the surface but call for very different approaches.</p>
 <p>In the first, a team leader and a long-serving staff member have fallen into a pattern of friction. Meetings are tense, emails have an edge, and each feels the other is undermining them. There is no allegation of anything unsafe — just a working relationship that has gone wrong and is affecting the team. This is close to an ideal mediation case. A single session, with good preparation, could resolve it and reset the relationship.</p>
 <p>In the second, a junior employee has made a detailed complaint that a senior manager has been sexually harassing them and has implied their job is at risk if they speak up. Here, almost every warning sign is present: a serious allegation that needs to be established, a stark power imbalance, and a person who does not feel safe. Sending these two into a mediation room as a first step would be inappropriate. The right first steps are safety, support, and an independent investigation. Mediation might have a role much later — but not now, and not as a substitute for a proper process.</p>

 <h2>How a responsible mediator handles the risky cases</h2>
 <p>A responsible mediator does not simply take a booking and put two people in a room. Before any workplace mediation, there should be a <strong>screening and preparation stage</strong>: the mediator speaks with each party separately, listens for safety concerns and power imbalances, and forms a judgement about whether mediation is appropriate and, if so, how it should be run. That might mean a shuttle format where the parties never sit face to face, allowing support people, setting clear ground rules, or — where it is the right call — advising that mediation should not proceed yet. Screening is not a formality; it is a genuine safeguard.</p>
 """,
 [("Can my employer force me to mediate?",
   "No. Mediation is voluntary. You should never be pressured into a process that does not feel safe, and you can raise safety or power-imbalance concerns at any point."),
  ("If mediation is not right now, is it ruled out forever?",
   "No. It often becomes appropriate later — after an investigation, once a situation is de-escalated, or once safety is assured — to repair the workplace."),
  ("Will the mediator decide who is right?",
   "No. A mediator never judges or imposes a decision. If you want a binding ruling on the facts, mediation is not that — but very few workplace disputes actually benefit from a public ruling."),
  ("Is workplace mediation confidential?",
   "Yes. Mediation is confidential and conducted on a without-prejudice basis, which means what is said in the process generally cannot be used against you later — and that protection is a large part of what lets people speak openly and settle."),
  ("How do I know if mediation fits my specific situation?",
   "The honest test is a single question: can both people come to the table able to speak freely and safely, with a genuine aim of finding a workable outcome? If you are unsure, an initial no-obligation conversation will give you a straight assessment — including an honest answer when mediation is not the right step.")],
 "Is Mediation Right for Your Workplace Dispute?",
 "Get an honest assessment — <em>not a sales pitch</em>.",
 "Not sure whether mediation fits your situation? That is the most useful reason of all to talk to us. We will tell you honestly what your options are — including when mediation is not the right step.")

# ---- REDUNDANCY: WAS IT GENUINE? ----
build("redundancy-was-it-genuine",
 "Redundancy: Was It Genuine? The Legal Test Explained",
 "A genuine redundancy is a complete defence to unfair dismissal. This guide explains the three-part legal test, the consultation mistake employers make most often, and how to assess your situation.",
 "Know the three-part test before accepting it",
 "Redundancy: <em>Was It Genuine?</em>",
 "Being made redundant is one of the strangest kinds of job loss. Unlike being sacked for something you did, redundancy is supposed to be about the role, not the person — and yet it can feel intensely personal, especially when your position disappears but the work somehow doesn't, or when you are the only one let go in a 'restructure.' This guide explains what 'genuine redundancy' actually means under Australian law, why the answer decides whether you can challenge it, the step employers most often get wrong, and how these disputes are resolved without a courtroom fight.",
 "Under section 389 of the Fair Work Act, a dismissal is only a genuine redundancy if all three conditions are met: the job is no longer required by anyone; the employer complied with any applicable consultation obligation; and redeployment was not reasonable. Miss any one element and the redundancy may not be genuine — opening the door to an unfair dismissal claim. Employers routinely assume the business reason alone is enough. It isn't.",
 """
 <h2>Why "genuine" is the whole ballgame</h2>
 <p>Here is the fact that changes everything: a genuine redundancy is a complete <strong>defence</strong> to an unfair dismissal claim. If your redundancy was genuine, you generally cannot bring an unfair dismissal case, no matter how upsetting the situation. But if your redundancy was <em>not</em> genuine — even where there was a real business reason behind it — that defence falls away, and an unfair dismissal claim can proceed on its merits.</p>
 <p>The question is not just "did the business have a reason?" It is "did this dismissal meet every element of the legal test for genuine redundancy?" Employers routinely assume the first question is the only one that matters. It isn't. And that gap is where a great many valid claims live.</p>

 <h2>The three-part test under section 389</h2>
 <p>Under section 389 of the <em>Fair Work Act 2009</em> (Cth), a dismissal is only a genuine redundancy if <strong>all three</strong> of the following are satisfied. Miss one, and it is not genuine.</p>
 <ol>
   <li><strong>The job is no longer required by anyone.</strong> The role must have genuinely ceased to be needed because of changes in the operational requirements of the business — a downturn, a restructure, automation, a merger, closing a site. The key word is <em>anyone</em>. If your duties were simply handed to someone else, or a near-identical role was created under a new title, the job arguably still exists and the redundancy may not be genuine. Replacing you with a cheaper worker doing the same job is not redundancy.</li>
   <li><strong>The employer complied with any consultation obligation.</strong> This is the big one — see below.</li>
   <li><strong>Redeployment was not reasonable.</strong> The employer must show there was no other reasonable role you could have been redeployed into, within the business or an associated entity. If a suitable vacancy existed and you were not offered it — or not genuinely considered for it — the redundancy may fail this limb.</li>
 </ol>

 <h2>The part employers most often get wrong: consultation</h2>
 <p>If there is one reason otherwise-lawful redundancies become successful unfair dismissal claims, it is consultation. The obligation usually comes not from the <em>Fair Work Act</em> itself, but from the <strong>modern award or enterprise agreement</strong> that covers the employee. Almost every modern award contains a consultation clause that is triggered by "major workplace change" — and because most employees are covered by an award or agreement, the obligation applies far more often than employers assume.</p>
 <p>When it applies, consultation is <strong>mandatory and must be genuine</strong>. That means the employer must notify affected employees of the proposed change <em>before</em> the decision is finalised; give them a real opportunity to respond and raise alternatives; and genuinely consider that response. The point that catches employers out, confirmed repeatedly by the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a>: <strong>even if consultation would not have changed the outcome, failing to consult means the redundancy is not genuine.</strong> A quick phone call announcing a decision already made is not consultation — it is notification, and it does not satisfy the obligation.</p>

 <h2>A worked example of where redundancy goes wrong</h2>
 <p>A business decides, for sound financial reasons, that it can no longer afford a particular role. The owner is certain it is a genuine redundancy — the money simply is not there. They call the employee in, explain the decision, and finish them up that afternoon with their entitlements paid. Clean and decisive, or so it seems.</p>
 <p>But if that employee is covered by a modern award with a consultation clause — as most are — the employer has just walked into a problem. There was no consultation before the decision was finalised, no opportunity for the employee to respond or suggest alternatives, and no genuine consideration of redeployment. The business reason was real, but the process was not followed. On these facts the redundancy may not be "genuine" for the purposes of section 389 — which means the unfair dismissal defence is gone. Cases with almost exactly these facts come before the Commission regularly, and employers are frequently surprised to learn that their sound business reason did not save them.</p>

 <h2>Signs your redundancy may not be genuine</h2>
 <ul>
   <li>Your duties are still being done by other people or under a different job title</li>
   <li>You were told the decision was final before anyone consulted you</li>
   <li>There were other roles you could have filled, and you were not offered or considered for them</li>
   <li>You were the only person selected, and the basis for choosing you is unclear or feels like a pretext</li>
   <li>Your award or agreement contains a consultation clause that was not followed</li>
 </ul>
 <p>Remember the <strong>21-day deadline</strong>: if you want to challenge a redundancy as an unfair dismissal, the application must be lodged with the Fair Work Commission within 21 days of the dismissal taking effect. See our <a href="/unfair-dismissal-21-day-rule/">unfair dismissal 21-day rule guide</a>.</p>
 <p>And if you suspect the redundancy was really a cover for dismissing you because of a protected attribute (age, pregnancy, disability) or because you exercised a workplace right, it may be a <strong>general protections matter</strong> — a different claim with its own deadlines, covered in our <a href="/general-protections-discrimination-mediation/">general protections guide</a>.</p>

 <h2>How mediation resolves redundancy disputes</h2>
 <p>Redundancy disputes are often as much about process, communication and dignity as they are about money — which makes them well suited to mediation. Rather than fighting over whether the technical test was met in a public hearing, mediation lets both sides craft a practical resolution: an agreed payment or additional entitlement, a reference or statement of service, outplacement or transition support, confidentiality, and a mutual release that ends the matter cleanly. For the employer, it avoids a published unfair dismissal finding. Both sides keep control of the result. See our <a href="/redundancy-restructure-mediation/">redundancy and restructure mediation page</a> for how we approach these matters.</p>
 """,
 [("Is redundancy pay compulsory?",
   "Minimum redundancy pay and notice are set by the National Employment Standards and any applicable award or agreement, based on length of service. Small businesses may be exempt from redundancy pay in some cases."),
  ("Can I be made redundant while on leave?",
   "Being on leave does not protect a genuinely redundant role, but it does not remove the consultation and process obligations either. Selecting someone because they are on certain protected leave can raise general protections issues."),
  ("My employer says it is a genuine redundancy. Can I still challenge it?",
   "Yes. 'Genuine redundancy' is a legal test, not just the employer's label. If the role still exists, consultation was skipped, or redeployment was reasonable and not offered, the redundancy may not be genuine."),
  ("How long do I have to challenge a redundancy?",
   "If challenging as an unfair dismissal, 21 calendar days from the dismissal taking effect. Act quickly — extensions are only granted in exceptional circumstances."),
  ("Does the size of my employer matter?",
   "Yes. Small businesses (fewer than 15 employees) have a longer minimum employment period and some redundancy-pay exemptions — but they still have to consult where an award or agreement requires it.")],
 "Redundancy: Was It Genuine?",
 "Know where you stand — <em>before you accept it</em>.",
 "Whether you are an employee questioning a redundancy that doesn't sit right, or an employer wanting to run a restructure the right way, an early conversation can save a great deal of stress and cost.")

# ---- CONTESTING A WILL: YOUR OPTIONS ----
build("contesting-a-will",
 "Contesting a Will in Australia: Your Options",
 "There are two different ways to challenge a will in Australia, with strict and varying state-by-state deadlines. This guide explains both, the time limits, and why mediation resolves most estate disputes.",
 "Know your options — and your deadlines",
 "Contesting a Will in Australia: <em>Your Options</em>",
 "When someone close to you dies and the will leaves you out — or leaves you far less than you needed to get by — the hurt is real, and it is rarely only about money. It can feel like a final judgement from someone you loved, or like a stranger's decision imposed on your family. This guide explains, in plain terms, the two very different ways a will can be challenged in Australia, the strict and varying time limits that apply, what the process actually looks like, and why mediation resolves most of these disputes without dragging a grieving family through court.",
 "There are two distinct challenges: a family provision claim (arguing the will fails to make adequate provision for you, not that it is invalid) and a validity challenge (arguing the will should not stand at all — on grounds like lack of testamentary capacity, undue influence, or fraud). Most disputes are family provision claims. Time limits are strict, vary by state, and missing one usually ends your claim permanently — in Tasmania, the deadline is just three months from probate.",
 """
 <h2>Two very different challenges</h2>
 <p><strong>A family provision claim.</strong> This is by far the most common. You are <em>not</em> arguing the will is invalid. You accept it is a real, properly made will — but you say it fails to make adequate provision for you, someone the deceased had a responsibility to provide for. The court can then redistribute part of the estate to correct that inadequate provision. Family provision claims are, in essence, a safety net the law provides for close family and dependants who have been left without proper support.</p>
 <p><strong>A challenge to the will's validity.</strong> Here you are arguing the will itself should not stand at all. The usual grounds are: the deceased lacked <em>testamentary capacity</em> (they were not of sound mind when they made it); <em>undue influence</em> (someone pressured or coerced them); <em>fraud or forgery</em>; or improper <em>execution</em> (the will was not signed and witnessed correctly). If a validity challenge succeeds, the court may fall back to an earlier valid will, or to the intestacy rules if there is none.</p>
 <p>Most disputes are family provision claims, so the rest of this guide focuses mainly on those.</p>

 <h2>Who can make a family provision claim?</h2>
 <p>Eligibility varies between states and territories, but the categories generally include: spouses and de facto partners (current and, in some places, former); children, including in many cases adult children and stepchildren; and people who were wholly or partly dependent on the deceased. Being eligible does not guarantee a claim will succeed — it only opens the door. The court then weighs a range of factors including your financial position, the size of the estate, the nature and length of your relationship with the deceased, and the competing needs of other beneficiaries.</p>
 <p>Importantly, estrangement does not automatically defeat a claim — courts have redirected provision to estranged adult children in genuine financial need — but it is one factor among many.</p>

 <h2>The time limits — strict, and different by state</h2>
 <p>This is the part that catches people out, and it is the single most important practical point in this guide. <strong>There is no national deadline. Time limits differ across every state and territory, and missing one usually ends your claim permanently.</strong></p>
 <figure class="tbl"><table>
 <thead><tr><th>State / Territory</th><th>Deadline</th><th>Starts from</th></tr></thead>
 <tbody>
 <tr><td>New South Wales</td><td>12 months</td><td>Date of death</td></tr>
 <tr><td>Victoria</td><td>6 months</td><td>Grant of probate</td></tr>
 <tr><td>Queensland</td><td>Notify executor within 6 months; file within 9 months</td><td>Date of death</td></tr>
 <tr><td>South Australia</td><td>6 months</td><td>Grant of probate</td></tr>
 <tr><td>Western Australia</td><td>6 months</td><td>Grant of probate</td></tr>
 <tr><td>Tasmania</td><td>3 months — the shortest in Australia</td><td>Grant of probate</td></tr>
 <tr><td>ACT / NT</td><td>Generally 6 months</td><td>Grant of probate / date of death</td></tr>
 </tbody></table></figure>
 <p>Note that the starting point differs too — some states run from the date of death, others from the grant of probate. Courts have only limited discretion to allow a late claim, usually only where there is a compelling explanation and the estate has not already been distributed. If you think you may have a claim, <strong>get advice immediately</strong>. Do not wait until you feel emotionally ready — the clock does not.</p>

 <h2>What the process looks like</h2>
 <p>In most jurisdictions, a family provision claim follows a fairly predictable path, and mediation is built into it:</p>
 <ol>
   <li>The claim is filed with the relevant Supreme Court.</li>
   <li>A first directions hearing takes place, often around 28 days later, where the court orders an exchange of financial information — the applicant's position and the estate's assets and liabilities.</li>
   <li><strong>Mediation is then held</strong>, frequently within a few weeks of that hearing. In many states, attempting mediation is effectively a compulsory component before a final hearing. This means that, often within a couple of months of a claim being filed, the applicant, the executor, and the beneficiaries are sitting down to try to resolve it.</li>
   <li>If it settles, the agreed terms are put to the court and orders are made.</li>
   <li>If it does not settle, the matter proceeds to a final hearing — a slower, costlier and public outcome.</li>
 </ol>

 <h2>Why mediation, not a court battle</h2>
 <p>Estate disputes are uniquely destructive when litigated, and mediation is uniquely suited to them. Litigation costs come out of the very estate being fought over — a contested claim that runs to hearing can consume a significant chunk of what is left for everyone. Mediation costs a fraction of that. It is also private (court filings and judgments are public), faster (most resolve in a single session versus 12 to 18 months or more in court), and it preserves relationships that litigation tends to end permanently.</p>
 <p>This is also worth naming: estate disputes surface at the rawest possible time, in the weeks and months after a death, when grief is fresh. Old family tensions resurface sharpened by loss. A courtroom fight tends to harden these wounds; mediation is structured to let people be heard — sometimes for the first time. In mediation, the family decides. At a hearing, a judge who never knew the deceased decides for everyone. Our <a href="/estate-dispute-mediation/">estate and inheritance dispute mediation page</a> explains how we approach these sensitive matters.</p>
 """,
 [("Can I contest a will if I was left something, just not enough?",
   "Yes. A family provision claim is about whether provision was adequate for your proper maintenance and support — you can be a beneficiary and still claim."),
  ("Does estrangement stop me claiming?",
   "No, though it is a factor the court weighs. Courts have made provision for estranged adult children in genuine financial need."),
  ("What if the estate has already been distributed?",
   "This makes a claim much harder, and in some states impossible — which is another reason to act before the deadline."),
  ("Do I need a lawyer to contest a will?",
   "Family provision claims are legally technical and most participants are represented. But the resolution itself — mediation — is where matters are usually settled, and that is a process built around agreement, not argument."),
  ("Is mediation mandatory in estate disputes?",
   "In many states, attempting mediation is effectively a compulsory component of a family provision claim before it can proceed to a final hearing."),
  ("How much does it cost?",
   "Far less than a contested hearing. Mediator costs are usually shared between the parties, and resolving early preserves more of the estate for everyone.")],
 "Contesting a Will",
 "Talk to us before the deadline passes — <em>time matters here</em>.",
 "If you believe a will has not made fair provision for you, or should not stand at all, time may already be short — and in some states, very short. Get advice early, while all your options are still open.")

# ---- COMMERCIAL DISPUTE GUIDE ----
build("commercial-dispute-guide",
 "Commercial Dispute Guide: Resolving Business Conflict Without Court",
 "Business disputes resolved by mediation are faster, cheaper, and more private than litigation. This guide covers the main types of commercial dispute and why litigation is usually the wrong first move.",
 "Resolve business conflict without litigation",
 "Commercial Dispute Guide: <em>Resolving Business Conflict Without Court</em>",
 "Every business dispute arrives at the worst possible time. A key customer stops paying just when cash is tight. A supplier lets you down in the middle of a big job. A co-founder you have worked beside for a decade suddenly wants out, and cannot agree on the terms. Left to escalate, any of these can swallow months of management time, tens of thousands in legal fees, and a good deal of the goodwill your business runs on. This guide explains the main types of commercial dispute, why litigation is so often the wrong first move, and how mediation resolves these matters faster, more cheaply, and more privately.",
 "Commercial disputes — contract fights, partnership breakdowns, lease disputes, franchise conflicts — are resolved far faster and more cheaply through mediation than litigation. Most commercial mediations resolve in a single session. Litigation routinely takes one to three years, costs substantial money on both sides, and exposes sensitive commercial information to the public record. Many commercial contracts already require mediation before you can litigate.",
 """
 <h2>The common types of commercial dispute</h2>
 <ul>
   <li><strong>Contract disputes.</strong> Non-payment, defective or late supply, disagreement over what the contract actually requires, or one party walking away from its obligations. Most begin as a difference of interpretation that hardens into a standoff.</li>
   <li><strong>Partnership and shareholder disputes.</strong> Often the most damaging, because they are personal as well as commercial — deadlock over strategy, disagreement about drawings or reinvestment, one owner feeling they carry the load while another takes the rewards, or a fundamental falling-out. Where a partner or director is leaving, these overlap with our <a href="/partnership-executive-exit-mediation/">partnership and executive exit guidance</a>.</li>
   <li><strong>Commercial and retail lease disputes.</strong> Rent reviews, outgoings, make-good obligations at end of lease, renewal, and assignment. These have their own special rules — see below.</li>
   <li><strong>Franchise, supply, and distribution disputes.</strong> Disagreements between franchisors and franchisees, or along a supply chain, often governed by specific codes such as the Franchising Code of Conduct.</li>
   <li><strong>Business sale and purchase disputes.</strong> Earn-outs, warranties, and disagreements about what was really promised during a sale.</li>
 </ul>

 <h2>Why litigation is usually the wrong first move</h2>
 <ul>
   <li><strong>It destroys value.</strong> Public conflict unsettles customers, staff, suppliers and lenders. The reputational damage and distraction can cost far more than the amount in dispute. A partnership fight played out in court can erode the value of the business faster than any settlement figure.</li>
   <li><strong>It is slow.</strong> Commercial litigation routinely takes one to three years to reach a final hearing. That is years of uncertainty, distraction, and money tied up.</li>
   <li><strong>It is expensive.</strong> Commercial cases are document-heavy and often require expert evidence. Legal costs on both sides can run into serious money, and even the "winner" may be out of pocket.</li>
   <li><strong>It is public.</strong> Court filings and judgments are on the public record. Sensitive commercial information — your margins, your contracts, your internal emails — can end up exposed.</li>
   <li><strong>It burns relationships.</strong> In business you often still have to deal with the other side, or share an industry, suppliers or customers with them.</li>
 </ul>

 <h2>Counting the real cost of a business dispute</h2>
 <p>When business owners weigh whether to fight or settle, they often look only at the amount in dispute and the legal fees. But the true cost is much broader: the legal fees themselves; the management time diverted from running the business (real money even though it never appears on an invoice); the opportunity cost of decisions delayed and deals not pursued; the strain on cash flow; and the harder-to-measure damage to relationships with customers, staff and suppliers who sense the turmoil.</p>
 <p>Set against all that, the cost of a mediated resolution — often a single session, shared between the parties — is modest. The question is rarely "can we win?" It is "what will winning cost us, and is there a faster way to an outcome we can live with?"</p>

 <h2>A special case: retail and commercial leases</h2>
 <p>Retail lease disputes deserve their own mention because in most of Australia, <strong>mediation is a mandatory step before a tribunal will hear the matter.</strong> In NSW, retail lease disputes must generally go to the <a href="https://www.smallbusiness.nsw.gov.au/" target="_blank" rel="noopener">NSW Small Business Commissioner</a> for mediation before NCAT. Victoria uses the Victorian Small Business Commission before VCAT. Queensland, South Australia, Western Australia, the ACT and NT operate similar pathways.</p>
 <p>Many commercial contracts also contain <strong>dispute-resolution clauses</strong> obliging the parties to mediate before litigating. If your contract has one, mediation is not just sensible — it may be a contractual precondition to going to court at all. Check your agreement early.</p>

 <h2>How to prepare for a commercial mediation</h2>
 <p>Preparation makes the difference between a mediation that resolves and one that stalls. Before the session, get your key documents in order — the contract at the heart of the dispute, the correspondence that shows how it unfolded, and any figures that support your position. Just as importantly, work out your own numbers honestly: what outcome you genuinely want, what you would accept, and what your realistic alternative is if the matter does not settle and instead goes to court. That alternative — the cost, time, risk and disruption of litigating — is the true benchmark against which any settlement offer should be judged.</p>
 <p>It also helps to separate your interests from your positions. A position is a demand — <em>I want the full amount plus costs.</em> An interest is the underlying need — <em>I need to protect my cash flow, keep this customer, and not set a precedent.</em> Interests can often be satisfied in more than one way, which is where creative commercial settlements come from.</p>
 """,
 [("Is mediation binding in a commercial dispute?",
   "The mediation process is voluntary, but once you sign a settlement agreement or deed, that becomes an enforceable contract. You are not bound until you agree."),
  ("What if the other side refuses to mediate?",
   "Many contracts require mediation, and for retail leases it is generally mandatory. Even where it is voluntary, a refusal to mediate can be viewed poorly by a court later."),
  ("Can mediation handle a dispute that is both commercial and personal, like a partnership breakup?",
   "Yes — that is one of its great strengths. A single settlement can resolve the money, the ownership, the restraints, and how the split is communicated, all at once."),
  ("How long does commercial mediation take?",
   "Most commercial mediations resolve in a single session. Compare that with one to three years for litigation."),
  ("Is commercial mediation confidential?",
   "Yes. Mediation is private and without prejudice — a major advantage over public court proceedings.")],
 "Commercial Dispute Guide",
 "Resolve it faster — <em>and keep it private</em>.",
 "Before you commit your business to a slow, costly and public legal fight, talk to us about resolving it faster, more privately, and with a commercial outcome that actually works.")

# ---- REAL ESTATE & CONSTRUCTION DISPUTES ----
build("real-estate-construction-disputes",
 "Real Estate &amp; Construction Disputes: Resolving Them Without a Tribunal",
 "Property disputes escalate fast. This guide covers building defects, boundary fights, co-ownership deadlocks, and why mediation resolves most in a single session instead of months at tribunal.",
 "Resolve property disputes without the tribunal fight",
 "Real Estate &amp; Construction Disputes: <em>Resolving Them Without a Tribunal</em>",
 "Property disputes have a particular way of escalating. What starts as a crack in a new wall, a fence in the wrong spot, or a disagreement over a final invoice can quickly become a matter of principle — and then a matter for lawyers. Because property is valuable and emotions run high, these disputes are among the most likely to spiral into expensive, drawn-out tribunal or court proceedings. This guide explains the common types of real estate and construction dispute, the formal pathways that may apply, and why mediation is so often the faster, cheaper and less bruising way to resolve them.",
 "Property disputes — building defects, boundary fights, co-ownership deadlocks, strata conflicts — are well suited to mediation because the outcomes people actually want are practical, not just financial. A works schedule, a cost-sharing arrangement, a buy-out. These are things mediation can deliver that a tribunal generally cannot. Most property mediations resolve in a single session.",
 """
 <h2>The common types of property dispute</h2>
 <ul>
   <li><strong>Building and construction disputes.</strong> The largest category — between homeowners and builders, builders and subcontractors, and developers and contractors. Usual flashpoints: defective work, delays, cost overruns, disputed variations, and disagreements about whether work meets the contract or relevant standards. Because they often turn on technical questions, they can become a battle of expert reports, which is exactly what makes litigating them so costly.</li>
   <li><strong>Boundary and fencing disputes.</strong> Encroachments, dividing-fence cost-sharing, and access disputes between neighbours. These are frequently more about relationship and principle than money — which is precisely why a purely legal approach so often fails to actually resolve them.</li>
   <li><strong>Co-ownership disputes.</strong> Siblings who inherited a house, friends who invested together, or a couple who have separated and cannot agree on whether to sell, how to manage the property, or how to divide the proceeds. A court can ultimately order a sale, but that is a slow and blunt outcome.</li>
   <li><strong>Strata and owners-corporation disputes.</strong> Conflicts between lot owners or between owners and the body corporate over levies, by-laws, common property, and building defects. These have their own tribunal pathways and are covered in more depth in our <a href="/strata-neighbour-dispute-mediation/">strata and neighbour dispute guidance</a>.</li>
   <li><strong>Off-the-plan and sale disputes.</strong> Disagreements over whether the finished product matches what was promised, delayed settlements, and disputes about deposits.</li>
 </ul>

 <h2>Why property disputes are so well suited to mediation</h2>
 <ul>
   <li><strong>They are fact-heavy and expert-driven.</strong> Litigating a construction defect means duelling expert reports, site inspections and technical argument — slow and expensive. Mediation lets the parties agree a practical path (an agreed scope of rectification, for instance) without paying two experts to fight it out.</li>
   <li><strong>The relationship often continues.</strong> Neighbours remain neighbours. Co-owners may still be family. A body corporate and its lot owners have to keep living together. A judgment does not repair that; a negotiated agreement can.</li>
   <li><strong>The outcomes people actually want are practical, not just financial.</strong> What an owner usually wants is the defect fixed, or the fence agreed, or the property sold on sensible terms. Mediation can deliver a works schedule, a timeline, a cost-sharing arrangement or a buy-out. A court generally cannot.</li>
   <li><strong>Speed matters.</strong> Building disputes in particular get worse with time — defects deteriorate, costs rise, and positions harden. A tribunal matter can take many months just to reach a first hearing. Mediation can be arranged and resolved far faster.</li>
 </ul>

 <h2>The formal pathways — and where mediation fits</h2>
 <p>State civil and administrative tribunals — NCAT in NSW, VCAT in Victoria, QCAT in Queensland — handle a large share of building, strata and tenancy disputes, and frequently encourage or require mediation or conciliation before a final hearing. Building commissions and fair trading bodies in each state offer complaint and, in some cases, resolution services for residential building work. Building contracts themselves very often contain dispute-resolution clauses requiring mediation or expert determination before litigating.</p>
 <p>Private mediation can run before you engage any of these processes, alongside them, or as the resolution step within them. The advantage of engaging early is that you may resolve the matter before it hardens into a formal proceeding, saving the cost and delay entirely. Getting advice early also helps you choose the right pathway — some property disputes have time limits or notification requirements that are easy to miss.</p>

 <h2>The hidden costs of fighting a property dispute</h2>
 <p>The amount named in a property dispute is rarely the real cost. A construction dispute that goes the distance can require multiple expert reports, each running into thousands of dollars, plus solicitors, plus barristers for a hearing — and the defects themselves often worsen while everyone argues, increasing the eventual repair bill. A boundary dispute between neighbours can poison daily life for years and reduce the saleability of both properties. A co-ownership deadlock can leave an asset frozen and deteriorating while its owners pay to fight over it.</p>
 <p>Set against that, mediation looks very different. A single session, with costs typically shared, can resolve in hours what litigation would take a year or more to grind through — and it can do so in a way that actually fixes the underlying problem rather than just assigning blame.</p>

 <h2>How to prepare for a property mediation</h2>
 <p>A property mediation goes best when both sides come organised. If yours is a building or construction matter, bring the contract, any variations, the relevant plans and specifications, photographs of the work in question, and any expert reports or quotes for rectification. The clearer you can be about exactly which items are in dispute and what each would cost to resolve, the faster the conversation moves from grievance to solution.</p>
 <p>For a boundary or co-ownership dispute, bring the title documents, any survey, and a clear sense of the outcome you actually want. As with any mediation, it pays to think through your realistic alternative in advance: what will it cost you, in money and time and stress, if this does not settle and instead goes to a tribunal or court? That figure is the yardstick for any offer on the table.</p>
 """,
 [("My builder and I are at war over defects. Is it too late to mediate?",
   "Almost never. Even matters already in a tribunal are frequently resolved at mediation. The sooner you mediate, the more cost you save."),
  ("Can mediation force the other side to fix defective work?",
   "Mediation cannot force anything — but a mediated settlement can include a binding, agreed schedule of rectification works with timeframes. That is often exactly what an owner wants, and what a damages award does not deliver."),
  ("We are co-owners who cannot agree whether to sell. Can mediation help?",
   "Yes. Co-ownership deadlocks are well suited to mediation, which can produce a buy-out, an agreed sale process, or a management arrangement — without the cost and finality of a court-ordered sale."),
  ("Is a retail lease dispute different?",
   "Yes. In most states you must attempt mediation through the Small Business Commissioner before going to a tribunal. See our commercial dispute guide for detail."),
  ("How long does property mediation take?",
   "Most property mediations resolve in a single session, compared with many months for a tribunal or court outcome.")],
 "Real Estate &amp; Construction Disputes",
 "Resolve your property dispute — <em>before it spirals</em>.",
 "Before a property disagreement becomes an expensive, drawn-out tribunal fight, talk to us about whether mediation can resolve it quickly and cleanly.")

# ---- WORKPLACE DISPUTE GUIDE ----
build("workplace-dispute-guide",
 "Workplace Dispute Guide: Your Rights, the FWC &amp; Mediation",
 "A plain-English map of your options in an Australian workplace dispute — FWC, unfair dismissal, general protections, bullying, redundancy, and how mediation resolves most without a hearing.",
 "Your rights, your options, plain English",
 "Workplace Dispute Guide: <em>Your Rights, the FWC &amp; Mediation</em>",
 "Trouble at work has a way of taking over your whole life. Whether you have been dismissed, passed over, bullied, made redundant, or you are an employer facing a claim you did not see coming, the stress is real and the path forward is rarely obvious. There is a maze of acronyms — FWC, NES, awards, general protections — and a lot of conflicting advice online. This guide cuts through it. It explains your main options in plain English, how the Fair Work system fits together, where the critical deadlines are, and how mediation resolves the large majority of these disputes without a hearing.",
 "Australian workplace disputes divide into several distinct legal shapes — unfair dismissal, redundancy, general protections, bullying, partnership exits, and internal grievances — each with different tests and deadlines. The Fair Work Commission is built to encourage resolution before a hearing; the large majority of matters settle at conciliation. Private mediation works alongside the FWC or in situations the Commission does not cover, and resolves most disputes in a single session.",
 """
 <h2>First, the deadlines — because some are brutally short</h2>
 <p>Before anything else, understand this: some workplace claims have very short deadlines, and missing them can end your rights entirely. The most important is the <strong>21-day rule</strong>. If you have been dismissed and want to challenge it as an unfair dismissal, or bring a general protections claim involving dismissal, you have just <strong>21 calendar days</strong> from when the dismissal takes effect to lodge with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a>. That is three weeks, weekends included, and extensions are only granted in exceptional circumstances. If you have recently lost your job and something feels wrong, treat it as urgent and read our <a href="/unfair-dismissal-21-day-rule/">unfair dismissal 21-day rule guide</a> first.</p>
 <p>Not every workplace matter has such a tight limit — an ongoing pay dispute or a bullying situation works differently — but because you may not know at first which category yours falls into, the safe move is always to get advice early.</p>

 <h2>Your main options — a plain-English map</h2>
 <ul>
   <li><a href="/unfair-dismissal-termination-mediation/"><strong>Unfair dismissal.</strong></a> The question is whether your dismissal was "harsh, unjust or unreasonable." It looks at both the reason for the dismissal and the fairness of the process. Tight 21-day deadline; eligibility rules apply.</li>
   <li><a href="/redundancy-restructure-mediation/"><strong>Redundancy disputes.</strong></a> The question is whether your redundancy was <em>genuine</em> — because a genuine redundancy is a defence to an unfair dismissal claim. If the role still exists, consultation was skipped, or redeployment was reasonable and not offered, it may not be genuine.</li>
   <li><a href="/general-protections-discrimination-mediation/"><strong>General protections and discrimination.</strong></a> The question is whether you suffered "adverse action" because you have or exercised a workplace right, or because of a protected attribute like age, sex, race, disability, pregnancy or carer's responsibilities. These claims can be powerful and carry their own deadlines.</li>
   <li><a href="/workplace-bullying-harassment-mediation/"><strong>Bullying and harassment.</strong></a> Repeated unreasonable behaviour that creates a risk to health and safety. Specific avenues apply, including applying to the Fair Work Commission for an order to stop bullying — aimed at stopping ongoing behaviour rather than awarding compensation.</li>
   <li><a href="/partnership-executive-exit-mediation/"><strong>Partnership and executive exits.</strong></a> High-stakes separations at the top of a business — partners falling out, directors leaving under strain, senior executives negotiating a dignified departure. These blend employment, commercial and sometimes corporate issues.</li>
   <li><a href="/workplace-investigations-grievance-mediation/"><strong>Workplace investigations and grievances.</strong></a> Knowing when a matter needs a formal investigation, when it is better mediated, and how to handle a grievance without inflaming it.</li>
 </ul>

 <h2>How the Fair Work system actually works</h2>
 <p>The Fair Work Commission is Australia's national workplace tribunal — and it is worth understanding its basic instinct: it is built to encourage resolution, not to run trials. For most claim types, the Commission's first move is to offer <strong>conciliation</strong> — an informal, confidential, without-prejudice discussion led by an impartial staff member, designed to help the two sides reach their own agreement. The large majority of matters settle at this stage. Only the minority that don't go on to a Commission Member for a binding decision.</p>
 <p>Alongside the Commission sit two other useful government bodies. The <a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a> is the go-to source for information about workplace rights, pay and entitlements. <a href="https://www.safeworkaustralia.gov.au/" target="_blank" rel="noopener">Safe Work Australia</a> sets the national framework for work health and safety, including the psychosocial hazards — like role conflict and workplace bullying — that employers now have a positive duty to manage.</p>

 <h2>Where private mediation fits alongside all of this</h2>
 <p>Private mediation is not an alternative that competes with the Fair Work system — it works with it. Mediation can be used in three ways: <strong>before you lodge</strong>, to try to resolve the matter directly and quickly, sometimes avoiding a formal claim altogether; <strong>alongside a lodged claim</strong>, with one of our own mediators handling your specific dispute, more time than a short conciliation call allows, and a process tailored to the matter; or <strong>in situations the Commission does not cover</strong>, such as many partnership disputes or internal grievances.</p>
 <p>The advantages are consistent across all workplace disputes: faster (usually a single session), private (no public record), cheaper than a contested hearing, and it keeps the outcome in your hands. It also tends to preserve relationships — which matters enormously when the people involved have to keep working together, or when a business cannot afford a public fight.</p>
 <p>Mediation is not right for every situation, and we are honest about that. Where there is violence, serious harassment, a severe power imbalance, or a need to establish serious facts first, another step may need to come first. Our guide on <a href="/is-mediation-right-for-workplace-dispute/">whether mediation is right for your workplace dispute</a> walks through that honestly.</p>

 <h2>What to expect if you come to us</h2>
 <p>You start with a fixed-fee consultation — a proper conversation, not a sales pitch — where we listen to your situation, tell you honestly which type of claim or process fits, flag any deadlines that are running, and set out your realistic options. There are no surprises on cost, because the fee is agreed up front.</p>
 <p>If mediation is the right path, one of our own mediators — experienced in employment law and workplace dynamics — works with you directly. The mediator speaks with each side privately first, to understand the issues and check for any safety or power-imbalance concerns. The session can run with everyone together or in a shuttle format, in person or online. In most matters, agreement is reached in that session, and we guide you on turning it into a binding, enforceable deed of settlement. If mediation is not the right path, we will tell you that too, and point you toward the process that is.</p>

 <h2>Preventing disputes before they start</h2>
 <p>Not every workplace problem is a legal dispute yet — and the cheapest dispute is the one that never happens. A great deal of workplace conflict traces back to team dynamics that were never properly understood: unclear roles, overlapping responsibilities, and behaviour that gets read as personal when it is really structural. <a href="/belbin-team-roles-training/">Belbin Team Roles training</a> helps organisations build balanced teams and give people a shared, non-personal language for difference — heading off conflict before it ever becomes a grievance or a claim.</p>
 """,
 [("I have been dismissed. What is the first thing I should do?",
   "Check the date your dismissal took effect and count forward 21 days — that is likely your deadline to lodge with the Fair Work Commission. Then get advice quickly, well before that date."),
  ("Do I need a lawyer for a workplace dispute?",
   "Not necessarily. Many matters are resolved without one, and Fair Work processes are designed to be accessible. But early advice — even a single consultation — often changes the outcome, especially on which claim applies and what it is worth."),
  ("Is mediation compulsory for workplace disputes?",
   "There is no across-the-board requirement to mediate a workplace dispute (unlike family law parenting matters). But the Commission strongly encourages conciliation, many contracts require mediation, and courts expect genuine attempts to resolve before litigating."),
  ("Can an employer use mediation too?",
   "Absolutely. Employers facing a claim, or wanting to handle a grievance or restructure correctly, benefit just as much from early advice and mediation as employees do."),
  ("How much does workplace mediation cost?",
   "We use transparent, fixed-fee pricing — see our fee structure page. Mediation is a fraction of the cost of a contested hearing.")],
 "Workplace Dispute Guide",
 "Not sure which option fits? <em>Start here.</em>",
 "Workplace disputes are stressful precisely because the path is unclear. Talk it through with someone who can tell you which option fits, what the deadlines are, and whether mediation is the right step.")

print("Resource pages built.")
