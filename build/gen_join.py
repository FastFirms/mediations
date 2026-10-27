#!/usr/bin/env python3
"""Generate /join-our-mediator-network/ — mediator network expression of interest.

Build: python3 build/gen_join.py
Posts directly to a dedicated Formspree form (separate from all client intake).
No payment, fee-split or earnings information may appear on this page.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html,
                       org_schema, breadcrumb_schema)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "join-our-mediator-network"

TITLE = "Join Our Mediator Network | Mediations Australia"
DESC = ("Interested in joining Mediations Australia's national mediator network? Register your "
        "expression of interest and tell us about your experience, specialisations and locations.")

QA = [
    ("Do I need to be based in a capital city?",
     "No. We're interested in practitioners in metropolitan and regional locations, especially those able to provide face-to-face mediation in their local area."),
    ("Can I express interest if I primarily mediate online?",
     "Yes. Tell us about your online and in-person capabilities so we can understand your practice."),
    ("What practice areas are relevant?",
     "We welcome a range of mediation experience, including family, workplace, commercial, property, estate and other dispute areas. Please select the areas in which you have appropriate expertise."),
    ("Does submitting an expression of interest mean I've joined the network?",
     "No. Each expression of interest is reviewed, and any next steps are discussed individually."),
    ("Will I need to provide accreditation or insurance details?",
     "We ask for a summary of your professional credentials initially. Supporting verification may be requested later through an appropriate secure process."),
]

STATES = [("NSW","New South Wales"),("VIC","Victoria"),("QLD","Queensland"),("WA","Western Australia"),
          ("SA","South Australia"),("TAS","Tasmania"),("ACT","Australian Capital Territory"),("NT","Northern Territory")]
PRACTICE_TYPES = [("independent_mediator","Independent mediator"),("lawyer_mediator","Lawyer-mediator"),
                  ("fdr_practitioner","FDR practitioner"),("workplace_hr_mediator","Workplace / HR mediator"),("other","Other")]
CREDENTIALS = [("amdras","AMDRAS accredited"),("fdrp","Registered FDR practitioner (FDRP)"),
               ("other_credential","Other professional credential"),("working_toward","Currently working toward accreditation"),
               ("prefer_to_explain","Prefer to explain")]
EXPERIENCE = [("under_2","Under 2 years"),("2_5","2–5 years"),("6_10","6–10 years"),("11_plus","11+ years")]
AREAS = [("family_parenting","Family and parenting"),("property_financial","Property and financial settlement"),
         ("workplace_employment","Workplace and employment"),("commercial_business","Commercial and business"),
         ("estate_inheritance","Estate and inheritance"),("elder_intergenerational","Elder and intergenerational"),
         ("neighbourhood_strata_property","Neighbourhood, strata and property"),("other_specialist","Other specialist dispute areas")]
DELIVERY = [("in_person","In person"),("online","Online"),("both","Both")]
VENUE = [("own_venue","Own or regular venue"),("can_arrange","Can arrange a venue"),
         ("depends","Depends on location"),("not_applicable","Not applicable")]
CAPACITY = [("available","Currently available"),("limited","Limited capacity"),
            ("future","Future interest"),("prefer_discuss","Prefer to discuss")]
LOCATIONS = ["Sydney","Melbourne","Brisbane","Perth","Adelaide","Canberra","Hobart","Darwin",
             "Gold Coast","Sunshine Coast","Newcastle","Regional Australia"]

CSS = """<style>
.eoi[hidden],.eoi-done[hidden],.eoi .formerr[hidden]{display:none}
section.sec>.wrap-narrow{padding-left:24px;padding-right:24px}
.eoi{background:var(--cream);border:1px solid var(--line);border-radius:var(--r,20px);padding:clamp(22px,4vw,40px);display:flex;flex-direction:column;gap:34px}
.eoi fieldset{border:0;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 20px}
.eoi legend{font-family:var(--serif);font-size:1.25rem;color:var(--ink);padding:0;margin-bottom:18px;grid-column:1/-1}
.eoi .full{grid-column:1/-1}
.eoi .f{display:flex;flex-direction:column;gap:7px;min-width:0}
.eoi label.l,.eoi .l{font-size:.92rem;font-weight:600;color:var(--ink)}
.eoi .req{color:var(--terra)}
.eoi .opt{font-weight:400;color:var(--ink-soft);font-size:.85rem}
.eoi input[type=text],.eoi input[type=email],.eoi input[type=tel],.eoi input[type=url],.eoi select,.eoi textarea{width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand);color:var(--ink)}
.eoi textarea{resize:vertical;min-height:110px}
.eoi input:focus-visible,.eoi select:focus-visible,.eoi textarea:focus-visible{outline:2px solid var(--sage-deep);outline-offset:2px;border-color:var(--sage-deep)}
.eoi .hint{font-size:.84rem;color:var(--ink-soft)}
.eoi .err{font-size:.86rem;color:#a3361f}
.eoi .err:empty{display:none}
.eoi [aria-invalid=true]{border-color:#a3361f!important}
.eoi .chips{display:flex;flex-wrap:wrap;gap:10px}
.eoi .chip{position:relative;display:inline-flex}
.eoi .chip input{position:absolute;opacity:0;inset:0;margin:0;cursor:pointer}
.eoi .chip span{display:inline-block;padding:10px 16px;border:1.5px solid var(--line);border-radius:100px;background:var(--sand);font-size:.92rem;color:var(--ink);transition:background .15s,border-color .15s}
.eoi .chip input:checked+span{background:var(--sage-light);border-color:var(--sage-deep);color:var(--sage-deep);font-weight:600}
.eoi .chip input:focus-visible+span{outline:2px solid var(--sage-deep);outline-offset:2px}
.eoi .ck{display:flex;gap:12px;align-items:flex-start;font-size:.95rem;color:var(--ink-soft);line-height:1.55}
.eoi .ck input{width:20px;height:20px;margin-top:2px;accent-color:var(--sage-deep);flex-shrink:0}
.eoi .ck a{color:var(--sage-deep);text-decoration:underline}
.eoi .hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.eoi .formerr{background:#fbeeea;border:1px solid #e7b9ab;color:#7a2a17;border-radius:12px;padding:14px 18px;font-size:.95rem}
.eoi-done{background:var(--sage-light);border-left:4px solid var(--sage-deep);border-radius:0 16px 16px 0;padding:32px}
.eoi-done h3{margin:0 0 12px!important}
.eoi-done p{color:var(--ink)!important;line-height:1.75;margin:0!important}
.loc-list{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 30px}
.loc-list span{padding:7px 14px;border-radius:100px;background:var(--cream);border:1px solid var(--line);font-size:.9rem;color:var(--ink-soft)}
@media(max-width:640px){.eoi fieldset{grid-template-columns:minmax(0,1fr)}}
</style>"""


def opts(items, placeholder="Select…"):
    return f'<option value="">{placeholder}</option>' + "".join(f'<option value="{v}">{esc(t)}</option>' for v, t in items)


def chips(name, items, kind="checkbox"):
    return '<div class="chips">' + "".join(
        f'<label class="chip"><input type="{kind}" name="{name}" value="{v}"><span>{esc(t)}</span></label>'
        for v, t in items) + "</div>"


def field(fid, label, control, required=False, hint="", full=False):
    mark = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">(optional)</span>'
    hint_html = f'<span class="hint" id="{fid}-hint">{hint}</span>' if hint else ""
    return (f'<div class="f{" full" if full else ""}"><label class="l" for="{fid}">{label}{mark}</label>'
            f'{control}{hint_html}<span class="err" id="{fid}-err" role="alert"></span></div>')


def group(gid, label, control, required=False):
    mark = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">(optional)</span>'
    return (f'<div class="f full" role="group" aria-labelledby="{gid}-l" id="{gid}">'
            f'<span class="l" id="{gid}-l">{label}{mark}</span>{control}'
            f'<span class="err" id="{gid}-err" role="alert"></span></div>')


def inp(fid, name, typ="text", req=False, auto="", maxlen=200, ph=""):
    a = f' autocomplete="{auto}"' if auto else ""
    r = ' required aria-required="true"' if req else ""
    p = f' placeholder="{ph}"' if ph else ""
    return f'<input id="{fid}" name="{name}" type="{typ}" maxlength="{maxlen}"{a}{r}{p} aria-describedby="{fid}-err">'


def form_html():
    return f"""<form class="eoi" id="eoiForm" novalidate>
  <div class="formerr" id="eoiFormErr" role="alert" hidden></div>
  <fieldset>
    <legend>Your contact details</legend>
    {field("e-name","Full name",inp("e-name","name",req=True,auto="name",maxlen=120),True)}
    {field("e-email","Professional email",inp("e-email","email","email",True,"email",254),True)}
    {field("e-phone","Phone",inp("e-phone","phone","tel",True,"tel",30),True)}
    {field("e-city","Primary city or suburb",inp("e-city","city",req=True,auto="address-level2",maxlen=100),True)}
    {field("e-state","State or territory",f'<select id="e-state" name="state" required aria-required="true" aria-describedby="e-state-err">{opts(STATES)}</select>',True)}
    {field("e-org","Practice or organisation name",inp("e-org","organisation",auto="organization",maxlen=150))}
    {field("e-website","Professional website or LinkedIn",inp("e-website","website","url",auto="url",maxlen=300,ph="https://"),full=True)}
  </fieldset>

  <fieldset>
    <legend>Your professional profile</legend>
    {field("e-ptype","Current role or practice type",f'<select id="e-ptype" name="practice_type" aria-describedby="e-ptype-err">{opts(PRACTICE_TYPES)}</select>')}
    {field("e-exp","Years of mediation experience",f'<select id="e-exp" name="experience_band" required aria-required="true" aria-describedby="e-exp-err">{opts(EXPERIENCE)}</select>',True)}
    {group("credential_types","Accreditation or registration",chips("credential_types",CREDENTIALS),True)}
    {field("e-cbody","Accrediting or registration body",inp("e-cbody","credential_body",maxlen=150))}
    {field("e-cid","Registration number",inp("e-cid","credential_identifier",maxlen=80),hint="Please don't upload documents at this stage.")}
    {group("practice_areas","Practice areas",chips("practice_areas",AREAS),True)}
    {field("e-bg","Short professional background",'<textarea id="e-bg" name="background" maxlength="500" rows="4" aria-describedby="e-bg-hint e-bg-err"></textarea>',hint="Up to 500 characters.",full=True)}
  </fieldset>

  <fieldset>
    <legend>Coverage and availability</legend>
    {field("e-regions","Regions or cities you service",'<textarea id="e-regions" name="regions_served" maxlength="300" rows="2" required aria-required="true" aria-describedby="e-regions-hint e-regions-err"></textarea>',True,"Include any regional areas you can cover.",True)}
    {group("delivery_mode","How do you deliver mediation?",chips("delivery_mode",DELIVERY,"radio"),True)}
    {field("e-venue","In-person venue access",f'<select id="e-venue" name="venue_access" aria-describedby="e-venue-err">{opts(VENUE)}</select>')}
    {field("e-cap","Capacity for additional matters",f'<select id="e-cap" name="capacity_band" aria-describedby="e-cap-err">{opts(CAPACITY)}</select>')}
    {field("e-lang","Languages other than English",inp("e-lang","languages",maxlen=150),full=True)}
  </fieldset>

  <fieldset>
    <legend>A little more about you</legend>
    {field("e-why","Why are you interested in joining our network?",'<textarea id="e-why" name="motivation" maxlength="500" rows="4" aria-describedby="e-why-hint e-why-err"></textarea>',hint="Up to 500 characters.",full=True)}
    <div class="f full">
      <label class="ck"><input type="checkbox" name="accuracy_confirmed" id="e-acc" aria-describedby="e-acc-err"><span>I confirm that the information provided is accurate to the best of my knowledge. <span class="req" aria-hidden="true">*</span></span></label>
      <span class="err" id="e-acc-err" role="alert"></span>
    </div>
    <div class="f full">
      <label class="ck"><input type="checkbox" name="privacy_acknowledged" id="e-priv" aria-describedby="e-priv-err"><span>I have read the <a href="/privacy-policy/" target="_blank" rel="noopener">Privacy Policy</a> and understand Mediations Australia will use my information to assess and respond to this expression of interest. <span class="req" aria-hidden="true">*</span></span></label>
      <span class="err" id="e-priv-err" role="alert"></span>
    </div>
    <div class="f full">
      <label class="ck"><input type="checkbox" name="marketing_opt_in" id="e-mkt"><span>I'd like to receive occasional updates about the Mediations Australia practitioner network. <span class="opt">(optional)</span></span></label>
    </div>
  </fieldset>

  <div class="hp" aria-hidden="true"><label for="e-hp">Leave this field empty</label><input id="e-hp" name="_hp" type="text" tabindex="-1" autocomplete="off"></div>
  <div><button type="submit" class="btn btn-primary" id="eoiSubmit" style="font-size:1.05rem;padding:16px 34px"><span id="eoiSubmitTxt">Submit Expression of Interest</span> <span class="arr">→</span></button></div>
</form>
<div class="eoi-done" id="eoiDone" tabindex="-1" hidden>
  <h3>Thank you for your interest</h3>
  <p>Thank you for your interest in the Mediations Australia Mediator Network. We've received your expression of interest. Our team will review your information and contact you if we'd like to discuss next steps. Submission does not guarantee acceptance or future work.</p>
</div>"""


JS = """<script>
(function(){
  var f=document.getElementById('eoiForm'); if(!f) return;
  var started=false, busy=false;
  function ev(n){try{if(window.gtag)gtag('event',n,{form_name:'mediator_network_eoi'})}catch(e){}}
  ev('mediator_eoi_view');
  function start(){if(!started){started=true;ev('mediator_eoi_start')}}
  f.addEventListener('input',start);f.addEventListener('change',start);
  var MAP={name:'e-name',email:'e-email',phone:'e-phone',city:'e-city',state:'e-state',organisation:'e-org',website:'e-website',
    practice_type:'e-ptype',experience_band:'e-exp',credential_types:'credential_types',credential_body:'e-cbody',credential_identifier:'e-cid',
    practice_areas:'practice_areas',background:'e-bg',regions_served:'e-regions',delivery_mode:'delivery_mode',venue_access:'e-venue',
    capacity_band:'e-cap',languages:'e-lang',motivation:'e-why',accuracy_confirmed:'e-acc',privacy_acknowledged:'e-priv'};
  var fe=document.getElementById('eoiFormErr'), btn=document.getElementById('eoiSubmit'), txt=document.getElementById('eoiSubmitTxt');
  function clear(){f.querySelectorAll('.err').forEach(function(e){e.textContent=''});f.querySelectorAll('[aria-invalid]').forEach(function(e){e.removeAttribute('aria-invalid')});fe.hidden=true}
  function show(errs){var first=null;Object.keys(errs).forEach(function(k){var id=MAP[k];if(!id)return;var el=document.getElementById(id),er=document.getElementById(id+'-err');if(er)er.textContent=errs[k];if(el){el.setAttribute('aria-invalid','true');if(!first)first=el.matches('input,select,textarea')?el:el.querySelector('input')}});if(first)first.focus()}
  function vals(n){return Array.prototype.map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(i){return i.value})}
  function v(n){var el=f.elements[n];return el&&el.value!==undefined?String(el.value).trim():''}
  function check(d){var e={};
    if(!d.name)e.name='Full name is required.';
    if(!d.email)e.email='Email is required.';else if(!/^[^\\s@<>()]+@[^\\s@<>()]+\\.[a-z]{2,}$/i.test(d.email))e.email='Please enter a valid email address.';
    if(!d.phone)e.phone='Phone is required.';else if(d.phone.replace(/\\D/g,'').length<8)e.phone='Please enter a valid phone number.';
    if(!d.city)e.city='City or suburb is required.';
    if(!d.state)e.state='Please select a state or territory.';
    if(d.website&&!/^https?:\\/\\/\\S+\\.\\S+$/i.test(d.website))e.website='Please enter a full web address starting with https://';
    if(!d.credential_types.length)e.credential_types='Please select at least one option.';
    if(!d.experience_band)e.experience_band='Please select your years of experience.';
    if(!d.practice_areas.length)e.practice_areas='Please select at least one practice area.';
    if(!d.regions_served)e.regions_served='Please tell us which regions or cities you service.';
    if(!d.delivery_mode)e.delivery_mode='Please select how you deliver mediation.';
    if(!d.accuracy_confirmed)e.accuracy_confirmed='Please confirm your information is accurate.';
    if(!d.privacy_acknowledged)e.privacy_acknowledged='Please acknowledge the Privacy Policy.';
    return e}
  function fail(msg){ev('mediator_eoi_submit_error');fe.textContent=msg;fe.hidden=false}
  f.addEventListener('submit',function(x){x.preventDefault();if(busy)return;clear();
    var d={_gotcha:v('_hp'),name:v('name'),email:v('email'),phone:v('phone'),city:v('city'),state:v('state'),
      organisation:v('organisation'),website:v('website'),practice_type:v('practice_type'),credential_types:vals('credential_types'),
      credential_body:v('credential_body'),credential_identifier:v('credential_identifier'),experience_band:v('experience_band'),
      practice_areas:vals('practice_areas'),background:v('background'),regions_served:v('regions_served'),delivery_mode:(vals('delivery_mode')[0]||''),
      venue_access:v('venue_access'),capacity_band:v('capacity_band'),languages:v('languages'),motivation:v('motivation'),
      accuracy_confirmed:f.elements.accuracy_confirmed.checked,privacy_acknowledged:f.elements.privacy_acknowledged.checked,
      marketing_opt_in:f.elements.marketing_opt_in.checked};
    var e=check(d);if(Object.keys(e).length){show(e);return}
    busy=true;btn.disabled=true;txt.textContent='Submitting…';
    d._subject='Mediator Network EOI — '+d.name+' ('+d.state+')';d._replyto=d.email;d.source='mediator_network_eoi';
    fetch('https://formspree.io/f/xoeeerjo',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(d)})
      .then(function(r){return r.json().catch(function(){return{}}).then(function(j){return{s:r.status,j:j}})})
      .then(function(r){
        if(r.s>=200&&r.s<300){ev('mediator_eoi_submit_success');f.hidden=true;var dn=document.getElementById('eoiDone');dn.hidden=false;setTimeout(function(){location.href='/join-our-mediator-network/thank-you/'},350);return}
        fail('Something went wrong. Please try again, or email hello@mediationsaustralia.com.au.')})
      .catch(function(){fail('We could not reach our server. Please check your connection and try again.')})
      .then(function(){busy=false;btn.disabled=false;txt.textContent='Submit Expression of Interest'})});
})();
</script>"""


def build():
    schema = [org_schema(), breadcrumb_schema([("Home", ""), ("Join Our Mediator Network", SLUG)])]
    doc = head(TITLE, DESC, SLUG, extra_schema=schema)
    doc = doc.replace("</head>", CSS + "\n</head>")
    doc += nav()

    why_cards = "".join(
        f'<article class="card"><h3>{h}</h3><p>{p}</p></article>' for h, p in [
            ("Relevant matters", "Opportunities to be considered for matters that align with your experience and practice areas."),
            ("Local and online capability", "Help parties access suitable mediation, including face-to-face services where practicable."),
            ("Professional standards", "A focus on competence, impartiality, confidentiality and appropriate professional practice."),
            ("Coordinated intake", "A central team working toward clear enquiry handling, matter preparation and communication."),
        ])
    areas_list = "".join(f"<li>{esc(t)}</li>" for _, t in AREAS)
    locs = "".join(f"<span>{esc(l)}</span>" for l in LOCATIONS)

    doc += f"""<main id="main">
{crumb_html([("Home",""),("Join Our Mediator Network",None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>Join us</span>
    <h1>Join the Mediations Australia <em>Mediator Network</em></h1>
    <p class="lede">We're growing our national network of experienced mediators to help more Australians resolve disputes through a professional, impartial and constructive process. If you're an established practitioner who shares our commitment to quality dispute resolution, we'd welcome an expression of interest.</p>
    <div class="phero-cta">
      <a href="#expression-of-interest" class="btn btn-primary">Express Your Interest <span class="arr">&#8595;</span></a>
      <a href="/about-mediations-australia/" class="btn btn-ghost">Learn About Mediations Australia</a>
    </div>
    <p style="margin-top:22px;font-size:.92rem;color:var(--ink-soft)">Expressions of interest are reviewed individually. Submission does not guarantee appointment to the network.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="reveal" style="max-width:62ch">
      <p class="sec-tag">Who we are</p>
      <h2 class="sec-title">A national approach to <em>resolving disputes</em></h2>
      <p class="sec-intro" style="margin-bottom:18px">Mediations Australia helps individuals, families, organisations and professional advisers explore constructive alternatives to prolonged disputes and litigation. Our work spans a range of mediation needs, from family and property matters to workplace, commercial and estate disputes.</p>
      <p class="sec-intro">As demand for local and online mediation grows, we're developing a network of practitioners who can bring relevant experience, professional judgement and a commitment to impartial practice to matters across Australia.</p>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="reveal">
      <p class="sec-tag">Why express interest?</p>
      <h2 class="sec-title">Be part of a professional, <em>nationally connected</em> network</h2>
    </div>
    <div class="cards reveal" style="margin-top:44px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{why_cards}</div>
  </div>
</section>

<section class="sec" style="padding:0">
  <div class="wrap-narrow">
    <p class="sec-tag">Who we'd like to hear from</p>
    <h2 style="margin-top:10px">Experienced mediators <em>across Australia</em></h2>
    <p>We welcome expressions of interest from suitably qualified and experienced practitioners, including mediators with recognised Australian accreditation and practitioners with relevant specialist credentials. We are particularly interested in mediators who can support local, face-to-face matters as well as online mediation.</p>
    <h3>Areas of practice</h3>
    <ul>{areas_list}</ul>
    <h3>Locations</h3>
    <p style="margin-bottom:14px">We'd particularly like to hear from practitioners in and around:</p>
    <div class="loc-list">{locs}</div>
    <h3>Professional attributes</h3>
    <p>Clear communication, impartiality, appropriate screening and professional boundaries, reliable administration, and a constructive approach to working with parties and advisers.</p>
  </div>
</section>

<section class="sec" style="padding:0">
  <div class="wrap-narrow">
    <p class="sec-tag">How it works</p>
    <h2 style="margin-top:10px">A straightforward <em>first step</em></h2>
    <ol>
      <li><strong>Tell us about your practice.</strong> Complete the short form below with your credentials, experience, areas of practice and locations.</li>
      <li><strong>Our team reviews your information.</strong> We may contact you to discuss experience, availability, professional requirements and potential fit.</li>
      <li><strong>Next steps by invitation.</strong> Where appropriate, we may request verification documents or arrange a conversation before considering network participation.</li>
    </ol>
    <div class="answer"><p><strong>Important:</strong> An expression of interest is not an application for employment and does not create a practitioner appointment or promise work.</p></div>
  </div>
</section>

<section class="sec" id="expression-of-interest" style="padding:0;scroll-margin-top:90px">
  <div class="wrap-narrow">
    <p class="sec-tag">Express your interest</p>
    <h2 style="margin-top:10px">Tell us about your <em>practice</em></h2>
    <p>Share a little about your mediation practice. It takes about 3–5 minutes. Please do not include client names, confidential case details or sensitive personal information in your submission.</p>
    {form_html()}
  </div>
</section>
"""
    doc += faq_html(QA, heading="Questions from <em>practitioners</em>.", tag="Common questions")
    doc += """<section class="cta-band">
  <div class="phero-blob"></div>
  <div class="wrap">
    <div class="reveal">
      <h2>Help more people access <em>constructive dispute resolution</em>.</h2>
      <p>If our approach aligns with your professional practice, we'd be pleased to hear from you.</p>
      <a href="#expression-of-interest" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Express Your Interest <span class="arr">→</span></a>
    </div>
  </div>
</section>
"""
    doc += "</main>" + page_end()
    doc = doc.replace("</body>", JS + "\n</body>")

    path = os.path.join(OUT, SLUG)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as fh:
        fh.write(doc)
    print(f"Built: /{SLUG}/")
    build_thanks()


def build_thanks():
    slug = f"{SLUG}/thank-you"
    doc = head("Thank You | Join Our Mediator Network | Mediations Australia",
               "Thank you for your expression of interest in the Mediations Australia Mediator Network.",
               slug, extra_schema=[org_schema()])
    doc = doc.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                      '<meta name="robots" content="noindex, follow">')
    doc += nav()
    doc += f"""<main id="main">
{crumb_html([("Home",""),("Join Our Mediator Network",SLUG),("Thank you",None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>Expression of interest received</span>
    <h1>Thank you for your <em>interest</em></h1>
    <p class="lede">We've received your expression of interest in the Mediations Australia Mediator Network. Our team will review your information and contact you if we'd like to discuss next steps.</p>
    <div class="phero-cta">
      <a href="/" class="btn btn-primary">Back to Home <span class="arr">→</span></a>
      <a href="/about-mediations-australia/" class="btn btn-ghost">Learn About Mediations Australia</a>
    </div>
  </div>
</section>

<section class="sec" style="padding:0">
  <div class="wrap-narrow">
    <p class="sec-tag">What happens next</p>
    <h2 style="margin-top:10px">Our review <em>process</em></h2>
    <ol>
      <li><strong>We review your information.</strong> Each expression of interest is considered individually against our network needs, practice areas and locations.</li>
      <li><strong>We may be in touch.</strong> If there's a potential fit, we may contact you to discuss your experience, availability and professional requirements.</li>
      <li><strong>Next steps by invitation.</strong> Where appropriate, we may request verification documents or arrange a conversation before considering network participation.</li>
    </ol>
    <div class="answer"><p><strong>Please note:</strong> Submission does not guarantee acceptance to the network or future work. If you need to update anything you've sent, email <a href="mailto:hello@mediationsaustralia.com.au">hello@mediationsaustralia.com.au</a>.</p></div>
  </div>
</section>
</main>"""
    doc += page_end()
    doc = doc.replace("</head>", CSS + "\n</head>")
    doc = doc.replace("</body>", "<script>try{if(window.gtag)gtag('event','mediator_eoi_thank_you_view',{form_name:'mediator_network_eoi'})}catch(e){}</script>\n</body>")
    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as fh:
        fh.write(doc)
    print(f"Built: /{slug}/")


if __name__ == "__main__":
    build()
