#!/usr/bin/env python3
"""Generate deep, substantive location pages (~1500+ words) with verified local detail."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN, OFFICES, SERVICES)
from location_data import LOCATION_DATA

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEAREST = {"NSW":"Sydney","VIC":"Melbourne","QLD":"Brisbane","WA":"Perth",
           "SA":"Melbourne","ACT":"Sydney","TAS":"Melbourne","NT":"Brisbane"}

OFFICE_GEO = {
    "Sydney":    {"lat": -33.8688, "lng": 151.2093,
                  "street": "Suite 508, 41/464-480 Kent St", "suburb": "Sydney", "state": "NSW", "post": "2000"},
    "Melbourne": {"lat": -37.8183, "lng": 144.9521,
                  "street": "Level 23, Collins Square Tower Five, 727 Collins St", "suburb": "Melbourne", "state": "VIC", "post": "3008"},
    "Brisbane":  {"lat": -27.4705, "lng": 153.0260,
                  "street": "Suite 507, 12B Anzac Square Arcade, 198 Adelaide St", "suburb": "Brisbane", "state": "QLD", "post": "4000"},
    "Perth":     {"lat": -31.9505, "lng": 115.8605,
                  "street": "Level 25, 108 St Georges Tce", "suburb": "Perth", "state": "WA", "post": "6000"},
}

def localservice_schema(city, state, slug, has_office=False):
    schema = {
        "@type": "LegalService",
        "@id": f"{DOMAIN}/{slug}/#legalservice",
        "name": f"Mediations Australia — {city}",
        "description": f"Nationally accredited mediators serving {city} and {state}, resolving family, property, workplace and commercial disputes without court.",
        "url": f"{DOMAIN}/{slug}/",
        "telephone": PHONE,
        "parentOrganization": {"@id": f"{DOMAIN}/#organization"},
        "areaServed": {"@type": "City", "name": city},
        "priceRange": "Free initial consultation",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens": "09:00", "closes": "17:00",
        },
    }
    if has_office and city in OFFICE_GEO:
        geo = OFFICE_GEO[city]
        schema["address"] = {
            "@type": "PostalAddress",
            "streetAddress": geo["street"],
            "addressLocality": geo["suburb"],
            "addressRegion": geo["state"],
            "postalCode": geo["post"],
            "addressCountry": "AU",
        }
        schema["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": geo["lat"],
            "longitude": geo["lng"],
        }
    return schema

# Keyword-first H1s: target phrase leads, persuasive tail varies by state.
# Primary ranking phrase "{City} Mediation" appears at the very start of every H1.
H1S = {
 "NSW":"{c} <em>Mediation</em>",
 "VIC":"{c} <em>Mediation</em>",
 "QLD":"{c} <em>Mediation</em>",
 "WA":"{c} <em>Mediation</em>",
 "SA":"{c} <em>Mediation</em>",
 "ACT":"{c} <em>Mediation</em>",
 "TAS":"{c} <em>Mediation</em>",
 "NT":"{c} <em>Mediation</em>",
}

def build(slug, city, state, own_reg, reg_desc, circuit, regions, has_office,
          office_addr, context, state_note, court_ref):
    nearest = NEAREST[state]
    h1 = H1S.get(state, "{c} <em>Mediation</em>").format(c=esc(city))
    title = f"{city} Mediation | Accredited Family Mediators"
    desc = (f"Nationally accredited {city} mediators resolve family, property and workplace "
            f"disputes without court — faster and cheaper. Call {PHONE}.")
    if has_office:
        office_line = f"Our {city} office is located at {office_addr}, and we also offer secure online mediation across {state}."
    else:
        office_line = (f"While our nearest office is in {nearest}, we regularly serve {city} clients "
                       f"both in person by arrangement and through secure online mediation — giving you "
                       f"the same nationally accredited mediators wherever you are in {state}.")

    qa = [
     (f"How much does mediation cost in {city}?",
      f"In {city} you start with a free initial consultation, so there are no billing surprises. Mediation typically costs a fraction of a contested court case — often the difference between a few hundred to a few thousand dollars shared between the parties, versus tens of thousands per side in litigation. Most matters resolve in one or two sessions."),
     (f"Where do you provide mediation in {city}?",
      f"We serve {regions}. {office_line}"),
     (f"Do {city} family law matters have to go to court?",
      f"Usually not. For most parenting matters you must attempt family dispute resolution first, and around 90% of the disputes we mediate resolve without a judge. A matter would only proceed to {court_ref} if it genuinely cannot be resolved by agreement."),
     (f"How long does mediation take in {city}?",
      f"Most {city} mediations resolve within one to two sessions, often in a single day. By contrast, a contested matter through {court_ref} can take one to three years to reach a final hearing."),
     (f"Can I do {city} mediation online?",
      f"Yes. We offer secure online mediation to all {city} and {state} clients, which is especially convenient for regional areas and removes any need to travel. Online agreements are just as binding once formalised."),
     ("Are your mediators nationally accredited?",
      "Yes. Our mediators are accredited under the Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS), the national benchmark, and many are also experienced family lawyers."),
     (f"What types of disputes can be mediated in {city}?",
      f"We mediate family and separation matters, property settlements, parenting arrangements, workplace and employment disputes, commercial and business disputes, estate and inheritance disputes, and personal injury claims across {city} and {state}."),
    ]

    schema = [org_schema(),
              breadcrumb_schema([("Home",""),(f"{city} Mediation",slug)]),
              localservice_schema(city, state, slug, has_office=has_office),
              faq_schema(qa)]
    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += f"""<main id="main">
{crumb_html([("Home",""),(f"{city} Mediation",None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>Serving {esc(city)} &amp; {esc(state)} · Nationally accredited</span>
    <h1>{h1}</h1>
    <p class="lede">Mediation in {esc(city)} gives individuals, families and businesses a faster, more affordable and less stressful way to resolve disputes. Our nationally accredited mediators help you reach a lasting agreement — and keep the decision in your hands, not a judge's.</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> Mediations Australia provides nationally accredited mediation in {esc(city)}, resolving family, property, workplace and commercial disputes faster and at a fraction of the cost of court. We serve {esc(regions)}, in person and through secure online mediation across {esc(state)}, with a 90% resolution rate and free initial consultations.</p></div></div>
<article class="body"><div class="wrap-narrow reveal">

<h2>Why choose mediation in {esc(city)}?</h2>
<p>When a relationship breaks down — whether between separating partners, business owners, employer and employee, or family members — the instinct is often to engage lawyers and prepare for court. But for the overwhelming majority of {esc(city)} disputes, litigation is the slowest, most expensive and most stressful path available. {esc(context)}</p>
<p>Mediation offers a fundamentally different approach. Instead of handing control to a judge, you and the other party work with a neutral, nationally accredited mediator to reach your own agreement. The mediator doesn't take sides or impose a decision — their role is to guide a structured, confidential conversation that cuts through conflict and finds workable solutions. Sometimes court is genuinely necessary, and a good lawyer will tell you when. But trying mediation first almost always saves time, money and stress, whatever happens next.</p>

<h2>{esc(city)} mediation vs going to court: an honest comparison</h2>
<p>It's worth being clear-eyed about the difference between the two paths, because for most people in {esc(city)} the contrast is stark:</p>
<ul>
  <li><strong>Time.</strong> Most {esc(city)} mediations resolve in a single day. A contested matter through {esc(court_ref)} can take one to three years to reach a final hearing.</li>
  <li><strong>Cost.</strong> Mediation starts with a fixed fee and is usually shared between the parties. Litigation can consume tens or even hundreds of thousands of dollars per side — frequently a significant share of the very assets in dispute.</li>
  <li><strong>Control.</strong> In mediation you design the outcome. In court, a judge who has known your situation for hours decides matters you've lived for years.</li>
  <li><strong>Privacy.</strong> Mediation is confidential and conducted on a "without prejudice" basis. Court proceedings are part of the public record.</li>
  <li><strong>Relationships.</strong> Litigation is adversarial by design. Mediation is collaborative, which matters enormously when you'll continue to co-parent, share a business, or move in the same circles.</li>
</ul>

<h2>How the {esc(city)} court system fits in</h2>
<p>{esc(reg_desc)}. {esc(circuit)} {esc(state_note)} Understanding where your matter would otherwise be heard matters, because it shows just how much mediation can save you. Rather than waiting for a listing at {esc(court_ref)}, you can often resolve your dispute in a single day — and if you do reach agreement, we can formalise it so it carries the same legal weight as a court order.</p>

<h2>Family, divorce, property and parenting mediation in {esc(city)}</h2>
<p>Whatever stage of separation you're at, there's a {esc(city)} mediation service built around it:</p>
<ul>
  <li><strong><a href="/family-law-mediation/">Family mediation in {esc(city)}</a></strong> — accredited family mediators resolving parenting and property without court.</li>
  <li><strong><a href="/divorce-mediation/">Divorce mediation in {esc(city)}</a></strong> — settle parenting, property and finances together as your marriage ends.</li>
  <li><strong><a href="/property-settlement-mediation/">Property settlement mediation in {esc(city)}</a></strong> — divide assets, debts and superannuation fairly and finally.</li>
  <li><strong><a href="/parenting-plan-mediation/">Parenting and child custody mediation in {esc(city)}</a></strong> — child-focused arrangements that actually last.</li>
</ul>
<p>Can't get to an office? Our <a href="/online-divorce/">secure online mediation</a> gives {esc(city)} and {esc(state)} clients the same nationally accredited mediators from anywhere — no travel, same structured process, same binding outcomes. And you can check <a href="/how-much-does-mediation-cost/">what mediation costs</a> before you commit to anything.</p>

<h2>What we resolve for {esc(city)} clients</h2>
<p>Our {esc(city)} mediators work across the full spectrum of dispute resolution. Whatever you're facing, there is almost always a path through it that doesn't begin in a courtroom:</p>
<ul>
  <li><strong><a href="/family-law-mediation/">Family law and separation</a></strong> — the practical and emotional work of separating, including divorce, without an adversarial court fight.</li>
  <li><strong><a href="/property-settlement-mediation/">Property settlements</a></strong> — dividing assets, debts, the family home and superannuation fairly and finally.</li>
  <li><strong><a href="/parenting-plan-mediation/">Parenting arrangements</a></strong> — child-focused plans covering living arrangements, time with each parent and decision-making.</li>
  <li><strong><a href="/workplace-mediation/">Workplace and employment disputes</a></strong> — resolving conflict, dismissals and complaints before they reach the Fair Work Commission.</li>
  <li><strong>Commercial and business disputes</strong> — contracts, partnerships and shareholder disagreements settled quickly and privately.</li>
  <li><strong>Estate and inheritance disputes</strong> — contested wills and family disagreements resolved with dignity.</li>
</ul>

<h2>What to expect from {esc(city)} mediation</h2>
<p>The process is designed to be calm, clear and free of jargon. You begin with a free initial consultation, where we listen to your situation and give you an honest view of whether mediation can help. One of our accredited mediators takes on your matter. The mediation itself can be conducted with everyone in the same room, or in separate rooms with the mediator moving between you — known as "shuttle" mediation — which is useful where there is high conflict or a safety concern. Where agreement is reached, we help you formalise it through <a href="/consent-orders/">consent orders</a> or a <a href="/financial-agreements-mediation/">binding financial agreement</a> so it is legally enforceable. You can <a href="/how-mediation-works/">read our full step-by-step guide to how mediation works</a> for more detail.</p>

<h2>Why {esc(city)} clients choose Mediations Australia</h2>
<p>Our mediators are nationally accredited under AMDRAS, and many are also experienced family lawyers — so the legal realities of your matter are understood from the outset. We're early-resolution focused, we work alongside your existing lawyer where you have one, and many of the people we help are in fact referred to us by the very solicitors advising them. With a 90% resolution rate across thousands of matters, free initial consultations and both in-person and online options, {esc(city)} clients get genuine expertise and a real alternative to litigation. <a href="/about-mediations-australia/">Learn more about Mediations Australia →</a></p>

<h2>{esc(city)} family lawyers <em>and</em> mediators</h2>
<p>If you were searching for "{esc(city)} family lawyers", you're in the right place. Our team includes accredited family lawyers — but the way we work is different. Rather than starting with the assumption that your matter belongs in court, we start with the question of whether it needs to. For the vast majority of separations, the answer is no: mediation resolves matters faster, far more cheaply, and with less damage to the family. We give you the legal insight of a family lawyer and the resolution focus of a mediator, in one place. <a href="/mediate-or-litigate/">See why mediation usually beats litigation →</a></p>

</div></article>"""

    # ── EXPANDED LOCAL CONTENT (fatten pages substantially) ─────────────────
    STATE_COURT_COSTS = {
        "NSW": ("$30,000–$80,000", "12–24 months"),
        "VIC": ("$30,000–$80,000", "12–24 months"),
        "QLD": ("$25,000–$75,000", "10–22 months"),
        "WA":  ("$25,000–$75,000", "10–22 months"),
        "SA":  ("$20,000–$65,000", "10–20 months"),
        "ACT": ("$25,000–$70,000", "10–20 months"),
        "TAS": ("$20,000–$65,000", "10–20 months"),
        "NT":  ("$20,000–$65,000", "10–20 months"),
    }
    lit_cost, lit_time = STATE_COURT_COSTS.get(state, ("$25,000–$70,000", "12–24 months"))

    SUBURB_DETAIL = {
        "sydney-mediation": "the Sydney CBD, Surry Hills, Pyrmont, the North Shore (Chatswood, St Leonards, Pymble), the Eastern Suburbs (Bondi, Randwick, Maroubra), the Northern Beaches (Manly, Dee Why, Mona Vale), the Hills District (Castle Hill, Kellyville), Parramatta and Greater Western Sydney (Blacktown, Penrith, Campbelltown), the Inner West (Leichhardt, Marrickville, Strathfield) and Wollongong",
        "melbourne-mediation": "Melbourne CBD, Fitzroy, Collingwood, South Yarra, the inner east (Hawthorn, Kew, Camberwell), the eastern suburbs (Box Hill, Glen Waverley, Knox), the south-east (Dandenong, Berwick, Frankston), the west (Footscray, Sunshine, Werribee), the northern suburbs (Preston, Bundoora, Epping) and the Mornington Peninsula",
        "brisbane-mediation": "Brisbane CBD, New Farm, Teneriffe, Woolloongabba, the northern suburbs (Chermside, Aspley, Bracken Ridge), the south side (Mount Gravatt, Sunnybank, Capalaba), Ipswich, the western corridor, Logan, the Redlands and Bayside",
        "perth-mediation": "Perth CBD, Subiaco, Leederville, Victoria Park, the northern suburbs (Joondalup, Wanneroo, Burns Beach), the southern suburbs (Fremantle, Cockburn, Mandurah, Rockingham) and the eastern suburbs (Midland, Mundaring)",
        "adelaide-mediation": "the Adelaide CBD, the inner eastern suburbs (Burnside, Kensington, Norwood), the northern suburbs (Elizabeth, Salisbury, Gawler), the southern suburbs (Noarlunga, Morphett Vale, Aldinga) and the Adelaide Hills",
        "canberra-mediation": "all ACT suburbs — Tuggeranong, Woden, Belconnen, Gungahlin, the Inner North and Inner South — and Queanbeyan and the surrounding Capital Region of NSW",
        "gold-coast-mediation": "Southport, Surfers Paradise, Broadbeach, Burleigh Heads, Robina, Coomera, Hope Island, Helensvale, Upper Coomera and Coolangatta",
        "newcastle-mediation": "Newcastle CBD, the Hunter Valley, Lake Macquarie, Maitland, Cessnock, the Upper Hunter, Port Stephens and the Central Coast",
        "wollongong-mediation": "Wollongong, Shellharbour, Kiama, Albion Park, Dapto, the Illawarra and the NSW South Coast from Nowra to Ulladulla",
        "geelong-mediation": "Geelong, Torquay, Lara, Leopold, Drysdale, Ocean Grove, Barwon Heads, Colac and the Surf Coast",
        "hobart-mediation": "Hobart, Kingston, Glenorchy, the Derwent Valley, the Huon Valley and southern Tasmania",
        "darwin-mediation": "Darwin, Palmerston, the rural area, Katherine and the Top End",
        "cairns-mediation": "Cairns, the northern beaches, the Atherton Tablelands, Port Douglas and Far North Queensland",
        "townsville-mediation": "Townsville, the northern beaches, Thuringowa, Ayr and North Queensland",
        "toowoomba-mediation": "Toowoomba, the Darling Downs, the Lockyer Valley and South West Queensland",
        "sunshine-coast-mediation": "Maroochydore, Noosa, Caloundra, Nambour, Mooloolaba and the wider Sunshine Coast",
        "bendigo-mediation": "Bendigo, the Loddon region, Castlemaine, Heathcote and central Victoria",
        "coffs-harbour-mediation": "Coffs Harbour, the Mid North Coast, Grafton, Woolgoolga and surrounding regions",
        "launceston-mediation": "Launceston, the Tamar Valley, Devonport, Burnie and northern Tasmania",
        "mackay-mediation": "Mackay, the Whitsundays, Proserpine, Sarina and the central Queensland coast",
        "rockhampton-mediation": "Rockhampton, Gladstone, Yeppoon, Emerald and central Queensland",
    }
    suburb_detail = SUBURB_DETAIL.get(slug, f"across {esc(regions)}")

    doc += f"""<section class="sec" style="padding-top:0"><div class="wrap-narrow reveal">
<h2>Mediation costs in {esc(city)}: what you can expect to pay</h2>
<p>Cost is the most common concern we hear from {esc(city)} clients considering mediation. Here is an honest comparison — drawn from real Australian figures — so you can make an informed decision.</p>
<figure class="tbl"><table>
<thead><tr><th>Approach</th><th>Typical cost (per party)</th><th>Timeframe</th><th>Who decides</th></tr></thead>
<tbody>
<tr><td><strong>Mediation (Mediations Australia)</strong></td><td>$1,500–$4,500 total shared</td><td>1–2 sessions, often same day</td><td>You and the other party</td></tr>
<tr><td>Mediation with solicitor support</td><td>$3,000–$8,000 total</td><td>2–4 weeks</td><td>You and the other party</td></tr>
<tr><td>Solicitor-negotiated settlement</td><td>$8,000–$25,000 each</td><td>3–9 months</td><td>Lawyers negotiate</td></tr>
<tr><td>Contested court hearing ({esc(court_ref)})</td><td>{lit_cost} each</td><td>{lit_time}</td><td>Judge</td></tr>
</tbody></table></figure>
<p>The most important figure in this table is not what you spend on mediation — it is what you avoid spending on litigation. A contested property settlement drawn from {esc(court_ref)} can cost both parties more than $100,000 combined, with funds drawn directly from the asset pool that was supposed to be divided. Mediation costs a fraction of this. And because the initial consultation is free, there is genuinely no cost to finding out whether it will help.</p>
<p>For most parenting matters in {esc(city)}, resolution happens in a single session of three to five hours. Property settlements involving more complex assets may take two sessions. That is still far faster and cheaper than the alternative.</p>
<p><a href="/how-much-does-mediation-cost/">See our full guide to mediation costs in Australia →</a></p>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap-narrow reveal">
<h2>Areas and suburbs we serve in {esc(city)}</h2>
<p>Our {esc(city)} mediation service covers {suburb_detail}, as well as regional {esc(state)} through our secure online mediation service.</p>
<p>Online mediation gives {esc(city)} and regional {esc(state)} clients access to exactly the same nationally accredited mediators as our in-person sessions — with no travel required. Agreements reached online are just as legally valid once formalised through consent orders or a binding financial agreement. If you are unsure whether we serve your area, call us on {PHONE} and we will give you an immediate answer.</p>
{f'<p>Our {esc(city)} office is at {esc(office_addr)}, with accessible facilities and parking nearby.</p>' if has_office else f'<p>Our nearest office is in {esc(NEAREST[state])}, and we arrange {esc(city)} in-person sessions by prior arrangement — or conduct your matter entirely online, which most regional {esc(state)} clients prefer.</p>'}
<p><a href="/online-divorce/">Find out more about our online mediation service →</a></p>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap-narrow reveal">
<h2>2025 family law changes: what they mean for {esc(city)} clients</h2>
<p>The <em>Family Law Amendment Act 2024</em> made significant changes that took effect in May 2025. They affect how property settlements and parenting arrangements are assessed — including, critically, the <em>consent orders</em> that formalise mediated agreements.</p>
<ul>
<li><strong>Property settlements:</strong> Following the High Court's Ascot Investments decision, the controversial "add-backs" practice has largely been removed. Courts can no longer routinely add back amounts one party spent before trial, which changes the negotiating landscape — and makes reaching agreement through mediation even more valuable, because you control the outcome rather than waiting for a court to apply evolving law to your circumstances.</li>
<li><strong>Parenting arrangements:</strong> The 2023 amendments (already in effect) removed the presumption of equal shared parental responsibility. Courts now focus purely on what is in the child's best interests, without a default presumption toward equal time. An agreed parenting plan reached in mediation gives both parents far more control over the outcome than any court order — and reflects what actually works for the family rather than a legal default.</li>
<li><strong>Family violence emphasis:</strong> The amended Act gives greater weight to family violence considerations in both property and parenting matters. Where there are safety concerns, special mediation arrangements — including shuttle mediation, where parties never meet — are available. Call us to discuss this confidentially.</li>
</ul>
<p>These changes make the case for early mediation in {esc(city)} stronger than ever. In a legal landscape that is actively evolving, an agreed outcome now is more predictable than waiting for a judge to apply new law to your circumstances — possibly 12–24 months from now.</p>
<p><a href="/changes-to-the-family-law-act-2025-you-must-know/">Read our full guide to the 2025 Family Law Act changes →</a></p>
</div></section>"""

    # city-specific service pages (for cities that have them)
    city_key = slug.replace('-mediation', '')
    SVC_CITY = {
        "property-settlement-mediation": ("Property Settlement", "Divide assets, superannuation and the family home by agreement — without court."),
        "divorce-mediation":             ("Divorce Mediation",   "Resolve property, parenting and finances across the whole separation in one process."),
        "parenting-mediation":           ("Parenting Arrangements", "Child-focused arrangements agreed by both parents — faster and more durable than court orders."),
        "workplace-mediation":           ("Workplace Mediation", "Resolve employment disputes, grievances and unfair dismissal claims before they escalate."),
    }
    CITIES_WITH_SVC = {"sydney","melbourne","brisbane","perth","adelaide","canberra","gold-coast"}
    if city_key in CITIES_WITH_SVC:
        svc_cards = "".join(
            f'<article class="card"><h3>{esc(name)}</h3><p>{esc(desc)}</p>'
            f'<a class="more" href="/{svc}-{city_key}/">Learn more <span class="arr">→</span></a></article>'
            for svc, (name, desc) in SVC_CITY.items())
        doc += f"""<section class="sec" style="padding-top:0"><div class="wrap">
<div class="reveal"><p class="sec-tag">{esc(city)} specialist services</p>
<h2 class="sec-title">{esc(city)} mediation, <em>by dispute type</em>.</h2>
<p class="sec-intro" style="max-width:54ch">Each service below is tailored specifically to {esc(city)} &mdash; with local court registry detail, realistic cost and timing, and {esc(city)}-specific legal context.</p></div>
<div class="cards reveal" style="margin-top:46px">{svc_cards}</div></div></section>"""
    # generic services grid
    cards = "".join(
        f'<article class="card"><h3>{esc(n)}</h3><p>{esc(d)}</p>'
        f'<a class="more" href="/{s}/">Learn more <span class="arr">→</span></a></article>'
        for s, n, d in SERVICES[:6])
    doc += f"""<section class="sec" style="padding-top:0"><div class="wrap">
<div class="reveal"><p class="sec-tag">All services</p>
<h2 class="sec-title">Every kind of dispute, <em>resolved locally</em>.</h2></div>
<div class="cards reveal" style="margin-top:46px">{cards}</div></div></section>"""
    doc += faq_html(qa, heading=f"{city} mediation FAQs")
    doc += cta_band(f"Resolve your {esc(city)} dispute, <em>starting today</em>.",
        f"Book a free initial consultation with a nationally accredited {esc(city)} mediator and find out how mediation can help — in person or online.")
    doc += "</main>" + page_end()
    path = os.path.join(OUT, slug); os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)
    # word count
    import re
    text = re.sub(r'<[^>]+>',' ', doc)
    return slug, len(text.split())

results = [build(*row) for row in LOCATION_DATA]
print("Deep location pages built:")
for s,w in results: print(f"  {s}: ~{w} words")
