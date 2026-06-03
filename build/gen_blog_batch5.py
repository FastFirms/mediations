#!/usr/bin/env python3
"""Batch 5 cornerstones: separation guide, de facto, spousal maintenance, child support."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- SEPARATION GUIDE (absorbs 9) ----
post("separation-guide",
 "Separation in Australia: The Complete Guide (2026)",
 "Separating in Australia? A complete guide to your first steps: the date of separation, who pays the bills, who stays in the house, updating your will, and protecting yourself.",
 "Separation",
 "Separation in Australia: <em>The Complete Guide</em>",
 "Separation is one of life's hardest transitions \u2014 and one of the most practical. This guide covers what separation legally means, the first steps to take, who pays what, who stays in the home, and how to protect yourself financially and emotionally while you work out the path forward.",
 [("what-is","What does separation mean?"),
  ("date","Why the date of separation matters"),
  ("first-steps","First practical steps"),
  ("bills","Who pays the bills during separation?"),
  ("house","Who stays in the house?"),
  ("protect","Protecting yourself"),
  ("next","What comes next")],
 key_takeaway("Separation means the end of a relationship, and it can happen even while living under one roof. The date of separation matters because it starts time limits for property and divorce. Practical priorities are securing finances, sorting interim arrangements for bills and the home, updating your will, and reaching agreement on parenting and property \u2014 ideally through mediation.")
 + """
<h2 id="what-is">What does separation mean?</h2>
<p>Separation is the point at which at least one partner decides the relationship is over and acts on that decision. There's no form to file to "become separated" \u2014 it happens in fact, not on paper. You can even be <a href="/separation-under-one-roof/">separated while still living in the same house</a>, which is common for financial reasons or for the children's stability.</p>
"""
 + inline_cta("Just separated and not sure where to start? A consultation will help you map your next steps calmly.")
 + f"""
<h2 id="date">Why the date of separation matters</h2>
<p>Your date of separation is more than symbolic \u2014 it has legal consequences. It starts the 12-month clock you need before you can apply for divorce, and it begins the time limits for property settlement (two years from separation for <a href="/de-facto-relationships-guide/">de facto couples</a>). It can also affect how contributions after separation are assessed, and the {cite('aifs')} documents how common and significant this life transition is. Where the date is unclear \u2014 especially with separation under one roof \u2014 it's worth getting advice early. The {cite("family_law_act")} governs how these timeframes apply.</p>

<h2 id="first-steps">First practical steps</h2>
<ol>
  <li><strong>Secure your important documents</strong> \u2014 ID, financial records, tax returns, superannuation statements.</li>
  <li><strong>Understand your finances</strong> \u2014 list assets, debts and accounts so you know the full picture.</li>
  <li><strong>Think about the children</strong> \u2014 stability and routine matter most in the early days.</li>
  <li><strong>Consider interim arrangements</strong> \u2014 who lives where, and how bills are covered, while things settle.</li>
  <li><strong>Get early guidance</strong> \u2014 understanding your options prevents costly missteps. <a href="/getting-ready-for-separation/">See our separation checklist \u2192</a></li>
</ol>
"""
 + callout("Separation isn't divorce",
   "You can be separated indefinitely without divorcing. Divorce is a separate legal step that formally ends the marriage \u2014 and it doesn't, by itself, resolve property or parenting. See our divorce guide for that process.")
 + """
<h2 id="bills">Who pays the bills during separation?</h2>
<p>There's no automatic rule, and this is a frequent flashpoint. In the interim, the sensible approach is to maintain the status quo where possible \u2014 keep paying joint commitments like the mortgage to protect both parties' credit and the asset itself \u2014 while you negotiate a fair arrangement. Where one partner controlled the finances, interim spousal maintenance may be appropriate. These interim questions are exactly the kind of thing mediation resolves quickly. <a href="/spousal-maintenance-guide/">See spousal maintenance \u2192</a></p>

<h2 id="house">Who stays in the house?</h2>
<p>Neither partner is automatically required to leave the family home, and leaving doesn't mean giving up your claim to it. Who stays in the short term is often a practical decision \u2014 but if there's family violence, safety changes everything and protective orders can determine occupation. Mediation can help reach a workable interim arrangement without escalation. <a href="/domestic-violence-and-family-law/">If safety is a concern, read this \u2192</a></p>
"""
 + inline_cta("Disagreeing about the house or the bills? Mediation settles interim arrangements fast \u2014 book a consultation.")
 + """
<h2 id="protect">Protecting yourself</h2>
<ul>
  <li><strong>Update your will</strong> \u2014 separation doesn't automatically revoke gifts to an ex in every state; review it promptly.</li>
  <li><strong>Review beneficiary nominations</strong> on superannuation and insurance.</li>
  <li><strong>Protect your privacy</strong> \u2014 change passwords and secure your personal accounts.</li>
  <li><strong>Keep records</strong> \u2014 of finances and important communications.</li>
  <li><strong>Look after your wellbeing</strong> \u2014 lean on support, including <a href="/divorce-counselling/">counselling</a>.</li>
</ul>

<h2 id="next">What comes next</h2>
<p>Once the immediate practicalities are stable, the substantive questions \u2014 dividing property and finalising parenting \u2014 come into focus. For the vast majority of people, <a href="/family-law-mediation/">mediation</a> is the fastest, least costly and least damaging way to resolve them. <a href="/property-settlement-after-separation/">See property settlement after separation \u2192</a></p>
"""
 ,
 [("Do I have to leave the house when I separate?",
   "No. Neither partner is automatically required to leave the family home, and leaving doesn't forfeit your claim to it. If there's family violence, safety and protective orders change this."),
  ("Who pays the bills after separation?",
   "There's no automatic rule. Maintaining joint commitments like the mortgage in the interim is usually sensible. Where one partner controlled finances, interim spousal maintenance may apply."),
  ("Why does the date of separation matter?",
   "It starts the 12-month period before you can apply for divorce and begins time limits for property settlement. It can also affect how post-separation contributions are assessed."),
  ("Can I be separated but still live together?",
   "Yes. Separation under one roof is recognised in Australia. You may need to show the relationship has genuinely ended despite sharing a home."),
  ("Should I update my will after separating?",
   "Yes, promptly. Separation does not automatically revoke gifts to an ex in every state, so review your will and beneficiary nominations.")],
 [("getting-ready-for-separation","Getting Ready for Separation"),
  ("separation-under-one-roof","Separation Under One Roof"),
  ("property-settlement-after-separation","Property Settlement"),
  ("spousal-maintenance-guide","Spousal Maintenance"),
  ("family-law-mediation","Family Law Mediation"),
  ("divorce-counselling","Divorce Counselling")],
 read_min=10)
print("separation-guide built")

# ---- DE FACTO RELATIONSHIPS GUIDE (absorbs 3) ----
post("de-facto-relationships-guide",
 "De Facto Relationships and Separation in Australia (2026)",
 "De facto rights in Australia: what counts as a de facto relationship, how assets are split, time limits, and how de facto law compares to marriage. Complete 2026 guide.",
 "De facto",
 "De Facto Relationships and Separation in Australia",
 "De facto couples have substantially the same property and financial rights as married couples in Australia \u2014 many people don't realise this. This guide explains what legally counts as a de facto relationship, how assets are divided when you separate, the strict time limits, and how it all compares to marriage.",
 [("what-is","What is a de facto relationship?"),
  ("rights","What rights do de facto couples have?"),
  ("split","How are de facto assets split?"),
  ("time-limit","The two-year time limit"),
  ("vs-marriage","De facto vs marriage"),
  ("protect","Protecting yourself")],
 key_takeaway("A de facto relationship exists where two people live together on a genuine domestic basis without being married. Under the Family Law Act, de facto couples have substantially the same property, superannuation and maintenance rights as married couples. The key difference is the time limit: de facto couples generally have two years from separation to apply for a property settlement.")
 + f"""
<h2 id="what-is">What is a de facto relationship?</h2>
<p>Under the {cite("family_law_act")}, a de facto relationship exists where two people (of any gender) live together on a genuine domestic basis and are not married to each other. No single factor decides it \u2014 a court looks at the whole picture: how long you were together, whether you lived together, the nature of the financial arrangements, whether there was a sexual relationship, shared property, children, and how the relationship was presented publicly.</p>
<p>Generally, you need to have been in the relationship for at least two years, or have a child together, or have made substantial contributions \u2014 for the property regime to apply.</p>
"""
 + inline_cta("Unsure whether your relationship qualifies as de facto? We'll help you understand where you stand.")
 + """
<h2 id="rights">What rights do de facto couples have?</h2>
<p>This surprises many people: de facto couples have substantially the same rights as married couples when it comes to property settlement, superannuation splitting and spousal maintenance. The same <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">four-step process</a> applies to dividing assets. Being unmarried does not mean walking away with only what's in your name — a point reinforced across <a href="https://www.fcfcoa.gov.au/" target="_blank" rel="noopener">Federal Circuit and Family Court</a> property matters.</p>

<h2 id="split">How are de facto assets split?</h2>
<p>Exactly as for married couples: identify the asset pool, assess contributions (financial and non-financial), consider future needs, and check the result is just and equitable. There's no automatic 50/50. <a href="/property-settlement-after-separation/">See the full property settlement guide \u2192</a> and resolve it through <a href="/de-facto-mediation/">de facto mediation</a> rather than court.</p>
"""
 + callout("The two-year limit is stricter than for marriage",
   "De facto couples must generally apply within two years of separation \u2014 there's no divorce step to reset the clock. Miss it and you need the court's permission, which isn't guaranteed. Act promptly.")
 + """
<h2 id="time-limit">The two-year time limit</h2>
<p>This is the single most important practical difference. De facto couples generally have <strong>two years from the date of separation</strong> to apply for a property settlement or maintenance. Because there's no divorce process to mark the timeline, it's easy to let the limit slip by. If you're separating from a de facto partner, treat the clock as already running.</p>

<h2 id="vs-marriage">De facto vs marriage</h2>
<p>The rights are largely the same; the differences are mostly procedural. Married couples divorce (and have 12 months after divorce for property); de facto couples don't divorce but have two years from separation. Proving a de facto relationship existed can itself sometimes be contested, whereas marriage is a matter of record. <a href="/financial-agreements-mediation/">A binding financial agreement can provide certainty either way \u2192</a></p>
"""
 + inline_cta("Separating from a de facto partner? The two-year clock is ticking \u2014 book a consultation today.")
 + """
<h2 id="protect">Protecting yourself</h2>
<p>Whether you're entering, in, or leaving a de facto relationship, you can protect your position. A <a href="/binding-financial-agreements-guide/">binding financial agreement</a> can set out how assets would be divided. On separation, mediation lets you reach a fair settlement quickly and formalise it through consent orders or an agreement \u2014 well inside the two-year window. <a href="/de-facto-mediation/">See de facto mediation \u2192</a></p>
"""
 ,
 [("What counts as a de facto relationship in Australia?",
   "Two people living together on a genuine domestic basis without being married. Courts weigh duration, cohabitation, finances, children and public aspects. Generally two years together, a child, or substantial contributions brings the property regime into play."),
  ("Do de facto couples have the same rights as married couples?",
   "Substantially, yes \u2014 for property settlement, superannuation splitting and spousal maintenance the same Family Law Act framework applies. The main difference is the time limit."),
  ("How are assets divided when de facto couples separate?",
   "Using the same four-step process as married couples: identify the pool, assess contributions, consider future needs, and ensure the result is just and equitable. There's no automatic 50/50."),
  ("What is the time limit for de facto property claims?",
   "Generally two years from the date of separation. After that you need the court's permission to apply, which isn't guaranteed."),
  ("How do I prove a de facto relationship existed?",
   "Through evidence of living together, shared finances, the length of the relationship, children, and how the relationship was presented publicly. No single factor is decisive.")],
 [("de-facto-mediation","De Facto Mediation"),
  ("property-settlement-after-separation","Property Settlement"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("binding-financial-agreements-guide","Binding Financial Agreements"),
  ("financial-agreements-mediation","Financial Agreements Mediation"),
  ("separation-guide","Separation Guide")],
 read_min=9)
print("de-facto-relationships-guide built")

# ---- SPOUSAL MAINTENANCE GUIDE (absorbs 3) ----
post("spousal-maintenance-guide",
 "Spousal Maintenance in Australia: Who Pays and How Much? (2026)",
 "Spousal maintenance in Australia explained: who is eligible, how much is paid, how long it lasts, and how it differs from child support. Complete 2026 guide.",
 "Property &amp; finances",
 "Spousal Maintenance in Australia: <em>Who Pays, and How Much?</em>",
 "Spousal maintenance is financial support one partner may pay the other after separation, where one can't adequately support themselves and the other has the capacity to help. It's separate from child support and from the property split. Here's who's eligible, how it's calculated, and how long it lasts.",
 [("what-is","What is spousal maintenance?"),
  ("eligible","Who is eligible?"),
  ("how-much","How much is paid?"),
  ("how-long","How long does it last?"),
  ("vs-child-support","Spousal maintenance vs child support"),
  ("de-facto","Does it apply to de facto couples?"),
  ("agree","How to agree it without court")],
 key_takeaway("Spousal maintenance is support paid by one former partner to the other where the recipient cannot adequately meet their own reasonable needs and the payer has the capacity to pay. It's assessed on need and capacity \u2014 not a fixed formula \u2014 and is separate from child support and the property settlement. It can be a lump sum or periodic, and is often time-limited.")
 + f"""
<h2 id="what-is">What is spousal maintenance?</h2>
<p>Spousal maintenance (sometimes loosely called "alimony", a US term) is financial support one spouse or de facto partner pays the other after separation. It exists to address a genuine imbalance: where one person can't adequately support themselves and the other has the capacity to help. It is governed by the {cite("family_law_act")} and is distinct from both child support and the division of property.</p>
"""
 + inline_cta("Wondering if you can claim \u2014 or might have to pay \u2014 spousal maintenance? Get clarity in a consultation.")
 + """
<h2 id="eligible">Who is eligible?</h2>
<p>Eligibility turns on two questions working together:</p>
<ul>
  <li><strong>Need:</strong> can the applicant reasonably meet their own living expenses from their income and resources?</li>
  <li><strong>Capacity:</strong> can the other party afford to pay after meeting their own reasonable needs?</li>
</ul>
<p>The court also considers factors like age, health, income, earning capacity, the care of children, and the standard of living during the relationship. Maintenance isn't automatic \u2014 it must be justified on these grounds.</p>

<h2 id="how-much">How much is paid?</h2>
<p>Unlike child support, there's no fixed formula. The amount reflects the gap between the recipient's reasonable needs and their capacity to meet them, limited by the payer's ability to pay. It can be ordered as a lump sum or as periodic (e.g. monthly) payments. Because it's discretionary and fact-specific, it's an area where reaching agreement through <a href="/spousal-support-mediation/">mediation</a> often produces a fairer, faster result than litigation.</p>
"""
 + callout("It's about need and capacity \u2014 not punishment",
   "Spousal maintenance isn't a reward or a penalty. It's a practical adjustment to help a financially weaker partner transition to independence, for as long as that genuinely takes.")
 + """
<h2 id="how-long">How long does it last?</h2>
<p>Often it's time-limited \u2014 designed to support the recipient while they retrain, re-enter the workforce, or otherwise move toward self-sufficiency. It can be reviewed if circumstances change significantly (the <a href="https://www.fcfcoa.gov.au/" target="_blank" rel="noopener">Federal Circuit and Family Court</a> handles these applications), and it generally ends if the recipient remarries (and may be affected by entering a new de facto relationship). Permanent maintenance is uncommon and usually reserved for cases of age or incapacity.</p>

<h2 id="vs-child-support">Spousal maintenance vs child support</h2>
<p>They're frequently confused but are entirely separate. <a href="/child-support-guide/">Child support</a> is for the children's costs and is calculated by a formula administered by Services Australia. Spousal maintenance is for an adult former partner's own support and is assessed on need and capacity. You can be entitled to one, both, or neither.</p>
"""
 + inline_cta("Spousal maintenance is rarely clear-cut. Let us help you reach a fair figure without a court fight.")
 + """
<h2 id="de-facto">Does it apply to de facto couples?</h2>
<p>Yes. De facto partners can claim maintenance on the same need-and-capacity basis as married couples \u2014 subject to the usual <a href="/de-facto-relationships-guide/">de facto time limits</a> (generally two years from separation). <a href="/de-facto-mediation/">See de facto mediation \u2192</a></p>

<h2 id="agree">How to agree it without court</h2>
<p>Because spousal maintenance is discretionary, it's well suited to negotiated agreement. Through <a href="/spousal-support-mediation/">spousal support mediation</a> you can agree an amount and duration that works for both of you, then formalise it in <a href="/consent-orders-explained/">consent orders</a> or a <a href="/binding-financial-agreements-guide/">binding financial agreement</a> \u2014 avoiding the cost and uncertainty of a court determination.</p>
"""
 ,
 [("What is spousal maintenance?",
   "Financial support one former partner pays the other after separation, where the recipient can't adequately support themselves and the payer has the capacity to pay. It's separate from child support and the property split."),
  ("Who has to pay spousal maintenance?",
   "A former partner who has the financial capacity to pay, where the other genuinely cannot meet their reasonable needs. It's assessed on need and capacity, not automatically owed."),
  ("How much spousal maintenance is paid?",
   "There's no fixed formula. It reflects the gap between the recipient's reasonable needs and their own capacity, limited by the payer's ability to pay. It can be a lump sum or periodic."),
  ("How long does spousal maintenance last?",
   "Often time-limited to support a transition to self-sufficiency. It can be reviewed if circumstances change and generally ends on remarriage. Permanent maintenance is uncommon."),
  ("Is spousal maintenance the same as child support?",
   "No. Child support is for children's costs and is formula-based via Services Australia. Spousal maintenance is for an adult partner's own support, assessed on need and capacity.")],
 [("spousal-support-mediation","Spousal Support Mediation"),
  ("child-support-guide","Child Support Guide"),
  ("property-settlement-after-separation","Property Settlement"),
  ("de-facto-relationships-guide","De Facto Relationships"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("financial-agreements-mediation","Financial Agreements Mediation")],
 read_min=9)
print("spousal-maintenance-guide built")

# ---- CHILD SUPPORT GUIDE (absorbs 4) ----
post("child-support-guide",
 "Child Support in Australia: How It Works (2026 Guide)",
 "How child support works in Australia: the formula, how payments are assessed, when it stops, and how to resolve disputes. Complete 2026 guide for separated parents.",
 "Parenting",
 "Child Support in Australia: <em>How It Works</em>",
 "Child support helps cover the costs of raising children after separation. In Australia it's calculated by a formula administered by Services Australia, based on both parents' incomes and care arrangements. This guide explains how it's assessed, when it stops, and how to resolve disputes without conflict.",
 [("what-is","What is child support?"),
  ("formula","How is child support calculated?"),
  ("care","How care arrangements affect it"),
  ("private","Self-managed vs agency collection"),
  ("stops","When does child support stop?"),
  ("disputes","Resolving child support disputes"),
  ("vs-spousal","Child support vs spousal maintenance")],
 key_takeaway("Child support in Australia is calculated by a formula administered by Services Australia, based on both parents' incomes, the cost of children, and the percentage of care each parent provides. It can be self-managed by agreement or collected by the agency. It generally continues until the child turns 18, and is separate from spousal maintenance.")
 + f"""
<h2 id="what-is">What is child support?</h2>
<p>Child support is a financial contribution toward the costs of raising children whose parents have separated. The system is administered by {cite("services_australia_cs")}, and the underlying principle (supported by <a href="https://aifs.gov.au/" target="_blank" rel="noopener">family studies research</a>) is simple: both parents share responsibility for supporting their children financially, in proportion to their capacity and the care they provide.</p>
"""
 + inline_cta("Child support questions tangled up with parenting arrangements? Mediation can resolve both together.")
 + """
<h2 id="formula">How is child support calculated?</h2>
<p>The standard formula takes into account:</p>
<ul>
  <li>Both parents' taxable incomes (with a self-support amount set aside for each)</li>
  <li>The cost of children, based on research-derived figures</li>
  <li>The percentage of care each parent provides</li>
  <li>The number and ages of the children</li>
</ul>
<p>The result is an assessment of how much one parent pays the other. Because it's formula-based, child support is more predictable than spousal maintenance \u2014 but the inputs (especially income and care percentages) can still be the subject of dispute.</p>

<h2 id="care">How care arrangements affect it</h2>
<p>The percentage of care each parent provides directly affects the assessment \u2014 more care generally means paying less (or receiving more), because you're already meeting costs directly. This is why child support and <a href="/parenting-plans-guide/">parenting arrangements</a> are closely linked, and why resolving them together through mediation makes sense.</p>
"""
 + callout("Care percentages and payments are linked",
   "Because care levels feed the formula, disputes about parenting time can become disputes about money. Mediation lets you settle the parenting arrangement and the financial picture in one coherent process.")
 + """
<h2 id="private">Self-managed vs agency collection</h2>
<p>Parents have options for how child support is handled. You can reach a <strong>private agreement</strong> and manage payments yourselves (self-management), enter a formal <strong>child support agreement</strong>, or have Services Australia <strong>assess and/or collect</strong> payments. Many parents prefer a private or agreed arrangement where the relationship allows it \u2014 mediation can help you build one that's fair and durable.</p>

<h2 id="stops">When does child support stop?</h2>
<p>Child support generally continues until a child turns 18. It can end earlier in certain circumstances, and in some cases support for a child completing their final year of school can be extended past 18 on application. Adult child maintenance (for example, for a child with a disability or in tertiary study) is a separate, limited category.</p>
"""
 + inline_cta("Disagreeing about child support or care levels? We'll help you reach a fair, lasting arrangement.")
 + """
<h2 id="disputes">Resolving child support disputes</h2>
<p>Disputes often arise over income (especially where someone is self-employed), care percentages, or special circumstances the formula doesn't capture. There are formal review processes through the agency, but many disputes are resolved faster and with less conflict through <a href="/child-support-mediation/">child support mediation</a> \u2014 particularly when they're bound up with parenting arrangements.</p>

<h2 id="vs-spousal">Child support vs spousal maintenance</h2>
<p>Keep the two separate in your mind: child support is for the <em>children's</em> costs and is formula-based; <a href="/spousal-maintenance-guide/">spousal maintenance</a> is for an adult former partner's <em>own</em> support and is assessed on need and capacity. They can apply together or independently.</p>
"""
 ,
 [("How is child support calculated in Australia?",
   "By a formula administered by Services Australia, based on both parents' incomes, the cost of children, the percentage of care each provides, and the number and ages of the children."),
  ("Does the amount of care affect child support?",
   "Yes. The percentage of care each parent provides feeds directly into the formula \u2014 more care generally means paying less or receiving more, since you're meeting costs directly."),
  ("When does child support stop?",
   "Generally when the child turns 18, though it can end earlier or, on application, be extended to the end of the final school year. Adult child maintenance is a separate limited category."),
  ("Can parents arrange child support privately?",
   "Yes. Parents can self-manage by agreement, enter a formal child support agreement, or use Services Australia to assess and collect. Mediation helps build a fair private arrangement."),
  ("Is child support the same as spousal maintenance?",
   "No. Child support is for children's costs and is formula-based; spousal maintenance is for an adult partner's own support and assessed on need and capacity. They can apply together or separately.")],
 [("child-support-mediation","Child Support Mediation"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("spousal-maintenance-guide","Spousal Maintenance"),
  ("parenting-plan-mediation","Parenting Plan Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=9)
print("child-support-guide built")
