#!/usr/bin/env python3
"""Australian Mediation Preparation Tool — prepare-for-mediation page."""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─────────────────────────────────────────────────────────────────────────────
#  TOOL HTML
# ─────────────────────────────────────────────────────────────────────────────
TOOL_HTML = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<section class="sec mpt-outer" style="border-top:2px solid var(--line);padding:80px 0 96px;background:var(--sand)">
<div class="wrap" style="max-width:860px">

<div style="text-align:center;margin-bottom:56px">
  <p class="sec-tag">Free Australian tool</p>
  <h2 class="sec-title" style="margin-bottom:16px">Prepare for <em>Mediation</em></h2>
  <p style="color:var(--ink-soft);max-width:56ch;margin:0 auto;font-size:1.05rem;line-height:1.7">A free guided tool for Australians involved in a family or property dispute. Work through your issues, clarify your priorities, and download a personal Mediation Preparation Summary.</p>
</div>

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:52px" class="mpt-intro-grid">
  <div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 24px">
    <div style="width:44px;height:44px;background:rgba(30,96,64,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    </div>
    <h3 style="font-family:var(--sans);font-size:1rem;font-weight:700;color:var(--ink);margin:0 0 8px">Who it&rsquo;s for</h3>
    <p style="font-size:.9rem;color:var(--ink-soft);line-height:1.65;margin:0">Anyone preparing for mediation in Australia &mdash; parenting arrangements, property settlement, or other disputes. No account required.</p>
  </div>
  <div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 24px">
    <div style="width:44px;height:44px;background:rgba(30,96,64,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
    </div>
    <h3 style="font-family:var(--sans);font-size:1rem;font-weight:700;color:var(--ink);margin:0 0 8px">How it works</h3>
    <p style="font-size:.9rem;color:var(--ink-soft);line-height:1.65;margin:0">9 guided steps covering your dispute type, key issues, current arrangements, and priorities. Nothing stored on our servers.</p>
  </div>
  <div style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:28px 24px">
    <div style="width:44px;height:44px;background:rgba(30,96,64,.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--sage)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
    </div>
    <h3 style="font-family:var(--sans);font-size:1rem;font-weight:700;color:var(--ink);margin:0 0 8px">What you get</h3>
    <p style="font-size:.9rem;color:var(--ink-soft);line-height:1.65;margin:0">A PDF Mediation Preparation Summary to keep, bring to your session, or share with your mediator. General information only &mdash; not legal advice.</p>
  </div>
</div>
<style>@media(max-width:640px){.mpt-intro-grid{grid-template-columns:1fr!important}}</style>

<div style="max-width:800px;margin:0 auto">
<style>
.mpt-card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:40px 44px;box-shadow:var(--shadow)}
.mpt-stepper{display:flex;align-items:center;justify-content:space-between;margin-bottom:36px;gap:3px}
.mpt-step{display:flex;flex-direction:column;align-items:center;gap:4px;flex:1;cursor:default}
.mpt-step-dot{width:26px;height:26px;border-radius:50%;border:2px solid var(--line);background:#fff;display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:700;font-family:var(--sans);color:var(--ink-soft);transition:all .25s;flex-shrink:0}
.mpt-step.done .mpt-step-dot{background:var(--sage);border-color:var(--sage);color:#fff}
.mpt-step.active .mpt-step-dot{background:var(--sage);border-color:var(--sage);color:#fff;box-shadow:0 0 0 4px rgba(30,96,64,.15)}
.mpt-step-label{font-size:.6rem;font-family:var(--sans);font-weight:500;color:var(--ink-soft);text-align:center;display:none}
.mpt-step.active .mpt-step-label{display:block;color:var(--sage);font-weight:600}
.mpt-step-conn{height:2px;flex:1;background:var(--line);border-radius:1px;margin-bottom:20px;transition:background .25s;min-width:4px}
.mpt-step-conn.done{background:var(--sage)}
.mpt-progress-wrap{margin-bottom:6px}
.mpt-progress-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;font-family:var(--sans);font-size:.82rem;color:var(--ink-soft)}
.mpt-progress-meta strong{color:var(--ink)}
.mpt-progress{background:var(--sand-deep);height:6px;border-radius:3px;overflow:hidden}
.mpt-progress-bar{height:100%;background:var(--sage);border-radius:3px;transition:width .35s cubic-bezier(.16,1,.3,1);width:0%}
.mpt-section{display:none}.mpt-section.active{display:block;animation:mptFade .2s ease}
@keyframes mptFade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.mpt-section-header{margin-bottom:28px;padding-bottom:20px;border-bottom:1px solid var(--line)}
.mpt-section-title{font-size:1.35rem;color:var(--ink);margin:0 0 4px;font-family:var(--serif);font-weight:500;line-height:1.25}
.mpt-section-sub{font-size:.9rem;color:var(--ink-soft);font-family:var(--sans);margin:0}
.mpt-group{margin-bottom:22px}
.mpt-group .mpt-lbl{display:block;margin-bottom:8px;color:var(--ink);font-weight:600;font-size:.88rem;font-family:var(--sans);letter-spacing:.01em}
.mpt-help{font-size:.82rem;color:var(--ink-soft);font-family:var(--sans);margin-top:6px;line-height:1.6}
.mpt-group select,.mpt-group input[type=text],.mpt-group textarea{width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:10px;font-size:.95rem;font-family:var(--sans);color:var(--ink);background:#fff;outline:none;transition:border-color .2s;box-sizing:border-box}
.mpt-group select:focus,.mpt-group input[type=text]:focus,.mpt-group textarea:focus{border-color:var(--sage)}
.mpt-group textarea{min-height:96px;resize:vertical;line-height:1.6}
.mpt-group input[type=date]{accent-color:var(--sage);color-scheme:light;padding:12px 14px;border:1.5px solid var(--line);border-radius:10px;font-size:.95rem;font-family:var(--sans);color:var(--ink);background:#fff;outline:none;transition:border-color .2s;width:100%;box-sizing:border-box}
.mpt-group input[type=date]:focus{border-color:var(--sage)}
.mpt-radios,.mpt-checks{display:flex;flex-direction:column;gap:8px}
.mpt-radio-opt,.mpt-check-opt{display:flex;align-items:flex-start;gap:12px;padding:13px 16px;border:1.5px solid var(--line);border-radius:12px;cursor:pointer;transition:border-color .2s,background .2s;background:#fff;font-family:var(--sans);font-size:.9rem;color:var(--ink);line-height:1.5}
.mpt-radio-opt:hover,.mpt-check-opt:hover{border-color:var(--sage);background:rgba(30,96,64,.04)}
.mpt-radio-opt input,.mpt-check-opt input{accent-color:var(--sage);margin-top:2px;flex-shrink:0;width:16px;height:16px}
.mpt-radio-opt.sel,.mpt-check-opt.sel{border-color:var(--sage);background:rgba(30,96,64,.06)}
.mpt-cg{margin-bottom:18px}
.mpt-cg-label{font-size:.78rem;font-weight:700;font-family:var(--sans);color:var(--ink-soft);letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
.mpt-nav{display:flex;justify-content:space-between;align-items:center;margin-top:32px;padding-top:24px;border-top:1px solid var(--line)}
.mpt-back{font-family:var(--sans);font-size:.9rem;font-weight:600;color:var(--ink-soft);background:none;border:1.5px solid var(--line);border-radius:40px;padding:11px 24px;cursor:pointer;transition:all .2s}
.mpt-back:hover{border-color:var(--ink-soft);color:var(--ink)}
.mpt-next,.mpt-dl{font-family:var(--sans);font-size:.95rem;font-weight:700;color:#fff;background:var(--sage);border:none;border-radius:40px;padding:12px 32px;cursor:pointer;transition:background .2s}
.mpt-next:hover,.mpt-dl:hover{background:#174d33}
.mpt-notice{background:rgba(30,96,64,.07);border:1px solid rgba(30,96,64,.2);border-radius:12px;padding:16px 18px;font-size:.84rem;font-family:var(--sans);color:var(--ink-soft);line-height:1.65;margin-bottom:20px}
.mpt-notice strong{color:var(--ink)}
.mpt-wa{background:rgba(255,160,0,.08);border:1px solid rgba(255,160,0,.35);border-radius:12px;padding:16px 18px;font-size:.84rem;font-family:var(--sans);color:var(--ink-soft);line-height:1.65;margin-bottom:20px;display:none}
.mpt-warn{background:rgba(210,50,50,.06);border:1px solid rgba(210,50,50,.2);border-radius:12px;padding:16px 18px;font-size:.84rem;font-family:var(--sans);color:var(--ink-soft);line-height:1.65;margin-bottom:20px;display:none}
.mpt-rv{padding:14px 0;border-bottom:1px solid var(--line);display:flex;gap:16px}
.mpt-rv-l{font-size:.78rem;font-weight:700;font-family:var(--sans);color:var(--ink-soft);text-transform:uppercase;letter-spacing:.05em;min-width:130px;flex-shrink:0;padding-top:2px}
.mpt-rv-v{font-size:.88rem;font-family:var(--sans);color:var(--ink);line-height:1.6}
/* Branch visibility */
.mpt-p,.mpt-f{display:none}
.mpt-bp .mpt-p{display:block}
.mpt-bf .mpt-f{display:block}
@media(max-width:600px){
  .mpt-card{padding:28px 20px}
  .mpt-step-label{display:none!important}
  .mpt-rv{flex-direction:column;gap:2px}
  .mpt-rv-l{min-width:0}
}
</style>

<div class="mpt-card">
  <div class="mpt-stepper" id="mptStepper"></div>
  <div class="mpt-progress-wrap">
    <div class="mpt-progress-meta">
      <span><strong id="mptStepLbl">Step 1 of 9</strong></span>
      <span id="mptPct">0% complete</span>
    </div>
    <div class="mpt-progress"><div class="mpt-progress-bar" id="mptBar"></div></div>
  </div>

  <form id="mptForm">

  <!-- 1 Getting started -->
  <div class="mpt-section active" data-s="1">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Getting started</h3>
      <p class="mpt-section-sub">A few basics to personalise your preparation summary.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_state">Which Australian state or territory is most closely connected with your dispute?</label>
      <select name="mpt_state" id="mpt_state">
        <option value="">&#8212; Select &#8212;</option>
        <option value="ACT">Australian Capital Territory</option>
        <option value="NSW">New South Wales</option>
        <option value="NT">Northern Territory</option>
        <option value="QLD">Queensland</option>
        <option value="SA">South Australia</option>
        <option value="TAS">Tasmania</option>
        <option value="VIC">Victoria</option>
        <option value="WA">Western Australia</option>
        <option value="Multiple">More than one state or territory</option>
        <option value="Unsure">I&rsquo;m not sure</option>
      </select>
      <p class="mpt-help">Laws, courts, tribunals and dispute-resolution processes can differ between Australian states and territories. We ask this so the tool can flag relevant information.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_name">Your first name <span style="font-weight:400;color:var(--ink-soft)">(optional &mdash; appears only in your PDF)</span></label>
      <input type="text" name="mpt_name" id="mpt_name" placeholder="e.g. Alex">
    </div>
    <div class="mpt-notice">
      <strong>General information only.</strong> This tool helps you organise your thinking and identify issues to discuss in mediation. It does not give legal advice, assess legal merits, or determine your rights. Nothing you enter is stored on our servers. If you need advice about your situation, consider consulting an Australian lawyer.
    </div>
  </div>

  <!-- 2 Dispute type -->
  <div class="mpt-section" data-s="2">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Your dispute</h3>
      <p class="mpt-section-sub">Select the type of dispute you&rsquo;re preparing for.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl">What best describes your dispute?</label>
      <div class="mpt-radios">
        <label class="mpt-radio-opt">
          <input type="radio" name="mpt_type" value="parenting">
          <span><strong>Family and Parenting</strong><br><span style="font-size:.82rem;color:var(--ink-soft)">Parenting arrangements, where children live, time with each parent, parental responsibility</span></span>
        </label>
        <label class="mpt-radio-opt">
          <input type="radio" name="mpt_type" value="property">
          <span><strong>Separation and Property</strong><br><span style="font-size:.82rem;color:var(--ink-soft)">Property settlement, superannuation, financial disclosure, spousal maintenance</span></span>
        </label>
      </div>
      <p class="mpt-help">Your answers in the following steps will be tailored to the type you select. If your dispute involves both, choose the one you most want to prepare for now.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_brief">Briefly describe the dispute in your own words <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <textarea name="mpt_brief" id="mpt_brief" placeholder="e.g. We separated 6 months ago and are working out arrangements for our two children and the family home..."></textarea>
      <p class="mpt-help">This appears in your preparation summary. Please avoid entering identification numbers, financial account numbers, or information that is not necessary for your preparation.</p>
    </div>
  </div>

  <!-- 3 About the situation (branched) -->
  <div class="mpt-section" data-s="3">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">About the situation</h3>
      <p class="mpt-section-sub" id="mptS3sub">Tell us a little more about your situation.</p>
    </div>

    <!-- Parenting branch -->
    <div class="mpt-p">
      <div class="mpt-wa" id="mptWa">
        <strong>Western Australia:</strong> Family-law processes in Western Australia differ from those in other states and territories. For parenting matters, a certificate under <strong>section 66H of the <em>Family Court Act 1997</em> (WA)</strong> may be relevant rather than a section 60I certificate under the federal Act. Proceedings may involve the Family Court of Western Australia. Consider obtaining advice specific to Western Australia if formal proceedings or orders are relevant.
      </div>
      <div class="mpt-group">
        <label class="mpt-lbl">Have you participated in Family Dispute Resolution (FDR) about these issues?</label>
        <div class="mpt-radios" id="mptFdrOpts">
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="yes"> Yes &mdash; we have participated in FDR</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="no"> No &mdash; we have not yet attended FDR</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="arranged"> FDR has been arranged</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="cert60i"> I have a section 60I certificate</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="cert66h"> I have a section 66H certificate (WA)</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="exempt"> I believe an exemption may apply</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_fdr" value="unsure"> I&rsquo;m not sure</label>
        </div>
        <p class="mpt-help">Family Dispute Resolution is a process used to help people affected by separation resolve family-law disputes. A registered Family Dispute Resolution Practitioner conducts FDR. Completing this tool is not FDR and does not result in the issue of a section 60I or 66H certificate.</p>
      </div>
      <div class="mpt-notice" id="mptFdrNote" style="display:none">
        <strong>FDR and parenting applications:</strong> In many parenting matters, people are required to make a genuine effort to resolve their dispute through Family Dispute Resolution before applying to a family law court for parenting orders, unless an exception applies. A registered Family Dispute Resolution Practitioner may issue a certificate under section 60I of the <em>Family Law Act 1975</em> (Cth) (or section 66H in WA) in circumstances provided by the legislation.
      </div>
      <div class="mpt-group">
        <label class="mpt-lbl" for="mpt_children">Children involved <span style="font-weight:400;color:var(--ink-soft)">(optional &mdash; first names or ages only)</span></label>
        <input type="text" name="mpt_children" id="mpt_children" placeholder="e.g. Two children, ages 8 and 11">
        <p class="mpt-help">First names or approximate ages are sufficient. You do not need to provide full names or dates of birth.</p>
      </div>
      <div class="mpt-group">
        <label class="mpt-lbl" for="mpt_other_p">The other parent <span style="font-weight:400;color:var(--ink-soft)">(optional &mdash; first name only)</span></label>
        <input type="text" name="mpt_other_p" id="mpt_other_p" placeholder="e.g. Jamie, or 'former partner'">
      </div>
    </div>

    <!-- Property branch -->
    <div class="mpt-f">
      <div class="mpt-group">
        <label class="mpt-lbl" for="mpt_sep_when">When did the separation occur? <span style="font-weight:400;color:var(--ink-soft)">(approximate, optional)</span></label>
        <input type="text" name="mpt_sep_when" id="mpt_sep_when" placeholder="e.g. Early 2024, or approximately 18 months ago">
        <p class="mpt-help">An approximate date or year is sufficient.</p>
      </div>
      <div class="mpt-group">
        <label class="mpt-lbl" for="mpt_other_f">The other party <span style="font-weight:400;color:var(--ink-soft)">(optional &mdash; first name only)</span></label>
        <input type="text" name="mpt_other_f" id="mpt_other_f" placeholder="e.g. Sam, or 'former partner'">
      </div>
      <div class="mpt-group">
        <label class="mpt-lbl">Is the former family home still involved in the dispute?</label>
        <div class="mpt-radios">
          <label class="mpt-radio-opt"><input type="radio" name="mpt_home" value="jointly_owned"> Jointly owned &mdash; not yet resolved</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_home" value="one_living"> One party is living in it</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_home" value="sold"> It has already been sold</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_home" value="renting"> We were renting &mdash; no family home</label>
          <label class="mpt-radio-opt"><input type="radio" name="mpt_home" value="na"> Not applicable</label>
        </div>
      </div>
      <div class="mpt-notice">
        <strong>Property and financial agreements:</strong> Agreements about property or financial matters following separation may require specific formal steps to be legally enforceable. Consider obtaining independent legal advice about how any agreement should be documented.
      </div>
    </div>
  </div>

  <!-- 4 Issues to discuss (branched) -->
  <div class="mpt-section" data-s="4">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Issues to discuss</h3>
      <p class="mpt-section-sub">Select the issues you want to raise in mediation. Tick all that apply.</p>
    </div>

    <!-- Parenting issues -->
    <div class="mpt-p">
      <div class="mpt-cg">
        <div class="mpt-cg-label">Living &amp; time arrangements</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Where the children live"> Where the children live</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Time with each parent"> Time with each parent</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Weekday arrangements"> Weekday arrangements</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Weekend arrangements"> Weekend arrangements</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Changeovers"> Changeovers</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Holidays &amp; special occasions</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="School holidays"> School holidays</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Christmas and New Year"> Christmas and New Year</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Easter"> Easter</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Birthdays"> Birthdays</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Mother's Day and Father's Day"> Mother&rsquo;s Day and Father&rsquo;s Day</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Religious or cultural occasions"> Religious or cultural occasions</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Parenting decisions</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Education and school choice"> Education and school choice</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Health and medical treatment"> Health and medical treatment</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Major long-term decisions"> Major long-term decisions</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Extracurricular activities"> Extracurricular activities</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Cultural and religious upbringing"> Cultural and religious upbringing</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Communication</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Communication with the children"> Communication with the children</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Communication between parents"> Communication between parents</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Travel &amp; relocation</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Interstate travel"> Interstate travel</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Overseas travel and passports"> Overseas travel and passports</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Relocation"> Relocation</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Extended family &amp; others</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Grandparents and extended family"> Grandparents and extended family</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="New partners"> New partners</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Financial &amp; ongoing</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Child support"> Child support</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Child-related expenses"> Child-related expenses</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Review of arrangements over time"> Review of arrangements over time</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Process for resolving future disagreements"> Process for resolving future disagreements</label>
        </div>
      </div>
    </div>

    <!-- Property/financial issues -->
    <div class="mpt-f">
      <div class="mpt-cg">
        <div class="mpt-cg-label">Property</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Family home"> Family home</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Investment property"> Investment property</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Property valuations"> Property valuations</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Financial assets</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Bank accounts and savings"> Bank accounts and savings</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Shares and managed investments"> Shares and managed investments</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Superannuation"> Superannuation</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Businesses and business valuations"> Businesses and business valuations</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Trusts and companies"> Trusts and companies</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Vehicles &amp; personal property</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Motor vehicles"> Motor vehicles</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Personal property"> Personal property</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Liabilities</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Mortgage"> Mortgage</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Personal loans and credit cards"> Personal loans and credit cards</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="HECS-HELP or study debts"> HECS-HELP or study debts</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Tax liabilities"> Tax liabilities</label>
        </div>
      </div>
      <div class="mpt-cg">
        <div class="mpt-cg-label">Other financial matters</div>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Financial disclosure"> Financial disclosure</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Spousal maintenance"> Spousal maintenance</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Inheritances or gifts"> Inheritances or gifts</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_issues[]" value="Child-related expenses"> Child-related expenses</label>
        </div>
      </div>
    </div>

    <div class="mpt-group" style="margin-top:16px">
      <label class="mpt-lbl" for="mpt_issues_other">Any other issues not listed above? <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <input type="text" name="mpt_issues_other" id="mpt_issues_other" placeholder="e.g. Specific item, pets, business assets not listed...">
    </div>
  </div>

  <!-- 5 Current arrangements -->
  <div class="mpt-section" data-s="5">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Current arrangements</h3>
      <p class="mpt-section-sub">Are any arrangements or orders currently in place?</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl">Select any that apply:</label>
      <div class="mpt-checks">
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Informal arrangements"> Informal arrangements</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Parenting plan"> Parenting plan</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Interim parenting orders"> Interim parenting orders</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Final parenting orders"> Final parenting orders</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Consent orders"> Consent orders</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Other court orders"> Other court orders</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="Proposed agreement only"> Proposed agreement only</label>
        <label class="mpt-check-opt"><input type="checkbox" name="mpt_current[]" value="No formal arrangements"> No formal arrangements</label>
      </div>
    </div>
    <div class="mpt-warn" id="mptOrdersWarn">
      <strong>Existing court orders:</strong> Existing court orders can have legal consequences. If you are considering arrangements that differ from existing orders, consider obtaining independent legal advice before agreeing to changes.
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_current_detail">Describe the current arrangements briefly <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <textarea name="mpt_current_detail" id="mpt_current_detail" placeholder="e.g. Children currently spend alternate weekends with each parent. No formal orders are in place."></textarea>
    </div>
  </div>

  <!-- 6 Areas of agreement -->
  <div class="mpt-section" data-s="6">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Areas of agreement</h3>
      <p class="mpt-section-sub">Knowing what you&rsquo;ve already agreed helps focus mediation on what remains unresolved.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_agreed">What have you and the other party already agreed, if anything? <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <textarea name="mpt_agreed" id="mpt_agreed" placeholder="e.g. We have agreed that both children will remain at their current school. We have not yet agreed on holiday arrangements or changeover locations."></textarea>
      <p class="mpt-help">Include areas of both agreement and disagreement. If you haven&rsquo;t agreed on anything yet, leave this blank.</p>
    </div>
  </div>

  <!-- 7 Priorities -->
  <div class="mpt-section" data-s="7">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Your priorities</h3>
      <p class="mpt-section-sub">What matters most to you in reaching an agreement?</p>
    </div>
    <div class="mpt-p">
      <div class="mpt-group">
        <label class="mpt-lbl">Which of these are particularly important to you? <span style="font-weight:400;color:var(--ink-soft)">(select all that apply)</span></label>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Stability for the children"> Stability for the children</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="School routine"> School routine</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Maintaining relationships with each parent"> Maintaining relationships with each parent</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Relationships with siblings"> Relationships with siblings</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Relationships with grandparents and extended family"> Relationships with grandparents and extended family</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Cultural connections"> Cultural connections</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Religious arrangements"> Religious arrangements</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Health needs"> Health needs</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Additional or special needs"> Additional or special needs</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Extracurricular activities"> Extracurricular activities</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Distance between households"> Distance between households</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Parents' work arrangements"> Parents&rsquo; work arrangements</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Age and developmental needs"> Age and developmental needs</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Communication between parents"> Communication between parents</label>
        </div>
      </div>
    </div>
    <div class="mpt-f">
      <div class="mpt-group">
        <label class="mpt-lbl">Which of these are priorities for you? <span style="font-weight:400;color:var(--ink-soft)">(select all that apply)</span></label>
        <div class="mpt-checks">
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Reaching a settlement without going to court"> Reaching a settlement without going to court</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Retaining the family home"> Retaining the family home</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Selling the family home"> Selling the family home</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Protecting superannuation"> Protecting superannuation</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Financial security"> Financial security</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Full financial disclosure"> Full financial disclosure</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Business continuity"> Business continuity</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="Minimising legal costs"> Minimising legal costs</label>
          <label class="mpt-check-opt"><input type="checkbox" name="mpt_pri[]" value="A fair outcome for both parties"> A fair outcome for both parties</label>
        </div>
      </div>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_pri_other">Anything else that&rsquo;s important to you? <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <textarea name="mpt_pri_other" id="mpt_pri_other" style="min-height:72px" placeholder="e.g. I want to avoid court proceedings if possible. It is important that both parties have input into decisions."></textarea>
    </div>
  </div>

  <!-- 8 Questions & notes -->
  <div class="mpt-section" data-s="8">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Questions and notes</h3>
      <p class="mpt-section-sub">Record questions to raise and anything else to remember for your session.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_questions">Questions you want to raise in mediation <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <textarea name="mpt_questions" id="mpt_questions" placeholder="e.g. How will we handle school-night arrangements? What happens if one party wants to move interstate?"></textarea>
      <p class="mpt-help">These are for your own preparation. You can raise as many or as few questions as you like in the session.</p>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl" for="mpt_notes">Additional notes <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <textarea name="mpt_notes" id="mpt_notes" placeholder="e.g. Documents to bring, background context, things to keep in mind..."></textarea>
    </div>
    <div class="mpt-group">
      <label class="mpt-lbl">Is there an upcoming court, tribunal or mediation date? <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
      <input type="date" name="mpt_date" id="mpt_date">
      <input type="text" name="mpt_date_desc" style="margin-top:10px" placeholder="Describe the date (e.g. Mediation session, directions hearing, filing deadline)">
      <p class="mpt-help">Using this tool does not pause, extend or satisfy any court, tribunal, statutory or contractual deadline. If you are concerned about a deadline, obtain advice promptly.</p>
    </div>
  </div>

  <!-- 9 Review & download -->
  <div class="mpt-section" data-s="9">
    <div class="mpt-section-header">
      <h3 class="mpt-section-title">Review and download</h3>
      <p class="mpt-section-sub">Your Mediation Preparation Summary is ready.</p>
    </div>
    <div id="mptReview" style="margin-bottom:24px"></div>
    <div class="mpt-notice">
      <strong>About your summary:</strong> This is a personal preparation document only. It is not legal advice, a legal opinion, an assessment of the merits of the dispute, or a recommendation about settlement. Laws and dispute-resolution procedures differ across Australia. Consider obtaining independent Australian legal advice about your rights, obligations, deadlines or any proposed agreement. Completing this tool does not constitute Family Dispute Resolution and does not result in the issue of a section 60I or section 66H certificate.
    </div>
    <div style="text-align:center;margin:24px 0">
      <button type="button" id="mptDl" class="mpt-dl" style="font-size:1rem;padding:14px 40px">&#11015;&nbsp; Download My Preparation Summary</button>
    </div>
    <div style="text-align:center;padding:28px;background:var(--sand);border-radius:16px;border:1px solid var(--line)">
      <div style="font-size:1.4rem;margin-bottom:8px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p style="font-family:var(--sans);font-size:.92rem;color:var(--ink);margin:0 0 16px;line-height:1.6">We hope this preparation tool has been helpful. If it has, a 5&#8209;star Google review helps other Australians find free resources like this.</p>
      <a href="https://g.page/r/CZcsK4llG5XFEAE/review" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:8px;font-family:var(--sans);font-size:.88rem;font-weight:600;color:var(--sage);text-decoration:none;border:1.5px solid var(--sage);border-radius:40px;padding:10px 20px">Leave a Google Review &#8599;</a>
    </div>
  </div>

  </form>

  <div class="mpt-nav">
    <button type="button" class="mpt-back" id="mptBack" style="visibility:hidden">&#8592; Back</button>
    <button type="button" class="mpt-next" id="mptNext">Next &#8594;</button>
  </div>
</div>

</div><!-- /max-width -->
</div><!-- /wrap -->
</section>

<script>
(function(){
  var LABELS=['About','Dispute','Situation','Issues','Arrangements','Agreed','Priorities','Questions','Download'];
  var cur=1,total=LABELS.length,dtype='';
  var form=document.getElementById('mptForm');
  var bar=document.getElementById('mptBar');
  var slbl=document.getElementById('mptStepLbl');
  var pctEl=document.getElementById('mptPct');
  var back=document.getElementById('mptBack');
  var next=document.getElementById('mptNext');
  var dl=document.getElementById('mptDl');

  /* Build stepper */
  var stpr=document.getElementById('mptStepper');
  LABELS.forEach(function(lbl,i){
    var n=i+1;
    if(i>0){var c=document.createElement('div');c.className='mpt-step-conn';c.id='mptC'+n;stpr.appendChild(c);}
    var s=document.createElement('div');s.className='mpt-step'+(n===1?' active':'');s.id='mptS'+n;
    s.innerHTML='<div class="mpt-step-dot">'+n+'</div><div class="mpt-step-label">'+lbl+'</div>';
    stpr.appendChild(s);
  });

  /* Radio/checkbox highlight */
  document.querySelectorAll('.mpt-radio-opt input,.mpt-check-opt input').forEach(function(inp){
    inp.addEventListener('change',function(){
      if(inp.type==='radio'){
        document.querySelectorAll('input[name="'+inp.name+'"]').forEach(function(r){
          r.closest('.mpt-radio-opt').classList.toggle('sel',r.checked);
        });
      } else {
        inp.closest('.mpt-check-opt').classList.toggle('sel',inp.checked);
      }
    });
  });

  /* Dispute type branch */
  document.querySelectorAll('input[name="mpt_type"]').forEach(function(r){
    r.addEventListener('change',function(){
      dtype=r.value;
      form.classList.remove('mpt-bp','mpt-bf');
      if(dtype==='parenting') form.classList.add('mpt-bp');
      if(dtype==='property') form.classList.add('mpt-bf');
      var sub=document.getElementById('mptS3sub');
      if(sub) sub.textContent=dtype==='parenting'
        ?'Tell us about the children and whether Family Dispute Resolution has been attempted.'
        :'Tell us about the separation and the family home.';
    });
  });

  /* WA note */
  document.getElementById('mpt_state').addEventListener('change',function(){
    var el=document.getElementById('mptWa');
    if(el) el.style.display=this.value==='WA'?'block':'none';
  });

  /* FDR notice */
  document.querySelectorAll('input[name="mpt_fdr"]').forEach(function(r){
    r.addEventListener('change',function(){
      var el=document.getElementById('mptFdrNote');
      if(el) el.style.display=(r.checked&&(r.value==='no'||r.value==='unsure'))?'block':'none';
    });
  });

  /* Court orders warning */
  var orderVals=['Interim parenting orders','Final parenting orders','Consent orders','Other court orders'];
  document.querySelectorAll('input[name="mpt_current[]"]').forEach(function(cb){
    cb.addEventListener('change',function(){
      var warn=document.getElementById('mptOrdersWarn');
      if(!warn) return;
      var has=orderVals.some(function(v){
        var el=document.querySelector('input[name="mpt_current[]"][value="'+v+'"]');
        return el&&el.checked;
      });
      warn.style.display=has?'block':'none';
    });
  });

  function render(){
    document.querySelectorAll('.mpt-section').forEach(function(s){
      s.classList.toggle('active',parseInt(s.dataset.s)===cur);
    });
    LABELS.forEach(function(_,i){
      var n=i+1;
      var s=document.getElementById('mptS'+n);
      s.classList.remove('active','done');
      if(n<cur) s.classList.add('done');
      if(n===cur) s.classList.add('active');
      if(n>1){var c=document.getElementById('mptC'+n);if(c)c.classList.toggle('done',n<=cur);}
    });
    var p=Math.round((cur-1)/total*100);
    bar.style.width=p+'%';
    slbl.textContent='Step '+cur+' of '+total;
    pctEl.textContent=p+'% complete';
    back.style.visibility=cur===1?'hidden':'visible';
    next.style.display=cur===total?'none':'';
    if(cur===total) buildReview();
    var card=form.closest('.mpt-card');
    if(card) window.scrollTo({top:card.getBoundingClientRect().top+window.scrollY-80,behavior:'smooth'});
  }

  function buildReview(){
    var fd=new FormData(form);
    var g=function(n){return(fd.get(n)||'').toString().trim()||null;};
    var ga=function(n){var v=fd.getAll(n);return v.length?v:null;};
    var html='';
    function row(l,v){if(v)html+='<div class="mpt-rv"><div class="mpt-rv-l">'+l+'</div><div class="mpt-rv-v">'+v+'</div></div>';}
    var stateMap={ACT:'Australian Capital Territory',NSW:'New South Wales',NT:'Northern Territory',QLD:'Queensland',SA:'South Australia',TAS:'Tasmania',VIC:'Victoria',WA:'Western Australia',Multiple:'More than one state/territory',Unsure:'Not specified'};
    row('State/Territory',stateMap[g('mpt_state')]||g('mpt_state'));
    row('Dispute type',dtype==='parenting'?'Family and Parenting':dtype==='property'?'Separation and Property':null);
    row('Overview',g('mpt_brief'));
    if(dtype==='parenting'){
      var fdrMap={yes:'Participated in FDR',no:'Not yet attended FDR',arranged:'FDR has been arranged',cert60i:'Has a section 60I certificate',cert66h:'Has a section 66H certificate (WA)',exempt:'An exemption may apply',unsure:'Not specified'};
      row('FDR status',fdrMap[g('mpt_fdr')]||null);
      row('Children',g('mpt_children'));
      row('Other parent',g('mpt_other_p'));
    }
    if(dtype==='property'){
      row('Separation',g('mpt_sep_when'));
      row('Other party',g('mpt_other_f'));
      var homeMap={jointly_owned:'Jointly owned — not yet resolved',one_living:'One party living in it',sold:'Has been sold',renting:'No family home (renting)',na:'Not applicable'};
      row('Family home',homeMap[g('mpt_home')]||null);
    }
    var issues=ga('mpt_issues[]');
    var issueStr=issues?issues.join(', '):null;
    if(g('mpt_issues_other')) issueStr=(issueStr?issueStr+', ':'')+g('mpt_issues_other');
    row('Issues selected',issueStr);
    var cur2=ga('mpt_current[]');
    row('Current arrangements',cur2?cur2.join(', '):null);
    row('Already agreed',g('mpt_agreed'));
    var pri=ga('mpt_pri[]');
    var priStr=pri?pri.join(', '):null;
    if(g('mpt_pri_other')) priStr=(priStr?priStr+'; ':'')+g('mpt_pri_other');
    row('Priorities',priStr);
    row('Questions to raise',g('mpt_questions'));
    row('Notes',g('mpt_notes'));
    if(g('mpt_date')){
      var dp=g('mpt_date').split('-');
      var months=['January','February','March','April','May','June','July','August','September','October','November','December'];
      var auD=dp.length===3?(parseInt(dp[2])+' '+months[parseInt(dp[1])-1]+' '+dp[0]):g('mpt_date');
      row('Upcoming date',auD+(g('mpt_date_desc')?' — '+g('mpt_date_desc'):''));
    }
    document.getElementById('mptReview').innerHTML=html||'<p style="color:var(--ink-soft);font-family:var(--sans);font-size:.9rem">No details entered yet.</p>';
  }

  back.addEventListener('click',function(){if(cur>1){cur--;render();}});
  next.addEventListener('click',function(){if(cur<total){cur++;render();}});

  /* PDF download */
  dl.addEventListener('click',function(){
    if(!window.jspdf||!window.jspdf.jsPDF){alert('PDF library not loaded. Please check your internet connection and try again.');return;}
    var jsPDF=window.jspdf.jsPDF;
    var doc=new jsPDF();
    var fd=new FormData(form);
    var g=function(n){return(fd.get(n)||'').toString().trim();};
    var ga=function(n){return fd.getAll(n);};
    var M=20,W=170,y=22;
    var MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];
    var now=new Date();
    var auNow=now.getDate()+' '+MONTHS[now.getMonth()]+' '+now.getFullYear();
    var stateLabels={ACT:'Australian Capital Territory',NSW:'New South Wales',NT:'Northern Territory',QLD:'Queensland',SA:'South Australia',TAS:'Tasmania',VIC:'Victoria',WA:'Western Australia',Multiple:'More than one state/territory',Unsure:'Not specified'};
    var dispType=dtype==='parenting'?'Family and Parenting':dtype==='property'?'Separation and Property':'Not specified';
    var stateName=stateLabels[g('mpt_state')]||g('mpt_state')||'Not specified';

    var chk=function(h){if(y+h>275){doc.addPage();y=22;}};
    var ln=function(txt,sz,bold,gap,ind){
      doc.setFont('helvetica',bold?'bold':'normal');doc.setFontSize(sz);
      var x=M+(ind||0),w=W-(ind||0);
      var ls=doc.splitTextToSize(txt,w);
      chk(ls.length*(sz*0.44)+2);
      doc.text(ls,x,y);y+=ls.length*(sz*0.44)+(gap!==undefined?gap:4);
    };
    var rule=function(){chk(8);doc.setDrawColor(200,200,200);doc.setLineWidth(0.25);doc.line(M,y,190,y);doc.setDrawColor(0);doc.setLineWidth(0.2);y+=8;};
    var sec=function(title){rule();ln(title,11,true,6);};
    var bullet=function(txt){ln('•  '+txt,10,false,3,4);};

    /* Header */
    doc.setFont('helvetica','bold');doc.setFontSize(17);
    doc.text('MY MEDIATION PREPARATION SUMMARY',105,y,{align:'center'});y+=9;
    doc.setFont('helvetica','normal');doc.setFontSize(9);
    doc.text('Prepared using the Mediations Australia Australian Mediation Preparation Tool',105,y,{align:'center'});y+=12;
    doc.setFontSize(10);
    doc.text('Prepared: '+auNow,M,y);y+=6;
    doc.text('State/Territory: '+stateName,M,y);y+=6;
    doc.text('Dispute type: '+dispType,M,y);y+=10;

    /* Disclaimer */
    rule();
    ln('ABOUT THIS DOCUMENT',10,true,4);
    doc.setFont('helvetica','italic');doc.setFontSize(8.5);
    var disc=doc.splitTextToSize('This document was generated from information entered using the Mediations Australia Australian Mediation Preparation Tool. It is a personal preparation document only and is not legal advice, a legal opinion, an assessment of the merits of the dispute, or a recommendation about settlement. Laws and dispute-resolution procedures differ across Australia and depend on individual circumstances. Consider obtaining independent Australian legal advice if you need advice about your rights, obligations, deadlines or a proposed agreement. Completing this tool does not constitute participation in Family Dispute Resolution and does not result in the issue of a section 60I or section 66H certificate.',W);
    chk(disc.length*4+4);doc.text(disc,M,y);y+=disc.length*4+8;

    /* 1. Overview */
    sec('1. OVERVIEW');
    if(g('mpt_name')) ln('Prepared by: '+g('mpt_name'),10,false,4);
    ln('State/Territory: '+stateName,10,false,4);
    ln('Dispute type: '+dispType,10,false,4);
    if(g('mpt_brief')) ln('Summary: '+g('mpt_brief'),10,false,6);

    if(dtype==='parenting'){
      sec('2. FAMILY DISPUTE RESOLUTION');
      var fdrL={yes:'Participated in FDR',no:'Not yet attended FDR',arranged:'FDR has been arranged',cert60i:'Has a section 60I certificate',cert66h:'Has a section 66H certificate (WA)',exempt:'An exemption may apply',unsure:'Not specified'};
      ln('FDR status: '+(fdrL[g('mpt_fdr')]||'Not specified'),10,false,4);
      if(g('mpt_children')) ln('Children: '+g('mpt_children'),10,false,4);
      if(g('mpt_other_p')) ln('Other parent: '+g('mpt_other_p'),10,false,4);
      if(g('mpt_state')==='WA'){
        chk(16);
        doc.setFont('helvetica','italic');doc.setFontSize(8.5);
        var waNote=doc.splitTextToSize('Note - Western Australia: Family-law processes in Western Australia differ from other states. A certificate under section 66H of the Family Court Act 1997 (WA) may be relevant. Consider obtaining advice specific to Western Australia.',W);
        doc.text(waNote,M,y);y+=waNote.length*4+6;
      }
    }

    if(dtype==='property'){
      sec('2. SEPARATION AND PROPERTY');
      if(g('mpt_sep_when')) ln('Separation: '+g('mpt_sep_when'),10,false,4);
      if(g('mpt_other_f')) ln('Other party: '+g('mpt_other_f'),10,false,4);
      var homeL={jointly_owned:'Jointly owned - not yet resolved',one_living:'One party living in it',sold:'Has been sold',renting:'No family home (renting)',na:'Not applicable'};
      if(g('mpt_home')) ln('Family home: '+(homeL[g('mpt_home')]||g('mpt_home')),10,false,4);
    }

    var issues=ga('mpt_issues[]');
    if(issues.length||g('mpt_issues_other')){
      sec('3. ISSUES FOR DISCUSSION');
      issues.forEach(function(v){bullet(v);});
      if(g('mpt_issues_other')) bullet(g('mpt_issues_other'));
    }

    var curr=ga('mpt_current[]');
    if(curr.length||g('mpt_current_detail')){
      sec('4. CURRENT ARRANGEMENTS');
      curr.forEach(function(v){bullet(v);});
      if(g('mpt_current_detail')) ln(g('mpt_current_detail'),10,false,6);
    }

    if(g('mpt_agreed')){
      sec('5. AREAS OF AGREEMENT');
      ln(g('mpt_agreed'),10,false,6);
    }

    var pri=ga('mpt_pri[]');
    if(pri.length||g('mpt_pri_other')){
      sec('6. MY PRIORITIES');
      pri.forEach(function(v){bullet(v);});
      if(g('mpt_pri_other')) ln(g('mpt_pri_other'),10,false,6);
    }

    if(g('mpt_questions')){
      sec('7. QUESTIONS TO RAISE');
      ln(g('mpt_questions'),10,false,6);
    }

    if(g('mpt_notes')||g('mpt_date')){
      sec('8. ADDITIONAL NOTES');
      if(g('mpt_notes')) ln(g('mpt_notes'),10,false,6);
      if(g('mpt_date')){
        var dp=g('mpt_date').split('-');
        var auD=dp.length===3?(parseInt(dp[2])+' '+MONTHS[parseInt(dp[1])-1]+' '+dp[0]):g('mpt_date');
        ln('Upcoming date: '+auD+(g('mpt_date_desc')?' - '+g('mpt_date_desc'):''),10,false,4);
        chk(12);
        doc.setFont('helvetica','italic');doc.setFontSize(8.5);
        var warn=doc.splitTextToSize('Using this tool does not pause, extend or satisfy any court, tribunal, statutory or contractual deadline. If you are concerned about a deadline, obtain information or advice promptly.',W);
        doc.text(warn,M,y);y+=warn.length*4+6;
      }
    }

    /* Footer on every page */
    var pages=doc.getNumberOfPages();
    for(var p=1;p<=pages;p++){
      doc.setPage(p);
      doc.setFont('helvetica','normal');doc.setFontSize(7.5);
      doc.text('General information only - not legal advice. Mediations Australia - www.mediationsaustralia.com.au',105,289,{align:'center'});
    }

    doc.save('mediation-preparation-summary.pdf');
  });

  render();
})();
</script>
"""

# ── FAQ ──────────────────────────────────────────────────────────────────────
qa = [
    ("What is a Mediation Preparation Summary?",
     "A Mediation Preparation Summary is a personal document that helps you organise your thinking before a mediation session. It identifies the issues you want to discuss, your current situation, what has already been agreed, and your priorities. It is for your own use and is not a legal document."),
    ("Is this tool confidential?",
     "Nothing you enter is stored on Mediations Australia's servers. Your answers exist only in your browser session and in the PDF you download. We treat the privacy of your information seriously."),
    ("What is the difference between mediation and Family Dispute Resolution?",
     "Mediation is a process in which an independent mediator helps participants identify issues, discuss concerns, explore options and attempt to reach agreement. Family Dispute Resolution (FDR) is a specific form of dispute resolution for family law matters conducted by a registered Family Dispute Resolution Practitioner. Completing this preparation tool is not FDR and does not result in the issue of a section 60I or section 66H certificate."),
    ("Do I need a lawyer before using this tool?",
     "No. This tool is designed to help you prepare independently. However, if legal rights, obligations, deadlines or proposed agreements are involved, we recommend considering independent legal advice. This tool provides general information only and does not give legal advice."),
    ("What happens after I complete mediation?",
     "If the parties reach agreement, the mediator may help record it. How an agreement is documented, and whether it is legally binding, depends on the type of dispute and the circumstances. For parenting matters, options include a parenting plan or consent orders. For property matters, options may include a financial agreement or consent orders. Seek legal advice about the appropriate form of any agreement."),
    ("Can I use this tool if I am in Western Australia?",
     "Yes. The tool recognises that family-law processes in Western Australia differ from those in other states and territories. When you select Western Australia, the tool surfaces information relevant to the Family Court of Western Australia and the section 66H certificate under the Family Court Act 1997 (WA).")
]

# ── Article body ──────────────────────────────────────────────────────────────
BODY = """
<h2 id="why-prepare">Why preparation matters in mediation</h2>
<p>Mediation is most effective when both parties arrive with a clear sense of the issues they want to address, the outcome they are hoping for, and the areas where agreement may already exist. Arriving unprepared can mean mediation sessions run over time, revisit territory unnecessarily, or stall on issues that could have been identified in advance.</p>
<p>A preparation session with a mediator can help &mdash; but having your own thinking organised beforehand means you can use that time productively. Common preparation tasks include identifying the issues in dispute, reviewing any existing arrangements or orders, noting what has already been agreed, and thinking through your priorities. This tool guides you through each of these steps and produces a summary you can keep, bring to your session, or share with your mediator in advance.</p>

<h2 id="what-is-mediation">What mediation is &mdash; and what it is not</h2>
<p>Mediation is a process in which an independent mediator helps participants identify the issues in dispute, discuss their concerns, explore options, and attempt to reach their own agreement. The mediator does not decide the outcome and does not take sides. The participants decide whether to agree and on what terms.</p>
<p>Mediation is different from arbitration or a court hearing, where a decision is imposed on the parties. It is also different from negotiations conducted entirely through lawyers. In mediation, participants speak for themselves, which is why preparation matters. The more clearly you can articulate what you want to discuss, what matters most to you, and where you might have flexibility, the more productively the session can proceed.</p>

<h2 id="fdr">Family Dispute Resolution and parenting matters</h2>
<p>For parenting disputes in Australia, it is important to understand the difference between ordinary mediation and Family Dispute Resolution (FDR). FDR is a specific process under the <em>Family Law Act 1975</em> (Cth) conducted by a registered Family Dispute Resolution Practitioner. In many parenting matters, parties are required to make a genuine effort to resolve their dispute through FDR before applying to a family law court for parenting orders, unless an exception applies.</p>
<p>A registered FDR Practitioner may issue a certificate under section 60I of the Act &mdash; or, in Western Australia, section 66H of the <em>Family Court Act 1997</em> (WA) &mdash; in circumstances provided by the legislation. Completing this preparation tool is not FDR, does not satisfy any FDR requirement, and does not result in the issue of any certificate. If you are unsure whether you need to participate in FDR, consider obtaining legal advice.</p>

<h2 id="property-disputes">Preparing for property and financial disputes</h2>
<p>Property and financial disputes following separation can involve a wide range of assets and liabilities &mdash; the family home, investment properties, superannuation, bank accounts, vehicles, businesses, trusts, and debts. Preparing effectively means identifying all of the issues in scope, understanding what exists, and thinking through your priorities.</p>
<p>This tool guides you through the key property and financial issues that commonly arise following separation. However, it does not provide legal or financial advice, and it does not constitute financial disclosure for the purposes of any legal process. How a financial agreement is documented, and whether it is legally enforceable, will depend on the circumstances. Consider obtaining independent legal advice about the appropriate form of any agreement reached.</p>

<h2 id="legal-advice">When to seek legal advice</h2>
<p>This tool is general information only. Consider obtaining independent Australian legal advice if any of the following apply to your situation: there are existing court orders; a proposed agreement involves significant financial interests or property; you are uncertain about your rights or obligations; there are safety concerns of any kind; or a court, tribunal or statutory deadline may be relevant. A family lawyer can advise you about the appropriate form for documenting any agreement reached in mediation.</p>
<p>If family violence or safety concerns are present, mediation may not be appropriate. Mediators are not able to provide a safe environment for all disputes. In that case, seek advice from a lawyer, contact 1800RESPECT (1800&nbsp;737&nbsp;732), or contact the police if you or your children are at risk.</p>
"""

# ── Page build ────────────────────────────────────────────────────────────────
def build():
    slug = 'prepare-for-mediation'
    title = 'Free Mediation Preparation Tool | Mediations Australia'
    desc  = 'Prepare for mediation in Australia with our free guided tool. Identify your issues, clarify priorities and download a personal Mediation Preparation Summary.'
    h1    = 'Free Australian Mediation <em>Preparation Tool</em>'
    lede  = ('Organise your thinking, identify the issues you want to discuss, and download '
             'a personal Mediation Preparation Summary &mdash; tailored for Australian '
             'family and property disputes.')
    ans   = ('Preparing for mediation means clarifying the issues in dispute, understanding '
             'your current situation, and thinking through your priorities and options. This '
             'free tool guides you through each step and creates a downloadable PDF summary.')
    crumb = 'Mediation Preparation Tool'
    cta_h = 'Ready to speak with a mediator?'
    cta_p = ('Our accredited mediators work across Australia. Book a free consultation '
             'to discuss your situation.')

    schema = [
        org_schema(),
        breadcrumb_schema([("Home",""),("Resources","preparing-for-mediation"),(crumb, slug)]),
        article_schema(crumb, desc),
        faq_schema(qa),
    ]

    d = head(title, desc, slug, extra_schema=schema) + nav()
    d += f"""<main id="main">
{crumb_html([("Home",""),("Resources",None),(crumb,None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Free resource</span>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
<div class="phero-cta">
  <a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">&rarr;</span></a>
  <a href="tel:{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
</div>
</div></section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {ans}</p></div></div>"""

    d += TOOL_HTML

    d += f'<article class="body"><div class="wrap-narrow reveal">{BODY}</div></article>'
    d += faq_html(qa, heading=f"{crumb} — Frequently Asked Questions")
    d += cta_band(cta_h, cta_p)
    d += "</main>" + page_end()

    p = os.path.join(OUT, slug)
    os.makedirs(p, exist_ok=True)
    with open(os.path.join(p, "index.html"), "w") as fh:
        fh.write(d)

    words = len(re.sub(r'<[^>]+>', ' ', d).split())
    return slug, words


if __name__ == '__main__':
    slug, words = build()
    print(f'Built: {slug}/  ({words:,} words)')
