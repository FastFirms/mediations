#!/usr/bin/env python3
"""Generate city-level 'family lawyers' pages that intercept lawyer-search intent
and honestly reframe it: most people at this stage need a mediator, not litigation.

Tier 1 (~1,500 words): 10 cities with strongest organic traffic.
Tier 2 (~800 words): 11 additional regional/secondary cities.
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN, SERVICES)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEAREST = {"NSW": "Sydney", "VIC": "Melbourne", "QLD": "Brisbane", "WA": "Perth",
           "SA": "Melbourne", "ACT": "Sydney", "TAS": "Melbourne", "NT": "Brisbane"}


def localservice_schema(city, state, slug):
    """LocalService schema for a city family-lawyers page (no physical office)."""
    return {
        "@type": "LegalService",
        "@id": DOMAIN + "/" + slug + "/#legalservice",
        "name": "Mediations Australia — " + city + " Family Mediation",
        "description": (
            "Nationally accredited mediators serving " + city + " and " + state +
            ", resolving family, property and parenting disputes without court. "
            "The honest alternative to engaging a family lawyer at separation."
        ),
        "url": DOMAIN + "/" + slug + "/",
        "telephone": PHONE,
        "parentOrganization": {"@id": DOMAIN + "/#organization"},
        "areaServed": {"@type": "City", "name": city},
        "priceRange": "Free initial consultation",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00",
            "closes": "17:00",
        },
    }


# ---------------------------------------------------------------------------
# City data
# ---------------------------------------------------------------------------

TIER1 = [
    # (slug, city, state, nearest_office, court_ref, local_context, city_specific)
    ("canberra-family-lawyers", "Canberra", "ACT", "Sydney",
     "the Canberra registry of the Federal Circuit and Family Court of Australia",
     "Canberra is a small, close-knit city where family law disputes carry a particular "
     "weight — you’re likely to encounter the other party at the school gate, at work, "
     "or in the same social circles. Confidentiality matters more here than almost anywhere, "
     "which is one reason mediation suits Canberra clients especially well.",
     "<h2>What makes Canberra family law matters distinctive</h2>"
     "<p>Canberra’s demographic profile shapes its family law matters in ways that make "
     "out-of-court resolution particularly valuable. A high proportion of ACT residents are "
     "Commonwealth public servants, many with defined benefit superannuation entitlements that "
     "require specialist valuation — and whose employment is part of the public record "
     "the moment a matter enters the courts. Defence personnel with security clearances face "
     "similar sensitivities: a contested, public court proceeding can create professional "
     "complications that have nothing to do with the legal outcome.</p>"
     "<p>Canberra also has one of the highest median property values in Australia. The family "
     "home — often acquired on dual public sector incomes — is frequently the most significant "
     "asset in the property pool. And in a city where the legal profession, the public service, "
     "and the private sector all overlap significantly, the lawyer you engage and the judge "
     "who hears your matter may well know people you both know. Confidential mediation "
     "removes that exposure entirely.</p>"),

    ("penrith-family-lawyers", "Penrith", "NSW", "Sydney",
     "the Parramatta registry of the Federal Circuit and Family Court of Australia",
     "Penrith and Greater Western Sydney have seen significant population growth, and with it, "
     "a sharp rise in family law matters. The Parramatta registry serves this region, but waiting "
     "times for contested matters routinely run to 18 months to two years — which makes "
     "resolving matters by agreement, through mediation, a genuinely compelling alternative.",
     "<h2>Family law in Greater Western Sydney: what Penrith clients face</h2>"
     "<p>Western Sydney’s property market has seen extraordinary price growth over the past "
     "decade. Many Penrith families who bought a home for $400,000-$600,000 are now sitting "
     "on a property worth $900,000 or more. That equity is real and significant — but "
     "litigation consumes a meaningful portion of it. A contested matter through the Parramatta "
     "registry, with both parties paying legal fees for 18-24 months, can easily cost "
     "$60,000-$120,000 in combined legal costs. Mediation typically resolves the same matter "
     "for $3,000–$4,500 total, shared between the parties.</p>"
     "<p>The Parramatta registry is one of the busiest family law registries in Australia. "
     "Greater Western Sydney’s rapid population growth has not been matched by proportionate "
     "court resources. Waiting times for contested final hearings are among the longest in "
     "the country — which means the practical choice for Penrith families is often between "
     "resolving through mediation in a single day, or waiting years for a court date while"
     "legal costs accumulate.</p>"),

    ("ballarat-family-lawyers", "Ballarat", "VIC", "Melbourne",
     "the Melbourne registry of the Federal Circuit and Family Court of Australia, "
     "which circuits to Ballarat",
     "Ballarat is regional Victoria’s largest inland city. Family law matters here often "
     "involve significant property equity — farms, investment properties, local businesses "
     "— alongside parenting arrangements. The nearest major registry is Melbourne, 110 "
     "kilometres away, which makes a local, early-resolution approach particularly valuable.",
     "<h2>Property and farming matters in Ballarat family law</h2>"
     "<p>Ballarat and the Central Highlands have a significant proportion of family law matters "
     "involving farming properties, rural land, and multi-generational family assets — where "
     "values are genuinely difficult to agree on and division is complex. A working farm "
     "cannot simply be split in two, and its valuation for property settlement purposes often "
     "requires specialist input. Mediation allows that process to happen in a structured, "
     "confidential setting, with both parties able to bring their own advisers and reach a "
     "practical outcome — without handing the decision to a Melbourne judge who may have "
     "limited familiarity with agricultural assets or Central Highlands property values.</p>"
     "<p>The Melbourne registry circuits to Ballarat, but circuit sittings are infrequent. "
     "Matters that cannot be resolved locally face the prospect of travel to Melbourne and "
     "the Melbourne registry’s considerable waiting list. For Ballarat families managing "
     "a farm, a local business, or young children, the practical burden of protracted "
     "Melbourne litigation is substantial. Early mediation removes that burden almost entirely.</p>"),

    ("mandurah-family-lawyers", "Mandurah", "WA", "Perth",
     "the Family Court of Western Australia",
     "Mandurah is one of Australia’s fastest-growing cities, with many families who have "
     "significant assets tied up in property. Western Australia operates its own separate family "
     "court system — the Family Court of Western Australia — which makes WA-aware "
     "mediators genuinely valuable. Resolving matters before they enter that system saves time, "
     "money and stress.",
     "<h2>Mandurah, the Peel Region, and the WA family court system</h2>"
     "<p>Western Australia is the only state with its own dedicated family court — the "
     "Family Court of Western Australia — which operates under slightly different procedures "
     "from the federal system covering the rest of Australia. For Mandurah clients, matters "
     "are heard in Perth (75 kilometres away) rather than a federal registry. Navigating "
     "WA’s distinct family law procedures is one reason why mediators with WA-specific "
     "experience are more useful here than a generalist approach.</p>"
     "<p>The Peel Region has a high proportion of FIFO workers in the resources sector, "
     "whose income structures — irregular rosters, resource sector bonuses, employer-provided "
     "housing — require particular care in property settlements and parenting arrangements. "
     "Mandurah’s coastal property market has also experienced significant price growth, making "
     "the family home a major and often contested component of the property pool. Resolving "
     "these matters through mediation — where both parties can address the specific realities "
     "of FIFO parenting and resource sector income directly — typically produces far more "
     "workable outcomes than a court order drafted without that local context.</p>"),

    ("hobart-family-lawyers", "Hobart", "TAS", "Melbourne",
     "the Hobart registry of the Federal Circuit and Family Court of Australia",
     "Tasmania’s small legal and social community means family law disputes can have a wide "
     "ripple effect on professional and personal relationships. Hobart has its own FCFCOA registry, "
     "but court waiting times still run to over a year for contested matters. Mediation’s "
     "confidentiality and speed are particularly valuable here.",
     "<h2>Why confidentiality matters more in Hobart family law</h2>"
     "<p>Hobart is Australia’s second smallest capital city, and its tight social fabric means "
     "family law disputes carry a different weight than in a larger city. The legal profession, "
     "the medical community, the public service, the business sector and the education sector "
     "all overlap significantly in Hobart — people know each other, and word travels. Court "
     "proceedings are a matter of public record. For many Hobart clients, the confidentiality "
     "of mediation is not just a convenience but a genuine professional necessity.</p>"
     "<p>Tasmania’s property market has experienced sharp price growth over recent years, "
     "particularly in Hobart’s inner suburbs. The family home — often purchased years ago "
     "at a fraction of its current value — is now frequently the dominant asset in the "
     "property pool, and its division requires careful, considered negotiation. A mediated "
     "settlement reached between the parties, with the benefit of independent legal advice "
     "alongside, almost always produces a more workable outcome than an order made by a "
     "Hobart judge on the basis of a few hours of evidence.</p>"),

    ("bendigo-family-lawyers", "Bendigo", "VIC", "Melbourne",
     "the Melbourne registry of the Federal Circuit and Family Court of Australia, "
     "which circuits to Bendigo",
     "Bendigo is one of regional Victoria’s major centres, 150 kilometres from Melbourne. "
     "Family law matters here often involve farming properties, local business interests, and "
     "multi-generational assets. Getting these resolved without litigation — which would "
     "require travel to Melbourne and months of delay — is a significant practical advantage.",
     ""),

    ("central-coast-family-lawyers", "Central Coast", "NSW", "Sydney",
     "the Newcastle or Sydney registry of the Federal Circuit and Family Court of Australia",
     "The Central Coast sits between Sydney and Newcastle, with a large and growing population "
     "of families who have relocated from Sydney. Many matters involve significant property assets "
     "accumulated during the Sydney boom years. Both the Sydney and Newcastle registries handle "
     "Central Coast matters, and both have substantial waiting lists for contested proceedings.",
     ""),

    ("darwin-family-lawyers", "Darwin", "NT", "Brisbane",
     "the Darwin registry of the Federal Circuit and Family Court of Australia",
     "Darwin has a highly transient population, with significant defence, mining and government "
     "sector families. Matters here sometimes involve interstate or international elements, remote "
     "property, and unique asset structures. The Territory’s remoteness makes online mediation "
     "especially practical — resolving a matter without travel or waiting for circuit court "
     "listings is a genuine advantage.",
     ""),

    ("launceston-family-lawyers", "Launceston", "TAS", "Melbourne",
     "the Launceston registry of the Federal Circuit and Family Court of Australia",
     "Launceston is northern Tasmania’s main city, with a close-knit professional and social "
     "community. Family law matters here — particularly those involving farming properties, "
     "local businesses, or multi-generational family assets — benefit enormously from a "
     "confidential, out-of-court process where the outcome doesn’t become part of the "
     "public record.",
     ""),

    ("adelaide-family-lawyers", "Adelaide", "SA", "Melbourne",
     "the Adelaide registry of the Federal Circuit and Family Court of Australia",
     "Adelaide is one of Australia’s most liveable capital cities, but family law disputes "
     "here are no less complex than anywhere else. The Adelaide registry handles a significant "
     "caseload, and contested matters take considerable time to resolve. South Australians "
     "increasingly turn to mediation as the faster, more affordable alternative — often "
     "resolving matters the Adelaide courts would take two years to hear.",
     ""),
]

TIER2 = [
    # (slug, city, state, nearest_office, court_ref, local_context)
    ("wollongong-family-lawyers", "Wollongong", "NSW", "Sydney",
     "the Wollongong circuit of the Federal Circuit and Family Court of Australia",
     "Wollongong and the Illawarra region are served by the Sydney and Wollongong circuit courts, "
     "but contested matters still involve significant delay. Many Wollongong families resolve "
     "property and parenting matters through mediation, avoiding the need to travel to Sydney "
     "for court."),

    ("campbelltown-family-lawyers", "Campbelltown", "NSW", "Sydney",
     "the Parramatta registry of the Federal Circuit and Family Court of Australia",
     "Campbelltown and South-West Sydney are served by the Parramatta registry. With one of the "
     "fastest-growing populations in NSW, the registry faces significant pressure — which "
     "makes early mediation a compelling alternative to waiting for a contested hearing."),

    ("ipswich-family-lawyers", "Ipswich", "QLD", "Brisbane",
     "the Brisbane registry of the Federal Circuit and Family Court of Australia",
     "Ipswich is one of Queensland’s fastest-growing cities. Family law matters here are "
     "generally heard through the Brisbane registry, which has a substantial caseload. Mediation "
     "offers Ipswich families a way to resolve parenting and property matters in weeks rather than "
     "the years a contested Brisbane hearing can take."),

    ("rockhampton-family-lawyers", "Rockhampton", "QLD", "Brisbane",
     "the Rockhampton circuit of the Federal Circuit and Family Court of Australia",
     "Rockhampton is central Queensland’s main regional centre. Court circuits serve the "
     "region but are infrequent, making the waiting time for contested matters particularly long. "
     "Online mediation removes the need to travel entirely, and is especially practical for "
     "regional Queensland clients."),

    ("melbourne-family-lawyers", "Melbourne", "VIC", "Melbourne",
     "the Melbourne registry of the Federal Circuit and Family Court of Australia",
     "Melbourne is Australia’s second largest city and one of its most active family law "
     "jurisdictions. While Mediations Australia has a Melbourne office, our role here is "
     "mediation — not litigation. For Melbourne clients caught up in the family court "
     "system’s delays, mediation offers a dramatically faster path."),

    ("geelong-family-lawyers", "Geelong", "VIC", "Melbourne",
     "the Melbourne registry of the Federal Circuit and Family Court of Australia, "
     "which circuits to Geelong",
     "Geelong is Victoria’s second city. Family law matters here may be heard at the "
     "Geelong circuit or the Melbourne registry. Either way, contested proceedings take "
     "considerable time. Many Geelong clients resolve matters through mediation in a single day — "
     "without the need to travel to Melbourne."),

    ("toowoomba-family-lawyers", "Toowoomba", "QLD", "Brisbane",
     "the Toowoomba circuit of the Federal Circuit and Family Court of Australia",
     "Toowoomba is Queensland’s largest inland city. Circuit court sittings serve the region, "
     "but they are infrequent and contested matters face long delays. Online mediation is "
     "particularly practical here, removing the need for travel and resolving matters far faster "
     "than the court circuit allows."),

    ("perth-family-lawyers", "Perth", "WA", "Perth",
     "the Family Court of Western Australia",
     "Perth is served by the Family Court of Western Australia — the only state-run family "
     "court in Australia. While Mediations Australia has a Perth office, our focus is mediation "
     "and early resolution. For Perth clients, resolving matters through mediation avoids the WA "
     "family court system’s waiting times entirely."),

    ("gold-coast-family-lawyers", "Gold Coast", "QLD", "Brisbane",
     "the Brisbane registry of the Federal Circuit and Family Court of Australia",
     "The Gold Coast’s rapid growth has brought with it a significant increase in family "
     "law matters, particularly those involving investment properties and business interests. "
     "Contested matters are heard through the Brisbane registry, which faces a heavy caseload. "
     "Many Gold Coast clients resolve their disputes through mediation, well before reaching court."),

    ("townsville-family-lawyers", "Townsville", "QLD", "Brisbane",
     "the Townsville registry of the Federal Circuit and Family Court of Australia",
     "Townsville is North Queensland’s main city, with its own FCFCOA registry. Defence "
     "families, mining sector workers, and rural property owners are common in Townsville family "
     "law matters. Online mediation is especially practical here, removing the need for travel "
     "and resolving matters faster than the registry allows."),

    ("newcastle-family-lawyers", "Newcastle", "NSW", "Sydney",
     "the Newcastle registry of the Federal Circuit and Family Court of Australia",
     "Newcastle and the Hunter Region are served by the Newcastle registry of the FCFCOA. The "
     "region has a significant industrial and property-owning population, with many family law "
     "matters involving significant assets. Mediation resolves most Newcastle matters far faster "
     "than the contested court pathway."),
]


# ---------------------------------------------------------------------------
# Tier 1 builder (~1,500 words)
# ---------------------------------------------------------------------------

def build_tier1(slug, city, state, nearest_office, court_ref, local_context, city_specific=""):
    ec = esc(city)
    es = esc(state)
    ecr = esc(court_ref)
    elc = esc(local_context)

    title = city + " Family Lawyers | Should You Mediate First?"
    desc = (
        "Most people searching for family lawyers in " + city + " need a mediator first. "
        "Our nationally accredited mediators resolve 90% of matters without court — "
        "faster, cheaper, and more private. Call " + PHONE + "."
    )

    h1 = ec + " Family Lawyers"

    answer_box = (
        "Most people searching for family lawyers in " + ec + " are at an early research "
        "stage — weighing up their options, not yet committed to litigation. For the "
        "vast majority, the right first step is mediation, not engaging a lawyer. Mediation "
        "resolves 90% of family disputes in one to two sessions, costs a fraction of court, "
        "and keeps the decision in your hands. Our nationally accredited mediators (many with "
        "family law backgrounds) help " + ec + " clients resolve parenting, property and "
        "financial matters without court — and work alongside your lawyer where you "
        "have one."
    )

    qa = [
        (
            "Do I need a family lawyer in " + city + " to separate?",
            "No. Separation itself requires no legal involvement at all — it is simply "
            "the decision to live separately. For the practical matters that follow (parenting "
            "arrangements, property division), most " + ec + " couples resolve these through "
            "mediation or negotiation, without either party engaging a lawyer. You may want "
            "independent legal advice at some stage — and we encourage that — but "
            "you don’t need to engage a family lawyer to begin the process."
        ),
        (
            "What does a family lawyer in " + city + " cost?",
            "Family lawyers in " + ec + " typically charge between $300 and $600 per hour. "
            "A contested matter — one that proceeds to a final hearing — commonly "
            "costs $15,000 to $150,000 or more per side, and that’s before court filing "
            "fees and barrister costs. Most matters settle before a final hearing, but the "
            "legal costs incurred getting there are rarely recovered. Mediation, by contrast, "
            "typically costs $3,000–$4,500 total, shared between both parties."
        ),
        (
            "Can I use a mediator instead of a family lawyer in " + city + "?",
            "For the vast majority of " + ec + " matters, yes. Mediation resolves parenting "
            "arrangements, property settlements, de facto separations, and financial matters "
            "without either party needing a family lawyer. Where the matter is complex, or "
            "where you want independent legal advice before or after mediation, a lawyer can "
            "work alongside your mediator — this is common and works well."
        ),
        (
            "What’s the difference between a mediator and a family lawyer?",
            "A family lawyer represents your interests and advises you on the law. A mediator "
            "is a neutral third party who helps both sides reach their own agreement — "
            "the mediator doesn’t take sides or give legal advice. Many of our mediators "
            "have family law backgrounds, so they understand the legal landscape, but their "
            "role in the room is to facilitate agreement, not to advocate for either party."
        ),
        (
            "How long does family law take in " + city + "?",
            "A contested family law matter through " + ecr + " can take one to three years "
            "to reach a final hearing. Mediation, by contrast, typically resolves matters in "
            "a single day — compared to years for a contested court matter. The "
            "difference in time, cost and stress is substantial."
        ),
        (
            "Can I still use my lawyer if I choose mediation?",
            "Yes, and many clients do. You can obtain independent legal advice before or after "
            "mediation, bring a lawyer as a support person, or have your lawyer review any "
            "agreement before it is formalised. Mediation and legal advice are complementary, "
            "not mutually exclusive."
        ),
        (
            "What if my ex has already engaged a family lawyer?",
            "It is still worth raising mediation. Many family lawyers in " + ec + " actively "
            "encourage their clients to attempt mediation before proceeding to court — "
            "both because the law requires it for parenting matters (Section 60I) and because "
            "resolving early saves everyone time and money. A lawyer who genuinely has your "
            "interests at heart will not discourage you from trying."
        ),
    ]

    schema = [
        org_schema(),
        breadcrumb_schema([
            ("Home", ""),
            (city + " Family Lawyers", slug),
        ]),
        localservice_schema(city, state, slug),
        faq_schema(qa),
    ]

    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += "<main id=\"main\">\n"
    doc += crumb_html([("Home", ""), (ec + " Family Lawyers", None)])

    # Hero section
    doc += (
        "<section class=\"phero\">\n"
        "  <div class=\"phero-blob\"></div>\n"
        "  <div class=\"wrap\">\n"
        "    <span class=\"eyebrow\"><span class=\"pulse\"></span>Serving "
        + ec + " &amp; " + es + " · Nationally accredited</span>\n"
        "    <h1>" + h1 + "</h1>\n"
        "    <p class=\"lede\">If you’ve searched for a family lawyer in "
        + ec + ", you’re not alone — it’s the instinctive first search "
        "at separation. But most people at this stage have more options than they realise. "
        "Our nationally accredited mediators help " + ec + " clients resolve parenting, "
        "property and financial matters without court — faster, more privately, and "
        "at a fraction of the cost.</p>\n"
        "    <div class=\"phero-cta\">\n"
        "      <a href=\"" + BOOK_URL + "\" class=\"btn btn-primary\">"
        "Book a Free Consultation <span class=\"arr\">→</span></a>\n"
        "      <a href=\"" + PHONE_HREF + "\" class=\"btn btn-ghost\">Call " + PHONE + "</a>\n"
        "    </div>\n"
        "  </div>\n"
        "</section>\n"
    )

    # Answer box
    doc += (
        "<div class=\"wrap-narrow\">"
        "<div class=\"answer reveal\"><p>" + answer_box + "</p></div>"
        "</div>\n"
    )

    # Article body
    doc += "<article class=\"body\"><div class=\"wrap-narrow reveal\">\n"

    # Section 1
    doc += (
        "<h2>What most people searching for family lawyers in "
        + ec + " actually need</h2>\n"
        "<p>" + elc + "</p>\n"
        "<p>When a relationship ends, “family lawyer” is almost everyone’s "
        "first search. It makes sense — it’s the phrase we all know, and the "
        "instinct to protect yourself is natural. But “family lawyer” conflates "
        "two very different things: legal advice (which you may well need at some point) and "
        "litigation (which most people can avoid entirely).</p>\n"
        "<p>In Australia, the law actually <em>requires</em> most separating couples to "
        "attempt family dispute resolution — mediation — before they can apply "
        "to court for parenting orders. That requirement exists because parliament recognised "
        "what research has long shown: the great majority of family matters can and should "
        "be resolved without a judge. Our mediators (many of whom have family law backgrounds) "
        "help " + ec + " clients reach legally sound, durable agreements — without "
        "anyone needing to step into a courtroom.</p>\n"
    )

    # City-specific section (Tier 1 top 5 only)
    if city_specific:
        doc += city_specific + "\n"

    # Section 2
    doc += (
        "<h2>When you genuinely need a family lawyer</h2>\n"
        "<p>We want to be honest about this, because it matters. There are situations where "
        "a family lawyer is not just helpful but necessary:</p>\n"
        "<ul>\n"
        "  <li><strong>Family violence or safety concerns.</strong> If there is a history "
        "of family violence, coercion or significant power imbalance, mediation may not be "
        "appropriate. A family lawyer can advise on protective orders and your legal rights.</li>\n"
        "  <li><strong>Complex asset structures.</strong> Trusts, business interests, "
        "overseas assets, or substantial superannuation may require specialist legal and "
        "financial advice that goes beyond what a mediator provides.</li>\n"
        "  <li><strong>One party refuses to engage.</strong> Mediation requires both "
        "parties’ willingness to participate. If the other party flatly refuses, "
        "a Section 60I certificate from a mediator enables you to proceed to court.</li>\n"
        "  <li><strong>Enforcement of existing orders.</strong> If court orders have already "
        "been made and are being breached, you need a lawyer, not a mediator.</li>\n"
        "  <li><strong>Urgency or risk of asset dissipation.</strong> If you believe assets "
        "are being hidden or dissipated, urgent legal intervention may be necessary.</li>\n"
        "</ul>\n"
        "<p>In all these cases, we’ll tell you directly — and where appropriate, "
        "refer you to a family lawyer. Our role is resolution, not revenue.</p>\n"
    )

    # Section 3
    doc += (
        "<h2>When mediation resolves your " + ec + " matter without one</h2>\n"
        "<p>For the remaining majority — which our experience suggests is around 90% "
        "of the people who contact us — mediation is not just an option but the "
        "better path. It works particularly well for:</p>\n"
        "<ul>\n"
        "  <li><strong>Parenting arrangements.</strong> Where to live, school decisions, "
        "holiday arrangements, communication — a child-focused mediation produces "
        "arrangements that both parents have agreed to and are therefore far more likely "
        "to honour.</li>\n"
        "  <li><strong>Property division.</strong> The family home, investment properties, "
        "superannuation, business assets and debts can all be addressed in a structured "
        "mediation session, without litigation.</li>\n"
        "  <li><strong>De facto separation.</strong> De facto couples have the same legal "
        "rights and obligations as married couples under Australian family law, and the "
        "same mediation pathway is available.</li>\n"
        "  <li><strong>Financial and spousal maintenance matters.</strong> Ongoing financial "
        "support arrangements can be negotiated and formalised through mediation.</li>\n"
        "  <li><strong>Consent orders.</strong> Once an agreement is reached in mediation, "
        "we can help you formalise it as <a href=\"/consent-orders/\">consent orders</a> "
        "or a <a href=\"/financial-agreements-mediation/\">binding financial agreement</a> "
        "— giving it the same legal weight as a court order.</li>\n"
        "</ul>\n"
    )

    # Section 4
    doc += (
        "<h2>The cost comparison: mediation vs litigation in " + ec + "</h2>\n"
        "<p>The financial difference between the two paths is substantial — and often "
        "decisive for " + ec + " clients who look at the numbers clearly:</p>\n"
        "<ul>\n"
        "  <li><strong>Mediation:</strong> Free initial consultation. Total mediation "
        "costs typically $2,000–$8,000, shared between both parties. Most matters "
        "resolve in one to two sessions. Formalising the agreement as consent orders "
        "adds a modest additional cost.</li>\n"
        "  <li><strong>Family law litigation:</strong> $300–$600 per hour for a "
        "solicitor, plus barrister fees for hearings. A contested matter — property "
        "or parenting — commonly costs each party $15,000–$150,000 or more. "
        "Court filing fees are additional. Legal costs are almost never recovered from "
        "the other side in family law.</li>\n"
        "  <li><strong>Time:</strong> Most " + ec + " mediations resolve in 1 day. "
        "A contested matter through " + ecr + " can take one to three years to reach "
        "a final hearing, during which time legal costs accumulate and uncertainty "
        "affects every decision you make.</li>\n"
        "  <li><strong>What’s at stake:</strong> In many " + ec + " separations, "
        "legal costs in litigation consume a meaningful share of the very assets "
        "being disputed. Mediation preserves more of those assets for both parties.</li>\n"
        "</ul>\n"
    )

    # Section 5
    doc += (
        "<h2>How " + ec + " mediation works</h2>\n"
        "<p>The process is designed to be clear, calm and free of jargon. Here is what "
        "to expect:</p>\n"
        "<ol>\n"
        "  <li><strong>Free consultation.</strong> We speak with you (and separately with "
        "the other party, where appropriate) to understand the situation and confirm "
        "that mediation is suitable.</li>\n"
        "  <li><strong>Intake.</strong> Each party completes a brief intake process. "
        "We review the key issues and prepare a structured agenda for the session.</li>\n"
        "  <li><strong>Mediation session.</strong> A nationally accredited mediator "
        "facilitates a structured conversation. Sessions can be conducted in the same "
        "room, in separate rooms (“shuttle mediation”), or online — "
        "whatever works best for your situation.</li>\n"
        "  <li><strong>Agreement.</strong> Where the parties reach agreement, it is "
        "documented in a Heads of Agreement during or shortly after the session.</li>\n"
        "  <li><strong>Formalisation.</strong> We help you convert your agreement into "
        "consent orders or a binding financial agreement, giving it legal force. "
        "If parenting orders are needed, we can issue a Section 60I certificate "
        "enabling either party to apply to court if required.</li>\n"
        "</ol>\n"
        "<p>Most " + ec + " matters complete steps one to four within two to four weeks. "
        "Formalisation takes a few more weeks. That’s measured in weeks, not years. "
        "You can <a href=\"/how-mediation-works/\">read our full guide to how mediation "
        "works</a> for more detail.</p>\n"
    )

    # Section 6
    doc += (
        "<h2>Working with your lawyer in mediation</h2>\n"
        "<p>Mediation and legal advice are not mutually exclusive — in fact, the two "
        "work well together. Many of our " + ec + " clients come to us after getting "
        "initial legal advice from a family lawyer. Others obtain advice during or after "
        "the mediation process to ensure any agreement is fair and legally sound. "
        "Some bring their lawyer as a support person to the session itself.</p>\n"
        "<p>A good family lawyer will often actively encourage mediation — partly "
        "because the law requires it for parenting matters, and partly because resolving "
        "early saves their client time, money and distress. We work alongside family "
        "lawyers regularly, and many of our referrals come from the legal profession.</p>\n"
        "<p>If you already have a lawyer, speak to them about mediation. If they are "
        "pushing you toward immediate litigation without first exploring resolution, "
        "it is worth seeking a second opinion.</p>\n"
    )

    # Section 7
    doc += (
        "<h2>Why " + ec + " clients choose Mediations Australia</h2>\n"
        "<ul>\n"
        "  <li><strong>AMDRAS accredited.</strong> Our mediators are accredited under "
        "the Australian Mediator and Dispute Resolution Accreditation Standards — "
        "the national benchmark for mediation quality.</li>\n"
        "  <li><strong>Family law backgrounds.</strong> Many of our mediators are also "
        "experienced family lawyers, so the legal realities of your matter are understood "
        "from the first conversation.</li>\n"
        "  <li><strong>90% resolution rate.</strong> Nine in ten matters we mediate resolve "
        "without proceeding to court — a track record built across thousands of "
        "Australian family disputes.</li>\n"
        "  <li><strong>Free initial consultation.</strong> No billing surprises. You know "
        "what the initial consultation costs before you commit to anything.</li>\n"
        "  <li><strong>In person or online.</strong> We serve " + ec + " clients in "
        "person (by arrangement) and through secure online mediation — same process, "
        "same mediators, same binding outcomes, wherever you are in " + es + ".</li>\n"
        "  <li><strong>We work alongside your lawyer.</strong> If you have a family "
        "lawyer, we work with them, not against them. Many of our clients are referred "
        "by the lawyers advising them.</li>\n"
        "</ul>\n"
        "<p><a href=\"/about-mediations-australia/\">Learn more about Mediations Australia "
        "→</a></p>\n"
    )

    doc += "</div></article>\n"

    # Service cards
    cards = "".join(
        "<article class=\"card\"><h3>" + esc(n) + "</h3><p>" + esc(d) + "</p>"
        "<a class=\"more\" href=\"/" + s + "/\">Learn more <span class=\"arr\">→</span></a></article>"
        for s, n, d in SERVICES[:6]
    )
    doc += (
        "<section class=\"sec\" style=\"padding-top:0\"><div class=\"wrap\">\n"
        "<div class=\"reveal\"><p class=\"sec-tag\">Family mediation services in "
        + ec + "</p>\n"
        "<h2 class=\"sec-title\">Resolve it without court, <em>starting today</em>.</h2></div>\n"
        "<div class=\"cards reveal\" style=\"margin-top:46px\">" + cards + "</div>"
        "</div></section>\n"
    )

    doc += faq_html(qa, heading=city + " family lawyers — common questions")
    doc += cta_band(
        "Talk to an accredited mediator in " + ec + " today.",
        "Book a free initial consultation and find out whether mediation can resolve your "
        "matter — before you commit to a family lawyer and a litigation path. "
        "In person or online, same nationally accredited mediators."
    )
    doc += "</main>" + page_end()

    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)

    text = re.sub(r"<[^>]+>", " ", doc)
    return slug, len(text.split())


# ---------------------------------------------------------------------------
# Tier 2 builder (~800 words)
# ---------------------------------------------------------------------------

def build_tier2(slug, city, state, nearest_office, court_ref, local_context):
    ec = esc(city)
    es = esc(state)
    ecr = esc(court_ref)
    elc = esc(local_context)

    title = city + " Family Lawyers | Mediation First — Mediations Australia"
    desc = (
        "Searching for family lawyers in " + city + "? Our nationally accredited "
        "mediators resolve 90% of family matters without court. Faster, cheaper, "
        "more private. Call " + PHONE + "."
    )

    h1 = ec + " Family Lawyers"

    answer_box = (
        "Most people searching for family lawyers in " + ec + " are at an early research "
        "stage — weighing up their options, not yet committed to litigation. For the "
        "vast majority, the right first step is mediation, not engaging a lawyer. Mediation "
        "resolves 90% of family disputes in one to two sessions, costs a fraction of court, "
        "and keeps the decision in your hands. Our nationally accredited mediators (many with "
        "family law backgrounds) help " + ec + " clients resolve parenting, property and "
        "financial matters without court — and work alongside your lawyer where you "
        "have one."
    )

    qa = [
        (
            "Do I need a family lawyer in " + city + " to separate?",
            "No. Separation requires no formal legal process. For the practical matters "
            "that follow — parenting and property — most " + ec + " couples "
            "resolve these through mediation without either party engaging a solicitor. "
            "Independent legal advice is worth getting at some stage, but you don’t "
            "need a family lawyer to begin."
        ),
        (
            "What does a family lawyer in " + city + " cost?",
            "Family lawyers in " + ec + " typically charge $300–$600 per hour. "
            "A contested matter through " + ecr + " commonly costs each party "
            "$15,000–$150,000 or more. Mediation typically costs $2,000–$8,000 "
            "total, shared between both parties."
        ),
        (
            "Can I use a mediator instead of a family lawyer in " + city + "?",
            "For the majority of " + ec + " family matters, yes — and it’s "
            "usually faster, cheaper and less stressful. Mediation resolves parenting "
            "arrangements, property and financial matters without court. Where you want "
            "legal advice, a lawyer can work alongside your mediator."
        ),
        (
            "How long does mediation take compared to family court in " + city + "?",
            "Most mediations resolve in a single day. A contested "
            "matter through " + ecr + " can take one to three years. The time difference "
            "is one of the most compelling reasons to try mediation first."
        ),
        (
            "What if my ex has already engaged a family lawyer?",
            "It is still worth raising mediation. Many family lawyers actively encourage "
            "clients to attempt resolution before court — it is legally required "
            "for parenting matters, and it saves everyone time and money. We are happy "
            "to work with both parties and their lawyers."
        ),
    ]

    schema = [
        org_schema(),
        breadcrumb_schema([
            ("Home", ""),
            (city + " Family Lawyers", slug),
        ]),
        localservice_schema(city, state, slug),
        faq_schema(qa),
    ]

    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += "<main id=\"main\">\n"
    doc += crumb_html([("Home", ""), (ec + " Family Lawyers", None)])

    # Hero
    doc += (
        "<section class=\"phero\">\n"
        "  <div class=\"phero-blob\"></div>\n"
        "  <div class=\"wrap\">\n"
        "    <span class=\"eyebrow\"><span class=\"pulse\"></span>Serving "
        + ec + " &amp; " + es + " · Nationally accredited</span>\n"
        "    <h1>" + h1 + "</h1>\n"
        "    <p class=\"lede\">If you’ve searched for a family lawyer in "
        + ec + ", the honest truth is that most people at this stage need a mediator "
        "before they need a lawyer. Our nationally accredited mediators resolve "
        "90% of " + ec + " family matters without court — faster, more privately, "
        "and at a fraction of the cost of litigation.</p>\n"
        "    <div class=\"phero-cta\">\n"
        "      <a href=\"" + BOOK_URL + "\" class=\"btn btn-primary\">"
        "Book a Free Consultation <span class=\"arr\">→</span></a>\n"
        "      <a href=\"" + PHONE_HREF + "\" class=\"btn btn-ghost\">Call " + PHONE + "</a>\n"
        "    </div>\n"
        "  </div>\n"
        "</section>\n"
    )

    # Answer box
    doc += (
        "<div class=\"wrap-narrow\">"
        "<div class=\"answer reveal\"><p>" + answer_box + "</p></div>"
        "</div>\n"
    )

    # Article body
    doc += "<article class=\"body\"><div class=\"wrap-narrow reveal\">\n"

    # Section 1
    doc += (
        "<h2>What most people searching for family lawyers in "
        + ec + " actually need</h2>\n"
        "<p>" + elc + "</p>\n"
        "<p>In Australia, the law requires most separating couples to attempt family dispute "
        "resolution — mediation — before applying to court for parenting orders. "
        "That requirement exists because the great majority of family matters can be resolved "
        "without litigation. Our mediators (many of whom have family law backgrounds) help "
        + ec + " clients reach legally sound, durable agreements without court. For the "
        "situations where a family lawyer is genuinely necessary — family violence, "
        "complex assets, a party who refuses to engage — we will tell you honestly "
        "and refer you on.</p>\n"
    )

    # Section 2
    doc += (
        "<h2>Mediation vs engaging a family lawyer in "
        + ec + ": the honest comparison</h2>\n"
        "<ul>\n"
        "  <li><strong>Cost.</strong> Mediation typically costs $3,000–$4,500 total, "
        "shared between the parties. Family law litigation commonly costs each party $15,000–$150,000 "
        "or more. Legal costs in family law are almost never recovered from the other side.</li>\n"
        "  <li><strong>Time.</strong> Most " + ec + " mediations resolve in weeks. A "
        "contested matter through " + ecr + " can take one to three years.</li>\n"
        "  <li><strong>Control.</strong> In mediation, you design the outcome. In court, "
        "a judge who has known your situation for hours decides matters you’ve lived "
        "for years.</li>\n"
        "  <li><strong>Privacy.</strong> Mediation is confidential and conducted on a "
        "“without prejudice” basis. Court proceedings are public record.</li>\n"
        "  <li><strong>Co-parenting.</strong> Litigation is adversarial. Mediation is "
        "collaborative — which matters when you will continue to co-parent or move "
        "in the same community.</li>\n"
        "</ul>\n"
    )

    # Section 3
    doc += (
        "<h2>How mediation works in " + ec + "</h2>\n"
        "<p>The process is straightforward. We begin with a free consultation to understand "
        "your situation. One of our own accredited mediators works with you from there. The session itself "
        "can be conducted in person, in separate rooms, or online — whatever suits "
        "your circumstances. Where agreement is reached, we document it and help you "
        "formalise it as <a href=\"/consent-orders/\">consent orders</a> or a "
        "<a href=\"/financial-agreements-mediation/\">binding financial agreement</a>, "
        "giving it the same legal weight as a court order. Most " + ec + " matters complete "
        "this entire process within a few weeks. "
        "<a href=\"/how-mediation-works/\">See our full step-by-step guide →</a></p>\n"
    )

    # Section 4
    doc += (
        "<h2>Why " + ec + " clients choose Mediations Australia</h2>\n"
        "<p>Our mediators are accredited under AMDRAS, and many are also experienced family "
        "lawyers — so the legal realities of your matter are understood from the first "
        "conversation. We have a 90% resolution rate across thousands of Australian family "
        "disputes. We offer free initial consultations (no billing surprises), and we serve "
        + ec + " clients both in person (by arrangement) and through secure online mediation "
        "across " + es + ". We work alongside your existing lawyer where you have one, "
        "and many of our clients are referred to us by the very solicitors advising them. "
        "<a href=\"/about-mediations-australia/\">Learn more about Mediations Australia "
        "→</a></p>\n"
        "<p>You can also check <a href=\"/how-much-does-mediation-cost/\">what mediation "
        "costs</a> before you commit to anything, and explore our "
        "<a href=\"/online-divorce/\">secure online mediation service</a> if you’d "
        "prefer to resolve your matter from home.</p>\n"
    )

    doc += "</div></article>\n"

    # Service cards
    cards = "".join(
        "<article class=\"card\"><h3>" + esc(n) + "</h3><p>" + esc(d) + "</p>"
        "<a class=\"more\" href=\"/" + s + "/\">Learn more <span class=\"arr\">→</span></a></article>"
        for s, n, d in SERVICES[:6]
    )
    doc += (
        "<section class=\"sec\" style=\"padding-top:0\"><div class=\"wrap\">\n"
        "<div class=\"reveal\"><p class=\"sec-tag\">Family mediation services in "
        + ec + "</p>\n"
        "<h2 class=\"sec-title\">Resolve it without court, <em>starting today</em>.</h2></div>\n"
        "<div class=\"cards reveal\" style=\"margin-top:46px\">" + cards + "</div>"
        "</div></section>\n"
    )

    doc += faq_html(qa, heading=city + " family lawyers — common questions")
    doc += cta_band(
        "Talk to a " + ec + " mediator before you engage a family lawyer.",
        "Book a free initial consultation and understand your options. Nine in ten matters "
        "we mediate resolve without court — in weeks, not years."
    )
    doc += "</main>" + page_end()

    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)

    text = re.sub(r"<[^>]+>", " ", doc)
    return slug, len(text.split())


# ---------------------------------------------------------------------------
# Build all pages
# ---------------------------------------------------------------------------

results = []
for row in TIER1:
    results.append(("T1", build_tier1(*row)))
for row in TIER2:
    results.append(("T2", build_tier2(*row)))

print("Family lawyers pages built:")
for tier, (slug, words) in results:
    print("  [" + tier + "] " + slug + ": ~" + str(words) + " words")
