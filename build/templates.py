#!/usr/bin/env python3
"""Shared template components for Mediations Australia site generation."""
import html, json, datetime

DOMAIN = "https://www.mediationsaustralia.com.au"
BUILD_DATE = datetime.date.today().isoformat()  # e.g. "2026-08-08"
PHONE = "(02) 7227 7373"
PHONE_HREF = "tel:0272277373"
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

def esc(s): return html.escape(html.unescape(str(s)), quote=True)

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

def head(title, desc, slug, og_type="website", extra_schema=None, canonical_url=None):
    """Build <head> with full SEO/AEO meta + JSON-LD.
    canonical_url: override the default canonical (e.g. point a /questions/ page at its parent cornerstone).
    """
    canonical = canonical_url if canonical_url else (f"{DOMAIN}/" if slug == "" else f"{DOMAIN}/{slug}/")
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
    svc_mega = f"""<div class="drop mega mega-services">{cols}</div>"""
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
            <span class="mega-head">Costs &amp; Affordability</span>
            <a href="/access-mediation/"><b>Access Mediation</b><span>Reduced-fee pathway — check your contribution</span></a>
            <a href="/cant-afford-mediation/"><b>Can't Afford Mediation?</b><span>Every realistic option in Australia</span></a>
            <a href="/is-family-mediation-free-australia/"><b>Is Family Mediation Free?</b><span>When it's free, subsidised, or reduced-fee</span></a>
            <a href="/who-pays-mediation-one-person-earns-more/"><b>Who Pays When One Earns More?</b><span>Individual assessment — your fee is separate</span></a>
            <a href="/asset-rich-cash-poor-mediation/"><b>Asset Rich, Cash Poor</b><span>Property doesn't equal accessible cash</span></a>
            <a href="/family-relationship-centre-vs-private-mediation/"><b>FRC vs Private Mediation</b><span>Honest comparison of both options</span></a>
          </div>
          <div class="mega-col">
            <span class="mega-head">Family &amp; Separation</span>
            <a href="/what-am-i-entitled-to-in-a-separation-in-australia/"><b>What Am I Entitled To?</b><span>Property, super and support explained</span></a>
            <a href="/property-settlement-after-separation/"><b>Property Settlement Guide</b><span>The four-step process, without court</span></a>
            <a href="/consent-orders-explained/"><b>Consent Orders Explained</b><span>Making your agreement legally binding</span></a>
            <a href="/separation-guide/"><b>Separation Guide</b><span>First steps, rights, and protecting yourself</span></a>
            <a href="/parenting-plans-guide/"><b>Parenting Plans Guide</b><span>What to include and how to agree one</span></a>
            <a href="/mediation-with-a-narcissist/"><b>Mediation With a Narcissist</b><span>Strategies for high-conflict situations</span></a>
          </div>
          <div class="mega-col">
            <span class="mega-head">Workplace &amp; Business</span>
            <a href="/workplace-dispute-guide/"><b>Workplace Dispute Guide</b><span>Your rights, the FWC, and mediation</span></a>
            <a href="/unfair-dismissal-21-day-rule/"><b>Unfair Dismissal: The 21-Day Rule</b><span>Deadlines, eligibility, what to do</span></a>
            <a href="/commercial-dispute-guide/"><b>Commercial Dispute Guide</b><span>Contracts, partnerships, shareholders, leases</span></a>
            <a href="/contesting-a-will/"><b>Contesting a Will</b><span>Grounds, time limits, mediation</span></a>
            <a href="/real-estate-construction-disputes/"><b>Real Estate &amp; Construction</b><span>Building, boundary and property issues</span></a>
            <a href="/guides/" class="mega-see-all">See all 63 guides →</a>
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
<script src="/widget.js" defer></script>
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
    "@id": f"{DOMAIN}/#dan-toombs",
    "name": "Dan Toombs",
    "jobTitle": "Founder & Accredited Mediator",
    "description": (
        "Dan Toombs is an AMDRAS-accredited mediator, award-winning lawyer, "
        "former tribunal member (QCAT), former CEO and Board Director, "
        "and Winston Churchill Fellow. He founded Mediations Australia to give "
        "individuals and businesses a practical, durable alternative to litigation."
    ),
    "url": f"{DOMAIN}/our-team/dan-toombs/",
    "image": f"{DOMAIN}/assets/images/Dan-Bio.png",
    "sameAs": [
        "https://www.linkedin.com/in/dantoombs/",
        "https://amdras.au/",
        "https://www.churchilltrust.com.au/",
    ],
    "knowsAbout": [
        "Family law mediation",
        "Workplace mediation",
        "Commercial mediation",
        "Dispute resolution",
        "Fair Work Act",
        "Belbin Team Roles",
        "Adaptive Leadership",
    ],
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "AMDRAS Accredited Mediator"},
        {"@type": "EducationalOccupationalCredential", "name": "Winston Churchill Fellow"},
    ],
    "memberOf": {"@type": "Organization", "@id": f"{DOMAIN}/#organization"},
}

def person_schema():
    """Return the DAN_TOOMBS Person node as a standalone schema block."""
    return DAN_TOOMBS

def article_schema(headline, desc):
    return {"@type": "Article", "headline": headline, "description": desc,
            "datePublished": BUILD_DATE, "dateModified": BUILD_DATE,
            "image": f"{DOMAIN}/assets/images/MA-social.png",
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

def quiz_card():
    """Return the self-contained 'Will Mediation Work for Me?' assessment card HTML+CSS+JS."""
    return """<div id="hero-check" style="background:var(--sage-deep);color:var(--cream);border-radius:22px;padding:clamp(24px,3vw,34px);box-shadow:0 4px 32px rgba(13,34,24,.18)">
  <div id="qmintro" style="margin-bottom:18px">
    <p style="font-family:var(--body-serif);font-size:clamp(1.1rem,2vw,1.4rem);font-weight:400;color:var(--cream);margin:0 0 8px;line-height:1.3">Will Mediation Work for Me?</p>
    <p style="font-size:.84rem;color:rgba(216,234,217,.65);margin:0 0 16px;line-height:1.55">Around 2 minutes &mdash; tailored to your situation.</p>
    <button id="qstartbtn" onclick="qStart()" style="display:flex;align-items:center;gap:8px;background:rgba(168,200,159,.12);border:1px solid rgba(168,200,159,.35);color:var(--cream);padding:12px 20px;border-radius:11px;font-size:.92rem;font-family:var(--sans);cursor:pointer;width:100%;justify-content:center;transition:background .16s,border-color .16s">
      Start the assessment <span style="font-size:1.1em">&#8594;</span>
    </button>
    <p style="font-size:.74rem;color:rgba(216,234,217,.38);margin:14px 0 0;line-height:1.5">This tool gives general guidance only and is not legal advice. If safety is a concern, please call 000 or 1800RESPECT (1800 737 732).</p>
  </div>
  <div class="qprogress" aria-hidden="true" id="qprogbar" style="display:none"><div class="qprogress-fill" id="qpfill" style="width:8%"></div></div>
  <div id="quiz60" style="display:none">
    <!-- Q1: Dispute type -->
    <div class="qstep" id="qs1">
      <p class="qlabel">Step 1 of 9 &mdash; What needs to be resolved?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs1','qs2_property',{type:'property'},'18%')"><span class="qcircle"></span>Property &amp; finances</button>
        <button class="qbtn" onclick="qGo('qs1','qs2_parenting',{type:'parenting'},'18%')"><span class="qcircle"></span>Parenting &amp; children</button>
        <button class="qbtn" onclick="qGo('qs1','qs2_both',{type:'both'},'18%')"><span class="qcircle"></span>Both &mdash; property and parenting</button>
        <button class="qbtn" onclick="qGo('qs1','qs2_workplace',{type:'workplace'},'18%')"><span class="qcircle"></span>Workplace or employment</button>
        <button class="qbtn" onclick="qGo('qs1','qs2_business',{type:'business'},'18%')"><span class="qcircle"></span>Business or commercial</button>
        <button class="qbtn" onclick="qGo('qs1','qs2_estate',{type:'estate'},'18%')"><span class="qcircle"></span>Estate or inheritance</button>
        <button class="qbtn" onclick="qGo('qs1','qs2_other',{type:'other'},'18%')"><span class="qcircle"></span>Something else</button>
      </div>
    </div>
    <!-- Q2 branches by type -->
    <div class="qstep" id="qs2_property" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; Where are things at with property?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_property','qs3',{stage:'not_started'},'28%')"><span class="qcircle"></span>We haven&rsquo;t started dividing anything yet</button>
        <button class="qbtn" onclick="qGo('qs2_property','qs3',{stage:'talking'},'28%')"><span class="qcircle"></span>We&rsquo;ve been talking but can&rsquo;t quite agree</button>
        <button class="qbtn" onclick="qGo('qs2_property','qs3',{stage:'stalled'},'28%')"><span class="qcircle"></span>Talks have stalled or broken down</button>
        <button class="qbtn" onclick="qGo('qs2_property','qs3',{stage:'lawyers'},'28%')"><span class="qcircle"></span>Lawyers or solicitors are now involved</button>
        <button class="qbtn" onclick="qGo('qs2_property','qs3',{stage:'court'},'28%')"><span class="qcircle"></span>Court proceedings have started</button>
        <button class="qbtn" onclick="qGo('qs2_property','qs3',{stage:'unsure'},'28%')"><span class="qcircle"></span>I&rsquo;m not sure where we stand</button>
      </div>
      <button class="qback" onclick="qBack('qs2_property','qs1','8%')">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_parenting" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; What does the parenting situation look like?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_parenting','qs3',{stage:'informal'},'28%')"><span class="qcircle"></span>Nothing is formalised &mdash; we&rsquo;re working it out informally</button>
        <button class="qbtn" onclick="qGo('qs2_parenting','qs3',{stage:'formalise'},'28%')"><span class="qcircle"></span>We have an arrangement we want to make legally binding</button>
        <button class="qbtn" onclick="qGo('qs2_parenting','qs3',{stage:'broken_arr'},'28%')"><span class="qcircle"></span>An arrangement exists but it&rsquo;s breaking down</button>
        <button class="qbtn" onclick="qGo('qs2_parenting','qs3',{stage:'vary_orders'},'28%')"><span class="qcircle"></span>We need to change or update existing court orders</button>
        <button class="qbtn" onclick="qGo('qs2_parenting','qs3',{stage:'contested'},'28%')"><span class="qcircle"></span>The other parent and I strongly disagree on arrangements</button>
        <button class="qbtn" onclick="qGo('qs2_parenting','qs3',{stage:'safety_concern'},'28%')"><span class="qcircle"></span>Safety or family violence concerns are involved</button>
      </div>
      <button class="qback" onclick="qBack('qs2_parenting','qs1','8%')">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_both" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; Which is more pressing right now?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_both','qs3',{stage:'parenting_first'},'28%')"><span class="qcircle"></span>Sorting out the children&rsquo;s arrangements</button>
        <button class="qbtn" onclick="qGo('qs2_both','qs3',{stage:'property_first'},'28%')"><span class="qcircle"></span>Dividing property and finances</button>
        <button class="qbtn" onclick="qGo('qs2_both','qs3',{stage:'equal'},'28%')"><span class="qcircle"></span>Both are equally urgent</button>
        <button class="qbtn" onclick="qGo('qs2_both','qs3',{stage:'guidance'},'28%')"><span class="qcircle"></span>I need guidance on where to start</button>
        <button class="qbtn" onclick="qGo('qs2_both','qs3',{stage:'stalled'},'28%')"><span class="qcircle"></span>Talks on both have stalled</button>
        <button class="qbtn" onclick="qGo('qs2_both','qs3',{stage:'court'},'28%')"><span class="qcircle"></span>One or both issues are before the court</button>
      </div>
      <button class="qback" onclick="qBack('qs2_both','qs1','8%')">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_workplace" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; What type of workplace matter is this?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_workplace','qs3',{stage:'unfair_dismiss'},'28%')"><span class="qcircle"></span>Unfair dismissal or termination</button>
        <button class="qbtn" onclick="qGo('qs2_workplace','qs3',{stage:'harassment'},'28%')"><span class="qcircle"></span>Workplace harassment or bullying</button>
        <button class="qbtn" onclick="qGo('qs2_workplace','qs3',{stage:'colleague'},'28%')"><span class="qcircle"></span>Ongoing conflict with a colleague or manager</button>
        <button class="qbtn" onclick="qGo('qs2_workplace','qs3',{stage:'contract'},'28%')"><span class="qcircle"></span>Pay, contract or entitlements dispute</button>
        <button class="qbtn" onclick="qGo('qs2_workplace','qs3',{stage:'urgent'},'28%')"><span class="qcircle"></span>Time limits are approaching (e.g. 21-day Fair Work deadline)</button>
        <button class="qbtn" onclick="qGo('qs2_workplace','qs3',{stage:'general_wp'},'28%')"><span class="qcircle"></span>General workplace tension or breakdown</button>
      </div>
      <button class="qback" onclick="qBack('qs2_workplace','qs1','8%')">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_business" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; What type of business dispute is this?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_business','qs3',{stage:'partner'},'28%')"><span class="qcircle"></span>Partnership or director dispute</button>
        <button class="qbtn" onclick="qGo('qs2_business','qs3',{stage:'contract_b'},'28%')"><span class="qcircle"></span>Contract or supplier dispute</button>
        <button class="qbtn" onclick="qGo('qs2_business','qs3',{stage:'customer'},'28%')"><span class="qcircle"></span>Customer or client dispute</button>
        <button class="qbtn" onclick="qGo('qs2_business','qs3',{stage:'ip'},'28%')"><span class="qcircle"></span>IP, trade secrets or confidentiality</button>
        <button class="qbtn" onclick="qGo('qs2_business','qs3',{stage:'wind_up'},'28%')"><span class="qcircle"></span>Business exit, buyout or wind-up</button>
        <button class="qbtn" onclick="qGo('qs2_business','qs3',{stage:'other_b'},'28%')"><span class="qcircle"></span>Other commercial matter</button>
      </div>
      <button class="qback" onclick="qBack('qs2_business','qs1','8%')">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_estate" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; What is the estate dispute about?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_estate','qs3',{stage:'will_contest'},'28%')"><span class="qcircle"></span>Contesting the validity of a will</button>
        <button class="qbtn" onclick="qGo('qs2_estate','qs3',{stage:'family_provision'},'28%')"><span class="qcircle"></span>Family Provision claim (inadequate share)</button>
        <button class="qbtn" onclick="qGo('qs2_estate','qs3',{stage:'executor'},'28%')"><span class="qcircle"></span>Dispute with the executor or trustee</button>
        <button class="qbtn" onclick="qGo('qs2_estate','qs3',{stage:'beneficiary'},'28%')"><span class="qcircle"></span>Conflict between beneficiaries</button>
        <button class="qbtn" onclick="qGo('qs2_estate','qs3',{stage:'asset_val'},'28%')"><span class="qcircle"></span>Asset valuation or distribution disagreement</button>
        <button class="qbtn" onclick="qGo('qs2_estate','qs3',{stage:'other_e'},'28%')"><span class="qcircle"></span>Other estate or succession matter</button>
      </div>
      <button class="qback" onclick="qBack('qs2_estate','qs1','8%')">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_other" hidden>
      <p class="qlabel">Step 2 of 9 &mdash; Can you describe the situation a little?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs2_other','qs3',{stage:'neighbour'},'28%')"><span class="qcircle"></span>Neighbour or property boundary dispute</button>
        <button class="qbtn" onclick="qGo('qs2_other','qs3',{stage:'strata'},'28%')"><span class="qcircle"></span>Strata or body corporate matter</button>
        <button class="qbtn" onclick="qGo('qs2_other','qs3',{stage:'consumer'},'28%')"><span class="qcircle"></span>Consumer or service provider dispute</button>
        <button class="qbtn" onclick="qGo('qs2_other','qs3',{stage:'community'},'28%')"><span class="qcircle"></span>Community or organisation conflict</button>
        <button class="qbtn" onclick="qGo('qs2_other','qs3',{stage:'family_other'},'28%')"><span class="qcircle"></span>Family conflict (not separation-related)</button>
        <button class="qbtn" onclick="qGo('qs2_other','qs3',{stage:'unsure_other'},'28%')"><span class="qcircle"></span>I&rsquo;m not sure how to describe it</button>
      </div>
      <button class="qback" onclick="qBack('qs2_other','qs1','8%')">&#8592; Back</button>
    </div>
    <!-- Q3: Barriers (multi-select) -->
    <div class="qstep" id="qs3" hidden>
      <p class="qlabel">Step 3 of 9 &mdash; What concerns you most? <span style="font-weight:400;opacity:.65">(select all that apply)</span></p>
      <div class="qopts qmulti" id="qs3opts">
        <label class="qcheck"><input type="checkbox" value="cost"><span class="qcircle"></span>The cost of the process</label>
        <label class="qcheck"><input type="checkbox" value="time"><span class="qcircle"></span>How long it might take</label>
        <label class="qcheck"><input type="checkbox" value="other_agree"><span class="qcircle"></span>The other party won&rsquo;t agree to participate</label>
        <label class="qcheck"><input type="checkbox" value="power"><span class="qcircle"></span>There&rsquo;s a power imbalance between us</label>
        <label class="qcheck"><input type="checkbox" value="trust"><span class="qcircle"></span>I don&rsquo;t trust the other party to be honest</label>
        <label class="qcheck"><input type="checkbox" value="emotion"><span class="qcircle"></span>Emotions are too raw right now</label>
        <label class="qcheck"><input type="checkbox" value="outcome"><span class="qcircle"></span>I&rsquo;m not sure mediation can resolve our specific issues</label>
        <label class="qcheck"><input type="checkbox" value="none_concerns"><span class="qcircle"></span>None of the above &mdash; I&rsquo;m open to it</label>
      </div>
      <button class="qcontinue" id="qs3cont" onclick="qMultiNext('qs3','barriers','qs4',{prog:'38%'})" disabled>Continue &#8594;</button>
      <button class="qback" onclick="qBackFromMulti('qs3','qs2')">&#8592; Back</button>
    </div>
    <!-- Q4: Issues by type (multi-select) -->
    <div class="qstep" id="qs4" hidden>
      <p class="qlabel">Step 4 of 9 &mdash; What specifically needs to be resolved? <span style="font-weight:400;opacity:.65">(select all that apply)</span></p>
      <div class="qopts qmulti" id="qs4opts"></div>
      <button class="qcontinue" id="qs4cont" onclick="qMultiNext('qs4','issues','qs5',{prog:'48%'})" disabled>Continue &#8594;</button>
      <button class="qback" onclick="qBackFromMulti('qs4','qs3')">&#8592; Back</button>
    </div>
    <!-- Q5: Distance from agreement -->
    <div class="qstep" id="qs5" hidden>
      <p class="qlabel">Step 5 of 9 &mdash; How far apart are you from an agreement?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs5','qs6',{distance:'close'},'58%')"><span class="qcircle"></span>Very close &mdash; just a few details to work out</button>
        <button class="qbtn" onclick="qGo('qs5','qs6',{distance:'some'},'58%')"><span class="qcircle"></span>Some gaps, but we&rsquo;re not far off</button>
        <button class="qbtn" onclick="qGo('qs5','qs6',{distance:'moderate'},'58%')"><span class="qcircle"></span>Moderate distance &mdash; we disagree on several things</button>
        <button class="qbtn" onclick="qGo('qs5','qs6',{distance:'far'},'58%')"><span class="qcircle"></span>We&rsquo;re far apart &mdash; positions seem entrenched</button>
        <button class="qbtn" onclick="qGo('qs5','qs6',{distance:'unknown'},'58%')"><span class="qcircle"></span>I genuinely don&rsquo;t know</button>
      </div>
      <button class="qback" onclick="qBack('qs5','qs4','48%')">&#8592; Back</button>
    </div>
    <!-- Q6: Other party engagement -->
    <div class="qstep" id="qs6" hidden>
      <p class="qlabel">Step 6 of 9 &mdash; How do you think the other party would respond to mediation?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs6','qs7',{engagement:'keen'},'66%')"><span class="qcircle"></span>They&rsquo;d likely be open to it</button>
        <button class="qbtn" onclick="qGo('qs6','qs7',{engagement:'uncertain'},'66%')"><span class="qcircle"></span>Not sure &mdash; we haven&rsquo;t discussed it</button>
        <button class="qbtn" onclick="qGo('qs6','qs7',{engagement:'reluctant'},'66%')"><span class="qcircle"></span>Probably reluctant but might agree</button>
        <button class="qbtn" onclick="qGo('qs6','qs7',{engagement:'resistant'},'66%')"><span class="qcircle"></span>They&rsquo;ve resisted any discussion so far</button>
        <button class="qbtn" onclick="qGo('qs6','qs7',{engagement:'hostile'},'66%')"><span class="qcircle"></span>They&rsquo;re hostile &mdash; I don&rsquo;t think they&rsquo;ll engage</button>
        <button class="qbtn" onclick="qGo('qs6','qs7',{engagement:'no_contact'},'66%')"><span class="qcircle"></span>We have no direct contact with each other</button>
      </div>
      <button class="qback" onclick="qBack('qs6','qs5','58%')">&#8592; Back</button>
    </div>
    <!-- Q7: Ability to negotiate freely (safety signal) -->
    <div class="qstep" id="qs7" hidden>
      <p class="qlabel">Step 7 of 9 &mdash; In your situation, do you feel you&rsquo;d be able to speak up and negotiate freely?</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs7','qs8',{negotiate:'yes'},'74%')"><span class="qcircle"></span>Yes &mdash; I&rsquo;d feel comfortable speaking up</button>
        <button class="qbtn" onclick="qGo('qs7','qs8',{negotiate:'mostly'},'74%')"><span class="qcircle"></span>Mostly &mdash; there are some dynamics I&rsquo;d need support with</button>
        <button class="qbtn" onclick="qGo('qs7','qs8',{negotiate:'unsure'},'74%')"><span class="qcircle"></span>I&rsquo;m not sure</button>
        <button class="qbtn" onclick="qGo('qs7','qs8',{negotiate:'no'},'74%')"><span class="qcircle"></span>No &mdash; I&rsquo;d feel pressured or silenced</button>
        <button class="qbtn" onclick="qGo('qs7','qs8',{negotiate:'private'},'74%')"><span class="qcircle"></span>I&rsquo;d prefer not to say</button>
      </div>
      <button class="qback" onclick="qBack('qs7','qs6','66%')">&#8592; Back</button>
    </div>
    <!-- Q8: Safety concern (critical) -->
    <div class="qstep" id="qs8" hidden>
      <p class="qlabel">Step 8 of 9 &mdash; Are there any safety concerns in your situation?</p>
      <p style="font-size:.8rem;color:rgba(216,234,217,.5);margin:-4px 0 12px;line-height:1.5">Your answer is confidential and helps us recommend the right process.</p>
      <div class="qopts">
        <button class="qbtn" onclick="qGo('qs8','qs9',{safety:'no'},'82%')"><span class="qcircle"></span>No &mdash; there are no safety concerns</button>
        <button class="qbtn" onclick="qGo('qs8','qs9',{safety:'unsure'},'82%')"><span class="qcircle"></span>I&rsquo;m not sure &mdash; the situation has been difficult</button>
        <button class="qbtn" onclick="qGo('qs8','qs9',{safety:'yes'},'82%')"><span class="qcircle"></span>Yes &mdash; there are safety or family violence concerns</button>
        <button class="qbtn" onclick="qGo('qs8','qs9',{safety:'private'},'82%')"><span class="qcircle"></span>I&rsquo;d prefer not to say</button>
      </div>
      <button class="qback" onclick="qBack('qs8','qs7','74%')">&#8592; Back</button>
    </div>
    <!-- Q9: Desired outcomes (multi-select, some conditional) -->
    <div class="qstep" id="qs9" hidden>
      <p class="qlabel">Step 9 of 9 &mdash; What matters most to you in how this is resolved? <span style="font-weight:400;opacity:.65">(select all that apply)</span></p>
      <div class="qopts qmulti" id="qs9opts">
        <label class="qcheck"><input type="checkbox" value="quick"><span class="qcircle"></span>A quick resolution</label>
        <label class="qcheck"><input type="checkbox" value="affordable"><span class="qcircle"></span>Keeping costs manageable</label>
        <label class="qcheck"><input type="checkbox" value="private"><span class="qcircle"></span>Keeping it private and out of court</label>
        <label class="qcheck"><input type="checkbox" value="control"><span class="qcircle"></span>Having control over the outcome</label>
        <label class="qcheck qfamily" value="kids_wellbeing"><input type="checkbox" value="kids"><span class="qcircle"></span>Protecting the children&rsquo;s wellbeing</label>
        <label class="qcheck qfamily" value="coparent"><input type="checkbox" value="coparent"><span class="qcircle"></span>Maintaining a workable co-parenting relationship</label>
        <label class="qcheck"><input type="checkbox" value="relationship"><span class="qcircle"></span>Preserving the relationship where possible</label>
        <label class="qcheck"><input type="checkbox" value="fair"><span class="qcircle"></span>A fair outcome for everyone</label>
      </div>
      <button class="qcontinue" id="qs9cont" onclick="qFinish()" disabled>See my result &#8594;</button>
      <button class="qback" onclick="qBackFromMulti('qs9','qs8')">&#8592; Back</button>
    </div>
    <!-- Result -->
    <div class="qstep" id="qresult" hidden>
      <div id="qbadge"></div>
      <p id="qverdict" style="font-family:var(--body-serif);font-size:1.15rem;line-height:1.35;margin:0 0 10px;color:var(--cream)"></p>
      <p id="qnote" style="font-size:.86rem;line-height:1.65;color:rgba(216,234,217,.72);margin:0 0 16px"></p>
      <div id="qbullets" style="display:grid;gap:9px;padding:15px 17px;background:rgba(168,200,159,.08);border:1px solid rgba(168,200,159,.18);border-radius:12px;margin-bottom:20px"></div>
      <a href="/contact-us/" class="btn btn-primary" style="width:100%;text-align:center;justify-content:center;display:flex;padding:14px 20px;font-size:.95rem">Book a free consultation <span class="arr">&#8594;</span></a>
      <button class="qback" onclick="qReset()" style="width:100%;text-align:center;margin-top:10px">&#8592; Start again</button>
      <p style="font-size:.72rem;color:rgba(216,234,217,.32);margin:12px 0 0;line-height:1.5;text-align:center">General guidance only &mdash; not legal advice. If safety is a concern, call 1800RESPECT (1800 737 732).</p>
    </div>
  </div>
</div>
<style>
.qprogress{height:3px;background:rgba(168,200,159,.15);border-radius:999px;margin-bottom:22px;overflow:hidden}
.qprogress-fill{height:100%;background:linear-gradient(90deg,#4a9e6a,#a8c89f);border-radius:999px;transition:width .4s cubic-bezier(.4,0,.2,1)}
#quiz60 .qlabel{display:flex;align-items:center;gap:8px;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:rgba(216,234,217,.5);margin:0 0 14px;font-family:var(--sans);line-height:1.4;flex-wrap:wrap}
#quiz60 .qopts{display:grid;gap:7px}
#quiz60 .qbtn{display:flex;align-items:center;gap:12px;text-align:left;border:1px solid rgba(168,200,159,.18);background:rgba(168,200,159,.04);padding:11px 15px;border-radius:11px;font-size:.88rem;color:rgba(247,250,247,.82);cursor:pointer;transition:background .16s,border-color .16s,transform .16s,color .16s;font-family:var(--sans);line-height:1.4;width:100%}
#quiz60 .qbtn:hover{background:rgba(168,200,159,.13);border-color:rgba(168,200,159,.5);color:var(--cream);transform:translateX(3px)}
#quiz60 .qbtn:active{background:rgba(168,200,159,.22);transform:translateX(3px) scale(.98)}
.qcircle{width:15px;height:15px;border-radius:50%;border:1.5px solid rgba(168,200,159,.35);flex-shrink:0;transition:border-color .16s,background .16s}
#quiz60 .qbtn:hover .qcircle{border-color:#a8c89f;background:rgba(168,200,159,.25)}
#quiz60 .qback{margin-top:13px;background:none;border:none;color:rgba(216,234,217,.4);font-size:.8rem;cursor:pointer;padding:0;font-family:var(--sans);transition:color .15s;display:block}
#quiz60 .qback:hover{color:rgba(216,234,217,.85)}
#qbadge{display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em}
.qmulti{display:grid;gap:7px}
.qcheck{display:flex;align-items:center;gap:12px;border:1px solid rgba(168,200,159,.18);background:rgba(168,200,159,.04);padding:11px 15px;border-radius:11px;font-size:.88rem;color:rgba(247,250,247,.82);cursor:pointer;transition:background .16s,border-color .16s;font-family:var(--sans);line-height:1.4}
.qcheck input[type=checkbox]{display:none}
.qcheck:hover{background:rgba(168,200,159,.1);border-color:rgba(168,200,159,.4);color:var(--cream)}
.qcheck.qsel{background:rgba(168,200,159,.16);border-color:rgba(168,200,159,.6);color:var(--cream)}
.qcheck.qsel .qcircle{background:#4a9e6a;border-color:#4a9e6a}
.qcontinue{margin-top:14px;width:100%;padding:12px 18px;background:rgba(168,200,159,.15);border:1px solid rgba(168,200,159,.4);color:var(--cream);border-radius:11px;font-size:.9rem;font-family:var(--sans);cursor:pointer;transition:background .16s,border-color .16s;text-align:center}
.qcontinue:not(:disabled):hover{background:rgba(168,200,159,.28);border-color:rgba(168,200,159,.7)}
.qcontinue:disabled{opacity:.35;cursor:not-allowed}
#qmintro .qstartbtn:hover,#qstartbtn:hover{background:rgba(168,200,159,.22)!important;border-color:rgba(168,200,159,.6)!important}
@keyframes qfade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
#quiz60 .qstep:not([hidden]){animation:qfade .24s ease both}
@media(max-width:900px){#hero-check{order:-1}}
</style>
<script>
var _qd={type:null,stage:null,barriers:[],issues:[],distance:null,engagement:null,negotiate:null,safety:null,outcomes:[]};
var _qhist=[];
var _BG='display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em;background:rgba(168,200,159,.14);border:1px solid rgba(168,200,159,.32);color:#a8c89f';
var _BY='display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em;background:rgba(240,165,0,.15);border:1px solid rgba(240,165,0,.3);color:#f5c347';
var _BR='display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em;background:rgba(200,100,80,.14);border:1px solid rgba(200,100,80,.32);color:#e8957a';
var _IC='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
var _IH='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>';
var _IW='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
var _IS='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>';
var _Q4OPTS={
  property:['Family home — sale, transfer or who keeps it','Superannuation splitting','Savings, investments or bank accounts','Business assets or partnership share','Investment properties','Trusts or family company interests','Debts and liabilities'],
  parenting:['Day-to-day living arrangements (time with each parent)','School holidays and special occasions','Decision-making (health, education, religion)','Relocation or moving interstate','Child support arrangements','Formalising as a parenting plan or consent orders','Handover and communication protocols'],
  both:['Family home or property','Superannuation and finances','Children\\u2019s living arrangements','Parenting decision-making','Debt and liabilities','Formalising agreements as consent orders'],
  workplace:['Unfair dismissal or redundancy terms','Workplace harassment or bullying','Performance management dispute','Pay, entitlements or leave','Return to work or modified duties','Working relationship breakdown'],
  business:['Profit sharing or financial distributions','Ownership stakes or shareholder rights','Business direction or strategy','Contracts, IP or confidentiality','Exit terms or buyout price','Liability or debt allocation'],
  estate:['Distribution of assets from the estate','Family Provision claim (inadequate share)','Executor conduct or decisions','Property valuations','Debts owed to or by the estate','Care arrangements or promises made before death'],
  other:['Financial matters','Relationship or communication issues','Use of shared property or space','Responsibilities or obligations','Other specific concerns']
};
function _qprog(w){document.getElementById('qpfill').style.width=w;}
function _qbadge(st,ic,lbl){var b=document.getElementById('qbadge');b.style.cssText=st;b.innerHTML=ic+' '+lbl;}
function _qset(vt,nt,bl){
  document.getElementById('qverdict').textContent=vt;
  document.getElementById('qnote').textContent=nt;
  document.getElementById('qbullets').innerHTML=bl.map(function(b){return'<div style="display:flex;gap:10px;font-size:.84rem;color:rgba(216,234,217,.88);line-height:1.5"><span style="color:#a8c89f;flex-shrink:0;margin-top:2px">'+_IC+'</span><span>'+b+'</span></div>';}).join('');
}
function _qshow(id){document.getElementById(id).hidden=false;}
function _qhide(id){document.getElementById(id).hidden=true;}
function qStart(){
  document.getElementById('qmintro').style.display='none';
  document.getElementById('qprogbar').style.display='block';
  document.getElementById('quiz60').style.display='block';
  _qprog('8%');
}
function qGo(from,to,data,prog){
  Object.assign(_qd,data);
  _qhist.push({id:from,prog:prog});
  _qhide(from);
  if(to==='qs4'){_qBuildQ4();}
  if(to==='qs9'){_qBuildQ9();}
  _qshow(to);
  _qprog(prog);
  document.getElementById('hero-check').scrollIntoView({behavior:'smooth',block:'nearest'});
}
function qBack(from,to,prog){
  _qhide(from);
  _qshow(to);
  _qprog(prog);
}
function qBackFromMulti(from,toPrefix){
  _qhide(from);
  var target=toPrefix==='qs2'?'qs2_'+_qd.type:toPrefix;
  _qshow(target);
  var prevProg=from==='qs3'?'18%':from==='qs4'?'28%':from==='qs9'?'82%':'38%';
  _qprog(prevProg);
}
function _qMultiToggle(el,contId){
  el.classList.toggle('qsel');
  var cont=document.getElementById(contId);
  var any=el.closest('.qopts').querySelectorAll('.qcheck.qsel').length>0;
  cont.disabled=!any;
}
function _qSetupMulti(optsId,contId){
  document.getElementById(optsId).querySelectorAll('.qcheck').forEach(function(el){
    el.onclick=function(){_qMultiToggle(el,contId);};
  });
}
function qMultiNext(stepId,field,to,opts){
  var vals=[];
  document.getElementById(stepId+'opts').querySelectorAll('.qcheck.qsel').forEach(function(el){
    var v=el.querySelector('input[type=checkbox]').value;
    vals.push(v);
  });
  _qd[field]=vals;
  _qhide(stepId);
  if(to==='qs4'){_qBuildQ4();}
  if(to==='qs9'){_qBuildQ9();}
  _qshow(to);
  _qprog(opts.prog);
}
function _qBuildQ4(){
  var type=_qd.type||'other';
  var items=_Q4OPTS[type]||_Q4OPTS.other;
  var html=items.map(function(lbl,i){return'<label class="qcheck"><input type="checkbox" value="opt'+i+'"><span class="qcircle"></span>'+lbl+'</label>';}).join('');
  document.getElementById('qs4opts').innerHTML=html;
  _qSetupMulti('qs4','qs4cont');
}
function _qBuildQ9(){
  var isFamily=(_qd.type==='parenting'||_qd.type==='both');
  document.getElementById('qs9opts').querySelectorAll('.qfamily').forEach(function(el){
    el.style.display=isFamily?'':'none';
  });
  _qSetupMulti('qs9','qs9cont');
}
function qFinish(){
  var vals=[];
  document.getElementById('qs9opts').querySelectorAll('.qcheck.qsel').forEach(function(el){
    vals.push(el.querySelector('input').value);
  });
  _qd.outcomes=vals;
  _qhide('qs9');
  _qShowResult();
}
function _qCompute(){
  var d=_qd;
  if(d.safety==='yes'||d.safety==='unsure'||d.safety==='private'||d.negotiate==='no'){return'assessment_first';}
  if(d.type==='workplace'&&d.stage==='urgent'){return'urgent_or_specialist';}
  var challenges=0;
  if(d.negotiate==='mostly'||d.negotiate==='unsure'){challenges+=1;}
  if(d.engagement==='hostile'||d.engagement==='resistant'){challenges+=1;}
  if(d.distance==='far'){challenges+=1;}
  if(d.barriers.indexOf('power')>-1){challenges+=1;}
  if(challenges>=2){return'promising_with_challenges';}
  return'explore';
}
function _qShowResult(){
  var cat=_qCompute(),vt,nt,bl;
  _qprog('100%');
  if(cat==='assessment_first'){
    _qbadge(_BR,_IS,'A conversation first is advisable');
    vt='Your situation calls for a careful first step.';
    nt='Some of what you\\'ve described suggests it would help to speak with one of our mediators before committing to any process. We can assess what approach will work best for you, in complete confidence.';
    bl=['Free and completely confidential initial consultation.','We screen for safety concerns before any joint process begins.','Shuttle mediation (separate rooms, no direct contact) available where needed.','If mediation isn\\'t appropriate, we\\'ll tell you honestly and point you toward better options.'];
  }else if(cat==='urgent_or_specialist'){
    _qbadge(_BY,_IW,'Act quickly — time limits may apply');
    vt='Fair Work time limits are strict — early advice matters.';
    nt='Unfair dismissal and general protections applications must typically be lodged within 21 days of dismissal. Mediation at this stage can resolve matters before a formal hearing — faster and with far less cost.';
    bl=['Same-week appointments available for urgent Fair Work matters.','Mediation prevents costly tribunal proceedings in most cases.','Confidential assessment at no obligation.','We work alongside your legal advisers where needed.'];
  }else if(cat==='promising_with_challenges'){
    _qbadge(_BG,_IH,'Mediation is worth exploring');
    vt='Mediation can work here — the dynamics are worth discussing first.';
    nt='Some of what you\\'ve described suggests mediation may face challenges, but that doesn\\'t mean it can\\'t work. Our mediators are trained to manage power imbalances, entrenched positions, and reluctant parties. A brief consultation will help us assess the best approach.';
    if(_qd.type==='property'||_qd.type==='both'){
      bl=['Even difficult negotiations usually settle before reaching court.','Shuttle mediation (separate rooms) is available if face-to-face isn\\'t workable.','Your solicitor can review any agreement before you sign.','Fixed fee — no billing surprises.'];
    }else if(_qd.type==='parenting'){
      bl=['Shuttle mediation available — no direct contact required.','Safety screening completed before any joint process begins.','Section 60I certificate issued — required for consent order applications.','Child-focused process with full confidentiality protections.'];
    }else{
      bl=['Our mediators manage high-conflict and reluctant-party situations regularly.','Completely confidential — nothing leaves the mediation room.','A free consultation helps us design the right approach for your situation.','If mediation isn\\'t right, we\\'ll say so honestly.'];
    }
  }else{
    _qbadge(_BG,_IC,'Mediation looks well suited to your situation');
    vt='Based on what you\\'ve shared, mediation is likely a strong path forward.';
    nt='Your situation has many of the factors that make mediation work well — and resolve quickly. Most matters like yours reach a resolution in one or two sessions, at a fraction of the cost of court.';
    if(_qd.type==='property'){
      bl=['Property settlements typically reached in a single day.','Agreement formalised as legally binding consent orders.','Fixed fee quoted in writing — no surprises.','No lawyers required in the room if you prefer.'];
    }else if(_qd.type==='parenting'){
      bl=['Parenting plan formalised as consent orders.','Section 60I certificate issued — required for court applications.','Child-centred process, fully confidential.','Most parenting matters resolve in a single session.'];
    }else if(_qd.type==='both'){
      bl=['Both property and parenting handled in one cohesive process.','Section 60I certificate issued and consent orders prepared.','One mediator, one process — more efficient, less stressful.','Fixed fee covers both issues.'];
    }else if(_qd.type==='workplace'){
      bl=['Completely confidential — nothing leaves the mediation room.','Preserves the employment relationship where possible.','Faster and far less costly than Fair Work or tribunal.','Most workplace disputes settle in a single session.'];
    }else if(_qd.type==='business'){
      bl=['Commercially sensitive — everything remains private.','Binding agreement enforceable as a contract.','Typically resolved in one to two sessions.','A fraction of the cost of commercial litigation.'];
    }else if(_qd.type==='estate'){
      bl=['Suitable for contested wills, Family Provision claims and executor disputes.','Agreement reached before legal costs deplete the estate.','Family matters stay within the family — fully confidential.','Typically resolved in one to two sessions.'];
    }else{
      bl=['Free confidential consultation — no obligation.','Wide range of dispute types within our scope.','If mediation isn\\'t the right fit, we\\'ll say so honestly and point you toward better options.'];
    }
  }
  _qset(vt,nt,bl);
  _qshow('qresult');
  document.getElementById('hero-check').scrollIntoView({behavior:'smooth',block:'nearest'});
}
function qReset(){
  _qd={type:null,stage:null,barriers:[],issues:[],distance:null,engagement:null,negotiate:null,safety:null,outcomes:[]};
  _qhist=[];
  ['qs2_property','qs2_parenting','qs2_both','qs2_workplace','qs2_business','qs2_estate','qs2_other','qs3','qs4','qs5','qs6','qs7','qs8','qs9','qresult'].forEach(function(id){_qhide(id);});
  _qshow('qs1');
  _qprog('8%');
  document.getElementById('qmintro').style.display='none';
  document.getElementById('qprogbar').style.display='block';
  document.getElementById('quiz60').style.display='block';
}
document.addEventListener('DOMContentLoaded',function(){
  _qSetupMulti('qs3','qs3cont');
});
</script>"""


def service_hero_with_quiz(eyebrow, h1, lede, crumb_items):
    """Two-column service hero: left=H1+lede+CTAs (left-aligned), right=quiz card."""
    crumb = crumb_html(crumb_items)
    return f"""{crumb}
<section class="phero" style="padding-bottom:clamp(48px,6vw,80px)">
  <div class="phero-blob"></div>
  <div class="wrap hero-quiz-grid" style="display:grid;grid-template-columns:1fr 400px;gap:clamp(32px,5vw,64px);align-items:start">
    <div>
      <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      <div class="phero-cta">
        <a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">&#8594;</span></a>
        <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
      </div>
    </div>
    {quiz_card()}
  </div>
</section>"""

print("templates module ready")
