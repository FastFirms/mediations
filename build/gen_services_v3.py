#!/usr/bin/env python3
"""Batch 2 of cornerstone-depth service pages.

Six high-value commercial service pages, each ~1,500-1,800 words, built to the
same standard as the blog cornerstones: keyword-first H1, key-takeaway answer
box, TOC, 7-8 substantive sections, inline CTAs, data tables where useful,
FAQ with schema, related grid.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)
from authority_sources import cite
from workplace_pricing import price_block as _wp_block, offers_schema, faq_answers
WP_PRICE_BLOCK = _wp_block()
WP_FAQ = faq_answers()
from gen_services_v2 import inline_cta, key_takeaway, callout, toc, related_grid, service_page

# ====================================================================
# 4. PARENTING PLAN MEDIATION
# ====================================================================
service_page(
    slug="parenting-plan-mediation",
    title="Parenting Plan Mediation in Australia | Mediations Australia",
    desc="Build a workable parenting plan through accredited mediation. Child-focused arrangements, faster than court, with the option to make it legally binding via consent orders.",
    breadcrumb_label="Parenting Plan Mediation",
    eyebrow="Your kids need stability — we can help create it",
    h1_html='Parenting Plan Mediation \u2014 <em>arrangements built around your kids</em>.',
    lede="A parenting plan is the practical agreement that runs your kids' lives after separation \u2014 where they live, when they see each parent, how decisions get made. Mediation is how most Australian parents build one that actually works in real life, rather than handing the decision to a court.",
    toc_items=[
        ("what-is","What is a parenting plan?"),
        ("vs-orders","Parenting plan vs consent orders"),
        ("included","What goes into a parenting plan"),
        ("how","How mediation builds it"),
        ("child-focus","Keeping the child at the centre"),
        ("changing","Changing the plan over time"),
        ("binding","Making it legally binding"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "A parenting plan is a written, signed agreement between parents covering living arrangements, time with each parent, decision-making, and communication. It's not directly enforceable by a court \u2014 for that you need consent orders \u2014 but it's the practical, flexible framework most separated families actually run their lives by. Mediation is how parents build a parenting plan that holds together, fast and at a fraction of the cost of court."
    ),
    body_html="""
<h2 id="what-is">What is a parenting plan?</h2>
<p>A parenting plan is a written agreement between parents that sets out how they'll share the care and raising of their children after separation. It covers the practical details \u2014 where the children live, the time they spend with each parent, how decisions are made, how communication happens \u2014 in enough detail to actually function as a working arrangement.</p>

<p>It must be in writing, signed by both parents, and dated. It can be reached directly or, more often, through <a href=\"/family-law-mediation/\">family law mediation</a>. The Family Law Act recognises parenting plans as the way parents typically organise life after separation \u2014 they're explicitly contemplated in the legislation as a legitimate alternative to court orders.</p>
""" + inline_cta("Want a parenting arrangement that actually works in everyday life? Book a consultation with an accredited mediator.") + """

<h2 id="vs-orders">Parenting plan vs consent orders</h2>
<p>This is the most important distinction to understand. A parenting plan and consent orders cover similar ground, but they're not the same thing:</p>

<figure class="tbl"><table><caption>Parenting plan vs consent orders</caption>
<thead><tr><th></th><th>Parenting plan</th><th>Consent orders</th></tr></thead>
<tbody>
<tr><td>Format</td><td>Written, signed, dated agreement</td><td>Court-approved orders</td></tr>
<tr><td>Legally enforceable?</td><td>No, not directly</td><td>Yes, same as a judge's order</td></tr>
<tr><td>Flexibility to change</td><td>High \u2014 just agree and update</td><td>Low \u2014 needs court application</td></tr>
<tr><td>Cost</td><td>Mediation fee only</td><td>Mediation + filing fee + drafting</td></tr>
<tr><td>Time to put in place</td><td>Days</td><td>Weeks (court processing)</td></tr>
<tr><td>Best when</td><td>Parents communicate, want flexibility</td><td>Need certainty, history of conflict</td></tr>
</tbody></table></figure>

<p>For many families, the right answer is a parenting plan first \u2014 lived in for a while, refined as the kids grow \u2014 with consent orders later if the arrangements stabilise and you want them locked in. Some families go straight to consent orders. We help you choose. <a href=\"/parenting-plans-guide/\">See the full parenting plans guide \u2192</a></p>

<h2 id="included">What goes into a parenting plan</h2>
<p>A well-built plan covers the issues you'll actually face week to week:</p>
<ul>
  <li><strong>Living arrangements</strong> \u2014 primary residence, time at each home, the weekly rhythm</li>
  <li><strong>Time with each parent</strong> \u2014 the weekly pattern, holidays, special days (birthdays, Christmas, Mother's/Father's Day)</li>
  <li><strong>School holidays</strong> \u2014 how the longer breaks are divided</li>
  <li><strong>Travel</strong> \u2014 within Australia and overseas, including consent for passports</li>
  <li><strong>Decision-making</strong> \u2014 schooling, healthcare, religion, extracurriculars</li>
  <li><strong>Day-to-day communication</strong> \u2014 between parents and with the children</li>
  <li><strong>Changeover</strong> \u2014 location, time, who does it</li>
  <li><strong>Future changes</strong> \u2014 how the plan gets updated as kids grow and life shifts</li>
  <li><strong>Disputes</strong> \u2014 how disagreements get resolved (often: back to mediation)</li>
</ul>
""" + inline_cta("Sweat the small stuff while you're calm \u2014 it prevents 90% of future arguments. Mediation does this systematically.") + f"""

<h2 id="how">How mediation builds it</h2>
<ol>
  <li><strong>Initial intake</strong> \u2014 each parent meets separately with the practitioner. We map the issues, assess any safety concerns, and prepare you for the session.</li>
  <li><strong>Pre-mediation thinking</strong> \u2014 you work through what you want, what the kids need, what's practical given work and distance.</li>
  <li><strong>The mediation session</strong> \u2014 you and your former partner work through the arrangement with the mediator's guidance. Joint session or <a href=\"/shuttle-mediation-guide/\">shuttle (separate rooms)</a> depending on the dynamics.</li>
  <li><strong>Drafting the plan</strong> \u2014 the agreement is documented in plain language while it's fresh.</li>
  <li><strong>Sign-off</strong> \u2014 both parents sign and date the plan. Done.</li>
  <li><strong>Optional formalisation</strong> \u2014 if you want it legally binding, the plan becomes the basis for consent orders.</li>
</ol>

<p>This is a recognised approach under the {cite("ag_fdr")} framework, and the practitioner is accredited to issue a {esc("Section 60I certificate")} if the matter doesn't fully resolve.</p>

<h2 id="child-focus">Keeping the child at the centre</h2>
<p>The single most important principle in any parenting plan: it's about what the children need, not about what either parent feels they're owed. The legal test is the <strong>best interests of the child</strong> \u2014 the same standard a court applies. <a href=\"/child-custody-mediation/\">See how the best-interests test works \u2192</a></p>

<p>In practice, this means thinking about:</p>
<ul>
  <li><strong>Stability and routine</strong> \u2014 children, especially younger ones, thrive on predictability</li>
  <li><strong>Meaningful relationships with both parents</strong> \u2014 where safe</li>
  <li><strong>The children's developmental stage</strong> \u2014 a toddler's needs aren't a teenager's needs</li>
  <li><strong>Their voice (age-appropriately)</strong> \u2014 older children's views matter, without making them decide</li>
  <li><strong>Safety, above all</strong> \u2014 where there are concerns, they take priority over contact</li>
</ul>
""" + callout("Avoid the parenting plan trap of equal time obsession",
   "Many parents get fixated on a 50/50 split. The law doesn't start from there \u2014 it starts from what works for the kids. Sometimes that's 50/50; often it's something different. The right arrangement is the one your children can live well inside.") + """

<h2 id="changing">Changing the plan over time</h2>
<p>This is where parenting plans really shine. Children grow, circumstances change, what worked at five doesn't work at fifteen. A parenting plan can be updated by simple agreement \u2014 sign a new one, date it, done. Compare that with court orders, which require a fresh application to change.</p>

<p>The flexibility cuts both ways: it means a plan only holds if both parents continue to honour it. Where one parent stops cooperating, a plan offers less protection than a court order. That's why many families build the parenting plan first, then move to consent orders once the arrangements have proved stable. <a href=\"/consent-orders/\">See consent orders \u2192</a></p>

<h2 id="binding">Making it legally binding</h2>
<p>A parenting plan itself isn't directly enforceable. To give it the force of law \u2014 so that breaches have legal consequences \u2014 the plan needs to be converted into <strong>consent orders</strong>: a court-approved version of the same arrangement. The court reviews the proposed orders against the best-interests test, and if approved, they're enforceable just like a judge had ordered them.</p>

<p>We handle this conversion as part of the mediation service \u2014 you're not left to find separate lawyers to draft the orders. Most families who go this route do so within a few weeks of finalising their plan. <a href=\"/bfa-or-consent-orders/\">See which option suits you \u2192</a></p>
""" + inline_cta("Whether you need a parenting plan, consent orders, or both \u2014 we'll work it out with you. Book a Free Consultation.") + """

<h2 id="get-started">Getting started</h2>
<p>The first step is a free initial consultation. We'll listen to your situation, assess whether mediation is the right path for your family, and outline what's involved. Most parenting plan mediations are resolved in one or two sessions \u2014 a matter of weeks, not the years a contested matter can take.</p>

<p>If your situation has any safety concerns or family violence history, we'll assess that honestly and help you understand the alternatives. Mediation isn't appropriate for every family \u2014 but it's the right path for most, and we'll tell you straight which side of that line you're on.</p>
""",
    faq_items=[
        ("Is a parenting plan legally binding?",
         "Not directly. A parenting plan is a written agreement, but it's not enforceable in the same way a court order is. To make it legally enforceable, you formalise it into consent orders \u2014 which the court reviews and approves."),
        ("How is a parenting plan different from consent orders?",
         "A parenting plan is a private signed agreement; consent orders are court-approved orders with the force of a judge's decision. Plans offer more flexibility and lower cost; orders offer enforceability and certainty."),
        ("What should a parenting plan include?",
         "Living arrangements, time with each parent, school holidays, travel, decision-making on major issues (school, health, religion), day-to-day communication, changeover, and how future disputes get resolved."),
        ("Can a parenting plan be changed?",
         "Yes, easily \u2014 both parents simply agree and sign an updated version. This flexibility is one of its main advantages over consent orders, which require court application to vary."),
        ("Do I need to do mediation before I can apply to court for parenting orders?",
         "Generally yes \u2014 the Family Law Act requires you to attempt Family Dispute Resolution and obtain a Section 60I certificate before applying, unless an exemption applies."),
        ("What if my ex won't stick to the parenting plan?",
         "If breaches are persistent and the plan isn't being honoured, you can move to consent orders (court-approved and enforceable). We help you make that transition."),
        ("How does a parenting plan deal with child support?",
         "Parenting plans focus on care arrangements. Child support is a separate question administered by Services Australia, though parents can set out a private arrangement in the plan too if they prefer."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("child-custody-mediation","Child Custody Mediation"),
        ("consent-orders","Consent Orders"),
        ("parenting-plans-guide","Parenting Plans: Complete Guide"),
        ("section-60i-certificates","Section 60I Certificates"),
        ("child-support-mediation","Child Support Mediation"),
        ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
    bg_image="/assets/images/hero-parenting-plan-mediation.jpg",
    bg_pos="center 50%",
)


# ====================================================================
# 5. CONSENT ORDERS
# ====================================================================
service_page(
    slug="consent-orders",
    title="Consent Orders in Australia | Mediations Australia",
    desc="Make your mediated agreement legally binding through consent orders. How they work, what they cost, how long they take \u2014 with accredited support through the full process.",
    breadcrumb_label="Consent Orders",
    eyebrow="Make your agreement stick \u2014 legally and permanently",
    h1_html='Consent Orders \u2014 <em>your agreement, with the force of law</em>.',
    lede="Consent orders turn your mediated agreement into a binding court order \u2014 same effect as if a judge had ordered it, but without ever needing to fight one out in court. It's the standard, sensible final step for most separating couples who've reached agreement and want it to stick.",
    toc_items=[
        ("what-are","What are consent orders?"),
        ("when-needed","When you need them"),
        ("parenting-property","For parenting and property"),
        ("how","How the process works"),
        ("costs","Costs and timeframes"),
        ("approved","How the court reviews them"),
        ("vs-bfa","Consent orders vs BFA"),
        ("changing","Changing or enforcing"),
    ],
    takeaway=key_takeaway(
        "Consent orders are court-approved orders that record your agreement on parenting, property and/or financial matters and make it legally binding \u2014 with the same effect as if a judge had decided. You don't need to attend court. The application is filed with the Federal Circuit and Family Court, which reviews it against the legal tests and approves it. The standard, cost-effective way to give a mediated agreement the force of law."
    ),
    body_html=f"""
<h2 id="what-are">What are consent orders?</h2>
<p>Consent orders are orders the {cite("fcfcoa")} makes based on an agreement the parties have already reached. You and your former partner agree the terms (typically through <a href=\"/family-law-mediation/\">mediation</a>), file the application with the court, and a registrar reviews and approves the orders. From that point on, the orders are legally binding \u2014 enforceable in exactly the same way as orders made after a contested hearing.</p>

<p>The key distinction: there's no contest. You're not asking the court to decide between competing positions \u2014 you're asking it to formalise a position you've already agreed. The court's job is to make sure the orders are just and equitable (for property) or in the best interests of the children (for parenting), then sign them off.</p>
""" + inline_cta("Reached agreement and want it locked in legally? Consent orders are the standard next step \u2014 talk to us.") + """

<h2 id="when-needed">When you need them</h2>
<p>You don't strictly <em>need</em> consent orders for every separation \u2014 but you need them in any situation where you want the agreement to be legally enforceable. That's most situations.</p>
<ul>
  <li><strong>For property settlement</strong>, consent orders are usually essential. Without them, either party can technically come back and make a property claim later (subject to time limits). Orders close the door on future claims.</li>
  <li><strong>For parenting arrangements</strong>, consent orders aren't strictly required \u2014 a parenting plan can do the job in stable, cooperative situations. But where there's any risk of breach or future dispute, consent orders give you enforceability.</li>
  <li><strong>For superannuation splitting</strong>, consent orders (or a BFA) are essentially required \u2014 super funds need the formal order to action a split.</li>
</ul>

<h2 id="parenting-property">For parenting and property</h2>
<p>The same court process covers both. You can file consent orders for parenting only, property only, or both together. Many separating couples do both together \u2014 one application, one filing fee, one set of approved orders covering the whole picture.</p>

<p>The court applies different tests:</p>
<ul>
  <li><strong>For property:</strong> the orders must be <em>just and equitable</em> in all the circumstances. The registrar checks the agreement against the asset pool and the four-step framework. <a href=\"/property-settlement-after-separation/\">See the four-step framework \u2192</a></li>
  <li><strong>For parenting:</strong> the orders must be in the <em>best interests of the children</em>. The registrar checks the arrangement is workable and child-focused. <a href=\"/child-custody-mediation/\">See the best-interests test \u2192</a></li>
</ul>

<h2 id="how">How the process works</h2>
<ol>
  <li><strong>Reach agreement</strong> \u2014 through mediation, direct negotiation, or with lawyers.</li>
  <li><strong>Draft the orders</strong> \u2014 the agreement is translated into the precise legal language the court needs. This matters: vague orders cause problems later.</li>
  <li><strong>Prepare the Application for Consent Orders (Form 11)</strong> \u2014 the supporting document covering financial disclosure, the asset pool, contributions, future needs.</li>
  <li><strong>Both parties sign</strong> the application and the proposed orders.</li>
  <li><strong>File with the court</strong> \u2014 electronically through the Commonwealth Courts Portal.</li>
  <li><strong>The court reviews</strong> \u2014 a registrar checks the application against the legal tests. They may ask for clarification or amendments.</li>
  <li><strong>Orders made</strong> \u2014 typically within four to eight weeks, depending on workload. You receive sealed orders.</li>
</ol>

<p>You generally do not need to attend court. The process is paper-based (or, more accurately, screen-based). <a href=\"/consent-orders-explained/\">See the consent orders explainer \u2192</a></p>
""" + inline_cta("The drafting is where consent orders go right or wrong. Get it done by people who do it weekly. Book a consultation.") + """

<h2 id="costs">Costs and timeframes</h2>
<p>Consent orders are dramatically cheaper than a contested matter, and reasonably predictable in cost:</p>
<ul>
  <li><strong>Court filing fee</strong>: a few hundred dollars, payable when the application is lodged. Fee reductions may apply for eligible applicants.</li>
  <li><strong>Drafting and supporting documents</strong>: typically $1,500\u2013$3,500 depending on complexity. Property matters with businesses or trusts are at the higher end.</li>
  <li><strong>Time to orders being made</strong>: typically 4\u20138 weeks from filing.</li>
</ul>

<p>That's the whole picture \u2014 no hourly billing, no surprises. Compare it to the $50,000\u2013$200,000+ per side that contested litigation can run.</p>

<h2 id="approved">How the court reviews them</h2>
<p>The registrar isn't rubber-stamping. They look for specific things:</p>
<ul>
  <li><strong>For property:</strong> does the proposed division appear just and equitable? Are the financial disclosures sensible? Has super been addressed?</li>
  <li><strong>For parenting:</strong> are the arrangements practical and child-focused? Are there safety concerns the orders need to account for?</li>
  <li><strong>Drafting:</strong> are the orders clear, specific and enforceable? Vague orders cause future disputes.</li>
</ul>

<p>If something doesn't sit right, the registrar will come back with questions or suggested amendments. This is why getting the application well-drafted up front saves time \u2014 the application either sails through or it gets bounced back for revision.</p>

<h2 id="vs-bfa">Consent orders vs binding financial agreement</h2>
<p>Both make a property/financial agreement binding, but they're different paths:</p>

<figure class=\"tbl\"><table><caption>Consent orders vs BFA</caption>
<thead><tr><th></th><th>Consent orders</th><th>Binding financial agreement</th></tr></thead>
<tbody>
<tr><td>Court involved?</td><td>Yes \u2014 reviewed and approved</td><td>No \u2014 private contract</td></tr>
<tr><td>Legal certainty</td><td>Very high</td><td>High, with caveats</td></tr>
<tr><td>Independent legal advice required?</td><td>Recommended, not required</td><td>Required for both parties</td></tr>
<tr><td>Court fee</td><td>Yes</td><td>No</td></tr>
<tr><td>Time to finalise</td><td>4\u20138 weeks</td><td>Days, once advice is done</td></tr>
<tr><td>Can cover parenting?</td><td>Yes</td><td>No \u2014 financial only</td></tr>
<tr><td>Risk of being set aside</td><td>Very low</td><td>Slightly higher</td></tr>
</tbody></table></figure>

<p>For most separating couples, consent orders are the safer, more comprehensive option. BFAs make sense in specific cases. <a href=\"/bfa-or-consent-orders/\">See which is right for you \u2192</a></p>
""" + inline_cta("Not sure whether consent orders or a BFA suits you? We'll explain the difference and help you choose.") + """

<h2 id="changing">Changing or enforcing orders</h2>
<p>Consent orders are durable but not entirely immovable:</p>
<ul>
  <li><strong>Property orders</strong> are essentially final \u2014 they can only be set aside in narrow circumstances (fraud, miscarriage of justice, fundamental change). That finality is exactly the point of having them.</li>
  <li><strong>Parenting orders</strong> can be varied if there's been a significant change in circumstances \u2014 but only by application to the court, not by private agreement.</li>
  <li><strong>Enforcement</strong>: where one party breaches an order, the other can apply to enforce it. Breaches carry real consequences, which is exactly why orders are more protective than a parenting plan.</li>
</ul>
""",
    faq_items=[
        ("Do I have to go to court for consent orders?",
         "No. The process is paper-based (filed electronically through the Commonwealth Courts Portal). You generally don't need to attend court \u2014 the registrar reviews the application and either approves it or asks for clarification."),
        ("How long do consent orders take?",
         "Typically 4\u20138 weeks from filing to orders being made, depending on the court's workload. The mediation step before that is usually a few weeks. So the full path from starting to mediate to having sealed orders is often 6\u201310 weeks."),
        ("How much do consent orders cost?",
         "A court filing fee (a few hundred dollars) plus drafting fees (typically $1,500\u2013$3,500 depending on complexity). That's the whole picture \u2014 dramatically cheaper than contested litigation."),
        ("Do we both need lawyers?",
         "It's recommended but not legally required for consent orders (unlike BFAs, which do require independent legal advice for each party). For complex matters, getting advice protects both parties."),
        ("Can consent orders cover both parenting and property?",
         "Yes \u2014 the same application can cover both, in one filing. Many separating couples do them together."),
        ("Can consent orders be changed later?",
         "Property orders are essentially final, except in narrow circumstances. Parenting orders can be varied if there's been a significant change in circumstances, by application to the court."),
        ("What happens if my ex breaches the orders?",
         "You can apply to the court to enforce them. Breaches of consent orders carry the same legal consequences as breaches of any other court orders \u2014 which is why orders are far more protective than a parenting plan or informal agreement."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("consent-orders-explained","Consent Orders Explained"),
        ("financial-agreements-mediation","Financial Agreements"),
        ("bfa-or-consent-orders","BFA or Consent Orders?"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("parenting-plan-mediation","Parenting Plan Mediation"),
        ("property-settlement-after-separation","Property Settlement Guide"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
    bg_image="/assets/images/hero-consent-orders-mediation.jpg",
    bg_pos="center 50%",
)


# ====================================================================
# 6. FINANCIAL AGREEMENTS MEDIATION (BFAs)
# ====================================================================
service_page(
    slug="financial-agreements-mediation",
    title="Binding Financial Agreements (BFAs) | Mediations Australia",
    desc="Reach a binding financial agreement through accredited mediation. How BFAs work, when they're appropriate, and how to make yours hold up. Free consultation.",
    breadcrumb_label="Financial Agreements",
    eyebrow="Protect what you've both worked hard for",
    h1_html='Financial Agreements Mediation \u2014 <em>private, binding, lawyer-proof</em>.',
    lede="A binding financial agreement (BFA) is a private contract setting out how you and your partner divide finances \u2014 before, during, or after a relationship. Done right, it's enforceable without involving a court. Done wrong, it's challenged and set aside. The difference is in the drafting.",
    toc_items=[
        ("what-is","What is a binding financial agreement?"),
        ("when","When BFAs make sense"),
        ("types","Three types of BFA"),
        ("requirements","What makes a BFA binding"),
        ("how","How we build yours"),
        ("vs-orders","BFA vs consent orders"),
        ("risks","The risks to avoid"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "A binding financial agreement (BFA) is a private contract under the Family Law Act setting out how property and finances are divided \u2014 typically used before marriage (a prenup), during a relationship, or after separation. It's binding without court involvement, but it must meet strict requirements: independent legal advice for both parties, proper disclosure, and careful drafting. We mediate the substance and handle the formal requirements so the agreement actually holds."
    ),
    body_html=f"""
<h2 id="what-is">What is a binding financial agreement?</h2>
<p>A BFA is a contract between partners that sets out how their property and financial affairs are to be divided. It's a creature of the {cite("family_law_act")} \u2014 sections 90B\u201390KA for married couples, 90UB\u201390UM for de facto couples \u2014 and when properly executed, it's binding without ever needing court approval.</p>

<p>People often call them \"prenups\" but BFAs come in three forms (covered below), and the term is much broader than the pre-wedding contract most people picture.</p>
""" + inline_cta("Thinking about a BFA? Get the substance right through mediation, then we handle the formal requirements. Book a consultation.") + """

<h2 id="when">When BFAs make sense</h2>
<p>BFAs work particularly well when:</p>
<ul>
  <li>One or both partners is entering a relationship with significant existing assets</li>
  <li>There's a family business, trust, or inheritance that needs to be quarantined</li>
  <li>Both partners want certainty about what happens financially if the relationship ends</li>
  <li>You want to avoid court involvement entirely \u2014 even the paperwork-only consent orders process</li>
  <li>Speed matters \u2014 BFAs can be finalised in days once the legal advice is done, vs weeks for consent orders</li>
</ul>

<p>They don't suit every situation \u2014 BFAs can't cover parenting arrangements, and there are circumstances where consent orders are the safer choice. <a href=\"/bfa-or-consent-orders/\">See BFA or consent orders \u2192</a></p>

<h2 id="types">Three types of BFA</h2>
<p>The Family Law Act creates three distinct moments at which a BFA can be made:</p>
<ol>
  <li><strong>Before the relationship</strong> (s 90B / s 90UB) \u2014 the \"prenup\". Made before marriage or before moving in together, setting out what would happen on separation.</li>
  <li><strong>During the relationship</strong> (s 90C / s 90UC) \u2014 sometimes called a \"postnup\". Made while you're together, for example to formalise the arrangement after acquiring a major asset or inheritance.</li>
  <li><strong>After separation</strong> (s 90D / s 90UD) \u2014 finalising a settlement without going through consent orders.</li>
</ol>

<p>All three are binding contracts. The legal requirements are essentially the same; what differs is the timing and the financial situation being captured.</p>

<h2 id="requirements">What makes a BFA binding</h2>
<p>This is where BFAs are won or lost. The legislation imposes strict formal requirements:</p>
<ul>
  <li><strong>Independent legal advice for both parties</strong> \u2014 each party must receive advice from their own lawyer, on the effect of the agreement and whether it's advantageous or disadvantageous.</li>
  <li><strong>Statement of legal advice</strong> \u2014 each lawyer signs a statement confirming the advice was given.</li>
  <li><strong>Both parties must sign</strong> \u2014 with the statements attached.</li>
  <li><strong>The agreement must be in writing</strong> \u2014 obviously, but also: it must cover the right matters and be drafted precisely.</li>
  <li><strong>No legal incapacity, duress, fraud or undue influence</strong> \u2014 the agreement must be entered freely.</li>
  <li><strong>Proper disclosure</strong> \u2014 each party should fully disclose their financial position. Hiding assets is a route to having the agreement set aside.</li>
</ul>
""" + callout("The legal advice requirement is not optional",
   "A BFA without proper independent legal advice for both parties is liable to be set aside. The advice isn't a tick-box \u2014 it's a substantive requirement. We make sure it happens properly, because the agreement is only as good as its formal compliance.") + f"""

<h2 id="how">How we build yours</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 we understand what you want the BFA to do, and confirm it's the right instrument for your situation.</li>
  <li><strong>Disclosure</strong> \u2014 full and frank financial disclosure between the parties.</li>
  <li><strong>Mediation on the substance</strong> \u2014 working through the terms together, building the agreement everyone can live with.</li>
  <li><strong>Drafting</strong> \u2014 translating the agreement into precise legal language.</li>
  <li><strong>Independent legal advice</strong> \u2014 each party obtains advice from their own lawyer. We can refer to appropriate independent lawyers if needed.</li>
  <li><strong>Signing</strong> \u2014 with the legal advice statements attached.</li>
  <li><strong>Done</strong> \u2014 the BFA is binding from signing. No court involvement.</li>
</ol>

<h2 id="vs-orders">BFA vs consent orders</h2>
<p>The choice between a BFA and consent orders is one of the most common questions we get. Both can make a financial settlement binding, but they work differently:</p>

<figure class=\"tbl\"><table><caption>BFA vs consent orders</caption>
<thead><tr><th></th><th>BFA</th><th>Consent orders</th></tr></thead>
<tbody>
<tr><td>Court involvement</td><td>None</td><td>Reviewed and approved</td></tr>
<tr><td>Independent legal advice</td><td>Required for both</td><td>Recommended but not required</td></tr>
<tr><td>Privacy</td><td>Completely private</td><td>Filed with the court</td></tr>
<tr><td>Speed to finalise</td><td>Days once advice is done</td><td>4\u20138 weeks court processing</td></tr>
<tr><td>Cost</td><td>Higher (two sets of legal advice)</td><td>Lower per party (filing fee shared)</td></tr>
<tr><td>Covers parenting?</td><td>No \u2014 financial only</td><td>Yes</td></tr>
<tr><td>Risk of being set aside</td><td>Slightly higher</td><td>Very low</td></tr>
</tbody></table></figure>

<p>In general: BFAs offer privacy and speed; consent orders offer maximum legal certainty. We help you choose based on your specific situation. <a href=\"/consent-orders/\">See consent orders \u2192</a></p>
""" + inline_cta("The choice between BFA and consent orders is fact-specific. We'll walk you through it in a consultation.") + """

<h2 id="risks">The risks to avoid</h2>
<p>BFAs that get set aside almost always fail for predictable reasons:</p>
<ul>
  <li><strong>Inadequate legal advice</strong> \u2014 cursory advice, or advice that didn't cover the right matters. Get the advice properly.</li>
  <li><strong>Incomplete disclosure</strong> \u2014 one party hid assets or income. The agreement is built on a false picture.</li>
  <li><strong>Duress or undue influence</strong> \u2014 one party was pressured, or signed under time pressure (the classic wedding-eve prenup).</li>
  <li><strong>Vagueness in drafting</strong> \u2014 unclear terms invite later argument. Precise drafting matters.</li>
  <li><strong>Material change of circumstances</strong> \u2014 some BFAs are set aside where circumstances change so radically that enforcing them would be unconscionable.</li>
</ul>

<h2 id="get-started">Getting started</h2>
<p>The first step is a free initial consultation. We'll listen to your situation, assess whether a BFA is the right instrument (vs consent orders or another path), and outline the process and timeline. If you proceed, we mediate the substance, handle the drafting, and ensure the formal requirements are met so the agreement actually holds.</p>
""",
    faq_items=[
        ("What is a binding financial agreement?",
         "A private contract between partners under the Family Law Act setting out how property and finances are divided. Used before, during, or after a relationship \u2014 binding without court involvement."),
        ("Do both parties need a lawyer for a BFA?",
         "Yes \u2014 each party must receive independent legal advice from their own lawyer, with a signed statement confirming the advice. This is a strict requirement; without it, the BFA can be set aside."),
        ("How long does a BFA take to finalise?",
         "Once the substance is agreed through mediation and the drafting is done, finalising the signed agreement (with independent legal advice for each party) typically takes days to a couple of weeks."),
        ("Is a BFA the same as a prenup?",
         "A prenup is one form of BFA \u2014 made before marriage. BFAs can also be made during the relationship (postnup) or after separation. All three are governed by the same legislation."),
        ("Can a BFA cover parenting arrangements?",
         "No. BFAs cover financial matters only. Parenting arrangements need to be set out in a parenting plan or consent orders."),
        ("Are BFAs ever set aside?",
         "Yes, in specific circumstances: inadequate legal advice, incomplete disclosure, duress, unconscionable circumstances, or material change of circumstances. Properly executed BFAs with thorough advice are robust."),
        ("BFA or consent orders \u2014 which should I choose?",
         "BFAs offer privacy, speed and no court involvement; consent orders offer maximum legal certainty and can cover parenting. The right choice depends on your situation \u2014 we walk you through it."),
    ],
    related_items=[
        ("consent-orders","Consent Orders"),
        ("binding-financial-agreements-guide","Binding Financial Agreements: Complete Guide"),
        ("bfa-or-consent-orders","BFA or Consent Orders?"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("property-settlement-after-separation","Property Settlement Guide"),
        ("family-law-mediation","Family Law Mediation"),
        ("de-facto-mediation","De Facto Mediation"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
    bg_image="/assets/images/hero-financial-agreements-mediation.jpg",
    bg_pos="center 50%",
)


# ====================================================================
# 7. SECTION 60I CERTIFICATES
# ====================================================================
service_page(
    slug="section-60i-certificates",
    title="Section 60I Certificates in Australia | Mediations Australia",
    desc="Get a Section 60I certificate from an accredited Family Dispute Resolution Practitioner. Required before parenting court applications under the Family Law Act. Free consultation.",
    breadcrumb_label="Section 60I Certificates",
    eyebrow="Required before court — we can issue yours",
    h1_html='Section 60I Certificates \u2014 <em>the document the court requires</em>.',
    lede="Before you can file a parenting application in court, you generally need a Section 60I certificate \u2014 proof that you've attempted Family Dispute Resolution. We're accredited Family Dispute Resolution Practitioners, and we issue valid certificates as part of the mediation process.",
    toc_items=[
        ("what-is","What is a Section 60I certificate?"),
        ("when-required","When you need one"),
        ("types","The five certificate types"),
        ("how","How we issue them"),
        ("exemptions","Exemptions from the requirement"),
        ("after","What happens after you get one"),
        ("costs","Costs and timeframes"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "A Section 60I certificate is issued by an accredited Family Dispute Resolution Practitioner to confirm that FDR was attempted for a parenting matter. You generally need one before you can file a parenting application in court — and we’re accredited to issue it."
    ),
    body_html=f"""
<h2 id="what-is">What is a Section 60I certificate?</h2>
<p>Named after the section of the {cite("family_law_act")} that creates the requirement, a Section 60I certificate is a formal document issued by an accredited Family Dispute Resolution Practitioner (FDRP). It records that the parties to a parenting dispute have either attempted dispute resolution, or that the matter wasn't suitable for it, or that one party refused to engage.</p>

<p>Without a certificate (or an exemption), the {cite("fcfcoa")} will not accept a parenting application. So if you've reached a stalemate on parenting and the only way forward is court, you need to come through Family Dispute Resolution first \u2014 and the certificate is the proof.</p>
""" + inline_cta("Need a Section 60I certificate so you can move forward? Book a consultation \u2014 we're accredited to issue them.") + """

<h2 id="when-required">When you need one</h2>

<figure class="tbl"><table><caption>Section 60I certificate \u2014 required vs not required</caption>
<thead><tr><th>Required</th><th>Not required</th></tr></thead>
<tbody>
<tr><td>Applying for a parenting order</td><td>Property or financial matters</td></tr>
<tr><td>Varying an existing parenting order</td><td>Divorce applications</td></tr>
<tr><td>&nbsp;</td><td>Matters covered by a recognised exemption</td></tr>
</tbody></table></figure>

<h2 id="types">The five certificate types</h2>
<p>The certificate doesn't say who's \"right\" \u2014 it records what happened. There are five recognised types under the Act:</p>

<figure class=\"tbl\"><table><caption>Section 60I certificate types</caption>
<thead><tr><th>Type</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>(a) Did not attend \u2014 other party refused</td><td>You attempted FDR; the other party refused or failed to attend.</td></tr>
<tr><td>(b) Did not attend \u2014 not appropriate</td><td>FDR was not appropriate (e.g. safety concerns, urgency).</td></tr>
<tr><td>(c) Made a genuine effort</td><td>Both parties attended and made a genuine effort to resolve.</td></tr>
<tr><td>(d) Did not make a genuine effort</td><td>One or both parties attended but did not genuinely try to resolve.</td></tr>
<tr><td>(e) Started but not appropriate to continue</td><td>FDR began but became inappropriate during the process.</td></tr>
</tbody></table></figure>

<p>The type matters: a (c) certificate (both made genuine effort) versus an (a) certificate (other party refused) tells the court a very different story.</p>

<h2 id="how">How we issue them</h2>
<ol>
  <li><strong>Initial intake</strong> \u2014 we meet with you, and separately with the other parent, to understand the situation and assess suitability for FDR.</li>
  <li><strong>FDR is attempted</strong> \u2014 we run the dispute resolution process. Many matters fully resolve here and never need a certificate.</li>
  <li><strong>If matters don't fully resolve</strong>, we issue the certificate \u2014 of the type that accurately reflects what happened.</li>
  <li><strong>The certificate is yours</strong> \u2014 valid for 12 months from the date of issue, you can file it with any court application.</li>
</ol>

<p>The role is regulated by the {cite("ag_fdr")}, and only accredited FDRPs can issue Section 60I certificates. Our team is accredited and issues them regularly.</p>
""" + inline_cta("Most matters resolve in mediation \u2014 the certificate is the backup if they don't. Either way, the process moves you forward.") + """

<h2 id="exemptions">Exemptions from the FDR requirement</h2>
<p>The Family Law Act recognises that mediation isn't appropriate in every situation. You may be exempt from needing a Section 60I certificate where:</p>
<ul>
  <li><strong>Family violence</strong> \u2014 there's been violence or risk of it</li>
  <li><strong>Child abuse</strong> \u2014 there's been abuse of a child or risk of it</li>
  <li><strong>Urgency</strong> \u2014 the matter is genuinely urgent</li>
  <li><strong>Incapacity</strong> \u2014 a party can't participate effectively (illness, location, etc.)</li>
  <li><strong>Serious breach of an existing order</strong> \u2014 there's been a serious breach within the last 12 months</li>
  <li><strong>Original consent orders sought</strong> \u2014 you're applying for orders that just formalise an agreement reached</li>
</ul>

<p>Exemptions aren't automatic \u2014 you need to satisfy the court that one applies. <a href=\"/is-family-law-mediation-compulsory/\">See the full exemption guide \u2192</a></p>

<h2 id="after">What happens after you get one</h2>
<p>Once issued, the certificate is valid for 12 months. You can file it with your parenting application. The court takes the certificate type into account in how it manages the matter:</p>
<ul>
  <li><strong>A type (c) certificate</strong> (both made genuine effort) shows the court FDR was tried in good faith. The matter moves to the next stage.</li>
  <li><strong>A type (a) or (d)</strong> (other party refused, or didn't make genuine effort) can affect how the court views the parties' conduct. It may have cost consequences too.</li>
</ul>

<h2 id="costs">Costs and timeframes</h2>
<p>If FDR resolves the matter, you've avoided court entirely \u2014 the certificate isn't issued because it isn't needed. The cost is the cost of mediation, typically $3,000\u2013$7,000 total (usually shared).</p>

<p>If matters don't fully resolve and a certificate is issued, the cost is essentially the same \u2014 the certificate is part of the FDR process, not an additional fee. From initial consultation to certificate (if needed) typically takes 4\u20138 weeks, depending on scheduling and how complex the issues are.</p>

<h2 id="get-started">Getting started</h2>
<p>The first step is a free initial consultation. We\u2019ll explain the process, assess whether FDR is appropriate, and outline how the certificate would be issued if needed. Most parenting matters resolve at mediation \u2014 the certificate is the backup, not the primary goal.</p>
""" + inline_cta("Ready to get started? Book a free consultation \u2014 we\u2019ll explain the process and what to expect.") + """
""",
    faq_items=[
        ("What is a Section 60I certificate?",
         "A document issued by an accredited Family Dispute Resolution Practitioner recording that you've attempted Family Dispute Resolution for a parenting matter. Required before you can file most parenting applications in court."),
        ("Who can issue a Section 60I certificate?",
         "Only an accredited Family Dispute Resolution Practitioner (FDRP), registered under the framework administered by the Attorney-General's Department. Not all mediators are FDRPs."),
        ("Do I need a Section 60I certificate for property matters?",
         "No \u2014 the requirement applies only to parenting matters. Property and financial matters have different pre-action requirements."),
        ("What are the exemptions from needing a certificate?",
         "Family violence or risk of it, child abuse or risk, urgency, inability to participate effectively, serious breach of an existing order, and applications for consent orders that formalise an existing agreement."),
        ("How long is a Section 60I certificate valid?",
         "12 months from the date of issue."),
        ("What if my ex won't attend mediation?",
         "If your former partner refuses or fails to attend, the practitioner can issue a type (a) certificate \u2014 \"did not attend, other party refused\" \u2014 which allows you to proceed to court."),
        ("Does a Section 60I certificate mean the court will decide in my favour?",
         "No \u2014 the certificate doesn't take sides. It records what happened in the FDR process. The court then assesses the parenting application on its merits."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("child-custody-mediation","Child Custody Mediation"),
        ("parenting-plan-mediation","Parenting Plan Mediation"),
        ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
        ("parenting-plans-guide","Parenting Plans Guide"),
        ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
        ("family-court-process","The Family Court Process"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
    bg_image="/assets/images/hero-section-60i-certificates.jpg",
    bg_pos="center 50%",
)


# ====================================================================
# 8. WORKPLACE MEDIATION
# ====================================================================
service_page(
    slug="workplace-mediation",
    title="Workplace Mediation in Australia | Mediations Australia",
    desc="Discuss a workplace dispute with an independent mediator. Explore suitability, the process, pricing and practical next steps for your organisation.",
    breadcrumb_label="Workplace Mediation",
    eyebrow="Workplace mediation",
    h1_html='Workplace mediation for <em>Australian organisations</em>',
    lede="Workplace mediation is a structured conversation in which an independent mediator helps people explore a workplace dispute and possible agreed ways forward. It is different from an investigation or a legal ruling. It starts with a suitability discussion, including safety, the people involved and any formal complaint or legal process already underway.",
    toc_items=[
        ("what-is","What is workplace mediation?"),
        ("disputes","Which disputes fit"),
        ("suitability","Suitability, and when another process comes first"),
        ("how","How the process works"),
        ("reporting","What the employer receives, and what stays private"),
        ("funding","Funding and independence"),
        ("dan","Meet Dan Toombs"),
        ("pricing","Pricing"),
        ("vs-fwc","Mediation and the Fair Work Commission"),
        ("sectors","Sectors we work with"),
        ("get-started","Confidential organisational enquiry"),
    ],
    takeaway=key_takeaway(
        "Workplace mediation is a voluntary process in which an independent mediator helps people in a workplace dispute "
        "talk through the issues and work towards their own practical agreement. The mediator does not investigate, decide "
        "who is right or impose an outcome. Mediations Australia's workplace mediation is $2,200 + GST for a half day or "
        "$3,800 + GST for a full day, covering two parties with intake for each."
    ),
    body_html=f"""
<h2 id="what-is">What is workplace mediation?</h2>
<p>Workplace mediation brings the people in a dispute together, with an independent mediator, to discuss what has happened and what would make working together workable again. It is voluntary, and the participants shape any agreement.</p>
<p>It helps to be precise about what it is <em>not</em>:</p>
<ul>
  <li><strong>Not an investigation.</strong> An investigator gathers evidence and makes findings of fact. A mediator does not.</li>
  <li><strong>Not a legal ruling.</strong> The mediator is not a judge, arbitrator or tribunal, and does not decide legal rights.</li>
  <li><strong>Not performance management or counselling.</strong> Those processes address one person's conduct or wellbeing, not a dispute between people.</li>
</ul>
<p>The Fair Work Commission and the Fair Work Ombudsman have their own roles in workplace disputes; see the {cite("fair_work")} for official information. Mediations Australia is a private provider and is not part of the Fair Work system.</p>
""" + inline_cta("Not sure whether mediation fits your situation? Start with a confidential suitability conversation.", btn="Discuss your workplace dispute", href="/contact-us/") + """

<h2 id="disputes">Which disputes fit</h2>
<p>Mediation tends to suit disputes where the people involved need to keep working together, or need to agree how they will part ways, and both are willing to take part.</p>
<ul>
  <li><p><strong>Manager–employee disputes.</strong> Disagreements about expectations, workload, feedback or how someone has been treated. The power imbalance matters: separate intake helps the mediator understand each person's position and whether a joint session is appropriate, and the organisation needs to have authority to implement any practical changes agreed.</p></li>
  <li><p><strong>Co-worker disputes.</strong> Communication breakdowns, overlapping roles, handover problems and working-style friction that has become personal. Mediation focuses on behaviour and practical arrangements, not on diagnosing personalities.</p></li>
  <li><p><strong>Leadership and executive conflict.</strong> Disputes within a leadership team or between a senior leader and a board or CEO.</p></li>
  <li><p><strong>Team conflict.</strong> Disputes involving several people. These are usually approached as facilitated multi-party work and quoted on request; see <a href="/team-conflict-facilitation/">team conflict facilitation</a>.</p></li>
  <li><p><strong>Restoring working relationships.</strong> For example after a restructure, a return from leave, or after an investigation has concluded but the relationships have not recovered.</p></li>
  <li><p><strong>Exits.</strong> Where an employment relationship is ending and the people involved want to agree terms. Independent legal advice is important here. See <a href="/employment-dispute-mediation/">employment dispute mediation</a>.</p></li>
</ul>
<p>Related services: <a href="/workplace-bullying-harassment-mediation/">bullying and harassment complaints</a>, <a href="/workplace-investigations-grievance-mediation/">investigations and grievances</a>, <a href="/unfair-dismissal-termination-mediation/">unfair dismissal and termination</a>, <a href="/partnership-executive-exit-mediation/">partnership and executive exits</a>.</p>

<h2 id="suitability">Suitability, and when another process comes first</h2>
<p>Mediation is not right for every workplace dispute. Before anything is booked, the mediator considers:</p>
<ul>
  <li><strong>Safety.</strong> Where there are allegations of violence, sexual harassment, threats or serious bullying, safety and any legal obligations come first. Mediation must never be used to suppress a complaint.</li>
  <li><strong>Whether facts need to be established.</strong> If serious allegations need findings, an investigation usually comes first. Mediation can help rebuild working relationships afterwards.</li>
  <li><strong>Deadlines and formal processes.</strong> Some claims have short statutory time limits. Arranging private mediation does not stop those clocks; check deadlines and get advice promptly. See the <a href="/workplace-dispute-guide/">workplace dispute guide</a>.</li>
  <li><strong>Willingness and capacity.</strong> Each person must agree to take part and be able to participate safely and genuinely.</li>
</ul>
<p>Our <a href="/is-mediation-right-for-workplace-dispute/">suitability guide</a> walks through these questions in more detail.</p>

<h2 id="how">How the process works</h2>
<ol>
  <li><p><strong>Referral.</strong> An employer (usually HR, a manager, the CEO or the board), the parties jointly, or one party can make contact. We clarify who is commissioning the mediation and who will receive what information before anything starts.</p></li>
  <li><p><strong>Separate intake.</strong> The mediator speaks with each participant separately to understand their perspective, their goals and any concerns about safety or participation. Intake with each party is included in the fee.</p></li>
  <li><p><strong>Participation and support.</strong> Whether a support person or representative attends is discussed at intake and agreed in advance.</p></li>
  <li><p><strong>The mediation session.</strong> Usually a joint session, in person or online. Where direct contact is not appropriate, the mediator can work with each person separately (shuttle mediation).</p></li>
  <li><p><strong>Agreed actions.</strong> If the participants reach agreement, the practical commitments are written down in plain language.</p></li>
  <li><p><strong>Review.</strong> Where useful, a later check-in confirms whether the arrangements are working.</p></li>
</ol>

<h2 id="reporting">What the employer receives, and what stays private</h2>
<p>Confidentiality is what allows people to speak candidly, but it is not absolute and it should never be assumed. Before intake, the commissioning organisation and the participants agree in writing:</p>
<ul>
  <li>what, if anything, will be reported back to the employer (often only whether the mediation went ahead and any agreed actions the participants consent to share);</li>
  <li>how notes and records are handled;</li>
  <li>the limits of confidentiality, for example where there is a risk to someone's safety or a legal obligation to disclose.</li>
</ul>
<p>Whether discussions in mediation can later be used in legal proceedings depends on the law and the circumstances, so get legal advice if that matters to you. We do not promise blanket legal privilege.</p>

<h2 id="funding">Funding and independence</h2>
<p>Most workplace mediations are paid for by the employer. Paying does not buy an outcome: the mediator is independent of all participants, including the organisation that pays, and does not take instructions about what the result should be. This is explained to every participant at intake.</p>
""" + inline_cta("Want to talk through a dispute in confidence before deciding anything?", btn="Discuss your workplace dispute", href="/contact-us/") + f"""

<h2 id="dan">Meet Dan Toombs</h2>
<div style="display:flex;gap:1.25rem;align-items:flex-start;flex-wrap:wrap;padding:1.25rem;border:1px solid var(--line);border-radius:12px;background:var(--cream)">
<img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder and Mediator, Mediations Australia" width="96" height="96" loading="lazy" style="border-radius:50%;object-fit:cover;width:96px;height:96px;flex-shrink:0">
<div style="flex:1;min-width:220px">
<p style="margin:0 0 .5rem">Dan Toombs is the Founder of Mediations Australia and an <strong>AMDRAS-accredited mediator</strong>. His experience includes serving as a <strong>Member of the Guardianship and Administration Tribunal (Queensland)</strong>, whose jurisdiction is now within QCAT, leading a community legal centre as <strong>CEO</strong>, and serving as a <strong>Board Director of Legal Aid Queensland</strong>. He is an <strong>Accredited Belbin Team Roles Facilitator</strong> and has trained in Adaptive Leadership through the Australian Adaptive Leadership Institute.</p>
<p style="margin:0 0 .5rem">Dan has mediated workplace disputes across professional services, healthcare, education, construction, and the not-for-profit sector.</p>
<p style="margin:0"><a href="/our-team/dan-toombs/">View Dan's profile →</a> · <a href="/belbin-team-roles-training/">Belbin Team Roles training</a></p>
</div></div>
<p>Dan's tribunal experience gives him an adjudicator's perspective for reality-testing options, and his leadership and governance background is relevant to manager, executive and board disputes. Who mediates a particular matter depends on suitability and availability, which we confirm when you get in touch.</p>

<h2 id="pricing">Pricing</h2>
{WP_PRICE_BLOCK}
<p>The full breakdown, including examples with additional parties, is on our <a href="/workplace-mediation-cost/">workplace mediation cost</a> page. These are Mediations Australia's fees, not an industry average.</p>

<h2 id="vs-fwc">Mediation and the Fair Work Commission</h2>
<p>The Fair Work Commission deals with certain formal claims, such as unfair dismissal and general protections disputes, and has its own conciliation processes. Private mediation is different: it is arranged by agreement, usually earlier, and is not a substitute for the Commission where a formal claim is needed.</p>
<figure class="tbl"><table><caption>Private workplace mediation and Fair Work Commission processes</caption>
<thead><tr><th></th><th>Private workplace mediation</th><th>Fair Work Commission</th></tr></thead>
<tbody>
<tr><td>Who arranges it</td><td>The employer and/or participants, by agreement</td><td>Usually starts when a formal application is lodged</td></tr>
<tr><td>Typical timing</td><td>Early, often before formal claims</td><td>After an application, within statutory time limits</td></tr>
<tr><td>Who decides the outcome</td><td>The participants, by agreement</td><td>Conciliation by agreement; some matters can be determined by the Commission</td></tr>
<tr><td>Deadlines</td><td>Does not stop statutory time limits</td><td>Strict filing deadlines apply to some claims</td></tr>
</tbody></table></figure>
<p>If a claim deadline may apply, get advice straight away. <a href="/workplace-dispute-guide/">See the workplace dispute guide →</a></p>

<h2 id="sectors">Sectors we work with</h2>
<p>We work with organisations of different sizes and structures, including:</p>
<ul>
  <li><strong>Not-for-profits and NGOs</strong>, where conflict can affect staff, governance and service delivery. <a href="/ngo-not-for-profit-mediation/">NGO and not-for-profit workplace mediation →</a></li>
  <li><strong>Small businesses</strong> without an HR team, including where the owner is one of the people in the dispute. Neutral, external commissioning matters here, and the fee structure is the same.</li>
  <li><strong>Health and education</strong>, where professional hierarchies and service continuity matter. Mediation never overrides patient or student safety processes or mandatory reporting.</li>
  <li><strong>Professional services and construction</strong>, including partner, project-team and site-leadership disputes.</li>
</ul>

<h2 id="get-started">Confidential organisational enquiry</h2>
<p>The first step is a confidential conversation about suitability. Please don't include sensitive details about individuals in an online form; we will discuss the situation with you directly. There is no obligation, and we will tell you honestly if another process would serve you better.</p>
""",
    faq_items=[
        ("What is workplace mediation?",
         "A voluntary process in which an independent mediator helps people in a workplace dispute discuss the issues and work towards their own agreement. The mediator does not investigate, decide who is right or make a legal ruling."),
        ("Who can arrange workplace mediation?",
         "Usually an employer, through HR, a manager, the CEO or the board. Participants can also arrange it jointly, or one party can make contact and we will ask the other whether they are willing to take part. Everyone must agree to participate."),
        ("Does the employer paying affect neutrality?",
         "No. Most workplace mediations are paid for by the employer, but the mediator is independent of everyone, including the organisation that pays, and does not take instructions about the outcome. This is explained to each participant at intake."),
        ("Can a support person attend?",
         "Often, yes. Whether a support person or representative attends, and what their role is, is discussed at intake and agreed before the session so everyone knows who will be present."),
        ("What is reported to the employer?",
         "Only what is agreed in writing before intake. Often that is whether the mediation went ahead and any agreed actions the participants consent to share. Confidentiality has limits, such as safety risks or legal obligations, which are explained in advance."),
        ("When is an investigation needed instead?",
         "Where serious allegations need findings of fact, or there are safety concerns or legal obligations to respond, an investigation or other formal process usually comes first. Mediation can help rebuild working relationships afterwards."),
        ("How much does workplace mediation cost?", WP_FAQ["cost"]),
        ("Are the prices per person?", WP_FAQ["per_person"]),
    ],
    related_items=[
        ("workplace-mediation-cost","Workplace Mediation Cost"),
        ("workplace-mediation-guide","Workplace Mediation: Complete Guide"),
        ("is-mediation-right-for-workplace-dispute","Is Mediation Right for a Workplace Dispute?"),
        ("workplace-dispute-guide","Workplace Dispute Guide"),
        ("workplace-bullying-harassment-mediation","Bullying & Harassment Mediation"),
        ("workplace-investigations-grievance-mediation","Investigations & Grievances"),
        ("ngo-not-for-profit-mediation","NGO & Not-for-Profit Mediation"),
        ("our-team/dan-toombs","Dan Toombs"),
    ],
    bg_image="/assets/images/hero-workplace-mediation.jpg",
    bg_pos="center 50%",
    offers=offers_schema("workplace-mediation"),
)


# ====================================================================
# 9. ONLINE DIVORCE / ONLINE MEDIATION
# ====================================================================
service_page(
    slug="online-divorce",
    title="Online Divorce & Online Mediation in Australia | Mediations Australia",
    desc="Resolve your separation by secure video from anywhere in Australia. Online mediation works just as effectively as in-person \u2014 and removes distance, scheduling, and travel as obstacles.",
    breadcrumb_label="Online Divorce",
    eyebrow="End it cleanly, from wherever you are",
    h1_html='Online Divorce &amp; Mediation \u2014 <em>resolve it from anywhere</em>.',
    lede="The whole process \u2014 mediation, agreement, formalisation \u2014 can run online. From regional Australia, from interstate, from overseas if needed. Secure video, accredited mediators, full legal effect. The only difference is you skip the drive.",
    toc_items=[
        ("what-is","What is online mediation?"),
        ("works","How well does it actually work?"),
        ("when","When online suits best"),
        ("how","How the process runs"),
        ("technology","The technology"),
        ("regional","For regional and remote Australia"),
        ("costs","Costs"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Online mediation runs the same process as in-person mediation \u2014 same accredited mediators, same legal effect, same outcomes \u2014 by secure video conference. It's particularly suited to regional and remote Australia, to interstate partners, to busy schedules, and to high-conflict matters where being in the same physical space adds heat. Most family law mediations work equally well online or in person."
    ),
    body_html=f"""
<h2 id="what-is">What is online mediation?</h2>
<p>Online mediation is family law mediation conducted by secure video conference rather than in a physical room. The accredited mediator, you, and your former partner all join from your own locations. The process is otherwise identical: same structured stages, same legal effect, same kind of outcomes.</p>

<p>It moved from emergency adaptation to mainstream practice over the past several years. Today it's the default for many separating couples \u2014 particularly where partners live in different places, where travel is impractical, or where being in the same physical room would add unhelpful intensity.</p>
""" + inline_cta("Live in regional Australia, or in different places? Online mediation removes distance as an obstacle entirely.") + """

<h2 id="works">How well does it actually work?</h2>
<p>Honestly: at least as well as in-person, and for some matters better. Research and practice both bear this out.</p>

<p>What works equally well online:</p>
<ul>
  <li>The structured dispute resolution process itself</li>
  <li>Document sharing and review</li>
  <li>Drafting heads of agreement in real time</li>
  <li>Shuttle mediation (separate \"rooms\" are easier online than in person)</li>
  <li>Getting independent advice in parallel</li>
</ul>

<p>What's different (not worse):</p>
<ul>
  <li>You can't read body language as fully \u2014 but you also don't get the in-person tension that can derail conversations</li>
  <li>The mediator works harder to manage turn-taking \u2014 but does so reliably</li>
  <li>You need a quiet space at your end \u2014 which means you have to set up to focus</li>
</ul>

<h2 id="when">When online suits best</h2>
<ul>
  <li><strong>Regional or remote Australia</strong> \u2014 access to accredited specialists without the travel</li>
  <li><strong>Interstate partners</strong> \u2014 one in Sydney, one in Perth; no flights needed</li>
  <li><strong>Australians overseas</strong> \u2014 a partner who's moved abroad can still mediate the Australian matter</li>
  <li><strong>Busy schedules</strong> \u2014 no half-day lost to travel and a return trip</li>
  <li><strong>High-conflict matters</strong> \u2014 the physical distance often reduces emotional charge</li>
  <li><strong>Childcare logistics</strong> \u2014 you can do it while kids are at school without arranging a sitter</li>
  <li><strong>Safety concerns</strong> \u2014 where being in the same building isn't appropriate</li>
</ul>

<h2 id="how">How the process runs</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 by video, no different from any other consultation.</li>
  <li><strong>Intake</strong> \u2014 each party meets the mediator separately by video.</li>
  <li><strong>Document gathering and disclosure</strong> \u2014 shared electronically through secure channels.</li>
  <li><strong>The mediation session</strong> \u2014 by video, typically a half or full day. Joint session, or with each party in a separate \"room\" (shuttle mediation) where appropriate.</li>
  <li><strong>Heads of Agreement</strong> \u2014 drafted live in a shared document.</li>
  <li><strong>Formalisation</strong> \u2014 consent orders or BFA, also handled online.</li>
</ol>

<h2 id="technology">The technology</h2>
<p>We use secure, encrypted video conferencing. You don't need any specialist software \u2014 a modern laptop, tablet or smartphone is fine. We send a meeting link; you click and join. The technology should be invisible.</p>

<p>Documents are shared through secure channels with appropriate access controls. Nothing sensitive travels by email attachment unless you specifically want it that way.</p>
""" + inline_cta("Distance shouldn't be the reason your matter doesn't resolve. It isn't, with online mediation.") + """

<h2 id="regional">For regional and remote Australia</h2>
<p>Access to accredited family law specialists is uneven across Australia. Online mediation closes that gap entirely. Whether you're in a regional town, on a property hours from the nearest courthouse, or in a remote community, you get the same accredited mediators, the same process, and the same legal effect as someone in central Sydney.</p>

<p>It also opens up choice. Rather than working with whoever's nearest, you can work with the mediator best suited to your matter \u2014 whether that's a specialist in high-conflict matters, business assets, or something specific to your situation.</p>

<h2 id="costs">Costs</h2>
<p>Online mediation costs the same or slightly less than in-person. There's no travel time built into the fees, and no venue costs. Typical total: $3,000\u2013$7,000 (shared between the parties), depending on complexity.</p>

<h2 id="get-started">Getting started</h2>
<p>The first step is a free initial online consultation. We'll listen to your situation, assess whether mediation is the right path, and outline the process. The first conversation alone usually clarifies a lot.</p>
""",
    faq_items=[
        ("Does online mediation work as well as in-person?",
         "Yes \u2014 for most family law matters, equally well or better. The structured process translates fully to video; document sharing is easier; shuttle mediation (separate rooms) is more natural online; and the physical distance often reduces emotional charge."),
        ("What technology do I need?",
         "A modern laptop, tablet or smartphone, a reasonable internet connection, and a quiet space. We use secure video conferencing \u2014 you click a link to join, no specialist software needed."),
        ("Is online mediation as legally valid as in-person?",
         "Yes. The legal effect is identical. Agreements reached online can be formalised through consent orders or a binding financial agreement in exactly the same way."),
        ("Can I do online mediation from overseas?",
         "Yes. Many Australians live overseas and resolve Australian family law matters through online mediation. Time zones need to be worked around but otherwise it's straightforward."),
        ("Is online mediation secure?",
         "We use encrypted video conferencing and secure document-sharing channels with appropriate access controls. Confidentiality is the same as for any mediation \u2014 protected by the mediation framework."),
        ("How much does online mediation cost?",
         "The same or slightly less than in-person \u2014 typically $3,000\u2013$7,000 total, usually shared between the parties."),
        ("Can high-conflict matters be mediated online?",
         "Often particularly well. Shuttle mediation (separate \"rooms\") is more natural online than in person, and the physical distance reduces the emotional intensity of being together."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("how-to-get-a-divorce-in-australia-a-step-by-step-guide","How to Get a Divorce"),
        ("how-mediation-works","How Mediation Works"),
        ("shuttle-mediation-guide","Shuttle Mediation"),
        ("preparing-for-mediation","Preparing for Mediation"),
        ("cost-of-divorce-in-australia","Cost of Divorce"),
        ("high-conflict-mediation","High-Conflict Mediation"),
        ("divorce-without-a-lawyer","Divorce Without a Lawyer"),
    ],
    bg_image="/assets/images/hero-online-divorce-mediation.jpg",
    bg_pos="center 50%",
)

print("\nBatch 2 service cornerstones built (5 pages).")
