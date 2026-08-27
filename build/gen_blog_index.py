#!/usr/bin/env python3
"""Blog/guides index page — topic-based UX redesign."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, cta_band,
                       org_schema, breadcrumb_schema, BOOK_URL, PHONE_HREF, PHONE, DOMAIN)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── CORNERSTONE GUIDES ────────────────────────────────────────────────────────
# Organised by topic section for the redesigned page.
# Each entry: (slug, title, blurb)

SEPARATION = [
    ("separation-guide",               "Separation in Australia: Complete Guide",            "First steps, the date of separation, who stays in the house, and protecting yourself."),
    ("de-facto-relationships-guide",   "De Facto Relationships & Separation",                "What counts as de facto, how assets are split, the two-year limit."),
    ("how-to-get-a-divorce-in-australia-a-step-by-step-guide", "How to Get a Divorce in Australia", "Eligibility, the 12-month rule, applying online, cost, and serving papers."),
    ("how-long-does-a-divorce-take",   "How Long Does a Divorce Take?",                      "The 12-month rule, processing times, and avoiding delays."),
    ("divorce-without-a-lawyer",       "Divorce Without a Lawyer",                           "How to DIY the application and the cost-effective middle path."),
    ("mediation-before-divorce",       "Mediation Before Divorce",                           "Why resolving parenting and property before filing saves time and money."),
    ("my-ex-wont-sign-divorce-papers", "My Ex Won't Sign the Divorce Papers",                "Your ex cannot block a divorce. The sole-applicant process explained."),
    ("same-sex-family-law",            "Same-Sex Separation & Divorce",                      "Equal rights for LGBTQ+ couples in divorce, property, parenting and de facto matters."),
]

PARENTING = [
    ("child-custody-mediation",        "Child Custody Mediation",                            "What the law says about custody, 50/50 care, and how parents agree without court."),
    ("parenting-plans-guide",          "Parenting Plans in Australia",                       "What to include, whether it's binding, and how to agree one through mediation."),
    ("fathers-rights",                 "Fathers' Rights After Separation",                   "The truth about 50/50 care, parental responsibility, and securing meaningful time."),
    ("mothers-rights",                 "Mothers' Rights in Family Law",                      "Parental responsibility, the best-interests test, and the myth of automatic preference."),
    ("co-parenting-mediation",         "Co-Parenting Mediation",                             "Resolving ongoing disputes over schedules, decisions and communication."),
    ("child-support-guide",            "Child Support in Australia",                         "The formula, how care affects payments, when it stops, and resolving disputes."),
    ("parental-alienation-australia",  "Parental Alienation in Australia",                   "What it is, how the law treats it, and rebuilding the relationship without court."),
    ("grandparents-rights",            "Grandparents' Rights in Australia",                  "How grandparents seek time with grandchildren — and why mediation comes first."),
    ("best-apps-for-separated-parents","Best Apps for Separated Parents",                    "Co-parenting apps that reduce conflict and create a court-admissible record."),
    ("stepparent-rights",              "Step-Parent Rights in Australia",                    "Parental responsibility, contact after separation, and staying in a child's life."),
]

PROPERTY = [
    ("property-settlement-after-separation", "Property Settlement After Separation",          "The four-step process, asset pool, time limits and how to settle without court."),
    ("what-am-i-entitled-to-in-a-separation-in-australia", "What Am I Entitled To?",         "How property, super and support are divided — and how to reach a fair split."),
    ("binding-financial-agreements-guide", "Binding Financial Agreements",                   "Prenups and postnups explained — what makes them valid and BFA vs consent orders."),
    ("consent-orders-explained",       "Consent Orders Explained",                           "How to make your agreement legally binding without going to court."),
    ("consent-orders-2026-update",     "Consent Orders 2026: What Changed",                  "The 2025 reforms, updated process, and what you need to know this year."),
    ("superannuation-and-divorce",     "Superannuation and Divorce",                         "How super splitting works, valuation, and why it matters — especially for carers."),
    ("property-settlement-mediation-guide", "Property Settlement Mediation Guide",           "How to prepare, what to bring, what to expect on the day."),
    ("what-is-in-the-property-pool",   "What's in the Property Pool?",                      "Assets, super, businesses, debts and inheritances — what counts."),
    ("spousal-maintenance-guide",      "Spousal Maintenance in Australia",                   "Who pays, how much, how long it lasts, and how it differs from child support."),
    ("business-in-divorce",            "Business in Divorce",                                "How businesses and trusts are valued and divided — and how to protect yours."),
    ("who-pays-bills-during-separation","Who Pays Bills During Separation?",                 "Mortgage, utilities, joint cards — and how to set up an interim arrangement."),
    ("pets-and-family-law",            "Pets and Family Law",                                "Who gets the pet after separation and the 2025 law changes."),
    ("delaying-property-settlement",   "Can My Ex Delay Settlement?",                        "Stalling tactics, time limits, and how mediation forces progress."),
]

PROCESS = [
    ("what-is-mediation-in-family-law","What Is Mediation in Family Law?",                  "How the process works, the mediator's role, why it succeeds, cost and time."),
    ("how-long-does-mediation-take",   "How Long Does Mediation Take?",                     "Most disputes resolve in one or two sessions — compared with years in court."),
    ("is-family-law-mediation-compulsory","Is Mediation Compulsory?",                       "When a Section 60I certificate is required, the exemptions, and if your ex refuses."),
    ("shuttle-mediation-guide",        "Shuttle Mediation Explained",                       "How keeping parties apart resolves high-conflict disputes safely."),
    ("online-mediation-australia",     "Online Mediation in Australia",                     "How it works, when to use it, and how to choose an accredited mediator."),
    ("mediate-or-litigate",            "Mediate or Litigate? How to Choose",                "An honest comparison of cost, time, control and outcomes."),
    ("what-happens-if-mediation-fails","What If Mediation Fails?",                          "Section 60I certificates, going to court, and why failure usually still helps."),
    ("arbitration-in-family-law",      "Arbitration in Family Law",                         "How a binding private decision is reached, faster than court."),
    ("are-mediation-agreements-legally-binding","Are Mediation Agreements Binding?",        "Heads of agreement, consent orders, BFAs — what each means for enforceability."),
    ("family-court-process-2026",      "The Family Court Process (2026)",                   "From filing to trial — how long it takes, what it costs, and how to avoid it."),
    ("conciliation-vs-mediation",      "Conciliation vs Mediation",                         "What each is, how the third party's role differs, and which suits your dispute."),
]

COSTS = [
    ("how-much-does-mediation-cost",   "How Much Does Mediation Cost?",                     "Family mediation fees, who pays, free options, and why it's far cheaper than court."),
    ("cost-of-divorce-in-australia",   "How Much Does Divorce Cost?",                       "Court fees, lawyer costs, and how mediation saves tens of thousands."),
    ("who-pays-for-mediation",         "Who Pays for Mediation?",                           "How the fee is usually split, when one party pays, and free options."),
    ("private-vs-free-mediation",      "Private vs Free Mediation",                         "Wait times, cost, complexity and outcomes — how to choose."),
    ("cant-afford-mediation",          "Can't Afford Mediation?",                           "Free, subsidised, Legal Aid, and reduced-fee — every realistic pathway."),
    ("is-family-mediation-free-australia","Is Family Mediation Free?",                      "When mediation can be free, when it's subsidised, and what to do if not."),
    ("family-relationship-centre-vs-private-mediation","FRC vs Private Mediation",          "An honest 10-factor comparison — when an FRC is the right call."),
    ("legal-aid-vs-private-mediation", "Legal Aid vs Private Mediation",                    "What Legal Aid covers and what to do if you don't qualify."),
    ("divorce-mediator-vs-divorce-lawyer","Mediator vs Lawyer: Which Do You Need?",         "What each does, what they cost, and why most people benefit from both."),
]

HIGH_CONFLICT = [
    ("mediation-with-a-narcissist",    "Mediation With a Narcissist",                       "Yes — often better than court. Proven strategies for high-conflict exes."),
    ("high-conflict-mediation",        "High-Conflict Family Law Mediation",                "How shuttle mediation resolves even the most bitter disputes."),
    ("high-conflict-family-law-mediation","When High-Conflict Mediation Works",             "When it works, when it doesn't, and what to do instead."),
    ("domestic-violence-and-family-law","Domestic Violence & Family Law",                   "Protection orders, safety during separation, mediation exemptions, and help."),
]

WORKPLACE = [
    ("workplace-mediation-guide",      "Workplace Mediation in Australia",                  "How it resolves workplace conflict, the Fair Work process, and the benefits."),
    ("victorian-right-to-work-from-home","Victoria's Right to Work From Home",              "What the law means for employers and employees — and resolving disputes fast."),
]

ESTATE = [
    ("estate-inheritance-dispute-mediation","Estate & Inheritance Dispute Mediation",       "Contested wills, family provision claims, executor disputes — resolved faster than court."),
]

LEGAL_UPDATES = [
    ("changes-to-family-law-act-2025", "Changes to the Family Law Act 2025",                "The new property framework, family violence, pets — what the reforms mean for you."),
    ("surrogacy-laws",                 "Surrogacy Laws in Australia",                       "Altruistic vs commercial, legal parentage, and the state-by-state rules."),
    ("can-you-record-your-ex",         "Can You Record Your Ex?",                           "Surveillance laws, whether recordings can be used in court, and what to do instead."),
]

# ── TOPIC SECTIONS ────────────────────────────────────────────────────────────
TOPICS = [
    ("separation",    "separation-icon",   "Separation & Divorce",        SEPARATION),
    ("parenting",     "parenting-icon",    "Parenting & Children",        PARENTING),
    ("property",      "property-icon",     "Property & Finances",         PROPERTY),
    ("process",       "process-icon",      "The Mediation Process",       PROCESS),
    ("costs",         "costs-icon",        "Costs & Affordability",       COSTS),
    ("highconflict",  "conflict-icon",     "High Conflict & Safety",      HIGH_CONFLICT),
    ("workplace",     "workplace-icon",    "Workplace Disputes",          WORKPLACE),
    ("estate",        "estate-icon",       "Estate & Inheritance",        ESTATE),
    ("updates",       "updates-icon",      "Legal Updates",               LEGAL_UPDATES),
]

# Build flat slug set for imported detection
cornerstone_slugs = set()
for _,_,_,posts in TOPICS:
    for slug,_,_ in posts:
        cornerstone_slugs.add(slug)

# ── SCHEMA ────────────────────────────────────────────────────────────────────
schema=[org_schema(),breadcrumb_schema([("Home",""),("Guides","guides")]),
        {"@type":"CollectionPage","name":"Mediation & Dispute Resolution Guides",
         "url":f"{DOMAIN}/guides/","isPartOf":{"@id":f"{DOMAIN}/#website"}}]

d = head("Mediation &amp; Dispute Resolution Guides | Mediations Australia",
    "Practical, expert guides on mediation, separation, workplace disputes, estate matters and more — written by accredited mediators to help you resolve disputes without court.",
    "guides", extra_schema=schema) + nav()

# ── TOPIC NAV ICONS (inline SVGs) ─────────────────────────────────────────────
TOPIC_ICONS = {
    "separation-icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "parenting-icon":  '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "property-icon":   '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>',
    "process-icon":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>',
    "costs-icon":      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "conflict-icon":   '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    "workplace-icon":  '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "estate-icon":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14,2 14,8 20,8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10,9 9,9 8,9"/></svg>',
    "updates-icon":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><polyline points="23,4 23,10 17,10"/><polyline points="1,20 1,14 7,14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',
}

# ── TOPIC NAV ─────────────────────────────────────────────────────────────────
def topic_nav():
    items = ""
    for tid, icon_key, label, posts in TOPICS:
        count = len(posts)
        icon = TOPIC_ICONS.get(icon_key, "")
        items += f'<a href="#{tid}" class="tnav-item"><span class="tnav-icon">{icon}</span><span class="tnav-label">{esc(label)}</span><span class="tnav-count">{count}</span></a>'
    return f'<nav class="topic-nav" aria-label="Guide topics"><div class="wrap tnav-inner">{items}</div></nav>'

# ── GUIDE CARD (compact, list-style within a topic) ───────────────────────────
def guide_card(slug, title, blurb):
    return (f'<a href="/{slug}/" class="gcard">'
            f'<span class="gcard-title">{esc(title)}</span>'
            f'<span class="gcard-blurb">{esc(blurb)}</span>'
            f'<span class="gcard-arr">→</span>'
            f'</a>')

# ── TOPIC SECTION ─────────────────────────────────────────────────────────────
def topic_section(tid, icon_key, label, posts):
    icon = TOPIC_ICONS.get(icon_key, "")
    cards = "".join(guide_card(s, t, b) for s, t, b in posts)
    return (f'<section class="tsec" id="{tid}">'
            f'<div class="wrap">'
            f'<div class="tsec-hd"><span class="tsec-icon">{icon}</span>'
            f'<h2>{esc(label)}</h2>'
            f'<span class="tsec-count">{len(posts)} guide{"s" if len(posts)!=1 else ""}</span>'
            f'</div>'
            f'<div class="gcards">{cards}</div>'
            f'</div></section>')

# ── AUTO-DISCOVER IMPORTED FOR SEARCH ─────────────────────────────────────────
SKIP_SLUGS = {
    "guides","about-mediations-australia","contact-us","book-a-consultation",
    "how-mediation-works","preparing-for-mediation","our-fee-structure",
    "family-law-mediation","divorce-mediation","property-settlement-mediation",
    "parenting-plan-mediation","section-60i-certificates","financial-agreements-mediation",
    "spousal-support-mediation","child-support-mediation","de-facto-mediation",
    "grandparents-mediation","consent-orders","online-divorce","workplace-mediation",
    "estate-dispute-mediation","collaborative-family-lawyers","family-law-arbitration",
    "divorce-counselling","memberships","our-mediators","our-team",
    "sydney-mediation","melbourne-mediation","brisbane-mediation","perth-mediation",
    "adelaide-mediation","canberra-mediation","gold-coast-mediation","newcastle-mediation",
    "wollongong-mediation","geelong-mediation","hobart-mediation","townsville-mediation",
    "cairns-mediation","toowoomba-mediation","ballarat-mediation","bendigo-mediation",
    "launceston-mediation","mackay-mediation","rockhampton-mediation","sunshine-coast-mediation",
    "bundaberg-mediation","darwin-mediation","coffs-harbour-mediation",
    "parenting-plan-template","bfa-or-consent-orders","getting-ready-for-separation",
    "family-law-cost-estimator","separation-under-one-roof-assessment",
    "questions","assets","sitemap",
}

import re as _re

def _read_title(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    m = _re.search(r"<title>(.*?)</title>", s, _re.I | _re.S)
    if not m: return None
    t = _re.sub(r"<[^>]+>","",m.group(1)).strip()
    t = _re.sub(r"\s*\|.*$","",t).strip()
    t = t.replace("&amp;","&")
    return t if t else None

# All searchable guides: cornerstones + imported
all_search = []
for _, _, _, posts in TOPICS:
    for slug, title, blurb in posts:
        all_search.append((slug, title))

imported_items = []
for slug in sorted(
    dd for dd in os.listdir(OUT)
    if os.path.isdir(os.path.join(OUT, dd))
    and dd not in cornerstone_slugs
    and dd not in SKIP_SLUGS
    and os.path.exists(os.path.join(OUT, dd, "index.html"))
    and open(os.path.join(OUT, dd, "index.html"), encoding="utf-8", errors="ignore").read().count("body-import") > 0
):
    title = _read_title(os.path.join(OUT, slug, "index.html"))
    if title:
        imported_items.append((slug, title))

# Combined search data (JSON for JS)
import json as _json
search_data = _json.dumps(
    [{"s": s, "t": t} for s, t in all_search] +
    [{"s": s, "t": t} for s, t in imported_items],
    ensure_ascii=False
)

n_total = len(all_search) + len(imported_items)

# ── BUILD PAGE ────────────────────────────────────────────────────────────────
d += f"""<main id="main">
{crumb_html([("Home",""),("Guides",None)])}

<section class="guides-hero"><div class="wrap">
  <span class="eyebrow"><span class="pulse"></span>Expert guides — free</span>
  <h1>Find the guide <em>you need</em>.</h1>
  <p class="lede">Practical answers on separation, property, parenting, workplace and estate disputes — written by accredited mediators.</p>
  <div class="ghero-search">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="search" id="gsearch" placeholder="Search {n_total} guides &amp; articles…" aria-label="Search guides" autocomplete="off">
  </div>
  <div id="search-results" class="search-results" hidden></div>
</div></section>

{topic_nav()}

{"".join(topic_section(tid, ik, label, posts) for tid, ik, label, posts in TOPICS)}

<section class="tsec" id="more-articles">
<div class="wrap">
  <div class="tsec-hd">
    <span class="tsec-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></span>
    <h2>More articles &amp; guides</h2>
    <span class="tsec-count">{len(imported_items)} articles</span>
  </div>
  <div class="aa-filter-wrap"><input type="search" id="aa-search" placeholder="Filter these articles…" aria-label="Filter articles" autocomplete="off"></div>
  <div class="gcards" id="aa-grid">{"".join(f'<a href="/{s}/" class="gcard aa-item"><span class="gcard-title">{esc(t)}</span><span class="gcard-arr">→</span></a>' for s,t in imported_items)}</div>
</div></section>
"""

d += cta_band("Can't find what you're <em>looking for</em>?",
    "Book a free consultation and get a direct answer from an accredited mediator — tailored to your situation.")
d += "</main>" + page_end()

# ── STYLES ────────────────────────────────────────────────────────────────────
d = d.replace("</head>", """<style>
/* Hero */
.guides-hero{padding:56px 0 48px;background:var(--sand)}
.guides-hero h1{font-size:clamp(2rem,4vw,3rem);margin-bottom:16px}
.ghero-search{position:relative;display:flex;align-items:center;max-width:560px;margin-top:28px}
.ghero-search svg{position:absolute;left:18px;color:var(--ink-soft);pointer-events:none;flex-shrink:0}
#gsearch{width:100%;padding:16px 20px 16px 52px;border:1.5px solid var(--line);border-radius:14px;font-size:1rem;font-family:inherit;color:var(--ink);background:#fff;outline:none;transition:border-color .15s;box-shadow:0 2px 8px rgba(0,0,0,.06)}
#gsearch:focus{border-color:var(--sage)}

/* Search results dropdown */
.search-results{position:absolute;top:calc(100% + 6px);left:0;right:0;background:#fff;border:1.5px solid var(--line);border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,.12);max-height:420px;overflow-y:auto;z-index:200}
.sr-item{display:flex;align-items:center;padding:13px 18px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink);transition:background .12s;gap:12px;font-size:.95rem}
.sr-item:last-child{border-bottom:none}
.sr-item:hover{background:var(--sand)}
.sr-item em{color:var(--sage-deep);font-style:normal;font-weight:600}
.sr-none{padding:18px;color:var(--ink-soft);font-size:.92rem;text-align:center}

/* Topic nav */
.topic-nav{background:var(--cream);border-bottom:1px solid var(--line);padding:20px 0}
.tnav-inner{display:flex;flex-wrap:wrap;gap:10px}
.tnav-item{display:flex;align-items:center;gap:9px;padding:12px 20px;border-radius:100px;border:1.5px solid var(--line);background:#fff;color:var(--ink);text-decoration:none;font-size:.92rem;font-weight:500;transition:all .15s;white-space:nowrap}
.tnav-item:hover{border-color:var(--sage);color:var(--sage-deep);background:var(--sand)}
.tnav-icon{color:var(--sage-deep);display:flex;align-items:center;flex-shrink:0}
.tnav-count{background:var(--sage-light);color:var(--sage-deep);border-radius:100px;padding:2px 10px;font-size:.78rem;font-weight:600}

/* Topic sections */
.tsec{padding:60px 0;border-bottom:1px solid var(--line)}
.tsec:nth-child(even){background:var(--cream)}
.tsec-hd{display:flex;align-items:center;gap:16px;margin-bottom:32px}
.tsec-icon{width:48px;height:48px;border-radius:14px;background:var(--sage-light);color:var(--sage-deep);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.tsec-hd h2{margin:0;font-size:1.6rem}
.tsec-count{margin-left:auto;font-size:.88rem;color:var(--ink-soft);white-space:nowrap;flex-shrink:0}

/* Guide cards */
.gcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.gcard{display:grid;grid-template-columns:1fr auto;grid-template-rows:auto auto;gap:4px 14px;align-items:start;padding:22px 24px;background:#fff;border:1.5px solid var(--line);border-radius:14px;text-decoration:none;color:var(--ink);transition:all .15s}
.gcard:hover{border-color:var(--sage);box-shadow:0 4px 18px rgba(0,0,0,.09);transform:translateY(-1px)}
.gcard-title{font-weight:600;font-size:1.02rem;color:var(--ink);grid-column:1;line-height:1.4}
.gcard-blurb{font-size:.87rem;color:var(--ink-soft);line-height:1.55;grid-column:1;margin-top:6px}
.gcard-arr{grid-column:2;grid-row:1/3;color:var(--sage-deep);font-size:1.2rem;align-self:center;opacity:.4;transition:opacity .15s,transform .15s}
.gcard:hover .gcard-arr{opacity:1;transform:translateX(4px)}

/* More articles filter */
.aa-filter-wrap{margin-bottom:24px}
#aa-search{width:100%;max-width:440px;padding:12px 18px;border:1.5px solid var(--line);border-radius:10px;font-size:.95rem;font-family:inherit;color:var(--ink);background:#fff;outline:none;transition:border-color .15s}
#aa-search:focus{border-color:var(--sage)}
.aa-item{align-items:center}

@media(max-width:768px){
  .gcards{grid-template-columns:1fr}
  .tnav-inner{gap:8px}
  .tnav-item{padding:10px 16px;font-size:.86rem}
}
</style></head>""")

# ── SEARCH SCRIPT ─────────────────────────────────────────────────────────────
d = d.replace("</body>", f"""<script>
(function(){{
  var DATA={search_data};
  var inp=document.getElementById('gsearch');
  var box=document.getElementById('search-results');
  if(!inp)return;
  function hl(text,q){{
    if(!q)return text;
    var re=new RegExp('('+q.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&')+')','gi');
    return text.replace(re,'<em>$1</em>');
  }}
  // Filter the "more articles" section
  var aas=document.getElementById('aa-search');
  var aag=document.getElementById('aa-grid');
  if(aas&&aag){{
    aas.addEventListener('input',function(){{
      var q=this.value.trim().toLowerCase();
      Array.from(aag.querySelectorAll('.aa-item')).forEach(function(el){{
        el.hidden=q.length>1&&el.textContent.toLowerCase().indexOf(q)===-1;
      }});
    }});
  }}
  inp.addEventListener('input',function(){{
    var q=this.value.trim();
    if(q.length<2){{box.hidden=true;return;}}
    var ql=q.toLowerCase();
    var hits=DATA.filter(function(d){{return d.t.toLowerCase().indexOf(ql)!==-1;}}).slice(0,12);
    if(!hits.length){{
      box.innerHTML='<p class="sr-none">No guides found — try different keywords.</p>';
    }}else{{
      box.innerHTML=hits.map(function(d){{
        return '<a class="sr-item" href="/'+d.s+'/">'+hl(d.t,q)+'</a>';
      }}).join('');
    }}
    box.hidden=false;
  }});
  document.addEventListener('click',function(e){{
    if(!inp.contains(e.target)&&!box.contains(e.target))box.hidden=true;
  }});
}})();
</script>
</body>""")

os.makedirs(os.path.join(OUT, "guides"), exist_ok=True)
open(os.path.join(OUT, "guides", "index.html"), "w").write(d)
n_guides = sum(len(p) for _,_,_,p in TOPICS)
print(f"Guides index built — {n_guides} cornerstones + {len(imported_items)} imported | {len(TOPICS)} topic sections")
