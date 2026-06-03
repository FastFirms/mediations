#!/usr/bin/env python3
"""Batch 2 cornerstone posts at full depth, built on the blog engine."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- CONSENT ORDERS EXPLAINED ----
post("consent-orders-explained",
 "Consent Orders Explained: How They Work in Australia (2026)",
 "What are consent orders, how do you apply, how long do they take and what do they cost? A complete 2026 guide to making your agreement legally binding without going to court.",
 "Consent orders",
 "Consent Orders Explained: <em>Making It Legally Binding</em>",
 "Consent orders turn an agreement you've already reached into legally binding court orders \u2014 without anyone setting foot in a courtroom. This guide explains exactly what they are, how to apply, what they cost, how long they take, and how to change or enforce them.",
 [("what-are","What are consent orders?"),
  ("how-apply","How do you apply for consent orders?"),
  ("how-long","How long do consent orders take?"),
  ("cost","What do consent orders cost?"),
  ("just-equitable","The 'just and equitable' test"),
  ("change","Can you change consent orders?"),
  ("breach","What happens if someone breaches them?")],
 key_takeaway("Consent orders are written agreements approved by the Federal Circuit and Family Court that become legally binding without a hearing. They can cover property, finances and parenting. You apply jointly, a registrar checks the terms are just and equitable (for property) or in the child's best interests (for parenting), and the filing fee is modest \u2014 far cheaper than litigation.")
 + f"""
<h2 id="what-are">What are consent orders?</h2>
<p>Consent orders are an agreement between separating parties that has been approved by a court and made into formal orders. Once approved, they carry the same legal weight as orders a judge would make after a hearing \u2014 but you avoid the hearing entirely. They can deal with property and financial matters, parenting arrangements, or both.</p>
<p>The key advantage is certainty. A handshake agreement or even a written one isn't automatically enforceable; consent orders are. They close the door on future claims and give both parties confidence the deal will hold. According to the {cite("fcfcoa_consent_orders")}, the process is designed to be straightforward where parties already agree.</p>
"""
 + inline_cta("Reached an agreement and want to make it official? We'll help you turn it into binding consent orders.")
 + f"""
<h2 id="how-apply">How do you apply for consent orders?</h2>
<p>The process is largely a paperwork exercise when both parties agree:</p>
<ol>
  <li><strong>Reach agreement</strong> \u2014 ideally through <a href="/family-law-mediation/">mediation</a>, which is the most efficient way to get there.</li>
  <li><strong>Prepare the documents</strong> \u2014 an Application for Consent Orders plus a proposed Minute of Consent Orders setting out the terms.</li>
  <li><strong>File with the court</strong> \u2014 lodged through the Commonwealth Courts Portal.</li>
  <li><strong>Registrar review</strong> \u2014 a court registrar checks the orders are appropriate, without you attending.</li>
  <li><strong>Orders made</strong> \u2014 once approved, they're sealed and legally binding.</li>
</ol>
<p>For property matters, full financial disclosure between the parties is essential \u2014 the {cite("fcfcoa_disclosure")} sets out this duty.</p>

<h2 id="how-long">How long do consent orders take?</h2>
<p>Once filed, consent orders are typically processed within a few weeks, though timeframes vary with court workload. The real variable is how long it takes to <em>reach</em> the agreement in the first place \u2014 which is exactly why mediation matters: it compresses the agreement stage from months to weeks. <a href="/how-long-does-mediation-take/">See how long mediation takes \u2192</a></p>
"""
 + callout("Consent orders vs a binding financial agreement",
   "Both make a financial settlement binding, but consent orders are court-approved (and generally cheaper), while a binding financial agreement is a private contract requiring independent legal advice for each party. Not sure which fits? See our comparison guide.")
 + f"""
<h2 id="cost">What do consent orders cost?</h2>
<p>The court filing fee for an Application for Consent Orders is modest \u2014 around $200 \u2014 set out in the {cite("fcfcoa_fees")}. On top of that you may have the cost of preparing the documents. Compared with the tens of thousands a contested property case can cost, consent orders are an inexpensive way to lock in certainty. <a href="/our-fee-structure/">See our transparent fees \u2192</a></p>

<h2 id="just-equitable">The 'just and equitable' test</h2>
<p>For property orders, the registrar won't simply rubber-stamp whatever you submit \u2014 they must be satisfied the division is "just and equitable" under the {cite("family_law_act")}. For parenting orders, the test is the best interests of the child. This is a protection, not an obstacle: it ensures the orders are sound and will hold up. A well-prepared application that reflects a fair, mediated agreement generally satisfies the test without difficulty. <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">Learn what a fair division looks like \u2192</a></p>
"""
 + inline_cta("We prepare consent order applications that satisfy the court the first time \u2014 no costly back-and-forth.")
 + """
<h2 id="change">Can you change consent orders?</h2>
<p>Yes, but not casually. Financial consent orders are usually final \u2014 that finality is the point. They can only be set aside in limited circumstances such as fraud, non-disclosure, or a significant change that makes them impracticable. Parenting consent orders can be changed if circumstances change significantly and it's in the child's best interests, ideally by agreement (often revisited through mediation) rather than fresh litigation.</p>

<h2 id="breach">What happens if someone breaches them?</h2>
<p>Because consent orders are court orders, breaching them has real consequences. For parenting orders, a contravention application can be brought, and penalties range from make-up time through to fines. For financial orders, enforcement mechanisms exist to compel compliance. If a breach happens, returning to mediation is often the fastest way to resolve it before escalating to enforcement. <a href="/family-law-mediation/">Talk to us about resolving a breach \u2192</a></p>
"""
 ,
 [("What are consent orders in Australia?",
   "Consent orders are a written agreement approved by the Federal Circuit and Family Court that becomes legally binding without a hearing. They can cover property, finances and parenting arrangements."),
  ("How long do consent orders take?",
   "Once filed, they're typically processed within a few weeks, depending on court workload. Reaching the underlying agreement \u2014 best done through mediation \u2014 is usually the longer part."),
  ("How much do consent orders cost?",
   "The court filing fee is modest (around $200), plus any cost of preparing the documents. This is far cheaper than a contested property case."),
  ("Can consent orders be changed later?",
   "Financial consent orders are usually final and can only be set aside in limited circumstances. Parenting orders can be varied if circumstances change significantly and it's in the child's best interests."),
  ("What happens if my ex breaches consent orders?",
   "Because they're court orders, breaches can be enforced. Parenting breaches can lead to a contravention application; financial orders have enforcement mechanisms. Mediation is often the fastest first step.")],
 [("consent-orders","Consent Orders Service"),
  ("financial-agreements-mediation","Binding Financial Agreements"),
  ("bfa-or-consent-orders","BFA or Consent Orders?"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("how-mediation-works","How Mediation Works")],
 read_min=9)

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
