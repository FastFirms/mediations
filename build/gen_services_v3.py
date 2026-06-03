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
from gen_services_v2 import inline_cta, key_takeaway, callout, toc, related_grid, service_page

# ====================================================================
# 4. PARENTING PLAN MEDIATION
# ====================================================================
service_page(
    slug="parenting-plan-mediation",
    title="Parenting Plan Mediation in Australia | Mediations Australia",
    desc="Build a workable parenting plan through accredited mediation. Child-focused arrangements, faster than court, with the option to make it legally binding via consent orders.",
    breadcrumb_label="Parenting Plan Mediation",
    eyebrow="Service",
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
""" + inline_cta("Whether you need a parenting plan, consent orders, or both \u2014 we'll work it out with you. Book a free consultation.") + """

<h2 id="get-started">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll listen to your situation, assess whether mediation is the right path for your family, and outline what's involved. Most parenting plan mediations are resolved in one or two sessions \u2014 a matter of weeks, not the years a contested matter can take.</p>

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
)


# ====================================================================
# 5. CONSENT ORDERS
# ====================================================================
service_page(
    slug="consent-orders",
    title="Consent Orders in Australia | Mediations Australia",
    desc="Make your mediated agreement legally binding through consent orders. How they work, what they cost, how long they take \u2014 with accredited support through the full process.",
    breadcrumb_label="Consent Orders",
    eyebrow="Service",
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
)


# ====================================================================
# 6. FINANCIAL AGREEMENTS MEDIATION (BFAs)
# ====================================================================
service_page(
    slug="financial-agreements-mediation",
    title="Binding Financial Agreements (BFAs) | Mediations Australia",
    desc="Reach a binding financial agreement through accredited mediation. How BFAs work, when they're appropriate, and how to make yours hold up. Free consultation.",
    breadcrumb_label="Financial Agreements",
    eyebrow="Service",
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
<p>The first step is a fixed-fee consultation. We'll listen to your situation, assess whether a BFA is the right instrument (vs consent orders or another path), and outline the process and timeline. If you proceed, we mediate the substance, handle the drafting, and ensure the formal requirements are met so the agreement actually holds.</p>
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
)


# ====================================================================
# 7. SECTION 60I CERTIFICATES
# ====================================================================
service_page(
    slug="section-60i-certificates",
    title="Section 60I Certificates in Australia | Mediations Australia",
    desc="Get a Section 60I certificate from an accredited Family Dispute Resolution Practitioner. Required before parenting court applications under the Family Law Act. Free consultation.",
    breadcrumb_label="Section 60I Certificates",
    eyebrow="Service",
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
        "A Section 60I certificate is the document an accredited Family Dispute Resolution Practitioner (FDRP) issues to record that you've attempted Family Dispute Resolution for a parenting matter. You generally need one before you can file a parenting application in court, unless an exemption applies. There are five certificate types, depending on what actually happened in the FDR process. We're accredited to issue them."
    ),
    body_html=f"""
<h2 id="what-is">What is a Section 60I certificate?</h2>
<p>Named after the section of the {cite("family_law_act")} that creates the requirement, a Section 60I certificate is a formal document issued by an accredited Family Dispute Resolution Practitioner (FDRP). It records that the parties to a parenting dispute have either attempted dispute resolution, or that the matter wasn't suitable for it, or that one party refused to engage.</p>

<p>Without a certificate (or an exemption), the {cite("fcfcoa")} will not accept a parenting application. So if you've reached a stalemate on parenting and the only way forward is court, you need to come through Family Dispute Resolution first \u2014 and the certificate is the proof.</p>
""" + inline_cta("Need a Section 60I certificate so you can move forward? Book a consultation \u2014 we're accredited to issue them.") + """

<h2 id="when-required">When you need one</h2>
<p>You need a Section 60I certificate (or a valid exemption) before you can file:</p>
<ul>
  <li>An application for a parenting order</li>
  <li>An application to vary an existing parenting order (with some exceptions)</li>
</ul>

<p>You do NOT need a Section 60I certificate for:</p>
<ul>
  <li>Property or financial matters \u2014 they have different pre-action requirements</li>
  <li>Divorce applications</li>
  <li>Matters that fall within a recognised exemption (see below)</li>
</ul>

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
<p>The first step is a fixed-fee consultation. We'll explain the process, assess whether FDR is appropriate for your situation, and outline how the certificate would be issued if needed. Most parenting matters resolve at FDR \u2014 the certificate is the backup, not the primary goal.</p>
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
)


# ====================================================================
# 8. WORKPLACE MEDIATION
# ====================================================================
service_page(
    slug="workplace-mediation",
    title="Workplace Mediation in Australia | Mediations Australia",
    desc="Resolve workplace disputes through accredited mediation \u2014 before they reach the Fair Work Commission. Confidential, fast, and constructive. Free consultation.",
    breadcrumb_label="Workplace Mediation",
    eyebrow="Service",
    h1_html='Workplace Mediation \u2014 <em>resolve it before the FWC</em>.',
    lede="Workplace conflict costs businesses far more than the dispute itself \u2014 in lost productivity, damaged teams, and the eye-watering price of letting things escalate to formal proceedings. Mediation resolves conflict early, confidentially, and in a way that lets working relationships continue.",
    toc_items=[
        ("what-is","What is workplace mediation?"),
        ("disputes","What disputes we resolve"),
        ("how","How the process works"),
        ("benefits","The benefits for employers"),
        ("benefits-staff","The benefits for staff"),
        ("vs-fwc","Mediation vs the Fair Work Commission"),
        ("costs","Costs and timeframes"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Workplace mediation is a confidential, voluntary process where a neutral mediator helps people in a workplace dispute reach a practical resolution. It resolves conflict between colleagues, between staff and management, or following a bullying or harassment complaint \u2014 typically in a single session, far faster and cheaper than a formal grievance process or Fair Work Commission application. The mediator doesn't impose an outcome; the participants shape the agreement."
    ),
    body_html=f"""
<h2 id="what-is">What is workplace mediation?</h2>
<p>Workplace mediation applies the same principles as family law mediation to disputes in the workplace: a neutral, accredited mediator helps the people involved talk through the issues and reach a practical, agreed resolution. It's confidential, it's voluntary, and the mediator doesn't take sides or impose an outcome.</p>

<p>Used early \u2014 ideally before a dispute has hardened into formal complaints or escalated to the {cite("fair_work")} \u2014 it's the most cost-effective and least disruptive way to resolve workplace conflict.</p>
""" + inline_cta("Workplace conflict draining your team? Bring in a neutral mediator before it escalates. Talk to us.") + """

<h2 id="disputes">What disputes we resolve</h2>
<p>The pattern of disputes we see covers most common workplace conflicts:</p>
<ul>
  <li><strong>Interpersonal conflict</strong> between colleagues or within a team</li>
  <li><strong>Manager\u2013staff disputes</strong> \u2014 expectations, performance, treatment</li>
  <li><strong>Communication breakdowns</strong> following organisational change, restructure, or new leadership</li>
  <li><strong>Bullying, harassment or grievance complaints</strong> \u2014 either informally raised or formally lodged</li>
  <li><strong>Disputes about roles, responsibilities or workload</strong></li>
  <li><strong>Conflict following return to work</strong> \u2014 after leave, injury, or workplace investigation</li>
  <li><strong>Discrimination complaints</strong> at an early stage</li>
  <li><strong>End-of-employment disputes</strong> \u2014 before they become unfair dismissal claims</li>
</ul>

<h2 id="how">How the process works</h2>
<ol>
  <li><strong>Referral and confidentiality</strong> \u2014 the workplace (or the parties) refers the matter; everyone confirms agreement to participate and to confidentiality.</li>
  <li><strong>Individual intake meetings</strong> \u2014 the mediator meets each person separately to understand the situation, what they want from the process, and any sensitivities.</li>
  <li><strong>The mediation session</strong> \u2014 the parties work through the issues with the mediator's guidance. Either joint session, or shuttle mediation (mediator moves between rooms) where the dynamics suit it better.</li>
  <li><strong>Reaching agreement</strong> \u2014 practical commitments are agreed and documented in plain language.</li>
  <li><strong>Follow-up</strong> \u2014 sometimes a check-in confirms the arrangements are working.</li>
</ol>

<p>Most workplace matters resolve in a single session. The whole process \u2014 from referral to documented agreement \u2014 typically takes two to four weeks.</p>

<h2 id="benefits">The benefits for employers</h2>
<ul>
  <li><strong>Cost</strong> \u2014 a fraction of what formal grievance investigations, Fair Work proceedings, or staff turnover cost</li>
  <li><strong>Speed</strong> \u2014 weeks rather than months</li>
  <li><strong>Confidentiality</strong> \u2014 protects the business, the team, and individual reputations</li>
  <li><strong>Retention</strong> \u2014 resolves the underlying problem rather than just losing a good employee</li>
  <li><strong>Preserves working relationships</strong> \u2014 critical where the parties have to continue working together</li>
  <li><strong>Reduces legal risk</strong> \u2014 a well-resolved dispute doesn't escalate to formal claims</li>
  <li><strong>Cultural signal</strong> \u2014 shows the business takes conflict seriously and resolves it constructively</li>
</ul>
""" + callout("Workplace conflict is more expensive than people realise",
   "Research consistently puts the cost of unresolved workplace conflict at thousands of dollars per employee per year \u2014 in lost productivity, sickness absence, and turnover. Mediation typically pays for itself many times over.") + """

<h2 id="benefits-staff">The benefits for staff</h2>
<ul>
  <li><strong>Voice</strong> \u2014 a chance to be heard in a structured, safe way</li>
  <li><strong>Confidentiality</strong> \u2014 candour without fear it'll be used against you later</li>
  <li><strong>Outcome you can live with</strong> \u2014 you help shape the resolution, not have one imposed</li>
  <li><strong>Avoids the trauma</strong> of formal proceedings or a Fair Work hearing</li>
  <li><strong>Faster closure</strong> \u2014 weeks not months of uncertainty</li>
  <li><strong>Preserves your professional reputation</strong> \u2014 no public record of conflict</li>
</ul>

<h2 id="vs-fwc">Mediation vs the Fair Work Commission</h2>
<p>The Fair Work Commission offers conciliation for certain workplace matters \u2014 unfair dismissal, general protections disputes, some others. It's a valuable formal process. But many workplace conflicts are better resolved <em>before</em> they become formal Fair Work matters:</p>

<figure class=\"tbl\"><table><caption>Workplace mediation vs Fair Work proceedings</caption>
<thead><tr><th></th><th>Workplace mediation</th><th>Fair Work Commission</th></tr></thead>
<tbody>
<tr><td>When</td><td>Early \u2014 before formal claims</td><td>After a claim is lodged</td></tr>
<tr><td>Cost</td><td>Single fee, often days of work</td><td>Significant time, often legal fees</td></tr>
<tr><td>Time</td><td>Weeks</td><td>Months</td></tr>
<tr><td>Outcome</td><td>Parties shape the agreement</td><td>Conciliated or arbitrated decision</td></tr>
<tr><td>Privacy</td><td>Completely confidential</td><td>Some matters become public</td></tr>
<tr><td>Working relationship</td><td>Often preserved</td><td>Often broken by then</td></tr>
</tbody></table></figure>

<p>Mediation isn't a replacement for Fair Work proceedings where they're appropriate \u2014 it's a way to avoid needing them. <a href=\"/workplace-mediation-guide/\">See the full workplace mediation guide \u2192</a></p>
""" + inline_cta("Early mediation is dramatically cheaper than letting things escalate. We respond fast.") + """

<h2 id="costs">Costs and timeframes</h2>
<p>Workplace mediation is typically billed as a single fixed fee covering the intake, the session, and the documented agreement. Costs depend on complexity but are usually a single-figure thousands rather than the tens of thousands a formal grievance investigation or Fair Work matter can run.</p>

<p>Timing is fast: most matters are scheduled within a week or two of referral, and resolved in a single session. The whole process from referral to documented resolution typically completes inside a month.</p>

<h2 id="get-started">Getting started</h2>
<p>The first step is a confidential conversation. We can be engaged by the employer, by the parties jointly, or sometimes by one party where the other later agrees. We'll listen, assess whether mediation is right for the situation, and outline a clear path forward. The conversation itself is confidential and obligation-free.</p>
""",
    faq_items=[
        ("What is workplace mediation?",
         "A confidential, voluntary process where a neutral mediator helps people in a workplace dispute reach a practical agreed resolution. The mediator doesn't take sides or impose an outcome \u2014 the participants shape it."),
        ("What kinds of workplace disputes can be mediated?",
         "Interpersonal conflict between colleagues or teams, manager\u2013staff disputes, communication breakdowns, bullying or harassment complaints, disputes about roles or workload, and many end-of-employment situations."),
        ("Is workplace mediation confidential?",
         "Yes. Confidentiality is what lets participants speak honestly without fear it will be used against them later \u2014 and it's often what unlocks a resolution that formal processes can't."),
        ("How is it different from a Fair Work Commission process?",
         "Mediation typically happens early \u2014 before formal claims. It's faster, cheaper, more private, and lets parties shape their own outcome. Fair Work processes are valuable but more formal, slower, and often more adversarial."),
        ("How long does workplace mediation take?",
         "Most matters resolve in a single session, with the whole process \u2014 referral, intake, session, agreement \u2014 typically completing inside a month."),
        ("Who pays for workplace mediation?",
         "Usually the employer, particularly where they've initiated the referral. Sometimes the cost is shared, or one party pays. The mediator clarifies this at the start."),
        ("What if mediation doesn't resolve the dispute?",
         "The parties retain all their other options \u2014 formal grievance, Fair Work, legal action. Anything discussed in mediation stays confidential and generally can't be used in those later processes."),
    ],
    related_items=[
        ("workplace-mediation-guide","Workplace Mediation: Complete Guide"),
        ("conciliation-vs-mediation","Conciliation vs Mediation"),
        ("how-mediation-works","How Mediation Works"),
        ("estate-dispute-mediation","Estate Dispute Mediation"),
        ("family-law-arbitration","Family Law Arbitration"),
        ("what-is-mediation-in-family-law","What Is Mediation?"),
        ("preparing-for-mediation","Preparing for Mediation"),
        ("about-mediations-australia","About Mediations Australia"),
    ],
)


# ====================================================================
# 9. ONLINE DIVORCE / ONLINE MEDIATION
# ====================================================================
service_page(
    slug="online-divorce",
    title="Online Divorce & Online Mediation in Australia | Mediations Australia",
    desc="Resolve your separation by secure video from anywhere in Australia. Online mediation works just as effectively as in-person \u2014 and removes distance, scheduling, and travel as obstacles.",
    breadcrumb_label="Online Divorce",
    eyebrow="Service",
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
<p>The first step is a fixed-fee online consultation. We'll listen to your situation, assess whether mediation is the right path, and outline the process. The first conversation alone usually clarifies a lot.</p>
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
)

print("\nBatch 2 service cornerstones built (5 pages).")
