#!/usr/bin/env python3
"""
Import blog posts from the live WordPress site.
Fetches each URL, extracts article content, generates a static HTML page
wrapped in the site's design system. Skips slugs that already exist.
"""
import os, sys, re, time, urllib.request, urllib.error
from html import unescape as _unescape

sys.path.insert(0, os.path.dirname(__file__))
from templates import head, nav, page_end, esc, crumb_html, BOOK_URL, PHONE, PHONE_HREF, DOMAIN, org_schema, breadcrumb_schema, article_schema

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POST_CSS = """<style>
/* Reading progress bar */
.progress-track{position:fixed;top:0;left:0;right:0;height:3px;z-index:999;pointer-events:none}
.progress-bar{height:100%;width:0;background:var(--sage-deep);transition:width .1s linear}
/* Hero — 2-column */
.post-hero{padding:0;border-bottom:1px solid var(--line);overflow:hidden}
.hero-inner{display:grid;grid-template-columns:1fr;max-width:1180px;margin:0 auto;padding:48px 24px 0}
@media(min-width:800px){.hero-inner{grid-template-columns:1fr 380px;gap:48px;padding:60px 48px 0;align-items:start}}
.hero-text{padding-bottom:36px}
.post-meta{display:flex;gap:12px;align-items:center;font-size:.88rem;color:var(--ink-soft);margin-bottom:18px;flex-wrap:wrap}
.post-meta .cat{background:var(--sage-light);color:var(--sage-deep);padding:5px 16px;border-radius:100px;font-weight:700;font-size:.78rem;text-transform:uppercase;letter-spacing:.05em}
.hero-text h1{font-size:clamp(2.3rem,5.2vw,4rem);line-height:1.15;letter-spacing:-.015em;margin:0 0 18px;font-family:var(--serif);font-weight:500;color:var(--ink)}
.hero-dek{font-size:1.1rem;font-style:italic;color:var(--ink-soft);margin:0 0 28px;font-family:var(--serif);max-width:54ch;line-height:1.65}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:28px;align-items:center}
.btn-outline-dark{display:inline-flex;align-items:center;padding:13px 22px;border:2px solid var(--sage-deep);color:var(--sage-deep);border-radius:8px;font-weight:600;font-size:.95rem;text-decoration:none;white-space:nowrap;transition:background .18s,color .18s}
.btn-outline-dark:hover{background:var(--sage-deep);color:#fff;text-decoration:none}
.author-byline{display:flex;align-items:center;gap:14px;padding-top:20px;border-top:1px solid var(--line)}
.author-byline img{width:44px;height:44px;border-radius:50%;object-fit:cover;flex-shrink:0}
.author-byline div{display:flex;flex-direction:column;gap:2px}
.author-name{font-weight:600;font-size:.95rem;color:var(--ink)}
.author-name a{color:inherit;text-decoration:none}
.author-cred{font-size:.82rem;color:var(--ink-soft)}
/* Hero art box */
.hero-art{display:block;width:100%;aspect-ratio:4/3;border-radius:16px;overflow:hidden;position:relative;margin-top:4px}
@media(min-width:800px){.hero-art{aspect-ratio:1/1;border-radius:20px;margin-top:0}}
.hero-art-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top}
.hero-usps{position:absolute;bottom:0;left:0;right:0;padding:14px 16px;z-index:2;display:flex;flex-direction:column;gap:6px}
.hero-usp{display:flex;align-items:center;gap:9px;background:var(--sage-light);border-radius:8px;padding:8px 13px}
.hero-usp-icon{width:15px;height:15px;flex-shrink:0;color:var(--sage-deep)}
.hero-usp span{font-size:.78rem;font-weight:600;color:var(--ink);line-height:1.3}
/* 2-column content grid */
.content-grid{max-width:1180px;margin:0 auto;padding:0 24px;display:block}
@media(min-width:980px){.content-grid{display:grid;grid-template-columns:240px 1fr;gap:52px;padding:0 48px;align-items:start}}
@media(min-width:980px){.content-grid.no-toc{grid-template-columns:1fr}}
@media(min-width:980px){.content-grid.no-toc .article-body{max-width:760px;margin:0 auto}}
/* Sidebar TOC (desktop) */
.toc-desktop{display:none}
@media(min-width:980px){.toc-desktop{display:block;position:sticky;top:96px;align-self:start}}
.toc-inner{background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin-top:32px}
.toc-label{font-size:.75rem;font-family:var(--sans);font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-soft);margin:0 0 14px}
.toc-list{list-style:none;padding:0;margin:0;counter-reset:toc;display:flex;flex-direction:column}
.toc-list li{counter-increment:toc;display:block}
.toc-list a{display:flex;gap:10px;padding:7px 0;font-size:.87rem;color:var(--sage-deep);text-decoration:none;border-bottom:1px solid var(--line);line-height:1.35;align-items:baseline}
.toc-list li:last-child a{border-bottom:none}
.toc-list a::before{content:counter(toc,decimal-leading-zero);font-size:.7rem;font-weight:700;color:var(--ink-soft);flex-shrink:0;min-width:24px}
.toc-list a:hover{color:var(--terra)}
/* Mobile TOC (collapsible) */
.toc-mobile{background:var(--cream);border:1px solid var(--line);border-radius:14px;margin:24px 0 28px;overflow:hidden}
@media(min-width:980px){.toc-mobile{display:none}}
.toc-mobile summary{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;cursor:pointer;font-weight:600;font-size:.95rem;list-style:none;user-select:none;color:var(--ink)}
.toc-mobile summary::-webkit-details-marker{display:none}
.toc-mobile .chevron{width:18px;height:18px;transition:transform .25s;flex-shrink:0;color:var(--ink-soft)}
.toc-mobile[open] .chevron{transform:rotate(180deg)}
.toc-mobile .toc-list{padding:0 18px 14px}
.toc-mobile .toc-list a{border-bottom:1px solid var(--line)}
.toc-mobile .toc-list li:last-child a{border-bottom:none}
/* Article body */
.article-body{padding:32px 0 60px;min-width:0;grid-column:2}
.article-body h2{font-size:clamp(1.4rem,3vw,2rem);margin:40px 0 12px;scroll-margin-top:90px}
.article-body h2:first-child{margin-top:0}
.article-body h3{font-size:1.2rem;margin:28px 0 8px;scroll-margin-top:90px}
.article-body p{font-size:1.06rem;color:var(--ink-soft);margin-bottom:18px;max-width:68ch}
.article-body ul,.article-body ol{margin:0 0 22px;padding-left:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.article-body ul li{position:relative;padding-left:28px;color:var(--ink-soft);font-size:1.04rem}
.article-body ul li::before{content:"";position:absolute;left:0;top:8px;width:15px;height:15px;background:var(--sage-light);border-radius:50%}
.article-body ul li::after{content:"";position:absolute;left:4px;top:11px;width:7px;height:4px;border-left:2px solid var(--sage-deep);border-bottom:2px solid var(--sage-deep);transform:rotate(-45deg)}
.article-body ol{counter-reset:li}
.article-body ol li{position:relative;padding-left:40px;color:var(--ink-soft);font-size:1.04rem;counter-increment:li}
.article-body ol li::before{content:counter(li);position:absolute;left:0;top:0;width:25px;height:25px;background:var(--sage);color:var(--cream);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.82rem;font-weight:600}
.article-body a{color:var(--sage-deep);text-decoration:underline;text-underline-offset:2px}
.article-body a:hover{color:var(--terra)}
.article-body a.btn,.article-body a.btn:hover{color:#fff;text-decoration:none}
/* Tables */
.article-body .table-wrap{border-radius:12px;overflow:hidden;box-shadow:var(--shadow);margin:20px 0 28px;overflow-x:auto}
.article-body table{width:100%;border-collapse:collapse;font-size:.97rem;background:var(--cream);display:table}
.article-body th{background:var(--sage-deep);color:var(--cream);text-align:left;padding:13px 16px;font-weight:600;font-family:var(--sans)}
.article-body td{padding:12px 16px;border-bottom:1px solid var(--line);color:var(--ink-soft)}
.article-body tr:last-child td{border-bottom:none}
.article-body tr:nth-child(even) td{background:rgba(90,113,89,.04)}
/* Answer / key-takeaway box */
.answer{background:var(--sage-light);border-left:4px solid var(--sage-deep);border-radius:0 14px 14px 0;padding:20px 26px;margin:0 0 28px}
.answer p{color:var(--ink);font-size:1.05rem;margin:0;max-width:none!important}
.answer strong{color:var(--sage-deep)}
/* CTA blocks — dark green */
.post-cta{margin:36px 0}
.post-cta-inner{background:var(--sage-light);border-radius:20px;padding:28px 32px;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.post-cta-inner p{color:var(--ink)!important;font-family:var(--serif);font-size:1.1rem;font-style:italic;margin:0!important;max-width:none!important;flex:1;min-width:240px;line-height:1.5}
.post-cta-inner .btn{flex-shrink:0;background:var(--sage-deep);color:#fff!important;font-weight:700;text-decoration:none!important;border-radius:100px;white-space:nowrap}
.post-cta-inner .btn:hover{background:var(--ink);text-decoration:none!important}
/* Source note */
.source-note{font-size:.85rem;color:var(--ink-soft);font-style:italic;margin:-12px 0 24px}
/* Legacy wrappers pass-through */
.post-body,.body-import{display:contents}
/* Mobile */
@media(max-width:799px){.hero-actions{flex-direction:column;align-items:stretch}.hero-actions .btn,.hero-actions .btn-outline-dark{width:100%;text-align:center;justify-content:center;box-sizing:border-box}}
@media(max-width:600px){.article-body h2{font-size:1.35rem}.post-cta-inner{flex-direction:column;align-items:stretch}.post-cta-inner .btn{width:100%;text-align:center}}
</style>"""

_CHEVRON = '<svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'

_HERO_IMAGE_POOL = [
    "family-law-mediation-consultation.webp",
    "mediation-initial-consultation-australia.webp",
    "family-mediation-separated-parents.webp",
    "family-mediation-private-consultation.webp",
    "mediation-private-consultation-session.webp",
    "family-mediation-initial-intake.webp",
    "family-mediation-note-taking-session.webp",
    "mediation-intake-consultation.webp",
]

def _get_hero_image(slug):
    s = slug.lower()
    if "60i" in s or "certificate" in s:
        return "section-60i-certificate-mediation.webp"
    if "consent-order" in s:
        return "consent-orders-document-review.webp"
    if "review-consent" in s or "consent-review" in s:
        return "consent-orders-review-mediation.webp"
    if "consent" in s:
        return "consent-orders-client-speaking-mediation.webp"
    if "binding-financial" in s or "bfa" in s:
        return "binding-financial-agreement-mediation.webp"
    if "parenting-plan" in s:
        return "parenting-plan-mediation.webp"
    if "parenting" in s and "custody" in s:
        return "parenting-custody-dispute-mediation.webp"
    if "parenting" in s or "custody" in s or "children" in s:
        return "parenting-dispute-mediation.webp"
    if "property-settlement" in s:
        return "property-settlement-mediation.webp"
    if "property" in s:
        return "property-settlement-discussion.webp"
    if "divorce" in s:
        return "divorce-mediation-separated-couple.webp"
    if "de-facto" in s or "defacto" in s or "de_facto" in s:
        return "de-facto-mediation-consultation.webp"
    if "separat" in s:
        return "divorce-settlement-mediation.webp"
    if "estate" in s or "probate" in s or "will-dispute" in s or "inherit" in s:
        return "estate-dispute-mediation.webp"
    if "workplace" in s or "employ" in s:
        return "workplace-mediation-session.webp"
    if "commercial" in s or "business" in s or "contract" in s or "franchise" in s:
        return "commercial-mediation-dispute-resolution.webp"
    if "financial" in s or "asset" in s or "superannuation" in s or "matrimonial" in s:
        return "financial-agreement-mediation.webp"
    if "family-law" in s or "family-court" in s or "family" in s:
        return "family-law-mediation-consultation.webp"
    if "cost" in s or "fee" in s or "price" in s or "afford" in s or "cheap" in s:
        return "mediation-intake-consultation.webp"
    if "arbitration" in s:
        return "commercial-dispute-resolution-boardroom.webp"
    if "court" in s or "litigation" in s or "tribunal" in s:
        return "commercial-business-dispute-mediation.webp"
    return _HERO_IMAGE_POOL[hash(slug) % len(_HERO_IMAGE_POOL)]

def _hero_art(h1_raw, slug=""):
    img = _get_hero_image(slug)
    alt = f"{h1_raw} — Mediations Australia"
    _check = '<svg class="hero-usp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
    _shield = '<svg class="hero-usp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
    _cal = '<svg class="hero-usp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
    return f"""<div class="hero-art">
  <img src="/assets/images/{img}" alt="{alt}" width="380" height="380" loading="eager" class="hero-art-img">
  <div class="hero-usps">
    <div class="hero-usp">{_check}<span>Nationally Accredited AMDRAS Mediators</span></div>
    <div class="hero-usp">{_shield}<span>Up to 90% Cheaper than Going to Court/Tribunal</span></div>
    <div class="hero-usp">{_cal}<span>Australia-Wide + Free Consultation &amp; No Obligation</span></div>
  </div>
</div>"""
_PROG_JS = '<script>(function(){var b=document.getElementById("prog");if(!b)return;function u(){var s=document.documentElement.scrollTop||document.body.scrollTop,h=document.documentElement.scrollHeight-document.documentElement.clientHeight;b.style.width=(h>0?Math.round(s/h*100):0)+"%"}window.addEventListener("scroll",u,{passive:true});u()})();</script>'

def _slugify(text):
    """Convert heading text to a URL-safe id."""
    text = re.sub(r'<[^>]+>', '', text)
    text = _unescape(text).lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')[:50]

def _extract_toc(body):
    """Pull inline post-toc nav from body, or auto-generate from h2 tags.
    Adds id= attributes to bare h2 tags so anchor links work.
    Returns (cleaned_body, ul_items_html)."""
    # Try explicit post-toc nav first
    m = re.search(r'<nav[^>]*class="[^"]*post-toc[^"]*"[^>]*>.*?<ul>(.*?)</ul>.*?</nav>', body, re.S | re.I)
    if m:
        ul_inner = m.group(1).strip()
        cleaned = re.sub(r'<nav[^>]*class="[^"]*post-toc[^"]*"[^>]*>.*?</nav>', '', body, flags=re.S | re.I).strip()
        return cleaned, ul_inner
    # Find all h2 tags (with or without id=); fall back to h3 if fewer than 2
    h2_tags = list(re.finditer(r'<h2([^>]*)>(.*?)</h2>', body, re.S | re.I))
    if len(h2_tags) < 2:
        h3_tags = list(re.finditer(r'<h3([^>]*)>(.*?)</h3>', body, re.S | re.I))
        if len(h3_tags) < 2:
            return body, ""
        # Promote h3 → h2 and use them for the TOC
        h2_tags = h3_tags
        _promote_h3 = True
    else:
        _promote_h3 = False
    items = []
    new_body = body
    offset = 0
    for tag in h2_tags:
        attrs, inner = tag.group(1), tag.group(2)
        id_m = re.search(r'\bid="([^"]+)"', attrs)
        if id_m:
            hid = id_m.group(1)
            if _promote_h3:
                new_tag = f'<h2 id="{hid}"{attrs}>{inner}</h2>'
                start, end = tag.start() + offset, tag.end() + offset
                new_body = new_body[:start] + new_tag + new_body[end:]
                offset += len(new_tag) - (end - start)
        else:
            # Generate and inject an id= attribute (and promote h3→h2 if needed)
            hid = _slugify(inner)
            new_tag = f'<h2 id="{hid}">{inner}</h2>'
            start, end = tag.start() + offset, tag.end() + offset
            new_body = new_body[:start] + new_tag + new_body[end:]
            offset += len(new_tag) - (end - start)
        label = re.sub(r'<[^>]+>', '', inner).strip()
        if label:
            items.append(f'<li><a href="#{hid}">{esc(label)}</a></li>')
    return new_body, "".join(items)

def _toc_blocks(items):
    """Return (sidebar_html, mobile_html) from TOC list items HTML string."""
    if not items:
        return "", ""
    sidebar = (
        '<aside class="toc-desktop" aria-label="Table of contents">'
        '<div class="toc-inner"><p class="toc-label">In this guide</p>'
        f'<ul class="toc-list">{items}</ul></div></aside>'
    )
    mobile = (
        '<details class="toc-mobile">'
        f'<summary><span>In this guide</span>{_CHEVRON}</summary>'
        f'<ul class="toc-list">{items}</ul></details>'
    )
    return sidebar, mobile

EXPERT_BIO = """<aside style="margin-top:3rem;padding:1.5rem;background:var(--surf,#f7f8fa);border-radius:10px;border:1px solid var(--border,#e5e7eb)"><p style="font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted,#6b7280);margin:0 0 1rem">About the expert</p><div style="display:flex;gap:1.25rem;align-items:flex-start"><img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia" width="80" height="80" loading="lazy" style="border-radius:50%;flex-shrink:0;object-fit:cover;width:80px;height:80px"><div><p style="font-weight:700;margin:0 0 .15rem;font-size:1rem">Dan Toombs</p><p style="margin:0 0 .75rem;color:var(--muted,#6b7280);font-size:.875rem">Founder, Mediations Australia</p><p style="margin:0 0 .75rem;font-size:.9rem;line-height:1.6">Dan Toombs is the Founder of Mediations Australia, an award-winning lawyer, former Tribunal Member and nationally accredited mediator (AMDRAS). His career spans law, adjudication and organisational leadership, giving him particular insight into the systemic, structural and human dynamics that drive complex disputes.</p><a href="/our-mediators/" style="font-size:.875rem;font-weight:600">View Dan Toombs&#x2019; profile &rarr;</a></div></div></aside>"""

URLS = [
    "https://mediationsaustralia.com.au/what-is-alimony-in-australia/",
    "https://mediationsaustralia.com.au/how-much-does-a-family-lawyer-cost-in-australia/",
    "https://mediationsaustralia.com.au/separated-under-one-roof/",
    "https://mediationsaustralia.com.au/mediation-who-pays/",
    "https://mediationsaustralia.com.au/section-79-of-the-family-law-act-1975/",
    "https://mediationsaustralia.com.au/property-settlement-after-separation/",
    "https://mediationsaustralia.com.au/mediation-with-a-narcissist/",
    "https://mediationsaustralia.com.au/family-mediation/",
    "https://mediationsaustralia.com.au/parenting-plans-example/",
    "https://mediationsaustralia.com.au/consent-orders-example/",
    "https://mediationsaustralia.com.au/who-gets-the-dog-how-mediation-resolves-pet-disputes-after-separation/",
    "https://mediationsaustralia.com.au/online-mediation-australia/",
    "https://mediationsaustralia.com.au/strata-neighbour-dispute-mediation/",
    "https://mediationsaustralia.com.au/estate-inheritance-dispute-mediation/",
    "https://mediationsaustralia.com.au/right-to-disconnect-workplace-mediation/",
    "https://mediationsaustralia.com.au/shareholder-partnership-dispute-mediation/",
    "https://mediationsaustralia.com.au/commercial-lease-dispute-mediation-australia/",
    "https://mediationsaustralia.com.au/why-your-employee-mediation-fails-how-to-make-it-work/",
    "https://mediationsaustralia.com.au/conflict-resolution-in-the-workplace/",
    "https://mediationsaustralia.com.au/contesting-a-will-in-australia-can-mediation-avoid-a-court-battle/",
    "https://mediationsaustralia.com.au/workplace-discrimination-mediation-your-options-in-australia/",
    "https://mediationsaustralia.com.au/franchise-disputes-in-australia-mediation-under-the-franchising-code-of-conduct/",
    "https://mediationsaustralia.com.au/workplace-bullying-complaints-how-mediation-can-help/",
    "https://mediationsaustralia.com.au/online-mediation-how-virtual-sessions-work-and-why-theyre-effective/",
    "https://mediationsaustralia.com.au/redundancy-and-restructuring-disputes-how-mediation-can-help/",
    "https://mediationsaustralia.com.au/how-employers-can-use-mediation-to-reduce-workplace-conflict-costs/",
    "https://mediationsaustralia.com.au/how-mediation-exposes-workplace-issues-and-how-belbin-team-roles-can-help/",
    "https://mediationsaustralia.com.au/why-workplace-conflicts-really-happen-how-mediation-resolves-them/",
    "https://mediationsaustralia.com.au/why-arbitration-might-be-the-best-way-to-resolve-your-complex-family-law-dispute/",
    "https://mediationsaustralia.com.au/shinohara-how-the-2025-family-law-changes-abolished-add-backs/",
    "https://mediationsaustralia.com.au/how-to-separate-from-your-spouse-or-partner-in-australia/",
    "https://mediationsaustralia.com.au/binding-child-support-agreements-in-australia-important-2026-update/",
    "https://mediationsaustralia.com.au/what-happens-when-property-values-change-before-your-divorce-settlement-in-australia/",
    "https://mediationsaustralia.com.au/de-facto-relationships/",
    "https://mediationsaustralia.com.au/five-things-to-do-before-uttering-i-want-a-divorce/",
    "https://mediationsaustralia.com.au/kennon-v-spry/",
    "https://mediationsaustralia.com.au/workplace-disputes-are-surging-why-early-mediation-is-the-smarter-path-forward/",
    "https://mediationsaustralia.com.au/consent-orders-2025-update/",
    "https://mediationsaustralia.com.au/50-years-of-the-family-law-act-how-mediation-has-changed-the-landscape/",
    "https://mediationsaustralia.com.au/contesting-a-will-with-mediation/",
    "https://mediationsaustralia.com.au/understanding-family-conflict-and-why-mediation-is-your-best-path-forward/",
    "https://mediationsaustralia.com.au/why-going-to-court-for-your-family-law-dispute-is-a-mistake/",
    "https://mediationsaustralia.com.au/abc-expose-the-hidden-cost-of-family-court-battles/",
    "https://mediationsaustralia.com.au/are-mediation-agreements-legally-binding/",
    "https://mediationsaustralia.com.au/binding-financial-agreement/",
    "https://mediationsaustralia.com.au/avoid-these-mistakes-with-a-binding-financial-agreement/",
    "https://mediationsaustralia.com.au/binding-financial-agreement-v-consent-orders/",
    "https://mediationsaustralia.com.au/why-mediation-works-the-science-behind-it/",
    "https://mediationsaustralia.com.au/how-long-does-mediation-take/",
    "https://mediationsaustralia.com.au/estate-dispute-mediation/",
    "https://mediationsaustralia.com.au/preparing-for-mediation/",
    "https://mediationsaustralia.com.au/binding-financial-agreement-what-you-need-to-know/",
    "https://mediationsaustralia.com.au/how-to-lodge-a-caveat-over-property-in-family-law-matters/",
    "https://mediationsaustralia.com.au/preparing-for-property-settlement-when-youre-financially-vulnerable/",
    "https://mediationsaustralia.com.au/ex-delaying-property-settlement/",
    "https://mediationsaustralia.com.au/my-partner-wants-me-out-understanding-your-rights-when-youre-not-on-the-title/",
    "https://mediationsaustralia.com.au/the-role-of-fair-work-australia-and-workplace-mediation/",
    "https://mediationsaustralia.com.au/what-is-workplace-mediation-2023-important-update/",
    "https://mediationsaustralia.com.au/what-is-section-79a-of-family-law-act/",
    "https://mediationsaustralia.com.au/divorce-fees-in-australia/",
    "https://mediationsaustralia.com.au/fathers-rights-after-separation/",
    "https://mediationsaustralia.com.au/what-is-the-difference-between-mediation-and-family-dispute-resolution/",
    "https://mediationsaustralia.com.au/conciliation-in-family-law/",
    "https://mediationsaustralia.com.au/difference-between-mediation-conciliation/",
    "https://mediationsaustralia.com.au/create-parenting-plan-that-works/",
    "https://mediationsaustralia.com.au/what-factors-do-property-settlement-lawyers-consider-when-dividing-assets/",
    "https://mediationsaustralia.com.au/property-settlement-mediation-most-effective-strategies-for-resolving-property-settlement-disputes/",
    "https://mediationsaustralia.com.au/12-essential-things-to-know-about-binding-financial-agreements-in-australia/",
    "https://mediationsaustralia.com.au/family-mediation-process-guide/",
    "https://mediationsaustralia.com.au/mediation-in-family-law-a-comprehensive-guide/",
    "https://mediationsaustralia.com.au/what-is-a-prenup-agreement-in-2024/",
    "https://mediationsaustralia.com.au/how-to-resolve-your-property-settlement-with-mediation-in-australia/",
    "https://mediationsaustralia.com.au/what-hannahs-law-means/",
    "https://mediationsaustralia.com.au/court-ordered-drug-and-alcohol-testing/",
    "https://mediationsaustralia.com.au/can-my-ex-wife-claim-money-after-divorce-in-australia/",
    "https://mediationsaustralia.com.au/what-do-i-do-if-my-former-partner-will-not-do-mediation/",
    "https://mediationsaustralia.com.au/best-apps-for-separated-parents/",
    "https://mediationsaustralia.com.au/my-ex-wont-sign-divorce-papers/",
    "https://mediationsaustralia.com.au/are-gifts-included-in-property-settlements-in-australia/",
    "https://mediationsaustralia.com.au/how-do-de-facto-couples-split-assets/",
    "https://mediationsaustralia.com.au/cryptocurrency-and-digital-assets-in-property-settlements/",
    "https://mediationsaustralia.com.au/whats-the-difference-between-a-de-facto-relationship-and-marriage/",
    "https://mediationsaustralia.com.au/de-facto-relationships-and-prenups-what-you-have-to-know/",
    "https://mediationsaustralia.com.au/changes-to-the-family-law-act-2025-you-must-know/",
    "https://mediationsaustralia.com.au/investment-property-division-in-family-law-disputes/",
    "https://mediationsaustralia.com.au/family-law-mediator/",
    "https://mediationsaustralia.com.au/what-are-procedural-orders-in-family-court/",
    "https://mediationsaustralia.com.au/how-to-apply-file-for-get-a-divorce-in-western-australia-wa/",
    "https://mediationsaustralia.com.au/how-often-do-fathers-get-50-50-custody-in-australia/",
    "https://mediationsaustralia.com.au/postnuptial-agreement-australia-everything-you-need-to-know/",
    "https://mediationsaustralia.com.au/how-long-do-consent-orders-take/",
    "https://mediationsaustralia.com.au/property-in-divorce-settlement/",
    "https://mediationsaustralia.com.au/the-pros-and-cons-of-shuttle-mediation/",
    "https://mediationsaustralia.com.au/what-am-i-entitled-to-in-a-separation-in-australia/",
    "https://mediationsaustralia.com.au/property-settlement-after-separation-time-limit/",
    "https://mediationsaustralia.com.au/what-is-a-litigation-guardian-in-australia/",
    "https://mediationsaustralia.com.au/when-is-mediation-not-a-good-idea/",
    "https://mediationsaustralia.com.au/what-is-the-magellan-list/",
    "https://mediationsaustralia.com.au/how-to-get-a-divorce-in-australia-a-step-by-step-guide/",
    "https://mediationsaustralia.com.au/cost-of-divorce-in-australia/",
    "https://mediationsaustralia.com.au/family-loan-agreement-matters/",
    "https://mediationsaustralia.com.au/supporting-your-child-through-parents-separation-a-comprehensive-guide-for-australian-families/",
    "https://mediationsaustralia.com.au/separation-or-divorce-which-is-better/",
    "https://mediationsaustralia.com.au/12-best-strategies-for-effective-parenting-plans-in-australia/",
    "https://mediationsaustralia.com.au/same-sex-divorce-in-australia/",
    "https://mediationsaustralia.com.au/can-you-sue-a-family-trust-in-australia/",
    "https://mediationsaustralia.com.au/australia-lgbt-marriage-mediation/",
    "https://mediationsaustralia.com.au/what-is-an-avo/",
    "https://mediationsaustralia.com.au/spousal-maintenance/",
    "https://mediationsaustralia.com.au/fathers-rights-in-family-law-2022-update/",
    "https://mediationsaustralia.com.au/how-to-get-a-divorce-in-new-south-wales/",
    "https://mediationsaustralia.com.au/child-support-payments-and-taxes/",
    "https://mediationsaustralia.com.au/prenups-for-women/",
    "https://mediationsaustralia.com.au/trial-separation/",
    "https://mediationsaustralia.com.au/divorce-without-lawyers/",
    "https://mediationsaustralia.com.au/parental-alienation-australia-dont-let-your-ex-destroy-your-childs-love-for-you/",
    "https://mediationsaustralia.com.au/five-benefits-of-using-mediation-to-resolve-divorce-issues/",
    "https://mediationsaustralia.com.au/mediation-vs-collaborative-law/",
    "https://mediationsaustralia.com.au/family-law-mediation-what-happens-if-i-dont-want-to-do-it/",
    "https://mediationsaustralia.com.au/what-to-expect-at-a-family-law-mediation-for-property-division/",
    "https://mediationsaustralia.com.au/attend-mediation-in-family-law-matters/",
    "https://mediationsaustralia.com.au/is-family-law-mediation-compulsory/",
    "https://mediationsaustralia.com.au/family-law-mediation-for-property-settlements/",
    "https://mediationsaustralia.com.au/superannuation-and-family-law-important-2024-update/",
    "https://mediationsaustralia.com.au/understanding-mediation-2024/",
    "https://mediationsaustralia.com.au/what-is-the-average-split-in-a-divorce-settlement-australia/",
    "https://mediationsaustralia.com.au/getting-divorced-or-separated-the-2022-guide/",
    "https://mediationsaustralia.com.au/who-pays-bills-during-separation/",
    "https://mediationsaustralia.com.au/what-happens-to-superannuation-if-i-separate-or-divorce/",
    "https://mediationsaustralia.com.au/in-a-divorce-who-gets-what/",
    "https://mediationsaustralia.com.au/60-40-split-divorce-australia/",
    "https://mediationsaustralia.com.au/divorce-without-a-lawyer/",
    "https://mediationsaustralia.com.au/the-cost-of-divorce-in-australia/",
    "https://mediationsaustralia.com.au/high-conflict-family-law-mediation/",
    "https://mediationsaustralia.com.au/how-long-does-a-divorce-take/",
    "https://mediationsaustralia.com.au/divorce-property-settlement-your-best-options-in-2022/",
    "https://mediationsaustralia.com.au/points-to-consider-family-mediation-lawyers-in-australia/",
    "https://mediationsaustralia.com.au/family-court-mediation-process/",
    "https://mediationsaustralia.com.au/understanding-divorce-laws-in-nsw/",
    "https://mediationsaustralia.com.au/mediate-collaborate-or-litigate/",
    "https://mediationsaustralia.com.au/the-different-ways-to-resolve-family-law-disputes/",
    "https://mediationsaustralia.com.au/post-prenup-agreement/",
    "https://mediationsaustralia.com.au/joint-tenancy-and-divorce/",
    "https://mediationsaustralia.com.au/applying-for-a-divorce-in-australia/",
    "https://mediationsaustralia.com.au/property-settlement-in-family-law/",
    "https://mediationsaustralia.com.au/divorce-certificate-in-australia/",
    "https://mediationsaustralia.com.au/understanding-property-settlement-in-divorce-a-guide-to-private-agreements/",
    "https://mediationsaustralia.com.au/what-is-mediation-in-family-law/",
    "https://mediationsaustralia.com.au/stepparent-rights-and-family-law-in-australia/",
    "https://mediationsaustralia.com.au/what-are-family-reports-in-family-law-matters/",
    "https://mediationsaustralia.com.au/what-are-the-mothers-rights-in-family-law/",
    "https://mediationsaustralia.com.au/how-property-settlements-work/",
    "https://mediationsaustralia.com.au/how-to-force-a-property-settlement/",
    "https://mediationsaustralia.com.au/mediate-workplace-conflict-in-australia/",
    "https://mediationsaustralia.com.au/how-to-get-ready-for-property-settlement-mediation/",
    "https://mediationsaustralia.com.au/mediation-in-property-settlement-cases/",
    "https://mediationsaustralia.com.au/when-should-we-consider-property-settlement-mediation/",
    "https://mediationsaustralia.com.au/domestic-violence/",
    "https://mediationsaustralia.com.au/what-is-a-restraining-order/",
    "https://mediationsaustralia.com.au/arbitration-in-family-law/",
    "https://mediationsaustralia.com.au/the-marriage-separation-process-in-nsw/",
    "https://mediationsaustralia.com.au/consent-order/",
    "https://mediationsaustralia.com.au/how-do-i-change-a-consent-order/",
    "https://mediationsaustralia.com.au/breach-of-family-court-order/",
    "https://mediationsaustralia.com.au/surrogacy-laws-in-australia-2024/",
    "https://mediationsaustralia.com.au/family-law-separation-agreements-the-2024-guide/",
    "https://mediationsaustralia.com.au/application-for-divorce/",
    "https://mediationsaustralia.com.au/what-is-child-custody-mediation/",
    "https://mediationsaustralia.com.au/what-is-a-dvo-everything-you-need-to-know/",
    "https://mediationsaustralia.com.au/intervention-orders/",
    "https://mediationsaustralia.com.au/mediation-or-litigation-what-is-the-best/",
    "https://mediationsaustralia.com.au/what-happens-to-business-in-divorce/",
    "https://mediationsaustralia.com.au/family-court-process-2024-update/",
    "https://mediationsaustralia.com.au/joint-divorce-application/",
    "https://mediationsaustralia.com.au/what-you-need-to-know-about-parenting-plans/",
    "https://mediationsaustralia.com.au/role-of-a-mediator-divorce-mediation/",
    "https://mediationsaustralia.com.au/difference-mediator-and-conciliator/",
    "https://mediationsaustralia.com.au/what-is-a-dvo-how-to-apply-for-a-domestic-violence-order/",
    "https://mediationsaustralia.com.au/divorce-property-settlement-examples-in-australia/",
    "https://mediationsaustralia.com.au/family-law-regulations-explained/",
    "https://mediationsaustralia.com.au/divorce-application-process/",
    "https://mediationsaustralia.com.au/grandparents-rights-how-to-see-your-grandchildren-2022-update/",
    "https://mediationsaustralia.com.au/how-much-does-mediation-cost/",
    "https://mediationsaustralia.com.au/shuttle-mediation/",
    "https://mediationsaustralia.com.au/how-do-i-contact-centrelink/",
    "https://mediationsaustralia.com.au/parenting-plan-vs-parenting-order/",
    "https://mediationsaustralia.com.au/best-divorce-lawyers-in-sydney/",
    "https://mediationsaustralia.com.au/travel-overseas-after-a-separation/",
    "https://mediationsaustralia.com.au/how-are-assets-divided-in-a-divorce/",
    "https://mediationsaustralia.com.au/mediation-for-separation/",
    "https://mediationsaustralia.com.au/does-a-husband-have-to-support-his-wife/",
    "https://mediationsaustralia.com.au/who-gets-to-stay-in-the-house-during-separation/",
    "https://mediationsaustralia.com.au/when-child-support-stops-guide/",
    "https://mediationsaustralia.com.au/grandparents-custody-in-australia/",
    "https://mediationsaustralia.com.au/what-am-i-entitled-to-in-a-separation/",
    "https://mediationsaustralia.com.au/what-is-divorce-law-in-australia/",
    "https://mediationsaustralia.com.au/separation-lawyer-sydney/",
    "https://mediationsaustralia.com.au/im-contemplating-separation-do-i-see-a-lawyer-or-a-mediation-practice-first/",
    "https://mediationsaustralia.com.au/the-7-most-common-questions-about-mediation/",
    "https://mediationsaustralia.com.au/5-reasons-why-you-should-consider-mediation-for-child-custody-disputes/",
    # sitemap2
    "https://mediationsaustralia.com.au/the-role-of-the-lawyer-in-mediation/",
    "https://mediationsaustralia.com.au/why-you-have-to-update-your-will-after-separation/",
    "https://mediationsaustralia.com.au/what-do-i-need-to-disclose-in-my-property-settlement-dispute/",
    "https://mediationsaustralia.com.au/how-to-resolve-your-family-law-dispute-online/",
    "https://mediationsaustralia.com.au/how-to-prepare-for-a-property-settlement-mediation/",
    "https://mediationsaustralia.com.au/what-am-i-entitled-to-in-a-divorce-or-separation-in-australia/",
    "https://mediationsaustralia.com.au/how-long-does-it-take-to-get-a-divorce/",
    "https://mediationsaustralia.com.au/can-you-record-your-ex-without-permission/",
    "https://mediationsaustralia.com.au/what-is-the-role-of-an-independent-childrens-lawyer/",
    "https://mediationsaustralia.com.au/what-you-need-to-know-about-parenting-coordination-2022-update/",
    "https://mediationsaustralia.com.au/what-if-my-ex-dies-before-our-property-settlement-is-finalised/",
    "https://mediationsaustralia.com.au/pre-separation-checklist/",
    "https://mediationsaustralia.com.au/the-difference-between-a-divorce-lawyer-and-a-mediator/",
    "https://mediationsaustralia.com.au/how-to-sell-property-during-a-divorce/",
    "https://mediationsaustralia.com.au/commonly-asked-family-law-questions/",
    "https://mediationsaustralia.com.au/final-hearing-in-family-law-disputes/",
    "https://mediationsaustralia.com.au/how-to-make-changes-to-a-parenting-order/",
    "https://mediationsaustralia.com.au/how-to-protect-your-online-privacy-following-separation/",
    "https://mediationsaustralia.com.au/duty-of-disclosure-in-australian-family-law/",
    "https://mediationsaustralia.com.au/divorce-law-near-me/",
    "https://mediationsaustralia.com.au/how-long-do-consent-orders-take-in-family-law-matters/",
    "https://mediationsaustralia.com.au/parenting-payments-in-australia/",
    "https://mediationsaustralia.com.au/when-should-i-think-about-parenting-mediation-or-custody-mediation/",
    "https://mediationsaustralia.com.au/how-to-get-divorce-papers-the-2022-guide/",
    "https://mediationsaustralia.com.au/how-are-contributions-assessed-in-family-law-matters-2/",
    "https://mediationsaustralia.com.au/nothing-alternate-about-alternate-dispute-resolution-adr/",
    "https://mediationsaustralia.com.au/how-to-convince-your-ex-partner-to-do-mediation/",
    "https://mediationsaustralia.com.au/how-to-get-ready-for-mediation/",
    "https://mediationsaustralia.com.au/litigation-or-mediation-choose-very-wisely/",
    "https://mediationsaustralia.com.au/how-does-mediation-help-co-parenting/",
    "https://mediationsaustralia.com.au/is-mediation-expensive/",
    "https://mediationsaustralia.com.au/becoming-independent-sooner-how-mediation-can-help-you-agree-on-spousal-support/",
    "https://mediationsaustralia.com.au/how-mediation-can-help-in-financial-agreements/",
    "https://mediationsaustralia.com.au/how-you-can-reach-an-agreement-in-mediation/",
    "https://mediationsaustralia.com.au/costs-of-going-to-court/",
    "https://mediationsaustralia.com.au/how-are-contributions-assessed-in-family-law-matters/",
    "https://mediationsaustralia.com.au/what-is-included-in-a-matrimonial-property-pool/",
    "https://mediationsaustralia.com.au/what-is-a-section-60i-certificate-why-do-i-need-one/",
    "https://mediationsaustralia.com.au/pets-and-family-law-who-gets-the-pets-after-separation/",
]


class _Follow308(urllib.request.HTTPRedirectHandler):
    def http_error_308(self, req, fp, code, msg, headers):
        return self.http_error_302(req, fp, code, msg, headers)

_opener = urllib.request.build_opener(_Follow308())

def fetch_html(url):
    url = url.replace("://mediationsaustralia.com.au/", "://www.mediationsaustralia.com.au/")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SiteImporter/1.0)"})
    with _opener.open(req, timeout=20) as r:
        return r.read().decode("utf-8", errors="replace")


def extract_meta_title(html):
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not m:
        return ""
    t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    t = re.sub(r"\s*[|–—-]\s*(Mediations Australia|Mediation Australia).*$", "", t, flags=re.I).strip()
    return t


def extract_meta_desc(html):
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
    if not m:
        m = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.I | re.S)
    return m.group(1).strip() if m else ""


def extract_h1(html):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def _div_contents(html, class_fragment):
    """Return inner HTML of the first div whose class contains class_fragment,
    using depth tracking to avoid early truncation from nested divs."""
    start = re.compile(r'<div[^>]+class="[^"]*' + class_fragment + r'[^"]*"[^>]*>', re.I)
    m = start.search(html)
    if not m:
        return ""
    pos = m.end()
    depth = 1
    tag = re.compile(r'<(/?)div[\s>]', re.I)
    end = pos
    while depth > 0 and pos < len(html):
        t = tag.search(html, pos)
        if not t:
            break
        depth += -1 if t.group(1) else 1
        end = t.start()
        pos = t.end()
    inner = html[m.end():end].strip()
    return inner if len(inner) > 200 else ""


def extract_article_body(html):
    for cls in ("entry-content", "post-content", "article-content", "the-content"):
        body = _div_contents(html, cls)
        if body:
            return body
    # Fallback: static-site post-body div (used when fetching from live static pages)
    m = re.search(r'<div class="post-body"><div class="wrap-narrow">(.*?)<aside\b', html, re.S)
    if m and len(m.group(1).strip()) > 200:
        return m.group(1).strip()
    m = re.search(r'<div class="post-body"><div class="wrap-narrow">(.*?)</div>\s*</div>\s*<', html, re.S)
    if m and len(m.group(1).strip()) > 200:
        return m.group(1).strip()
    # Fallback: full <article> contents
    m = re.search(r"<article[^>]*>(.*?)</article>", html, re.S | re.I)
    if m and len(m.group(1).strip()) > 200:
        return m.group(1).strip()
    return ""


def _wrap_tables(html):
    """Wrap bare <table> elements in a div so border-radius/overflow work in all browsers.
    Idempotent — strips existing table-wrap wrappers first to prevent double-wrapping on rebuild."""
    # Strip any existing table-wrap divs immediately around a table (prevent triple nesting)
    while '<div class="table-wrap"><div class="table-wrap">' in html:
        html = html.replace('<div class="table-wrap"><div class="table-wrap">', '<div class="table-wrap">')
        html = re.sub(r'</table>(</div>){2,}', '</table></div>', html)
    # Wrap any still-bare tables (not preceded by table-wrap)
    html = re.sub(r'(?<!["\w])(?<!wrap">)<table(\b)', r'<div class="table-wrap"><table\1', html)
    # Don't double-add closing div
    html = re.sub(r'</table>(?!</div>)', r'</table></div>', html)
    return html


def clean_body(html):
    html = re.sub(r'href="https://mediationsaustralia\.com\.au/([^"]*)"', r'href="/\1"', html)
    html = re.sub(r"\[/?[a-z_]+[^\]]*\]", "", html)
    html = re.sub(r'\s*style="[^"]*"', "", html)
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S | re.I)
    html = re.sub(r"<p>\s*</p>", "", html)
    html = re.sub(r'<figure[^>]*class="[^"]*wp-block-image[^"]*"[^>]*>', "<figure>", html)
    html = re.sub(r"<h1[^>]*>.*?</h1>", "", html, flags=re.S | re.I)
    # Strip all images and figures — WP media library images don't carry over
    html = re.sub(r"<figure[^>]*>.*?</figure>", "", html, flags=re.S | re.I)
    html = re.sub(r"<img[^>]*/?>", "", html, flags=re.I)
    html = re.sub(r"<div[^>]+class=\"[^\"]*wp-block-[^\"]*\"[^>]*>", "<div>", html, flags=re.I)
    # Strip WP "Summarise with AI" widget and similar injected containers
    html = re.sub(r'<div[^>]+class="[^"]*summarize-with-ai[^"]*"[^>]*>.*?</div>', "", html, flags=re.S | re.I)
    # Strip WP content-inner wrapper divs (page builder residue)
    html = re.sub(r'<div[^>]+class="[^"]*content-inner[^"]*"[^>]*>', '', html, flags=re.I)
    # Strip Tailwind/AI-generated class attributes from inline elements and headings
    html = re.sub(r'(<(?:p|a|li|span|em|strong|blockquote|h[2-6])\b[^>]*?)\s+class="[^"]*(?:font-|text-|break-|whitespace-|leading-\[|underline|decoration-|hover:|focus:|-mb-|-mt-)[^"]*"', r'\1', html, flags=re.I)
    # Fix double-encoded entities (e.g. &amp;amp; → &amp; so browser renders & correctly)
    html = re.sub(r"&amp;(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);", r"&\1;", html)
    return html.strip()


def truncate(s, limit):
    if len(s) <= limit:
        return s
    return s[: limit - 1].rsplit(" ", 1)[0] + "…"


# Slugs whose WP URL 308-redirects to a different path — map to the actual fetch URL.
FETCH_URL_OVERRIDES = {
    "mediation-vs-collaborative-law":        "https://www.mediationsaustralia.com.au/mediate-or-litigate/",
    "australia-lgbt-marriage-mediation":     "https://www.mediationsaustralia.com.au/same-sex-family-law/",
    "mediation-in-property-settlement-cases":"https://www.mediationsaustralia.com.au/property-settlement-mediation-guide/",
    "what-is-a-dvo-everything-you-need-to-know": "https://www.mediationsaustralia.com.au/domestic-violence-and-family-law/",
}

# Override title/desc/h1 for specific slugs (CTR fixes, stale WP data).
# Slugs listed here are force-rebuilt even if the directory already exists.
from expanded_bodies import EXPANDED as _EXPANDED  # batch-expanded body content

META_OVERRIDES = {
    # ── Noindex off-topic imports ──────────────────────────────────────────────
    "parenting-payments-in-australia": {
        "noindex": True,
    },
    "how-do-i-contact-centrelink": {
        "noindex": True,
    },

    # ── Internal link injections (body_suffix) ─────────────────────────────────
    "what-is-a-restraining-order": {
        "body_suffix": """
<div class="answer reveal" style="margin-top:2rem">
<h3>Need mediation, not a restraining order?</h3>
<p>A restraining order addresses safety. But for the underlying family dispute — parenting arrangements, property division, separation — mediation is almost always the better first step. Our nationally accredited mediators work with families across Australia:</p>
<ul>
<li><strong><a href="/perth-mediation/">Perth family mediators</a></strong> — serving the Perth CBD, Fremantle, Joondalup and the wider Perth metro area.</li>
<li><strong><a href="/sydney-mediation/">Sydney family mediators</a></strong> — serving the Sydney CBD, North Shore, Eastern Suburbs, Inner West and Parramatta.</li>
<li><strong><a href="/melbourne-mediation/">Melbourne family mediators</a></strong> — serving Melbourne CBD, inner east, inner north, the Mornington Peninsula and outer suburbs.</li>
<li><strong><a href="/brisbane-mediation/">Brisbane family mediators</a></strong> — serving Brisbane CBD, Ipswich, Logan, the Redlands and South East Queensland.</li>
<li><a href="/family-law-mediation/">All family mediation services →</a></li>
</ul>
<p><a href="/book-a-consultation/" class="btn btn-primary" style="margin-top:0.5rem">Book a Free Consultation</a></p>
</div>""",
    },

    # ── Consent orders cornerstone (2,000+ words) ──────────────────────────────
    "consent-orders-2025-update": {
        "title": "Consent Orders in Australia: 2025 Complete Guide",
        "desc":  "Everything you need to know about consent orders in Australia — costs, process, timeline and the 2025 changes. Written by accredited family mediators.",
        "h1":    "Consent Orders in Australia: 2025 Complete Guide",
        "read_min": "12",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> Consent orders are court-approved agreements that formalise property settlements, superannuation splits and parenting arrangements after separation. They carry the same legal weight as a contested court order — but are reached by agreement, usually without a court hearing. Costs typically run $2,400–$5,500 all-in, and approval takes 6–12 weeks. The 2025 Family Law Act changes did not remove consent orders but did alter what courts consider "just and equitable" — meaning your agreement must reflect the updated framework.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#what-are-consent-orders">What are consent orders?</a></li>
<li><a href="#types">Types of consent orders</a></li>
<li><a href="#process">The consent orders process, step by step</a></li>
<li><a href="#costs-timeline">Costs and timeline: a worked example</a></li>
<li><a href="#consent-orders-vs-bfa">Consent orders vs binding financial agreements</a></li>
<li><a href="#after">After consent orders are made</a></li>
<li><a href="#vary">Can consent orders be changed?</a></li>
<li><a href="#2025-changes">2025 Family Law Act changes and consent orders</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="what-are-consent-orders">What Are Consent Orders?</h2>
<p>A consent order is a written agreement between separated or divorcing parties that has been approved by the Federal Circuit and Family Court of Australia (FCFCOA). Once approved, it becomes a legally binding court order — enforceable in the same way as an order made after a contested hearing, but without the parties ever having to appear before a judge.</p>
<p>The critical distinction is that consent orders are reached by <em>agreement</em>. The court's role is to review the agreement and confirm that it is just and equitable (for property orders) or in the best interests of the child (for parenting orders) — not to impose its own decision. If the court is satisfied, the orders are sealed and both parties receive a sealed copy. The whole process usually happens on the papers, without a hearing.</p>
<p>Consent orders are one of the most important tools in Australian family law. They give separated families the certainty of a court order with the efficiency and control of a negotiated agreement. Most are reached following family dispute resolution (mediation) or solicitor-led negotiation.</p>

<h2 id="types">Types of Consent Orders</h2>
<h3>Property and financial consent orders</h3>
<p>Property consent orders divide assets, liabilities and superannuation between the parties. They can cover the family home, investment properties, bank accounts, vehicles, business interests, share portfolios, and any debts. Superannuation splitting orders — which direct a portion of one party's superannuation to the other — are a common component of property orders and require a separate procedural step.</p>
<p>Property orders must be applied for within <strong>12 months of the date a divorce order takes effect</strong> (for married couples) or <strong>within 2 years of the end of a de facto relationship</strong>. Waiting beyond these time limits requires the court's permission — which is not automatically granted.</p>

<h3>Parenting consent orders</h3>
<p>Parenting consent orders cover all arrangements relating to children: where they live, how much time they spend with each parent, how major decisions (education, medical treatment, religion) are made, and how parents communicate about the children. They replace the older concept of "custody and access" and can be as detailed or as brief as the parents decide.</p>
<p>Parenting orders can be made without a divorce. They are available to any separated parents — married, de facto, or never-partnered — and can be applied for at any time. Unlike property orders, there is no time limit.</p>

<h3>Maintenance and spousal support orders</h3>
<p>In some cases, consent orders include ongoing spousal maintenance — regular payments from one party to the other, typically where one party has significantly lower earning capacity following the relationship. These are less common than property and parenting orders, and are always time-limited.</p>

<h2 id="process">The Consent Orders Process, Step by Step</h2>
<p>The process of obtaining consent orders involves more steps than many people expect. Understanding the sequence helps avoid delays — and mistakes that cause orders to be rejected.</p>
<ol>
<li><strong>Reach agreement.</strong> The parties must first agree on the terms. Most do this through mediation, solicitor-led negotiation, or direct discussion with legal advice. No agreement = no consent orders. This is where mediation is most valuable: it structures the conversation, surfaces issues early, and reaches durable agreements faster than litigation.</li>
<li><strong>Prepare the documents.</strong> A draft Minutes of Consent and an Application for Consent Orders (Form 11) must be prepared and filed with the court. The documents must use prescribed language and follow the court's formatting requirements. Errors in drafting are the most common reason applications are returned.</li>
<li><strong>Complete financial disclosure.</strong> For property orders, both parties must provide full disclosure of their financial position. Each party completes a financial statement disclosing assets, liabilities, income and superannuation. The duty of disclosure under the <em>Family Law Rules</em> is not optional — non-disclosure is a basis for setting aside orders later.</li>
<li><strong>File with the court.</strong> The Application for Consent Orders, Minutes of Consent, financial statements and any supporting documents are filed with the FCFCOA. The filing fee is currently $160 for consent orders (eligible concession cardholders may apply for a fee reduction).</li>
<li><strong>Registrar review.</strong> A judicial registrar reviews the application on the papers. They check that the orders are just and equitable (property) or in the best interests of the child (parenting). They may seek more information, request changes to the terms, or in rare cases list the matter for a short hearing.</li>
<li><strong>Orders sealed and issued.</strong> If approved, the court seals the orders. Both parties receive sealed copies. Property orders typically include a direction to the relevant title office, share registry, superannuation fund or other institution.</li>
</ol>

<h2 id="costs-timeline">Costs and Timeline: A Worked Example</h2>
<p>One of the most common questions we hear is: <em>what does it actually cost to get consent orders?</em> Here is a realistic worked example for a property settlement (home + superannuation, no children) reaching agreement through mediation.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Typical cost</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Initial legal advice</td><td>$300–$600 per party</td><td>One consult to understand your rights before negotiating</td></tr>
<tr><td>Family mediation</td><td>$1,800–$3,600 shared</td><td>One or two sessions; cost split between parties</td></tr>
<tr><td>Drafting consent orders</td><td>$600–$1,500</td><td>Solicitor-drafted; complexity varies</td></tr>
<tr><td>FCFCOA filing fee</td><td>$160</td><td>Per application; hardship waivers available</td></tr>
<tr><td>Superannuation split (if applicable)</td><td>$500–$1,000</td><td>Fund trustee approval process adds cost and time</td></tr>
<tr><td><strong>Total (typical range)</strong></td><td><strong>$2,400–$5,500</strong></td><td><strong>Per party; shared costs reduce the total significantly</strong></td></tr>
</tbody></table></div>
<p>Compare this to a contested property hearing, which commonly costs $30,000–$80,000 per party (FCFCOA figures) and takes 12–24 months to reach a final hearing. The financial case for reaching agreement — and formalising it through consent orders — is overwhelming for the vast majority of separations.</p>
<p><strong>Timeline from agreement to sealed orders:</strong> once the application is filed, approval typically takes <strong>6–12 weeks</strong> for straightforward property matters. Complex matters or those involving superannuation splitting orders may take longer. Parenting consent orders with no financial component can be faster.</p>

<blockquote><p>"The biggest mistake people make with consent orders is waiting. Property orders have a time limit — 12 months from the divorce order for married couples. We've had clients come to us after the window had passed who had to apply to the court for special leave just to formalise an agreement they'd already reached. Start the process while it's still straightforward." — Dan Toombs, Founder, Mediations Australia</p></blockquote>

<h2 id="consent-orders-vs-bfa">Consent Orders vs Binding Financial Agreements</h2>
<p>The other common way to formalise a financial settlement is through a binding financial agreement (BFA), sometimes called a "pre-nup" or "post-nup." The two mechanisms are quite different:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Consent orders</th><th>Binding financial agreement</th></tr></thead>
<tbody>
<tr><td><strong>Court involvement</strong></td><td>Yes — court reviews and approves</td><td>No — purely private contract</td></tr>
<tr><td><strong>Legal advice required</strong></td><td>Not mandatory (but strongly advised)</td><td>Yes — both parties must get independent legal advice</td></tr>
<tr><td><strong>Can cover superannuation splitting</strong></td><td>Yes, with trustee involvement</td><td>Yes, for regulated super funds</td></tr>
<tr><td><strong>Easier to set aside</strong></td><td>Harder — court order</td><td>Easier — more grounds for challenge</td></tr>
<tr><td><strong>Cost to set aside</strong></td><td>High — needs court proceedings</td><td>Lower — contract law principles apply</td></tr>
<tr><td><strong>Best for</strong></td><td>Most post-separation settlements</td><td>Pre-nuptial agreements; complex business arrangements</td></tr>
</tbody></table></div>
<p>For most post-separation property settlements, consent orders are the preferred option because the court's involvement provides certainty and makes the orders harder to challenge later. BFAs are typically used for pre-nuptial or post-nuptial arrangements, or where the parties have specific reasons for wanting to keep the settlement entirely private.</p>

<h2 id="after">After Consent Orders Are Made</h2>
<p>Once consent orders are sealed, both parties are bound by their terms. Non-compliance is a serious matter: the court can impose penalties including fines, enforcement orders, or in extreme cases, imprisonment.</p>
<p>For property orders, the practical steps following sealing typically include:</p>
<ul>
<li>Transferring title of real property (the solicitor prepares the transfer documents and lodges them with the title office)</li>
<li>Refinancing the mortgage if one party is retaining the family home</li>
<li>Splitting or rolling over superannuation (each fund trustee has its own process and timeframes — typically 2–4 weeks after receiving the sealed order)</li>
<li>Transferring or selling vehicles, shares and other assets as specified</li>
<li>Closing or separating joint accounts and liabilities</li>
</ul>
<p>For parenting orders, the transition to the new arrangements should be planned carefully, especially where children are involved. We recommend explaining the new arrangements to children in age-appropriate terms and giving them time to adjust — changes in living arrangements are significant for children regardless of how well-planned they are.</p>

<h2 id="vary">Can Consent Orders Be Changed?</h2>
<p>Consent orders can be varied, but not easily — and the threshold is higher for property orders than for parenting orders.</p>
<p><strong>Property consent orders</strong> can be set aside or varied in limited circumstances: if there has been a significant miscarriage of justice due to fraud, non-disclosure, duress or a material change in circumstances, or if circumstances have changed so dramatically that compliance would be impractical or cause significant injustice. This is a high bar. The court's reluctance to reopen settled property matters is by design — finality is one of the main benefits of consent orders.</p>
<p><strong>Parenting consent orders</strong> are easier to vary, because the best interests of the child remain paramount and children's circumstances change. A significant change in circumstances — a parent relocating, a child's needs changing, a new safety concern — provides grounds to apply to vary. Many parenting matters are reviewed as children age.</p>
<p>If you expect your parenting arrangements to evolve, it is worth considering a parenting plan (less formal, more flexible) alongside or instead of consent orders, or building review points into the consent orders themselves.</p>

<h2 id="2025-changes">2025 Family Law Act Changes and Consent Orders</h2>
<p>The <em>Family Law Amendment Act 2024</em> made significant changes that took effect in 2025, and they have implications for consent orders:</p>
<p><strong>Property settlements:</strong> The 2025 amendments (following the High Court's Ascot Investments / Shinohara decision) have largely resolved the controversial "add-backs" debate. Courts can no longer routinely add back to the property pool amounts that one party spent before trial — which changes the negotiation landscape for property settlements. If your separation predates 2025 and a property settlement was being negotiated under earlier principles, it is worth reviewing the position with a lawyer.</p>
<p><strong>Parenting matters:</strong> The 2023 amendments (already in force before 2025) removed the presumption of equal shared parental responsibility. Courts now focus purely on the best interests of the child, without a default presumption toward equal time or equal responsibility. Consent orders for parenting arrangements should reflect this: rather than anchoring on "equal time," they should focus on what actually works for the child. Our mediators ensure parenting agreements reflect the post-2023 legal landscape.</p>
<p><strong>Financial agreements:</strong> The Albanese government flagged reforms to binding financial agreements in 2024, potentially requiring legal advice to be certified in a prescribed form. If you are considering a BFA rather than consent orders, take current legal advice on the requirements.</p>
<p>These changes reinforce the case for getting consent orders formalised by people who understand the current law — not templates from the internet.</p>

<p><a href="/book-a-consultation/" class="btn btn-primary">Talk to a Mediator — Free Consultation</a></p>

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Do I need a lawyer to get consent orders?</h3>
<p>You don't legally need a lawyer, but it is strongly advisable for property matters. Errors in drafting consent orders — wrong terminology, incomplete financial disclosure, incorrect superannuation procedures — are the most common reason applications are returned or, worse, result in orders that don't do what the parties intended. Most people engage a solicitor to draft the Minutes of Consent, even when they've negotiated the terms themselves through mediation.</p>

<h3>Can I do consent orders without court?</h3>
<p>Not for formal consent orders — the court must approve and seal them. However, the process almost always happens entirely on the papers (no court attendance required). You file the application and, 6–12 weeks later, receive your sealed orders. The exception is where the registrar identifies a concern and lists the matter for a short hearing — this is uncommon.</p>

<h3>What happens if one party refuses to sign?</h3>
<p>Consent orders require both parties' signatures. If one party refuses, you cannot obtain consent orders — you would need to apply for orders through the contested litigation process, or try mediation first to reach agreement. An accredited mediator can often help parties who are "almost there" find the final point of agreement.</p>

<h3>How long do consent orders take to be approved?</h3>
<p>Once filed, most straightforward consent orders are approved in 6–12 weeks. Complex matters, or those involving superannuation splitting, may take longer. The registrar may also request additional information, which adds time. Filing complete and correct documents from the start is the best way to avoid delays.</p>

<h3>Can consent orders cover superannuation?</h3>
<p>Yes. Superannuation splitting orders can be included in consent orders for most regulated super funds. The process requires notification to the fund trustee, who has 28 days to flag any concerns. Once the orders are sealed, the trustee implements the split as directed. Self-managed superannuation funds (SMSFs) have additional complexity — get specialist advice.</p>

<h3>What is the difference between consent orders and a parenting plan?</h3>
<p>A parenting plan is a written agreement signed by both parents, but it is not a court order — it is not directly enforceable. Consent orders are court-approved and enforceable. Many families start with a parenting plan for flexibility, then formalise arrangements through consent orders as they stabilise. If you think arrangements may need adjusting as children grow, a parenting plan (or consent orders with built-in review points) is worth considering.</p>

<h3>What if I need to change consent orders?</h3>
<p>Property consent orders can be set aside on limited grounds (fraud, non-disclosure, significant change in circumstances). Parenting consent orders can be varied where there has been a significant change in circumstances. In both cases, mediation is worth trying before going to court — and is often required for parenting matters.</p>

<h3>Are consent orders the same as a divorce?</h3>
<p>No. Divorce legally ends a marriage — it does not divide property or determine parenting arrangements. Consent orders (or a contested hearing) do that. You can apply for divorce without having finalised property or parenting matters, but the 12-month time limit for property consent orders starts running from the date the divorce order takes effect. Don't confuse the two processes.</p>"""
    },


    # ── AI-Overview-resistant cornerstones ────────────────────────────────────
    "best-apps-for-separated-parents": {
        "title": "Best Apps for Separated Parents in Australia (2025)",
        "desc":  "An accredited mediator's guide to the best co-parenting apps for separated Australian parents — what works, what to avoid, and how to pick one that holds up in court.",
        "h1":    "Best Apps for Separated Parents in Australia (2025)",
        "read_min": "9",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> The best co-parenting app for separated Australian parents is one that both parties will actually use. In 2025, <strong>OurFamilyWizard</strong> and <strong>Talking Parents</strong> are the leading court-admissible options with tamper-proof message logs, while <strong>AppClose</strong> and <strong>Cozi</strong> suit lower-conflict situations. No app replaces a formalised parenting plan or consent orders — but the right one dramatically reduces misunderstandings and conflict between sessions.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#why-apps-matter">Why co-parenting apps matter after separation</a></li>
<li><a href="#top-apps">Top co-parenting apps: comparison table</a></li>
<li><a href="#ourfamilywizard">OurFamilyWizard — best for court-admissible records</a></li>
<li><a href="#talking-parents">Talking Parents — best free court-ready option</a></li>
<li><a href="#appclose">AppClose — best for lower-conflict co-parenting</a></li>
<li><a href="#what-to-look-for">What to look for when choosing an app</a></li>
<li><a href="#app-and-mediation">How apps fit into mediation and parenting plans</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="why-apps-matter">Why Co-Parenting Apps Matter After Separation</h2>
<p>Most post-separation conflict doesn't happen in a courtroom — it happens in text messages, missed pickups and arguments about who said what three months ago. Co-parenting apps don't solve conflict, but they do three things that dramatically reduce it: they keep all communication in one documented place, they create schedules both parties can see in real time, and they produce records that are admissible if matters escalate.</p>
<p>As an accredited family mediator, I see the same pattern repeatedly: families who use a dedicated co-parenting app have measurably lower communication conflict by the time they reach a second mediation session (if they need one at all). The accountability a shared platform creates — where both parties know every message is logged and timestamped — changes the tone of communication almost immediately.</p>
<p>That said, an app is a tool, not a solution. It works best when it sits alongside a properly documented parenting plan or consent orders that set out the rules clearly — because an app can record what was said, but it can't enforce what was agreed.</p>

<h2 id="top-apps">Top Co-Parenting Apps: Comparison Table</h2>
<figure class="tbl"><table>
<thead><tr><th>App</th><th>Cost</th><th>Court-admissible logs</th><th>Shared calendar</th><th>Expense tracking</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><strong>OurFamilyWizard</strong></td><td>~$99–$199/yr per parent</td><td>Yes — certified</td><td>Yes</td><td>Yes</td><td>High-conflict; court proceedings</td></tr>
<tr><td><strong>Talking Parents</strong></td><td>Free (premium ~$9.99/mo)</td><td>Yes — unalterable</td><td>Yes</td><td>Basic</td><td>Any conflict level; budget-conscious</td></tr>
<tr><td><strong>AppClose</strong></td><td>Free (premium ~$9.99/mo)</td><td>Limited</td><td>Yes</td><td>Yes</td><td>Lower conflict; practical co-parenting</td></tr>
<tr><td><strong>Cozi</strong></td><td>Free (premium ~$29.99/yr)</td><td>No</td><td>Yes</td><td>No</td><td>Low conflict; blended families</td></tr>
<tr><td><strong>2Houses</strong></td><td>~$10/mo</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Financial transparency; EU-origin</td></tr>
</tbody></table></figure>

<h2 id="ourfamilywizard">OurFamilyWizard — Best for Court-Admissible Records</h2>
<p>OurFamilyWizard (OFW) is the most widely used co-parenting platform in Australian family law proceedings. Its key differentiator is the <strong>ToneMeter</strong> — an AI tool that flags hostile or inflammatory language before a message is sent — and its certified, tamper-proof message logs that courts accept as evidence without additional authentication.</p>
<p>OFW is particularly useful where there has been a history of disputed communications, where matters are already before the court, or where one party has a pattern of rewriting history. The ability to generate a printable, certified communication log that a judge, registrar or family report writer can review has real practical value.</p>
<p>The cost (~$99–$199 per parent per year) is higher than alternatives, but for families in litigation or high-conflict situations it is modest compared to the legal costs of disputed communications. Many family lawyers now recommend OFW as standard in contested parenting matters.</p>
<blockquote><p>"I recommend OurFamilyWizard to clients who are in, or likely to enter, contested proceedings. The certified logs remove an enormous source of dispute — whether a message was sent, what it said, and how it was worded. That dispute resolution cost alone often justifies the subscription." — Dan Toombs, Founder, Mediations Australia</p></blockquote>

<h2 id="talking-parents">Talking Parents — Best Free Court-Ready Option</h2>
<p>Talking Parents offers unalterable message logs and a shared calendar at no cost, with premium features (phone call recording, additional storage) available for around $9.99/month. It is the strongest free option for parents who need court-admissible communication records but don't require the full feature set of OurFamilyWizard.</p>
<p>Messages in Talking Parents cannot be edited or deleted by either party once sent — the immutability of the record is its main selling point. This makes it suitable for parenting matters that may proceed to the court, without the OFW price tag.</p>
<p>For the majority of separated Australian families who are not in active litigation but want a documented record as a precaution, Talking Parents offers the best combination of functionality and cost.</p>

<h2 id="appclose">AppClose — Best for Lower-Conflict Co-Parenting</h2>
<p>AppClose is designed for practical co-parenting rather than dispute management. It includes a shared calendar, expense tracking, a journal for documenting child-related events, and basic messaging — but its communication logs are not court-certified in the same way as OFW or Talking Parents.</p>
<p>For separated families with low to medium conflict who primarily need schedule coordination and expense splitting, AppClose is easier to use and introduces less adversarial friction than a court-focused platform. The expense tracking feature is particularly useful for managing child-related costs where both parents contribute.</p>

<h2 id="what-to-look-for">What to Look For When Choosing an App</h2>
<p>Beyond the specific platforms above, the right co-parenting app for your family depends on:</p>
<ul>
<li><strong>Conflict level.</strong> High conflict or active proceedings → OurFamilyWizard. Lower conflict → AppClose or Cozi. Uncertain → Talking Parents (scales either way).</li>
<li><strong>Whether both parties will use it.</strong> The best app in the world doesn't work if one party refuses to engage. Start with something simple if buy-in is uncertain — you can always upgrade.</li>
<li><strong>Expense tracking needs.</strong> If child costs are a source of conflict, choose an app with built-in expense logging and request/approval workflows.</li>
<li><strong>Device compatibility.</strong> All major apps support iOS and Android. Confirm web browser access if either parent doesn't have a smartphone.</li>
<li><strong>Privacy from new partners.</strong> Consider whether notifications or shared accounts could create issues with new relationships.</li>
</ul>

<h2 id="app-and-mediation">How Apps Fit Into Mediation and Parenting Plans</h2>
<p>A co-parenting app is most effective when it sits alongside a properly documented parenting arrangement — either a <a href="/parenting-plan-mediation/">parenting plan</a> agreed through mediation, or <a href="/consent-orders/">consent orders</a> approved by the court. The app provides the communication infrastructure; the plan provides the rules.</p>
<p>In mediation, we often help separating parents agree on which app they'll use and how — for example, agreeing that all child-related communication happens through the app (not text messages), that each party responds within 24 hours to time-sensitive messages, and that financial requests for child-related expenses are submitted through the app's expense tool. These agreements can be written into the parenting plan itself.</p>
<p>If you're at the stage of choosing a co-parenting app, you may also be at the stage where mediation can help establish the parenting arrangements the app will support. <a href="/parenting-plan-mediation/">Read more about parenting plan mediation →</a></p>
<p><a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation</a></p>

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Are co-parenting app messages admissible in Australian court?</h3>
<p>OurFamilyWizard and Talking Parents both produce certified, unalterable message logs that Australian family courts accept as evidence without additional authentication steps. Standard text messages are also admissible but can be disputed — the advantage of a dedicated platform is the tamper-proof, timestamped record. If there is any prospect of court proceedings, use a court-ready platform from the start.</p>

<h3>Can I be forced to use a particular co-parenting app?</h3>
<p>A court can include a direction to use a specific co-parenting app as part of a parenting order, and this happens in high-conflict cases. More commonly, app use is agreed between the parties — either directly or through mediation — and written into a parenting plan. If your co-parent refuses to use any app, document your communications carefully in whatever medium they use.</p>

<h3>What if my co-parent won't use a co-parenting app?</h3>
<p>You can't force a co-parent to use an app outside of a court order. If they won't engage with any communication platform, the practical alternative is to keep all communications in writing (email or text) and save records systematically. If communication breakdown is serious, mediation can help establish communication protocols — and an app recommendation is often part of that outcome.</p>

<h3>Is there a free co-parenting app with court-admissible logs?</h3>
<p>Yes — Talking Parents offers unalterable message logs at no cost (the free tier includes the core court-ready features). OurFamilyWizard requires a paid subscription but has more comprehensive features. For the majority of separated parents who need court-ready records without active litigation costs, Talking Parents is the best free option.</p>

<h3>Do I need a co-parenting app if I have consent orders?</h3>
<p>Consent orders set out the rules — a co-parenting app helps implement them day-to-day and creates a record if compliance is later disputed. Most families benefit from using both. An app doesn't replace the legal framework consent orders provide; it makes living within that framework smoother and less conflictual.</p>"""
    },

    "my-ex-wont-sign-divorce-papers": {
        "title": "My Ex Won't Sign Divorce Papers: What Happens Next",
        "desc":  "In Australia, your ex cannot block a divorce by refusing to sign. Here's exactly what to do — step by step — including how mediation can resolve the underlying dispute.",
        "h1":    "My Ex Won't Sign Divorce Papers: What Happens Next",
        "read_min": "8",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> In Australia, your ex cannot prevent a divorce by refusing to sign. After 12 months of separation, one party can apply for divorce without the other's consent — the court doesn't require both signatures. What your ex CAN complicate is the property settlement and parenting arrangements. That's where mediation matters most.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#can-they-stop-it">Can my ex actually stop the divorce?</a></li>
<li><a href="#how-divorce-works">How Australian divorce works — the 12-month rule</a></li>
<li><a href="#one-party-application">Applying for divorce without your ex's agreement</a></li>
<li><a href="#what-they-can-dispute">What your ex CAN dispute — and what to do about it</a></li>
<li><a href="#timeline">Realistic timeline: from application to finalised</a></li>
<li><a href="#mediation-role">Where mediation fits in</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="can-they-stop-it">Can My Ex Actually Stop the Divorce?</h2>
<p>No. Under Australian law, divorce cannot be blocked by one party refusing to sign or engage with the process. This is a fundamental feature of Australia's no-fault divorce system, which was introduced with the <em>Family Law Act 1975</em>. Neither party has to prove fault, and neither party has the power to prevent the other from divorcing once the legal requirements are met.</p>
<p>What your ex CAN do is make the associated matters — property settlement, parenting arrangements, spousal maintenance — more difficult to resolve. And those are the things that actually affect your life long-term. The divorce itself is a legal formality; it's the financial and parenting outcomes that deserve your attention.</p>

<h2 id="how-divorce-works">How Australian Divorce Works — the 12-Month Rule</h2>
<p>To apply for divorce in Australia, you must have been separated for at least 12 months. "Separated" means you have been living apart — emotionally, practically, or in some cases physically within the same home. You don't need your ex's agreement or signature to establish that you are separated.</p>
<p>Key points about the Australian divorce process:</p>
<ul>
<li><strong>No fault required.</strong> The only ground for divorce in Australia is irretrievable breakdown of the marriage, established by 12 months' separation. You don't need to prove anything about why the relationship ended.</li>
<li><strong>One party can apply.</strong> Either party can file a sole application for divorce. The other party is served with the application but cannot veto it.</li>
<li><strong>Children's welfare is assessed separately.</strong> Where there are children under 18, the court checks that satisfactory arrangements are in place — but this is a separate consideration, not a reason to refuse the divorce itself.</li>
<li><strong>Time limits on property orders.</strong> You have 12 months from the date the divorce order takes effect to apply for property consent orders or court orders. Missing this deadline requires the court's permission — which is not automatic.</li>
</ul>

<h2 id="one-party-application">Applying for Divorce Without Your Ex's Agreement</h2>
<p>A sole application for divorce is straightforward. You file through the <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a>. The steps are:</p>
<ol>
<li><strong>Confirm 12 months' separation.</strong> You'll need to state the date of separation in the application.</li>
<li><strong>File the application.</strong> Online via the FCFCOA portal. The filing fee is currently $1,060 (reduced fee for eligible concession cardholders).</li>
<li><strong>Serve your ex.</strong> For a sole application, you must serve your ex with the application at least 28 days before the hearing (42 days if they're overseas). You cannot serve them yourself — this must be done by someone else (a process server, friend, or family member over 18).</li>
<li><strong>Attend the hearing (if required).</strong> If you have children under 18, you generally need to attend. Without children under 18, attendance is usually not required for a sole application.</li>
<li><strong>Divorce order takes effect.</strong> One month and one day after the court makes the order.</li>
</ol>
<p>If your ex cannot be located for service, there are substituted service orders available. If your ex is overseas, different timelines apply but the process is essentially the same.</p>

<h2 id="what-they-can-dispute">What Your Ex CAN Dispute — and What To Do About It</h2>
<p>While your ex cannot stop the divorce, they can make property and parenting matters contentious. This is where most of the real conflict — and cost — sits.</p>
<figure class="tbl"><table>
<thead><tr><th>Matter</th><th>Can ex block?</th><th>Time limit</th><th>Best first step</th></tr></thead>
<tbody>
<tr><td>The divorce itself</td><td>No</td><td>Apply after 12 months separation</td><td>Sole application to FCFCOA</td></tr>
<tr><td>Property settlement</td><td>Can delay and complicate</td><td>12 months from divorce order</td><td>Mediation first; court if necessary</td></tr>
<tr><td>Parenting arrangements</td><td>Can dispute terms (not your right to apply)</td><td>No time limit</td><td>Family dispute resolution (mediation)</td></tr>
<tr><td>Spousal maintenance</td><td>Can dispute amount/duration</td><td>12 months from divorce order</td><td>Mediation or legal negotiation</td></tr>
</tbody></table></figure>
<p>For property matters, the 12-month window after the divorce order is critical. Many people focus on the divorce and miss the fact that their property settlement clock is now running. Don't let the deadline pass.</p>

<h2 id="timeline">Realistic Timeline: From Application to Finalised</h2>
<p>Here is a realistic worked timeline for a sole divorce application in Australia:</p>
<ul>
<li><strong>Week 1:</strong> File sole application online with FCFCOA. Pay $1,060 filing fee (or reduced amount if eligible).</li>
<li><strong>Weeks 1–3:</strong> Arrange service on your ex (process server ~$150–$300 typically).</li>
<li><strong>4 weeks before hearing:</strong> Service must be complete.</li>
<li><strong>Hearing date:</strong> Usually 6–10 weeks after filing. Typically 5–10 minutes if uncontested and no children under 18.</li>
<li><strong>+1 month + 1 day:</strong> Divorce order takes effect. Property settlement clock starts.</li>
<li><strong>Total from filing to final order:</strong> Usually 3–4 months.</li>
</ul>
<blockquote><p>"The question I hear most from people whose ex 'won't cooperate' is whether they can be stopped. The answer is no — but that relief is often followed by: 'So what do I do about the house?' That's the real question, and it's the one mediation is designed to answer. We help both parties reach a property and parenting agreement without court, which is almost always faster, cheaper and less damaging than litigation." — Dan Toombs, Founder, Mediations Australia</p></blockquote>

<h2 id="mediation-role">Where Mediation Fits In</h2>
<p>Mediation doesn't affect the divorce application itself — that proceeds regardless. What mediation does is resolve the matters your ex CAN complicate: the property settlement, the parenting arrangements, superannuation splitting and any maintenance.</p>
<p>For parenting matters, <a href="/family-law-mediation/">family dispute resolution</a> is legally required before most parenting applications can be filed with the court. For property matters, it's not mandatory but it is almost always faster and cheaper than litigation — particularly given the 12-month window that runs from the divorce order date.</p>
<p>In our experience, even high-conflict situations can reach resolution through mediation when the parties are properly prepared and the process is well-structured. The fact that your ex "won't cooperate" on the divorce doesn't mean they won't engage in a mediated property or parenting process — the incentive to avoid court costs is powerful for both parties.</p>
<p><a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation</a></p>

<h2 id="faq">Frequently Asked Questions</h2>

<h3>What if my ex ignores the divorce application after being served?</h3>
<p>If your ex is properly served but doesn't respond, the divorce proceeds without them. They don't need to reply, agree, or attend the hearing. Ignoring a divorce application doesn't stop it — the court will grant the order if the legal requirements are satisfied.</p>

<h3>Can my ex contest the divorce on the grounds that the marriage isn't over?</h3>
<p>Technically, your ex can file a response disputing that 12 months of separation has occurred. In practice, this is very rarely successful — especially where both parties have been living separately, told others about the separation, or have existing interim parenting or financial arrangements. Courts are rarely persuaded that a marriage hasn't broken down when one party has filed for divorce.</p>

<h3>Does my ex have to attend the hearing?</h3>
<p>For a sole application, no. Your ex is served with the application and can attend if they wish, but they are not required to. The hearing is usually brief (5–10 minutes) and uncontested if the legal requirements are met.</p>

<h3>What happens to the property if my ex won't agree to a settlement?</h3>
<p>If your ex won't negotiate a property settlement, you have two options: apply to the court for property orders (contested litigation), or seek court-ordered mediation first. Litigation can take 12–24 months and cost $30,000–$80,000+ per party. Most property matters are resolved before a contested hearing — but the process of filing and negotiating under litigation pressure is expensive. Starting with mediation avoids this entirely for the majority of cases.</p>

<h3>Is there a time limit on property settlements after divorce?</h3>
<p>Yes — 12 months from the date the divorce order takes effect. After this, you need the court's permission to apply for property orders, which is not automatically granted. Don't let this window pass. If your ex won't negotiate, begin the mediation or legal process well before the 12-month deadline.</p>

<h3>We separated but haven't formally divorced. Does the 12-month rule still apply?</h3>
<p>For a divorce application, yes — you need 12 months of separation. But property and parenting applications can be made without a divorce. For de facto couples, property time limits run from the end of the relationship (not a divorce order) — generally 2 years. If you're uncertain about the timeline that applies to your situation, get legal advice promptly.</p>"""
    },

    "who-pays-bills-during-separation": {
        "title": "Who Pays the Bills During Separation in Australia?",
        "desc":  "Understand exactly who is responsible for the mortgage, utilities, car loans and credit cards during separation — and what to do when your ex stops paying.",
        "h1":    "Who Pays the Bills During Separation in Australia?",
        "read_min": "9",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> During separation, both parties remain legally responsible for any <em>joint</em> debt — regardless of who lives in the property or uses the asset. Individual debts stay with the named person. The family court does not intervene in day-to-day bills while you are separated, but it can make interim orders and will consider financial conduct when dividing the asset pool. The practical answer: document everything, get an interim agreement in place quickly, and don't let unresolved bills become a lever in the property settlement.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#joint-vs-individual">Joint debts vs individual debts: who owes what</a></li>
<li><a href="#mortgage">The family home mortgage during separation</a></li>
<li><a href="#utilities">Utilities, rates and household bills</a></li>
<li><a href="#credit-cards">Credit cards and personal loans</a></li>
<li><a href="#car">Car loans and vehicle expenses</a></li>
<li><a href="#when-ex-stops">When your ex stops paying</a></li>
<li><a href="#interim-agreements">Getting an interim financial agreement</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="joint-vs-individual">Joint Debts vs Individual Debts: Who Owes What</h2>
<p>The starting point is straightforward: a creditor (bank, utility company, landlord) looks at whose name is on the account. If you're both named, you're both liable — regardless of what your separation agreement says. If only one person is named, only that person is liable to the creditor, even if the other person benefited from or incurred the debt.</p>
<p>This distinction matters because separation agreements or consent orders operate between the two of you — they don't change your obligations to third-party creditors. A consent order saying "your ex will pay the mortgage" doesn't stop the bank coming after you if they don't pay, because the bank isn't party to your consent order.</p>
<figure class="tbl"><table>
<thead><tr><th>Debt type</th><th>Who owes the creditor?</th><th>What happens in the property settlement?</th></tr></thead>
<tbody>
<tr><td>Joint mortgage</td><td>Both parties jointly and severally</td><td>Included in asset pool; allocated with property</td></tr>
<tr><td>Joint credit card</td><td>Both parties</td><td>Included as liability in the pool</td></tr>
<tr><td>Individual mortgage (one name)</td><td>The named party only</td><td>Still included in the asset pool</td></tr>
<tr><td>Individual credit card</td><td>The named party only</td><td>May be included if used for family expenses</td></tr>
<tr><td>Utilities in one name</td><td>The named party only</td><td>Rarely included; treated as living expenses</td></tr>
<tr><td>Car loan in one name</td><td>The named party only</td><td>Included as liability attached to the vehicle</td></tr>
</tbody></table></figure>

<h2 id="mortgage">The Family Home Mortgage During Separation</h2>
<p>The family home mortgage is usually the biggest financial issue during separation. The practical questions are: who stays in the house, who pays the mortgage, and what happens to it in the property settlement?</p>
<p>If the mortgage is in both names, both parties remain legally liable to the bank regardless of who lives there. If the person staying in the house stops paying, the bank can pursue both of you — including affecting both credit ratings.</p>
<p>Common interim arrangements:</p>
<ul>
<li><strong>One party stays and pays.</strong> The remaining party pays the mortgage. The leaving party's continuing contribution is acknowledged in the property settlement (typically by an adjustment in their favour at settlement, or by the staying party receiving the property and refinancing into their sole name).</li>
<li><strong>One party stays, both continue paying.</strong> Less common, but used where the leaving party can't immediately refinance off the loan and both parties can afford to maintain repayments.</li>
<li><strong>Property is sold.</strong> Where neither party can maintain the mortgage alone, or neither wants the property, the home is sold and proceeds divided — either by agreement or court order.</li>
</ul>
<p>Whatever arrangement you reach, document it formally as quickly as possible — either through a <a href="/parenting-plan-mediation/">parenting and financial agreement</a> reached in mediation, or through interim consent orders.</p>

<h2 id="utilities">Utilities, Rates and Household Bills</h2>
<p>Ongoing household bills — electricity, gas, water, internet, rates — are generally treated as living expenses and aren't directly part of the property settlement. Who pays them during separation depends on who lives in the property and whose name is on the accounts.</p>
<p>If one party remains in the family home, it's generally expected that they pay the ongoing utilities and rates as part of their occupancy costs. If the property is rented out, rates and utilities become part of the rental income/expense calculation.</p>
<p>Council rates present a specific issue: they're usually payable by the owner(s) regardless of who occupies the property. If both names are on the title, both are legally responsible for rates arrears. Local councils can pursue unpaid rates against the property itself, which complicates any future sale.</p>

<h2 id="credit-cards">Credit Cards and Personal Loans</h2>
<p>Joint credit cards remain the liability of both card holders until the account is closed or refinanced into one person's name. During separation, both parties can typically continue to use a joint card — which is a significant risk if one party is spending freely in anticipation of a property settlement.</p>
<p>Practical steps to take early in separation:</p>
<ul>
<li>Freeze or close joint credit card accounts, or at minimum remove one party's card</li>
<li>Obtain your credit reports (free from Equifax, Illion or Experian) to identify all joint accounts</li>
<li>Request removal as a joint account holder where possible — note this requires the other party's cooperation or refinancing into a sole name</li>
<li>Document any large post-separation expenditure on joint accounts, as this may be relevant to the property settlement</li>
</ul>
<blockquote><p>"The issue I see most frequently in property mediation isn't a complicated asset structure — it's that one party has continued to incur joint debt during separation without the other's knowledge or agreement. By the time people reach mediation, the credit card debt has grown significantly and both parties are jointly liable. The earlier you get an interim financial agreement in place, the better." — Dan Toombs, Founder, Mediations Australia</p></blockquote>

<h2 id="car">Car Loans and Vehicle Expenses</h2>
<p>Car loans are typically in one party's name and attached to the specific vehicle. The loan stays with the named borrower in the eyes of the lender — even if the other party drives the car after separation. In the property settlement, the vehicle and its associated loan are included in the asset pool: the vehicle is an asset, the loan is a liability.</p>
<p>If the vehicle is in joint names or the loan is joint, both parties are liable to the lender regardless of who has possession of the car. As with credit cards, having possession of the vehicle doesn't protect you from liability under a joint loan if the other party stops paying.</p>

<h2 id="when-ex-stops">When Your Ex Stops Paying</h2>
<p>If your ex stops contributing to joint debts — the mortgage, credit cards, car loans — you face a choice: cover the payments yourself, let the debt default, or take legal action.</p>
<p>Letting joint debt default affects both parties' credit ratings and can result in enforcement action against the property. It's almost always the worst financial outcome. Covering the payments yourself preserves your credit rating and the asset, but creates an ongoing imbalance that should be documented and addressed in the property settlement.</p>
<p>If your ex is refusing to pay joint debts in a way that puts an asset at serious risk, you can apply to the court for urgent interim orders. The court can make orders requiring a party to maintain mortgage payments or other critical financial obligations pending the final property settlement. This is a measure of last resort — most situations are resolved more quickly and cheaply through mediation.</p>
<p>Whatever you pay in excess of your agreed share during separation should be documented — bank statements, loan statements, payment records — as it is directly relevant to the property settlement.</p>

<h2 id="interim-agreements">Getting an Interim Financial Agreement</h2>
<p>The most effective way to manage ongoing bills during separation is an interim financial agreement — a documented arrangement covering who pays what while the property settlement is being negotiated. This doesn't have to be a formal legal document initially, but it should be in writing and signed by both parties.</p>
<p>Mediation is the most efficient way to reach an interim financial agreement. In a single session, a mediator can help both parties agree on mortgage contributions, household bills, debt management and any maintenance arrangements — producing a written agreement both parties sign. This can then be formalised through <a href="/consent-orders/">consent orders</a> if needed.</p>
<p>An interim agreement reduces the risk of one party incurring debt unilaterally, gives both parties clarity about their financial obligations, and reduces the scope for financial conflict during what is already a stressful period.</p>
<p><a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation</a></p>

<h2 id="faq">Frequently Asked Questions</h2>

<h3>Do I have to keep paying the mortgage if I've moved out?</h3>
<p>If your name is on the mortgage, you remain legally liable to the bank regardless of whether you live in the property. Stopping payments will affect your credit rating and may trigger enforcement action. The practical solution is to reach an interim agreement — through mediation or direct negotiation — about how mortgage payments will be managed pending the property settlement. Your ongoing payments can be factored into the final property division.</p>

<h3>Can my ex run up debt on a joint account without my consent?</h3>
<p>Yes — both account holders can typically use a joint account until it is frozen or closed, even after separation. If you're concerned about post-separation spending on joint accounts, freeze or close them as soon as possible. Post-separation expenditure may be relevant to the property settlement, but it's easier to prevent than to remedy.</p>

<h3>What counts as "wastage" of marital assets during separation?</h3>
<p>Following the High Court's Ascot Investments decision (effective 2025), courts can no longer automatically add back amounts one party spent before trial. However, deliberate waste, reckless spending or disposal of assets to defeat the other party's claims can still be considered in the property settlement in appropriate circumstances. Courts look at the full financial conduct of both parties — keeping records of significant financial transactions during separation is advisable.</p>

<h3>Can the court make my ex pay the bills?</h3>
<p>The court can make interim orders requiring a party to maintain mortgage payments or other obligations pending the final property settlement. In practice, interim orders are sought where there is an urgent risk to a significant asset — for example, imminent mortgage default. They are not routine; the court expects parties to try mediation and negotiation first. An urgent interim hearing is available in genuinely time-critical situations.</p>

<h3>How do ongoing bills affect the property settlement?</h3>
<p>All significant debts — mortgage, car loans, credit cards — are included in the asset pool. Who paid what during separation is relevant context for the settlement, particularly if one party has been paying joint obligations the other has abandoned. Document your payments carefully. An unequal financial contribution during separation is a factor courts and mediators take into account when dividing assets.</p>

<h3>We have children — does that affect who pays the bills?</h3>
<p>The parent with primary care of the children often has a stronger case for remaining in the family home (which affects who pays the mortgage). Child support — the financial transfer between parents for the cost of raising children — is separate from property settlement bills and is calculated under the Child Support Scheme administered by Services Australia. Child support payments are not a substitute for property settlement, and do not offset each other.</p>"""
    },

    "five-things-to-do-before-uttering-i-want-a-divorce": {
        "title": "Five Things to Do Before You Say 'I Want a Divorce'",
        "desc":  "Before you say 'I want a divorce', these five steps protect your finances, your children and your future. A practical guide from an accredited mediator.",
        "h1":    "Five Things to Do Before You Say 'I Want a Divorce'",
        "read_min": "7",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> The words "I want a divorce" cannot be unsaid. Before you say them, five practical steps — from understanding your financial position to exploring alternatives to court — can protect your assets, preserve your parenting relationship, and keep control of the outcome in your hands.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#understand-finances">1. Understand your financial position</a></li>
<li><a href="#get-legal-advice">2. Get independent legal advice</a></li>
<li><a href="#think-about-children">3. Put your children first</a></li>
<li><a href="#explore-mediation">4. Explore mediation before court</a></li>
<li><a href="#protect-documents">5. Protect and copy important documents</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="understand-finances">1. Understand Your Financial Position</h2>
<p>Before a separation conversation begins, get a clear picture of the shared financial landscape. Many people are surprised to discover how much — or how little — they actually know about their household finances.</p>
<p>Make a list of all assets and liabilities: the family home and its current market value, any investment properties, superannuation balances (yours and your partner's), bank accounts, share portfolios, vehicles, and any outstanding debts including mortgages, personal loans and credit cards.</p>
<p>This matters for two reasons. First, it gives you a realistic view of what a property settlement might look like. Second, it prevents assets from disappearing or being moved in the early days of separation — a scenario that happens more often than people expect.</p>
<p>If you don't have ready access to financial records, now is the time to find them. Bank statements, tax returns, superannuation statements and mortgage documents are all relevant. Under Australian family law, both parties have a duty of disclosure — but the obligation only becomes enforceable once proceedings begin.</p>

<h2 id="get-legal-advice">2. Get Independent Legal Advice</h2>
<p>You don't need a lawyer to separate, but you do need to understand your legal rights before you act. A single consultation with a family lawyer — sometimes called a "preliminary advice" session — will tell you what you're entitled to, what the likely timeframes are, and what your options are.</p>
<p>Australian family law applies a four-step process to property settlements: identifying the asset pool, assessing contributions (financial and non-financial), considering future needs, and arriving at a just and equitable outcome. The split is not automatically 50/50 — it depends on the specific facts of your relationship.</p>
<p>Knowing this before you have the separation conversation means you're not negotiating from a position of ignorance. It also means you won't make promises — "you can have the house" or "I'll pay for the kids' school fees" — that you later discover you can't keep.</p>
<blockquote><p>"The people who come to mediation least prepared are usually those who had the separation conversation before they understood their own position. A single legal advice session changes everything." — Dan Toombs, Founder, Mediations Australia</p></blockquote>

<h2 id="think-about-children">3. Put Your Children First</h2>
<p>If you have children, how you handle the first days and weeks of separation will shape your co-parenting relationship for years. Courts always apply the principle of what is in the best interests of the child — and this should be your guide too.</p>
<p>Before any conversation with your partner, think through some practical questions: Where will the children live? How will school pickup, medical appointments and holidays be managed? How will you communicate about the children after separation?</p>
<p>The research on children and separation is clear: children recover well from separation when both parents remain involved, cooperative, and shielded from conflict. They struggle when they're caught in the middle, used as messengers, or exposed to ongoing hostility.</p>
<p>A parenting plan doesn't need to be finalised before you separate — but having thought through a workable interim arrangement shows good faith and reduces early conflict. It also makes any future mediation or negotiation smoother, because you're starting from a position of "here's what could work" rather than entrenched positions.</p>

<h2 id="explore-mediation">4. Explore Mediation Before Court</h2>
<p>Most people assume separation means lawyers, court and years of conflict. It doesn't have to. In Australia, mediation — and specifically Family Dispute Resolution (FDR) — is required by law before most parenting matters can go to court. But many families also use mediation to resolve property and financial issues without litigation.</p>
<p>The advantages are significant. Mediation typically costs a fraction of contested court proceedings. It's faster — weeks or months rather than one to three years. And critically, the agreement you reach is one you've both had input into, which makes it more durable than an order imposed by a judge.</p>
<p>Nationally accredited mediators are neutral — they don't represent either party and don't give legal advice. Their role is to facilitate a structured conversation that helps both parties identify interests, explore options and reach agreements they can live with.</p>
<p>Before you say "I want a divorce," it's worth understanding that mediation may make the whole process far less painful than you fear.</p>
<p><a href="/book-a-consultation/" class="btn btn-primary">Talk to a Mediator — Free Consultation</a></p>

<h2 id="protect-documents">5. Protect and Copy Important Documents</h2>
<p>In the early days of separation, important documents can go missing — sometimes accidentally, sometimes not. Before any difficult conversation, it's prudent to locate and copy key records.</p>
<p>The documents most relevant to a property settlement include: recent tax returns for both parties, superannuation statements, bank and credit card statements for the past 12 months, mortgage documents and property valuations, business financial statements if either party owns a business, and life insurance policies.</p>
<p>You don't need to remove originals. In most cases, photographing or scanning documents is sufficient. The goal is to ensure you have access to records that establish the asset pool, because once separation is announced, access to joint accounts and shared filing systems can quickly become contested.</p>
<p>Store copies somewhere secure — a personal email account, a USB kept away from the family home, or with a trusted family member.</p>

<h2 id="faq">Frequently Asked Questions</h2>
<h3>Do I need to be legally separated before starting mediation?</h3>
<p>No. Mediation can begin at any point — before or after a formal separation. Many couples use it to negotiate the terms of their separation while still living together.</p>
<h3>What is the difference between separation and divorce in Australia?</h3>
<p>Separation is the decision to end the relationship — there is no formal legal process to separate. Divorce is the legal dissolution of a marriage, which requires a court order and can only be applied for after 12 months of separation. You can negotiate property settlements and parenting arrangements before applying for divorce.</p>
<h3>Does it matter who says "I want a divorce" first?</h3>
<p>No. Under Australian family law, separation is assessed by the conduct and intention of the parties, not by who initiated it. There is no legal advantage to initiating separation.</p>
<h3>Can we use mediation even if things are hostile?</h3>
<p>Yes, in many cases. Mediators are trained to manage high-conflict dynamics. Shuttle mediation — where parties are in separate rooms — is often used when direct communication is difficult. There are, however, circumstances where mediation is not appropriate, including situations involving family violence or significant power imbalances.</p>
<h3>How soon after separation should I see a mediator?</h3>
<p>As soon as possible. Early engagement with a mediator typically produces better outcomes — before positions harden, before legal costs accumulate, and before children are exposed to prolonged conflict.</p>
""",
    },
    "mediation-vs-collaborative-law": {
        "title": "Mediation vs Collaborative Law: Key Differences Explained",
        "desc":  "What's the difference between mediation and collaborative law? Compare costs, process and legal outcomes to choose the right path. Free consult.",
        "h1":    "Mediation vs Collaborative Law: Key Differences Explained",
    },
    "costs-of-going-to-court": {
        "title": "The Real Cost of Going to Court in Australia",
        "desc":  "Court costs in Australia: filing fees, lawyer fees, hidden costs, time. See what family court actually costs — and the cheaper alternative.",
        "h1":    "The Real Cost of Going to Court in Australia",
        "read_min": "10",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> A contested family law matter in Australia typically costs each party $30,000–$100,000 in legal fees alone, takes one to three years, and hands all decisions to a judge. For most disputes, mediation resolves the same issues in weeks for a fraction of that cost — with an agreement you control.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#filing-fees">Court filing fees</a></li>
<li><a href="#lawyer-fees">Lawyer and barrister fees</a></li>
<li><a href="#hidden-costs">Hidden costs most people miss</a></li>
<li><a href="#total-cost">What a contested case actually costs</a></li>
<li><a href="#time-cost">The cost of time</a></li>
<li><a href="#emotional-cost">Emotional and relationship cost</a></li>
<li><a href="#comparison">Court vs mediation: full comparison</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="filing-fees">Court filing fees</h2>
<p>The Federal Circuit and Family Court of Australia (FCFCOA) charges filing fees at every stage. These are government fees — separate from anything you pay a lawyer — and they add up quickly.</p>
<table><thead><tr><th>Application type</th><th>Fee (2026)</th></tr></thead><tbody>
<tr><td>Initiating application (financial/parenting)</td><td>$365</td></tr>
<tr><td>Response to initiating application</td><td>$185</td></tr>
<tr><td>Each interim hearing day</td><td>$545</td></tr>
<tr><td>First trial day</td><td>$1,090</td></tr>
<tr><td>Each subsequent trial day</td><td>$545</td></tr>
<tr><td>Subpoena (per subpoena)</td><td>$55</td></tr>
</tbody></table>
<p>A case that runs to a three-day trial — not unusual for contested property settlements — will accumulate $2,725 in court fees alone, before a single hour of legal time is charged. Hardship exemptions exist but are narrowly applied.</p>
<div class="post-cta reveal"><div class="post-cta-inner"><p>Concerned about what court will cost you? Get an honest picture in a free consultation — no obligation.</p><a href="/book-a-consultation/" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></div></div>

<h2 id="lawyer-fees">Lawyer and barrister fees</h2>
<p>Court fees are the smallest item on the bill. Solicitor and barrister fees dwarf them.</p>
<p><strong>Solicitor fees</strong> for family law matters in Australia typically run $350–$600 per hour depending on experience and city. A solicitor will spend time on correspondence, disclosure, court documents, conferences, and preparation — easily 50–150 hours on a contested matter before the trial begins.</p>
<p><strong>Barrister fees</strong> are charged separately. For a hearing day, a family law barrister charges $3,000–$8,000 per day. Preparation — reading briefs, drafting submissions — adds further fees at $400–$800 per hour.</p>
<table><thead><tr><th>Fee type</th><th>Typical range</th></tr></thead><tbody>
<tr><td>Solicitor hourly rate</td><td>$350–$600/hr</td></tr>
<tr><td>Barrister daily rate (hearing)</td><td>$3,000–$8,000/day</td></tr>
<tr><td>Barrister preparation rate</td><td>$400–$800/hr</td></tr>
<tr><td>Family report (psychologist)</td><td>$3,500–$8,000</td></tr>
<tr><td>Property valuation</td><td>$500–$2,000</td></tr>
<tr><td>Business valuation</td><td>$5,000–$25,000</td></tr>
</tbody></table>

<h2 id="hidden-costs">Hidden costs most people miss</h2>
<p>The line items above are visible. These costs often go unbudgeted:</p>
<ul>
<li><strong>Subpoenas and third-party disclosure.</strong> Obtaining bank records, superannuation statements, business records, and tax documents each generates subpoena fees, compliance costs, and solicitor time to review.</li>
<li><strong>Independent children's lawyer (ICL).</strong> Where the court appoints an ICL, both parties typically share the cost: $5,000–$15,000 in total.</li>
<li><strong>Lost income.</strong> Attending hearings, conferences, and meetings means time away from work. A three-day trial costs three days of income — plus preparation days either side.</li>
<li><strong>Ongoing housing costs.</strong> While proceedings drag on, you may maintain two households instead of one. For a case lasting 18 months, that duplication is real money.</li>
<li><strong>Mental health support.</strong> Litigation is psychologically gruelling. Counselling, therapy, and GP visits are a real cost of contested court proceedings that never appears in a legal bill.</li>
<li><strong>Cost orders against you.</strong> If a judge finds your conduct unreasonable — refusing a reasonable offer, for example — they can order you to pay part of the other side's costs. This is rare but real.</li>
</ul>

<h2 id="total-cost">What a contested case actually costs</h2>
<p>Aggregating court fees, solicitor fees, barrister fees, and expert reports, a <strong>contested family law property settlement</strong> in Australia typically costs each party:</p>
<table><thead><tr><th>Case complexity</th><th>Each party's legal costs</th><th>Total (both parties combined)</th></tr></thead><tbody>
<tr><td>Simple (2–3 hearing days, consent possible)</td><td>$15,000–$35,000</td><td>$30,000–$70,000</td></tr>
<tr><td>Moderate (4–8 hearing days, some contest)</td><td>$35,000–$70,000</td><td>$70,000–$140,000</td></tr>
<tr><td>Complex (business assets, business valuation, trial)</td><td>$70,000–$150,000+</td><td>$140,000–$300,000+</td></tr>
</tbody></table>
<p>That money comes from the asset pool. A couple with $600,000 in assets can spend $100,000 in combined legal fees — reducing the pool available to both parties by one sixth before it is divided.</p>
<div class="post-cta reveal"><div class="post-cta-inner"><p>Ready to protect more of your asset pool? Mediation typically costs a fraction of court for the same result.</p><a href="/book-a-consultation/" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></div></div>

<h2 id="time-cost">The cost of time</h2>
<p>The FCFCOA is under significant pressure. Wait times between filing and a final hearing vary but a contested trial — when parties cannot settle — routinely takes <strong>12–24 months</strong> from filing to judgment in most registries. Complex cases take longer.</p>
<p>During that period:</p>
<ul>
<li>Property cannot be sold or refinanced without both parties' consent or a court order</li>
<li>Superannuation remains unsplit</li>
<li>Business decisions are constrained</li>
<li>Emotional closure is deferred</li>
<li>Legal bills accumulate at every interlocutory step</li>
</ul>
<p>Children's matters resolve faster in many cases — the court prioritises interim parenting orders — but final parenting orders after a contested hearing can still take 12+ months.</p>

<h2 id="emotional-cost">Emotional and relationship cost</h2>
<p>Litigation is adversarial by design. Each side builds a case against the other. Evidence of bad conduct, parenting failures, financial dishonesty, or infidelity may be placed before a judge. Once documents are filed and positions hardened, co-parenting relationships — which must survive for years — are often seriously damaged.</p>
<p>Research consistently shows that parties who negotiate their own agreements (through mediation or direct negotiation) report higher satisfaction, greater compliance, and better co-parenting outcomes than those whose arrangements are imposed by a judge. A court order tells you what you must do; a mediated agreement reflects what you agreed to do. The difference in how it feels — and how it holds — is significant.</p>
<blockquote><p>"The cases I see in court are rarely ones where court was the only option. Most could have been resolved earlier, with less damage, if both parties had engaged with mediation first. By the time they reach a trial, the relationship — and often the asset pool — is in much worse shape than it needed to be."</p><footer>— Dan Toombs, Founder &amp; Accredited Mediator, Mediations Australia</footer></blockquote>

<h2 id="comparison">Court vs mediation: full comparison</h2>
<table><thead><tr><th>Factor</th><th>Family Court</th><th>Mediation</th></tr></thead><tbody>
<tr><td>Typical cost (per party)</td><td>$30,000–$100,000+</td><td>$1,500–$5,000 total (shared)</td></tr>
<tr><td>Timeframe</td><td>12–36 months</td><td>Days to weeks</td></tr>
<tr><td>Who decides</td><td>Judge</td><td>You and your ex-partner</td></tr>
<tr><td>Privacy</td><td>Public record (mostly)</td><td>Fully confidential</td></tr>
<tr><td>Flexibility</td><td>Limited — court's orders</td><td>High — tailored to your family</td></tr>
<tr><td>Co-parenting impact</td><td>Often damaging</td><td>Usually preserves relationship</td></tr>
<tr><td>Enforceability</td><td>Binding court orders</td><td>Binding via consent orders or BFA</td></tr>
<tr><td>Resolution rate</td><td>~5% reach a final trial</td><td>~85–90% reach agreement</td></tr>
</tbody></table>
<p>The 5% figure is important: around 95% of family law matters in Australia settle before trial — often at the courthouse door, under enormous financial and emotional pressure. Mediation achieves the same settlement, usually in far less time, at far lower cost, and with you in control of the outcome rather than a barrister bargaining on your behalf.</p>
<div class="post-cta reveal"><div class="post-cta-inner"><p>See if mediation is right for your situation — a free initial consultation takes 30 minutes.</p><a href="/book-a-consultation/" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></div></div>

<h2 id="faq">Frequently asked questions</h2>
<details><summary>Can I get legal aid for family court in Australia?</summary><p>Legal aid is available but means-tested and merit-tested. Eligibility thresholds are low — most people with a modest income and any assets do not qualify. Legal Aid offices also have limited capacity, and representation is often restricted to children's matters. Most property disputes proceed without legal aid.</p></details>
<details><summary>What if we settle before trial — will I still pay all those costs?</summary><p>No. Costs are proportional to the stage at which you settle. If you settle after filing but before any hearing, your combined costs may be $15,000–$40,000 rather than $100,000+. This is why settling early — ideally through mediation before filing — makes such a significant financial difference.</p></details>
<details><summary>Can the court order my ex to pay my legal costs?</summary><p>In limited circumstances. Family law courts generally make costs orders against a party whose conduct was unreasonable — for example, repeatedly ignoring subpoenas, making false allegations, or rejecting a reasonable offer that the court later betters. These orders are not automatic and are the exception rather than the rule.</p></details>
<details><summary>Is mediation legally binding?</summary><p>A mediated agreement itself is not automatically binding — but it can be made binding in two ways: by filing it with the court as consent orders (which the court approves and issues), or by having solicitors draft it as a Binding Financial Agreement under the Family Law Act. Either approach gives you the certainty of a binding document with the efficiency of mediation.</p></details>
<details><summary>Does mediation work if my ex won't cooperate?</summary><p>Mediation requires both parties to attend and engage. If your ex refuses, you may need to obtain a Section 60I certificate (which confirms genuine attempts at FDR were made) before the court will hear your application. We can advise on this and on situations where mediation is not appropriate — including cases involving family violence or where one party refuses to disclose financial information honestly.</p></details>
""",
    },

    "estate-dispute-mediation": {
        "title": "Estate Dispute Mediation in Australia",
        "desc":  "Families fighting over estates and wills? Mediation resolves inheritance disputes faster and cheaper than court, without destroying family relationships.",
        "h1":    "Estate Dispute Mediation in Australia",
        "read_min": "9",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> Estate and inheritance disputes — contested wills, executor conflicts, family provision claims — can be resolved through mediation in weeks rather than years. Mediation is private, preserves family relationships, and typically costs a fraction of litigation. Most inheritance disputes that go to court settle eventually anyway, but only after enormous cost to both the estate and the family.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#types">Types of estate disputes we mediate</a></li>
<li><a href="#why-mediation">Why mediation works for estate disputes</a></li>
<li><a href="#process">The mediation process for estate disputes</a></li>
<li><a href="#costs">Costs: mediation vs probate litigation</a></li>
<li><a href="#family-provision">Family provision claims and mediation</a></li>
<li><a href="#executor">When the executor is the problem</a></li>
<li><a href="#when-not">When mediation isn't appropriate</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="types">Types of estate disputes we mediate</h2>
<p>Inheritance disputes take many forms. Mediation can address almost all of them:</p>
<ul>
<li><strong>Contested wills.</strong> A beneficiary or excluded family member claims the will is invalid — because the testator lacked capacity, was unduly influenced, or the will was incorrectly witnessed.</li>
<li><strong>Family provision claims.</strong> An eligible person (spouse, child, former spouse, de facto partner, dependant) claims inadequate provision was made for them in the will or on intestacy.</li>
<li><strong>Executor disputes.</strong> Beneficiaries challenge how the executor is administering the estate — delays, poor investment decisions, conflicts of interest, or suspected misappropriation.</li>
<li><strong>Jointly-held property and assets.</strong> Disagreements about what falls within the estate versus assets held in trust, joint names, or through superannuation nominations.</li>
<li><strong>Superannuation death benefit disputes.</strong> Where a dependant challenges a trustee's decision about how super is paid following death.</li>
<li><strong>Business succession disputes.</strong> Where the deceased held an interest in a family business and successors disagree about valuation, buyouts, or ongoing management.</li>
<li><strong>Disagreements about estate administration.</strong> Sale of the family home, distribution timing, valuing personal items with sentimental significance.</li>
</ul>
<div class="post-cta reveal"><div class="post-cta-inner"><p>Estate disputes can escalate quickly. Early mediation protects the estate and the family. Book a free consultation.</p><a href="/book-a-consultation/" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></div></div>

<h2 id="why-mediation">Why mediation works for estate disputes</h2>
<p>Estate disputes have a particular character that makes mediation especially well-suited. Unlike commercial disputes between strangers, inheritance conflicts occur within families — people who will remain related for life and who share children, grandchildren, and memories. The stakes are not only financial; they are relational and emotional.</p>
<p>Litigation destroys what mediation can preserve. A court process in which siblings file affidavits detailing each other's failings, question the deceased's mental capacity, or allege undue influence causes harm that outlasts the outcome. Many families that litigate an estate dispute do not recover from it.</p>
<p>Mediation creates a different dynamic:</p>
<ul>
<li><strong>Confidentiality.</strong> Unlike court proceedings, mediation is private. Nothing said in mediation can be used against a party in subsequent litigation. Families can speak honestly without fear of it appearing in a judgment.</li>
<li><strong>Flexibility.</strong> A court can only divide money. A mediator can help parties reach agreements that involve property, personal items, ongoing arrangements, apologies, and relationship repair — things no judge can order.</li>
<li><strong>Speed.</strong> Probate litigation takes one to three years. Estate mediation typically resolves disputes in one or two sessions over a matter of weeks.</li>
<li><strong>Estate preservation.</strong> Legal fees in contested estate matters are typically paid from the estate — reducing what beneficiaries receive. Mediation protects the estate.</li>
</ul>

<h2 id="process">The mediation process for estate disputes</h2>
<p>Estate mediations follow a structured but flexible process:</p>
<ol>
<li><strong>Pre-mediation preparation.</strong> Each party provides relevant documents — the will, asset valuations, superannuation statements, correspondence from the executor. The mediator reviews these before the session and may speak with each party individually.</li>
<li><strong>Joint session opening.</strong> The mediator explains the process, ground rules, and confidentiality. Each party has an opportunity to describe their perspective and what they are seeking.</li>
<li><strong>Separate sessions (caucus).</strong> The mediator meets privately with each party — often multiple times — to explore interests beneath stated positions, test options, and reality-check expectations.</li>
<li><strong>Negotiation and agreement.</strong> The mediator helps parties move from positions to interests, and from interests to workable options. Where agreement is reached, it is documented.</li>
<li><strong>Formalising the outcome.</strong> Depending on the nature of the dispute, the agreement may be formalised as a deed of settlement, consent orders in the Supreme Court, or a variation to the estate distribution recorded by the executor.</li>
</ol>
<p>Solicitors may attend or be available for advice without actively running the process. Many parties find that having their solicitor present — but in a supporting rather than leading role — gives them confidence without escalating the process into adversarial territory.</p>

<h2 id="costs">Costs: mediation vs probate litigation</h2>
<table><thead><tr><th>Factor</th><th>Contested probate litigation</th><th>Estate mediation</th></tr></thead><tbody>
<tr><td>Typical duration</td><td>1–3 years</td><td>2–8 weeks</td></tr>
<tr><td>Legal costs (per party)</td><td>$30,000–$120,000+</td><td>$2,000–$8,000 total (shared)</td></tr>
<tr><td>Who pays</td><td>Often the estate (reducing distribution)</td><td>Parties share mediator fee</td></tr>
<tr><td>Privacy</td><td>Public (Supreme Court proceedings)</td><td>Fully confidential</td></tr>
<tr><td>Relationship impact</td><td>Typically severe</td><td>Usually manageable</td></tr>
<tr><td>Outcome flexibility</td><td>Limited — court orders only</td><td>Tailored — can include non-financial elements</td></tr>
</tbody></table>
<p>The cost comparison is stark. Legal costs in estate litigation are routinely paid from the estate — meaning every dollar spent on lawyers comes out of what beneficiaries inherit. A $500,000 estate that incurs $150,000 in combined legal fees distributes $350,000. Mediation costs a few thousand dollars.</p>
<div class="post-cta reveal"><div class="post-cta-inner"><p>Protect the estate and the family. Speak to a specialist estate mediator at no cost.</p><a href="/book-a-consultation/" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></div></div>

<h2 id="family-provision">Family provision claims and mediation</h2>
<p>Family provision claims — where an eligible person challenges a will on the ground that inadequate provision was made for them — are among the most common estate disputes in Australia. Each state and territory has its own legislation governing these claims, with different eligibility criteria and time limits:</p>
<table><thead><tr><th>State/Territory</th><th>Governing legislation</th><th>Time limit to file</th></tr></thead><tbody>
<tr><td>NSW</td><td>Succession Act 2006 (NSW)</td><td>12 months from death</td></tr>
<tr><td>VIC</td><td>Administration and Probate Act 1958 (VIC)</td><td>6 months from grant of probate</td></tr>
<tr><td>QLD</td><td>Succession Act 1981 (QLD)</td><td>9 months from death</td></tr>
<tr><td>WA</td><td>Family Provision Act 1972 (WA)</td><td>6 months from grant of probate</td></tr>
<tr><td>SA</td><td>Inheritance (Family Provision) Act 1972 (SA)</td><td>6 months from grant of probate</td></tr>
</tbody></table>
<p>Mediation can be used for family provision claims at any stage — before filing, after filing but before hearing, or (with court direction) during proceedings. Many courts actively encourage parties to attempt mediation before listing a final hearing. The Supreme Court of NSW, for example, routinely refers family provision matters to mediation.</p>

<h2 id="executor">When the executor is the problem</h2>
<p>Executors have significant obligations — to administer the estate promptly, honestly, and in accordance with the will. Where beneficiaries are concerned that an executor is not meeting those obligations, the options range from informal resolution to an application to the Supreme Court to remove the executor.</p>
<p>Mediation offers a middle path. In a structured session, beneficiaries can raise concerns about delays, asset handling, or suspected self-dealing. The executor can respond with their perspective and the practical constraints they face. Many executor disputes arise from miscommunication and poor transparency rather than bad faith — and mediation resolves those efficiently without the nuclear option of court proceedings.</p>
<p>Where there is genuine evidence of misappropriation or fraud, mediation is less appropriate — legal advice and potentially court action are warranted. We will say this plainly if it applies to your situation.</p>

<h2 id="when-not">When mediation isn't appropriate</h2>
<p>Mediation is not right for every estate dispute. It is unlikely to succeed where:</p>
<ul>
<li>There is strong evidence of fraud, forgery, or financial elder abuse — these require court investigation and potentially police involvement</li>
<li>A party lacks the legal or mental capacity to participate meaningfully</li>
<li>There is a significant power imbalance and one party cannot advocate for themselves even with support</li>
<li>Emergency orders are needed to freeze assets or prevent dissipation of the estate</li>
</ul>
<p>If any of these apply, we will tell you in the initial consultation and help you understand your options.</p>

<h2 id="faq">Frequently asked questions</h2>
<details><summary>Does the executor have to attend mediation?</summary><p>The executor is a necessary party to most estate mediations — they administer the estate and must implement any agreement. We can assist with engaging executors who are reluctant, and explain the practical and legal implications of refusing to participate in good faith.</p></details>
<details><summary>What if some beneficiaries are overseas or interstate?</summary><p>Mediations Australia conducts estate mediations online and by videoconference. Parties can participate from anywhere in Australia or internationally. We have experience facilitating multi-party estate mediations where parties are geographically dispersed.</p></details>
<details><summary>Will we need lawyers at the mediation?</summary><p>Solicitors can attend but are not required. Many parties prefer to have legal advice available — either with their solicitor present or available by phone — without having lawyers run the session. We recommend that any agreement reached is reviewed by a solicitor before being signed.</p></details>
<details><summary>How long does an estate mediation session take?</summary><p>Most estate mediations take a full day (six to eight hours). Complex disputes involving multiple parties, a contested will, and significant assets may require a second session. We schedule adequate time and do not rush outcomes.</p></details>
<details><summary>Can we mediate a disputed will if probate has already been granted?</summary><p>Yes. Probate being granted does not prevent mediation — it simply means the executor has formal authority to administer the estate. Family provision claims and distribution disputes can still be mediated after probate is granted.</p></details>
""",
    },

    "preparing-for-mediation": {
        "title": "How to Prepare for Mediation in Australia",
        "desc":  "Practical guide to preparing for family law mediation in Australia — what to bring, what to expect, and how to get the best outcome from your session.",
        "h1":    "How to Prepare for Mediation in Australia",
        "read_min": "8",
        "body": """
<div class="answer reveal"><p><strong>Key takeaway:</strong> Good preparation makes mediation significantly more effective. Know your financial position, think about your priorities (not just your positions), bring the right documents, and arrive with an open mind about solutions you haven't yet considered. Parties who prepare well reach better agreements faster — and feel more confident and in control throughout the process.</p></div>

<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>
<li><a href="#before">Before your mediation session</a></li>
<li><a href="#documents">Documents to bring</a></li>
<li><a href="#financial">Understanding your financial position</a></li>
<li><a href="#priorities">Knowing your priorities</a></li>
<li><a href="#on-the-day">What to expect on the day</a></li>
<li><a href="#emotional">Preparing emotionally</a></li>
<li><a href="#parenting">Preparing for parenting mediations</a></li>
<li><a href="#after">After mediation</a></li>
<li><a href="#faq">Frequently asked questions</a></li>
</ul></nav>

<h2 id="before">Before your mediation session</h2>
<p>The work you do before sitting down in a mediation session determines much of what is possible once you are there. Most mediations that fail do so because one or both parties arrived without having thought through what they actually need — as distinct from what they want or what they fear the other party will demand.</p>
<p>A useful framework before any mediation: separate your <strong>positions</strong> (what you are asking for) from your <strong>interests</strong> (why you are asking for it). "I want to keep the house" is a position. "I need housing stability for the children for the next three years" is an interest. Interests are usually more flexible than positions — there may be more than one way to meet them. Mediators work at the level of interests, not positions.</p>
<p>Before the session, also think about:</p>
<ul>
<li>What would a fair outcome actually look like?</li>
<li>What are you willing to give to get what you most need?</li>
<li>What happens if mediation doesn't reach agreement — what does that alternative actually cost you?</li>
<li>What does the other party genuinely need, and is there a way to meet that while also meeting yours?</li>
</ul>
<div class="post-cta reveal"><div class="post-cta-inner"><p>Not sure what to expect from your first mediation? Our team can walk you through the process in a free call.</p><a href="/book-a-consultation/" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></div></div>

<h2 id="documents">Documents to bring</h2>
<p>For property settlement and financial mediations, bring organised copies of everything relevant to your financial position. You do not need to have exchanged formal disclosure documents before mediation (though it helps), but both parties need a reasonable picture of the asset pool to have a productive conversation.</p>
<table><thead><tr><th>Category</th><th>What to bring</th></tr></thead><tbody>
<tr><td>Real estate</td><td>Recent valuation or comparable sales; current mortgage statement; rates notice</td></tr>
<tr><td>Bank accounts</td><td>Statements for all accounts in your name (past 12 months)</td></tr>
<tr><td>Superannuation</td><td>Latest member statement for each fund; rollover amounts if consolidated</td></tr>
<tr><td>Vehicles</td><td>Redbook valuation; finance payout figure if applicable</td></tr>
<tr><td>Debts</td><td>All loan statements: home loan, car loans, personal loans, credit cards</td></tr>
<tr><td>Business interests</td><td>Most recent financial statements; any valuation already obtained</td></tr>
<tr><td>Investments</td><td>Share portfolio statements; managed fund values; trust documents</td></tr>
<tr><td>Legal documents</td><td>Any existing court orders; pre-nuptial or financial agreements</td></tr>
</tbody></table>
<p>Do not wait until you have everything perfectly organised — bring what you have. The mediator can work with imprecise figures and note what remains to be confirmed. Perfect information is rarely available; approximate information, honestly given, is workable.</p>

<h2 id="financial">Understanding your financial position</h2>
<p>You do not need a lawyer or accountant to prepare for mediation, but you do need to understand your own financial situation reasonably well. Before the session:</p>
<ul>
<li><strong>Know your total assets.</strong> List everything you own — jointly or separately — and a realistic current value for each item.</li>
<li><strong>Know your total liabilities.</strong> List all debts — mortgage, credit cards, personal loans, tax debts, HECS — and the current payout amount.</li>
<li><strong>Calculate the net pool.</strong> Assets minus liabilities gives you the net pool available to divide. Understanding this figure helps you evaluate any proposal quickly.</li>
<li><strong>Know your superannuation balance.</strong> Super is an asset of the relationship in most cases. Log into your fund's member portal to get a current balance.</li>
<li><strong>Understand your post-settlement income needs.</strong> What do you need to live on? What housing can you afford after settlement? These practical realities should guide what you negotiate for.</li>
</ul>
<p>If you are unsure about any of these, a brief consultation with a family law solicitor before mediation is worthwhile — not to have the solicitor negotiate for you, but to make sure you understand your legal entitlements before you make decisions.</p>

<h2 id="priorities">Knowing your priorities</h2>
<p>The most effective negotiators in mediation know what they genuinely need versus what they would like. Before the session, rank your priorities honestly:</p>
<ul>
<li>What is the single most important thing you need from this settlement?</li>
<li>What would you give up to secure it?</li>
<li>What matters least to you — and could you trade that away?</li>
<li>Are there non-financial things you need: an apology, a commitment about the children's schooling, an agreement about how you communicate going forward?</li>
</ul>
<p>Understanding your own priorities helps you avoid being distracted by issues that feel important but are not actually central to your situation. Many mediations stall over relatively minor assets (a car, a piece of furniture, a pet) when the real issues are about housing security, income, or the children's arrangements. Know what you actually care about before you walk in.</p>

<h2 id="on-the-day">What to expect on the day</h2>
<p>A typical family law mediation session runs four to eight hours. Most people find this a significant commitment — emotionally as well as practically.</p>
<p>The session will generally follow this structure:</p>
<ol>
<li><strong>Opening.</strong> The mediator explains the process, confirms confidentiality, and invites each party to give an opening statement — what they are here for and what they hope to achieve. This is not a debate; each party speaks without interruption.</li>
<li><strong>Information exchange.</strong> The mediator helps both parties understand the factual landscape — the asset pool, the key issues, areas of agreement and disagreement.</li>
<li><strong>Private sessions.</strong> The mediator will meet privately with each party (called caucus). This is where you can speak frankly about what you really need, what you are concerned about, and what you might be willing to accept. What you say in caucus is confidential unless you authorise the mediator to share it.</li>
<li><strong>Joint negotiation.</strong> The mediator helps the parties move toward agreement, testing proposals and exploring options. This may involve multiple rounds of private sessions.</li>
<li><strong>Agreement (if reached).</strong> If the parties reach agreement, it is documented — usually as a written summary that both parties sign. This is then formalised by solicitors into consent orders or a binding financial agreement.</li>
</ol>
<p>Bring snacks or lunch. Be prepared for the session to go longer than anticipated if agreement is within reach. The mediator will manage the pace and call breaks as needed.</p>

<h2 id="emotional">Preparing emotionally</h2>
<p>Mediation is a structured professional process, but it covers deeply personal ground. You may be discussing your home, your children, your financial future, and your relationship with someone you are in conflict with. Emotional preparation matters as much as practical preparation.</p>
<ul>
<li><strong>Get enough sleep the night before.</strong> Decision-making deteriorates significantly when you are tired. This is not the moment to stay up late reviewing documents.</li>
<li><strong>Eat before you arrive.</strong> Low blood sugar affects judgment and patience. Do not arrive hungry.</li>
<li><strong>Have a support person available (not in the room).</strong> A friend, family member, or counsellor you can call during a break — not to advise on the legal issues, but to decompress and stay grounded.</li>
<li><strong>Have a plan for intense moments.</strong> There will be moments that feel unfair, where you want to react or shut down. Know in advance that you can ask for a break, request private time with the mediator, or take a few minutes outside.</li>
<li><strong>Remember the alternative.</strong> When mediation feels hard, the comparison is not an easier conversation — it is the alternative of two to three years of litigation, $50,000–$100,000 in legal costs, and a judge making your decisions.</li>
</ul>
<blockquote><p>"The most valuable thing I see clients do before mediation is think seriously about what they are actually trying to achieve — not just what they are afraid of losing. That shift from fear to clarity changes what is possible in the room."</p><footer>— Dan Toombs, Founder &amp; Accredited Mediator, Mediations Australia</footer></blockquote>

<h2 id="parenting">Preparing for parenting mediations</h2>
<p>Parenting mediations have a different emphasis to financial ones. The focus is on the children's needs and how both parents will meet them. To prepare:</p>
<ul>
<li><strong>Know your children's current routine</strong> in detail — school days, activities, care arrangements, medical appointments, relationships with extended family</li>
<li><strong>Think about what the children need</strong> (not just what you want) — stability, both parents, particular activities, school continuity</li>
<li><strong>Consider how decisions will be made</strong> — schooling, medical care, religion, extracurricular activities — and what arrangements you need for these</li>
<li><strong>Think practically about logistics</strong> — where each parent lives, work schedules, transport, school holidays, special occasions</li>
<li><strong>Be prepared to discuss communication</strong> — how you and the other parent will communicate about the children going forward, and what you each need that arrangement to look like</li>
</ul>
<p>Children do not attend mediation. Their voices may be represented through a family report (written by a psychologist who interviews the children and both parents) if one has been prepared — but more commonly, the mediator will invite each parent to speak to the children's needs from their own perspective.</p>

<h2 id="after">After mediation</h2>
<p>If you reach agreement, the next steps depend on the type of agreement:</p>
<ul>
<li><strong>Financial agreement.</strong> The summary document from mediation goes to solicitors, who draft either a Binding Financial Agreement (BFA) or an application for consent orders. Both are legally binding once properly executed. This process typically takes two to six weeks.</li>
<li><strong>Parenting agreement.</strong> May be formalised as consent orders through the court (binding and enforceable) or as a parenting plan (not legally binding but documented). Consent orders are generally recommended where there is any concern about compliance.</li>
</ul>
<p>If mediation does not reach full agreement, partial agreements can still be recorded and help narrow the issues in any subsequent process. An impasse in mediation is not a failure — it clarifies where the genuine disagreement lies and often leads to faster resolution once both parties have had time to reflect.</p>

<h2 id="faq">Frequently asked questions</h2>
<details><summary>Do I need a lawyer at mediation?</summary><p>No — and many people mediate without a solicitor present. However, for complex financial matters or where you are unsure of your legal entitlements, having a solicitor available (either in the room or by phone) gives you confidence to make informed decisions. We recommend a solicitor review any agreement before you sign.</p></details>
<details><summary>What if my ex won't disclose their finances honestly?</summary><p>Mediation depends on reasonable financial transparency. If you have strong evidence that your ex is concealing assets or income, raise this with the mediator before or at the start of the session. Mediation can still proceed where disclosure is imperfect, but you should not agree to a financial settlement based on information you have real reason to doubt. A solicitor can advise on the formal disclosure obligations that apply in court proceedings.</p></details>
<details><summary>Can I change my mind after signing the mediation agreement?</summary><p>The summary from mediation is generally not itself binding — it becomes binding once solicitors formalise it as consent orders or a BFA. Until that final document is signed, either party can withdraw. However, walking away from a mediated agreement has consequences: it may affect your credibility in any subsequent proceedings, and you will bear the cost and delay of a different process.</p></details>
<details><summary>How long does a typical mediation session take?</summary><p>Family law property mediations typically take four to eight hours. Parenting mediations are often shorter — two to four hours for less complex arrangements. We schedule full days to avoid rushing any agreement, and we are transparent about this upfront so you can arrange your day accordingly.</p></details>
<details><summary>What if I feel unsafe or intimidated?</summary><p>Your safety is the first priority. If you have family violence concerns, tell us before the session — we will arrange separate arrival times, separate waiting areas, and can conduct the entire mediation via shuttle (no joint sessions) or by video. Mediation is not appropriate where there is an active safety risk, and we will not proceed in a way that puts you at risk.</p></details>
""",
    },
}
META_OVERRIDES.update(_EXPANDED)  # merge batch-expanded bodies

def _strip_wp_markup(html):
    """Extract real article text from WordPress page-builder HTML (wpb_row/vc_row wrappers)."""
    if 'wpb_row' not in html and 'vc_row' not in html and 'vc_col-sm' not in html:
        return html
    # Extract content from wpb_text_column sections only (skip wpb_raw_html which has embeds/iframes)
    chunks = re.findall(
        r'class="wpb_text_column[^"]*"[^>]*>.*?<div class="wpb_wrapper">(.*?)</div>\s*</div>\s*</div>',
        html, re.S
    )
    if chunks:
        # Filter out chunks that are mostly non-text (quiz widgets, shortcodes, etc.)
        text_chunks = []
        for chunk in chunks:
            text_only = re.sub(r'<[^>]+>', ' ', chunk)
            text_only = re.sub(r'\s+', ' ', text_only).strip()
            # Only keep chunks with substantial readable text (p/h tags, not just widget divs)
            if len(text_only) > 100 and re.search(r'<[ph][1-6]?\b', chunk, re.I):
                text_chunks.append(chunk.strip())
        if text_chunks:
            return '\n'.join(text_chunks)
    # Fallback: strip WP builder wrapper divs, keeping semantic content inside
    cleaned = re.sub(r'<div[^>]+class="[^"]*wpb_raw_html[^"]*"[^>]*>.*?</div>\s*</div>', '', html, flags=re.S)
    for cls in ('wpb_row', 'vc_row', 'vc_col', 'wpb_column', 'vc_column_container',
                'content-inner', 'row_col_wrap', 'row-bg-wrap', 'wpb_wrapper', 'vc_column-inner'):
        cleaned = re.sub(r'<div[^>]+class="[^"]*' + cls + r'[^"]*"[^>]*>', '', cleaned, flags=re.I)
    return cleaned

def read_existing_body(slug):
    """Extract body content from already-built page (new or old format)."""
    path = os.path.join(OUT, slug, "index.html")
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        html = f.read()
    # New design format
    m = re.search(r'<div class="body-import">(.*?)</div>\s*(?:<aside|<div class="cta-inline")', html, re.S)
    if m:
        body = m.group(1).strip()
        return _strip_wp_markup(body)
    # Old format (pre-new-design)
    m = re.search(r'<div class="post-body">(.*?)</div>\s*(?:<div class="post-cta|<section class="cta-band|</article)', html, re.S)
    if m:
        body = m.group(1).strip()
        return _strip_wp_markup(body)
    return ""

def read_existing_meta(slug):
    path = os.path.join(OUT, slug, "index.html")
    if not os.path.exists(path):
        return None, None, None
    with open(path, encoding="utf-8") as f:
        html = f.read()
    title_m = re.search(r'<title>([^<]+)</title>', html)
    desc_m = re.search(r'<meta name="description" content="([^"]+)"', html)
    h1_m = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    title = _unescape(title_m.group(1)).replace(' | Mediations Australia', '').replace(' - Mediations Australia', '').strip() if title_m else None
    desc = _unescape(desc_m.group(1)) if desc_m else None
    h1 = _unescape(h1_m.group(1)) if h1_m else None
    return title, desc, h1

def build_page(url, slug):
    ov = META_OVERRIDES.get(slug, {})
    # If the override provides body directly, use it without fetching
    if ov.get("title") and ov.get("body"):
        body   = _wrap_tables(ov["body"])
        title  = ov["title"]
        desc   = ov["desc"]
        h1_raw = ov.get("h1", title)
        title = truncate(title, 60)
        desc  = truncate(desc, 160)
        _h1_plain = h1_raw[:60]
        schema = [org_schema(), breadcrumb_schema([("Home", ""), ("Guides", "guides"), (_h1_plain, None)]), article_schema(title, desc)]
        doc = head(title, desc, slug, og_type="article", extra_schema=schema)
        if ov.get("noindex"):
            doc = doc.replace('content="index, follow, max-image-preview:large"', 'content="noindex, nofollow"')
        doc = doc.replace("</head>", POST_CSS + "</head>")
        doc += nav()
        _crumb_label = h1_raw[:48] + ("…" if len(h1_raw) > 48 else "")
        _body_clean, _toc_items = _extract_toc(body)
        _sidebar, _mobile_toc = _toc_blocks(_toc_items)
        _grid_class = "content-grid" if _sidebar else "content-grid no-toc"
        _dek = esc(desc[:160]) if desc else ""
        doc += f"""<main id="main">
<div class="progress-track"><div class="progress-bar" id="prog"></div></div>
{crumb_html([("Home",""),("Guides","guides"),(_crumb_label,None)])}
<article>
<header class="post-hero">
<div class="hero-inner">
<div class="hero-text">
  <div class="post-meta"><span class="cat">Guide</span><span>{ov.get("read_min","9")} min read</span></div>
  <h1>{esc(h1_raw)}</h1>
  <p class="hero-dek">{_dek}</p>
  <div class="hero-actions">
    <a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation</a>
    <a href="tel:0272277373" class="btn-outline-dark">Call (02) 7227 7373</a>
  </div>
  <div class="author-byline">
    <img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia" width="44" height="44" loading="eager">
    <div>
      <span class="author-name"><a href="/our-mediators/">Dan Toombs</a></span>
      <span class="author-cred">Founder &amp; Accredited Mediator · AMDRAS · Multi-Award Winning Lawyer</span>
    </div>
  </div>
</div>
{_hero_art(h1_raw, slug)}
</div>
</header>
<div class="{_grid_class}">
{_sidebar}
<div class="article-body">
{_mobile_toc}
<div class="body-import">
{_body_clean}
</div>
{EXPERT_BIO}
</div>
</div>
</article>
<section class="cta-band" id="book"><div class="phero-blob"></div><div class="wrap"><div class="reveal">
<h2>Ready to resolve it <em>without court</em>?</h2>
<p>Book a free initial consultation and get honest, expert advice on your situation — with no obligation.</p>
<a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Book a Free Consultation <span class="arr">→</span></a>
</div></div></section>
</main>
{_PROG_JS}"""
        doc += page_end()
        path = os.path.join(OUT, slug)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
            f.write(doc)
        return
    existing_body = read_existing_body(slug)
    # Discard extracted body if it contains nested post-hero (means it was a bad prior rebuild)
    if existing_body and 'class="post-hero"' in existing_body:
        existing_body = ""
    def _clean_existing(b):
        b = re.sub(r'<div[^>]+class="[^"]*content-inner[^"]*"[^>]*>', '', b, flags=re.I)
        b = re.sub(r'(<(?:p|a|li|span|em|strong|blockquote|h[2-6])\b[^>]*?)\s+class="[^"]*(?:font-|text-|break-|whitespace-|leading-\[|underline|decoration-|hover:|focus:|-mb-|-mt-)[^"]*"', r'\1', b, flags=re.I)
        return b

    if ov and ov.get("title") and existing_body:
        # Has explicit title override and recoverable body — apply new meta
        body   = _clean_existing(existing_body)
        title  = ov["title"]
        desc   = ov["desc"]
        h1_raw = ov.get("h1", title)
    elif existing_body:
        # Non-expanded post with existing built HTML — recover meta from it, no fetch needed
        body = _clean_existing(existing_body)
        _et, _ed, _eh = read_existing_meta(slug)
        title  = _et or slug.replace("-", " ").title()
        desc   = _ed or ""
        h1_raw = _eh or title
    else:
        fetch_url = FETCH_URL_OVERRIDES.get(slug, url)
        html = fetch_html(fetch_url)
        body = extract_article_body(html)

        # Apply META_OVERRIDES title/desc/h1 if present; otherwise take from fetched page
        if ov.get("title"):
            title  = ov["title"]
            desc   = ov["desc"]
            h1_raw = ov.get("h1", title)
        else:
            title = _unescape(extract_meta_title(html))
            desc  = extract_meta_desc(html)
            h1_raw = _unescape(extract_h1(html))
            if not title:
                title = slug.replace("-", " ").title()
            if not h1_raw:
                h1_raw = title

        body = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", body, flags=re.S | re.I)
        body = clean_body(body)

    body = _wrap_tables(body)
    if ov.get("body_suffix"):
        body = body + ov["body_suffix"]
    title = truncate(title, 60)
    desc = truncate(desc, 160) if desc else truncate(title + " — Mediations Australia.", 160)

    title = truncate(title, 60)
    desc = truncate(desc, 160) if desc else truncate(title + " — Mediations Australia.", 160)

    _h1_plain = h1_raw[:60]
    schema = [org_schema(), breadcrumb_schema([("Home", ""), ("Guides", "guides"), (_h1_plain, None)]), article_schema(title, desc)]
    doc = head(title, desc, slug, og_type="article", extra_schema=schema)
    if ov.get("noindex"):
        doc = doc.replace('content="index, follow, max-image-preview:large"', 'content="noindex, nofollow"')
    doc = doc.replace("</head>", POST_CSS + "</head>")
    doc += nav()
    _crumb_label = h1_raw[:48] + ("…" if len(h1_raw) > 48 else "")
    _body_clean, _toc_items = _extract_toc(body)
    _sidebar, _mobile_toc = _toc_blocks(_toc_items)
    _grid_class = "content-grid" if _sidebar else "content-grid no-toc"
    _dek = esc(desc[:160]) if desc else ""
    doc += f"""<main id="main">
<div class="progress-track"><div class="progress-bar" id="prog"></div></div>
{crumb_html([("Home",""),("Guides","guides"),(_crumb_label,None)])}
<article>
<header class="post-hero">
<div class="hero-inner">
<div class="hero-text">
  <div class="post-meta"><span class="cat">Guide</span><span>8 min read</span></div>
  <h1>{esc(h1_raw)}</h1>
  <p class="hero-dek">{_dek}</p>
  <div class="hero-actions">
    <a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation</a>
    <a href="tel:0272277373" class="btn-outline-dark">Call (02) 7227 7373</a>
  </div>
  <div class="author-byline">
    <img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia" width="44" height="44" loading="eager">
    <div>
      <span class="author-name"><a href="/our-mediators/">Dan Toombs</a></span>
      <span class="author-cred">Founder &amp; Accredited Mediator · AMDRAS · Multi-Award Winning Lawyer</span>
    </div>
  </div>
</div>
{_hero_art(h1_raw, slug)}
</div>
</header>
<div class="{_grid_class}">
{_sidebar}
<div class="article-body">
{_mobile_toc}
<div class="body-import">
{_body_clean}
</div>
{EXPERT_BIO}
</div>
</div>
</article>
<section class="cta-band" id="book"><div class="phero-blob"></div><div class="wrap"><div class="reveal">
<h2>Ready to resolve it <em>without court</em>?</h2>
<p>Book a free initial consultation and get honest, expert advice on your situation — with no obligation.</p>
<a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Book a Free Consultation <span class="arr">→</span></a>
</div></div></section>
</main>
{_PROG_JS}"""
    doc += page_end()

    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)


# ── Main ──────────────────────────────────────────────────────────────────────

existing = {d for d in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, d))}

seen_slugs: set = set()
unique_urls = []
for url in URLS:
    slug = url.rstrip("/").split("/")[-1]
    if slug not in seen_slugs:
        seen_slugs.add(slug)
        unique_urls.append((url, slug))

built, skipped, failed = [], [], []
total = len(unique_urls)

for i, (url, slug) in enumerate(unique_urls, 1):
    try:
        build_page(url, slug)
        built.append(slug)
        print(f"  [{i}/{total}] OK  {slug}")
    except Exception as e:
        failed.append((slug, str(e)))
        print(f"  [{i}/{total}] FAIL {slug}: {e}")
    time.sleep(0.25)

print(f"\nDone. Built: {len(built)}  |  Skipped (already exist): {len(skipped)}  |  Failed: {len(failed)}")
if failed:
    print("Failed slugs:")
    for s, e in failed:
        print(f"  {s}: {e}")
