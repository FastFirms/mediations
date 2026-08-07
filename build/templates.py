#!/usr/bin/env python3
"""Shared template components for Mediations Australia site generation."""
import html, json

DOMAIN = "https://mediationsaustralia.com.au"
PHONE = "1800 952 380"
PHONE_HREF = "tel:1800952380"
BOOK_URL = "/book-a-consultation/"

# ---- Navigation data (shared megamenu) ----
SERVICES = [
    ("family-law-mediation", "Family Law Mediation", "Parenting & property, resolved without court"),
    ("divorce-mediation", "Divorce Mediation", "Resolve everything that comes with divorce"),
    ("online-divorce", "Online Divorce", "Separate from anywhere in Australia"),
    ("de-facto-mediation", "De Facto Disputes", "Same rights, same clear process"),
    ("property-settlement-mediation", "Property Settlement", "Divide assets fairly and finally"),
    ("financial-agreements-mediation", "Financial Agreements", "Binding agreements (BFAs), done right"),
    ("spousal-support-mediation", "Spousal Maintenance", "Fair support after separation"),
    ("consent-orders", "Consent Orders", "Make your agreement legally binding"),
    ("parenting-plan-mediation", "Parenting Plans", "Workable arrangements for your children"),
    ("child-support-mediation", "Child Support", "Resolve support disputes privately"),
    ("section-60i-certificates", "Section 60I Certificates", "Required before parenting court action"),
    ("grandparents-mediation", "Grandparents' Rights", "Stay in your grandchildren's lives"),
    ("workplace-mediation", "Workplace & Employment Mediation", "Resolve disputes before the Fair Work Commission"),
    ("unfair-dismissal-termination-mediation", "Unfair Dismissal & Termination", "The 21-day deadline, and how to protect your rights"),
    ("workplace-bullying-harassment-mediation", "Bullying & Harassment", "Where mediation helps — and where it doesn't"),
    ("general-protections-discrimination-mediation", "General Protections & Discrimination", "Adverse action and protected rights, resolved"),
    ("redundancy-restructure-mediation", "Redundancy & Restructure", "Was your redundancy genuine? Know your position"),
    ("partnership-executive-exit-mediation", "Partnership & Executive Exit", "High-stakes separations, resolved privately"),
    ("workplace-investigations-grievance-mediation", "Workplace Investigations & Grievances", "Handle complaints well; repair the workplace"),
    ("belbin-team-roles-training", "Belbin Team Roles", "Build balanced teams and prevent conflict before it starts"),
    ("commercial-mediation", "Commercial Mediation", "Partnership, contract and business disputes"),
    ("real-estate-mediation", "Real Estate & Construction", "Lease, building and property disputes"),
    ("estate-dispute-mediation", "Estate & Inheritance Disputes", "Resolve will and inheritance disputes privately"),
    ("elder-mediation", "Elder & Family Care", "Care arrangements for ageing parents"),
]

# Grouped layout for the Services megamenu.
# "---" inserts a visual divider. First item per column renders as a bold lead link.
SERVICE_GROUPS = [
    ("Family & Separation", [
        "family-law-mediation",
        "divorce-mediation",
        "online-divorce",
        "de-facto-mediation",
        "property-settlement-mediation",
        "financial-agreements-mediation",
        "spousal-support-mediation",
        "consent-orders",
    ]),
    ("Parenting & Children", [
        "parenting-plan-mediation",
        "child-support-mediation",
        "section-60i-certificates",
        "grandparents-mediation",
    ]),
    ("Workplace & Employment", [
        "workplace-mediation",
        "unfair-dismissal-termination-mediation",
        "workplace-bullying-harassment-mediation",
        "general-protections-discrimination-mediation",
        "redundancy-restructure-mediation",
        "partnership-executive-exit-mediation",
        "workplace-investigations-grievance-mediation",
        "---",
        "belbin-team-roles-training",
    ]),
    ("Business, Property & Estates", [
        "commercial-mediation",
        "real-estate-mediation",
        "estate-dispute-mediation",
        "elder-mediation",
    ]),
]

# Primary capital-city + major regional locations
LOCATIONS = [
    ("sydney-mediation", "Sydney"),
    ("melbourne-mediation", "Melbourne"),
    ("brisbane-mediation", "Brisbane"),
    ("perth-mediation", "Perth"),
    ("adelaide-mediation", "Adelaide"),
    ("canberra-mediation", "Canberra"),
    ("gold-coast-mediation", "Gold Coast"),
    ("newcastle-mediation", "Newcastle"),
    ("wollongong-mediation", "Wollongong"),
    ("geelong-mediation", "Geelong"),
    ("hobart-mediation", "Hobart"),
    ("darwin-mediation", "Darwin"),
    ("cairns-mediation", "Cairns"),
    ("townsville-mediation", "Townsville"),
    ("toowoomba-mediation", "Toowoomba"),
    ("sunshine-coast-mediation", "Sunshine Coast"),
    ("bendigo-mediation", "Bendigo"),
    ("coffs-harbour-mediation", "Coffs Harbour"),
    ("launceston-mediation", "Launceston"),
    ("mackay-mediation", "Mackay"),
    ("rockhampton-mediation", "Rockhampton"),
]

OFFICES = [
    ("Sydney", "Suite 508, 41/464–480 Kent St, NSW 2000"),
    ("Melbourne", "Level 23, 727 Collins St, VIC 3008"),
    ("Brisbane", "Suite 507, 198 Adelaide St, QLD 4000"),
    ("Perth", "Level 25, 108 St Georges Tce, WA 6000"),
]

def esc(s): return html.escape(s, quote=True)

def img(src, alt, w, h, cls="photo", caption=None, eager=False, srcset=None, sizes=None):
    """Responsive, CWV-safe <img> wrapped in <figure>. Drop optimised files
    (ideally WebP) in /assets/images/. ALWAYS pass true width/height so the
    browser reserves space and layout doesn't shift (protects CLS). Use
    eager=True only for an above-the-fold hero image (sets fetchpriority).
    Pass srcset as a list of (filename, width_descriptor) tuples, e.g.
    [('hero-800.jpg','800w'),('hero-1600.jpg','1600w')]. sizes defaults to
    '100vw' when srcset is provided."""
    loading = "eager" if eager else "lazy"
    prio = ' fetchpriority="high"' if eager else ''
    srcset_attr = ''
    sizes_attr = ''
    if srcset:
        srcset_str = ', '.join(f'/assets/images/{esc(f)} {d}' for f, d in srcset)
        srcset_attr = f' srcset="{srcset_str}"'
        sizes_val = sizes or '100vw'
        sizes_attr = f' sizes="{sizes_val}"'
    tag = (f'<img src="/assets/images/{esc(src)}" alt="{esc(alt)}" '
           f'width="{w}" height="{h}" loading="{loading}" decoding="async"{prio}'
           f'{srcset_attr}{sizes_attr}>')
    cap = f'<figcaption>{esc(caption)}</figcaption>' if caption else ''
    return f'<figure class="{cls}">{tag}{cap}</figure>'

def head(title, desc, slug, og_type="website", extra_schema=None):
    """Build <head> with full SEO/AEO meta + JSON-LD."""
    canonical = f"{DOMAIN}/" if slug == "" else f"{DOMAIN}/{slug}/"
    schema_blocks = extra_schema or []
    schema_json = json.dumps({"@context": "https://schema.org", "@graph": schema_blocks},
                             ensure_ascii=False, indent=2) if schema_blocks else ""
    schema_tag = f'<script type="application/ld+json">\n{schema_json}\n</script>' if schema_json else ""
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
<link rel="apple-touch-icon" href="/assets/images/favicon.png">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/images/MA-social.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Mediations Australia">
<meta property="og:locale" content="en_AU">
<meta name="twitter:image" content="{DOMAIN}/assets/images/MA-social.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
{schema_tag}
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7GTTR2T25L"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-7GTTR2T25L');</script>
</head>
<body>
<a href="#main" class="skip">Skip to main content</a>"""

def nav():
    svc_lookup = {s: (n, d) for s, n, d in SERVICES}
    cols = ""
    for group, slugs in SERVICE_GROUPS:
        links = ""
        for i, s in enumerate(slugs):
            if s == "---":
                links += '<hr style="border:none;border-top:1px solid var(--line);margin:8px 0">'
            elif i == 0:
                # First item is the pillar — bold lead link
                n, d = svc_lookup[s]
                links += f'<a href="/{s}/" class="mega-lead"><b>{esc(n)}</b><span>{esc(d)}</span></a>'
            elif s == "belbin-team-roles-training":
                n, d = svc_lookup[s]
                links += (f'<a href="/{s}/"><b>{esc(n)}</b>'
                          f'<span style="display:inline-flex;align-items:center;gap:6px">'
                          f'<em style="font-style:normal;font-size:.72rem;font-weight:600;letter-spacing:.04em;'
                          f'text-transform:uppercase;background:var(--sand-deep);color:var(--sage-deep);'
                          f'padding:1px 6px;border-radius:4px">Training</em></span>'
                          f'<span>{esc(d)}</span></a>')
            else:
                n, d = svc_lookup[s]
                links += f'<a href="/{s}/"><b>{esc(n)}</b><span>{esc(d)}</span></a>'
        cols += f'<div class="mega-col"><span class="mega-head">{esc(group)}</span>{links}</div>'
    svc_mega = f"""<div class="drop mega">{cols}</div>"""
    return f"""<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a href="/" class="logo"><img src="/assets/images/MA.svg" alt="Mediations Australia" width="180" height="36" loading="eager" style="display:block;height:36px;width:auto"></a>
    <nav class="nav-links" id="navlinks" aria-label="Primary">
      <a class="lnk" href="/about-mediations-australia/">About</a>
      <a class="lnk" href="/our-team/">Our Team</a>
      <span class="has-drop"><a class="lnk" href="/how-we-help/" aria-haspopup="true">How We Help</a>
        {svc_mega}
      </span>
      <a class="lnk" href="/how-mediation-works/">How it works</a>
      <a class="lnk" href="/our-fee-structure/">Our Fees</a>
      <span class="has-drop"><a class="lnk" href="/guides/" aria-haspopup="true">Resources</a>
        <div class="drop mega mega-resources">
          <div class="mega-col">
            <span class="mega-head">Start Here</span>
            <a href="/how-much-does-mediation-cost/"><b>How Much Does Mediation Cost?</b><span>Fees, who pays, and why it beats court</span></a>
            <a href="/how-long-does-mediation-take/"><b>How Long Does Mediation Take?</b><span>Most resolve in one or two sessions</span></a>
            <a href="/is-family-law-mediation-compulsory/"><b>Is Mediation Compulsory?</b><span>When it's required and the exemptions</span></a>
            <a href="/what-happens-if-mediation-fails/"><b>What If Mediation Fails?</b><span>Next steps and your options</span></a>
            <a href="/preparing-for-mediation/"><b>Preparing for Mediation</b><span>What to expect &amp; how to get ready</span></a>
            <a href="/family-law-cost-estimator/"><b>Cost Estimator</b><span>Mediation vs court costs</span></a>
          </div>
          <div class="mega-col">
            <span class="mega-head">Family &amp; Separation</span>
            <a href="/what-am-i-entitled-to-in-a-separation-in-australia/"><b>What Am I Entitled To?</b><span>Property, super and support explained</span></a>
            <a href="/property-settlement-after-separation/"><b>Property Settlement Guide</b><span>The four-step process, without court</span></a>
            <a href="/getting-ready-for-separation/"><b>Getting Ready for Separation</b><span>A practical checklist</span></a>
            <a href="/separation-under-one-roof/"><b>Separation Under One Roof</b><span>How it works legally and practically</span></a>
            <a href="/parenting-plan-template/"><b>Parenting Plan Template</b><span>What to include in your plan</span></a>
            <a href="/bfa-or-consent-orders/"><b>BFA or Consent Orders?</b><span>Which is right for you</span></a>
            <a href="/mediation-with-a-narcissist/"><b>Mediation With a Narcissist</b><span>Strategies for high-conflict situations</span></a>
          </div>
          <div class="mega-col">
            <span class="mega-head">Workplace &amp; Business</span>
            <a href="/workplace-dispute-guide/"><b>Workplace Dispute Guide</b><span>Your rights, the FWC, and mediation</span></a>
            <a href="/unfair-dismissal-21-day-rule/"><b>Unfair Dismissal: The 21-Day Rule</b><span>Deadlines, eligibility, what to do</span></a>
            <a href="/redundancy-was-it-genuine/"><b>Redundancy: Was It Genuine?</b><span>The genuine-redundancy test, plain English</span></a>
            <a href="/is-mediation-right-for-workplace-dispute/"><b>Is Mediation Right for My Dispute?</b><span>When it helps — and when it doesn't</span></a>
            <a href="/commercial-dispute-guide/"><b>Commercial Dispute Guide</b><span>Contracts, partnerships, shareholders, leases</span></a>
            <a href="/belbin-team-roles-training/"><b>Preventing Conflict (Belbin)</b><span>Build balanced teams, prevent disputes</span></a>
          </div>
          <div class="mega-col">
            <span class="mega-head">Estate &amp; Property</span>
            <a href="/contesting-a-will/"><b>Contesting a Will: Your Options</b><span>Grounds, time limits, mediation</span></a>
            <a href="/estate-inheritance-dispute-mediation/"><b>Estate &amp; Inheritance Disputes</b><span>Resolve without destroying the family</span></a>
            <a href="/real-estate-construction-disputes/"><b>Real Estate &amp; Construction Disputes</b><span>Building, boundary and property issues</span></a>
            <a href="/strata-neighbour-dispute-mediation/"><b>Strata &amp; Neighbour Disputes</b><span>Resolve without a tribunal</span></a>
            <a href="/guides/" class="mega-see-all">See all guides →</a>
          </div>
        </div>
      </span>
      <a class="lnk" href="/contact-us/">Contact</a>
      <a class="btn btn-primary" href="{BOOK_URL}" style="padding:11px 22px;font-size:.92rem">Book a Free Consultation</a>
    </nav>
    <button class="menu-btn" id="menuBtn" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>"""

def footer():
    svc = "".join(f'<li><a href="/{s}/">{esc(n)}</a></li>' for s, n, _ in SERVICES[:6])
    offices = "".join(f'<strong>{esc(c)}</strong>{esc(a)}' for c, a in OFFICES)
    locs = " ".join(f'<a href="/{s}/">{esc(n)}</a>' for s, n in LOCATIONS)
    return f"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="logo"><span class="dot"></span>Mediations Australia</div>
        <p style="font-size:.95rem;max-width:34ch;margin-bottom:18px">Nationally accredited mediators resolving disputes faster, fairer and without court — right across Australia.</p>
        <a class="btn btn-primary" href="{PHONE_HREF}" style="font-size:.95rem">Call {PHONE}</a>
      </div>
      <div>
        <h4>Family Law</h4>
        <ul>
          <li><a href="/family-law-mediation/">Family Law Mediation</a></li>
          <li><a href="/divorce-mediation/">Divorce Mediation</a></li>
          <li><a href="/property-settlement-mediation/">Property Settlement</a></li>
          <li><a href="/parenting-plan-mediation/">Parenting Plans</a></li>
          <li><a href="/child-support-mediation/">Child Support</a></li>
          <li><a href="/spousal-support-mediation/">Spousal Maintenance</a></li>
          <li><a href="/consent-orders/">Consent Orders</a></li>
          <li><a href="/financial-agreements-mediation/">Financial Agreements</a></li>
          <li><a href="/de-facto-mediation/">De Facto Disputes</a></li>
          <li><a href="/grandparents-mediation/">Grandparents' Rights</a></li>
        </ul>
      </div>
      <div>
        <h4>Other Services</h4>
        <ul>
          <li><a href="/workplace-mediation/">Workplace Mediation</a></li>
          <li><a href="/estate-dispute-mediation/">Estate Disputes</a></li>
          <li><a href="/online-divorce/">Online Mediation</a></li>
          <li><a href="/section-60i-certificates/">Section 60I Certificates</a></li>
          <li><a href="/online-mediation-australia/">Online Australia-wide</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about-mediations-australia/">About us</a></li>
          <li><a href="/how-mediation-works/">How it works</a></li>
          <li><a href="/our-fee-structure/">Our fees</a></li>
          <li><a href="/preparing-for-mediation/">Resources</a></li>
          <li><a href="/family-lawyers/">Family lawyers by city</a></li>
          <li><a href="/our-team/">Our team</a></li>
          <li><a href="/memberships/">Memberships</a></li>
          <li><a href="/contact-us/">Contact</a></li>
          <li><a href="{BOOK_URL}">Book a consultation</a></li>
        </ul>
      </div>
      <div class="foot-offices">
        <h4>Offices</h4>
        {offices}
      </div>
    </div>
    <div class="foot-locs">
      <h4>Mediation services near you</h4>
      <div class="ll">{locs}</div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Mediations Australia. All rights reserved. This site is general information, not legal advice. <a href="/privacy-policy/" style="color:inherit;text-decoration:underline;text-underline-offset:2px">Privacy Policy</a></span>
      <span>Nationally accredited under AMDRAS · Australia-wide &amp; online</span>
    </div>
  </div>
</footer>"""

SCRIPTS = """<script>
const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>10),{passive:true});
const mb=document.getElementById('menuBtn'),nl=document.getElementById('navlinks');
mb.addEventListener('click',()=>{const o=nl.classList.toggle('open');mb.classList.toggle('open',o);mb.setAttribute('aria-expanded',o)});
nl.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nl.classList.remove('open');mb.classList.remove('open');mb.setAttribute('aria-expanded',false)}));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// Mega menu: JS-driven open/close with close delay so gap between trigger and panel doesn't kill hover
document.querySelectorAll('.has-drop').forEach(hd=>{
  let t;
  const open=()=>{clearTimeout(t);hd.classList.add('open')};
  const close=()=>{t=setTimeout(()=>hd.classList.remove('open'),150)};
  hd.addEventListener('mouseenter',open);
  hd.addEventListener('mouseleave',close);
  const drop=hd.querySelector('.drop');
  if(drop){drop.addEventListener('mouseenter',open);drop.addEventListener('mouseleave',close);}
});
</script>
</body>
</html>"""

def page_end():
    return footer() + SCRIPTS

# ---- Schema builders ----
def org_schema():
    return {
        "@type": "LegalService", "@id": f"{DOMAIN}/#organization",
        "name": "Mediations Australia",
        "description": "Nationally accredited mediators resolving family, business, workplace, property and estate disputes across Australia without court.",
        "url": f"{DOMAIN}/", "telephone": PHONE, "areaServed": "AU",
        "priceRange": "Free initial consultation",
        "address": [{"@type": "PostalAddress", "addressLocality": c.split(",")[0],
                     "streetAddress": a, "addressCountry": "AU"} for c, a in OFFICES],
        # VERIFY before launch: confirm these match the real/live social profile URLs
        "sameAs": [
            "https://www.facebook.com/mediationsaustralia",
            "https://www.linkedin.com/company/mediations-australia",
            "https://www.youtube.com/@mediationsaustralia",
        ],
    }

def faq_schema(qa):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}

def breadcrumb_schema(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n,
         "item": f"{DOMAIN}/{s}/" if s else f"{DOMAIN}/"} for i, (n, s) in enumerate(trail)]}

def service_schema(name, desc, slug):
    return {"@type": "Service", "name": name, "description": desc,
            "provider": {"@id": f"{DOMAIN}/#organization"},
            "areaServed": "AU", "url": f"{DOMAIN}/{slug}/"}

DAN_TOOMBS = {
    "@type": "Person",
    "name": "Dan Toombs",
    "jobTitle": "Founder & Accredited Mediator",
    "url": f"{DOMAIN}/our-team/dan-toombs/",
    "sameAs": [
        "https://amdras.au/",
        "https://www.churchilltrust.com.au/",
    ],
}

def article_schema(headline, desc):
    return {"@type": "Article", "headline": headline, "description": desc,
            "author": DAN_TOOMBS,
            "publisher": {"@id": f"{DOMAIN}/#organization"}}

# ---- Reusable HTML fragments ----
def faq_html(qa, heading="Common questions", tag="Questions &amp; answers"):
    items = "".join(
        f'<details class="faq"><summary>{esc(q)}<span class="ico">+</span></summary>'
        f'<div class="ans"><p>{a}</p></div></details>' for q, a in qa)
    return f"""<section class="sec" id="faq" aria-labelledby="faqh" style="padding-top:0">
  <div class="wrap">
    <div class="reveal" style="text-align:center;max-width:60ch;margin:0 auto">
      <p class="sec-tag" style="text-align:center">{tag}</p>
      <h2 class="sec-title" id="faqh" style="margin:0 auto 8px">{heading}</h2>
    </div>
    <div class="faq-wrap reveal">{items}</div>
  </div>
</section>"""

def crumb_html(trail):
    parts = []
    for i, (n, s) in enumerate(trail):
        if i < len(trail) - 1:
            href = f"/{s}/" if s else "/"
            parts.append(f'<a href="{href}">{esc(n)}</a><span>›</span>')
        else:
            parts.append(esc(n))
    return f'<div class="wrap"><nav class="crumb" aria-label="Breadcrumb">{"".join(parts)}</nav></div>'

def cta_band(h, p, note=True):
    notes = ""
    if note:
        check = '<svg width="18" height="18" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="var(--sage)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        notes = f'<div class="note"><span>{check}No obligation</span><span>{check}Transparent pricing</span><span>{check}In person or online</span></div>'
    return f"""<section class="cta-band" id="book">
  <div class="phero-blob"></div>
  <div class="wrap">
    <div class="reveal">
      <h2>{h}</h2>
      <p>{p}</p>
      <a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Book a Free Consultation <span class="arr">→</span></a>
      {notes}
    </div>
  </div>
</section>"""

MEDIATION_TYPES = [
    ("Property Settlement",      "Property Settlement"),
    ("Parenting",                "Parenting"),
    ("Property &amp; Parenting", "Property & Parenting"),
    ("Other Family Law",         "Other Family Law"),
    ("Workplace",                "Workplace"),
    ("Estate",                   "Estate"),
    ("Something else",           "Something else"),
]

# Shared canonical form fields used across homepage, contact, and booking pages.
# field_style: inline style string applied to all inputs/select/textarea.
# prefix: short unique prefix for label `for`/input `id` pairs (avoid id clashes).
# subject: value for hidden _subject field.
# btn_label: submit button text.
def contact_form_fields(prefix="f", field_style="", subject="Consultation request — Mediations Australia", btn_label='Book a Free Consultation <span class="arr">→</span>'):
    fs = f' style="{field_style}"' if field_style else ''
    opts = "".join(f'<option value="{v}">{v}</option>' for v, _ in MEDIATION_TYPES)
    return f"""
        <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;opacity:0" aria-hidden="true">
        <input type="hidden" name="_subject" value="{esc(subject)}">
        <div class="form-row">
          <label for="{prefix}-name">Name</label>
          <input id="{prefix}-name" name="name" type="text" required autocomplete="name" placeholder="Your full name"{fs}>
        </div>
        <div class="form-row">
          <label for="{prefix}-phone">Phone</label>
          <input id="{prefix}-phone" name="phone" type="tel" required autocomplete="tel" placeholder="0400 000 000"{fs}>
        </div>
        <div class="form-row">
          <label for="{prefix}-email">Email</label>
          <input id="{prefix}-email" name="email" type="email" required autocomplete="email" placeholder="you@example.com"{fs}>
        </div>
        <div class="form-row">
          <label for="{prefix}-matter">Type of Mediation</label>
          <select id="{prefix}-matter" name="matter" required{fs}>
            <option value="" disabled selected>Select…</option>
            {opts}
          </select>
        </div>
        <div class="form-row">
          <label for="{prefix}-location">Your Location</label>
          <input id="{prefix}-location" name="location" type="text" placeholder="e.g. Sydney, Melbourne, or Online"{fs}>
        </div>
        <div class="form-row">
          <label for="{prefix}-message">Brief Explanation</label>
          <textarea id="{prefix}-message" name="message" rows="4" placeholder="A few sentences about your situation…"{fs}></textarea>
        </div>
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;font-size:1rem;padding:15px 20px">{btn_label}</button>"""

print("templates module ready")
