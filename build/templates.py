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
    ("property-settlement-mediation", "Property Settlement", "Divide assets fairly and finally"),
    ("parenting-plan-mediation", "Parenting Plans", "Workable arrangements for your children"),
    ("section-60i-certificates", "Section 60I Certificates", "Required before parenting court action"),
    ("financial-agreements-mediation", "Financial Agreements", "Binding agreements (BFAs), done right"),
    ("spousal-support-mediation", "Spousal Maintenance", "Fair support after separation"),
    ("child-support-mediation", "Child Support", "Resolve support disputes privately"),
    ("de-facto-mediation", "De Facto Disputes", "Same rights, same clear process"),
    ("grandparents-mediation", "Grandparents' Rights", "Stay in your grandchildren's lives"),
    ("consent-orders", "Consent Orders", "Make your agreement legally binding"),
    ("online-divorce", "Online Divorce", "Separate from anywhere in Australia"),
    ("workplace-mediation", "Workplace Mediation", "Resolve disputes before the FWC"),
]

# Grouped layout for the Services megamenu (scannable categories).
# Slugs reference SERVICES above; workplace + how-it-works live in the menu footer.
SERVICE_GROUPS = [
    ("Family & separation", ["family-law-mediation", "divorce-mediation", "online-divorce", "de-facto-mediation"]),
    ("Property & finances", ["property-settlement-mediation", "financial-agreements-mediation", "spousal-support-mediation", "consent-orders"]),
    ("Parenting & children", ["parenting-plan-mediation", "child-support-mediation", "section-60i-certificates", "grandparents-mediation"]),
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

def img(src, alt, w, h, cls="photo", caption=None, eager=False):
    """Responsive, CWV-safe <img> wrapped in <figure>. Drop optimised files
    (ideally WebP) in /assets/images/. ALWAYS pass true width/height so the
    browser reserves space and layout doesn't shift (protects CLS). Use
    eager=True only for an above-the-fold hero image (sets fetchpriority)."""
    loading = "eager" if eager else "lazy"
    prio = ' fetchpriority="high"' if eager else ''
    tag = (f'<img src="/assets/images/{esc(src)}" alt="{esc(alt)}" '
           f'width="{w}" height="{h}" loading="{loading}" decoding="async"{prio}>')
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
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Mediations Australia">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
{schema_tag}
</head>
<body>
<a href="#main" class="skip">Skip to main content</a>"""

def nav():
    svc_lookup = {s: (n, d) for s, n, d in SERVICES}
    cols = ""
    for group, slugs in SERVICE_GROUPS:
        links = "".join(
            f'<a href="/{s}/"><b>{esc(svc_lookup[s][0])}</b><span>{esc(svc_lookup[s][1])}</span></a>'
            for s in slugs)
        cols += f'<div class="mega-col"><span class="mega-head">{esc(group)}</span>{links}</div>'
    svc_mega = f"""<div class="drop mega">{cols}
      <div class="mega-foot">
        <span>Not sure which you need? <a href="/how-mediation-works/">See how mediation works</a> or resolve a <a href="/workplace-mediation/">workplace dispute</a>.</span>
        <a class="btn btn-primary" href="{BOOK_URL}">Book free consult <span class="arr">→</span></a>
      </div>
    </div>"""
    return f"""<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a href="/" class="logo"><span class="dot"></span>Mediations Australia</a>
    <nav class="nav-links" id="navlinks" aria-label="Primary">
      <span class="has-drop"><a class="lnk" href="/#disputes" aria-haspopup="true">Services</a>
        {svc_mega}
      </span>
      <a class="lnk" href="/how-mediation-works/">How it works</a>
      <a class="lnk" href="/guides/">Guides</a>
      <a class="lnk" href="/about-mediations-australia/">About</a>
      <span class="has-drop"><a class="lnk" href="/preparing-for-mediation/" aria-haspopup="true">Resources</a>
        <div class="drop">
          <a href="/preparing-for-mediation/"><b>Preparing for Mediation</b>What to expect &amp; how to get ready</a>
          <a href="/getting-ready-for-separation/"><b>Getting Ready for Separation</b>A practical checklist</a>
          <a href="/parenting-plan-template/"><b>Parenting Plan Template</b>What to include in your plan</a>
          <a href="/bfa-or-consent-orders/"><b>BFA or Consent Orders?</b>Which is right for you</a>
          <a href="/family-law-cost-estimator/"><b>Cost Estimator</b>Mediation vs court costs</a>
          <a href="/separation-under-one-roof/"><b>Separation Under One Roof</b>How it works</a>
        </div>
      </span>
      <a class="lnk" href="/contact-us/">Contact</a>
      <a class="btn btn-primary" href="{BOOK_URL}" style="padding:11px 22px;font-size:.92rem">Book free consult</a>
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
        <h4>Services</h4>
        <ul>{svc}<li><a href="/workplace-mediation/">Workplace Mediation</a></li></ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about-mediations-australia/">About us</a></li>
          <li><a href="/how-mediation-works/">How it works</a></li>
          <li><a href="/our-fee-structure/">Our fees</a></li>
          <li><a href="/preparing-for-mediation/">Resources</a></li>
          <li><a href="/our-mediators/">Our mediators</a></li>
          <li><a href="/memberships/">Memberships</a></li>
          <li><a href="/mediation-podcast/">Podcast</a></li>
          <li><a href="/books/">Books</a></li>
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
      <span>© 2026 Mediations Australia. All rights reserved. This site is general information, not legal advice.</span>
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
        "priceRange": "Fixed-fee consultations",
        "address": [{"@type": "PostalAddress", "addressLocality": c.split(",")[0],
                     "streetAddress": a, "addressCountry": "AU"} for c, a in OFFICES],
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

def article_schema(headline, desc):
    return {"@type": "Article", "headline": headline, "description": desc,
            "author": {"@type": "Organization", "name": "Mediations Australia"},
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
        notes = f'<div class="note"><span>{check}No obligation</span><span>{check}Fixed-fee, transparent</span><span>{check}In person or online</span></div>'
    return f"""<section class="cta-band" id="book">
  <div class="phero-blob"></div>
  <div class="wrap">
    <div class="reveal">
      <h2>{h}</h2>
      <p>{p}</p>
      <a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Book your free consultation <span class="arr">→</span></a>
      {notes}
    </div>
  </div>
</section>"""

print("templates module ready")
