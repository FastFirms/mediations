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
.article-body{padding:32px 0 60px;min-width:0}
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

def _extract_toc(body):
    """Pull the inline post-toc nav out of body. Returns (cleaned_body, ul_items_html)."""
    m = re.search(r'<nav[^>]*class="[^"]*post-toc[^"]*"[^>]*>.*?<ul>(.*?)</ul>.*?</nav>', body, re.S | re.I)
    if not m:
        return body, ""
    ul_inner = m.group(1).strip()
    cleaned = re.sub(r'<nav[^>]*class="[^"]*post-toc[^"]*"[^>]*>.*?</nav>', '', body, flags=re.S | re.I).strip()
    return cleaned, ul_inner

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
    """Wrap bare <table> elements in a div so border-radius/overflow work in all browsers."""
    html = re.sub(r'<table(\b)', r'<div class="table-wrap"><table\1', html)
    html = re.sub(r'</table>', r'</table></div>', html)
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
        doc = doc.replace("</head>", POST_CSS + "</head>")
        doc += nav()
        _crumb_label = h1_raw[:48] + ("…" if len(h1_raw) > 48 else "")
        _body_clean, _toc_items = _extract_toc(body)
        _sidebar, _mobile_toc = _toc_blocks(_toc_items)
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
<div class="content-grid">
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
    if ov and ov.get("title") and existing_body:
        # Has explicit title override and recoverable body — apply new meta
        body   = existing_body
        title  = ov["title"]
        desc   = ov["desc"]
        h1_raw = ov.get("h1", title)
    elif existing_body:
        # Non-expanded post with existing built HTML — recover meta from it, no fetch needed
        body = existing_body
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
    title = truncate(title, 60)
    desc = truncate(desc, 160) if desc else truncate(title + " — Mediations Australia.", 160)

    title = truncate(title, 60)
    desc = truncate(desc, 160) if desc else truncate(title + " — Mediations Australia.", 160)

    _h1_plain = h1_raw[:60]
    schema = [org_schema(), breadcrumb_schema([("Home", ""), ("Guides", "guides"), (_h1_plain, None)]), article_schema(title, desc)]
    doc = head(title, desc, slug, og_type="article", extra_schema=schema)
    doc = doc.replace("</head>", POST_CSS + "</head>")
    doc += nav()
    _crumb_label = h1_raw[:48] + ("…" if len(h1_raw) > 48 else "")
    _body_clean, _toc_items = _extract_toc(body)
    _sidebar, _mobile_toc = _toc_blocks(_toc_items)
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
<div class="content-grid">
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
