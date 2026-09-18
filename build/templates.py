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
    """Return the self-contained 60-second fit-check quiz card HTML+CSS+JS."""
    return """<div id="hero-check" style="background:var(--sage-deep);color:var(--cream);border-radius:22px;padding:clamp(24px,3vw,34px);box-shadow:0 4px 32px rgba(13,34,24,.18)">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px">
    <span style="font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:#a8c89f;font-weight:500">Free 60-second check</span>
  </div>
  <p style="font-family:var(--body-serif);font-size:clamp(1.1rem,2vw,1.35rem);font-weight:400;color:var(--cream);margin:0 0 20px;line-height:1.3">Will mediation work<br>for my situation?</p>
  <div class="qprogress" aria-hidden="true"><div class="qprogress-fill" id="qpfill" style="width:25%"></div></div>
  <div id="quiz60">
    <div class="qstep" id="qs1">
      <p class="qlabel"><span class="qdots"><span class="qdot qd-on"></span><span class="qdot"></span><span class="qdot"></span><span class="qdot"></span></span>What needs to be sorted out?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60cat('property')"><span class="qcircle"></span>Property &amp; finances</button>
        <button class="qbtn" onclick="q60cat('parenting')"><span class="qcircle"></span>Parenting &amp; children</button>
        <button class="qbtn" onclick="q60cat('both')"><span class="qcircle"></span>Both &mdash; property and parenting</button>
        <button class="qbtn" onclick="q60cat('other')"><span class="qcircle"></span>Workplace, business or estate</button>
      </div>
    </div>
    <div class="qstep" id="qs2_property" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span><span class="qdot"></span></span>Where are things at?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s2('fresh')"><span class="qcircle"></span>We haven&rsquo;t started dividing anything yet</button>
        <button class="qbtn" onclick="q60s2('stalled')"><span class="qcircle"></span>We&rsquo;ve talked but can&rsquo;t reach agreement</button>
        <button class="qbtn" onclick="q60s2('solicitors')"><span class="qcircle"></span>Solicitors are involved or exchanging letters</button>
        <button class="qbtn" onclick="q60s2('court')"><span class="qcircle"></span>Court proceedings have already started</button>
      </div>
      <button class="qback" onclick="q60s2back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_parenting" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span><span class="qdot"></span></span>What does the parenting situation look like?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s2('informal')"><span class="qcircle"></span>Nothing is formalised &mdash; we&rsquo;re working it out</button>
        <button class="qbtn" onclick="q60s2('broken')"><span class="qcircle"></span>An arrangement exists but it&rsquo;s not working</button>
        <button class="qbtn" onclick="q60s2('formalise')"><span class="qcircle"></span>We want to make our plan legally binding</button>
        <button class="qbtn" onclick="q60s2('orders')"><span class="qcircle"></span>One of us wants to change existing court orders</button>
      </div>
      <button class="qback" onclick="q60s2back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_both" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span><span class="qdot"></span></span>Which is the more pressing need right now?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s2('parenting_first')"><span class="qcircle"></span>Sorting out the children&rsquo;s arrangements</button>
        <button class="qbtn" onclick="q60s2('property_first')"><span class="qcircle"></span>Dividing the property and finances</button>
        <button class="qbtn" onclick="q60s2('equal')"><span class="qcircle"></span>Both are equally urgent</button>
        <button class="qbtn" onclick="q60s2('guidance')"><span class="qcircle"></span>I need guidance on where to start</button>
      </div>
      <button class="qback" onclick="q60s2back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs2_other" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span><span class="qdot"></span></span>What type of dispute is it?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s2('workplace')"><span class="qcircle"></span>Workplace or employment</button>
        <button class="qbtn" onclick="q60s2('business')"><span class="qcircle"></span>Business or commercial</button>
        <button class="qbtn" onclick="q60s2('estate')"><span class="qcircle"></span>Estate or inheritance</button>
        <button class="qbtn" onclick="q60s2('else')"><span class="qcircle"></span>Something else</button>
      </div>
      <button class="qback" onclick="q60s2back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs3_property" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span></span>What&rsquo;s the main asset involved?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s3('home')"><span class="qcircle"></span>The family home &mdash; who keeps it or how to sell</button>
        <button class="qbtn" onclick="q60s3('super')"><span class="qcircle"></span>Superannuation &amp; savings</button>
        <button class="qbtn" onclick="q60s3('complex')"><span class="qcircle"></span>A business, investment property or trust</button>
        <button class="qbtn" onclick="q60s3('general')"><span class="qcircle"></span>Several of the above, or I&rsquo;m not sure</button>
      </div>
      <button class="qback" onclick="q60s3back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs3_parenting" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span></span>How is communication with the other parent?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s3('ok')"><span class="qcircle"></span>We can talk reasonably when we need to</button>
        <button class="qbtn" onclick="q60s3('difficult')"><span class="qcircle"></span>It&rsquo;s difficult but we manage</button>
        <button class="qbtn" onclick="q60s3('broken')"><span class="qcircle"></span>Communication has largely broken down</button>
        <button class="qbtn" onclick="q60s3('nocontact')"><span class="qcircle"></span>We only speak through lawyers or family</button>
      </div>
      <button class="qback" onclick="q60s3back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs3_both" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span></span>Are you currently living separately?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s3('settled')"><span class="qcircle"></span>Yes &mdash; the transition has been relatively calm</button>
        <button class="qbtn" onclick="q60s3('tense')"><span class="qcircle"></span>Yes &mdash; but it&rsquo;s still tense and evolving</button>
        <button class="qbtn" onclick="q60s3('together')"><span class="qcircle"></span>No &mdash; we&rsquo;re still in the same home</button>
        <button class="qbtn" onclick="q60s3('complicated')"><span class="qcircle"></span>It&rsquo;s complicated</button>
      </div>
      <button class="qback" onclick="q60s3back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qs3_other" hidden>
      <p class="qlabel"><span class="qdots"><span class="qdot qd-done"></span><span class="qdot qd-done"></span><span class="qdot qd-on"></span><span class="qdot"></span></span>How urgent is resolution?</p>
      <div class="qopts">
        <button class="qbtn" onclick="q60s3('urgent')"><span class="qcircle"></span>Time limits are approaching (Fair Work, court deadlines)</button>
        <button class="qbtn" onclick="q60s3('serious')"><span class="qcircle"></span>It&rsquo;s serious but not immediately time-critical</button>
        <button class="qbtn" onclick="q60s3('preventive')"><span class="qcircle"></span>We want to resolve it before it escalates</button>
        <button class="qbtn" onclick="q60s3('proceedings')"><span class="qcircle"></span>Formal proceedings have already started</button>
      </div>
      <button class="qback" onclick="q60s3back()">&#8592; Back</button>
    </div>
    <div class="qstep" id="qresult" hidden>
      <div id="qbadge"></div>
      <p id="qverdict" style="font-family:var(--body-serif);font-size:1.2rem;line-height:1.3;margin:0 0 10px;color:var(--cream)"></p>
      <p id="qnote" style="font-size:.87rem;line-height:1.65;color:rgba(216,234,217,.72);margin:0 0 16px"></p>
      <div id="qbullets" style="display:grid;gap:9px;padding:15px 17px;background:rgba(168,200,159,.08);border:1px solid rgba(168,200,159,.18);border-radius:12px;margin-bottom:20px"></div>
      <a href="/contact-us/" class="btn btn-primary" style="width:100%;text-align:center;justify-content:center;display:flex;padding:14px 20px;font-size:.95rem">Book a free consultation <span class="arr">&#8594;</span></a>
      <button class="qback" onclick="q60reset()" style="width:100%;text-align:center;margin-top:10px">&#8592; Start again</button>
    </div>
  </div>
</div>
<style>
.qprogress{height:3px;background:rgba(168,200,159,.15);border-radius:999px;margin-bottom:22px;overflow:hidden}
.qprogress-fill{height:100%;background:linear-gradient(90deg,#4a9e6a,#a8c89f);border-radius:999px;transition:width .4s cubic-bezier(.4,0,.2,1)}
#quiz60 .qlabel{display:flex;align-items:center;gap:10px;font-size:.72rem;letter-spacing:.07em;text-transform:uppercase;color:rgba(216,234,217,.55);margin:0 0 12px;font-family:var(--sans)}
.qdots{display:flex;gap:5px;flex-shrink:0}
.qdot{width:6px;height:6px;border-radius:50%;background:rgba(168,200,159,.25);transition:background .3s,transform .3s}
.qdot.qd-on{background:#a8c89f;transform:scale(1.25)}
.qdot.qd-done{background:rgba(168,200,159,.55)}
#quiz60 .qopts{display:grid;gap:7px}
#quiz60 .qbtn{display:flex;align-items:center;gap:12px;text-align:left;border:1px solid rgba(168,200,159,.18);background:rgba(168,200,159,.04);padding:12px 16px;border-radius:11px;font-size:.92rem;color:rgba(247,250,247,.82);cursor:pointer;transition:background .16s,border-color .16s,transform .16s,color .16s;font-family:var(--sans);line-height:1.4;width:100%}
#quiz60 .qbtn:hover{background:rgba(168,200,159,.13);border-color:rgba(168,200,159,.5);color:var(--cream);transform:translateX(3px)}
#quiz60 .qbtn:active{background:rgba(168,200,159,.22);transform:translateX(3px) scale(.98)}
.qcircle{width:16px;height:16px;border-radius:50%;border:1.5px solid rgba(168,200,159,.35);flex-shrink:0;transition:border-color .16s,background .16s}
#quiz60 .qbtn:hover .qcircle{border-color:#a8c89f;background:rgba(168,200,159,.25)}
#quiz60 .qback{margin-top:13px;background:none;border:none;color:rgba(216,234,217,.4);font-size:.8rem;cursor:pointer;padding:0;font-family:var(--sans);transition:color .15s}
#quiz60 .qback:hover{color:rgba(216,234,217,.85)}
#qbadge{display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em}
@keyframes qfade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
#quiz60 .qstep:not([hidden]){animation:qfade .24s ease both}
@media(max-width:900px){#hero-check{order:-1}}
</style>
<script>
var _q60={t:null,s2:null,s3:null};
var _BG='display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em;background:rgba(168,200,159,.14);border:1px solid rgba(168,200,159,.32);color:#a8c89f';
var _BY='display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:999px;font-size:.74rem;font-weight:600;margin-bottom:14px;letter-spacing:.03em;background:rgba(240,165,0,.15);border:1px solid rgba(240,165,0,.3);color:#f5c347';
var _IC='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
var _IH='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>';
var _IW='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
function _q60prog(w){document.getElementById('qpfill').style.width=w;}
function _q60badge(st,ic,lbl){var b=document.getElementById('qbadge');b.style.cssText=st;b.innerHTML=ic+lbl;}
function _q60set(vt,nt,bl){
  document.getElementById('qverdict').textContent=vt;
  document.getElementById('qnote').textContent=nt;
  document.getElementById('qbullets').innerHTML=bl.map(function(b){return'<div style="display:flex;gap:10px;font-size:.85rem;color:rgba(216,234,217,.88);line-height:1.5"><span style="color:#a8c89f;flex-shrink:0;margin-top:1px">'+_IC+'</span>'+b+'</div>';}).join('');
}
function q60cat(val){
  _q60.t=val;
  document.getElementById('qs1').hidden=true;
  document.getElementById('qs2_'+val).hidden=false;
  _q60prog('50%');
}
function q60s2(val){
  _q60.s2=val;
  document.getElementById('qs2_'+_q60.t).hidden=true;
  document.getElementById('qs3_'+_q60.t).hidden=false;
  _q60prog('75%');
}
function q60s2back(){
  document.getElementById('qs2_'+_q60.t).hidden=true;
  document.getElementById('qs1').hidden=false;
  _q60prog('25%');
}
function q60s3(val){
  _q60.s3=val;
  document.getElementById('qs3_'+_q60.t).hidden=true;
  q60result();
}
function q60s3back(){
  document.getElementById('qs3_'+_q60.t).hidden=true;
  document.getElementById('qs2_'+_q60.t).hidden=false;
  _q60prog('50%');
}
function q60result(){
  var t=_q60.t,s2=_q60.s2,s3=_q60.s3,vt,nt,bl;
  if(t==='property'){
    if(s2==='fresh'){
      _q60badge(_BG,_IC,'Strong fit for mediation');
      vt='An ideal time to mediate — before positions harden.';
      nt='Starting early means you control the outcome. Most property settlements are reached in a single day, with no lawyers in the room if you prefer.';
    }else if(s2==='stalled'){
      _q60badge(_BG,_IC,'Strong fit for mediation');
      vt='Mediation is exactly the right step when direct talks have stalled.';
      nt='A skilled mediator opens a path forward that solicitor letters and direct negotiation can\\'t. Most stalled matters resolve within a single session.';
    }else if(s2==='solicitors'){
      _q60badge(_BG,_IC,'Strong fit for mediation');
      vt='Mediation works alongside your lawyers, not instead of them.';
      nt='A mediated agreement is reached faster and at a fraction of the cost of continuing by correspondence. Your solicitor can review any outcome before you sign.';
    }else{
      _q60badge(_BG,_IH,'Worth a conversation');
      vt='Even with proceedings underway, most property matters settle before a hearing.';
      nt='Courts frequently encourage mediation — and most disputes settle on terms both parties prefer to a judge\\'s decision. It\\'s not too late.';
    }
    if(s3==='home'){bl=['Sale, transfer or retention of the family home structured to suit both parties.','Stamp duty and CGT implications explained before you agree.','Outcome formalised as legally binding consent orders.'];}
    else if(s3==='super'){bl=['Superannuation splitting orders drafted and filed with the court.','We work alongside your financial advisers where needed.','Agreement formalised so both parties can move forward cleanly.'];}
    else if(s3==='complex'){bl=['Business assets, trusts and investment properties all within scope.','Commercially sensitive — everything stays completely private.','Mediator with commercial experience guides the valuation process.'];}
    else{bl=['Property settlement finalised without years of court.','Agreement formalised as legally binding consent orders.','Fixed fee quoted in writing before you commit to anything.'];}
  }else if(t==='parenting'){
    if(s2==='orders'){
      _q60badge(_BG,_IH,'Worth a conversation');
      vt='Changing existing orders works best when both parties agree — mediation gets you there.';
      nt='Courts want to see evidence of attempted agreement before varying orders. Mediation produces that agreement faster, and at far less cost than going back to court.';
      bl=['Agreed variation is faster and cheaper than a contested court application.','Changed circumstances documented in any new agreement.','Children\\'s needs remain the central focus throughout.'];
    }else{
      _q60badge(_BG,_IC,'Strong fit for mediation');
      if(s2==='formalise'){
        vt='Formalising your arrangement is straightforward — we issue the certificate courts require.';
        nt='A Section 60I certificate from our service is required before applying for consent orders. We can have your parenting plan formalised and ready to file.';
        bl=['Section 60I certificate issued — required before courts accept consent order applications.','Parenting plan converted into binding consent orders.','Child-focused process, fully confidential.'];
      }else if(s3==='broken'||s3==='nocontact'){
        vt='Even when communication has broken down, mediation still works.';
        nt='We use shuttle mediation where needed — separate rooms, staggered times — keeping the focus entirely on what\\'s best for the children, without direct contact.';
        bl=['Shuttle mediation: separate rooms and staggered times — no direct contact required.','Safety screening completed before any joint process begins.','Section 60I certificate issued if court orders are later needed.'];
      }else{
        vt='A parenting plan through mediation gives you both clarity and legal protection.';
        nt='Mediated parenting plans can be formalised as consent orders — legally binding and enforceable. Most matters are fully resolved in a single session.';
        bl=['Parenting plan resolved and formalised as consent orders.','Section 60I certificate issued — ready for court if ever needed.','Child-centred process with full confidentiality protections.'];
      }
    }
  }else if(t==='both'){
    _q60badge(_BG,_IC,'Strong fit for mediation');
    if(s2==='parenting_first'){
      vt='Sorting the parenting plan first is often the right call.';
      nt='Once arrangements for the children are settled, property negotiations become clearer and less emotionally charged. We handle both in one cohesive process.';
      bl=['Parenting plan formalised first, property settlement to follow.','Section 60I certificate issued — ready for consent orders.','Both issues resolved in fewer sessions than handling them separately.'];
    }else if(s2==='property_first'){
      vt='Financial clarity often makes parenting negotiations more straightforward.';
      nt='We structure the mediation to address both in the most efficient order — one mediator, one process, one outcome.';
      bl=['Property settlement reached and formalised as consent orders.','Parenting plan addressed in the same or a follow-up session.','One cohesive process — more efficient, less stressful.'];
    }else if(s2==='guidance'){
      vt='A free consultation will help you identify the right starting point.';
      nt='When both property and parenting need attention, the right order depends on urgency and what\\'s driving the most tension. We\\'ll help you work that out at no cost.';
      bl=['Free initial consultation — no obligation.','We assess priority and recommend a clear starting point.','Both issues handled in one cohesive mediation process.'];
    }else{
      vt='Both property and parenting can be resolved in the same mediation process.';
      nt='Handling both together is more efficient and less stressful — one mediator, one process, one outcome. Most matters are fully resolved within two sessions.';
      bl=['Parenting plan and property settlement reached in one process.','Section 60I certificate issued — consent orders ready to file.','Fixed fee covers both issues — no billing surprises.'];
    }
  }else{
    if(s2==='workplace'){
      if(s3==='urgent'){
        _q60badge(_BY,_IW,'Act quickly — time limits apply');
        vt='Fair Work time limits are strict — don\\'t wait to get advice.';
        nt='Unfair dismissal applications must be lodged within 21 days. General protections and other Fair Work matters have similar limits. We can arrange a rapid assessment this week.';
        bl=['Same-week appointments available for urgent Fair Work matters.','Early mediation prevents costly tribunal proceedings.','Confidential assessment at no obligation.'];
      }else{
        _q60badge(_BG,_IC,'Strong fit for mediation');
        vt='Workplace mediation protects relationships and avoids tribunal costs.';
        nt='Resolving a dispute before a formal complaint is filed protects everyone — the employee, the employer and the working relationship. Most workplace matters settle in a single session.';
        bl=['Completely confidential — nothing leaves the mediation room.','Preserves the employment relationship where possible.','Faster and far less costly than a Fair Work or tribunal process.'];
      }
    }else if(s2==='business'){
      _q60badge(_BG,_IC,'Strong fit for mediation');
      vt='Commercial disputes resolved through mediation are binding, private and fast.';
      nt='Business and partnership disputes typically resolve in one to two sessions. The outcome is as binding as a court order — but reached in days, not years.';
      bl=['Commercially sensitive — everything remains completely private.','Binding agreement enforceable as a contract.','A fraction of the cost and time of commercial litigation.'];
    }else if(s2==='estate'){
      _q60badge(_BG,_IC,'Strong fit for mediation');
      vt='Estate disputes fought through court erode the very estate being contested.';
      nt='A Family Provision claim through court can cost more than the estate is worth. Mediation gives every party a voice, preserves family relationships and resolves matters in weeks rather than years.';
      bl=['Suitable for contested wills, Family Provision claims and executor disputes.','Agreement reached before legal costs deplete the estate.','Completely confidential — family matters stay within the family.'];
    }else{
      _q60badge(_BG,_IH,'Worth a conversation');
      vt='Mediation works across a wide range of disputes — let\\'s talk through yours.';
      nt='A free consultation helps us assess whether mediation is the right fit and, if so, how to structure it for the best possible outcome.';
      bl=['Free confidential consultation — no obligation.','Wide range of dispute types within scope.','If mediation isn\\'t the right fit, we\\'ll say so honestly.'];
    }
  }
  _q60set(vt,nt,bl);
  _q60prog('100%');
  document.getElementById('qresult').hidden=false;
}
function q60reset(){
  _q60={t:null,s2:null,s3:null};
  ['qs2_property','qs2_parenting','qs2_both','qs2_other','qs3_property','qs3_parenting','qs3_both','qs3_other','qresult'].forEach(function(id){document.getElementById(id).hidden=true;});
  document.getElementById('qs1').hidden=false;
  _q60prog('25%');
}
</script>"""


def service_hero_with_quiz(eyebrow, h1, lede, crumb_items):
    """Two-column service hero: left=H1+lede+CTAs (left-aligned), right=quiz card."""
    crumb = crumb_html(crumb_items)
    return f"""{crumb}
<section class="phero" style="padding-bottom:clamp(48px,6vw,80px)">
  <div class="phero-blob"></div>
  <div class="wrap" style="display:grid;grid-template-columns:1fr 400px;gap:clamp(32px,5vw,64px);align-items:start">
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
