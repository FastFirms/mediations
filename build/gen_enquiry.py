#!/usr/bin/env python3
"""
build/gen_enquiry.py

Generates /book-a-consultation/index.html.

Feature flag:
  ENQUIRY_FORM_V2=1  → guided multi-step form + quick enquiry component
  ENQUIRY_FORM_V2=0  → original Formspree form (fallback, preserves SLA-safe text)

Never run gen_booking.py — it is out of sync with the live page.

Usage (from repo root or build/):
  python3 build/gen_enquiry.py
  ENQUIRY_FORM_V2=1 python3 build/gen_enquiry.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import head, nav, page_end, BOOK_URL, PHONE, PHONE_HREF, DOMAIN

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2  = os.environ.get("ENQUIRY_FORM_V2", "0").strip() == "1"

SLUG  = "book-a-consultation"
TITLE = "Book a Mediation Consultation | Mediations Australia"
DESC  = "Tell us about your dispute and we'll give you an honest view of whether mediation can help. No obligation. In person or online across Australia."
CANON = f"https://{DOMAIN}/book-a-consultation/"

SCHEMA = """{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LegalService",
      "@id": "https://mediationsaustralia.com.au/#organization",
      "name": "Mediations Australia",
      "description": "Nationally accredited mediators resolving family, business, workplace, property and estate disputes across Australia without court.",
      "url": "https://mediationsaustralia.com.au/",
      "telephone": "(02) 7227 7373",
      "areaServed": "AU",
      "priceRange": "Fixed-fee consultations",
      "address": [
        {"@type":"PostalAddress","addressLocality":"Sydney","streetAddress":"Suite 508, 41/464\\u2013480 Kent St, NSW 2000","addressCountry":"AU"},
        {"@type":"PostalAddress","addressLocality":"Melbourne","streetAddress":"Level 23, 727 Collins St, VIC 3008","addressCountry":"AU"},
        {"@type":"PostalAddress","addressLocality":"Brisbane","streetAddress":"Suite 507, 198 Adelaide St, QLD 4000","addressCountry":"AU"},
        {"@type":"PostalAddress","addressLocality":"Perth","streetAddress":"Level 25, 108 St Georges Tce, WA 6000","addressCountry":"AU"}
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type":"ListItem","position":1,"name":"Home","item":"https://mediationsaustralia.com.au/"},
        {"@type":"ListItem","position":2,"name":"Book a Consultation","item":"https://mediationsaustralia.com.au/book-a-consultation/"}
      ]
    }
  ]
}"""

ASIDE_HTML = """<aside>
  <div style="background:var(--sage-deep);color:var(--cream);border-radius:var(--r);padding:30px">
    <h2 style="color:var(--cream);font-size:1.4rem;margin-bottom:14px">Prefer to talk now?</h2>
    <p style="color:rgba(251,248,242,.85);margin-bottom:20px;font-size:.98rem">Call us directly and speak with our team about your situation.</p>
    <a href="{phone_href}" class="btn btn-primary" style="justify-content:center;width:100%">Call {phone}</a>
    <div style="margin-top:26px;padding-top:22px;border-top:1px solid rgba(251,248,242,.18);display:flex;flex-direction:column;gap:14px;font-size:.95rem">
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Fixed-fee, no surprises</div>
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>In person or online</div>
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Nationally accredited mediators</div>
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>90% resolved without court</div>
    </div>
  </div>
</aside>""".format(phone_href=PHONE_HREF, phone=PHONE)


def fallback_form_html():
    """Original Formspree form — SLA text updated to not promise a specific timeframe."""
    return """<form id="bookform" action="https://formspree.io/f/xwvgjnve" method="POST" novalidate style="background:var(--cream);border:1px solid var(--line);border-radius:var(--r);padding:36px;display:flex;flex-direction:column;gap:16px">
  <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;opacity:0" aria-hidden="true">
  <input type="hidden" name="_subject" value="New consultation request — Mediations Australia">
  <div class="form-row"><label for="b-name">Name</label><input id="b-name" name="name" type="text" required autocomplete="name" placeholder="Your full name" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)"></div>
  <div class="form-row"><label for="b-phone">Phone</label><input id="b-phone" name="phone" type="tel" required autocomplete="tel" placeholder="0400 000 000" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)"></div>
  <div class="form-row"><label for="b-email">Email</label><input id="b-email" name="email" type="email" required autocomplete="email" placeholder="you@example.com" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)"></div>
  <div class="form-row"><label for="b-matter">Type of Mediation</label><select id="b-matter" name="matter" required style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)"><option value="" disabled selected>Select&hellip;</option><option value="Property Settlement">Property Settlement</option><option value="Parenting">Parenting</option><option value="Property &amp; Parenting">Property &amp; Parenting</option><option value="Other Family Law">Other Family Law</option><option value="Workplace">Workplace</option><option value="Estate">Estate</option><option value="Something else">Something else</option></select></div>
  <div class="form-row"><label for="b-location">Your Location</label><input id="b-location" name="location" type="text" placeholder="e.g. Sydney, Melbourne, or Online" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)"></div>
  <div class="form-row"><label for="b-message">Brief Explanation</label><textarea id="b-message" name="message" rows="4" placeholder="A few sentences about your situation&hellip;" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand);resize:vertical"></textarea></div>
  <button type="submit" class="btn btn-primary" style="justify-content:center;font-size:1.05rem;padding:15px 20px">Book a Consultation <span class="arr">&rarr;</span></button>
  <p id="formnote" role="status" aria-live="polite" style="font-size:.88rem;color:var(--ink-soft);margin:0">We'll be in touch as soon as we can. Your details are kept private and confidential.</p>
</form>
<script>
const f=document.getElementById('bookform');
if(f){{f.addEventListener('submit',async function(e){{
  e.preventDefault();
  const note=document.getElementById('formnote');
  const btn=f.querySelector('button[type=submit]');
  const req=['b-name','b-email','b-phone'];let ok=true;
  req.forEach(id=>{{const el=document.getElementById(id);
    if(!el||!el.value.trim()){{if(el)el.style.borderColor='var(--terra)';ok=false;}}
    else{{el.style.borderColor='var(--line)';}}}});
  if(!ok){{note.textContent='Please complete the required fields so we can get back to you.';note.style.color='var(--terra-deep)';return;}}
  if(f.querySelector('[name=_gotcha]').value){{
    note.textContent='Thank you — your request has been received.';
    note.style.color='var(--sage-deep)';btn.textContent='Request sent ✓';btn.disabled=true;return;
  }}
  btn.disabled=true;btn.textContent='Sending…';
  note.textContent='Sending your request…';note.style.color='var(--ink-soft)';
  try{{
    const res=await fetch(f.action,{{method:'POST',body:new FormData(f),headers:{{Accept:'application/json'}}}});
    if(res.ok){{window.location.href='/thank-you/';}}
    else{{
      const data=await res.json().catch(()=>({{}}));
      const msg=(data.errors&&data.errors.map(x=>x.message).join(', '))||'Sorry, something went wrong. Please try again, or call us on {phone}.';
      note.textContent=msg;note.style.color='var(--terra-deep)';btn.disabled=false;btn.textContent='Book a Consultation';
    }}
  }}catch(err){{
    note.textContent='Network error — please try again, or call us on {phone}.';
    note.style.color='var(--terra-deep)';btn.disabled=false;btn.textContent='Book a Consultation';
  }}
}})}}</script>""".format(phone=PHONE)


def guided_form_html():
    """Guided multi-step enquiry form (ENQUIRY_FORM_V2=1)."""
    return """<style>[hidden]{display:none!important}</style>
<div id="enq-app" style="background:var(--cream);border:1px solid var(--line);border-radius:var(--r);padding:clamp(24px,3vw,36px)">

  <!-- Quick Enquiry (always visible fallback) -->
  <div id="enq-quick" style="border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin-bottom:20px;background:var(--sand)">
    <p style="font-size:.85rem;font-weight:600;color:var(--sage-deep);margin:0 0 12px;text-transform:uppercase;letter-spacing:.04em">Quick enquiry</p>
    <div id="enq-quick-form" style="display:flex;flex-direction:column;gap:12px">
      <input id="qk-name" type="text" placeholder="Your name" autocomplete="name" required style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff">
      <input id="qk-contact" type="email" placeholder="Email or phone" autocomplete="email" required style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff">
      <textarea id="qk-msg" rows="2" placeholder="Briefly, what's this about? (optional)" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff;resize:vertical"></textarea>
      <label style="display:flex;gap:8px;align-items:flex-start;font-size:.82rem;color:var(--ink-soft);cursor:pointer">
        <input id="qk-consent" type="checkbox" style="margin-top:2px;flex-shrink:0">
        I agree to the <a href="/privacy-policy/" target="_blank" style="color:var(--sage-deep)">privacy policy</a>
      </label>
      <input type="text" id="qk-hp" style="position:absolute;left:-9999px;opacity:0" tabindex="-1" autocomplete="off" aria-hidden="true">
      <p id="qk-note" role="status" aria-live="polite" style="font-size:.82rem;color:var(--ink-soft);margin:0;display:none"></p>
      <button id="qk-submit" class="btn btn-primary" style="justify-content:center;font-size:.95rem">Send quick enquiry <span class="arr">&rarr;</span></button>
    </div>
    <div id="qk-confirm" style="display:none;text-align:center;padding:12px 0">
      <p style="color:var(--sage-deep);font-weight:600;margin:0 0 4px">Enquiry received</p>
      <p id="qk-ref" style="font-size:.82rem;color:var(--ink-soft);margin:0"></p>
    </div>
    <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--line)">
      <button id="enq-guided-btn" class="btn" style="width:100%;justify-content:center;font-size:.88rem;background:none;border:1px solid var(--sage-deep);color:var(--sage-deep);padding:10px 16px">
        Find the right mediation pathway &rarr;
      </button>
    </div>
  </div>

  <!-- Guided multi-step form -->
  <div id="enq-guided" style="display:none">
    <div id="enq-prog-wrap" aria-hidden="true" style="margin-bottom:18px">
      <div style="height:4px;background:var(--line);border-radius:2px">
        <div id="enq-prog" style="height:100%;background:var(--sage);border-radius:2px;transition:width .3s ease;width:8%"></div>
      </div>
      <p id="enq-step-label" style="font-size:.78rem;color:var(--ink-soft);margin:6px 0 0;text-align:right"></p>
    </div>

    <!-- Safety notice (always present but hidden, shown when safety step reached) -->
    <div id="enq-safety-notice" style="display:none;background:#fff3cd;border:1px solid #ffc107;border-radius:8px;padding:12px 14px;margin-bottom:14px;font-size:.85rem">
      <strong>If you are in immediate danger in Australia, call 000.</strong><br>
      For family violence support: <strong>1800RESPECT — 1800 737 732</strong>
    </div>

    <div id="enq-steps"></div>

    <div id="enq-nav" style="display:flex;gap:10px;margin-top:18px">
      <button id="enq-back" class="btn" style="background:none;border:1px solid var(--line);color:var(--ink);flex:0 0 auto;padding:11px 18px" hidden>&larr; Back</button>
      <button id="enq-next" class="btn btn-primary" style="flex:1;justify-content:center" hidden>Next &rarr;</button>
      <button id="enq-submit" class="btn btn-primary" style="flex:1;justify-content:center" hidden>Submit enquiry &rarr;</button>
    </div>
    <div id="enq-error" role="alert" style="display:none;color:var(--terra-deep);font-size:.85rem;margin-top:8px"></div>

    <button id="enq-cancel" style="display:block;width:100%;background:none;border:none;color:var(--ink-soft);font-size:.8rem;margin-top:12px;cursor:pointer;padding:8px">
      &larr; Use quick enquiry instead
    </button>
  </div>

  <!-- Confirmation screen -->
  <div id="enq-success" style="display:none;text-align:center;padding:20px 10px">
    <div style="font-size:2.5rem;margin-bottom:12px">&#10003;</div>
    <h2 style="font-size:1.3rem;margin-bottom:8px">Enquiry received</h2>
    <p id="enq-success-ref" style="font-size:.85rem;color:var(--ink-soft);margin-bottom:14px"></p>
    <p style="font-size:.95rem;margin-bottom:20px">A member of our team will review your enquiry and be in touch.</p>
    <a href="/" class="btn btn-primary" style="justify-content:center">Return home</a>
  </div>
</div>

<script>
(function(){
'use strict';

// ── State ────────────────────────────────────────────────────────────────────
var _state = {
  form_variant: 'guided',
  submission_id: null,
  step: 0,
  answers: {},
  branch_answers: {}
};

// ── Category pre-fill from homepage quiz (sessionStorage, cleared after read) ─
var _prefill = null;
try {
  var raw = sessionStorage.getItem('ma_quiz_category');
  if (raw) { _prefill = raw; sessionStorage.removeItem('ma_quiz_category'); }
} catch(e) {}

var CAT_MAP = {
  property:'family_property', parenting:'family_parenting', both:'family_combined',
  workplace:'workplace_employment', business:'commercial_business',
  estate:'estate_inheritance', other:'other_unsure'
};

// ── Step definitions ─────────────────────────────────────────────────────────
var STEPS = [
  // Step 0: Dispute type
  {
    id:'category', label:'Step 1 — What needs to be resolved?', prog:'14%',
    render: function() {
      var opts = [
        {v:'family_parenting',  l:'Parenting arrangements or children'},
        {v:'family_property',   l:'Property or financial settlement'},
        {v:'family_combined',   l:'Both parenting and property'},
        {v:'workplace_employment', l:'Workplace or employment'},
        {v:'commercial_business',  l:'Business or commercial dispute'},
        {v:'estate_inheritance',   l:'Estate or inheritance'},
        {v:'elder_family',         l:'Elder care or family decision-making'},
        {v:'neighbour_property',   l:'Neighbour, boundary or strata'},
        {v:'construction_real_estate', l:'Construction or real estate'},
        {v:'other_unsure',         l:'Not sure / something else'},
      ];
      return _radioStep('matter_category', opts, _state.answers.matter_category);
    },
    validate: function() { return !!_state.answers.matter_category; },
    next: function() { return 1; }
  },
  // Step 1: Stage
  {
    id:'stage', label:'Step 2 — Where are things at?', prog:'28%',
    render: function() {
      var opts = [
        {v:'exploring',                  l:'Just exploring options'},
        {v:'discussing',                 l:'Trying to discuss but stuck'},
        {v:'ready_to_arrange',           l:'Ready to arrange mediation'},
        {v:'lawyers_involved',           l:'Lawyers are involved'},
        {v:'proceedings_started',        l:'Court proceedings have started'},
        {v:'court_date',                 l:'There is a court date'},
        {v:'agreement_needs_formalisation', l:'We have an agreement that needs formalising'},
        {v:'unsure',                     l:'Not sure'},
      ];
      return _radioStep('stage', opts, _state.answers.stage);
    },
    validate: function() { return !!_state.answers.stage; },
    next: function() { return 2; }
  },
  // Step 2: Other-party awareness
  {
    id:'other_party', label:'Step 3 — Does the other party know?', prog:'42%',
    render: function() {
      var opts = [
        {v:'agreed',               l:'Yes, and they are willing'},
        {v:'open_to_discussion',   l:'Yes, and they seem open'},
        {v:'unsure',               l:'Not sure'},
        {v:'not_asked',            l:"I haven't raised it yet"},
        {v:'declined',             l:'They have said no'},
        {v:'not_applicable',       l:'Not applicable'},
        {v:'prefer_not_to_say',    l:'Prefer not to say'},
      ];
      return _radioStep('party_b_status', opts, _state.answers.party_b_status);
    },
    validate: function() { return !!_state.answers.party_b_status; },
    next: function() { return 3; }
  },
  // Step 3: Delivery
  {
    id:'delivery', label:'Step 4 — How would you prefer to attend?', prog:'56%',
    render: function() {
      var cat = _state.answers.matter_category || '';
      var delivOpts = [
        {v:'online',        l:'Online (video)'},
        {v:'face_to_face',  l:'In person'},
        {v:'either',        l:'Either — flexible'},
        {v:'unsure',        l:'Not sure'},
      ];
      var timingOpts = [
        {v:'urgent',        l:'As soon as possible'},
        {v:'within_2_weeks',l:'Within 2 weeks'},
        {v:'within_month',  l:'Within a month'},
        {v:'flexible',      l:'Flexible'},
      ];
      var html = '<p style="font-size:.92rem;font-weight:600;margin:0 0 10px">How would you prefer to attend?</p>'
               + _radioStep('delivery_preference', delivOpts, _state.answers.delivery_preference, true)
               + '<p style="font-size:.92rem;font-weight:600;margin:18px 0 10px">Timing</p>'
               + _radioStep('timing', timingOpts, _state.answers.timing, true);
      if (_state.answers.delivery_preference === 'face_to_face' || _state.answers.delivery_preference === 'either') {
        html += '<p style="font-size:.92rem;font-weight:600;margin:18px 0 10px">Your state (optional)</p>'
              + '<select id="enq-state" style="width:100%;padding:11px 13px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff">'
              + '<option value="">Select state&hellip;</option>'
              + ['NSW','VIC','QLD','WA','SA','TAS','ACT','NT'].map(function(s){return '<option value="'+s+'"'+(s===_state.answers.state?' selected':'')+'>'+s+'</option>';}).join('')
              + '</select>';
      }
      return html;
    },
    validate: function() { return !!_state.answers.delivery_preference && !!_state.answers.timing; },
    onLeave: function() {
      var sel = document.getElementById('enq-state');
      if (sel) _state.answers.state = sel.value || null;
    },
    next: function() { return 4; }
  },
  // Step 4: Fee preference
  {
    id:'fees', label:'Step 5 — Fees and pathway', prog:'70%',
    render: function() {
      var isFamily = ['family_parenting','family_property','family_combined'].indexOf(_state.answers.matter_category) > -1;
      var opts = [
        {v:'standard_private',     l:'I will pay standard fees'},
        {v:'want_fee_information', l:"I'd like to understand what it costs first"},
        {v:'standard_fee_hardship',l:'Standard fee would be a genuine hardship'},
        {v:'need_free_service',    l:'I need a free or community service'},
        {v:'unsure',               l:'Not sure'},
      ];
      var html = _radioStep('fee_preference', opts, _state.answers.fee_preference);
      if (isFamily && _state.answers.fee_preference === 'standard_fee_hardship') {
        html += '<div style="margin-top:14px;padding:12px 14px;background:#f0f8f0;border:1px solid #c8e6c9;border-radius:8px;font-size:.85rem">'
             + '<strong>Access Mediation</strong> provides reduced-fee family mediation for eligible participants. '
             + 'Eligibility and capacity are assessed separately. '
             + '<a href="/access-mediation/" target="_blank" style="color:var(--sage-deep)">Learn more &rarr;</a>'
             + '</div>';
      }
      if (_state.answers.fee_preference === 'need_free_service') {
        html += '<div style="margin-top:14px;padding:12px 14px;background:#fff8e1;border:1px solid #ffe082;border-radius:8px;font-size:.85rem">'
             + 'Community mediation services may be available through Legal Aid or the Family Relationships Centres network. '
             + 'We can point you toward the right service.'
             + '</div>';
      }
      return html;
    },
    validate: function() { return !!_state.answers.fee_preference; },
    next: function() { return 5; }
  },
  // Step 5: Safety and contact guardrail
  {
    id:'safety', label:'Step 6 — Safety and contact', prog:'84%',
    render: function() {
      var safetyOpts = [
        {v:'no',  l:'No'},
        {v:'yes', l:'Yes'},
      ];
      var html = '<div style="margin-bottom:14px;padding:10px 12px;background:#f0f8f0;border-left:3px solid var(--sage);border-radius:0 6px 6px 0;font-size:.85rem">'
               + 'Is there anything about safety, pressure, how we contact you, or an urgent legal deadline that you want a mediator to know before we get in touch?'
               + '</div>'
               + _radioStep('safety_flag', safetyOpts, _state.answers.safety_flag);
      if (_state.answers.safety_flag === 'yes') {
        document.getElementById('enq-safety-notice').style.display = 'block';
        html += '<p style="font-size:.85rem;color:var(--ink-soft);margin-top:12px">You do not need to provide further details. Our team will contact you carefully and in confidence.</p>';
      } else {
        document.getElementById('enq-safety-notice').style.display = 'none';
      }
      html += '<p style="font-size:.92rem;font-weight:600;margin:20px 0 10px">Is email safe for us to use to contact you?</p>'
            + '<div style="display:flex;gap:10px;flex-wrap:wrap">'
            + _inlineRadio('safe_email_pref', 'yes', 'Yes', _state.answers.safe_email_pref)
            + _inlineRadio('safe_email_pref', 'sometimes', 'Sometimes', _state.answers.safe_email_pref)
            + _inlineRadio('safe_email_pref', 'no_phone', 'No — phone only', _state.answers.safe_email_pref)
            + '</div>'
            + '<p style="font-size:.92rem;font-weight:600;margin:14px 0 10px">Is voicemail safe?</p>'
            + '<div style="display:flex;gap:10px;flex-wrap:wrap">'
            + _inlineRadio('safe_voicemail', 'true', 'Yes', _state.answers.safe_voicemail)
            + _inlineRadio('safe_voicemail', 'false', 'No', _state.answers.safe_voicemail)
            + '</div>'
            + '<p style="font-size:.92rem;font-weight:600;margin:14px 0 10px">Best time to call?</p>'
            + '<div style="display:flex;gap:10px;flex-wrap:wrap">'
            + _inlineRadio('preferred_contact_time', 'morning', 'Morning', _state.answers.preferred_contact_time)
            + _inlineRadio('preferred_contact_time', 'afternoon', 'Afternoon', _state.answers.preferred_contact_time)
            + _inlineRadio('preferred_contact_time', 'evening', 'Evening', _state.answers.preferred_contact_time)
            + _inlineRadio('preferred_contact_time', 'flexible', 'Flexible', _state.answers.preferred_contact_time)
            + '</div>';
      return html;
    },
    validate: function() { return !!_state.answers.safety_flag; },
    next: function() { return 6; }
  },
  // Step 6: Contact and consent
  {
    id:'contact', label:'Step 7 — Your details', prog:'100%',
    render: function() {
      return '<div style="display:flex;flex-direction:column;gap:14px">'
           + '<div><label for="enq-name" style="font-size:.9rem;font-weight:600;display:block;margin-bottom:5px">Name <span style="color:var(--terra)">*</span></label>'
           + '<input id="enq-name" type="text" autocomplete="name" placeholder="Your full name" value="'+(escAttr(_state.answers.name))+'" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff"></div>'
           + '<div><label for="enq-email" style="font-size:.9rem;font-weight:600;display:block;margin-bottom:5px">Email</label>'
           + '<input id="enq-email" type="email" autocomplete="email" placeholder="you@example.com" value="'+(escAttr(_state.answers.email))+'" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff"></div>'
           + '<div><label for="enq-phone" style="font-size:.9rem;font-weight:600;display:block;margin-bottom:5px">Phone</label>'
           + '<input id="enq-phone" type="tel" autocomplete="tel" placeholder="0400 000 000" value="'+(escAttr(_state.answers.phone))+'" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff"></div>'
           + '<div><label for="enq-msg" style="font-size:.9rem;font-weight:600;display:block;margin-bottom:5px">Anything else? <span style="font-weight:400;color:var(--ink-soft)">(optional, max 500 characters)</span></label>'
           + '<textarea id="enq-msg" rows="3" maxlength="500" placeholder="A few words about your situation…" style="width:100%;padding:12px 14px;border:1.5px solid var(--line);border-radius:9px;font-family:var(--sans);font-size:.95rem;background:#fff;resize:vertical">'+(esc(_state.answers.message||''))+'</textarea></div>'
           + '<label style="display:flex;gap:10px;align-items:flex-start;font-size:.85rem;cursor:pointer">'
           + '<input id="enq-consent" type="checkbox"'+((_state.answers.privacy_consent)?' checked':'')+' style="margin-top:2px;flex-shrink:0">'
           + 'I have read and agree to the <a href="/privacy-policy/" target="_blank" style="color:var(--sage-deep)">privacy policy</a> <span style="color:var(--terra)">*</span></label>'
           + '<label style="display:flex;gap:10px;align-items:flex-start;font-size:.85rem;cursor:pointer">'
           + '<input id="enq-accuracy" type="checkbox"'+((_state.answers.accuracy_declaration)?' checked':'')+' style="margin-top:2px;flex-shrink:0">'
           + 'The information I have provided is accurate to the best of my knowledge <span style="color:var(--terra)">*</span></label>'
           + '</div>';
    },
    validate: function() {
      var name    = (document.getElementById('enq-name')?.value||'').trim();
      var email   = (document.getElementById('enq-email')?.value||'').trim();
      var phone   = (document.getElementById('enq-phone')?.value||'').trim();
      var consent = document.getElementById('enq-consent')?.checked;
      var accuracy= document.getElementById('enq-accuracy')?.checked;
      if (!name)           { _showError('Please enter your name.'); return false; }
      if (!email && !phone){ _showError('Please enter at least one safe contact — email or phone.'); return false; }
      if (!consent)        { _showError('Please confirm you have read the privacy policy.'); return false; }
      if (!accuracy)       { _showError('Please confirm the information is accurate.'); return false; }
      _state.answers.name              = name;
      _state.answers.email             = email || null;
      _state.answers.phone             = phone || null;
      _state.answers.message           = (document.getElementById('enq-msg')?.value||'').trim().slice(0,500) || null;
      _state.answers.privacy_consent   = true;
      _state.answers.accuracy_declaration = true;
      // safe contact flags
      _state.answers.safe_email = email ? (_state.answers.safe_email_pref !== 'no_phone') : false;
      _state.answers.safe_phone = !!phone;
      return true;
    },
    next: function() { return -1; } // submit
  },
];

// ── HTML helpers ──────────────────────────────────────────────────────────────
function esc(s) {
  return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function escAttr(s) { return esc(s); }

function _radioStep(field, opts, current, inline) {
  var wrap = inline ? 'display:flex;flex-wrap:wrap;gap:8px' : 'display:flex;flex-direction:column;gap:8px';
  return '<div style="'+wrap+'" id="enq-rg-'+field+'">'
    + opts.map(function(o){
        var sel = current === o.v;
        return '<label style="display:flex;align-items:center;gap:9px;border:1.5px solid '+(sel?'var(--sage-deep)':'var(--line)')+';border-radius:9px;padding:10px 14px;cursor:pointer;font-size:.88rem;background:'+(sel?'#f0f8f0':'#fff')+';flex:'+(inline?'0 0 auto':'1 1 auto')+'">'
             + '<input type="radio" name="enq-'+field+'" value="'+o.v+'"'+(sel?' checked':'')+' style="flex-shrink:0">'
             + esc(o.l)
             + '</label>';
      }).join('')
    + '</div>';
}
function _inlineRadio(field, val, label, current) {
  var sel = current === val;
  return '<label style="display:flex;align-items:center;gap:8px;border:1.5px solid '+(sel?'var(--sage-deep)':'var(--line)')+';border-radius:8px;padding:8px 13px;cursor:pointer;font-size:.85rem;background:'+(sel?'#f0f8f0':'#fff')+'">'
       + '<input type="radio" name="enq-'+field+'" value="'+val+'"'+(sel?' checked':'')+' style="flex-shrink:0">'
       + esc(label)+'</label>';
}

// ── Step rendering ────────────────────────────────────────────────────────────
function _renderStep(idx) {
  var step = STEPS[idx];
  var container = document.getElementById('enq-steps');
  var label     = document.getElementById('enq-step-label');
  var prog      = document.getElementById('enq-prog');
  var backBtn   = document.getElementById('enq-back');
  var nextBtn   = document.getElementById('enq-next');
  var submitBtn = document.getElementById('enq-submit');

  container.innerHTML = '<div style="animation:qfade .2s ease both">' + step.render() + '</div>';
  label.textContent = step.label;
  prog.style.width  = step.prog;

  backBtn.hidden   = (idx === 0);
  nextBtn.hidden   = (step.next() < 0);
  submitBtn.hidden = (step.next() >= 0);

  if (step.id === 'safety') {
    document.getElementById('enq-safety-notice').style.display = 'none';
  }

  // Bind radio change events
  var radios = container.querySelectorAll('input[type=radio]');
  radios.forEach(function(r) {
    r.addEventListener('change', function() { _onRadioChange(r); });
  });

  _clearError();
  _state.step = idx;
}

function _onRadioChange(r) {
  var name  = r.name.replace('enq-','');
  var value = r.value;
  if (['matter_category','stage','party_b_status','delivery_preference','timing',
       'fee_preference','safety_flag','safe_email_pref','safe_voicemail','preferred_contact_time'].indexOf(name) > -1) {
    _state.answers[name] = value;
  }
  // Re-render step to update conditional UI (fees note, safety notice, etc.)
  var curStep = STEPS[_state.step];
  var container = document.getElementById('enq-steps');
  container.innerHTML = '<div style="animation:qfade .2s ease both">' + curStep.render() + '</div>';
  var radios2 = container.querySelectorAll('input[type=radio]');
  radios2.forEach(function(r2) {
    r2.addEventListener('change', function() { _onRadioChange(r2); });
  });
}

function _showError(msg) {
  var el = document.getElementById('enq-error');
  el.textContent = msg; el.style.display = 'block';
}
function _clearError() {
  var el = document.getElementById('enq-error');
  el.textContent = ''; el.style.display = 'none';
}

// ── Navigation ────────────────────────────────────────────────────────────────
document.getElementById('enq-next').addEventListener('click', function() {
  _clearError();
  var step = STEPS[_state.step];
  if (step.onLeave) step.onLeave();
  if (!step.validate()) { _showError('Please make a selection to continue.'); return; }
  _renderStep(step.next());
});

document.getElementById('enq-back').addEventListener('click', function() {
  if (_state.step > 0) _renderStep(_state.step - 1);
});

document.getElementById('enq-submit').addEventListener('click', function() {
  _clearError();
  var step = STEPS[_state.step];
  if (!step.validate()) return;
  _submitGuided();
});

document.getElementById('enq-guided-btn').addEventListener('click', function() {
  document.getElementById('enq-quick').style.display = 'none';
  document.getElementById('enq-guided').style.display = 'block';
  // Analytics (non-sensitive)
  try { if(typeof gtag!=='undefined') gtag('event','enquiry_started',{form_variant:'guided'}); } catch(e){}
});

document.getElementById('enq-cancel').addEventListener('click', function() {
  document.getElementById('enq-guided').style.display = 'none';
  document.getElementById('enq-quick').style.display = 'block';
});

// ── Submission (guided) ───────────────────────────────────────────────────────
function _submitGuided() {
  var btn = document.getElementById('enq-submit');
  btn.disabled = true; btn.textContent = 'Sending…';

  var a = _state.answers;
  var payload = {
    form_variant:    'guided',
    submission_id:   _state.submission_id,
    matter_category: a.matter_category,
    stage:           a.stage,
    party_b_status:  a.party_b_status,
    delivery_preference: a.delivery_preference,
    state:           a.state || null,
    timing:          a.timing,
    fee_preference:  a.fee_preference,
    safety_flag:     a.safety_flag,
    safe_email:      !!a.safe_email,
    safe_phone:      !!a.safe_phone,
    safe_voicemail:  a.safe_voicemail === 'true',
    preferred_contact_time: a.preferred_contact_time || null,
    name:            a.name,
    email:           a.email || null,
    phone:           a.phone || null,
    message:         a.message || null,
    privacy_consent: true,
    accuracy_declaration: true,
    branch_answers:  _state.branch_answers,
    attribution_landing:  _safePath(window.performance?.navigation?.type === 0 ? document.referrer : ''),
    attribution_referrer: _safeTrunc(document.referrer, 300),
    attribution_utm_source:   _urlParam('utm_source'),
    attribution_utm_medium:   _urlParam('utm_medium'),
    attribution_utm_campaign: _urlParam('utm_campaign'),
    _hp: ''
  };

  fetch('/api/enquiry', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify(payload)
  })
  .then(function(r){ return r.json(); })
  .then(function(d) {
    if (d.ok) {
      _showSuccess(d.reference, d.operational_queue);
      try { if(typeof gtag!=='undefined') gtag('event','enquiry_submitted',{form_variant:'guided',operational_queue:d.operational_queue}); } catch(e){}
    } else {
      btn.disabled = false; btn.textContent = 'Submit enquiry →';
      _showError(d.error || 'Something went wrong. Please try again or call us on (02) 7227 7373.');
    }
  })
  .catch(function() {
    btn.disabled = false; btn.textContent = 'Submit enquiry →';
    _showError('Network error. Please try again or call us on (02) 7227 7373.');
  });
}

// ── Submission (quick) ────────────────────────────────────────────────────────
document.getElementById('qk-submit').addEventListener('click', function() {
  var name    = (document.getElementById('qk-name')?.value||'').trim();
  var contact = (document.getElementById('qk-contact')?.value||'').trim();
  var msg     = (document.getElementById('qk-msg')?.value||'').trim().slice(0,300);
  var consent = document.getElementById('qk-consent')?.checked;
  var hp      = document.getElementById('qk-hp')?.value||'';
  var note    = document.getElementById('qk-note');
  var btn     = document.getElementById('qk-submit');

  if (hp) { // honeypot
    document.getElementById('qk-form')?.querySelectorAll('input,textarea,button').forEach(function(el){el.style.display='none';});
    document.getElementById('qk-confirm').style.display='block';
    document.getElementById('qk-ref').textContent='Reference: MA-ENQ-BLOCKED';
    return;
  }
  if (!name || !contact) { note.textContent='Please enter your name and email or phone.'; note.style.display='block'; return; }
  if (!consent)           { note.textContent='Please confirm you agree to the privacy policy.'; note.style.display='block'; return; }

  btn.disabled = true; btn.textContent = 'Sending…'; note.style.display='none';

  var isEmail = contact.indexOf('@') > -1;
  fetch('/api/enquiry', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({
      form_variant:'quick',
      name:         name,
      email:        isEmail ? contact : null,
      phone:        isEmail ? null : contact,
      message:      msg || null,
      safe_email:   isEmail,
      safe_phone:   !isEmail,
      privacy_consent: true,
      _hp: ''
    })
  })
  .then(function(r){ return r.json(); })
  .then(function(d) {
    if (d.ok) {
      document.getElementById('qk-confirm').style.display='block';
      document.getElementById('qk-ref').textContent='Reference: '+d.reference;
      document.getElementById('enq-quick-form').style.display='none';
      document.getElementById('enq-guided-btn').style.display='none';
      try { if(typeof gtag!=='undefined') gtag('event','quick_enquiry_submitted'); } catch(e){}
    } else {
      btn.disabled = false; btn.textContent = 'Send quick enquiry →';
      note.textContent = d.error || 'Something went wrong. Please try again.'; note.style.display='block';
    }
  })
  .catch(function() {
    btn.disabled=false; btn.textContent='Send quick enquiry →';
    note.textContent='Network error. Please try again or call us.'; note.style.display='block';
  });
});

// ── Success screen ────────────────────────────────────────────────────────────
function _showSuccess(ref, queue) {
  document.getElementById('enq-app').querySelectorAll('#enq-quick,#enq-guided').forEach(function(el){el.style.display='none';});
  var s = document.getElementById('enq-success');
  s.style.display = 'block';
  document.getElementById('enq-success-ref').textContent = 'Reference: ' + ref;
}

// ── Utility ───────────────────────────────────────────────────────────────────
function _urlParam(name) {
  try { return new URLSearchParams(window.location.search).get(name); } catch(e){ return null; }
}
function _safeTrunc(s, n) { return (typeof s==='string') ? s.slice(0,n) : null; }
function _safePath(s)      { return _safeTrunc(s, 200); }

// ── Init ──────────────────────────────────────────────────────────────────────
// Generate a stable submission_id for idempotency
try { _state.submission_id = crypto.randomUUID(); } catch(e){ _state.submission_id = null; }

// Pre-populate category from homepage quiz if available
if (_prefill && CAT_MAP[_prefill]) {
  _state.answers.matter_category = CAT_MAP[_prefill];
}

// Render first step
_renderStep(0);

})();
</script>"""


def build():
    form_html = guided_form_html() if V2 else fallback_form_html()
    mode_note = "<!-- ENQUIRY_FORM_V2=1 -->" if V2 else "<!-- ENQUIRY_FORM_V2=0 (fallback) -->"

    doc = f"""{head(TITLE, DESC, SLUG, extra_schema=[SCHEMA])}
{nav()}
<main id="main">
<div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span>&rsaquo;</span>Book a Consultation</nav></div>
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Fixed-fee &middot; No obligation &middot; In person or online</span>
<h1>Book a Consultation &mdash; <em>take the first step</em>.</h1>
<p class="lede">Tell us about your dispute and we&rsquo;ll give you an honest view of whether mediation can help, how it works, and what it costs. There&rsquo;s no obligation, and the first conversation costs nothing but a few minutes.</p>
</div></section>
<section class="sec" style="padding-top:20px"><div class="wrap" style="max-width:920px">
{mode_note}
<div class="booking-grid" style="display:grid;grid-template-columns:1.3fr 1fr;gap:48px;align-items:start">
{form_html}
{ASIDE_HTML}
</div>
</div></section>
</main>{page_end()}"""

    path = os.path.join(OUT, SLUG, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Built: {path}  [{'V2 guided' if V2 else 'V1 fallback'}]")


if __name__ == "__main__":
    build()
