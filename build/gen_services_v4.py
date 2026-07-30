#!/usr/bin/env python3
"""Batch 3 — remaining service pages and blog top-ups.

Same cornerstone depth and structure, generated from compact data definitions
to stay reliable across many pages. Each is ~1,400-1,700 words with the full
component pattern: keyword-first H1, key-takeaway, TOC, 7+ sections,
inline CTAs, FAQ schema, related grid.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)
from authority_sources import cite
from gen_services_v2 import inline_cta, key_takeaway, callout, toc, related_grid, service_page


# ====================================================================
# 10. SPOUSAL SUPPORT MEDIATION
# ====================================================================
service_page(
    slug="spousal-support-mediation",
    title="Spousal Support Mediation in Australia | Mediations Australia",
    desc="Resolve spousal maintenance through accredited mediation \u2014 fair financial support after separation, agreed privately without court. Free consultation.",
    breadcrumb_label="Spousal Support Mediation",
    eyebrow="Service",
    h1_html='Spousal Support Mediation \u2014 <em>fair support, agreed not imposed</em>.',
    lede="Spousal maintenance is the financial support one former partner pays the other where the recipient can't reasonably meet their own needs. Mediation lets you reach a sensible agreement on amount, duration, and form \u2014 tailored to your situation rather than left to a court.",
    toc_items=[
        ("what-is","What is spousal maintenance?"),
        ("eligible","Who's eligible"),
        ("how-much","How much, and how long"),
        ("process","The mediation process"),
        ("forms","Lump sum, periodic, or in-kind"),
        ("vs-csa","Spousal maintenance vs child support"),
        ("binding","Making the agreement binding"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Spousal maintenance is financial support one former partner pays the other where the recipient can't adequately meet their own reasonable needs and the payer has the capacity to pay. Unlike child support, there's no fixed formula \u2014 amount, duration and form are negotiable. Mediation produces faster, fairer outcomes than court, and the agreement is then formalised through consent orders or a binding financial agreement."
    ),
    body_html=f"""
<h2 id="what-is">What is spousal maintenance?</h2>
<p>Spousal maintenance is financial support paid by one former partner to the other after separation. It's separate from child support, separate from the property settlement, and governed by the {cite("family_law_act")}. The principle behind it is straightforward: where one partner genuinely can't meet their own reasonable needs, and the other has the capacity to help, support should be paid.</p>

<p>It's not automatic, not punitive, and not common in every separation \u2014 but where it applies, it can be the difference between a fair transition and one that leaves one partner stranded.</p>
""" + inline_cta("Wondering if you can claim, or might have to pay, spousal maintenance? Get clarity in a consultation.") + """

<h2 id="eligible">Who's eligible</h2>
<p>Eligibility turns on two questions, working together:</p>
<ul>
  <li><strong>Need</strong> \u2014 can the applicant reasonably meet their own living expenses from their own income and resources?</li>
  <li><strong>Capacity</strong> \u2014 can the other party afford to pay, after meeting their own reasonable needs?</li>
</ul>
<p>Both must be satisfied. Courts also consider age, health, income, earning capacity, the care of children, and the standard of living during the relationship. <a href=\"/spousal-maintenance-guide/\">See the full spousal maintenance guide \u2192</a></p>

<h2 id="how-much">How much, and how long</h2>
<p>Unlike child support, there's no formula. The amount reflects the gap between the recipient's reasonable needs and their own capacity to meet them, limited by the payer's ability to pay. It can be a lump sum, regular periodic payments, or a combination.</p>

<p>Duration varies too. Often spousal maintenance is time-limited \u2014 supporting the recipient while they retrain, re-enter the workforce, or move toward self-sufficiency. It can be reviewed if circumstances change significantly, and it generally ends if the recipient remarries. Permanent maintenance is uncommon and usually reserved for cases of age or incapacity.</p>

<h2 id="process">The mediation process</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 we understand both situations.</li>
  <li><strong>Full financial disclosure</strong> \u2014 income, expenses, assets, capacity.</li>
  <li><strong>Pre-mediation intake</strong> \u2014 separate sessions with each party.</li>
  <li><strong>The mediation session</strong> \u2014 working through need, capacity, and the right form of support.</li>
  <li><strong>Documented agreement</strong> \u2014 amount, duration, form, and review provisions.</li>
  <li><strong>Formalisation</strong> \u2014 consent orders or binding financial agreement.</li>
</ol>
""" + callout("Spousal maintenance isn't about punishment \u2014 it's about practical transition",
   "The goal is to enable a financially weaker partner to transition to self-sufficiency, not to penalise the payer indefinitely. A well-mediated agreement reflects this reality.") + """

<h2 id="forms">Lump sum, periodic, or in-kind</h2>
<p>Mediation lets you craft the right form of support, not just the amount:</p>
<ul>
  <li><strong>Lump sum</strong> \u2014 a one-off payment, often from the property pool. Provides finality.</li>
  <li><strong>Periodic</strong> \u2014 regular weekly, fortnightly or monthly payments. Often time-limited.</li>
  <li><strong>In-kind</strong> \u2014 covering specific expenses like rent, school fees, or a mortgage. Less common but sometimes practical.</li>
  <li><strong>Mixed</strong> \u2014 a combination, e.g. a lump sum plus periodic payments for a period.</li>
</ul>

<h2 id="vs-csa">Spousal maintenance vs child support</h2>
<p>People conflate these but they're entirely separate:</p>
<ul>
  <li><strong>Child support</strong> is for the children's costs, calculated by a formula administered by Services Australia.</li>
  <li><strong>Spousal maintenance</strong> is for an adult partner's own support, assessed on need and capacity.</li>
</ul>
<p>You can be entitled to one, both, or neither. <a href=\"/child-support-mediation/\">See child support mediation \u2192</a></p>
""" + inline_cta("Spousal maintenance is rarely clear-cut. Let us help you reach a fair figure without a court fight.") + """

<h2 id="binding">Making the agreement binding</h2>
<p>The agreement is formalised through either consent orders (court-approved) or a binding financial agreement (private contract with independent legal advice for each party). Both make the support legally enforceable. <a href=\"/bfa-or-consent-orders/\">See which option suits you \u2192</a></p>

<h2 id="get-started">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll listen, assess the eligibility question honestly, and outline what's involved. Spousal maintenance matters often resolve in a single mediation session once full disclosure is in.</p>
""",
    faq_items=[
        ("Who can claim spousal maintenance?","A former partner who can't reasonably meet their own needs, where the other party has the capacity to pay. Both need and capacity must be present. Eligibility isn't automatic."),
        ("How much spousal maintenance gets paid?","There's no fixed formula. The amount reflects the gap between the recipient's reasonable needs and their own capacity, limited by the payer's ability to pay."),
        ("How long does spousal maintenance last?","Often time-limited, to support transition to self-sufficiency. It can be reviewed if circumstances change and generally ends on remarriage. Permanent maintenance is uncommon."),
        ("Is spousal maintenance the same as alimony?","Alimony is a US term. The Australian concept is spousal maintenance, governed by the Family Law Act and assessed on need and capacity."),
        ("Do de facto couples have spousal maintenance rights?","Yes. De facto partners can claim maintenance on the same need-and-capacity basis as married couples, subject to the usual de facto time limits."),
        ("Can we agree spousal maintenance without going to court?","Yes \u2014 that's what mediation is for. You agree the amount, duration and form, then formalise through consent orders or a binding financial agreement."),
        ("What if my ex's circumstances change?","Properly drafted spousal maintenance agreements include review provisions. Significant changes can be the basis for varying the arrangement, whether agreed or by court application."),
    ],
    related_items=[
        ("spousal-maintenance-guide","Spousal Maintenance: Complete Guide"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("child-support-mediation","Child Support Mediation"),
        ("financial-agreements-mediation","Financial Agreements"),
        ("consent-orders","Consent Orders"),
        ("de-facto-mediation","De Facto Mediation"),
        ("family-law-mediation","Family Law Mediation"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)


# ====================================================================
# 11. CHILD SUPPORT MEDIATION
# ====================================================================
service_page(
    slug="child-support-mediation",
    title="Child Support Mediation in Australia | Mediations Australia",
    desc="Resolve child support disputes privately through mediation \u2014 special expenses, care arrangements, and private agreements outside the standard formula. Free consultation.",
    breadcrumb_label="Child Support Mediation",
    eyebrow="Service",
    h1_html='Child Support Mediation \u2014 <em>resolve it privately, fairly</em>.',
    lede="The standard child support formula works for many families, but not all. Where there's a dispute about the assessment, special expenses to share, or a desire for a private arrangement that better fits your situation, mediation gets it sorted without escalation.",
    toc_items=[
        ("what-is","Child support: the basics"),
        ("when-mediate","When mediation helps"),
        ("formula","The formula \u2014 and where it falls short"),
        ("how","How the mediation process works"),
        ("private","Private vs agency-collected"),
        ("special","Special expenses"),
        ("parenting","Child support and parenting"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Child support is administered by Services Australia using a standard formula based on both parents' incomes and care arrangements. Where the formula doesn't fit \u2014 disputes over income, special expenses, complex care patterns \u2014 mediation lets parents reach a private agreement that works for their family. Agreements can be self-managed or registered with Services Australia."
    ),
    body_html=f"""
<h2 id=\"what-is\">Child support: the basics</h2>
<p>Child support in Australia is administered by {cite("services_australia_cs")}, using a formula that takes both parents' taxable incomes, the cost of children at different ages, and the percentage of care each parent provides. For most families the standard assessment works fine \u2014 a number gets calculated, payments flow, and life moves on.</p>

<p>Where it doesn't work fine is where mediation comes in: disputes about the assessment, special expenses the formula doesn't capture, complex or shared care, or where parents want a private arrangement better tailored to their situation.</p>
""" + inline_cta("Got a child support dispute that needs sorting? Mediation resolves it without escalating through the agency.") + """

<h2 id=\"when-mediate\">When mediation helps</h2>
<ul>
  <li><strong>Disputes about income</strong> \u2014 particularly with self-employed parents</li>
  <li><strong>Special expenses</strong> \u2014 private school, medical, extracurriculars \u2014 above the standard formula</li>
  <li><strong>Care percentage disputes</strong> \u2014 which directly affect the payment</li>
  <li><strong>Significant change in circumstances</strong> \u2014 job loss, new family, relocation</li>
  <li><strong>Building a private agreement</strong> instead of going through Services Australia</li>
  <li><strong>Where child support and parenting arrangements are entangled</strong> \u2014 better resolved together</li>
</ul>

<h2 id=\"formula\">The formula \u2014 and where it falls short</h2>
<p>The standard formula is administrative and broad-brush. It captures:</p>
<ul>
  <li>Both parents' taxable incomes (with a self-support amount set aside)</li>
  <li>The cost of children, based on research-derived figures</li>
  <li>The percentage of care each parent provides</li>
  <li>The number and ages of children</li>
</ul>
<p>What it doesn't capture well: special expenses, unusual care patterns, the realities of self-employment, contributions in kind, and the parties' own preferences. That's why private agreements exist. <a href=\"/child-support-guide/\">See the full child support guide \u2192</a></p>

<h2 id=\"how\">How the mediation process works</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 understanding the dispute or what you want to agree.</li>
  <li><strong>Financial disclosure</strong> \u2014 income, expenses, special costs for the children.</li>
  <li><strong>Pre-mediation intake</strong> \u2014 separately with each parent.</li>
  <li><strong>The session</strong> \u2014 working through the assessment, special expenses, and any care arrangements.</li>
  <li><strong>Agreement</strong> \u2014 either a Child Support Agreement (registered) or a private arrangement.</li>
  <li><strong>Implementation</strong> \u2014 registered with Services Australia if agreed, or self-managed.</li>
</ol>

<h2 id=\"private\">Private vs agency-collected</h2>
<p>Parents have three main options for how child support runs:</p>
<ul>
  <li><strong>Self-management</strong> \u2014 you agree, you pay, no agency involvement.</li>
  <li><strong>Private collection</strong> \u2014 Services Australia assesses but doesn't collect.</li>
  <li><strong>Agency collection</strong> \u2014 Services Australia assesses and collects.</li>
</ul>
<p>Mediation often produces self-managed or private arrangements where the relationship supports it.</p>
""" + inline_cta("Many parents prefer a private agreement over agency involvement. Mediation helps you build one that lasts.") + """

<h2 id=\"special\">Special expenses</h2>
<p>The formula covers ordinary costs of raising children. Above-formula expenses \u2014 private school, orthodontics, expensive extracurriculars, special medical needs \u2014 are exactly where parents most often disagree. Mediation lets you agree:</p>
<ul>
  <li>Which expenses count as special</li>
  <li>How they're shared (50/50, in proportion to income, otherwise)</li>
  <li>How they're paid \u2014 directly to providers, reimbursed, or pooled</li>
  <li>How decisions about new expenses get made</li>
</ul>

<h2 id=\"parenting\">Child support and parenting</h2>
<p>Care percentages feed the formula, which means disputes about parenting time can become disputes about money \u2014 and vice versa. Mediating them together produces a coherent outcome where both pieces fit. <a href=\"/child-custody-mediation/\">See child custody mediation \u2192</a></p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll understand what's in dispute, whether the standard formula is working, and what would actually help. Many child support matters resolve in a single session.</p>
""",
    faq_items=[
        ("Do I have to use the standard child support formula?","No. The formula is the default, but parents can agree their own arrangement \u2014 either a Child Support Agreement registered with Services Australia, or a private self-managed arrangement."),
        ("How are special expenses (school, medical) handled?","The standard formula doesn't cover them well. Mediation lets you agree which expenses count, how they're shared, and how new ones get decided."),
        ("Can child support be mediated alongside parenting arrangements?","Yes \u2014 and it often should be, since care percentages affect the formula. Mediating both together produces a coherent outcome."),
        ("What if my ex's income isn't what they're declaring?","Income disputes \u2014 especially with self-employed parents \u2014 are a common driver of child support mediation. The process lets you work through documents, capacity, and what a fair assessment looks like."),
        ("Can I have a child support agreement without Services Australia?","Yes \u2014 you can self-manage entirely, or register the agreement with Services Australia for them to enforce. Mediation produces agreements that work either way."),
        ("How long does child support mediation take?","Most matters resolve in a single session, with the whole process from consultation to documented agreement typically completing in 2\u20134 weeks."),
        ("Is the mediated agreement legally binding?","If registered as a Child Support Agreement with Services Australia, yes. Private agreements bind by contract but may need formalisation for full enforceability."),
    ],
    related_items=[
        ("child-support-guide","Child Support: Complete Guide"),
        ("parenting-plan-mediation","Parenting Plan Mediation"),
        ("child-custody-mediation","Child Custody Mediation"),
        ("spousal-support-mediation","Spousal Support Mediation"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("family-law-mediation","Family Law Mediation"),
        ("how-mediation-works","How Mediation Works"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)


# ====================================================================
# 12. DE FACTO MEDIATION
# ====================================================================
service_page(
    slug="de-facto-mediation",
    title="De Facto Mediation in Australia | Mediations Australia",
    desc="De facto separation has the same property rights as marriage \u2014 with a strict 2-year limit. Resolve it through accredited mediation, fast. Free consultation.",
    breadcrumb_label="De Facto Mediation",
    eyebrow="Service",
    h1_html='De Facto Mediation \u2014 <em>same rights, same urgency</em>.',
    lede="De facto separations carry substantially the same property and financial rights as marriage \u2014 but with a strict two-year time limit from separation. Mediation resolves the property division, superannuation, and any maintenance question well inside the window, without court.",
    toc_items=[
        ("what-is","What counts as de facto"),
        ("rights","The rights you have"),
        ("time-limit","The two-year time limit"),
        ("process","The mediation process"),
        ("property","Property and super"),
        ("parenting","Parenting where there are children"),
        ("binding","Making the agreement binding"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "De facto couples in Australia have substantially the same property, superannuation and maintenance rights as married couples \u2014 the surprise to many is just how similar they are. The critical difference is the time limit: de facto couples have just two years from separation to apply for a property settlement. Mediation resolves the issues well inside the window, faster and at a fraction of court cost."
    ),
    body_html=f"""
<h2 id=\"what-is\">What counts as de facto</h2>
<p>Under the {cite("family_law_act")}, a de facto relationship exists where two people live together on a genuine domestic basis without being married. No single factor decides it \u2014 courts look at the whole picture: duration, cohabitation, finances, children, public aspects, sexual relationship.</p>
<p>Generally you need to have been together for at least two years, or have a child together, or have made substantial contributions, for the property regime to apply.</p>
""" + inline_cta("Separating from a de facto partner? The two-year clock is already ticking \u2014 book a consultation today.") + """

<h2 id=\"rights\">The rights you have</h2>
<p>This surprises many people: de facto couples have substantially the same rights as married couples for property settlement, superannuation splitting and spousal maintenance. The same <a href=\"/what-am-i-entitled-to-in-a-separation-in-australia/\">four-step framework</a> applies. Being unmarried doesn't mean walking away with only what's in your name.</p>

<h2 id=\"time-limit\">The two-year time limit</h2>
<p>Here's the critical practical difference. De facto couples must generally apply for property settlement or maintenance <strong>within two years of separation</strong>. There's no divorce step to reset the clock, no extension if you weren't sure when the relationship ended. Miss it and you need the court's permission, which isn't guaranteed.</p>
""" + callout("Treat the two-year clock as already running","Because there's no formal separation step in de facto relationships, the date of separation is often disputed later. Acting promptly removes the question entirely.") + """

<h2 id=\"process\">The mediation process</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 understanding the relationship, the assets, and the time pressure.</li>
  <li><strong>Disclosure</strong> \u2014 full financial disclosure between the parties.</li>
  <li><strong>Pre-mediation intake</strong> \u2014 separately with each party.</li>
  <li><strong>The session</strong> \u2014 working through the asset pool, contributions, future needs.</li>
  <li><strong>Heads of Agreement</strong> \u2014 documented while it's fresh.</li>
  <li><strong>Formalisation</strong> \u2014 consent orders or BFA, inside the two-year window.</li>
</ol>

<h2 id=\"property\">Property and super</h2>
<p>The same four-step framework applies: identify the asset pool, assess contributions, consider future needs, ensure the result is just and equitable. Superannuation can be split exactly as for married couples. <a href=\"/property-settlement-mediation/\">See property settlement mediation \u2192</a></p>

<h2 id=\"parenting\">Parenting where there are children</h2>
<p>De facto status makes no difference to parenting law \u2014 the same best-interests test applies, and Family Dispute Resolution is required before parenting court applications. <a href=\"/parenting-plan-mediation/\">See parenting plan mediation \u2192</a></p>
""" + inline_cta("Inside two years, mediation gets it done. Outside two years, you're at the court's discretion. Move now.") + """

<h2 id=\"binding\">Making the agreement binding</h2>
<p>The mediated agreement is formalised through consent orders (court-approved) or a binding financial agreement (private contract with independent legal advice). Either way, well inside the two-year window. <a href=\"/de-facto-relationships-guide/\">See de facto relationships: complete guide \u2192</a></p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a fixed-fee consultation. Given the time limit, the sooner the better.</p>
""",
    faq_items=[
        ("Do de facto couples have the same property rights as married couples?","Substantially, yes \u2014 the same Family Law Act framework applies for property settlement, super splitting and spousal maintenance. The main difference is the time limit."),
        ("What's the time limit for de facto property claims?","Generally two years from the date of separation. After that you need the court's permission to apply, which isn't guaranteed."),
        ("How is a de facto relationship proved?","Through evidence of living together, shared finances, the length of the relationship, children, and how the relationship was presented publicly. No single factor is decisive."),
        ("Can same-sex de facto couples mediate?","Yes \u2014 same-sex de facto couples have identical rights under Australian family law. <a href=\"/same-sex-family-law/\">See same-sex separation \u2192</a>."),
        ("What if we're not sure when we separated?","Date of separation is sometimes contested in de facto matters. Acting promptly avoids needing to argue it later \u2014 mediation can also help agree the date."),
        ("Do parenting arrangements differ for de facto parents?","No \u2014 the parenting law is the same regardless of marital status. Best-interests test applies."),
        ("Can we mediate if one of us has moved overseas?","Yes \u2014 online mediation works well across borders. The Australian Family Law Act jurisdiction depends on the Australian connection."),
    ],
    related_items=[
        ("de-facto-relationships-guide","De Facto Relationships: Complete Guide"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
        ("financial-agreements-mediation","Financial Agreements"),
        ("consent-orders","Consent Orders"),
        ("same-sex-family-law","Same-Sex Separation"),
        ("family-law-mediation","Family Law Mediation"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)


# ====================================================================
# 13. GRANDPARENTS MEDIATION
# ====================================================================
service_page(
    slug="grandparents-mediation",
    title="Grandparents Mediation in Australia | Mediations Australia",
    desc="Restore or maintain time with your grandchildren through accredited mediation \u2014 the required first step before parenting court applications. Free consultation.",
    breadcrumb_label="Grandparents Mediation",
    eyebrow="Service",
    h1_html='Grandparents Mediation \u2014 <em>rebuild time with the grandkids</em>.',
    lede="When grandparents are cut off from grandchildren \u2014 by a difficult separation, family conflict, or estrangement \u2014 the path back usually runs through mediation, not court. The law expressly recognises children's right to spend time with significant people in their lives, and mediation is the way to make that real.",
    toc_items=[
        ("rights","What rights grandparents have"),
        ("when","When mediation helps"),
        ("process","The mediation process"),
        ("law","What the law says"),
        ("care","When grandchildren live with grandparents"),
        ("section-60i","Section 60I certificates"),
        ("formalising","Formalising the arrangement"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Grandparents don't have automatic rights in Australian family law, but the Family Law Act expressly recognises children's right to spend time with people significant to their care, welfare and development \u2014 including grandparents. Mediation is the required first step before applying for a parenting order, and it's usually the most effective path: it can rebuild communication where court would entrench division."
    ),
    body_html=f"""
<h2 id=\"rights\">What rights grandparents have</h2>
<p>It's worth being honest: grandparents don't have an automatic, freestanding \"right\" to see grandchildren. What they do have is the right to apply for a parenting order, and the law expressly recognises that children benefit from relationships with grandparents and other significant people. The framing matters \u2014 the law looks at it as <em>the child's</em> right to maintain meaningful relationships, not the adult's right of access.</p>

<p>In practice that's a strong basis. For grandparents who've been part of the children's lives, the best-interests test usually supports maintaining the connection.</p>
""" + inline_cta("Being kept from your grandchildren is painful. We can help you find a way back \u2014 book a consultation.") + """

<h2 id=\"when\">When mediation helps</h2>
<ul>
  <li>You've lost contact after a parent's separation or new relationship</li>
  <li>A falling-out with your own adult child has cost you the grandchildren</li>
  <li>You want to formalise existing time so it isn't dependent on parents' goodwill</li>
  <li>You've been caring for grandchildren informally and need a legal arrangement</li>
  <li>You want to maintain time after a death or family crisis</li>
</ul>

<h2 id=\"process\">The mediation process</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 understanding your situation, the relationship history, what you want.</li>
  <li><strong>Reaching out to the parents</strong> \u2014 we contact them and offer the mediation process.</li>
  <li><strong>Intake</strong> \u2014 separate sessions with all the adults involved.</li>
  <li><strong>The session</strong> \u2014 working through what arrangement serves the children.</li>
  <li><strong>Agreement</strong> \u2014 a parenting plan covering time, communication, decision-making.</li>
  <li><strong>Formalisation</strong> \u2014 consent orders if the arrangement needs the force of law.</li>
</ol>

<h2 id=\"law\">What the law says</h2>
<p>The {cite("family_law_act")} expressly contemplates grandparents applying for parenting orders. The best-interests test governs the outcome, considering:</p>
<ul>
  <li>The benefit of a meaningful relationship with significant people</li>
  <li>The need to protect children from harm</li>
  <li>The nature of the existing relationship</li>
  <li>The children's views (age-appropriately)</li>
  <li>The practical effect of any arrangement</li>
</ul>
<p><a href=\"/grandparents-rights/\">See grandparents' rights in detail \u2192</a></p>
""" + callout("Family Dispute Resolution applies","Like parents, grandparents generally need to attempt Family Dispute Resolution and obtain a Section 60I certificate before applying to court for a parenting order, unless an exemption applies.") + """

<h2 id=\"care\">When grandchildren live with grandparents</h2>
<p>Sometimes grandparents end up as the primary carers \u2014 where parents are unable to care due to illness, addiction or other circumstances. The legal arrangement is the same in principle: parenting orders can place children in grandparents' care, with the grandparents holding parental responsibility. Mediation is often part of this process even where the parents agree, because formalising the arrangement protects everyone. <a href=\"/child-custody-mediation/\">See how care arrangements work \u2192</a></p>

<h2 id=\"section-60i\">Section 60I certificates</h2>
<p>If mediation doesn't fully resolve the matter, the practitioner can issue a Section 60I certificate \u2014 allowing the grandparents' parenting application to proceed to court. <a href=\"/section-60i-certificates/\">See Section 60I certificates \u2192</a></p>
""" + inline_cta("Most matters resolve at mediation. The certificate is the backup if they don't. Either way you move forward.") + """

<h2 id=\"formalising\">Formalising the arrangement</h2>
<p>An informal agreement is fine where the parents are reliable. Where they're not, or where the situation needs the certainty of court orders, the mediated arrangement is converted into consent orders \u2014 enforceable in the same way as any court order. <a href=\"/consent-orders/\">See consent orders \u2192</a></p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll listen, assess the situation honestly, and outline what's possible. These matters are emotional but solvable \u2014 the path back to your grandchildren usually starts with a single conversation.</p>
""",
    faq_items=[
        ("Do grandparents have a right to see their grandchildren?","Not an automatic right, but the Family Law Act expressly contemplates grandparents applying for parenting orders, and the law recognises children's right to maintain significant relationships."),
        ("Do grandparents have to try mediation before court?","Generally yes \u2014 like parents, grandparents must usually attempt Family Dispute Resolution and obtain a Section 60I certificate before applying for a parenting order, unless an exemption applies."),
        ("Can grandchildren live with grandparents legally?","Yes. Where parents can't care for the children, grandparents can seek parenting orders placing the children with them, with grandparents holding parental responsibility."),
        ("What if the parents won't engage?","If parents refuse to mediate, the practitioner can issue a Section 60I certificate, allowing the application to proceed to court."),
        ("Does mediation cost more for grandparents?","No \u2014 the cost is the same as any other family law mediation. Typically $3,000\u2013$7,000 total, often shared between the parties involved."),
        ("Can mediation work if there's been a family rift?","Often it's exactly where mediation works best. The structured, neutral process can rebuild communication where direct conversation has failed."),
        ("How long does the process take?","Most matters resolve in one or two sessions over a few weeks. Compare that to the one to three years a contested court case can take."),
    ],
    related_items=[
        ("grandparents-rights","Grandparents' Rights: Complete Guide"),
        ("child-custody-mediation","Child Custody Mediation"),
        ("parenting-plan-mediation","Parenting Plan Mediation"),
        ("section-60i-certificates","Section 60I Certificates"),
        ("parenting-plans-guide","Parenting Plans Guide"),
        ("family-law-mediation","Family Law Mediation"),
        ("consent-orders","Consent Orders"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)


# ====================================================================
# 14. FAMILY LAW ARBITRATION
# ====================================================================
service_page(
    slug="family-law-arbitration",
    title="Family Law Arbitration in Australia | Mediations Australia",
    desc="Get a binding decision on property and financial matters \u2014 privately, fast \u2014 through accredited family law arbitration. The alternative to court. Free consultation.",
    breadcrumb_label="Family Law Arbitration",
    eyebrow="Service",
    h1_html='Family Law Arbitration \u2014 <em>a binding decision, privately</em>.',
    lede="When mediation doesn't quite get there, but court would be ruinously expensive and slow, arbitration is the middle path. A qualified arbitrator hears your matter and makes a binding decision \u2014 like a private judge, but on your timetable and out of public view.",
    toc_items=[
        ("what-is","What is family law arbitration?"),
        ("vs-mediation","Arbitration vs mediation"),
        ("what-can","What can be arbitrated"),
        ("how","How the process works"),
        ("binding","Is the decision binding?"),
        ("vs-court","Arbitration vs court"),
        ("when","When to choose arbitration"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Family law arbitration is a process where a qualified arbitrator hears a property or financial dispute and makes a legally binding decision \u2014 privately, on the parties' timetable, and far faster than court. Unlike mediation, the arbitrator decides the outcome. It's available for financial and property matters only \u2014 not parenting \u2014 and the award can be registered with the court and enforced like a court order."
    ),
    body_html=f"""
<h2 id=\"what-is\">What is family law arbitration?</h2>
<p>Arbitration is a form of dispute resolution where the parties appoint a qualified arbitrator to hear their dispute and make a binding decision. It combines some of the speed and privacy of mediation with the finality of a court decision. For couples who genuinely can't agree but want to avoid the cost and delay of litigation, it's a powerful middle path.</p>

<p>It's recognised under the {cite("family_law_act")} and the resulting award can be registered with the {cite("fcfcoa")} and enforced like a court order.</p>
""" + inline_cta("Need a binding decision without years in court? Arbitration might be the answer. Book a consultation.") + """

<h2 id=\"vs-mediation\">Arbitration vs mediation</h2>
<p>The fundamental difference: in mediation, you and your former partner reach your own agreement and the mediator decides nothing. In arbitration, the <em>arbitrator</em> decides. You present your case; they make the call.</p>
<p>For most family disputes, mediation is the right first move \u2014 it keeps you in control. Arbitration enters the picture when mediation has resolved most issues but a stubborn few remain, or when the parties genuinely can't agree but want to stay out of court.</p>

<h2 id=\"what-can\">What can be arbitrated</h2>
<ul>
  <li>Property settlements and division of assets</li>
  <li>Superannuation splitting</li>
  <li>Spousal maintenance</li>
  <li>Financial aspects of de facto separations</li>
</ul>
<p><strong>Arbitration is for financial matters only.</strong> Parenting disputes cannot be arbitrated \u2014 they're resolved through mediation or, if necessary, the court.</p>

<h2 id=\"how\">How the process works</h2>
<ol>
  <li><strong>Agreement to arbitrate</strong> \u2014 both parties consent and appoint a qualified arbitrator.</li>
  <li><strong>Setting the process</strong> \u2014 timetable, document protocols, how evidence is presented.</li>
  <li><strong>Pre-hearing</strong> \u2014 each party prepares their case, with disclosure as you'd expect in court.</li>
  <li><strong>The hearing</strong> \u2014 each side presents to the arbitrator. Less formal than court, often quicker.</li>
  <li><strong>The award</strong> \u2014 the arbitrator's binding decision, with reasons.</li>
  <li><strong>Registration</strong> \u2014 the award can be registered with the court and enforced like any court order.</li>
</ol>

<h2 id=\"binding\">Is the decision binding?</h2>
<p>Yes. Once registered with the {cite("fcfcoa")}, the award is enforceable just like a court order. There are limited grounds to challenge an award \u2014 narrower than appeals from a court decision \u2014 which is exactly what gives arbitration its finality.</p>
""" + callout("Faster and private","An arbitrated decision can be reached in a fraction of the time a contested court hearing takes, on a timetable you help set, and entirely out of the public eye \u2014 a real advantage for complex financial matters or business interests.") + """

<h2 id=\"vs-court\">Arbitration vs court</h2>
<p>Compared with a contested court hearing, arbitration is faster (months not years), cheaper (no court queue or repeated appearances), more private (no public record), and procedurally more flexible (you shape how it runs). The trade-off is narrower appeal rights, which most parties accept because finality is part of the appeal.</p>

<h2 id=\"when\">When to choose arbitration</h2>
<p>It's particularly useful where:</p>
<ul>
  <li>Mediation has narrowed the dispute but a binding decision is needed</li>
  <li>The matter is complex financially and benefits from a specialist arbitrator</li>
  <li>Privacy matters (a business, sensitive financial circumstances)</li>
  <li>Speed matters more than the broadest appeal rights</li>
  <li>The parties want certainty without years of court process</li>
</ul>
""" + inline_cta("Mediation first, arbitration if needed. We help you sequence them sensibly.") + """

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll assess whether arbitration is right for your matter, explain the process and likely cost, and outline how it sequences with mediation if you haven't tried that first. <a href=\"/arbitration-in-family-law/\">See the full arbitration guide \u2192</a></p>
""",
    faq_items=[
        ("What is family law arbitration?","A process where a qualified arbitrator hears a property or financial dispute and makes a legally binding decision, privately and faster than court. Used for financial matters only, not parenting."),
        ("How is arbitration different from mediation?","In mediation you reach your own agreement and the mediator decides nothing. In arbitration the arbitrator makes a binding decision for you, like a private judge."),
        ("Can parenting matters be arbitrated?","No. In Australia, arbitration is available for property and financial matters only. Parenting disputes are resolved through mediation or court."),
        ("Is an arbitrator's decision binding?","Yes. The arbitral award can be registered with the Federal Circuit and Family Court and enforced like a court order, with limited grounds to challenge."),
        ("Should I try mediation or arbitration first?","Most parties start with mediation to retain control of the outcome, then use arbitration only for any financial issues that remain unresolved \u2014 avoiding a full court case."),
        ("How long does arbitration take?","Typically months not years \u2014 dramatically faster than a contested court matter. The parties help set the timetable."),
        ("How much does arbitration cost?","Less than contested litigation but more than pure mediation \u2014 the arbitrator is making a substantive decision and the process is more intensive. We provide a clear estimate at the consultation."),
    ],
    related_items=[
        ("arbitration-in-family-law","Family Law Arbitration: Complete Guide"),
        ("family-law-mediation","Family Law Mediation"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("mediate-or-litigate","Mediate or Litigate?"),
        ("family-court-process","The Family Court Process"),
        ("financial-agreements-mediation","Financial Agreements"),
        ("consent-orders","Consent Orders"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)


# ====================================================================
# 15. ESTATE DISPUTE MEDIATION
# ====================================================================
service_page(
    slug="estate-dispute-mediation",
    title="Estate Dispute Mediation in Australia | Mediations Australia",
    desc="Contested wills and family inheritance disputes resolved privately through accredited mediation \u2014 preserving relationships at the hardest time. Free consultation.",
    breadcrumb_label="Estate Dispute Mediation",
    eyebrow="Service",
    h1_html='Estate Dispute Mediation \u2014 <em>resolve it without destroying the family</em>.',
    lede="Wills get contested. Promised inheritances disappear. Long-buried family tensions resurface around a death. Court can resolve the legal question but usually destroys what's left of the relationships. Mediation gets to a fair outcome while keeping the family intact.",
    toc_items=[
        ("what","What is estate dispute mediation?"),
        ("disputes","What we resolve"),
        ("law","The legal landscape"),
        ("how","How the process works"),
        ("when","When mediation helps"),
        ("vs-court","Mediation vs court for estate disputes"),
        ("costs","Costs and timeframes"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Estate dispute mediation resolves contested wills, family provision claims, and other inheritance conflicts through structured negotiation with a neutral mediator. It's confidential, far faster than estate litigation, and \u2014 critically \u2014 it preserves family relationships that court tends to destroy. Most estate disputes are well-suited to mediation; courts increasingly direct parties to attempt it before allowing litigation to proceed."
    ),
    body_html="""
<h2 id=\"what\">What is estate dispute mediation?</h2>
<p>Estate dispute mediation applies the same principles as family law mediation to disputes that arise after someone has died: contested wills, family provision claims, disputes between executors and beneficiaries, claims of undue influence, and arguments about how an estate is being administered.</p>
<p>The mediator is neutral, the process is confidential, and the outcome is shaped by the parties \u2014 not imposed by a judge.</p>
""" + inline_cta("Family disagreement over an estate? Mediation resolves it before lawyers eat the inheritance. Book a consultation.") + """

<h2 id=\"disputes\">What we resolve</h2>
<ul>
  <li><strong>Contested wills</strong> \u2014 challenges to validity, capacity, undue influence</li>
  <li><strong>Family provision claims</strong> \u2014 where someone feels inadequately provided for</li>
  <li><strong>Disputes between executors and beneficiaries</strong> \u2014 administration, valuations, distributions</li>
  <li><strong>Multi-beneficiary disagreements</strong> \u2014 about specific assets, sentimental items, or timing</li>
  <li><strong>Claims of unfulfilled promises</strong> \u2014 \"Dad always said the farm would be mine\"</li>
  <li><strong>Disputes about a deceased's earlier gifts or transfers</strong></li>
  <li><strong>Conflicts in blended families</strong> \u2014 between a spouse and adult children from previous relationships</li>
</ul>

<h2 id=\"law\">The legal landscape</h2>
<p>Estate law varies between Australian states and territories, but the broad framework is similar everywhere: there's a will (or the rules of intestacy), an executor administering it, and various rights of beneficiaries and potential claimants. Disputes get pulled into state supreme courts \u2014 expensive, slow, and devastating to families. Courts increasingly direct parties to mediate before allowing matters to proceed. We make that step productive.</p>

<h2 id=\"how\">How the process works</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 understanding the dispute, who's involved, what the estate looks like.</li>
  <li><strong>Engagement with the other parties</strong> \u2014 we reach out, explain the process, confirm participation.</li>
  <li><strong>Pre-mediation intake</strong> \u2014 separate sessions with each party.</li>
  <li><strong>The session</strong> \u2014 typically a full day, working through the issues with the mediator's guidance.</li>
  <li><strong>Deed of settlement</strong> \u2014 the resolution is documented in a binding settlement deed.</li>
  <li><strong>Implementation</strong> \u2014 the executor implements the agreed outcome.</li>
</ol>

<h2 id=\"when\">When mediation helps</h2>
<ul>
  <li>Before any court proceedings \u2014 saving everyone the cost</li>
  <li>After a claim is filed but before it gets to a defended hearing \u2014 settle on the steps of court</li>
  <li>Where the dispute is partly about money and partly about old family wounds \u2014 court can only do the money</li>
  <li>Where there are multiple parties \u2014 mediation handles complexity better than litigation</li>
  <li>Where the estate's value would be substantially eroded by legal fees</li>
</ul>
""" + callout("Estate litigation is unusually destructive","Estate disputes are particularly bad in court \u2014 they involve grief, old family dynamics, and a fixed pie that gets smaller with every legal fee. Mediation contains all of those costs.") + """

<h2 id=\"vs-court\">Mediation vs court for estate disputes</h2>
<p>Compared with estate litigation:</p>
<ul>
  <li><strong>Cost</strong> \u2014 a fraction. Estate litigation regularly consumes 20\u201340% of the estate's value.</li>
  <li><strong>Time</strong> \u2014 weeks not years.</li>
  <li><strong>Privacy</strong> \u2014 the family's affairs stay private rather than entering the public record.</li>
  <li><strong>Relationships</strong> \u2014 mediation keeps families speaking; litigation rarely does.</li>
  <li><strong>Flexibility</strong> \u2014 mediation can craft creative solutions a court can't order (in-kind transfers, staged distributions).</li>
</ul>
""" + inline_cta("Save the estate for the family, not the lawyers. Estate mediation does exactly that.") + """

<h2 id=\"costs\">Costs and timeframes</h2>
<p>Estate mediation is typically a single full-day session with intake. Costs depend on complexity but are usually a single-figure thousands rather than the tens or hundreds of thousands estate litigation can run. The full process from consultation to settlement deed typically takes 4\u20138 weeks.</p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll listen to the dispute, assess suitability, and outline a process. Even where court proceedings have begun, mediation can usually still resolve the matter \u2014 often more quickly than the court process can complete.</p>
""",
    faq_items=[
        ("What is estate dispute mediation?","A confidential, structured process where a neutral mediator helps parties resolve disputes about a deceased estate \u2014 contested wills, family provision claims, executor disputes \u2014 without going to court."),
        ("What kinds of estate disputes can be mediated?","Contested wills, family provision claims, disputes between executors and beneficiaries, multi-beneficiary disagreements, claims of unfulfilled promises, and conflicts in blended families."),
        ("Is estate mediation legally binding?","The mediation itself doesn't impose anything, but the agreement reached is documented in a binding settlement deed that's legally enforceable like any contract."),
        ("Can we mediate after court proceedings have started?","Yes \u2014 estate matters frequently settle through mediation after proceedings are filed. Courts often direct parties to mediate before allowing the matter to proceed to a hearing."),
        ("Who pays for estate mediation?","Often the estate itself pays, with the cost coming from the assets before distribution. Other arrangements are possible depending on circumstances."),
        ("How long does estate mediation take?","Most matters resolve in a single full-day session, with the full process from consultation to settlement deed typically taking 4\u20138 weeks."),
        ("Can mediation work for complex blended-family disputes?","Yes \u2014 it's particularly suited to multi-party situations that court would handle clumsily. The flexible format scales to the number of interests involved."),
    ],
    related_items=[
        ("workplace-mediation","Workplace Mediation"),
        ("family-law-mediation","Family Law Mediation"),
        ("how-mediation-works","How Mediation Works"),
        ("mediate-or-litigate","Mediate or Litigate?"),
        ("conciliation-vs-mediation","Conciliation vs Mediation"),
        ("preparing-for-mediation","Preparing for Mediation"),
        ("about-mediations-australia","About Mediations Australia"),
        ("contact-us","Contact"),
    ],
)


# ====================================================================
# 16. ACCREDITED FAMILY LAW MEDIATORS (about/positioning)
# ====================================================================
service_page(
    slug="accredited-family-law-mediators",
    title="Accredited Family Law Mediators in Australia | Mediations Australia",
    desc="Work with nationally accredited family law mediators across Australia \u2014 AMDRAS-certified, many also experienced family lawyers. Fixed-fee consultations.",
    breadcrumb_label="Accredited Family Law Mediators",
    eyebrow="Why us",
    h1_html='Accredited Family Law Mediators \u2014 <em>standards that matter</em>.',
    lede="Anyone can call themselves a mediator. Accreditation under AMDRAS means the person across the table has been trained, assessed, and is bound by an enforceable code of conduct. It's the difference between a recognised professional and someone with a website.",
    toc_items=[
        ("what-is","What does accredited mean"),
        ("amdras","AMDRAS: the national standard"),
        ("fdrp","FDRP for parenting matters"),
        ("lawyers","Mediators who are also lawyers"),
        ("matter","Why accreditation matters"),
        ("our-team","Our team's standards"),
        ("vs-non","Vs non-accredited"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Accreditation under the Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS) is the national framework for mediators in Australia. It requires formal training, supervised practice, a code of conduct, and ongoing professional development. For parenting matters, an additional registration as a Family Dispute Resolution Practitioner (FDRP) is required to issue Section 60I certificates. Every mediator at Mediations Australia meets these standards."
    ),
    body_html=f"""
<h2 id=\"what-is\">What does accredited mean</h2>
<p>\"Mediator\" is an unregulated word. There's no law stopping anyone from putting it on a business card. <strong>Accredited mediator</strong> is different \u2014 it's a recognised credential under a national framework, requiring formal training, supervised practice, ongoing development, and adherence to an enforceable code of conduct.</p>
<p>When you engage an accredited mediator, you know what you're getting: someone trained to a national standard, accountable to a professional body, and bound by ethical obligations that go beyond just doing the job.</p>
""" + inline_cta("Work with mediators held to national standards \u2014 not someone with a website. Book a consultation today.") + """

<h2 id=\"amdras\">AMDRAS: the national standard</h2>
<p>The Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS) is the national framework, maintained by the <a href=\"https://msb.org.au/\" target=\"_blank\" rel=\"noopener\">Mediator Standards Board</a>. To be accredited, a mediator must:</p>
<ul>
  <li>Complete formal training meeting the national standard</li>
  <li>Pass a competency assessment</li>
  <li>Practise under supervision</li>
  <li>Maintain Continuing Professional Development</li>
  <li>Adhere to the AMDRAS Practice Standards (impartiality, confidentiality, competence)</li>
  <li>Be subject to a complaints process</li>
</ul>
<p>That's a real bar. It's not something you can just declare yourself into.</p>

<h2 id=\"fdrp\">FDRP for parenting matters</h2>
<p>For parenting disputes that may proceed to court, the mediator must also be registered as a <strong>Family Dispute Resolution Practitioner (FDRP)</strong> under the framework administered by the {cite("ag_fdr")}. Only FDRPs can issue the {esc("Section 60I certificate")} the court requires for most parenting applications. <a href=\"/section-60i-certificates/\">See Section 60I certificates \u2192</a></p>

<h2 id=\"lawyers\">Mediators who are also lawyers</h2>
<p>Many of our mediators are also practising or formerly-practising family lawyers. That's deliberate. A mediator with legal training brings two things to the room a non-lawyer mediator doesn't:</p>
<ul>
  <li>Understanding of what a court would actually do with your matter \u2014 so the agreement reflects realistic outcomes</li>
  <li>Ability to spot issues in proposed terms that look fine but would cause problems later</li>
</ul>
<p>The combination of accredited mediator and family lawyer is genuinely unusual, and it's where a lot of our value lies.</p>
""" + callout("Lawyer-mediators don't take sides","A mediator who's also a lawyer is still neutral in the room. The legal background informs how the mediation runs and what gets flagged \u2014 it doesn't change the impartiality.") + """

<h2 id=\"matter\">Why accreditation matters</h2>
<p>Three concrete reasons:</p>
<ol>
  <li><strong>The certificate</strong> \u2014 if your matter ends up needing a Section 60I certificate, only an FDRP can issue it. A non-accredited mediator can't.</li>
  <li><strong>The standards</strong> \u2014 accredited mediators are bound by a Practice Standards code covering impartiality, confidentiality, conflicts of interest, and competence. Non-accredited mediators aren't.</li>
  <li><strong>The recourse</strong> \u2014 if something goes wrong, accreditation comes with a complaints process and meaningful consequences. Without it, you're on your own.</li>
</ol>

<h2 id=\"our-team\">Our team's standards</h2>
<p>Every mediator at Mediations Australia is nationally accredited under AMDRAS. For parenting work, they're also registered as FDRPs. Many are also experienced family lawyers. Continuing professional development is a requirement, not a nice-to-have \u2014 our mediators stay current with family law reform, evolving practice, and emerging considerations around family violence and child welfare.</p>
""" + inline_cta("Confidence comes from the credentials behind the people. Book a consultation with an accredited mediator.") + """

<h2 id=\"vs-non\">Vs non-accredited</h2>
<p>You can find non-accredited \"mediators\" \u2014 sometimes much cheaper. The risk is straightforward: they can't issue Section 60I certificates, they're not bound by enforceable standards, and you have no recourse if things go wrong. For low-stakes informal disputes, that may be acceptable. For family law matters with real consequences \u2014 children, property, futures \u2014 it isn't.</p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a fixed-fee consultation. You'll work with an accredited mediator from the start \u2014 we don't outsource to subcontractors and we don't put trainees on real matters.</p>
""",
    faq_items=[
        ("What does \"accredited mediator\" mean?","A mediator accredited under AMDRAS (the Australian Mediator and Dispute Resolution Accreditation Standards) has completed formal training, passed competency assessment, practises under a code of conduct, and maintains ongoing professional development."),
        ("Is every mediator in Australia accredited?","No \u2014 \"mediator\" itself is unregulated. Accreditation is the recognised national credential. Anyone offering mediation should be able to confirm their accreditation if asked."),
        ("What's the difference between a mediator and an FDRP?","An FDRP (Family Dispute Resolution Practitioner) is an accredited mediator additionally registered to handle parenting matters and issue Section 60I certificates required for court applications."),
        ("Are your mediators also lawyers?","Many are. The combination is deliberate \u2014 a mediator with family law experience brings legal awareness into the room without taking sides."),
        ("Why does it matter if my mediator is accredited?","Three reasons: only an accredited FDRP can issue Section 60I certificates; accredited mediators are bound by enforceable standards; and you have meaningful recourse through a complaints process if something goes wrong."),
        ("Is a non-accredited mediator cheaper?","Sometimes. The risk is no certificates can be issued, no standards apply, and you have no recourse \u2014 a poor trade for matters with real consequences."),
        ("Who maintains the AMDRAS standard?","The Mediator Standards Board, an independent body. The standard itself is reviewed and updated over time."),
    ],
    related_items=[
        ("our-mediators","Our Mediators"),
        ("memberships","Memberships & Accreditations"),
        ("about-mediations-australia","About Mediations Australia"),
        ("family-law-mediation","Family Law Mediation"),
        ("section-60i-certificates","Section 60I Certificates"),
        ("how-mediation-works","How Mediation Works"),
        ("collaborative-family-lawyers","Collaborative Family Lawyers"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)


# ====================================================================
# 17. COLLABORATIVE FAMILY LAWYERS
# ====================================================================
service_page(
    slug="collaborative-family-lawyers",
    title="Collaborative Family Lawyers in Australia | Mediations Australia",
    desc="Collaborative family law combines lawyer advice with a structured, non-court process. How it works, when it suits, and how it compares to mediation. Free consultation.",
    breadcrumb_label="Collaborative Family Lawyers",
    eyebrow="Service",
    h1_html='Collaborative Family Lawyers \u2014 <em>legal advice without the court fight</em>.',
    lede="Collaborative law is the middle path between DIY mediation and full litigation. Each party has their own lawyer, but every lawyer commits in writing to resolve the matter without court. The result is informed, supported negotiation \u2014 with the legal expertise you'd want, minus the adversarial mindset.",
    toc_items=[
        ("what-is","What is collaborative law"),
        ("vs-mediation","Collaborative vs mediation"),
        ("vs-litigation","Collaborative vs litigation"),
        ("how","How the process works"),
        ("commitment","The collaborative commitment"),
        ("suits","Who it suits"),
        ("costs","Costs and timeframes"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Collaborative family law is a structured process where each party has their own lawyer, but all parties \u2014 including the lawyers \u2014 sign a participation agreement committing to resolve the matter without going to court. If negotiations fail and litigation begins, the collaborative lawyers must withdraw. That commitment changes the dynamic completely: lawyers are incentivised to solve, not to fight."
    ),
    body_html="""
<h2 id=\"what-is\">What is collaborative law</h2>
<p>Collaborative family law (sometimes called \"collaborative practice\") is a structured non-litigation process developed in the 1990s and now well-established in Australia. The core feature is the <strong>participation agreement</strong> \u2014 a written commitment by both parties and both lawyers to resolve the matter without court, and a binding undertaking that if litigation begins, the collaborative lawyers must withdraw.</p>
<p>That last piece is what makes it work. The lawyers can't retreat to court if things get hard. They have to actually solve the problem.</p>
""" + inline_cta("Want lawyer support but not lawyer warfare? Collaborative law is the structured middle path. Talk to us.") + """

<h2 id=\"vs-mediation\">Collaborative vs mediation</h2>
<p>The key difference: in mediation, you and your former partner work with a single neutral mediator. In collaborative law, each of you has your own lawyer, and the four of you (plus sometimes additional experts) work through the matter together.</p>
<ul>
  <li><strong>Mediation</strong> is leaner, faster, and cheaper \u2014 best where the parties can engage directly and don't need individual legal advocacy in the room.</li>
  <li><strong>Collaborative law</strong> is more structured and more lawyer-supported \u2014 better where the legal questions are complex, where the parties want individual advocacy throughout, or where there's a meaningful power or knowledge imbalance.</li>
</ul>
<p>Many families do best with mediation. Some do better with collaborative law. We help you choose.</p>

<h2 id=\"vs-litigation\">Collaborative vs litigation</h2>
<p>Compared with traditional litigation:</p>
<ul>
  <li><strong>Same legal support</strong> \u2014 you have your own lawyer throughout</li>
  <li><strong>Different mindset</strong> \u2014 the lawyers commit to solving, not winning</li>
  <li><strong>Faster</strong> \u2014 no court queues</li>
  <li><strong>Cheaper</strong> \u2014 dramatically</li>
  <li><strong>Private</strong> \u2014 no public court record</li>
  <li><strong>More flexible outcomes</strong> \u2014 you can craft solutions a court couldn't order</li>
</ul>

<h2 id=\"how\">How the process works</h2>
<ol>
  <li><strong>Initial consultations</strong> \u2014 each party meets with their own collaborative lawyer.</li>
  <li><strong>Participation agreement</strong> \u2014 all four sign, committing to the collaborative process and the no-court undertaking.</li>
  <li><strong>Information gathering</strong> \u2014 full financial disclosure between the parties.</li>
  <li><strong>Joint meetings</strong> \u2014 a series of four-way meetings (parties and lawyers) working through the issues.</li>
  <li><strong>Specialist input</strong> \u2014 financial neutrals, child specialists, mental health professionals brought in as needed.</li>
  <li><strong>Agreement</strong> \u2014 documented and formalised through consent orders or BFA.</li>
</ol>

<h2 id=\"commitment\">The collaborative commitment</h2>
<p>The participation agreement is the heart of it. Everyone agrees:</p>
<ul>
  <li><strong>No court</strong> \u2014 the matter is to be resolved without filing.</li>
  <li><strong>Lawyers withdraw if litigation begins</strong> \u2014 a real consequence that aligns everyone's incentives.</li>
  <li><strong>Full disclosure</strong> \u2014 nothing held back to give tactical advantage.</li>
  <li><strong>Good faith</strong> \u2014 genuine engagement, not posturing.</li>
  <li><strong>Confidentiality</strong> \u2014 what's discussed stays in the process.</li>
</ul>
""" + callout("The withdrawal rule changes everything","The fact that the lawyers must withdraw if anyone goes to court isn't a technicality \u2014 it's the structural feature that aligns everyone's incentives toward solving rather than positioning. It's what makes collaborative law different from \"litigation with a friendly face\".") + """

<h2 id=\"suits\">Who it suits</h2>
<ul>
  <li>Couples who want individual legal advocacy but not a court fight</li>
  <li>Complex financial matters where ongoing legal input helps</li>
  <li>Significant power or knowledge imbalances between the parties</li>
  <li>Where one party wants their own legal advisor in the room throughout</li>
  <li>Where multidisciplinary input (finances, kids, mental health) is genuinely needed</li>
</ul>
""" + inline_cta("Not sure whether collaborative law or mediation suits you? We'll help you choose \u2014 honestly.") + """

<h2 id=\"costs\">Costs and timeframes</h2>
<p>Collaborative law costs more than mediation (two lawyers throughout) and less than litigation (no court process). Typical total: $15,000\u2013$40,000 across both parties, vs $100,000+ each for contested litigation. Timeframes are typically a few months from start to formalised agreement.</p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a consultation to understand your situation and assess whether collaborative law, mediation, or another approach suits best. We don't push everyone into the same process \u2014 different families need different paths.</p>
""",
    faq_items=[
        ("What is collaborative family law?","A structured non-litigation process where each party has their own lawyer, but all parties and lawyers sign a participation agreement committing to resolve the matter without court."),
        ("How is it different from mediation?","In mediation you work with a single neutral mediator. In collaborative law you each have your own lawyer, and the parties work through the matter together with that legal support."),
        ("What happens if collaborative law doesn't work?","The collaborative lawyers must withdraw if either party files in court. This is the structural feature that aligns everyone's incentives toward resolution."),
        ("Is the outcome legally binding?","The agreement reached is documented and then formalised through consent orders or a binding financial agreement, giving it the full legal effect of a court order or contract."),
        ("How much does collaborative law cost?","More than mediation (two lawyers throughout) but dramatically less than litigation. Typical total: $15,000\u2013$40,000 across both parties, vs $100,000+ each for contested matters."),
        ("How long does it take?","Typically a few months from start to formalised agreement, depending on complexity and how many joint meetings are needed."),
        ("Is collaborative law right for every separation?","No. For many separating couples mediation is faster, leaner and cheaper. Collaborative law suits where legal complexity, power imbalances, or a desire for individual advocacy make the lawyer-supported model worthwhile."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("accredited-family-law-mediators","Accredited Mediators"),
        ("financial-agreements-mediation","Financial Agreements"),
        ("consent-orders","Consent Orders"),
        ("mediate-or-litigate","Mediate or Litigate?"),
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("preparing-for-mediation","Preparing for Mediation"),
        ("best-divorce-lawyers-sydney","Best Divorce Lawyers in Sydney"),
    ],
)


# ====================================================================
# 18. DIVORCE COUNSELLING
# ====================================================================
service_page(
    slug="divorce-counselling",
    title="Divorce Counselling in Australia | Mediations Australia",
    desc="Emotional and psychological support through separation \u2014 counselling that runs alongside the legal process. Confidential, professional, evidence-based. Free consultation.",
    breadcrumb_label="Divorce Counselling",
    eyebrow="Support",
    h1_html='Divorce Counselling \u2014 <em>the other side of separation</em>.',
    lede="Separation is a legal process and an emotional one. The legal side gets the attention; the emotional side often gets squeezed in around the edges. Counselling makes space for the harder work: grief, identity, kids, what comes next. It runs alongside the legal process, not after it.",
    toc_items=[
        ("what-is","What divorce counselling is"),
        ("who","Who it's for"),
        ("kinds","Different kinds of counselling"),
        ("how","How it works"),
        ("alongside","Alongside mediation"),
        ("children","Counselling for the children"),
        ("when","When to start"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Divorce counselling provides emotional and psychological support through separation \u2014 individual counselling, couples sessions (sometimes), and child-focused work. It runs alongside the legal and financial process of separation, not instead of it. Most people find counselling makes the practical decisions easier, the kids more resilient, and the transition to whatever comes next more manageable."
    ),
    body_html="""
<h2 id=\"what-is\">What divorce counselling is</h2>
<p>Counselling during separation is professional psychological support \u2014 typically with a psychologist, social worker, or accredited counsellor \u2014 to work through the emotional dimensions of ending a relationship. That includes grief, anger, anxiety, identity, loneliness, parenting concerns, the specific stress of negotiation, and whatever else surfaces.</p>
<p>It's not legal advice, it's not mediation, and it's not relationship counselling aimed at reconciliation. It's targeted support for the human side of separation.</p>
""" + inline_cta("The emotional side of separation deserves its own support. Counselling helps. Talk to us.") + """

<h2 id=\"who\">Who it's for</h2>
<ul>
  <li>Anyone going through separation who's finding the emotional load heavy</li>
  <li>People with anxiety or low mood that's affecting their ability to make clear decisions</li>
  <li>Parents worried about their children's adjustment</li>
  <li>People with histories of trauma where separation reactivates older material</li>
  <li>Anyone navigating high-conflict separation where emotional regulation matters</li>
  <li>People dealing with family violence histories (with appropriate safeguards)</li>
</ul>

<h2 id=\"kinds\">Different kinds of counselling</h2>
<ul>
  <li><strong>Individual counselling</strong> \u2014 working through your own experience.</li>
  <li><strong>Co-parenting counselling</strong> \u2014 occasionally helpful for separated parents focused on the kids.</li>
  <li><strong>Child-focused counselling</strong> \u2014 direct support for the children, age-appropriate.</li>
  <li><strong>Family counselling</strong> \u2014 multi-person sessions where blended families or wider dynamics are involved.</li>
</ul>

<h2 id=\"how\">How it works</h2>
<p>Sessions are confidential and run on a regular cadence \u2014 typically weekly or fortnightly, for as long as you need. There's no fixed program length; counselling is responsive to what you're working on. Online and in-person options are both available.</p>

<h2 id=\"alongside\">Alongside mediation</h2>
<p>Counselling and <a href=\"/family-law-mediation/\">mediation</a> work well together. The mediation handles the legal and practical decisions; counselling supports the emotional capacity to make those decisions clearly. Many people find that doing both, in parallel, gets them through the separation in better shape than tackling either in isolation. Some find counselling beforehand actually makes mediation more productive.</p>
""" + callout("Counselling isn't reconciliation","Divorce counselling is about supporting you through the separation that's happening, not trying to reverse it. It's perfectly compatible with being clear the relationship is over.") + """

<h2 id=\"children\">Counselling for the children</h2>
<p>Children experience separation differently to adults, and they often benefit from professional support \u2014 someone who isn't a parent, who they can speak to about what they're feeling without worrying about either parent's reaction. Child-focused counselling is age-appropriate and works with the child's wider context.</p>
""" + inline_cta("Worried about how the kids are coping? Specialist child counselling can help. Talk to us.") + """

<h2 id=\"when\">When to start</h2>
<p>There's no \"right\" time. Some people start as soon as separation looks likely; others come to it months later when they realise they're stuck. Earlier tends to be easier \u2014 working through emotional material before key decisions are made beats trying to repair after. But \"earlier is better\" doesn't mean \"only valuable if you started early.\"</p>

<h2 id=\"get-started\">Getting started</h2>
<p>The first step is a conversation to understand what kind of support would help most. We work with experienced counsellors and psychologists across Australia, and we'll point you to the right kind of help.</p>
""",
    faq_items=[
        ("Is divorce counselling the same as couples counselling?","No. Couples counselling typically aims at the relationship; divorce counselling supports you through the ending of one. They're different goals."),
        ("Do I need a referral from my GP?","Not for private counselling. For Medicare-rebated sessions with a psychologist, you'll need a mental health plan from your GP."),
        ("Is it covered by Medicare?","Mental health treatment plans through a GP can provide Medicare rebates for a number of sessions with a psychologist each year. Counsellors and social workers may not attract the rebate but are often more affordable."),
        ("Is counselling confidential?","Yes \u2014 standard confidentiality protections apply, with the usual exceptions for safety risks. Anything discussed in counselling generally can't be used in court."),
        ("Can children attend counselling?","Yes, with appropriate consents. Child counselling is age-appropriate and run by practitioners specifically trained for working with children."),
        ("How long should counselling continue?","As long as is useful. Some people work through key issues in 6\u201312 sessions; others find longer-term support helpful, particularly through complex separations or where children's needs evolve."),
        ("Can I do counselling while also mediating?","Yes \u2014 they complement each other well. Mediation handles the practical decisions; counselling supports the emotional capacity to make them clearly."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("separation-guide","Separation: Complete Guide"),
        ("mediation-with-a-narcissist","Mediation with a Narcissist"),
        ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
        ("getting-ready-for-separation","Getting Ready for Separation"),
        ("preparing-for-mediation","Preparing for Mediation"),
        ("how-mediation-works","How Mediation Works"),
        ("contact-us","Contact"),
    ],
)

print("\nBatch 3 service cornerstones built (7 pages).")
