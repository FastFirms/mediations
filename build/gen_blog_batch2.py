#!/usr/bin/env python3
"""Batch 2 cornerstone posts at full depth, built on the blog engine."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- CONSENT ORDERS EXPLAINED ----
post("consent-orders-explained",
 "Consent Orders Explained: How They Work in Australia (2026)",
 "What are consent orders, how do you apply, and what do they cost? A 2026 guide to making your separation agreement legally binding without going to court.",
 "Consent orders",
 "Consent Orders Explained: <em>Making It Legally Binding</em>",
 "Consent orders turn an agreement you've already reached into legally binding court orders \u2014 without anyone setting foot in a courtroom. This guide explains exactly what they are, how to apply, what they cost, how long they take, and how to change or enforce them.",
 [("what-are","What are consent orders?"),
  ("parenting-property","Parenting vs property consent orders"),
  ("how-apply","How to apply: the forms and the portal"),
  ("time-limits","Time limits: the deadline to apply"),
  ("how-long","How long do consent orders take?"),
  ("cost","What do consent orders cost?"),
  ("just-equitable","How the court checks your orders"),
  ("superannuation","Splitting superannuation by consent"),
  ("change","Can you change or set aside consent orders?"),
  ("breach","Enforcing consent orders if someone breaches")],
 key_takeaway("Consent orders are written agreements approved by the Federal Circuit and Family Court that become legally binding without a hearing. They can cover property, finances and parenting. You apply jointly, a registrar checks the terms are just and equitable (for property) or in the child's best interests (for parenting), and the filing fee is modest \u2014 far cheaper than litigation.")
 + f"""
<h2 id="what-are">What are consent orders?</h2>
<p>Consent orders are an agreement between separating parties that a court has approved and turned into formal orders. Once made, they carry the same legal force as orders a judge would impose after a contested hearing \u2014 except you reach them yourselves and avoid the hearing entirely. They can deal with property and financial matters, parenting arrangements for children, or both in the one application.</p>
<p>The point of formalising an agreement this way is certainty. A handshake deal, or even a signed written one, is not automatically enforceable; consent orders are. For property, they also close the door on future claims between you, so neither party can come back years later for a second bite. According to the {cite("fcfcoa_consent_orders")}, the process is designed to be straightforward where the parties already agree \u2014 the court is checking your agreement, not re-running the dispute.</p>
<p>That distinction matters: consent orders are the <em>formalisation</em> step, not the negotiation. The hard part is reaching a fair agreement in the first place. Court has its place for genuine disputes, but where you can agree, consent orders let you keep control of the outcome instead of handing it to a judge.</p>
"""
 + inline_cta("Reached an agreement and want to make it official? We'll help you turn it into binding consent orders.")
 + """
<h2 id="parenting-property">Parenting consent orders vs property consent orders</h2>
<p>Consent orders come in two broad types, and the court applies a different test to each:</p>
<ul>
  <li><strong>Property and financial consent orders</strong> divide assets, debts and superannuation, and can deal with spousal maintenance. The court must be satisfied the division is "just and equitable".</li>
  <li><strong>Parenting consent orders</strong> set out where children live, the time they spend with each parent, and how major decisions about them are made. Here the court's only concern is the best interests of the child.</li>
</ul>
<p>You can apply for one or both, and most separating couples resolve everything together so the whole settlement is locked in at once. Parenting can also be handled less formally through a <a href="/parenting-plan-template/">parenting plan</a>, but a plan is not enforceable the way orders are \u2014 see <a href="/bfa-or-consent-orders/">how the instruments compare</a> if you are weighing your options.</p>
<figure class="tbl"><table><caption>Consent orders vs a binding financial agreement vs a contested court hearing</caption>
<thead><tr><th>&nbsp;</th><th>Consent orders</th><th>Binding financial agreement</th><th>Contested hearing</th></tr></thead>
<tbody>
<tr><td>Legally binding</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Court approves the terms</td><td>Yes (on the papers)</td><td>No (private contract)</td><td>Yes (a judge decides)</td></tr>
<tr><td>Independent legal advice required</td><td>No</td><td>Yes, for each party</td><td>Usually represented</td></tr>
<tr><td>Can cover parenting</td><td>Yes</td><td>No (financial only)</td><td>Yes</td></tr>
<tr><td>Typical cost</td><td>~$200 filing fee + preparation</td><td>Higher (two lawyers advise)</td><td>Tens of thousands</td></tr>
<tr><td>You keep control of the outcome</td><td>Yes</td><td>Yes</td><td>No</td></tr>
</tbody></table></figure>
"""
 + inline_cta("Already agreed on how to split things, or how the children's time will work? We'll turn it into binding consent orders — property, parenting, or both.")
 + f"""
<h2 id="how-apply">How to apply: the forms and the portal</h2>
<p>When both parties agree, applying for consent orders is largely a paperwork exercise \u2014 there is no hearing to attend. The steps are:</p>
<ol>
  <li><strong>Reach a clear agreement</strong> \u2014 ideally through <a href="/family-law-mediation/">mediation</a>, the most efficient way to settle every term and get it written down.</li>
  <li><strong>Exchange full financial disclosure</strong> (for property) \u2014 each party must honestly set out their assets, liabilities, income and superannuation. The {cite("fcfcoa_disclosure")} makes this an ongoing duty, and orders made on incomplete disclosure can later be set aside.</li>
  <li><strong>Prepare the documents</strong> \u2014 an Application for Consent Orders, which gives the court your financial and family details, plus a Minute of Consent Orders (the "minute of order") setting out the exact terms you want made.</li>
  <li><strong>File online</strong> \u2014 the application is lodged electronically through the {cite("comcourts_portal")}, with the filing fee paid at lodgement.</li>
  <li><strong>Registrar review</strong> \u2014 a court registrar reads the application on the papers to check the orders are appropriate. You do not appear.</li>
  <li><strong>Orders made and sealed</strong> \u2014 once approved, the orders are sealed with the court's stamp and are legally binding from that date.</li>
</ol>
<p>Getting the Minute right is where applications most often stumble: vague, unworkable or one-sided terms can prompt the registrar to ask questions or decline to make the orders, which costs weeks. A precisely drafted minute that reflects a fair, mediated agreement usually goes through cleanly.</p>
<figure class="tbl"><table><caption>What you file for consent orders</caption>
<thead><tr><th>Document</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>Application for Consent Orders</td><td>Gives the court your personal, family and financial details so it can assess the orders</td></tr>
<tr><td>Minute of Consent Orders</td><td>Sets out the exact orders you ask the court to make \u2014 the operative terms</td></tr>
<tr><td>Financial disclosure</td><td>Each party's assets, liabilities, income and superannuation (for property matters)</td></tr>
<tr><td>Superannuation documents</td><td>Where super is split: a valuation and notice to the fund trustee</td></tr>
</tbody></table></figure>
"""
 + inline_cta("We prepare consent order applications that satisfy the court the first time \u2014 no costly back-and-forth.")
 + f"""
<h2 id="time-limits">Time limits: the deadline to apply</h2>
<p>Property consent orders have a deadline, and it catches people out. Under the {cite("family_law_act")}:</p>
<figure class="tbl"><table><caption>Deadline to apply for property consent orders</caption>
<thead><tr><th>Situation</th><th>Deadline to apply</th></tr></thead>
<tbody>
<tr><td>Married couples</td><td>Within 12 months of the divorce becoming final</td></tr>
<tr><td>De facto couples</td><td>Within 24 months of the date of separation</td></tr>
<tr><td>Parenting arrangements</td><td>No time limit \u2014 best interests apply at any time</td></tr>
</tbody></table></figure>
<p>Applying after the deadline is not impossible, but you need the court's permission ("leave"), which is not guaranteed and adds cost and delay. Parenting orders have no equivalent time limit \u2014 a child's best interests can be addressed at any time \u2014 but it is always better to formalise arrangements while everyone is cooperating. If your deadline is approaching, don't let the paperwork drift. <a href="/property-settlement-after-separation/">Read our property settlement guide \u2192</a></p>

<h2 id="how-long">How long do consent orders take?</h2>
<p>Once filed, consent orders are typically processed within a few weeks, though timeframes shift with the court's workload at the time. There is no hearing date to wait for \u2014 a registrar simply reviews the papers when your application reaches the front of the queue.</p>
<p>The real variable is how long it takes to <em>reach</em> the agreement in the first place. That is where months can disappear if matters are left to drift or to lawyers' letters going back and forth. Mediation compresses that stage from months into a session or two, and then the formalisation is quick. <a href="/how-long-does-mediation-take/">See how long mediation takes \u2192</a></p>
"""
 + inline_cta("The faster you reach agreement, the faster it's sealed. A mediation session or two is usually all it takes.")
 + callout("Not sure whether to use consent orders or a BFA?",
   "Both make a financial settlement binding. Consent orders are court-approved and usually cheaper; a binding financial agreement is a private contract that offers more flexibility but requires independent legal advice for each party. Our BFA-or-consent-orders guide walks through which suits which situation.")
 + f"""
<h2 id="cost">What do consent orders cost?</h2>
<p>The court filing fee for an Application for Consent Orders is modest \u2014 around $200 \u2014 and is set out in the {cite("fcfcoa_fees")}. Fee reductions are available for people who hold certain concession cards or would face financial hardship. On top of the filing fee, your main cost is preparing the documents: a well-drafted Minute is worth the investment, because it is what makes the orders work.</p>
<p>Set that against a contested property case, which can consume tens of thousands of dollars \u2014 often a meaningful slice of the very asset pool you are dividing. Consent orders are one of the cheapest, most durable ways to lock in certainty. <a href="/our-fee-structure/">See our transparent fees \u2192</a></p>
"""
 + inline_cta("Curious what your matter would cost to formalise? Book a fixed-fee consultation and we'll give you a straight answer.")
 + f"""
<h2 id="just-equitable">How the court checks your orders</h2>
<p>A registrar will not simply rubber-stamp whatever you submit \u2014 and that protection is a feature, not an obstacle. For <strong>property</strong>, the orders must be "just and equitable" under the {cite("family_law_act")}. In practice the court works through a familiar four-step approach: identify and value the asset pool; weigh each party's financial and non-financial contributions; consider future needs (things like the care of children, age, health and earning capacity); then stand back to check the overall result is fair.</p>
<p>For <strong>parenting</strong>, the only test is the best interests of the child. The factors the court weighs were reshaped by recent reforms to the {cite("family_law_act")} \u2014 <a href="/changes-to-family-law-act-2025/">see what changed</a>. A well-prepared application that reflects a genuinely fair, child-focused agreement generally satisfies the registrar without difficulty. <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">Learn what a fair division looks like \u2192</a></p>

<h2 id="superannuation">Splitting superannuation by consent</h2>
<p>Superannuation is treated as property under Australian family law, so it can be divided by consent orders just like other assets. A super split moves a portion of one person's superannuation into the other's fund; it does not turn super into cash, and the split amount stays preserved under the normal superannuation rules until a condition of release is met.</p>
<p>Two practical points trip people up. First, you generally need to <strong>value the interest</strong> properly before splitting it \u2014 especially for defined-benefit funds. Second, the law requires you to give the superannuation fund's trustee <strong>procedural fairness</strong>: the trustee must be notified of the proposed orders and given the chance to object before the court makes them. Building these steps in from the start avoids a knock-back. <a href="/superannuation-and-divorce/">Read our superannuation and divorce guide \u2192</a></p>
"""
 + inline_cta("Superannuation splits have technical traps. We'll make sure your orders are drafted so the fund and the court both accept them.")
 + f"""
<h2 id="change">Can you change or set aside consent orders?</h2>
<p>Yes, but not casually \u2014 and the difference between property and parenting matters.</p>
<p><strong>Financial consent orders are usually final.</strong> That finality is the whole point: both of you can move on knowing the settlement is closed. A court will only set them aside in the limited circumstances set out in the {cite("family_law_act")} \u2014 for example fraud or a failure to disclose assets, duress, a later event that makes the orders impracticable to carry out, or a default in performance. This is also why honest, complete disclosure at the start protects you: orders built on hidden assets are vulnerable.</p>
<p><strong>Parenting consent orders can be changed</strong> where there has been a significant change in circumstances and it is in the child's best interests \u2014 ideally by fresh agreement (often revisited through mediation) rather than by going back to court. Children grow and lives shift, and the orders can evolve with them.</p>
"""
 + inline_cta("Circumstances changed and your orders no longer fit? Mediation can update them by agreement, without a court fight.")
 + f"""
<h2 id="breach">Enforcing consent orders if someone breaches</h2>
<p>Because consent orders are court orders, ignoring them carries real consequences. For <strong>parenting orders</strong>, the other parent can file a contravention application; if a breach is proven without reasonable excuse, outcomes range from make-up time and attendance at a parenting program through to bonds, fines and, in the most serious cases, imprisonment. For <strong>financial orders</strong>, the court has enforcement mechanisms to compel payment or the transfer of property.</p>
<p>Enforcement is the last resort, not the first. Where a breach reflects a genuine change in circumstances or a misunderstanding, returning to mediation is usually the faster, cheaper way to resolve it \u2014 and often the way to update the orders so the problem does not recur. <a href="/family-law-mediation/">Talk to us about resolving a breach \u2192</a></p>
"""
 ,
 [("What are consent orders in Australia?",
   "Consent orders are a written agreement approved by the Federal Circuit and Family Court that becomes legally binding without a hearing. They can cover property, finances and parenting arrangements."),
  ("Is there a time limit to apply for consent orders?",
   "Yes, for property. Married couples have 12 months from the date their divorce becomes final; de facto couples have 24 months from separation. Applying later needs the court's permission. Parenting orders have no time limit."),
  ("How long do consent orders take?",
   "Once filed, they're typically processed within a few weeks, depending on court workload. Reaching the underlying agreement \u2014 best done through mediation \u2014 is usually the longer part."),
  ("How much do consent orders cost?",
   "The court filing fee is modest (around $200), plus any cost of preparing the documents. This is far cheaper than a contested property case, and fee reductions are available in cases of hardship."),
  ("Do I need a lawyer to get consent orders?",
   "No, you can apply yourselves \u2014 but the application and the Minute of Consent Orders must be drafted correctly, or the registrar may decline them. Many people have a mediator or lawyer prepare the documents while keeping the process out of court."),
  ("Can consent orders include superannuation?",
   "Yes. Superannuation is treated as property and can be split by consent orders. The interest usually needs to be valued, and the super fund's trustee must be notified and given the chance to object before the orders are made."),
  ("Can consent orders be changed later?",
   "Financial consent orders are usually final and can only be set aside in limited circumstances such as fraud or non-disclosure. Parenting orders can be varied if circumstances change significantly and it's in the child's best interests."),
  ("What happens if my ex breaches consent orders?",
   "Because they're court orders, breaches can be enforced. Parenting breaches can lead to a contravention application; financial orders have enforcement mechanisms. Mediation is often the fastest first step.")],
 [("consent-orders","Consent Orders Service"),
  ("financial-agreements-mediation","Binding Financial Agreements"),
  ("bfa-or-consent-orders","BFA or Consent Orders?"),
  ("property-settlement-after-separation","Property Settlement After Separation"),
  ("superannuation-and-divorce","Superannuation & Divorce"),
  ("how-mediation-works","How Mediation Works")],
 read_min=11)

print("consent-orders-explained built")

# ---- PROPERTY SETTLEMENT AFTER SEPARATION (biggest cluster) ----
post("property-settlement-after-separation",
 "Property Settlement After Separation in Australia (2026 Guide)",
 "A complete guide to property settlement after separation in Australia: the four-step process, what's in the asset pool, time limits, disclosure, super, and how to settle without court.",
 "Property &amp; finances",
 "Property Settlement After Separation in Australia",
 "A property settlement divides your assets, debts and superannuation after a relationship ends. There's no automatic 50/50 \u2014 the outcome turns on contributions, future needs and what's fair. This guide covers the full process, the time limits, and how to settle without a court battle.",
 [("what-is","What is a property settlement?"),
  ("four-step","The four-step process"),
  ("asset-pool","What's in the asset pool?"),
  ("disclosure","The duty of disclosure"),
  ("super","Superannuation splitting"),
  ("time-limits","Time limits that apply"),
  ("how-to-settle","How to settle without court"),
  ("formalise","Making it legally binding")],
 key_takeaway("Property settlement follows a four-step process under the Family Law Act: identify the asset pool, assess contributions, weigh future needs, and check the result is just and equitable. Both parties must fully disclose their finances. Married couples generally have 12 months after divorce to apply; de facto couples have two years from separation. Mediation is the fastest route to a fair, binding outcome.")
 + f"""
<h2 id="what-is">What is a property settlement?</h2>
<p>A property settlement is the formal division of everything you and your former partner own and owe after separating. It's separate from the divorce itself \u2014 you don't have to be divorced (or even married) to do one. It applies to married and {('de facto')} couples alike, and covers the whole financial picture, not just the family home.</p>
<p>The governing law is the {cite("family_law_act")}, which sets out how property is to be divided. Crucially, it does not prescribe a fixed split.</p>
"""
 + inline_cta("Facing a property settlement? Get a clear, honest view of where you stand in a fixed-fee consultation.")
 + f"""
<h2 id="four-step">The four-step process</h2>
<p>Courts and mediators apply the same four-step framework:</p>
<figure class="tbl"><table><caption>The four-step property settlement process</caption>
<thead><tr><th>Step</th><th>What it involves</th></tr></thead>
<tbody>
<tr><td>1. Identify &amp; value the asset pool</td><td>List all assets, debts and superannuation, jointly and individually held.</td></tr>
<tr><td>2. Assess contributions</td><td>Financial and non-financial contributions across the whole relationship.</td></tr>
<tr><td>3. Consider future needs</td><td>Earning capacity, age, health, and care of children.</td></tr>
<tr><td>4. Just and equitable</td><td>Step back and confirm the overall division is genuinely fair.</td></tr>
</tbody></table></figure>
<p>This is the same framework explained in our guide to <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">what you're entitled to in a separation</a>.</p>

<h2 id="asset-pool">What's in the asset pool?</h2>
<ul>
  <li>The family home and any other real estate</li>
  <li>Superannuation (treated as property and able to be split)</li>
  <li>Savings, shares, and investments</li>
  <li>Vehicles, furniture and valuables</li>
  <li>Business interests, companies and trusts</li>
  <li>Debts and liabilities, which reduce the net pool</li>
</ul>
<p>Even assets held in one name alone, or acquired after separation, can form part of the pool depending on the circumstances.</p>
"""
 + callout("Beware of overlooked assets",
   "Superannuation, cryptocurrency, business goodwill and even inheritances can all be relevant. Full disclosure protects you \u2014 if assets surface later, a settlement can be reopened.")
 + f"""
<h2 id="disclosure">The duty of disclosure</h2>
<p>Both parties have a strict duty of full and frank financial disclosure, set out by the {cite("fcfcoa_disclosure")}. That means providing complete, honest information about income, assets, debts and financial resources. Hiding assets is taken seriously and can lead to penalties or a settlement being set aside. Mediation works best when disclosure is done thoroughly up front.</p>

<h2 id="super">Superannuation splitting</h2>
<p>Superannuation is treated as property under family law and can be split between partners. This is especially important where one partner has a much smaller balance because they reduced paid work to raise children. A super split is formalised through consent orders or a binding financial agreement. <a href="/financial-agreements-mediation/">See how financial agreements work \u2192</a></p>
"""
 + inline_cta("Worried something's being hidden, or unsure how super is split? We'll help you get full clarity.")
 + f"""
<h2 id="time-limits">Time limits that apply</h2>
<ul>
  <li><strong>Married couples:</strong> generally 12 months from the date a divorce becomes final.</li>
  <li><strong>De facto couples:</strong> generally two years from the date of separation.</li>
</ul>
<p>Miss the limit and you may need the court's permission to proceed, which isn't guaranteed. Acting promptly \u2014 and using mediation to move quickly \u2014 protects your position. <a href="/de-facto-mediation/">See de facto time limits \u2192</a></p>

<h2 id="how-to-settle">How to settle without court</h2>
<p>Most property settlements never need a judge. <a href="/property-settlement-mediation/">Property settlement mediation</a> lets you and your former partner work through the four-step framework with a neutral mediator and reach a fair agreement \u2014 in weeks, privately, and at a fraction of litigation's cost. It keeps the decision in your hands rather than handing it to a court. <a href="/mediate-or-litigate/">Compare mediation and litigation \u2192</a></p>

<h2 id="formalise">Making it legally binding</h2>
<p>Once you agree, formalise it \u2014 don't leave it informal. You can do this through <a href="/consent-orders-explained/">consent orders</a> (court-approved) or a <a href="/financial-agreements-mediation/">binding financial agreement</a> (a private contract). Either way, formalising closes off future claims and gives both parties certainty. <a href="/bfa-or-consent-orders/">Not sure which to choose? \u2192</a></p>
"""
 ,
 [("Is property split 50/50 after separation?",
   "Not automatically. The division follows a four-step process considering the asset pool, contributions, future needs and overall fairness. It may be 50/50 or weighted either way."),
  ("What's included in a property settlement?",
   "The family home, other real estate, superannuation, savings, shares, vehicles, business interests, trusts, and debts \u2014 jointly and individually held, sometimes including assets acquired after separation."),
  ("How long do I have to claim a property settlement?",
   "Married couples generally have 12 months from when the divorce is final; de facto couples generally have two years from separation. Late applications need the court's permission."),
  ("Can I do a property settlement without going to court?",
   "Yes. Most are resolved through mediation and then made binding via consent orders or a financial agreement, without a court hearing."),
  ("Is superannuation included in a property settlement?",
   "Yes. Superannuation is treated as property and can be split between partners, formalised through consent orders or a binding financial agreement.")],
 [("property-settlement-mediation","Property Settlement Mediation"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("financial-agreements-mediation","Binding Financial Agreements"),
  ("de-facto-mediation","De Facto Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce")],
 read_min=11)

print("property-settlement-after-separation built")
