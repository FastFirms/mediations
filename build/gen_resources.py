#!/usr/bin/env python3
"""Resource/guide pages + booking form. Keyword-first H1s, full schema."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build(slug,title,desc,eyebrow,h1,lede,ans,blocks,qa,crumb,cta_h,cta_p,is_article=True,tool_html=None,tool_position='after'):
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
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {ans}</p></div></div>"""
    if tool_html and tool_position=='before': d+=tool_html
    expert_bio = '<aside style="margin-top:3rem;padding:1.5rem;background:var(--surf,#f7f8fa);border-radius:10px;border:1px solid var(--border,#e5e7eb)"><p style="font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted,#6b7280);margin:0 0 1rem">About the expert</p><div style="display:flex;gap:1.25rem;align-items:flex-start"><img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia" width="80" height="80" loading="lazy" style="border-radius:50%;flex-shrink:0;object-fit:cover;width:80px;height:80px"><div><p style="font-weight:700;margin:0 0 .15rem;font-size:1rem">Dan Toombs</p><p style="margin:0 0 .75rem;color:var(--muted,#6b7280);font-size:.875rem">Founder, Mediations Australia</p><p style="margin:0 0 .75rem;font-size:.9rem;line-height:1.6">Dan Toombs is the Founder of Mediations Australia, an award-winning lawyer, former Tribunal Member and nationally accredited mediator (AMDRAS). His career spans law, adjudication and organisational leadership, giving him particular insight into the systemic, structural and human dynamics that drive complex disputes. A recipient of the National Human Rights Law Award and a Winston Churchill Fellow, Dan brings legal expertise, strategic insight and practical judgment to dispute resolution.</p><a href="https://www.mediationsaustralia.com.au/our-team/dan-toombs/" style="font-size:.875rem;font-weight:600">View Dan Toombs&#x2019; profile &rarr;</a></div></div><p style="margin:1rem 0 0;font-size:.8rem;color:var(--muted,#6b7280)">Last reviewed 14 August 2026</p></aside>'
    d+=f"""<article class="body"><div class="wrap-narrow reveal">{blocks}{expert_bio}</div></article>"""
    if tool_html and tool_position=='after': d+=tool_html
    if qa: d+=faq_html(qa,heading=f"{crumb} — FAQs")
    d+=cta_band(cta_h,cta_p)+"</main>"+page_end()
    p=os.path.join(OUT,slug); os.makedirs(p,exist_ok=True)
    open(os.path.join(p,"index.html"),"w").write(d)
    import re; return slug,len(re.sub(r'<[^>]+>',' ',d).split())

# ---- PARENTING PLAN BUILDER TOOL (embedded on parenting-plan-template page) ----
PARENTING_BUILDER = """
<section class="sec ppb-outer" style="border-top:2px solid var(--line);padding:80px 0 96px;background:var(--sand)">
<div class="wrap" style="max-width:860px">

<div style="text-align:center;margin-bottom:56px">
  <p class="sec-tag">Free interactive tool</p>
  <h2 class="sec-title" style="margin-bottom:16px">Build Your Parenting Plan <em>Agreement</em></h2>
  <p style="color:var(--ink-soft);max-width:54ch;margin:0 auto;font-size:1.05rem;line-height:1.7">A free tool for separated parents in Australia. Complete 9 guided steps, then download a ready-to-sign PDF — no account needed, nothing stored on our servers.</p>
</div>

<div class="ppb-intro-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:52px">
  <div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 24px">
    <div style="width:44px;height:44px;background:rgba(41,75,142,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    </div>
    <h3 style="font-family:var(--sans);font-size:1rem;font-weight:700;color:var(--ink);margin:0 0 8px">Who it&rsquo;s for</h3>
    <p style="font-size:.9rem;color:var(--ink-soft);line-height:1.65;margin:0">Separated or divorcing parents who want to formalise care arrangements for their children — whether you&rsquo;re starting from scratch or updating an existing plan.</p>
  </div>
  <div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 24px">
    <div style="width:44px;height:44px;background:rgba(41,75,142,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
    </div>
    <h3 style="font-family:var(--sans);font-size:1rem;font-weight:700;color:var(--ink);margin:0 0 8px">How to use it</h3>
    <p style="font-size:.9rem;color:var(--ink-soft);line-height:1.65;margin:0">Work through 9 steps covering every key area — living arrangements, holidays, education, health, finances, and more. Skip any section that doesn&rsquo;t apply and come back any time; your answers autosave as you go.</p>
  </div>
  <div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 24px">
    <div style="width:44px;height:44px;background:rgba(41,75,142,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
    </div>
    <h3 style="font-family:var(--sans);font-size:1rem;font-weight:700;color:var(--ink);margin:0 0 8px">What you get</h3>
    <p style="font-size:.9rem;color:var(--ink-soft);line-height:1.65;margin:0">A formatted PDF parenting plan agreement, ready for both parties to sign. Covers all standard Australian parenting plan clauses under the Family Law Act 1975. Free to download, private to your device.</p>
  </div>
</div>
<style>@media(max-width:640px){.ppb-intro-grid{grid-template-columns:1fr!important}}</style>

<div style="max-width:800px;margin:0 auto">

<style>
/* ── Builder card ───────────────────────────────────────────── */
.ppb-card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:40px 44px;box-shadow:var(--shadow)}
/* ── Step indicator ─────────────────────────────────────────── */
.ppb-stepper{display:flex;align-items:center;justify-content:space-between;margin-bottom:36px;gap:6px}
.ppb-step{display:flex;flex-direction:column;align-items:center;gap:6px;flex:1;cursor:default}
.ppb-step-dot{width:30px;height:30px;border-radius:50%;border:2px solid var(--line);background:#fff;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:700;font-family:var(--sans);color:var(--ink-soft);transition:all .25s;flex-shrink:0}
.ppb-step.done .ppb-step-dot{background:var(--sage);border-color:var(--sage);color:#fff}
.ppb-step.active .ppb-step-dot{background:var(--sage);border-color:var(--sage);color:#fff;box-shadow:0 0 0 4px rgba(41,75,142,.15)}
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
.ppb-form-group input:focus,.ppb-form-group select:focus,.ppb-form-group textarea:focus{outline:none;border-color:var(--sage);box-shadow:0 0 0 3px rgba(41,75,142,.1)}
.ppb-form-group input[type=date]{accent-color:var(--sage);color-scheme:light}
.ppb-form-group select{appearance:none;background-image:url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%233d5248' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:36px}
.ppb-form-group textarea{min-height:100px;resize:vertical;line-height:1.65}
/* ── Radio as cards ─────────────────────────────────────────── */
.ppb-radio-cards{display:flex;flex-direction:column;gap:10px;margin-top:6px}
.ppb-radio-card{display:flex;align-items:center;gap:14px;padding:14px 16px;border:1.5px solid var(--line);border-radius:10px;cursor:pointer;transition:border-color .18s,background .18s;background:#fff}
.ppb-radio-card:hover{border-color:var(--sage);background:var(--sand)}
.ppb-radio-card input[type=radio]{width:18px;height:18px;accent-color:var(--sage);flex-shrink:0;cursor:pointer}
.ppb-radio-card label{color:var(--ink);font-family:var(--sans);font-size:.93rem;cursor:pointer;margin:0;font-weight:400;line-height:1.4}
.ppb-radio-card.selected{border-color:var(--sage);background:rgba(41,75,142,.04)}
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
.ppb-btn-next{display:inline-flex;align-items:center;gap:8px;padding:14px 32px;border:none;border-radius:100px;font-size:.95rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:var(--sage);color:#fff;transition:all .2s;box-shadow:0 4px 14px rgba(41,75,142,.28)}
.ppb-btn-next:hover{background:var(--sage-deep);transform:translateY(-2px);box-shadow:0 8px 22px rgba(41,75,142,.32)}
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
.ppb-btn-dl{flex:1;min-width:160px;padding:16px 24px;border:none;border-radius:100px;font-size:1rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:var(--sage);color:#fff;box-shadow:0 4px 14px rgba(41,75,142,.28);transition:all .2s}
.ppb-btn-dl:hover{background:var(--sage-deep);transform:translateY(-2px)}
.ppb-btn-reset{flex:1;min-width:140px;padding:16px 24px;border:1.5px solid var(--line);border-radius:100px;font-size:.95rem;cursor:pointer;font-weight:600;font-family:var(--sans);background:#fff;color:var(--ink-soft);transition:all .2s}
.ppb-btn-reset:hover{border-color:var(--ink);color:var(--ink)}
/* ── Disclaimer ─────────────────────────────────────────────── */
.ppb-disclaimer{font-size:.82rem;color:var(--ink-soft);background:var(--sand);border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin-top:20px;font-family:var(--sans);line-height:1.65}
.ppb-disclaimer strong{color:var(--ink)}
/* ── Error state ────────────────────────────────────────────── */
.ppb-error{border-color:var(--sage)!important;box-shadow:0 0 0 3px rgba(41,75,142,.15)!important}
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
        <div class="ppb-form-group"><label>Party 1 Address</label><input type="text" name="parent1_address" autocomplete="street-address" placeholder="Street address, suburb, state"></div>
        <div class="ppb-form-group"><label>Party 2 Address</label><input type="text" name="parent2_address" autocomplete="street-address" placeholder="Street address, suburb, state"></div>
      </div>
      <div class="ppb-form-group"><label>Child / Children <span class="ppb-req">*</span></label><textarea name="children_info" required placeholder="Full name and date of birth for each child&#10;e.g. Sarah Elizabeth Smith, born 15 March 2016"></textarea><p class="ppb-help">Include all children covered by this agreement, one per line. Use full legal names as they appear on birth certificates.</p></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Agreement Date <span class="ppb-req">*</span></label><input type="date" name="agreement_date" required><p class="ppb-help">The date both parties sign. You can set today's date or a future date.</p></div>
        <div class="ppb-form-group"><label>Review Date — optional</label><input type="date" name="review_date"><p class="ppb-help">Parenting plans often benefit from a scheduled review as children grow. 12 months is a common starting point.</p></div>
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
        <p class="ppb-help" style="margin-bottom:10px">This is about <strong>decision-making</strong>, not where the children live. Equal shared responsibility is the default under Australian family law — it means both parents must consult on major long-term decisions, regardless of where the children spend most of their time.</p>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="parental_responsibility" value="equal" id="ppb_r1" required><label for="ppb_r1">Equal shared parental responsibility — both parents decide together on major issues</label></div>
          <div class="ppb-radio-card"><input type="radio" name="parental_responsibility" value="sole_parent1" id="ppb_r2"><label for="ppb_r2">Sole parental responsibility to Party 1</label></div>
          <div class="ppb-radio-card"><input type="radio" name="parental_responsibility" value="sole_parent2" id="ppb_r3"><label for="ppb_r3">Sole parental responsibility to Party 2</label></div>
        </div>
      </div>
      <div class="ppb-form-group">
        <label>Major decisions requiring consultation between both parties</label>
        <p class="ppb-help" style="margin-bottom:10px">Tick the areas where both parents must agree before a decision is made. Day-to-day decisions (haircuts, what to eat, bedtime) are made by whichever parent the child is with at the time.</p>
        <div class="ppb-check-grid">
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="education" id="ppb_m1"><label for="ppb_m1">Education</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="major medical treatment" id="ppb_m2"><label for="ppb_m2">Major medical treatment</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="religious upbringing" id="ppb_m3"><label for="ppb_m3">Religious upbringing</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="relocation" id="ppb_m4"><label for="ppb_m4">Relocation</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="name changes" id="ppb_m5"><label for="ppb_m5">Name changes</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="major_decisions[]" value="passport applications" id="ppb_m6"><label for="ppb_m6">Passport applications</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Cultural &amp; Religious Upbringing</label><textarea name="cultural_upbringing" placeholder="e.g. Both parties agree to support the children's participation in cultural events, speak both English and Mandarin at home, and observe significant religious occasions from both families"></textarea><p class="ppb-help">Day-to-day cultural practices, language, dietary requirements, and religious observances — separate from the major-decision veto above.</p></div>
    </div>

    <!-- Step 3: Living Arrangements -->
    <div class="ppb-section" data-section="3">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Living Arrangements</h3>
        <p class="ppb-section-subtitle">Where the children live and the regular care schedule.</p>
      </div>
      <div class="ppb-form-group">
        <label>The child/children shall live with <span class="ppb-req">*</span></label>
        <p class="ppb-help" style="margin-bottom:10px">This is about <strong>where the children sleep most nights</strong> — their primary home base. It doesn't affect parental responsibility (decision-making), which is set in the previous step.</p>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="primary_residence" value="equal" id="ppb_res1" required><label for="ppb_res1">Both parties equally — shared care arrangement</label></div>
          <div class="ppb-radio-card"><input type="radio" name="primary_residence" value="parent1" id="ppb_res2"><label for="ppb_res2">Primarily with Party 1</label></div>
          <div class="ppb-radio-card"><input type="radio" name="primary_residence" value="parent2" id="ppb_res3"><label for="ppb_res3">Primarily with Party 2</label></div>
        </div>
      </div>
      <div class="ppb-form-group">
        <label>Regular Care Schedule <span class="ppb-req">*</span></label>
        <p class="ppb-help" style="margin-bottom:10px">Choose the pattern that best describes the regular week-to-week routine. <strong>Week about</strong> = one week with each parent. <strong>2-2-5-5</strong> = each parent has 2 fixed days, then alternating 5-day blocks. <strong>2-2-3-3</strong> = shorter blocks that rotate more frequently.</p>
        <select name="schedule_type" required>
          <option value="">Select a schedule</option>
          <option value="week about (alternating weeks)">Week about — alternating weeks</option>
          <option value="2-2-5-5 schedule">2-2-5-5 schedule</option>
          <option value="2-2-3-3 schedule">2-2-3-3 schedule</option>
          <option value="alternate weekends">Alternate weekends with one parent</option>
          <option value="custom">Custom — I'll describe it below</option>
        </select>
      </div>
      <div class="ppb-form-group"><label>Detailed Schedule</label><textarea name="schedule_details" placeholder="Specific days, times, and any weekly variations"></textarea><p class="ppb-help">Spell out exactly which days and times the children are with each parent. The more specific, the less room for disagreement later.</p></div>
      <div class="ppb-form-group"><label>Changeover — time and location</label><textarea name="changeover_details" placeholder="e.g. Friday at 6:00 pm at the child's school"></textarea><p class="ppb-help">Changeover is when the children move from one parent to the other. Specify a neutral, consistent location where possible — school pick-up is often the least stressful option.</p></div>
      <div class="ppb-form-group"><label>Grandparents &amp; Extended Family</label><textarea name="extended_family" placeholder="e.g. Both parties support the children maintaining relationships with grandparents and extended family on both sides; reasonable time with extended family may occur during each parent's care time without requiring consent from the other parent"></textarea><p class="ppb-help">The Family Law Act recognises children's right to relationships with grandparents and other significant people in their lives.</p></div>
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
      <div class="ppb-form-group"><label>School Holiday Periods</label><textarea name="school_holidays" placeholder="e.g. School holidays split equally — each party takes two weeks per term break"></textarea><p class="ppb-help">School holidays often don't follow the regular week-to-week pattern. Decide here whether they're split equally, follow the normal schedule, or are arranged holiday by holiday. Include who books first and how far in advance.</p></div>
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
        <p class="ppb-help" style="margin-bottom:10px">Agree on the preferred channel for day-to-day parenting communication. Limiting communication to one or two channels helps reduce conflict and keeps a clear record.</p>
        <div class="ppb-check-grid">
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="email" id="ppb_c1"><label for="ppb_c1">Email</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="text message" id="ppb_c2"><label for="ppb_c2">Text message</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="phone calls" id="ppb_c3"><label for="ppb_c3">Phone calls</label></div>
          <div class="ppb-check-card"><input type="checkbox" name="parent_communication[]" value="parenting app" id="ppb_c4"><label for="ppb_c4">Parenting app (e.g. OurFamilyWizard)</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Child's contact with the other parent</label><textarea name="child_contact" placeholder="e.g. Daily phone or video call at 7:00 pm when staying with the other parent"></textarea><p class="ppb-help">Children generally benefit from regular contact with both parents. Set a reasonable time that doesn't disrupt bedtime routines. Both parents should encourage — not block — these calls.</p></div>
      <div class="ppb-form-group"><label>Photos &amp; Social Media</label><textarea name="social_media" placeholder="e.g. Both parties agree not to post images of the children on social media without the other parent's consent; photos shared privately between the parties only"></textarea><p class="ppb-help">One of the most common sources of conflict post-separation. This clause covers who can post photos of the children publicly — on Instagram, Facebook, TikTok, or any social platform — and under what conditions. Many parents agree that private sharing is fine but public posts require both parties to consent.</p></div>
    </div>

    <!-- Step 6: Education -->
    <div class="ppb-section" data-section="6">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Education</h3>
        <p class="ppb-section-subtitle">School decisions and extracurricular activities.</p>
      </div>
      <div class="ppb-form-group">
        <label>School Selection</label>
        <p class="ppb-help" style="margin-bottom:10px">Which school the children attend is a major long-term decision. If you selected equal shared parental responsibility in Step 2, both parents must agree on school changes — this clause spells out how that works in practice.</p>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="school_selection" value="joint decision by both parties" id="ppb_s1"><label for="ppb_s1">Joint decision by both parties</label></div>
          <div class="ppb-radio-card"><input type="radio" name="school_selection" value="primary carer decides after consultation" id="ppb_s2"><label for="ppb_s2">Primary carer decides after consultation</label></div>
          <div class="ppb-radio-card"><input type="radio" name="school_selection" value="continue at current school" id="ppb_s3"><label for="ppb_s3">Continue at current school</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Extracurricular Activities</label><textarea name="extracurricular_activities" placeholder="e.g. Both parties support current activities; new activities require agreement"></textarea><p class="ppb-help">Covers sport, music, tutoring, and other regular commitments. Agree on who pays, who transports, and how new activities are approved — especially ones that fall during the other parent's time.</p></div>
    </div>

    <!-- Step 7: Health -->
    <div class="ppb-section" data-section="7">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Health &amp; Medical Care</h3>
        <p class="ppb-section-subtitle">Medical decision-making and expense responsibilities.</p>
      </div>
      <div class="ppb-form-group">
        <label>Medical Decision Making</label>
        <p class="ppb-help" style="margin-bottom:10px">Routine care (GP visits, vaccinations, dental check-ups) is usually handled by whichever parent the child is with. This clause is about who decides on <strong>major</strong> treatment — surgery, specialist referrals, ongoing medication, or mental health care.</p>
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
        <p class="ppb-help" style="margin-bottom:10px">Child support is a separate legal obligation to this parenting plan. A <strong>Services Australia assessment</strong> calculates the amount based on both parents' incomes and care percentages — this is the most common approach. A <strong>private agreement</strong> is an alternative but must still be fair and in the children's interests.</p>
        <div class="ppb-radio-cards">
          <div class="ppb-radio-card"><input type="radio" name="child_support" value="Services Australia child support assessment" id="ppb_cs1"><label for="ppb_cs1">Services Australia assessment</label></div>
          <div class="ppb-radio-card"><input type="radio" name="child_support" value="private child support agreement between the parties" id="ppb_cs2"><label for="ppb_cs2">Private agreement between the parties</label></div>
          <div class="ppb-radio-card"><input type="radio" name="child_support" value="no child support payable" id="ppb_cs3"><label for="ppb_cs3">No child support payable</label></div>
        </div>
      </div>
      <div class="ppb-form-group"><label>Child Support Details</label><textarea name="support_details" placeholder="Amount, frequency, and payment method if private agreement"></textarea><p class="ppb-help">If using a private arrangement, state the weekly or monthly amount, the payment method (bank transfer is recommended), and the day of the month it's due.</p></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Education Expenses</label><textarea name="education_expenses" placeholder="e.g. School fees and uniforms shared equally"></textarea><p class="ppb-help">Covers fees, uniforms, excursions, laptops, and tutoring — costs outside the regular child support amount. Agree on how they're split and what counts as an "education expense."</p></div>
        <div class="ppb-form-group"><label>Medical &amp; Dental Expenses</label><textarea name="health_expenses" placeholder="e.g. Out-of-pocket costs shared equally after Medicare rebate"></textarea><p class="ppb-help">Covers out-of-pocket costs after Medicare and private health rebates. Agree who pays upfront and how the other parent reimburses their share.</p></div>
      </div>
    </div>

    <!-- Step 9: Dispute Resolution -->
    <div class="ppb-section" data-section="9">
      <div class="ppb-section-header">
        <h3 class="ppb-section-title">Dispute Resolution &amp; Other Provisions</h3>
        <p class="ppb-section-subtitle">How disagreements will be handled, and any other terms you want to include.</p>
      </div>
      <div class="ppb-form-group"><label>Dispute Resolution Process</label><textarea name="dispute_process" placeholder="e.g. Direct discussion first, then Family Dispute Resolution with an accredited mediator, then legal proceedings if unresolved"></textarea><p class="ppb-help">This clause sets out the steps both parents agree to follow when a disagreement arises. A tiered process — direct discussion first, then mediation, then court as a last resort — keeps disputes out of the legal system where possible and is required before most court applications anyway.</p></div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Domestic Travel</label><textarea name="travel_domestic" placeholder="e.g. Either parent may travel within Australia with the children; the other parent to be notified at least 7 days in advance with destination and contact details"></textarea><p class="ppb-help">Covers family holidays, interstate trips, and visits to relatives within Australia. Agree on how much notice is required and what details need to be shared (destination, dates, contact number).</p></div>
        <div class="ppb-form-group"><label>International Travel</label><textarea name="travel_international" placeholder="e.g. International travel requires written consent from both parties at least 30 days in advance; passports held by Party 1 and released for travel only by written agreement"></textarea><p class="ppb-help">Taking children overseas without the other parent's consent can be a criminal offence under the Family Law Act. Agree on notice periods, who holds the passports, and how consent is given in writing.</p></div>
      </div>
      <div class="ppb-row">
        <div class="ppb-form-group"><label>Relocation</label><textarea name="relocation" placeholder="e.g. Neither party may relocate with the children more than 50km from their current residence without written agreement from the other party or a court order"></textarea><p class="ppb-help">Relocation — moving far enough to significantly affect the care arrangement — is one of the most litigated issues in family law. This clause doesn't prevent either parent from moving, but requires agreement or a court order before the children move with them.</p></div>
        <div class="ppb-form-group"><label>Introduction of New Partners</label><textarea name="new_partners" placeholder="e.g. New partners introduced only after 6 months of relationship"></textarea><p class="ppb-help">Covers when and how new romantic partners are introduced to the children. Some parents prefer a minimum relationship duration; others simply ask for advance notice. There's no legal requirement — this is a personal agreement between the parties.</p></div>
      </div>
      <div class="ppb-form-group"><label>Additional Provisions</label><textarea name="additional_provisions" placeholder="Any other terms the parties agree to include"></textarea><p class="ppb-help">Anything not covered in the earlier steps — for example, agreements about screen time, dietary requirements, religious observances, or how to handle school report cards and medical appointments.</p></div>
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
      <div style="margin-top:32px;padding:24px 28px;background:var(--sand);border:1px solid var(--line);border-radius:14px;text-align:center">
        <p style="font-family:var(--sans);font-size:.95rem;color:var(--ink);margin:0 0 14px;line-height:1.6">We hope this parenting plan builder has been useful. If it has, spreading the word helps other separated parents find it — we'd be grateful for a quick Google review.</p>
        <a href="https://g.page/r/CZcsK4llG5XFEAE/review" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:10px;padding:13px 24px;background:#fff;border:1.5px solid var(--line);border-radius:100px;font-family:var(--sans);font-size:.9rem;font-weight:600;color:var(--ink);text-decoration:none;transition:border-color .2s,box-shadow .2s" onmouseover="this.style.borderColor='var(--sage)';this.style.boxShadow='0 4px 12px rgba(41,75,142,.12)'" onmouseout="this.style.borderColor='var(--line)';this.style.boxShadow='none'">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#f4b400" stroke="#f4b400" stroke-width="1" stroke-linejoin="round"/></svg>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#f4b400" stroke="#f4b400" stroke-width="1" stroke-linejoin="round"/></svg>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#f4b400" stroke="#f4b400" stroke-width="1" stroke-linejoin="round"/></svg>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#f4b400" stroke="#f4b400" stroke-width="1" stroke-linejoin="round"/></svg>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#f4b400" stroke="#f4b400" stroke-width="1" stroke-linejoin="round"/></svg>
          Leave a Google Review
        </a>
      </div>
    </div>

  </form>

  <div class="ppb-nav" id="ppbNav">
    <button type="button" class="ppb-btn-prev" id="ppbPrevBtn" disabled>← Previous</button>
    <button type="button" class="ppb-btn-next" id="ppbNextBtn">Next →</button>
  </div>
</div><!-- /.ppb-card -->
</div><!-- /max-width wrapper -->
</div><!-- /.wrap -->

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

  function changeSection(dir){
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
      row('Children',gd('children_info').replace(/\\n/g,'; '))+
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
    para('Concerning: '+g('children_info').replace(/\\n/g,'; '),11,false,10);
    para('PREAMBLE',13,true,6);
    para('This Parenting Plan is made between '+g('parent1_name')+' and '+g('parent2_name')+' in relation to the care, welfare and development of the above-named child/children. The parties acknowledge that it is in the best interests of the child/children that both parents continue to have meaningful relationships with them, consistent with the best interests principle under the Family Law Act 1975 (Cth).',11,false,10);
    /* Clause 1 */
    para('1. PARENTAL RESPONSIBILITY',12,true,6);
    var pr=g('parental_responsibility');
    if(pr==='equal') para('1.1 The parties shall have equal shared parental responsibility for the child/children.',11,false,4);
    else if(pr==='sole_parent1') para('1.1 '+g('parent1_name')+' shall have sole parental responsibility for the child/children.',11,false,4);
    else if(pr==='sole_parent2') para('1.1 '+g('parent2_name')+' shall have sole parental responsibility for the child/children.',11,false,4);
    var majors=fd.getAll('major_decisions[]');
    if(majors.length) para('1.2 The following major long-term decisions shall require consultation between both parties: '+majors.join(', ')+'.',11,false,4);
    if(g('cultural_upbringing')!=='[To be specified]') para('1.3 Cultural and religious upbringing: '+g('cultural_upbringing'),11,false,10);
    /* Clause 2 */
    para('2. LIVING ARRANGEMENTS',12,true,6);
    var res=g('primary_residence');
    if(res==='equal') para('2.1 The child/children shall spend equal time with both parties in a shared care arrangement.',11,false,4);
    else if(res==='parent1') para('2.1 The child/children shall live primarily with '+g('parent1_name')+' and spend time with '+g('parent2_name')+' per the schedule below.',11,false,4);
    else if(res==='parent2') para('2.1 The child/children shall live primarily with '+g('parent2_name')+' and spend time with '+g('parent1_name')+' per the schedule below.',11,false,4);
    para('2.2 Care schedule: '+g('schedule_type')+'.',11,false,4);
    if(g('schedule_details')!=='[To be specified]') para('2.3 '+g('schedule_details'),11,false,4);
    if(g('changeover_details')!=='[To be specified]') para('2.4 Changeovers: '+g('changeover_details'),11,false,4);
    if(g('extended_family')!=='[To be specified]') para('2.5 Grandparents and extended family: '+g('extended_family'),11,false,10);
    /* Clause 3 */
    para('3. HOLIDAYS AND SPECIAL OCCASIONS',12,true,6);
    [['3.1 Christmas and New Year','christmas_arrangement'],['3.2 Easter','easter_arrangement'],['3.3 School holidays','school_holidays'],['3.4 Birthdays','children_birthdays'],["3.5 Mother's and Father's Day",'parents_day']].forEach(function(a){if(g(a[1])!=='[To be specified]') para(a[0]+': '+g(a[1]),11,false,4);});y+=4;
    /* Clause 4 */
    para('4. COMMUNICATION',12,true,6);
    var comms=fd.getAll('parent_communication[]');
    if(comms.length) para('4.1 Communication between parents shall be by: '+comms.join(', ')+'.',11,false,4);
    if(g('child_contact')!=='[To be specified]') para('4.2 The child/children may contact the other parent: '+g('child_contact'),11,false,4);
    if(g('social_media')!=='[To be specified]') para('4.3 Photos and social media: '+g('social_media'),11,false,10);
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
    if(g('travel_domestic')!=='[To be specified]') para('8.2 Domestic travel: '+g('travel_domestic'),11,false,4);
    if(g('travel_international')!=='[To be specified]') para('8.3 International travel: '+g('travel_international'),11,false,4);
    if(g('relocation')!=='[To be specified]') para('8.4 Relocation: '+g('relocation'),11,false,4);
    if(g('new_partners')!=='[To be specified]') para('8.5 Introduction of new partners: '+g('new_partners'),11,false,4);
    if(g('additional_provisions')!=='[To be specified]') para('8.6 Additional provisions: '+g('additional_provisions'),11,false,10);
    /* Execution block — pre-calculate height, check once, then render without internal page breaks */
    var ePara=doc.splitTextToSize('The parties agree to be bound by the terms of this Parenting Plan and acknowledge they have read and understood its contents. This Plan may be varied by mutual written agreement at any time.',W);
    var eNotice=doc.splitTextToSize('IMPORTANT: A parenting plan is not a legally enforceable agreement. If you want your agreement to be legally binding and enforceable, you must apply to the Family Court for consent orders. Seek independent legal advice before signing.',W);
    var eHeight=16+10+ePara.length*5.5+10+eNotice.length*4.5+24+16+8+8+16;
    chk(eHeight);
    doc.setDrawColor(180,180,180);doc.setLineWidth(0.4);doc.line(M,y,190,y);doc.setDrawColor(0,0,0);doc.setLineWidth(0.2);y+=16;
    doc.setFont('helvetica','bold');doc.setFontSize(12);doc.text('EXECUTION',M,y);y+=10;
    doc.setFont('helvetica','normal');doc.setFontSize(11);doc.text(ePara,M,y);y+=ePara.length*5.5+10;
    doc.setFont('helvetica','italic');doc.setFontSize(9);doc.text(eNotice,M,y);y+=eNotice.length*4.5+24;
    doc.setFont('helvetica','normal');doc.setFontSize(9);
    doc.text(g('parent1_name'),M,y);doc.text(g('parent2_name'),110,y);y+=16;
    doc.setLineWidth(0.5);doc.line(M,y,90,y);doc.line(110,y,180,y);doc.setLineWidth(0.2);y+=8;
    doc.text('Signature',M,y);doc.text('Signature',110,y);y+=8;
    doc.text('Date: ____________________',M,y);doc.text('Date: ____________________',110,y);
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
# Download box shown above the builder on /parenting-plan-template/ (brief §4.1)
PPT_DOWNLOAD_BOX = """<div class="wrap-narrow"><div class="answer reveal" style="margin-top:1.5rem">
<p style="margin:0 0 .5rem"><strong>Download the free template:</strong> a blank parenting plan worksheet, no sign-up needed.</p>
<p style="margin:0;display:flex;gap:12px;flex-wrap:wrap">
<a class="btn btn-primary" href="/downloads/parenting-plan-template.pdf">PDF (5 pages, 140 KB)</a>
<a class="btn btn-ghost" href="/downloads/parenting-plan-template.docx">Word, editable (13 KB)</a></p>
<p style="margin:.6rem 0 0;font-size:.85rem">A discussion worksheet, not a court document. <a href="#download">How to use it</a></p>
</div></div>"""

build("parenting-plan-template",
 "Free Parenting Plan Template Australia | PDF & Word",
 "Download a free editable parenting plan template, explore practical examples, and understand how a parenting plan differs from enforceable court orders.",
 "A practical guide for separated parents",
 "Free parenting plan template for Australian parents",
 "Download our free parenting plan template as a <a href=\"/downloads/parenting-plan-template.pdf\"><strong>PDF</strong></a> or editable <a href=\"/downloads/parenting-plan-template.docx\"><strong>Word document</strong></a>, with no sign-up. Then use this guide to work through every section a thorough Australian parenting plan should cover, with worked examples and common mistakes to avoid.",
 "A parenting plan records agreed arrangements for children after separation. A template can help parents discuss practical details, but it does not replace individual legal advice or become a court order simply because it is signed. Download the blank worksheet below (PDF or Word), use the checklist to consider your child's needs, and seek help where safety concerns or disagreement make discussion difficult.",
 """
 <h2>What is a parenting plan?</h2>
 <p>A parenting plan is a written agreement between separated parents that sets out how their children will be raised across two households. Under the <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act 1975</a>, a parenting plan must be in writing and signed and dated by both parents. It is not a court order, but a court will consider it in any later dispute — and it is far more useful than an oral agreement that each party later remembers differently.</p>
 <p>A parenting plan is different from <a href="/consent-orders/">consent orders</a>, which are court-approved and directly enforceable. Many families use a parenting plan as a starting point and later formalise it as consent orders once arrangements have settled.</p>

 <h2 id="download">Download the blank parenting plan (PDF and Word)</h2>
 <p>Our free parenting plan template is a <strong>discussion worksheet</strong> with ten sections and space to write what you agree. No email or sign-up is needed.</p>
 <ul>
   <li><a href="/downloads/parenting-plan-template.pdf">Parenting plan template, PDF</a> (5 pages, about 140 KB): print it and fill it in by hand.</li>
   <li><a href="/downloads/parenting-plan-template.docx">Parenting plan template, Word</a> (about 13 KB): type into it on a computer and save your own copy.</li>
 </ul>
 <h3>How to use, edit and print it</h3>
 <p>Work through each section together, or separately before a mediation session. Leave sections blank if they do not apply. When you have agreed, Family Relationships Online explains that a parenting plan must be <strong>in writing, dated and signed by both parents</strong>, and can include ways to change arrangements and resolve disagreements (<a href="https://www.familyrelationships.gov.au/separation/family-mediation-dispute-res" target="_blank" rel="noopener">Family Relationships Online</a>). Keep a signed copy each. Children do not sign the plan.</p>
 <h3>When not to use a generic template</h3>
 <p>A template is a starting point, not a solution for every family. Get advice before relying on one if:</p>
 <ul>
   <li>there is family violence, abuse, coercion or a risk to a child;</li>
   <li>court orders already exist about the children;</li>
   <li>one parent wants to relocate a long distance;</li>
   <li>a child has complex health or developmental needs;</li>
   <li>you cannot discuss arrangements without pressure or fear.</li>
 </ul>
 <p>Prefer to build your plan step by step on screen? The interactive builder above walks you through the same topics.</p>

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

 <h2 id="states">Is this template valid in NSW, Queensland and Victoria?</h2>
 <p>Yes, the same template works across Australia. Parenting plans are part of federal family law under the <a href="https://www.legislation.gov.au/C2004A00275/latest/text" target="_blank" rel="noopener">Family Law Act 1975</a>, so there is no separate NSW, Queensland or Victorian parenting plan. What changes between families is the content, not the state.</p>
 <p><strong>Western Australia</strong> is the exception in procedure: WA has its own Family Court, and de facto matters there run under WA law. If you live in WA, check the <a href="https://www.familycourt.wa.gov.au/" target="_blank" rel="noopener">Family Court of Western Australia</a> or get local advice before formalising anything.</p>

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

 <h3>If you already have parenting orders</h3>
 <p>Do not assume a new parenting plan simply replaces existing court orders. How a later plan interacts with orders is a legal question, so get legal advice before agreeing to different arrangements or acting on them.</p>

 <h2>Common mistakes in parenting plans</h2>
 <ul>
   <li><strong>Too vague</strong> — "reasonable time with each parent" sounds flexible but causes constant negotiation and disputes.</li>
   <li><strong>No holiday detail</strong> — leaving holidays as "to be agreed" is the most common source of conflict.</li>
   <li><strong>No changeover specifics</strong> — ambiguity about time and place breeds conflict at handover.</li>
   <li><strong>Forgetting the children's activities</strong> — who drives to sport, who pays for extracurriculars, what happens when activities conflict with changeover?</li>
   <li><strong>No review mechanism</strong> — a plan written when a child is 4 won't suit a teenager.</li>
 </ul>

 <h2 id="safety">Safety and suitability</h2>
 <p>A parenting plan should be agreed freely. If you feel pressured, afraid or unsafe, do not use the template to negotiate directly with the other parent. A family dispute resolution practitioner assesses whether mediation is suitable, considering family violence, safety, bargaining power and risks to children, and may offer separate-room, telephone or video sessions. In an emergency call <strong>000</strong>; for confidential support call <a href="https://www.1800respect.org.au/" target="_blank" rel="noopener">1800RESPECT</a> on 1800 737 732.</p>

 <h2>How mediation helps you build a better plan</h2>
 <p>A mediator doesn't draft the plan for you — they help you and the other parent work through each section together, drawing out the details that matter, surfacing disagreements early, and finding workable solutions. The result is a plan both parents have genuinely agreed to, which is what makes it last. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
 """,
 [("Is there a free parenting plan template I can download?",
   "Yes. Our parenting plan template is free to download as a PDF or editable Word document, with no sign-up. It is a discussion worksheet, not a court document."),
  ("Is a parenting plan the same as a court order?",
   "No. A parenting plan records an agreement between parents, while a court order is made by a court. Parents can record mediation agreements in a written parenting plan and renegotiate it over time. Get legal advice about enforceability and any existing orders."),
  ("What makes a written parenting plan?",
   "Family Relationships Online says a parenting plan must be in writing, dated and signed by both parents. Those formal features do not mean any arrangement is safe or suitable, so seek individual advice before signing."),
  ("Do we have to sit together to work on the plan?",
   "Not necessarily. An FDR practitioner assesses whether mediation is suitable and may offer separate-room, telephone or video sessions. Tell the practitioner about any concerns before starting."),
  ("Is there a different template for NSW, Queensland or Victoria?",
   "No. Parenting plans fall under federal family law, so the same template works in every state. Western Australia has its own Family Court, so WA parents should check local procedures."),
  ("What should be included in a parenting plan in Australia?",
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
 tool_html=PPT_DOWNLOAD_BOX+PARENTING_BUILDER,tool_position='before')

# ---- BFA OR CONSENT ORDERS ----
# bfa-or-consent-orders: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- GETTING READY FOR SEPARATION ----
# getting-ready-for-separation: moved to gen_blog_batch35.py (blog template, Nov 2026)

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
# separation-under-one-roof: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- UNFAIR DISMISSAL: 21-DAY RULE ----
# unfair-dismissal-21-day-rule: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- IS MEDIATION RIGHT FOR YOUR WORKPLACE DISPUTE? ----
# is-mediation-right-for-workplace-dispute: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- REDUNDANCY: WAS IT GENUINE? ----
# redundancy-was-it-genuine: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- CONTESTING A WILL: YOUR OPTIONS ----
# contesting-a-will: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- COMMERCIAL DISPUTE GUIDE ----
# commercial-dispute-guide: moved to gen_blog_batch34.py (blog template, Nov 2026)

# ---- REAL ESTATE & CONSTRUCTION DISPUTES ----
# real-estate-construction-disputes: moved to gen_blog_batch35.py (blog template, Nov 2026)

# ---- WORKPLACE DISPUTE GUIDE ----
# workplace-dispute-guide: moved to gen_blog_batch35.py (blog template, Nov 2026)

print("Resource pages built.")
