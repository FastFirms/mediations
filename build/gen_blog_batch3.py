#!/usr/bin/env python3
"""Batch 3 cornerstone posts at full depth."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- HOW TO GET A DIVORCE IN AUSTRALIA (absorbs 14 posts) ----
post("how-to-get-a-divorce-in-australia-a-step-by-step-guide",
 "How to Get a Divorce in Australia: Step-by-Step Guide (2026)",
 "How to get a divorce in Australia in 2026: eligibility, the 12-month separation rule, how to apply online, costs, serving documents, and what happens with children. Step by step.",
 "Divorce",
 "How to Get a Divorce in Australia: <em>A Step-by-Step Guide</em>",
 "Getting divorced in Australia is more straightforward than most people expect. It's a no-fault system, you can apply online, and the divorce itself is separate from sorting out property and children. This guide walks you through every step, the eligibility rules, the cost, and the common pitfalls.",
 [("eligibility","Who can apply for a divorce?"),
  ("separation-rule","The 12-month separation rule"),
  ("step-by-step","How to apply: step by step"),
  ("cost","What does it cost?"),
  ("serving","Serving the divorce papers"),
  ("children","Divorce when you have children"),
  ("after","What a divorce does NOT resolve")],
 key_takeaway("Australia has a no-fault divorce system. To apply you must have been separated for at least 12 months and meet residency requirements. You apply online through the Commonwealth Courts Portal, pay the filing fee (around $1,100, or about $375 with a concession), and \u2014 if there are children under 18 \u2014 satisfy the court that proper arrangements are in place. The divorce itself does not divide property or settle parenting; those are separate.")
 + f"""
<h2 id="eligibility">Who can apply for a divorce?</h2>
<p>To apply for a divorce in Australia, you must satisfy the {cite("fcfcoa")} that:</p>
<ul>
  <li>You're an Australian citizen, a permanent resident, or have lived in Australia for at least the past 12 months;</li>
  <li>You have been separated for at least 12 months; and</li>
  <li>The marriage has broken down irretrievably, with no reasonable likelihood of getting back together.</li>
</ul>
<p>Australia follows a no-fault model under the {cite("family_law_act")} \u2014 the court doesn't care <em>why</em> the marriage ended, only that it has.</p>
"""
 + inline_cta("Unsure whether you're eligible or how to start? A quick consultation will give you clarity \u2014 no obligation.")
 + """
<h2 id="separation-rule">The 12-month separation rule</h2>
<p>You must be separated for at least 12 months and one day before you can apply. Separation can include being "separated under one roof" \u2014 living in the same home but no longer together as a couple \u2014 though you'll need to show evidence of that. <a href="/separation-under-one-roof/">See how separation under one roof works \u2192</a></p>
<p>If you got back together for a period of less than three months and then separated again, the earlier and later periods can sometimes be added together \u2014 but a reconciliation of three months or more resets the clock.</p>

<h2 id="step-by-step">How to apply: step by step</h2>
<ol>
  <li><strong>Gather your documents</strong> \u2014 marriage certificate, ID, and evidence of separation.</li>
  <li><strong>Create a Commonwealth Courts Portal account</strong> and complete the Application for Divorce.</li>
  <li><strong>Choose sole or joint</strong> \u2014 a joint application (both spouses) avoids serving documents; a sole application means you serve the other party.</li>
  <li><strong>Pay the filing fee</strong> and submit.</li>
  <li><strong>Serve the documents</strong> (sole applications only) within the required timeframe.</li>
  <li><strong>Attend the hearing if required</strong> \u2014 often not necessary, especially for joint applications or where there are no children under 18.</li>
  <li><strong>Divorce order takes effect</strong> one month and one day after it's granted.</li>
</ol>
"""
 + callout("Apply online from anywhere",
   "The entire divorce application is handled through the Commonwealth Courts Portal \u2014 you don't need to attend a registry in person to lodge it. Online mediation can resolve the property and parenting side the same way.")
 + f"""
<h2 id="cost">What does it cost?</h2>
<p>The divorce filing fee is set by federal regulation \u2014 around $1,100, with a reduced fee of roughly $375 for concession-card holders and those in financial hardship, per the {cite("fcfcoa_fees")}. If your application is straightforward and you do it yourself, that filing fee may be your only cost. <a href="/cost-of-divorce-in-australia/">See the full cost of divorce breakdown \u2192</a></p>

<h2 id="serving">Serving the divorce papers</h2>
<p>If you file a sole application, you must formally "serve" the documents on your spouse so they have notice. There are rules about how and when this must happen \u2014 you can't simply hand them over yourself. If your ex won't cooperate or can't be found, there are options including substituted service. <a href="/family-law-mediation/">If communication has broken down, mediation can help \u2192</a></p>
"""
 + inline_cta("Ex won't sign or can't be found? We can guide you through your options. Talk to us today.")
 + """
<h2 id="children">Divorce when you have children</h2>
<p>If there are children under 18, the court must be satisfied that proper arrangements have been made for their care before granting the divorce. This doesn't mean you need final parenting orders \u2014 but you do need workable arrangements. A <a href="/parenting-plan-mediation/">parenting plan</a> agreed through mediation is the simplest way to demonstrate this. For a sole application involving children, you may need to attend the hearing.</p>

<h2 id="after">What a divorce does NOT resolve</h2>
<p>This is the most misunderstood part: the divorce only ends the marriage. It does <strong>not</strong> divide your property, settle finances, or determine parenting arrangements. Those are separate processes \u2014 and there are time limits. You generally have <strong>12 months from the date the divorce is final</strong> to apply for property and financial orders. Don't let the divorce lull you into missing that window. <a href="/property-settlement-after-separation/">Sort your property settlement \u2192</a></p>
"""
 ,
 [("How long does it take to get divorced in Australia?",
   "You must be separated for at least 12 months before applying. After filing, a divorce order usually takes a few months and becomes final one month and one day after it's granted."),
  ("Can I get a divorce online in Australia?",
   "Yes. The Application for Divorce is lodged through the Commonwealth Courts Portal. You don't need to attend a registry in person to file."),
  ("How much does a divorce cost in Australia?",
   "The filing fee is around $1,100, with a reduced fee of about $375 for concession holders or those in financial hardship. A DIY application may have no other cost."),
  ("Do I need a lawyer to get divorced?",
   "No. You can file the divorce application yourself. Legal help is more useful for property settlement and parenting, which are separate from the divorce."),
  ("What if my spouse won't sign the divorce papers?",
   "You can file a sole application and serve them. If they won't cooperate or can't be found, options like substituted service exist. You don't need their consent to divorce.")],
 [("cost-of-divorce-in-australia","Cost of Divorce"),
  ("property-settlement-after-separation","Property Settlement After Separation"),
  ("how-long-does-mediation-take","How Long Does Mediation Take?"),
  ("separation-under-one-roof","Separation Under One Roof"),
  ("parenting-plan-mediation","Parenting Plan Mediation"),
  ("online-divorce","Online Divorce")],
 read_min=10)
print("how-to-get-a-divorce built")

# ---- BINDING FINANCIAL AGREEMENTS (absorbs 11 posts) ----
post("binding-financial-agreements-guide",
 "Binding Financial Agreements in Australia: Complete Guide (2026)",
 "What is a binding financial agreement (BFA)? How prenups and postnups work in Australia, what makes them valid, the risks, and how they compare to consent orders. Full 2026 guide.",
 "Property &amp; finances",
 "Binding Financial Agreements: <em>The Complete Guide</em>",
 "A binding financial agreement (BFA) is a private contract that decides how your assets are divided \u2014 before, during, or after a relationship. Often called a prenup or postnup, it offers flexibility and privacy, but only holds up if it's done strictly by the book. Here's what you need to know.",
 [("what-is","What is a binding financial agreement?"),
  ("types","Prenups, during, and after separation"),
  ("valid","What makes a BFA legally valid?"),
  ("vs-consent","BFA vs consent orders"),
  ("risks","The risks and how to avoid them"),
  ("set-aside","When can a BFA be set aside?"),
  ("right-for-you","Is a BFA right for you?")],
 key_takeaway("A binding financial agreement is a private contract under the Family Law Act that sets out how property and finances are divided. It can be made before, during or after a relationship. For it to be binding, each party must receive independent legal advice. BFAs offer flexibility and privacy but can be set aside for non-disclosure, fraud or duress \u2014 so they must be drafted carefully.")
 + f"""
<h2 id="what-is">What is a binding financial agreement?</h2>
<p>A binding financial agreement (BFA) is a private, written contract between partners that determines how their property, finances and sometimes spousal maintenance will be dealt with. Unlike <a href="/consent-orders-explained/">consent orders</a>, a BFA isn't approved by a court \u2014 it's an agreement the parties make between themselves under the {cite("family_law_act")}.</p>
<p>That privacy is a major attraction: there's no court scrutiny of the terms, and nothing becomes part of the public record. But it comes with a trade-off \u2014 the validity requirements are strict.</p>
"""
 + inline_cta("Considering a financial agreement? We'll help you get one that actually holds up. Book a consultation.")
 + """
<h2 id="types">Prenups, during, and after separation</h2>
<p>A BFA can be made at three points, and the popular names follow:</p>
<ul>
  <li><strong>Before a relationship or marriage</strong> \u2014 commonly called a "prenup". It sets expectations before assets are intermingled.</li>
  <li><strong>During a relationship</strong> \u2014 useful when circumstances change, such as an inheritance or starting a business.</li>
  <li><strong>After separation</strong> \u2014 a "postnup", used to finalise the split as an alternative to consent orders.</li>
</ul>
<p>The same agreement type is available to married and <a href="/de-facto-mediation/">de facto couples</a> alike.</p>

<h2 id="valid">What makes a BFA legally valid?</h2>
<p>This is where most BFAs succeed or fail. For a binding financial agreement to be enforceable:</p>
<ol>
  <li><strong>It must be in writing and signed</strong> by both parties.</li>
  <li><strong>Each party must receive independent legal advice</strong> \u2014 separately, from their own lawyer \u2014 before signing.</li>
  <li><strong>Each lawyer must provide a signed statement</strong> confirming that advice was given.</li>
  <li><strong>There must be full financial disclosure</strong> \u2014 hiding assets is fatal to a BFA.</li>
  <li><strong>It must not be signed under duress</strong> or undue pressure.</li>
</ol>
"""
 + callout("The independent advice rule is non-negotiable",
   "If even one party didn't get genuine independent legal advice, the whole agreement can collapse. This is the single most common reason BFAs are thrown out \u2014 don't cut corners on it.")
 + f"""
<h2 id="vs-consent">BFA vs consent orders</h2>
<figure class="tbl"><table><caption>Binding financial agreement vs consent orders</caption>
<thead><tr><th>Feature</th><th>BFA</th><th>Consent orders</th></tr></thead>
<tbody>
<tr><td>Approved by a court?</td><td>No \u2014 private contract</td><td>Yes \u2014 court-approved</td></tr>
<tr><td>Independent legal advice required?</td><td>Yes, for both parties</td><td>Not required</td></tr>
<tr><td>Privacy</td><td>High \u2014 stays private</td><td>Filed with the court</td></tr>
<tr><td>Can be made before a relationship?</td><td>Yes (prenup)</td><td>No</td></tr>
<tr><td>Typical cost</td><td>Higher (two lawyers)</td><td>Lower</td></tr>
<tr><td>Court tests fairness?</td><td>No</td><td>Yes (just and equitable)</td></tr>
</tbody></table></figure>
<p>Not sure which suits you? Our dedicated comparison breaks it down: <a href="/bfa-or-consent-orders/">BFA or consent orders? \u2192</a></p>
"""
 + inline_cta("Choosing between a BFA and consent orders is a judgment call. Let us help you pick the right one.")
 + f"""
<h2 id="risks">The risks and how to avoid them</h2>
<p>BFAs are powerful but fragile if done poorly. The main risks: inadequate independent advice, incomplete financial disclosure, signing too close to a wedding (which can suggest pressure), and poorly drafted terms that don't anticipate future change. The way to avoid all of them is careful drafting and genuine, unrushed independent advice for both parties.</p>

<h2 id="set-aside">When can a BFA be set aside?</h2>
<p>A court can set aside a binding financial agreement in defined circumstances, including: fraud or non-disclosure of a significant asset; the agreement being signed under duress or undue influence; impracticability (circumstances have changed so much it can't be carried out); or where a material change relating to the care of a child would cause hardship. The {cite("fcfcoa")} oversees these applications. Done properly, though, BFAs are difficult to overturn \u2014 which is the point.</p>

<h2 id="right-for-you">Is a BFA right for you?</h2>
<p>A BFA suits people who want maximum privacy and flexibility, who are protecting pre-existing or expected assets (a business, an inheritance), or who want certainty before entering a relationship. If you simply want to finalise a separation, <a href="/consent-orders-explained/">consent orders</a> are often simpler and cheaper. Mediation can help you reach the underlying agreement either way. <a href="/financial-agreements-mediation/">See financial agreements mediation \u2192</a></p>
"""
 ,
 [("What is a binding financial agreement?",
   "A BFA is a private written contract under the Family Law Act setting out how property and finances are divided. It can be made before, during or after a relationship and isn't approved by a court."),
  ("Do both parties need a lawyer for a BFA?",
   "Yes. For a BFA to be binding, each party must receive independent legal advice from their own lawyer, and each lawyer must sign a statement confirming it. This is essential to validity."),
  ("Is a prenup legally binding in Australia?",
   "Yes, if done correctly. A prenup is a binding financial agreement made before marriage or a relationship. It must meet strict requirements, including independent legal advice for both parties."),
  ("Can a binding financial agreement be overturned?",
   "Yes, in limited circumstances such as fraud, non-disclosure, duress, or impracticability. Done properly with full disclosure and independent advice, they're difficult to set aside."),
  ("BFA or consent orders \u2014 which is better?",
   "Consent orders are usually cheaper and court-approved; BFAs offer more privacy and flexibility and can be made before a relationship. The right choice depends on your circumstances.")],
 [("bfa-or-consent-orders","BFA or Consent Orders?"),
  ("financial-agreements-mediation","Financial Agreements Mediation"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("property-settlement-after-separation","Property Settlement After Separation"),
  ("de-facto-mediation","De Facto Mediation"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?")],
 read_min=11)
print("binding-financial-agreements-guide built")

# ---- PARENTING PLANS GUIDE (absorbs 8 posts) ----
post("parenting-plans-guide",
 "Parenting Plans in Australia: The Complete Guide (2026)",
 "What is a parenting plan, what should it include, and is it legally binding? A complete 2026 guide to parenting plans vs parenting orders, and how to agree one through mediation.",
 "Parenting",
 "Parenting Plans in Australia: <em>The Complete Guide</em>",
 "A parenting plan is a written agreement about how separated parents will raise their children \u2014 living arrangements, time, decisions and more. It's flexible and child-focused, but it's not the same as a parenting order. This guide covers what to include, whether it's binding, and how to agree one that lasts.",
 [("what-is","What is a parenting plan?"),
  ("include","What should a parenting plan include?"),
  ("binding","Is a parenting plan legally binding?"),
  ("vs-orders","Parenting plan vs parenting order"),
  ("best-interests","Putting the child's best interests first"),
  ("change","Changing a parenting plan"),
  ("how-to-agree","How to agree one through mediation")],
 key_takeaway("A parenting plan is a written, signed agreement between separated parents covering living arrangements, time with each parent, decision-making and more. It is not legally enforceable on its own, but a court will consider it. To make arrangements binding, they can be formalised as consent orders. Mediation is the best way to reach a workable, child-focused plan.")
 + f"""
<h2 id="what-is">What is a parenting plan?</h2>
<p>A parenting plan is a voluntary, written agreement between separated parents that sets out the practical arrangements for their children. It must be dated and signed by both parents. Unlike a court order, it's flexible and cooperative \u2014 the parents decide the terms themselves rather than having them imposed.</p>
<p>The {cite("frc")} encourages parents to reach their own arrangements wherever it's safe to do so, because plans the parents design together tend to work better and last longer than ones handed down by a court.</p>
"""
 + inline_cta("Want a parenting plan that genuinely works for your kids? Our mediators help you build one. Book a consultation.")
 + """
<h2 id="include">What should a parenting plan include?</h2>
<p>A thorough plan covers the realities of raising children across two homes:</p>
<ul>
  <li><strong>Living arrangements</strong> \u2014 where the children live and the day-to-day routine</li>
  <li><strong>Time with each parent</strong> \u2014 weekdays, weekends, and how changeovers happen</li>
  <li><strong>Holidays and special days</strong> \u2014 school holidays, birthdays, Christmas, cultural and religious occasions</li>
  <li><strong>Decision-making</strong> \u2014 how major long-term decisions (school, health, religion) are made</li>
  <li><strong>Communication</strong> \u2014 between the parents, and between each parent and the children</li>
  <li><strong>Travel</strong> \u2014 including interstate and overseas</li>
  <li><strong>Dispute resolution</strong> \u2014 agreeing to return to mediation before court if disagreements arise</li>
</ul>
<p>Our <a href="/parenting-plan-template/">parenting plan template guide</a> walks through each element in detail.</p>

<h2 id="binding">Is a parenting plan legally binding?</h2>
<p>This is the most important thing to understand: a parenting plan is <strong>not</strong> directly legally enforceable. If one parent doesn't follow it, you can't take them to court for "breaching" it the way you could with an order. However, it's far from worthless \u2014 if a parenting dispute later goes to court, the court will consider the most recent parenting plan and the arrangements in it. To make arrangements enforceable, you formalise them as <a href="/consent-orders-explained/">consent orders</a>.</p>
"""
 + callout("Plan first, orders later \u2014 a common path",
   "Many families start with a parenting plan to test what works, then convert the arrangements into consent orders once they've settled. You get flexibility early and enforceability once you're confident.")
 + f"""
<h2 id="vs-orders">Parenting plan vs parenting order</h2>
<figure class="tbl"><table><caption>Parenting plan vs parenting order</caption>
<thead><tr><th>Feature</th><th>Parenting plan</th><th>Parenting order</th></tr></thead>
<tbody>
<tr><td>Made by</td><td>The parents, by agreement</td><td>The court</td></tr>
<tr><td>Legally enforceable?</td><td>No</td><td>Yes</td></tr>
<tr><td>Flexibility</td><td>High \u2014 change anytime by agreement</td><td>Lower \u2014 needs court to vary</td></tr>
<tr><td>Cost</td><td>Low (especially via mediation)</td><td>Higher</td></tr>
<tr><td>Considered by a court later?</td><td>Yes</td><td>It is the order</td></tr>
</tbody></table></figure>

<h2 id="best-interests">Putting the child's best interests first</h2>
<p>Under the {cite("family_law_act")}, the child's best interests are the paramount consideration in all parenting matters. A good plan focuses on the children's needs \u2014 stability, safety, and meaningful relationships with both parents where safe \u2014 rather than on what each parent "wants". Keeping that focus is also what makes mediation so effective for parenting: it shifts the conversation from conflict to the children. <a href="/parenting-plan-mediation/">See parenting plan mediation \u2192</a></p>
"""
 + inline_cta("Mediation keeps the focus on your children, not the conflict. Talk to a child-focused mediator today.")
 + """
<h2 id="change">Changing a parenting plan</h2>
<p>One of the plan's strengths is flexibility. As children grow and circumstances shift, you can update the plan at any time \u2014 the new dated, signed version simply supersedes the old one. If you can't agree on a change, returning to mediation is far better than heading to court. Where arrangements are in consent orders instead, changing them requires either a fresh agreement or a court application.</p>

<h2 id="how-to-agree">How to agree one through mediation</h2>
<p>For most separated parents, <a href="/family-law-mediation/">mediation</a> is the ideal way to create a parenting plan. A neutral mediator helps you work through each element, keeps the discussion child-focused, and ensures nothing important is missed. For parenting matters, family dispute resolution is generally a required step before court anyway, per the {('Attorney-General')}'s framework \u2014 so starting with mediation puts you ahead. <a href="/preparing-for-mediation/">See how to prepare \u2192</a></p>
"""
 ,
 [("Is a parenting plan legally binding in Australia?",
   "No, a parenting plan is not directly enforceable on its own. However, a court will consider it in any later dispute. To make arrangements binding, formalise them as consent orders."),
  ("What should be included in a parenting plan?",
   "Living arrangements, time with each parent, holidays and special occasions, decision-making, communication, travel, and how to resolve future disputes \u2014 ideally through mediation."),
  ("What's the difference between a parenting plan and a parenting order?",
   "A parenting plan is a flexible agreement made by the parents and isn't enforceable; a parenting order is made by a court and is legally binding. Many families start with a plan and later formalise it."),
  ("Can a parenting plan be changed?",
   "Yes. Parents can update a parenting plan at any time by agreement \u2014 a new signed version supersedes the old one. If you can't agree, mediation is the best next step."),
  ("Do I need to go to court for a parenting plan?",
   "No. A parenting plan is made by agreement, usually through mediation. Family dispute resolution is generally required before court for parenting matters, so mediation is the natural first step.")],
 [("parenting-plan-mediation","Parenting Plan Mediation"),
  ("parenting-plan-template","Parenting Plan Template"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("family-law-mediation","Family Law Mediation"),
  ("child-support-mediation","Child Support Mediation"),
  ("preparing-for-mediation","Preparing for Mediation")],
 read_min=10)
print("parenting-plans-guide built")
