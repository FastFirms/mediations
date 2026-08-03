#!/usr/bin/env python3
"""Hub page: /family-lawyers/ — links to all city family-lawyer pages.
Internal link equity concentrator; intercepts "family lawyers [city]" + "family mediation" intent.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, BOOK_URL, PHONE, PHONE_HREF)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SLUG = "family-lawyers"
TITLE = "Family Lawyers & Mediation by City | Mediations Australia"
DESC = ("Find family mediation and dispute resolution services across Australia. "
        "City guides covering property, parenting, divorce and separation — without court.")

# (slug, city, state, blurb)
CITIES = [
    ("sydney-mediation",            "Sydney",         "NSW", "One of Australia's busiest family law jurisdictions. Mediation avoids the Parramatta and Sydney registry backlogs."),
    ("melbourne-mediation",         "Melbourne",      "VIC", "Major registry with long waiting lists for contested matters. Mediation resolves most cases in a single day."),
    ("brisbane-mediation",          "Brisbane",       "QLD", "Rapidly growing city with rising family law caseloads. Mediation offers a faster, local alternative to court."),
    ("perth-mediation",             "Perth",          "WA",  "WA operates its own family court system. Our mediators are experienced in WA-specific family law procedures."),
    ("adelaide-mediation",          "Adelaide",       "SA",  "South Australian families increasingly choose mediation over the Adelaide registry's contested matter wait times."),
    ("canberra-family-lawyers",     "Canberra",       "ACT", "Public servants, defence personnel and high-asset families benefit from the confidentiality mediation provides."),
    ("penrith-family-lawyers",      "Penrith",        "NSW", "Greater Western Sydney's busiest growth corridor. The Parramatta registry is under significant pressure."),
    ("newcastle-family-lawyers",    "Newcastle",      "NSW", "Hunter Valley families use mediation to resolve matters without the delays of the Newcastle registry."),
    ("wollongong-family-lawyers",   "Wollongong",     "NSW", "Illawarra clients resolve property and parenting matters through mediation, avoiding travel to Sydney courts."),
    ("central-coast-family-lawyers","Central Coast",  "NSW", "Large population of Sydney relocatees with significant property assets. Both Sydney and Newcastle registries apply."),
    ("campbelltown-family-lawyers", "Campbelltown",   "NSW", "South-West Sydney's fast-growing population is placing real pressure on the Parramatta registry."),
    ("gold-coast-family-lawyers",   "Gold Coast",     "QLD", "Queensland's second city. Brisbane registry handles Gold Coast matters — mediation avoids the wait."),
    ("ipswich-family-lawyers",      "Ipswich",        "QLD", "One of Queensland's fastest-growing cities. Mediation resolves matters the Brisbane registry takes years to hear."),
    ("toowoomba-family-lawyers",    "Toowoomba",      "QLD", "Regional Queensland's largest inland city. Circuit court sittings are infrequent — online mediation is ideal."),
    ("townsville-family-lawyers",   "Townsville",     "QLD", "North Queensland families use online mediation to resolve disputes without travelling to Brisbane courts."),
    ("rockhampton-family-lawyers",  "Rockhampton",    "QLD", "Central Queensland's main regional centre. Circuit court waiting times make early mediation especially valuable."),
    ("geelong-family-lawyers",      "Geelong",        "VIC", "Victoria's second city. Mediation resolves matters in a single day — no need to travel to Melbourne."),
    ("ballarat-family-lawyers",     "Ballarat",       "VIC", "Farming properties and multi-generational assets make Ballarat matters well suited to mediation."),
    ("bendigo-family-lawyers",      "Bendigo",        "VIC", "Regional Victoria's major inland centre. Mediation avoids costly and time-consuming Melbourne court listings."),
    ("mandurah-family-lawyers",     "Mandurah",       "WA",  "Peel Region families — many with FIFO arrangements — benefit from WA-aware mediation services."),
    ("hobart-family-lawyers",       "Hobart",         "TAS", "Tasmania's close-knit community makes mediation's confidentiality especially important."),
    ("launceston-family-lawyers",   "Launceston",     "TAS", "Northern Tasmania's main city. Farming and business assets make confidential mediation the sensible first step."),
    ("darwin-family-lawyers",       "Darwin",         "NT",  "Highly transient population with defence and mining families. Online mediation avoids circuit court delays entirely."),
    ("adelaide-family-lawyers",     "Adelaide (SA)",  "SA",  "Capital city guide focused on South Australian family law, mediation costs and the Adelaide registry."),
]

STATE_ORDER = ["NSW", "VIC", "QLD", "WA", "SA", "ACT", "TAS", "NT"]

def state_full(abbr):
    return {
        "NSW": "New South Wales", "VIC": "Victoria", "QLD": "Queensland",
        "WA": "Western Australia", "SA": "South Australia", "ACT": "Australian Capital Territory",
        "TAS": "Tasmania", "NT": "Northern Territory"
    }.get(abbr, abbr)

def city_cards_html():
    groups = {s: [] for s in STATE_ORDER}
    for entry in CITIES:
        slug, city, state, blurb = entry
        if state in groups:
            groups[state].append(entry)
    out = []
    for state in STATE_ORDER:
        entries = groups.get(state, [])
        if not entries:
            continue
        out.append(f'<h2 id="{state.lower()}">{esc(state_full(state))}</h2>')
        out.append('<div class="fl-hub-grid">')
        for slug, city, state_abbr, blurb in entries:
            out.append(
                f'<a href="/{esc(slug)}/" class="fl-hub-card">'
                f'<span class="fl-hub-city">{esc(city)}</span>'
                f'<span class="fl-hub-state">{esc(state_abbr)}</span>'
                f'<span class="fl-hub-blurb">{esc(blurb)}</span>'
                f'<span class="fl-hub-cta">See {esc(city)} guide →</span>'
                f'</a>'
            )
        out.append('</div>')
    return "\n".join(out)

def toc_html():
    links = " · ".join(
        f'<a href="#{s.lower()}">{state_full(s)}</a>'
        for s in STATE_ORDER
    )
    return f'<p class="fl-hub-toc">Jump to: {links}</p>'

def itemlist_schema():
    items = []
    for i, (slug, city, state, blurb) in enumerate(CITIES, 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": f"{city} family mediation",
            "url": f"https://www.mediationsaustralia.com.au/{slug}/"
        })
    return {"@type": "ItemList", "name": "Family mediation services by city", "itemListElement": items}

QA = [
    ("Do I need a family lawyer to use Mediations Australia?",
     "No. You can come to mediation without a lawyer, though we always recommend you obtain independent legal advice before formalising any agreement. Many clients consult a lawyer before or after the mediation session rather than throughout the process."),
    ("Is mediation available in my city?",
     "Yes. We offer online mediation to clients anywhere in Australia, and in-person sessions in Sydney, Melbourne, Brisbane, Perth and Adelaide. The city guides on this page cover the local court context for each region."),
    ("How much does family mediation cost compared to going to court?",
     "Mediation typically costs $3,000-$8,000 total, shared between the parties. A contested family law matter through court commonly costs each party $30,000-$150,000 or more, and takes one to three years to resolve."),
    ("What types of family law matters can be mediated?",
     "Property settlement, parenting arrangements, spousal maintenance, superannuation splitting, estate disputes, and separation agreements can all be resolved through mediation. We also provide section 60I certificates required before filing parenting matters in court."),
    ("What is a section 60I certificate and do I need one?",
     "A section 60I certificate confirms that you have attempted family dispute resolution before filing parenting orders in the Federal Circuit and Family Court. Mediations Australia is a registered FDR provider and can issue these certificates where attendance requirements are met."),
]

def build():
    schema = [
        org_schema(),
        breadcrumb_schema([("Home", ""), ("Family lawyers by city", SLUG)]),
        faq_schema(QA),
        itemlist_schema(),
    ]

    css = """<style>
.fl-hub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:24px 0 40px}
.fl-hub-card{display:flex;flex-direction:column;gap:6px;padding:20px 22px;background:var(--cream);
  border:1.5px solid var(--line);border-radius:14px;text-decoration:none;color:var(--ink);
  transition:border-color .18s,box-shadow .18s}
.fl-hub-card:hover{border-color:var(--sage-deep);box-shadow:0 4px 18px rgba(0,0,0,.08)}
.fl-hub-city{font-weight:700;font-size:1.05rem;color:var(--ink)}
.fl-hub-state{font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-soft);margin-top:-4px}
.fl-hub-blurb{font-size:.88rem;color:var(--ink-soft);line-height:1.5;margin-top:4px}
.fl-hub-cta{font-size:.85rem;font-weight:600;color:var(--sage-deep);margin-top:auto;padding-top:10px}
.fl-hub-toc{font-size:.88rem;color:var(--ink-soft);margin-bottom:32px;line-height:1.8}
.fl-hub-toc a{color:var(--sage-deep);text-decoration:none}
.fl-hub-toc a:hover{text-decoration:underline}
.fl-hub-table{width:100%;border-collapse:collapse;margin:24px 0 40px;font-size:.95rem}
.fl-hub-table th,.fl-hub-table td{padding:12px 16px;text-align:left;border-bottom:1px solid var(--line)}
.fl-hub-table thead th{font-weight:700;background:var(--cream)}
.fl-hub-table tbody tr:last-child td{border-bottom:none}
.fl-hub-table td:first-child{color:var(--ink-soft)}
</style>"""

    d = head(TITLE, DESC, SLUG, extra_schema=schema) + css + nav()
    d += f"""<main id="main">
{crumb_html([("Home", ""), ("Family lawyers by city", None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Family law &amp; mediation</span>
<h1>Family Lawyers by City</h1>
<p class="lede">Find local family law context and mediation services for every major Australian city. We've helped thousands of families resolve property and parenting matters without court — in 1 day, not years.</p>
<div class="phero-cta">
<a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
</div>
</div></section>

<div class="wrap-narrow"><div class="answer reveal">
<p><strong>In short:</strong> Mediations Australia is a nationally accredited mediation service — not a law firm. We work alongside family lawyers and help separating couples resolve property settlement, parenting arrangements and other disputes without going to court. Our city guides explain the local court context and how mediation fits in.</p>
</div></div>

<article class="body"><div class="wrap reveal">
<h2>How we work with family lawyers</h2>
<p>Many clients come to us on the recommendation of their family lawyer — because a good family lawyer knows that mediation often produces better outcomes, faster and for less cost, than contested litigation. We're not a replacement for legal advice: we strongly recommend every client obtain independent legal advice before formalising any agreement. What we provide is a structured, expert facilitation process that helps both parties reach an agreement they can live with.</p>
<p>Once an agreement is reached in mediation, your lawyer can formalise it as consent orders or a binding financial agreement — giving it the same legal force as a court order, without the wait, the cost, or the public record.</p>

<h2>Family mediation services across Australia</h2>
<p>We offer online mediation to clients anywhere in Australia, and in-person sessions in Sydney, Melbourne, Brisbane, Perth and Adelaide. Every city guide below explains the local family court context, typical waiting times, and what mediation can realistically achieve for families in that region.</p>

{toc_html()}
{city_cards_html()}

<h2>Why choose mediation over a contested court matter?</h2>
<div style="overflow-x:auto">
<table class="fl-hub-table">
<thead><tr><th></th><th>Mediation</th><th>Contested litigation</th></tr></thead>
<tbody>
<tr><td>Time to resolution</td><td>1 day</td><td>1&ndash;3 years</td></tr>
<tr><td>Typical total cost (per party)</td><td>$1,500&ndash;$4,000</td><td>$30,000&ndash;$150,000+</td></tr>
<tr><td>Who decides the outcome</td><td>You</td><td>A judge</td></tr>
<tr><td>Confidential</td><td>Yes &mdash; protected by law</td><td>No &mdash; public record</td></tr>
<tr><td>Preserves co-parenting relationship</td><td>Collaborative by design</td><td>Adversarial by design</td></tr>
</tbody>
</table>
</div>

<h2>What we can help you resolve</h2>
<ul>
<li><strong>Property settlement</strong> &mdash; division of assets, superannuation splitting, the family home</li>
<li><strong>Parenting arrangements</strong> &mdash; living arrangements, time with each parent, decision-making</li>
<li><strong>Spousal maintenance</strong> &mdash; interim and ongoing financial support</li>
<li><strong>Section 60I certificates</strong> &mdash; required before filing parenting orders in court</li>
<li><strong>Binding financial agreements</strong> &mdash; formalised with your lawyer after agreement is reached</li>
<li><strong>Separation agreements</strong> &mdash; practical arrangements for separating couples not yet divorcing</li>
</ul>
</div></article>"""

    d += faq_html(QA, heading="Family mediation FAQs")
    d += cta_band("Ready to resolve your matter?",
                  "Book a free consultation. We respond within one business day.")
    d += "</main>" + page_end()

    p = os.path.join(OUT, SLUG)
    os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "index.html"), "w").write(d)
    import re
    words = len(re.sub(r'<[^>]+>', ' ', d).split())
    print(f"Built: /{SLUG}/ — ~{words} words")

build()
