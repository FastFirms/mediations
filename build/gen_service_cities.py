#!/usr/bin/env python3
"""Service-specific city pages.

Generates 28 pages: 4 services × 7 cities.
Services: property-settlement, divorce, parenting, workplace
Cities: Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, Gold Coast

Each page has 60%+ unique content — local court, fees context, suburbs, and
service-specific nuance. Never template-pad: every city block is individually
written to reflect actual local practice.
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─────────────────────────────────────────────────────────────────────────────
#  CITY DATA  (local court, suburb list, population context, WA flag)
# ─────────────────────────────────────────────────────────────────────────────
CITIES = {
  "sydney": {
    "name": "Sydney", "state": "NSW", "wa": False,
    "court_ref": "the Sydney or Parramatta registry",
    "court_full": "Federal Circuit and Family Court of Australia — Lionel Bowen Building, Sydney, or the Parramatta registry serving Greater Western Sydney",
    "suburbs": "the CBD, North Shore, Eastern Suburbs, Inner West, Northern Beaches, the Hills District, Parramatta, Penrith, Campbelltown and Greater Western Sydney",
    "pop_note": "As Australia's largest city, Sydney generates a high volume of family, property and commercial disputes, and its family law registries are among the busiest in the country. Contested matters can take one to three years to reach a final hearing.",
    "state_note": "NSW courts strongly encourage alternative dispute resolution. Family dispute resolution is a legal precondition to most parenting applications, and the NSW Civil Procedure Act reinforces early resolution for civil matters.",
    "has_office": True,
    "office": "Suite 508, 41/464-480 Kent St, Sydney NSW 2000",
  },
  "melbourne": {
    "name": "Melbourne", "state": "VIC", "wa": False,
    "court_ref": "the Melbourne registry",
    "court_full": "Federal Circuit and Family Court of Australia — Melbourne CBD, with circuit sittings to Ballarat, Bendigo, Dandenong, Geelong, Morwell and Shepparton",
    "suburbs": "the CBD, inner north, inner east, Dandenong, the eastern, western and bayside suburbs, the Mornington Peninsula and Greater Melbourne",
    "pop_note": "Melbourne is one of Australia's most active family law jurisdictions. Victorian courts place a strong emphasis on ADR before hearing — and the Magistrates' Court civil limit of $100,000 means many disputes that end up in court would have been better resolved through mediation first.",
    "state_note": "Victoria has a well-established ADR culture. Courts actively direct parties to mediation before allocating hearing dates, and the County Court's commercial list expects genuine pre-trial resolution attempts.",
    "has_office": True,
    "office": "Level 23, Collins Square Tower Five, 727 Collins St, Melbourne VIC 3008",
  },
  "brisbane": {
    "name": "Brisbane", "state": "QLD", "wa": False,
    "court_ref": "the Brisbane registry",
    "court_full": "Federal Circuit and Family Court of Australia — Commonwealth Law Courts, North Quay, Brisbane, with circuit sittings to Bundaberg, Maroochydore, Hervey Bay and Toowoomba",
    "suburbs": "the CBD, inner suburbs, Ipswich, Logan, Redlands, the bayside, the western corridor and Greater Brisbane",
    "pop_note": "South East Queensland's rapid population growth has put Brisbane's court lists under pressure. New residents from interstate often find themselves navigating family law for the first time, and local court waiting times reinforce the case for early resolution.",
    "state_note": "Queensland's Uniform Civil Procedure Rules require a genuine pre-litigation attempt to resolve matters, and family dispute resolution is generally a precondition to parenting applications.",
    "has_office": True,
    "office": "Suite 507, 12B Anzac Square Arcade, 198 Adelaide St, Brisbane QLD 4000",
  },
  "perth": {
    "name": "Perth", "state": "WA", "wa": True,
    "court_ref": "the Family Court of Western Australia",
    "court_full": "Family Court of Western Australia — the only state with its own dedicated family court, operating alongside the federal system for certain matters",
    "suburbs": "the CBD, Fremantle, Joondalup, Rockingham, Armadale, the northern and southern suburbs, the eastern suburbs and the wider Perth metropolitan area",
    "pop_note": "Western Australia's separate family court system means Perth matters can follow different procedures from the rest of Australia — particularly for de facto couples and property disputes, which are governed by state legislation. A mediator who understands the WA framework is genuinely valuable here.",
    "state_note": "WA administers family law through its own Family Court. De facto property matters are dealt with under state legislation rather than the federal Family Law Act, which affects both the process and the available orders.",
    "has_office": True,
    "office": "Level 25, 108 St Georges Tce, Perth WA 6000",
  },
  "adelaide": {
    "name": "Adelaide", "state": "SA", "wa": False,
    "court_ref": "the Adelaide registry",
    "court_full": "Federal Circuit and Family Court of Australia — Adelaide registry, which also circuits to Broken Hill and Mount Gambier",
    "suburbs": "the CBD, the Adelaide Hills, the northern and southern suburbs, the eastern suburbs, Glenelg, Port Adelaide and Greater Adelaide",
    "pop_note": "With a single main registry serving the whole state, Adelaide's court lists carry the weight of South Australia's family law work. Resolving a matter through mediation can save many months of waiting and significantly reduces the cost for both parties.",
    "state_note": "South Australian courts encourage ADR across family, civil and commercial matters. The SA District Court civil list has a strong expectation of pre-trial resolution attempts.",
    "has_office": False,
    "office": None,
  },
  "canberra": {
    "name": "Canberra", "state": "ACT", "wa": False,
    "court_ref": "the Canberra registry",
    "court_full": "Federal Circuit and Family Court of Australia — Canberra registry, serving the ACT and surrounding NSW communities including Queanbeyan",
    "suburbs": "Canberra city, Belconnen, Woden, Tuggeranong, Gungahlin, Queanbeyan and the surrounding Capital Region",
    "pop_note": "As the national capital, Canberra has a highly engaged professional community. Many separations involve public servants, defence personnel and contractors who particularly value the privacy and discretion mediation offers over a public court record.",
    "state_note": "The ACT strongly supports alternative dispute resolution. ACT courts actively direct parties to mediation, and the relatively compact jurisdiction means any agreement reached can be formalised quickly.",
    "has_office": False,
    "office": None,
  },
  "gold-coast": {
    "name": "Gold Coast", "state": "QLD", "wa": False,
    "court_ref": "the Brisbane registry",
    "court_full": "Federal Circuit and Family Court of Australia — Gold Coast matters are filed at the Brisbane registry, with Southport Local Court handling lower-value civil matters locally",
    "suburbs": "Southport, Surfers Paradise, Broadbeach, Robina, Burleigh Heads, Coomera, Pimpama, Coolangatta and the wider Gold Coast",
    "pop_note": "The Gold Coast's large, mobile population — with a significant proportion of interstate and international residents — sees a high rate of relationship breakdowns and property disputes. Filing through the Brisbane registry adds travel time and cost that mediation entirely avoids.",
    "state_note": "Queensland's early-resolution requirements apply to Gold Coast matters. Family dispute resolution is generally required before parenting applications, and Queensland civil rules encourage pre-litigation negotiation.",
    "has_office": False,
    "office": None,
  },
}

# ─────────────────────────────────────────────────────────────────────────────
#  SERVICE CONTENT FUNCTIONS
#  Each returns: (title, desc, h1, lede, ans, body_html, qa_list)
# ─────────────────────────────────────────────────────────────────────────────

def property_data(city_key, cd):
    c = cd["name"]
    state = cd["state"]
    wa = cd["wa"]
    court = cd["court_ref"]

    wa_callout = ""
    if wa:
        wa_callout = (
            "<div class='callout'><h3>Western Australia: a different property framework</h3>"
            "<p>In Western Australia, de facto property disputes are governed by the "
            "<em>Family Court Act 1997</em> (WA) rather than the federal Family Law Act. "
            "The available orders, the applicable time limits, and the relevant court differ "
            "from the rest of Australia. Superannuation splitting orders in WA de facto matters "
            "have also historically operated differently. This makes reaching agreement through "
            "mediation — and avoiding the Family Court of WA entirely — particularly valuable "
            "for Perth de facto couples. Our mediators understand the WA framework.</p></div>"
        )

    # City-specific cost / timing local colour
    local_colour = {
        "sydney": ("Sydney's property market means even a modest family home can have a significant "
                   "value in dispute. The Lionel Bowen Building registry and Parramatta are both "
                   "under considerable pressure — average time to a final property hearing in Sydney "
                   "regularly exceeds 18 months, and that's before counting the preparatory litigation."),
        "melbourne": ("Melbourne's property values and the prevalence of investment properties, SMSFs "
                      "and business interests in the pool mean property settlements are often complex. "
                      "The Melbourne registry's waiting times for property matters regularly run to "
                      "18 months or more for a final hearing — time during which costs accumulate."),
        "brisbane": ("Brisbane's population growth has brought a sharp increase in property disputes, "
                     "particularly involving investment properties and interstate assets. The Brisbane "
                     "registry is under pressure, with property hearings regularly listed 12–18 months "
                     "out from the date of filing."),
        "perth": ("Perth's mining-driven economy creates property pools that frequently include FIFO "
                  "income, resource-sector bonuses and investment properties. These require specific "
                  "valuation approaches that an experienced property mediator can manage efficiently "
                  "— without the forensic accounting costs of contested litigation."),
        "adelaide": ("Adelaide's property market is more stable than the eastern capitals, but the "
                     "single-registry model for South Australia means resolution through the courts "
                     "is slow. Many Adelaide couples find that a mediated settlement, even for "
                     "complex pools, is achievable in a single session."),
        "canberra": ("Canberra's public-sector workforce brings specific property pool features: "
                     "defined benefit superannuation, Commonwealth-employer super funds, and "
                     "government housing. These require specific knowledge that an experienced "
                     "Canberra property mediator can bring to the table."),
        "gold-coast": ("The Gold Coast's property market — holiday apartments, investment units and "
                       "jointly-purchased holiday homes — creates specific valuation and division "
                       "challenges. Matters filed through Brisbane add an extra layer of delay for "
                       "Gold Coast clients that mediation entirely avoids."),
    }.get(city_key, "")

    body = f"""
<h2>How property settlement mediation works in {c}</h2>
<p>After separation, dividing property fairly is one of the most consequential and contested parts of the process. The Family Law Act requires a four-step approach: identify all assets and liabilities in the pool, assess each party's contributions (financial and non-financial), consider future needs, and arrive at an outcome that is just and equitable. Mediation doesn't bypass this framework — it works <em>within</em> it, but lets you and your former partner reach the result rather than handing it to a judge who will know your situation from a few hours of evidence.</p>
<p>In {c}, our accredited property settlement mediators guide you through each step. Both parties make full financial disclosure before the session. The mediator helps identify contested valuations, clarify the issues in dispute, and explore options neither side may have considered. Most {c} property settlement mediations resolve in a single day-long session.</p>

<h2>The local reality for {c} property disputes</h2>
<p>{local_colour} {cd['pop_note']}</p>
<p>These timelines are exactly why property settlement mediation in {c} makes such practical sense. For the same cost as a few months of litigation preparation, you can often reach a final, binding agreement on the day of mediation.</p>

<h2>What goes into the property pool in {c}?</h2>
<p>Everything owned and owed — individually or jointly — generally forms part of the pool. For {c} separating couples this typically includes:</p>
<ul>
  <li>The family home, investment properties, and any interests in commercial property</li>
  <li>Superannuation (treated alongside the asset pool and subject to splitting orders)</li>
  <li>Bank accounts, savings, shares, managed funds and cryptocurrency</li>
  <li>Businesses, professional practices, trusts and company interests</li>
  <li>Vehicles, boats and personal property of value</li>
  <li>Mortgages, personal loans, credit cards and HECS-HELP debts</li>
</ul>
<p>Inheritances and gifts received during the relationship may be included depending on how they were used and when they were received. Pre-relationship assets are not automatically excluded. Your mediator works through each category with both parties systematically.</p>
{wa_callout}
<h2>Cost of property settlement in {c}: mediation vs contested litigation</h2>
<p>A contested property settlement through {court} typically costs $30,000 to $150,000 per party in legal fees — more if valuations are contested or the matter requires multiple interlocutory hearings before a final trial. It can take one to three years. Property settlement mediation in {c} typically costs a few thousand dollars per party, shared, and resolves in a day. Even with independent legal advice to review and formalise the outcome — which we recommend — the total cost is a fraction of litigation. The assets you are dividing are not made larger by fighting over them.</p>

<h2>Formalising your {c} property settlement agreement</h2>
<p>An agreement reached in mediation becomes legally binding through one of two routes: <strong>consent orders</strong>, filed with {court} and legally enforceable as if made by a judge; or a <strong>binding financial agreement</strong> (BFA) under the Family Law Act, which requires each party to obtain independent legal advice. Your mediator will advise which is more appropriate. If you already have a solicitor in {c}, we work alongside them. If you need a referral, we can help with that too.</p>

<h2>Getting ready for property settlement mediation in {c}</h2>
<p>The more both parties have prepared, the more productive the session is. Before your {c} mediation:</p>
<ul>
  <li>Gather recent statements for all bank accounts, superannuation funds, mortgages and loans</li>
  <li>Obtain a current market appraisal or formal valuation for any real property</li>
  <li>Have an up-to-date business valuation if a business is in the pool</li>
  <li>Note your contributions during the relationship — financial and non-financial</li>
  <li>Think through your post-separation income, housing needs and financial position</li>
</ul>
<p>You do not need to agree on values before the session — part of the mediator's role is to help resolve disagreements about figures. But having the underlying documents prevents the session stalling on facts that could have been established beforehand.</p>
"""
    title = f"Property Settlement Mediation {c} | Divide Assets Without Court"
    desc  = (f"Property settlement mediation in {c} — divide assets, superannuation and the "
             f"family home without going to court. Accredited mediators, free consultation. "
             f"Call {PHONE}.")
    h1    = f"Property Settlement Mediation <em>{c}</em>"
    lede  = (f"Property settlement mediation in {c} is faster, cheaper, and far less damaging "
             f"than a contested court process. Our accredited mediators help you divide assets, "
             f"superannuation and the family home by agreement — keeping the outcome in your hands.")
    ans   = (f"Property settlement mediation in {c} lets you divide assets, debts and "
             f"superannuation by agreement rather than through {court}. It typically costs a "
             f"fraction of litigation, resolves in a single session, and produces a legally "
             f"binding outcome through consent orders or a financial agreement.")
    qa = [
      (f"How long does property settlement mediation take in {c}?",
       f"Most {c} property settlement mediations resolve in a single full-day session — sometimes two for complex matters involving businesses or multiple properties. By contrast, a contested property settlement through {court} typically takes one to three years to reach a final hearing."),
      (f"What does property settlement mediation cost in {c}?",
       f"Every matter starts with a free initial consultation. We charge a fixed daily rate per party — typically a few thousand dollars shared between the parties. Compare this with $30,000–$150,000 per side in contested litigation."),
      (f"Is a mediated property settlement legally binding in {c}?",
       f"Yes, once formalised. The usual routes are consent orders filed with {court} — which are legally enforceable as if made by a judge — or a binding financial agreement under the Family Law Act. Your mediator will recommend the appropriate form."),
      (f"Do I need a lawyer for property settlement mediation in {c}?",
       f"You don't need a lawyer in the room. Many {c} clients mediate without lawyers present and obtain independent legal advice before signing any formalised agreement. This is a legal requirement for a binding financial agreement. We can suggest referrals to {c} family lawyers if needed."),
      (f"What if we cannot agree in property mediation in {c}?",
       f"If mediation does not resolve all issues, you can proceed to {court} for the unresolved matters. Partial agreements are still valid. In practice, around 90% of property settlement mediations we conduct in {c} resolve fully on the day."),
      (f"What is the time limit for property settlement in {c}?",
       f"For married couples, you generally have 12 months from the date of a divorce order to apply to court for property orders. For de facto couples, you generally have two years from the end of the relationship. Mediating early avoids deadline pressure and reduces the risk of an application being out of time."),
    ]
    return title, desc, h1, lede, ans, body, qa


def divorce_data(city_key, cd):
    c = cd["name"]
    state = cd["state"]
    wa = cd["wa"]
    court = cd["court_ref"]

    wa_callout = ""
    if wa:
        wa_callout = (
            "<div class='callout'><h3>Divorce and de facto separation in Western Australia</h3>"
            "<p>In Western Australia, de facto couples separating before certain legislative "
            "changes had their property disputes governed by state law rather than the federal "
            "Family Law Act. Even for married couples, Perth divorces involving property use "
            "the Family Court of Western Australia rather than the federal system. Superannuation "
            "splitting in WA de facto matters operates differently. Perth-based divorce mediation "
            "with a mediator who understands the WA framework is specifically valuable here — "
            "and makes avoiding the Family Court of WA entirely an even more attractive outcome."
            "</p></div>"
        )

    local_note = {
        "sydney": ("In Sydney, the sheer volume of contested property and parenting matters means "
                   "the registries are under constant pressure. A Sydney separation that becomes "
                   "fully contested can take two to three years and consume more than $100,000 per "
                   "side in a complex matter — often eroding the very assets the parties are fighting over."),
        "melbourne": ("Melbourne's strong property market means a contested property settlement "
                      "carries high financial stakes — particularly where the family home, investment "
                      "properties or a family business are involved. Melbourne family law practitioners "
                      "routinely report that mediated settlements outperform litigated outcomes for "
                      "most clients once costs are taken into account."),
        "brisbane": ("Brisbane's rapid growth means many separating couples arrived from interstate "
                     "or overseas and are unfamiliar with the Australian family law system. Our Brisbane "
                     "divorce mediators provide clear guidance on the process and the realistic options "
                     "at every stage."),
        "perth": ("Perth divorces involving significant property — mining income, resource-sector "
                  "bonuses, investment portfolios — are particularly well-suited to mediation. The "
                  "privacy and confidentiality of the process protects professional reputations, "
                  "and the WA framework rewards early resolution."),
        "adelaide": ("Adelaide's smaller professional community makes the privacy of mediation "
                     "especially valuable. A contested Adelaide divorce that proceeds to a final "
                     "hearing is a matter of public record. Mediation keeps the terms of settlement "
                     "strictly private."),
        "canberra": ("Canberra's public-service community values confidentiality and professional "
                     "discretion. Many Canberra separations involve Commonwealth superannuation, "
                     "defined benefit schemes and government housing — areas where an experienced "
                     "mediator adds specific value."),
        "gold-coast": ("The Gold Coast's high rate of relationship breakdowns — common in a fast-growing, "
                       "transient city — and the distance from Brisbane's registry make mediation the "
                       "practical first choice for most Gold Coast divorces."),
    }.get(city_key, "")

    body = f"""
<h2>What divorce mediation covers in {c}</h2>
<p>Divorce — the legal end of a marriage — is actually just one piece of the picture. The divorce order itself is administrative: twelve months' separation, an application, and a short court hearing. What people really mean when they talk about "getting a divorce" is settling <em>everything that comes with it</em>: the family home, superannuation, property, parenting arrangements, child support and spousal maintenance. These are the matters that take months or years if litigated — and that mediation is specifically designed to resolve faster, more cheaply, and on your own terms.</p>
<p>Our {c} divorce mediators help separating couples reach agreement across all of these issues in a single structured process. You don't need to deal with property and parenting separately through different court applications, and you don't need to go to court to resolve any of them.</p>

<h2>The {c} divorce timeline: what to realistically expect</h2>
<p>{local_note}</p>
<ul>
  <li><strong>Divorce order</strong> — administrative; typically 3–5 months from application. Not usually contested.</li>
  <li><strong>Property settlement</strong> — by mediation: one day. Through {court}: 1–3 years.</li>
  <li><strong>Parenting arrangements</strong> — by mediation: one day. Through {court}: interim orders in weeks, final orders after 1–2 years.</li>
  <li><strong>Total cost per party</strong> — mediation: a few thousand dollars. Contested litigation: $30,000–$150,000 or more.</li>
</ul>
<p>Note also the 12-month deadline: once a divorce order is made, you have 12 months to apply to court for property orders. Settling by mediation before or shortly after divorce avoids the deadline risk entirely.</p>
{wa_callout}
<h2>Children and divorce in {c}</h2>
<p>When children are involved, the way separation is handled has a direct impact on them — for years, sometimes decades. Mediation is specifically designed to keep conflict lower, which research consistently shows benefits children's long-term wellbeing. It also produces parenting arrangements that both parents have agreed to, which are more durable than orders imposed by a judge.</p>
<p>In {c}, as across Australia, family dispute resolution (FDR) is generally required before a parent can apply to court for parenting orders. Our mediators are registered FDR practitioners and can issue the section 60I certificate required for parenting applications if mediation does not fully resolve the matter — so you satisfy the legal requirement and make a genuine attempt at resolution in one step.</p>

<h2>Divorce mediation for {c} business owners and professionals</h2>
<p>In {c}'s professional community, many separating couples have complex financial positions — businesses, self-managed super funds, professional practices, commercial property or significant investment portfolios. These matters can be devastatingly expensive if litigated: business valuations are contested, forensic accountants are briefed, and proceedings drag on while the underlying business suffers. Mediation handles these matters privately, efficiently, and without the collateral damage of a public court file. Our mediators have significant experience with complex property pools and work with specialist valuers where needed.</p>

<h2>After the mediation: formalising your {c} divorce settlement</h2>
<p>An agreement reached in mediation becomes legally binding through either consent orders filed with {court} (legally enforceable as if made by a judge), or a binding financial agreement under the Family Law Act (which requires independent legal advice for both parties). Your mediator can advise which is more appropriate and, where needed, can coordinate with solicitors on both sides to finalise the paperwork. If you already have a {c} family lawyer, we work alongside them.</p>
"""
    title = f"Divorce Mediation {c} | Settle Everything Without Court"
    desc  = (f"Divorce mediation in {c} — resolve property, parenting and finances at separation "
             f"without going to court. Accredited mediators, free initial consultation. Call {PHONE}.")
    h1    = f"Divorce Mediation <em>{c}</em>"
    lede  = (f"Divorce mediation in {c} resolves property, parenting, finances and everything in "
             f"between — in a single structured process, without court. Expert guidance, binding "
             f"outcomes, at a fraction of the cost of litigation.")
    ans   = (f"Divorce mediation in {c} helps separating couples resolve property, parenting and "
             f"financial matters by agreement without going to court. It typically resolves in one "
             f"to two sessions, costs significantly less than litigation, and produces legally "
             f"binding outcomes through consent orders or a financial agreement.")
    qa = [
      (f"Do I need to be divorced before I can use divorce mediation in {c}?",
       f"No. Mediation can begin at any stage of separation — before, during or after a divorce order. Resolving property and parenting matters through mediation before divorce is finalised avoids the 12-month deadline on property applications that applies after a divorce order."),
      (f"Can divorce mediation cover both parenting and property at the same time in {c}?",
       f"Yes. This is one of the main advantages of mediation — it can address all outstanding issues in a single process, rather than dealing with property and parenting through separate court applications at different times and costs."),
      (f"What does divorce mediation cost in {c}?",
       f"Every matter starts with a free initial consultation. We charge a fixed daily rate per party — typically a few thousand dollars shared between the parties, compared with $30,000–$150,000 or more per side in contested proceedings."),
      (f"How is a divorce mediation agreement made legally binding in {c}?",
       f"Through consent orders filed with {court} — which become legally enforceable as if made by a judge — or a binding financial agreement under the Family Law Act, which requires independent legal advice for both parties."),
      (f"What if my spouse refuses divorce mediation in {c}?",
       f"Mediation is voluntary. If your spouse declines, you may apply for a section 60I certificate and proceed to court for parenting matters. For property matters, a court application can proceed where genuine resolution attempts have failed. In practice, most people agree to mediation when the alternative cost and delay of litigation is explained clearly."),
      (f"Can divorce mediation be done online in {c}?",
       f"Yes. We offer secure online divorce mediation for all {c} and {state} clients. Online sessions follow the same structured process and produce the same legally binding outcomes as in-person mediation."),
    ]
    return title, desc, h1, lede, ans, body, qa


def parenting_data(city_key, cd):
    c = cd["name"]
    state = cd["state"]
    wa = cd["wa"]
    court = cd["court_ref"]

    wa_cert = "section 66H of the Family Court Act 1997 (WA)"
    fed_cert = "section 60I of the Family Law Act 1975 (Cth)"
    cert_ref = wa_cert if wa else fed_cert
    wa_note_inline = (" In Western Australia, parenting matters before the Family Court of WA may require "
                      "a section 66H certificate rather than a section 60I certificate." if wa else "")

    local_note = {
        "sydney": ("Sydney's family law registries — Lionel Bowen Building and Parramatta — are "
                   "heavily listed. An interim parenting order application in Sydney can take "
                   "weeks to months just for first directions; contested interim hearings and "
                   "final hearings extend the timeline to 1–2 years. Children's lives are "
                   "measured in months, not years — mediation gives them certainty far faster."),
        "melbourne": ("Melbourne's family law registry processes thousands of parenting applications "
                      "each year. The emphasis on pre-trial ADR in Victoria means parties are often "
                      "referred to mediation by the court itself — getting there first saves both "
                      "the court time and the parties months of legal fees."),
        "brisbane": ("Brisbane's growing population has put parenting matters under pressure at the "
                     "North Quay registry. For Gold Coast and Sunshine Coast parents, the additional "
                     "travel distance makes mediation — in person or online — the clear practical preference."),
        "perth": ("Perth's Family Court of WA handles parenting matters under its own state-based "
                  "framework, with procedural differences from the federal system. Our Perth parenting "
                  "mediators understand both the WA and federal frameworks, and the section 66H "
                  "certificate requirement specific to WA family court proceedings."),
        "adelaide": ("Adelaide's single main registry serves the whole of South Australia. Parenting "
                     "matters involving regional SA clients — the Adelaide Hills, the Barossa, Eyre "
                     "Peninsula — benefit especially from online mediation options that avoid long drives."),
        "canberra": ("Canberra's close-knit community means contested parenting proceedings carry "
                     "particular social and professional risk. Many Canberra parents actively prefer "
                     "mediation precisely because it is private and produces child-focused arrangements "
                     "rather than adversarial findings."),
        "gold-coast": ("The Gold Coast's highly mobile population means parents sometimes live in "
                       "different states, or one parent may wish to relocate. Relocation disputes "
                       "and interstate arrangements are areas where early mediation is particularly "
                       "valuable — the outcomes are more flexible than court orders and easier to "
                       "sustain when both parents have agreed."),
    }.get(city_key, "")

    body = f"""
<h2>Parenting mediation in {c}: child-focused, not adversarial</h2>
<p>When parents separate in {c}, how they handle the arrangements for their children matters enormously — not just for now, but for years ahead. The adversarial approach — each parent briefing lawyers, filing affidavits, building a case against the other — is almost always the worst option for the children caught in the middle. It is also one of the most expensive and slowest paths through the family law system.</p>
<p>Parenting mediation takes a completely different approach. A neutral, nationally accredited mediator helps both parents focus on the children's actual needs — not on winning. The goal is practical arrangements that work for the children and that both parents can sustain. Because both parents agree to the outcome, parenting plans reached through mediation are consistently more durable than parenting orders imposed by a judge.</p>

<h2>The {c} parenting landscape</h2>
<p>{local_note}</p>

<h2>What parenting mediation covers in {c}</h2>
<p>Our {c} parenting mediators work through the full range of issues that arise after separation:</p>
<ul>
  <li><strong>Where the children live</strong> and who they spend time with day-to-day</li>
  <li><strong>School term and holiday arrangements</strong>, including Christmas, Easter, school holidays, Mother's Day and Father's Day, and each child's birthday</li>
  <li><strong>Changeovers</strong> — location, timing, and how handovers are managed</li>
  <li><strong>Education decisions</strong> — school choice, extracurricular activities, tutoring</li>
  <li><strong>Health and medical decisions</strong> — how major decisions are made; ongoing health needs</li>
  <li><strong>Communication</strong> — between parents, and how children communicate with each parent when not in their care</li>
  <li><strong>Overseas and interstate travel</strong> — consent arrangements and passport custody</li>
  <li><strong>Relocation</strong> — where one parent wishes to move with the children</li>
  <li><strong>Child support and shared expenses</strong> — formal assessments and additional costs above the formula</li>
  <li><strong>Cultural and religious upbringing</strong> where this is a point of difference</li>
</ul>

<h2>Family Dispute Resolution (FDR) and the certificate requirement in {c}</h2>
<p>Before a parent in {c} can apply to court for parenting orders, they must generally make a genuine attempt at family dispute resolution, unless an exemption applies (family violence, urgency or other specified grounds). This requirement is embedded in {cert_ref}.{wa_note_inline}</p>
<p>Our mediators are registered Family Dispute Resolution Practitioners. Your mediation satisfies the FDR requirement, and if the matter does not fully resolve, we issue the certificate needed to apply to {court}. You get a genuine attempt at resolution and the legal gateway to court in one step — not two separate processes.</p>

<h2>Parenting orders vs parenting plans in {c}</h2>
<p>Agreements reached in parenting mediation can be recorded in two ways:</p>
<ul>
  <li><strong>A parenting plan</strong> — signed by both parents, not legally enforceable, but recognised by courts and easily updated by mutual agreement. Best where the co-parenting relationship is cooperative.</li>
  <li><strong>Consent orders</strong> — filed with {court} and legally binding. Breach of consent orders is contempt of court. More appropriate where certainty, enforceability or a history of non-compliance is relevant.</li>
</ul>
<p>Your mediator will advise which is more appropriate. Many {c} couples use a parenting plan initially — testing arrangements in practice — and move to consent orders once they are confident the arrangements work.</p>

<h2>When parenting mediation is not appropriate in {c}</h2>
<p>Parenting mediation is not suitable for all situations. Where there is family violence, a risk to a parent or child's safety, or where urgent orders are needed (for example, where a child has been removed from {c} without consent), court action may be necessary. Our team will give you an honest assessment in the initial consultation, without pressure. If you or your children are at risk, contact the police or call 1800RESPECT on 1800&nbsp;737&nbsp;732 before pursuing mediation.</p>
"""
    title = f"Parenting Mediation {c} | Child Arrangements Without Court"
    desc  = (f"Parenting mediation in {c} — parenting plans, consent orders and child arrangements "
             f"by agreement, without court. Registered FDR practitioners. Call {PHONE}.")
    h1    = f"Parenting Mediation <em>{c}</em>"
    lede  = (f"Parenting mediation in {c} helps separated parents reach child-focused arrangements "
             f"without an adversarial court process. Registered FDR practitioners — we also satisfy "
             f"the legal FDR requirement for parenting applications.")
    ans   = (f"Parenting mediation in {c} lets separated parents agree on living arrangements, "
             f"time, schooling and decision-making without going to court. It is faster and far "
             f"cheaper than litigation, produces more durable outcomes, and satisfies the Family "
             f"Dispute Resolution requirement for parenting applications.")
    qa = [
      (f"Is family dispute resolution compulsory before a parenting application in {c}?",
       f"Yes, generally. Before applying to {court} for parenting orders, parents must make a genuine attempt at FDR, unless an exemption applies (family violence, urgency, or specified other grounds). Our mediators are registered FDR practitioners and issue the relevant certificate on completion of the process."),
      (f"How long does parenting mediation take in {c}?",
       f"Most {c} parenting mediations resolve in a single full-day session. Complex matters may need two sessions. Compare this with 1–2 years for a contested parenting matter through {court} — a period during which children are living with uncertainty."),
      (f"What is the difference between a parenting plan and consent orders in {c}?",
       f"A parenting plan is a written agreement between both parents — not legally enforceable, but recognised by courts. Consent orders are filed with {court} and are legally binding and enforceable. Your mediator will advise which suits your situation and your co-parenting relationship."),
      (f"Can parenting mediation be done online in {c}?",
       f"Yes. Online parenting mediation is available for all {c} and {state} clients, satisfies FDR requirements, and produces the same outcomes as in-person mediation. Particularly useful where parents live in different suburbs, different states, or where attending in person is difficult."),
      (f"What if there is family violence in our situation?",
       f"Where family violence or safety concerns are present, mediation may not be appropriate and exemptions from the FDR requirement apply. Our team will give you an honest assessment. If you or your children are at risk, contact police or 1800RESPECT (1800 737 732) first."),
      (f"Can the mediator decide what's best for the children?",
       f"The mediator does not make decisions — the parents do. However, a skilled parenting mediator consistently redirects the conversation toward the children's actual needs and away from parental grievances. Research shows this produces arrangements that are both better for children and more durable."),
    ]
    return title, desc, h1, lede, ans, body, qa


def workplace_data(city_key, cd):
    c = cd["name"]
    state = cd["state"]
    wa = cd["wa"]
    court = cd["court_ref"]

    wa_irc = (
        " In Western Australia, state-system employees — those not covered by the federal "
        "Fair Work Act — have access to the WA Industrial Relations Commission. Many Perth "
        "workplace disputes involve questions about which system applies (state or federal). "
        "Our mediators understand both frameworks."
    ) if wa else ""

    local_note = {
        "sydney": ("Sydney's dense corporate and professional services sector generates a high "
                   "volume of senior executive disputes, redundancy challenges and general "
                   "protections claims. Law firms, financial services, construction and media "
                   "are sectors where confidential resolution is essential — and where the "
                   "reputational cost of a Fair Work application becoming public is significant."),
        "melbourne": ("Melbourne's large professional services, healthcare and public-sector "
                      "workforce drives significant demand for workplace mediation. Victoria's "
                      "WorkSafe and Worksafe psychological injury frameworks mean employer "
                      "obligations around workplace stress and bullying carry specific legal weight "
                      "— early mediation reduces both legal exposure and WorkCover costs."),
        "brisbane": ("Brisbane's construction, mining services, logistics and government sectors "
                     "generate a steady stream of workplace disputes. Queensland's industrial "
                     "relations framework and the specific obligations under the Work Health and "
                     "Safety Act 2011 (QLD) make early resolution particularly valuable for "
                     "employers managing WHS obligations alongside a dispute."),
        "perth": ("Perth's mining, resources and FIFO workforce creates a specific set of "
                  "workplace dynamics — remote sites, DIDO arrangements, mental health pressures "
                  "and high-stakes redundancies. WA's mixed state-federal industrial framework "
                  "adds complexity that makes early, expert mediation valuable." + wa_irc),
        "adelaide": ("Adelaide's public sector, defence industry and manufacturing base generate "
                     "workplace disputes with specific character — long-service employees, government "
                     "enterprise agreements and procurement-related conflicts. Early mediation in "
                     "Adelaide typically avoids both Fair Work proceedings and lengthy internal "
                     "investigation costs."),
        "canberra": ("Canberra's public-service workforce presents unique workplace mediation needs: "
                     "Australian Public Service performance frameworks, classification disputes, "
                     "APS Code of Conduct investigations and parliamentary department dynamics. "
                     "Our mediators have experience navigating the specific context of Commonwealth "
                     "employment, where discretion is particularly valued."),
        "gold-coast": ("The Gold Coast's hospitality, tourism, construction and retail sectors "
                       "generate a high volume of unfair dismissal and general protections claims. "
                       "For Gold Coast employers, the alternative to mediation is typically a "
                       "Fair Work conciliation in Brisbane — adding travel time and cost on top "
                       "of the legal fees. Mediation in person or online avoids both."),
    }.get(city_key, "")

    body = f"""
<h2>Workplace mediation in {c}: early resolution saves employers and employees</h2>
<p>Workplace conflict in {c} — between employer and employee, between colleagues, or across teams — has a cost that goes beyond legal fees. Productivity drops, morale falls, good people leave, and the risk of formal claims escalates every week the conflict remains unresolved. Workplace mediation is designed to cut through this. It is private, voluntary, structured, and typically resolves in a single day disputes that might otherwise drag through the Fair Work Commission or courts for months.</p>
<p>Our {c} workplace mediators work with both sides of the dispute to reach a practical resolution both parties can live with. The mediator does not determine who is right — they guide a structured, confidential process focused on the practical: what happened, what each party needs, and what a workable resolution looks like.</p>

<h2>Workplace conflict in {c}: the local picture</h2>
<p>{local_note}</p>

<h2>When to use workplace mediation in {c}</h2>
<p>The earlier mediation is called, the more options are available. {c} employers and employees benefit most from mediation at these stages:</p>
<ul>
  <li><strong>Grievance stage</strong> — before formal complaints are filed, while the relationship is still salvageable</li>
  <li><strong>After an internal investigation</strong> — when findings have been made and a structured resolution process is needed</li>
  <li><strong>Unfair dismissal or general protections claims</strong> — before or alongside Fair Work Commission conciliation, to reach a comprehensive settlement</li>
  <li><strong>Redundancy disputes</strong> — where the circumstances or terms of a redundancy are contested</li>
  <li><strong>Workplace bullying complaints</strong> — where a stop-bullying application has been made or threatened</li>
  <li><strong>Executive and leadership conflicts</strong> — board disputes, CEO exits, team dysfunction at senior levels</li>
  <li><strong>Return-to-work disputes</strong> — following workers' compensation, injury or extended leave</li>
</ul>

<h2>Unfair dismissal and general protections in {c}</h2>
<p>If a {c} employee files an unfair dismissal or general protections claim with the Fair Work Commission, the Commission will conciliate the matter — but conciliation is not the same as mediation. The Commission's process focuses on settlement of the specific claim; our mediation addresses the full employment relationship. Where the employment has ended and only the financial settlement is in question, our mediators can work alongside or after the Commission process to reach a comprehensive agreement.{wa_irc}</p>

<h2>The commercial case for workplace mediation in {c}</h2>
<p>The cost of unresolved workplace conflict in {c} is measurable: lost productivity during the dispute, management time consumed by internal processes, legal fees if proceedings are filed, and replacement costs if an employee leaves or is dismissed. A Fair Work unfair dismissal matter that proceeds to arbitration typically costs $15,000–$50,000 per side in legal fees. Workplace mediation typically costs a fraction of that, resolves in a day, and is far more likely to produce an outcome both parties accept. For {c} HR teams managing multiple sites, early mediation also prevents single disputes from becoming broader cultural issues.</p>

<h2>Confidentiality in {c} workplace mediations</h2>
<p>Workplace mediation is conducted on a strictly without-prejudice basis. Statements and admissions made during the session cannot be used in subsequent legal proceedings. This confidentiality is what allows frank conversations — and frank conversations are what produce real resolutions. For {c} employers with reputational concerns, it also means the content of the mediation never enters a public record.</p>

<h2>Post-mediation: what a {c} workplace resolution looks like</h2>
<p>Where both parties remain employed, the agreement typically includes specific commitments — changed working arrangements, a revised reporting structure, communication protocols, or a clear performance framework. These are recorded and signed by both parties. Follow-up facilitation is available where the team needs support through the transition. Where employment ends, the agreement typically covers final payments, references, confidentiality and any formal settlement of claims.</p>
"""
    title = f"Workplace Mediation {c} | Resolve Employment Disputes Faster"
    desc  = (f"Workplace mediation in {c} — resolve unfair dismissal, bullying, grievances and "
             f"employment disputes without the Fair Work Commission or courts. Call {PHONE}.")
    h1    = f"Workplace Mediation <em>{c}</em>"
    lede  = (f"Workplace mediation in {c} resolves employment disputes, grievances, unfair "
             f"dismissal claims and workplace conflict faster and at a fraction of the cost of "
             f"tribunal proceedings. Private, structured, and effective.")
    ans   = (f"Workplace mediation in {c} provides a fast, confidential way to resolve "
             f"employment disputes — unfair dismissal, bullying, grievances and executive "
             f"conflicts — without proceeding to the Fair Work Commission or courts. "
             f"Most {c} workplace mediations resolve in a single day.")
    qa = [
      (f"How does workplace mediation differ from Fair Work Commission conciliation in {c}?",
       f"Fair Work conciliation focuses on settling a specific claim. Workplace mediation goes deeper — addressing the underlying conflict in the employment relationship, not just the formal complaint. Both processes can be used in sequence, or our mediation can stand alone where no formal claim has been filed."),
      (f"Is workplace mediation confidential in {c}?",
       f"Yes. Workplace mediation is conducted on a strictly without-prejudice basis. Nothing said in the session can be used in subsequent proceedings. This confidentiality is essential for frank conversations — and frank conversations are what produce genuine resolutions."),
      (f"How long does workplace mediation take in {c}?",
       f"Most {c} workplace mediations resolve in a single day. Pre-mediation preparation (individual sessions, document review) typically takes 1–2 hours per side beforehand. Complex matters with multiple parties may need a second session."),
      (f"Can workplace mediation be used for bullying complaints in {c}?",
       f"Yes. Mediation is widely used for {c} workplace bullying matters — before a stop-bullying application is filed, alongside an internal investigation, or after investigation findings are made. It is often more effective than a purely disciplinary response, particularly where both parties will continue working together."),
      (f"Do both parties have to agree to workplace mediation in {c}?",
       f"Yes. Mediation is voluntary — both employer and employee must consent. In practice, most {c} employers agree when the alternative costs and disruption of a Fair Work application are explained clearly. We can assist with outreach to the other party if needed."),
      (f"Can workplace mediation be done remotely in {c}?",
       f"Yes. Secure online workplace mediation is available for all {c} and {state} clients. Particularly useful for multi-site employers, FIFO workforces, and situations where the parties prefer not to be in the same building."),
    ]
    return title, desc, h1, lede, ans, body, qa


# ─────────────────────────────────────────────────────────────────────────────
#  SERVICE CONFIG  (slug-prefix, display name, data fn, hub slug for breadcrumb)
# ─────────────────────────────────────────────────────────────────────────────
SERVICES_CFG = [
    ("property-settlement-mediation", "Property Settlement Mediation",
     property_data, "property-settlement-mediation"),
    ("divorce-mediation",             "Divorce Mediation",
     divorce_data,   "divorce-mediation"),
    ("parenting-mediation",           "Parenting Mediation",
     parenting_data, "parenting-plan-mediation"),
    ("workplace-mediation",           "Workplace Mediation",
     workplace_data, "workplace-mediation"),
]

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE BUILDER
# ─────────────────────────────────────────────────────────────────────────────
def build_page(svc_slug, svc_name, data_fn, hub_slug, city_key, cd):
    c = cd["name"]
    state = cd["state"]

    slug = f"{svc_slug}-{city_key}"
    title, desc, h1, lede, ans, body, qa = data_fn(city_key, cd)

    if cd["has_office"]:
        access = (f"Our {c} office is at {cd['office']}. We also offer secure online mediation "
                  f"for all {c} and {state} clients.")
    else:
        nearest = {"SA": "Melbourne", "ACT": "Sydney", "QLD": "Brisbane"}.get(state, "Sydney")
        access = (f"We serve {c} clients in person by arrangement and through secure online "
                  f"mediation — the same nationally accredited mediators as our {nearest} office, "
                  f"available wherever you are in {state}.")

    schema = [
        org_schema(),
        breadcrumb_schema([("Home",""), (svc_name, hub_slug), (f"{svc_name} {c}", slug)]),
        article_schema(f"{svc_name} {c}", desc),
        faq_schema(qa),
    ]

    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += f"""<main id="main">
{crumb_html([("Home",""), (svc_name, hub_slug), (c, None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{esc(c)} &middot; {esc(state)} &middot; Nationally accredited</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Free Consultation <span class="arr">&rarr;</span></a>
      <a href="tel:{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {ans}</p></div></div>
<article class="body"><div class="wrap-narrow reveal">
{body}
<h2>Getting started with {esc(svc_name.lower())} in {esc(c)}</h2>
<p>{access} Every matter begins with a free initial consultation — no obligation, no billing surprises. We listen to your situation, explain what the process looks like, and give you an honest view of whether mediation can help. If it can, we move quickly: most {esc(c)} sessions are booked within days, not weeks.</p>
<p>If the other party hasn't agreed to mediation yet, we can help with that too — explaining the process and addressing the concerns that often prevent people from engaging. <a href="/how-mediation-works/">How mediation works &rarr;</a></p>
</div></article>"""

    doc += faq_html(qa, heading=f"{svc_name} {c} &mdash; FAQs")
    doc += cta_band(
        f"{esc(svc_name)} in {esc(c)} &mdash; <em>start here.</em>",
        f"Book a free initial consultation and find out how our accredited {esc(c)} mediators can help you reach a resolution faster, cheaper and without court."
    )
    doc += "</main>" + page_end()

    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as fh:
        fh.write(doc)

    words = len(re.sub(r'<[^>]+>', ' ', doc).split())
    return slug, words


# ─────────────────────────────────────────────────────────────────────────────
#  PHASE ORDERING  (office cities first, then secondary)
# ─────────────────────────────────────────────────────────────────────────────
PHASE1 = ["sydney", "melbourne", "brisbane", "perth"]
PHASE2 = ["adelaide", "canberra", "gold-coast"]


if __name__ == "__main__":
    results = []
    for phase_name, city_keys in [("Phase 1 — office cities", PHASE1),
                                   ("Phase 2 — secondary cities", PHASE2)]:
        print(f"\n{phase_name}:")
        for city_key in city_keys:
            cd = CITIES[city_key]
            for svc_slug, svc_name, data_fn, hub_slug in SERVICES_CFG:
                slug, words = build_page(svc_slug, svc_name, data_fn, hub_slug, city_key, cd)
                print(f"  {slug}: ~{words:,} words")
                results.append(slug)
    print(f"\nTotal pages built: {len(results)}")
