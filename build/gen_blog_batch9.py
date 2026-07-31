#!/usr/bin/env python3
"""Batch 9: how-much-does-mediation-cost, arbitration, pets, same-sex, changes-2025."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- HOW MUCH DOES MEDIATION COST (absorbs 3) ----
post("how-much-does-mediation-cost",
 "How Much Does Mediation Cost in Australia? (2026 Guide)",
 "How much does mediation cost in Australia? A breakdown of family mediation fees, who pays, free and low-cost options, and why it's far cheaper than court.",
 "Costs &amp; fees",
 "How Much Does Mediation Cost in Australia?",
 "Family mediation in Australia typically costs far less than most people expect \u2014 and a fraction of going to court. This guide breaks down the real fees, who pays, the free and low-cost options that exist, and why mediation is the most cost-effective way to resolve a separation.",
 [("how-much","How much does it actually cost?"),
  ("what-affects","What affects the cost?"),
  ("who-pays","Who pays for mediation?"),
  ("free-options","Free and low-cost options"),
  ("vs-court","How it compares to court"),
  ("value","Why it's worth it")],
 key_takeaway("Private family mediation in Australia typically ranges from around $2,000 to $7,000 in total, commonly shared between the parties \u2014 often $3,000\u2013$4,500 for a full mediation day. Free and low-cost government-funded options exist through Family Relationship Centres. Either way, mediation costs a fraction of the tens of thousands per side that contested litigation can run.")
 + f"""
<h2 id="how-much">How much does it actually cost?</h2>
<p>Private family mediation generally costs somewhere between $2,000 and $7,000 in total, depending on the provider and complexity \u2014 often around $3,000 to $4,500 for a full day of mediation plus the agreement. Crucially, that's usually <em>shared</em> between the parties, so each person's share is lower again. Compare that to the {cite("fcfcoa_fees")} court fees plus legal costs of litigation, and the difference is dramatic.</p>
<figure class="tbl"><table><caption>Typical family mediation costs in Australia (indicative, 2026)</caption>
<thead><tr><th>Item</th><th>Typical total cost</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Intake / pre-mediation session</td><td>$200\u2013$500 per person</td><td>Separate confidential meeting with the mediator</td></tr>
<tr><td>Half-day mediation</td><td>$1,500\u2013$3,000</td><td>Suits simpler parenting or property matters</td></tr>
<tr><td>Full-day mediation</td><td>$3,000\u2013$5,000</td><td>Most common; usually shared between the parties</td></tr>
<tr><td>Section 60I certificate</td><td>Often included</td><td>Issued for parenting matters where required</td></tr>
<tr><td>Consent orders drafting</td><td>$700\u2013$2,500</td><td>Optional step to make the agreement binding</td></tr>
</tbody></table></figure>
<p>These are indicative ranges, not a quote \u2014 your actual cost depends on the factors below, and a good provider gives you a clear fixed fee before you start.</p>
"""
 + inline_cta("Want a clear, fixed quote for your situation? Book a consultation and we'll explain exactly what it costs.")
 + """
<h2 id="what-affects">What affects the cost?</h2>
<ul>
  <li><strong>Complexity</strong> \u2014 a simple parenting plan costs less than a complex property pool with businesses.</li>
  <li><strong>Number of sessions</strong> \u2014 most matters resolve in one, but some need more.</li>
  <li><strong>In person vs online</strong> \u2014 <a href="/online-divorce/">online mediation</a> can reduce costs.</li>
  <li><strong>Whether lawyers attend</strong> \u2014 optional, and adds cost if you choose to have yours present.</li>
  <li><strong>Formalising the agreement</strong> \u2014 consent orders or an agreement are an additional, modest step.</li>
</ul>

<h2 id="who-pays">Who pays for mediation?</h2>
<p>In most family mediations, the cost is shared equally between the parties \u2014 it's a joint process to reach a joint resolution, so splitting the fee is the norm. That said, the parties can agree a different arrangement, and in some cases one party covers more. This is something the mediator clarifies upfront so there are no surprises. <a href="/our-fee-structure/">See our transparent fee structure \u2192</a></p>
"""
 + callout("Shared cost, shared benefit",
   "Because mediation fees are usually split, your individual outlay is often just half of the headline figure \u2014 and you both walk away with a resolution, rather than each funding a separate lawyer to fight.")
 + f"""
<h2 id="free-options">Free and low-cost options</h2>
<p>Cost should never be a barrier to resolving a family dispute. Government-funded {cite("frc")} (Family Relationship Centres) offer family dispute resolution at free or low cost, particularly for parenting matters, with fees often based on income. These services are a valuable option, though private mediation typically offers more flexibility, faster scheduling, and capacity for complex financial matters.</p>

<h2 id="vs-court">How it compares to court</h2>
<p>This is the comparison that matters most. A contested court case can cost <em>each</em> party tens of thousands of dollars \u2014 sometimes over $100,000 in complex matters \u2014 over one to three years. Mediation resolves the same dispute for a few thousand dollars total, in weeks. The money saved stays with your family instead of funding a prolonged court case. <a href="/cost-of-divorce-in-australia/">See the full cost of divorce breakdown \u2192</a></p>
<figure class="tbl"><table><caption>Mediation vs a contested court case</caption>
<thead><tr><th></th><th>Mediation</th><th>Contested court case</th></tr></thead>
<tbody>
<tr><td>Typical cost</td><td>A few thousand dollars total, often shared</td><td>Tens of thousands per side</td></tr>
<tr><td>Timeframe</td><td>Weeks</td><td>One to three years</td></tr>
<tr><td>Who decides</td><td>You and your former partner</td><td>A judge</td></tr>
<tr><td>Privacy</td><td>Private and confidential</td><td>Public court process</td></tr>
</tbody></table></figure>
"""
 + inline_cta("Why spend tens of thousands fighting when mediation costs a fraction? Book a consultation today.")
 + """
<h2 id="value">Why it's worth it</h2>
<p>Beyond the raw numbers, mediation delivers value litigation can't: it's faster, it's private, it preserves co-parenting relationships, and it leaves you in control of the outcome. When you weigh the financial cost against the emotional cost of a prolonged court fight, mediation isn't just the cheaper option \u2014 it's the better one. <a href="/what-is-mediation-in-family-law/">See how mediation works \u2192</a></p>
"""
 ,
 [("How much does family mediation cost in Australia?",
   "Private mediation generally costs $2,000\u2013$7,000 in total, often $3,000\u2013$4,500 for a full day, and is usually shared between the parties. Free and low-cost government options also exist."),
  ("Who pays for mediation?",
   "In most family mediations the cost is shared equally between the parties, though they can agree a different arrangement. The mediator clarifies this upfront."),
  ("Are there free mediation options?",
   "Yes. Government-funded Family Relationship Centres offer family dispute resolution at free or low cost, particularly for parenting matters, often with fees based on income."),
  ("Is mediation cheaper than court?",
   "Far cheaper. A contested court case can cost each party tens of thousands of dollars over one to three years, while mediation resolves the same dispute for a few thousand total in weeks."),
  ("What makes mediation cost more or less?",
   "Complexity, the number of sessions, whether it's in person or online, whether lawyers attend, and the cost of formalising the agreement.")],
 [("cost-of-divorce-in-australia","Cost of Divorce"),
  ("our-fee-structure","Our Fee Structure"),
  ("what-is-mediation-in-family-law","What Is Mediation?"),
  ("family-law-cost-estimator","Cost Estimator"),
  ("mediate-or-litigate","Mediate or Litigate?"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=8)
print("how-much-does-mediation-cost built")

# ---- ARBITRATION IN FAMILY LAW (absorbs 1) ----
post("arbitration-in-family-law",
 "Arbitration in Family Law in Australia: How It Works (2026)",
 "Family law arbitration: how a binding decision on property and financial matters is reached privately, faster than court. How it differs from mediation.",
 "The process",
 "Arbitration in Family Law in Australia: <em>How It Works</em>",
 "When you need a definitive decision but want to avoid the cost and delay of court, arbitration is the answer. A qualified arbitrator hears both sides and makes a binding determination on property and financial matters \u2014 like a private judge, but faster. Here's how family law arbitration works.",
 [("what-is","What is family law arbitration?"),
  ("vs-mediation","How it differs from mediation"),
  ("what-can","What can be arbitrated?"),
  ("how-works","How the process works"),
  ("cost-time","Cost and timeframe"),
  ("binding","Is the decision binding?"),
  ("choosing","Choosing an arbitrator"),
  ("when-use","When to choose arbitration")],
 key_takeaway("Family law arbitration is a process where a qualified arbitrator hears a property or financial dispute and makes a legally binding decision, privately and far faster than court. Unlike mediation, the arbitrator decides the outcome. It's available for financial matters only \u2014 not parenting \u2014 and the award can be registered with the court and enforced like a court order.")
 + """
<h2 id="what-is">What is family law arbitration?</h2>
<p>Arbitration is a form of dispute resolution where the parties appoint a qualified arbitrator to hear their dispute and make a binding decision \u2014 essentially a private judge. It combines some of the speed and privacy of mediation with the finality of a court decision. For couples who genuinely can't agree but want to avoid the cost and delay of litigation, it's a powerful middle path.</p>
"""
 + inline_cta("Need a binding decision without the court wait? Find out if arbitration suits your matter. Book a consultation.")
 + """
<h2 id="vs-mediation">How it differs from mediation</h2>
<p>The difference is fundamental. In <a href="/what-is-mediation-in-family-law/">mediation</a>, you and your former partner reach your own agreement \u2014 the mediator decides nothing. In arbitration, you present your case and the <em>arbitrator</em> makes the decision for you. Mediation keeps control in your hands; arbitration hands it to a neutral decision-maker, but on your timetable and in private. Often the best approach is mediation first, with arbitration reserved for any issues that remain unresolved.</p>

<h2 id="what-can">What can be arbitrated?</h2>
<ul>
  <li>Property settlements and division of assets</li>
  <li>Superannuation splitting</li>
  <li>Spousal maintenance</li>
  <li>Financial aspects of de facto separations</li>
</ul>
<p>Importantly, arbitration in Australia is available for <strong>financial and property matters only</strong>. Parenting disputes cannot be arbitrated \u2014 they're resolved through mediation or, if necessary, the court. <a href="/property-settlement-after-separation/">See property settlement \u2192</a></p>
"""
 + callout("Faster and private",
   "An arbitrated decision can be reached in a fraction of the time a contested court hearing takes, on a timetable you help set, and entirely out of the public eye \u2014 a major advantage for those who value privacy.")
 + f"""
<h2 id="how-works">How the process works</h2>
<ol>
  <li><strong>Agree to arbitrate</strong> \u2014 both parties consent and appoint a qualified arbitrator.</li>
  <li><strong>Set the process</strong> \u2014 you help determine the timetable and how evidence is presented.</li>
  <li><strong>The hearing</strong> \u2014 each side presents its case to the arbitrator.</li>
  <li><strong>The award</strong> \u2014 the arbitrator makes a binding determination.</li>
  <li><strong>Registration</strong> \u2014 the award can be registered with the {cite("fcfcoa")} and enforced like a court order.</li>
</ol>
<p>The flexibility of the process is one of its great strengths. Rather than being locked into a court's crowded list and rigid procedures, you and your former partner \u2014 with the arbitrator's guidance \u2014 shape a timetable and format that suit the matter. A straightforward dispute over the division of a modest asset pool can be run efficiently on the papers, while a complex matter involving a business valuation or superannuation splitting can be given the fuller hearing it needs. Throughout, the {cite("family_law_act")} continues to govern the principles the arbitrator must apply, so the outcome reflects the same law a court would apply.</p>
"""
 + inline_cta("Curious how an arbitration would run for your matter? We'll walk you through the timetable and cost. Book a consultation.")
 + f"""
<h2 id="cost-time">Cost and timeframe</h2>
<p>Because arbitration sidesteps the court queue, it is almost always faster than litigation \u2014 and faster usually means cheaper. Where a contested court case can stretch across one to three years, an arbitration can often be concluded in a matter of weeks or a few months once the parties are ready. You pay the arbitrator's fee (and your own legal costs if you choose representation), but you avoid the drawn-out interlocutory steps, repeated court appearances, and delay that drive up the cost of litigation.</p>
<figure class="tbl"><table><caption>Arbitration compared with a contested court hearing (indicative)</caption>
<thead><tr><th></th><th>Arbitration</th><th>Contested court hearing</th></tr></thead>
<tbody>
<tr><td>Who decides</td><td>An arbitrator you jointly appoint</td><td>A judge assigned by the court</td></tr>
<tr><td>Timeframe</td><td>Weeks to a few months</td><td>One to three years</td></tr>
<tr><td>Privacy</td><td>Private and confidential</td><td>Public court process</td></tr>
<tr><td>Timetable</td><td>Set by the parties and arbitrator</td><td>Set by the court's list</td></tr>
<tr><td>Finality</td><td>Binding award, limited appeal grounds</td><td>Binding judgment, appeal rights</td></tr>
</tbody></table></figure>
<p>These are general comparisons rather than a quote \u2014 the actual cost depends on the arbitrator, the complexity of the matter, and whether lawyers are involved. What is consistent is that a decided matter costs far less than one that drags on. <a href="/cost-of-divorce-in-australia/">See the full cost of divorce breakdown \u2192</a></p>

<h2 id="binding">Is the decision binding?</h2>
<p>Yes. An arbitral award on financial matters can be registered with the court, at which point it's enforceable just like a court order. This gives genuine finality \u2014 the dispute is decided and done. There are limited grounds to challenge an award under the <a href='https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/' target='_blank' rel='noopener'>Family Law Act 1975</a>, which is what makes it a real alternative to a court hearing. <a href="/family-law-arbitration/">See our arbitration service \u2192</a></p>
"""
 + inline_cta("Get the finality of a decision without the years of litigation. Ask us whether arbitration fits your matter.")
 + """
<h2 id="choosing">Choosing an arbitrator</h2>
<p>Not everyone can arbitrate a family law matter. Arbitrators must be qualified and accredited to practise, and in property and financial matters they are typically experienced family law practitioners with specific arbitration training. This is an advantage: unlike a court hearing, where you cannot choose your judge, arbitration lets you and your former partner jointly appoint someone with the right expertise for your dispute — for example, an arbitrator with a strong background in business valuations or complex superannuation. Choosing an arbitrator you both respect also helps both parties accept the outcome. Your lawyer or mediator can help you identify a suitable, accredited arbitrator and confirm they are properly qualified before you commit.</p>
"""
 + inline_cta("Not sure who to appoint or whether your matter qualifies? We can point you to the right accredited arbitrator. Talk to us.")
 + """
<h2 id="when-use">When to choose arbitration</h2>
<p>Arbitration suits parties who have a genuine, narrow disagreement on financial matters that mediation hasn't resolved, who want a binding decision, and who value speed and privacy over a public court process. It's especially useful for complex financial matters where an arbitrator with specialist expertise can be appointed. For most people, the ideal sequence is: try <a href="/family-law-mediation/">mediation</a> first, and use arbitration for anything that remains. <a href="/mediate-or-litigate/">Compare your options \u2192</a></p>
"""
 ,
 [("What is family law arbitration?",
   "A process where a qualified arbitrator hears a property or financial dispute and makes a legally binding decision, privately and faster than court. It's used for financial matters, not parenting."),
  ("How is arbitration different from mediation?",
   "In mediation you reach your own agreement and the mediator decides nothing. In arbitration the arbitrator makes a binding decision for you, like a private judge."),
  ("Can parenting matters be arbitrated?",
   "No. In Australia, arbitration is available for property and financial matters only. Parenting disputes are resolved through mediation or the court."),
  ("Is an arbitrator's decision binding?",
   "Yes. An arbitral award on financial matters can be registered with the court and enforced like a court order, giving genuine finality with limited grounds to challenge."),
  ("Should I try mediation or arbitration first?",
   "Most people start with mediation to keep control of the outcome, and use arbitration for any financial issues that remain unresolved, avoiding a full court case.")],
 [("family-law-arbitration","Family Law Arbitration Service"),
  ("what-is-mediation-in-family-law","What Is Mediation?"),
  ("property-settlement-after-separation","Property Settlement"),
  ("mediate-or-litigate","Mediate or Litigate?"),
  ("family-court-process","The Family Court Process"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=8)
print("arbitration-in-family-law built")

# ---- PETS AND FAMILY LAW (absorbs 1) ----
post("pets-and-family-law",
 "Pets and Family Law: Who Gets the Pet After Separation?",
 "Who gets the pet after separation? How pets are treated in family law, the 2025 changes recognising pets, and how mediation resolves pet disputes.",
 "Property &amp; finances",
 "Pets and Family Law: <em>Who Gets the Pet After Separation?</em>",
 "For many people, the family pet is family \u2014 but the law has traditionally treated pets as property. That's now changing. This guide explains how pets are dealt with after separation, the recent law reforms recognising pets as more than mere possessions, and how mediation resolves pet disputes humanely.",
 [("how-treated","How does the law treat pets?"),
  ("changes","The law is changing"),
  ("factors","What's considered for who keeps the pet"),
  ("arrangements","Can you share a pet?"),
  ("formalise","Putting the agreement in writing"),
  ("mediation","Why mediation is ideal for pet disputes"),
  ("livestock","Working animals and livestock"),
  ("protect","Practical tips")],
 key_takeaway("Traditionally, Australian family law treated pets as property, dividing them like any other asset. Recent reforms to the Family Law Act now require courts to consider specific factors about the animal \u2014 including who cares for it and any family violence \u2014 rather than treating pets purely as possessions. Mediation lets separating couples agree humane, practical arrangements for a beloved pet.")
 + f"""
<h2 id="how-treated">How does the law treat pets?</h2>
<p>This often surprises people: historically, under the {cite("family_law_act")}, pets were treated as <em>property</em> \u2014 an asset to be allocated in the property settlement, the same as a car or furniture. There was no concept of "pet custody" or shared care in the way many owners assume. For people who consider their dog or cat a family member, that approach felt deeply inadequate.</p>
"""
 + inline_cta("Worried about what happens to your pet? We'll help you reach a humane arrangement. Book a consultation.")
 + f"""
<h2 id="changes">The law is changing</h2>
<p>Reforms to the {cite("family_law_act")} have introduced specific provisions for companion animals \u2014 recognising that pets aren't just ordinary property. Rather than simply allocating a pet as an asset, courts are now directed to consider relevant factors about the animal and the people involved when deciding who keeps it. It's a meaningful shift that brings the law closer to how families actually feel about their pets. <a href="/changes-to-family-law-act-2025/">See the 2025 Family Law Act changes \u2192</a></p>

<h2 id="factors">What's considered for who keeps the pet</h2>
<p>Under the reformed approach, relevant considerations can include:</p>
<ul>
  <li>Who has primarily cared for and met the costs of the animal</li>
  <li>Any history of family violence, including threats or harm involving the pet</li>
  <li>The relationship between the animal and each person (and any children)</li>
  <li>Each person's ability to care for the animal going forward</li>
</ul>
<p>Notably, the law recognises the link between pets and family violence \u2014 an important protection, as pets are sometimes used as a means of control.</p>
<figure class="tbl"><table><caption>What courts can and can't do with pets</caption>
<thead><tr><th>Question</th><th>Position under the reformed law</th></tr></thead>
<tbody>
<tr><td>Can a court allocate a pet to one person?</td><td>Yes \u2014 a court can order that one person keeps the animal.</td></tr>
<tr><td>Can a court order 'shared custody' of a pet?</td><td>No \u2014 a court generally won't make shared-time orders for an animal.</td></tr>
<tr><td>Can the parties agree to share a pet themselves?</td><td>Yes \u2014 you can agree any arrangement you both want, including shared time.</td></tr>
<tr><td>Is family violence relevant?</td><td>Yes \u2014 including threats or harm involving the animal.</td></tr>
<tr><td>Does who paid for the pet matter?</td><td>Yes \u2014 who cared for and met the costs of the animal is relevant.</td></tr>
</tbody></table></figure>
"""
 + callout("Pets and family violence",
   "The reforms specifically allow consideration of family violence involving an animal. Threats to harm a pet can be a form of coercive control, and the law now takes that seriously.")
 + """
<h2 id="arrangements">Can you share a pet?</h2>
<p>A court generally won't make "shared custody" orders for a pet the way it would for children \u2014 but <em>you</em> can agree to whatever arrangement works, including shared time, if you both want it. This is exactly where reaching your own agreement beats leaving it to a court: through negotiation you can craft a flexible, humane arrangement that a judge wouldn't impose. <a href="/property-settlement-after-separation/">See how property is divided \u2192</a></p>
"""
 + inline_cta("Want to keep sharing time with a pet you both love? We'll help you agree an arrangement that works. Book a consultation.")
 + """
<h2 id="formalise">Putting the agreement in writing</h2>
<p>Once you've agreed who keeps the pet \u2014 or how you'll share time with it \u2014 it's wise to record that agreement in writing rather than relying on a handshake. A pet arrangement can be documented within a broader parenting or property agreement, or set out in <a href="/consent-orders-explained/">consent orders</a> so it forms part of a final, binding settlement. Putting it in writing removes ambiguity about who is responsible for vet costs, insurance, day-to-day care, and any agreed shared time. It also means that if circumstances change or a disagreement resurfaces later, both of you can point to a clear, agreed record rather than re-litigating an emotional issue from scratch. A mediator can help you capture the detail \u2014 including practicalities like handovers and who covers ongoing expenses \u2014 so nothing is left to assumption.</p>

<h2 id="mediation">Why mediation is ideal for pet disputes</h2>
<p>Pet disputes are emotionally charged but rarely suited to the bluntness of a court order. <a href="/family-law-mediation/">Mediation</a> lets you and your former partner talk through what's genuinely best for the animal and agree an arrangement \u2014 sole care with visits, shared time, or a clean handover \u2014 that reflects your circumstances and your bond with the pet. It's faster, cheaper, and far kinder than fighting over a family member in court.</p>
"""
 + inline_cta("Your pet is family. Resolve it humanely through mediation rather than a court fight. Talk to us today.")
 + """
<h2 id="livestock">Working animals and livestock</h2>
<p>Not every animal in a separation is a companion pet. Rural and farming families often have working dogs, horses, or livestock that are both cherished and part of the property or a business. These animals can raise a mix of considerations — the emotional attachment that applies to any pet, alongside their value as assets or income-producing property. A working sheepdog integral to running a farm, or a herd that forms part of a family business, may be assessed differently from a household cat. Where animals straddle the line between companion and commercial asset, it's especially important to be clear about which lens applies, and mediation gives you room to reach a sensible, tailored outcome rather than a blunt allocation. <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">See what's included in the asset pool →</a></p>

<h2 id="protect">Practical tips</h2>
<ul>
  <li><strong>Keep records</strong> of who paid for and cared for the pet \u2014 vet bills, registration, food.</li>
  <li><strong>Register and microchip</strong> details matter and should be kept up to date.</li>
  <li><strong>Think about the animal's wellbeing</strong>, not just winning \u2014 stability matters to pets too.</li>
  <li><strong>Agree early</strong> \u2014 the sooner you settle it, the less distress for everyone, pet included.</li>
</ul>
"""
 ,
 [("Who gets the pet after separation in Australia?",
   "Traditionally pets were treated as property in the settlement, but recent Family Law Act reforms require courts to consider factors like who cares for the animal and any family violence."),
  ("Are pets treated as property in Australian family law?",
   "Historically yes, but reforms now recognise companion animals as more than ordinary property, directing courts to consider specific factors about the animal and the people involved."),
  ("Can you get shared custody of a pet?",
   "A court generally won't order shared 'custody' of a pet, but separating couples can agree any arrangement they both want, including shared time \u2014 best reached through mediation."),
  ("Does family violence affect who keeps the pet?",
   "Yes. The reforms specifically allow consideration of family violence involving an animal, recognising that threats to a pet can be a form of coercive control."),
  ("How can I resolve a dispute over our pet?",
   "Mediation is ideal \u2014 it lets you agree a humane, flexible arrangement for the animal that reflects your circumstances, faster and more kindly than a court fight.")],
 [("property-settlement-after-separation","Property Settlement"),
  ("changes-to-family-law-act-2025","Changes to the Family Law Act 2025"),
  ("family-law-mediation","Family Law Mediation"),
  ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?")],
 read_min=8)
print("pets-and-family-law built")

# ---- SAME-SEX FAMILY LAW (absorbs 2) ----
post("same-sex-family-law",
 "Same-Sex Separation and Divorce in Australia (2026 Guide)",
 "Same-sex separation and divorce in Australia: equal rights under family law, property, parenting and de facto considerations for LGBTQ+ couples.",
 "Divorce",
 "Same-Sex Separation and Divorce in Australia",
 "Since marriage equality, same-sex couples have exactly the same family law rights and obligations as everyone else \u2014 in divorce, property, and parenting. This guide covers what LGBTQ+ couples need to know when separating, including the issues that can be unique to same-sex families.",
 [("equal","Equal rights under the law"),
  ("divorce","Divorce for same-sex couples"),
  ("de-facto","De facto same-sex relationships"),
  ("property","Property settlement"),
  ("parenting","Parenting and children"),
  ("parentage","Legal parentage and donors"),
  ("unique","Issues unique to same-sex families"),
  ("mediation","How mediation helps")],
 key_takeaway("Since marriage equality in 2017, same-sex married couples have identical divorce, property and parenting rights to opposite-sex couples under the Family Law Act. Same-sex de facto couples have the same rights as other de facto couples. Parenting matters focus on the child's best interests regardless of parents' gender or sexuality. Mediation works equally well for same-sex separations.")
 + f"""
<h2 id="equal">Equal rights under the law</h2>
<p>Since marriage equality became law in Australia in 2017, same-sex couples have exactly the same legal standing as opposite-sex couples in every aspect of family law. The {cite("family_law_act")} applies equally \u2014 there's no separate or lesser regime — the <a href='https://www.fcfcoa.gov.au/' target='_blank' rel='noopener'>Federal Circuit and Family Court</a> applies the same rules to all couples. Whether married or de facto, LGBTQ+ couples have the same rights and obligations when a relationship ends.</p>
"""
 + inline_cta("Separating from a same-sex partner? You have full, equal rights. We'll help you navigate them. Book now.")
 + """
<h2 id="divorce">Divorce for same-sex couples</h2>
<p>Same-sex married couples divorce through exactly the same process as anyone else: 12 months' separation, an application through the Commonwealth Courts Portal, and the same eligibility rules. Couples who married overseas before Australian marriage equality and had that marriage recognised here can also divorce under Australian law. <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">See the full divorce process \u2192</a></p>

<h2 id="de-facto">De facto same-sex relationships</h2>
<p>Many same-sex couples are in de facto relationships, which carry substantially the same rights as marriage for property and maintenance. The same definition and the same two-year time limit apply. For couples together before marriage equality, the de facto framework has long provided these protections. <a href="/de-facto-relationships-guide/">See de facto relationships \u2192</a></p>
"""
 + callout("The law is the same \u2014 the dynamics can differ",
   "While the legal framework is identical, same-sex separations can involve unique practical issues \u2014 around parentage, donor arrangements, or assets accumulated before legal recognition. Experienced, inclusive guidance matters.")
 + """
<h2 id="property">Property settlement</h2>
<p>Property settlement for same-sex couples follows the identical <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">four-step process</a>: identify the asset pool, assess contributions, consider future needs, and ensure a just and equitable outcome. Superannuation splitting and binding financial agreements are equally available. <a href="/property-settlement-after-separation/">See property settlement \u2192</a></p>

<h2 id="parenting">Parenting and children</h2>
<p>Parenting matters focus solely on the best interests of the child \u2014 a parent's gender or sexuality is not a relevant factor. Same-sex families may face specific questions around legal parentage, donor or surrogacy arrangements, and the recognition of non-biological parents, which is why tailored advice is valuable. The guiding principle, though, is exactly the same: what serves the child. <a href="/parenting-plans-guide/">See parenting plans \u2192</a></p>
"""
 + inline_cta("Same-sex family matters deserve experienced, inclusive guidance. Talk to us confidentially today.")
 + """
<h2 id="parentage">Legal parentage and donors</h2>
<p>One area where same-sex families sometimes need particular care is legal parentage. Where a child was conceived through a donor, surrogacy, or assisted reproduction, the question of who is legally recognised as a parent can be more involved than for couples who conceive without assistance. In many cases the law recognises the non-biological parent \u2014 for example, the de facto or married partner of a birth mother who consented to the procedure \u2014 but the details depend on the circumstances and, for surrogacy, on state-specific rules. Known-donor arrangements can also raise questions about the donor's status. None of this changes the child-focused approach the court takes; it simply means it's worth confirming the legal parentage position early, so everyone understands where they stand. <a href="/surrogacy-laws/">See surrogacy laws in Australia \u2192</a></p>
<figure class="tbl"><table><caption>Same-sex couples: the family law position at a glance</caption>
<thead><tr><th>Issue</th><th>Position for same-sex couples</th></tr></thead>
<tbody>
<tr><td>Divorce (married)</td><td>Identical process and rules as opposite-sex couples</td></tr>
<tr><td>De facto rights</td><td>Same rights, same two-year threshold</td></tr>
<tr><td>Property settlement</td><td>Same four-step approach; super splitting available</td></tr>
<tr><td>Parenting</td><td>Decided on the child's best interests only</td></tr>
<tr><td>Legal parentage</td><td>Recognised, but donor/surrogacy details may need advice</td></tr>
</tbody></table></figure>

<h2 id="unique">Issues unique to same-sex families</h2>
<p>While the legal framework is identical, some practical dynamics can differ. Couples who were together for years before marriage equality may have accumulated assets across a period when their relationship had no formal legal recognition \u2014 which can make questions about contributions and the length of the relationship worth thinking through carefully. Others may have relied on informal arrangements with donors or co-parents that were never documented. And for some, the experience of family, friends, or wider community not fully accepting the relationship adds an emotional layer to an already difficult time. An inclusive, experienced approach recognises these realities rather than treating a same-sex separation as identical in every practical respect to any other. <a href="/de-facto-relationships-guide/">See how de facto relationships are assessed \u2192</a></p>
"""
 + inline_cta("Every family is different. We'll tailor our approach to your circumstances, respectfully. Reach out today.")
 + """
<h2 id="mediation">How mediation helps</h2>
<p><a href="/family-law-mediation/">Mediation</a> works just as effectively for same-sex separations \u2014 and offers the same benefits of speed, privacy, lower cost and control. It's also a space where the specific dynamics of a same-sex separation can be worked through respectfully, away from an adversarial courtroom. Whatever your family looks like, mediation helps you resolve things on your own terms. <a href="/what-is-mediation-in-family-law/">See how mediation works \u2192</a></p>
"""
 ,
 [("Do same-sex couples have the same divorce rights in Australia?",
   "Yes. Since marriage equality in 2017, same-sex married couples have identical divorce, property and parenting rights to opposite-sex couples under the Family Law Act."),
  ("Can same-sex couples who married overseas divorce in Australia?",
   "Yes. Overseas same-sex marriages recognised in Australia can be ended through the standard Australian divorce process, subject to the usual eligibility rules."),
  ("Do same-sex de facto couples have property rights?",
   "Yes. Same-sex de facto couples have substantially the same property and maintenance rights as other de facto couples, with the same two-year time limit from separation."),
  ("How does parenting work for same-sex families after separation?",
   "Parenting decisions focus solely on the child's best interests, regardless of the parents' gender or sexuality. Specific questions around parentage and donor arrangements may need tailored advice."),
  ("Does mediation work for same-sex separations?",
   "Yes, equally well. Mediation offers the same speed, privacy, lower cost and control, and provides a respectful space to work through any specific dynamics.")],
 [("how-to-get-a-divorce-in-australia-a-step-by-step-guide","How to Get a Divorce"),
  ("de-facto-relationships-guide","De Facto Relationships"),
  ("property-settlement-after-separation","Property Settlement"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("family-law-mediation","Family Law Mediation"),
  ("what-is-mediation-in-family-law","What Is Mediation?")],
 read_min=8)
print("same-sex-family-law built")

# ---- CHANGES TO FAMILY LAW ACT 2025 (absorbs 1) ----
post("changes-to-family-law-act-2025",
 "Changes to the Family Law Act 2025: What You Must Know",
 "Key 2025 changes to the Family Law Act: new property settlement framework, family violence, pets, and what the reforms mean for separating couples.",
 "Legal updates",
 "Changes to the Family Law Act 2025: <em>What You Must Know</em>",
 "The Family Law Act has undergone its most significant reforms in years. From a clearer property settlement framework to express recognition of family violence and pets, the 2025 changes affect anyone separating in Australia. Here's a plain-English summary of what's changed and what it means for you.",
 [("overview","Overview of the reforms"),
  ("property","A clearer property framework"),
  ("violence","Family violence front and centre"),
  ("pets","Pets recognised"),
  ("disclosure","Duty of disclosure strengthened"),
  ("parenting","Parenting law changes"),
  ("summary","The changes at a glance"),
  ("what-means","What it means for you")],
 key_takeaway("Recent reforms to the Family Law Act have codified the property settlement process, expressly required family violence (including economic abuse) to be considered in property matters, introduced specific provisions for companion animals (pets), and reinforced a child's best interests as paramount in parenting. The changes make outcomes clearer and bring the law closer to how families actually experience separation.")
 + f"""
<h2 id="overview">Overview of the reforms</h2>
<p>The {cite("family_law_act")} has been substantially updated, with reforms progressively taking effect through 2024 and 2025 (see the <a href='https://www.ag.gov.au/families-and-marriage/families' target='_blank' rel='noopener'>Attorney-General's Department</a>). The thrust of the changes is to make the law clearer, fairer and more reflective of modern families \u2014 particularly around property division, family violence, and the recognition of pets. If you're separating now, these are the rules that apply to you.</p>
"""
 + inline_cta("Unsure how the new laws affect your situation? Get up-to-date guidance in a consultation. Book today.")
 + """
<h2 id="property">A clearer property framework</h2>
<p>One of the most significant changes codifies the property settlement process \u2014 writing the long-established <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">four-step approach</a> more explicitly into the legislation. This brings greater clarity and predictability to how assets are divided, helping separating couples (and mediators) understand the framework that applies. The fundamentals \u2014 contributions, future needs, and a just and equitable outcome \u2014 remain, but are now set out more clearly. <a href="/property-settlement-after-separation/">See property settlement \u2192</a></p>

<h2 id="violence">Family violence front and centre</h2>
<p>The reforms expressly require the financial impact of family violence to be considered in property settlements. This is a major step: it recognises that abuse \u2014 including economic and financial abuse \u2014 can affect a person's contributions and future needs, and that the law should account for it. It's a significant protection for survivors. <a href="/domestic-violence-and-family-law/">See family violence and family law \u2192</a></p>
"""
 + callout("Economic abuse now expressly recognised",
   "The express inclusion of economic and financial abuse in property considerations is one of the most important reforms \u2014 acknowledging a form of harm that was previously easy to overlook.")
 + """
<h2 id="pets">Pets recognised</h2>
<p>The reforms introduce specific provisions for companion animals, directing courts to consider relevant factors \u2014 including who cares for the animal and any family violence involving it \u2014 rather than treating pets as ordinary property. It's a welcome, very human update. <a href="/pets-and-family-law/">See pets and family law \u2192</a></p>
"""
 + inline_cta("Want to know which of these reforms affect your matter? A short consultation will make it clear. Book today.")
 + f"""
<h2 id="disclosure">Duty of disclosure strengthened</h2>
<p>Another important thread in the reforms is a clearer, elevated <strong>duty of disclosure</strong> in financial matters. Both parties to a property settlement have always been required to give full and frank disclosure of their financial circumstances, but the reforms make this obligation more explicit within the legislation itself. In practical terms, this means each person must be open about their assets, income, and liabilities \u2014 and there are consequences for those who try to hide or understate what they have. For anyone resolving a property matter, this is reassuring: it reinforces that a fair settlement rests on honest information. The {cite("fcfcoa")} sets out what disclosure involves, and a mediator will expect both parties to come to the table having met it. <a href="/property-settlement-after-separation/">See how disclosure works in a settlement \u2192</a></p>

<h2 id="parenting">Parenting law changes</h2>
<p>Recent reforms also reshaped the parenting provisions, reinforcing that the <strong>best interests of the child</strong> are paramount and simplifying how those interests are assessed. Changes in this area have adjusted how parental responsibility and time are approached, always centring the child. <a href="/parenting-plans-guide/">See parenting plans \u2192</a> and <a href="/child-custody-mediation/">child custody mediation \u2192</a></p>
"""
 + inline_cta("Make sure your approach reflects the current law. We stay across the reforms so you don't have to.")
 + """
<h2 id="summary">The changes at a glance</h2>
<p>The reforms are wide-ranging, but the practical effect for most separating couples comes down to a handful of themes. The table below summarises what changed and why it matters.</p>
<figure class="tbl"><table><caption>Key Family Law Act reforms and what they mean</caption>
<thead><tr><th>Area</th><th>What changed</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Property</td><td>Four-step approach codified in legislation</td><td>Clearer, more predictable outcomes</td></tr>
<tr><td>Family violence</td><td>Financial impact (including economic abuse) must be considered</td><td>Stronger protection for survivors</td></tr>
<tr><td>Pets</td><td>Specific factors for companion animals introduced</td><td>Pets no longer treated as ordinary property</td></tr>
<tr><td>Disclosure</td><td>Duty of full and frank disclosure made more explicit</td><td>Settlements rest on honest information</td></tr>
<tr><td>Parenting</td><td>Best interests reinforced; assessment simplified</td><td>Clearer, child-focused decisions</td></tr>
</tbody></table></figure>
"""
 + inline_cta("A clearer law makes agreement easier. Let us help you resolve things under the current framework. Book a consultation.")
 + """
<h2 id="what-means">What it means for you</h2>
<p>If you're separating, the practical upshot is positive: a clearer property framework, stronger recognition of family violence (including economic abuse), humane treatment of pets, and a continued focus on children's best interests. These changes make outcomes more predictable \u2014 which is exactly what makes <a href="/family-law-mediation/">mediation</a> work even better, since both parties can negotiate against a clearer set of rules. <a href="/what-is-mediation-in-family-law/">See how mediation works \u2192</a></p>
<p class="source-note">Family law is subject to ongoing reform. For advice specific to your circumstances and the current law, speak with a qualified professional.</p>
"""
 ,
 [("What are the 2025 changes to the Family Law Act?",
   "Key reforms codify the property settlement process, require family violence (including economic abuse) to be considered in property matters, add provisions for pets, and reinforce children's best interests in parenting."),
  ("How do the reforms affect property settlements?",
   "They codify the four-step approach more explicitly into legislation, bringing greater clarity and predictability, and require the financial impact of family violence to be considered."),
  ("Does the Family Law Act now recognise pets?",
   "Yes. The reforms introduce specific provisions for companion animals, directing courts to consider factors like who cares for the animal and any family violence, rather than treating pets as ordinary property."),
  ("How is family violence treated under the new law?",
   "The reforms expressly require the financial impact of family violence \u2014 including economic and financial abuse \u2014 to be considered in property settlements, a significant protection for survivors."),
  ("What do the changes mean for me if I'm separating?",
   "A clearer property framework, stronger recognition of family violence, humane treatment of pets, and a continued focus on children's best interests \u2014 making outcomes more predictable.")],
 [("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("property-settlement-after-separation","Property Settlement"),
  ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
  ("pets-and-family-law","Pets and Family Law"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=8)
print("changes-to-family-law-act-2025 built")

# ---- STEP-PARENT RIGHTS (absorbs 1) ----
post("stepparent-rights",
 "Step-Parent Rights in Australia: Where You Stand (2026)",
 "Do step-parents have rights in Australia? Parental responsibility, contact after separation, child support, and how step-parents can stay in a child's life.",
 "Parenting",
 "Step-Parent Rights in Australia: <em>Where You Stand</em>",
 "Step-parents often play a huge role in a child's life \u2014 but their legal position isn't automatic. This guide explains what rights a step-parent has, what happens after a separation, when child support can apply, and how a step-parent can seek to maintain a relationship with a child they've helped raise.",
 [("automatic","Do step-parents have automatic rights?"),
  ("responsibility","Parental responsibility and step-parents"),
  ("after-separation","Contact after separation"),
  ("child-support","Can a step-parent owe child support?"),
  ("orders","Seeking parenting orders"),
  ("adoption","Step-parent adoption"),
  ("planning","Planning for blended families"),
  ("mediation","How mediation helps")],
 key_takeaway("Step-parents don't automatically have parental responsibility in Australia \u2014 that rests with the legal parents. But a step-parent who has played a significant role can apply for parenting orders to maintain a relationship with the child, decided on the child's best interests. In limited circumstances a step-parent can also be liable for child support. Mediation helps preserve these important relationships.")
 + f"""
<h2 id="automatic">Do step-parents have automatic rights?</h2>
<p>No \u2014 and this surprises many devoted step-parents. Under the {cite("family_law_act")}, parental responsibility automatically rests with a child's legal parents, not with a step-parent, regardless of how involved the step-parent has been. However, "no automatic rights" doesn't mean "no rights at all" \u2014 the law recognises that significant relationships matter to children, and there are pathways for step-parents to formalise their role through the <a href='https://www.fcfcoa.gov.au/' target='_blank' rel='noopener'>Federal Circuit and Family Court</a>.</p>
"""
 + inline_cta("Want to stay in the life of a child you've helped raise? We'll explain your options. Book a consultation.")
 + """
<h2 id="responsibility">Parental responsibility and step-parents</h2>
<p>A step-parent can acquire parental responsibility \u2014 for example, through a parenting order, or in some cases by adoption (a significant legal step requiring the relevant consents and court approval). Without one of these, a step-parent generally doesn't have legal decision-making authority for the child, even within an intact blended family. Understanding this early helps blended families plan sensibly.</p>

<h2 id="after-separation">Contact after separation</h2>
<p>When a step-parent and the child's parent separate, the step-parent has no automatic right to spend time with the child \u2014 but they can seek it. The law recognises a child's right to maintain relationships with people significant to their care, welfare and development, which can include a step-parent who has been a meaningful figure. The focus, as always, is the child's best interests. <a href="/child-custody-mediation/">See how the best-interests test works \u2192</a></p>
"""
 + callout("Significant relationships count",
   "A step-parent who has genuinely helped raise a child isn't invisible to the law. Where continuing that relationship serves the child, there are real pathways to preserve it.")
 + """
<h2 id="child-support">Can a step-parent owe child support?</h2>
<p>In limited circumstances, yes. While the primary obligation rests with the child's legal parents, a court can in some cases order a step-parent to contribute to a child's support \u2014 taking into account the length of the relationship, the role the step-parent played, and the child's needs. It's not common, but it's possible. <a href="/child-support-guide/">See child support \u2192</a></p>
<figure class="tbl"><table><caption>Where a step-parent stands in Australian family law</caption>
<thead><tr><th>Question</th><th>General position</th></tr></thead>
<tbody>
<tr><td>Automatic parental responsibility?</td><td>No \u2014 it rests with the legal parents</td></tr>
<tr><td>Can they get parental responsibility?</td><td>Yes \u2014 via a parenting order or, rarely, adoption</td></tr>
<tr><td>Automatic right to see the child after separation?</td><td>No \u2014 but they can apply for time</td></tr>
<tr><td>Can they apply for parenting orders?</td><td>Yes \u2014 as a person significant to the child's care</td></tr>
<tr><td>Can they be liable for child support?</td><td>In limited circumstances, yes</td></tr>
</tbody></table></figure>
"""
 + inline_cta("Unsure where you stand as a step-parent? A short conversation will clarify your options. Book a consultation.")
 + """
<h2 id="orders">Seeking parenting orders</h2>
<p>A step-parent who wants to maintain a relationship with a child after separation can apply for parenting orders. Like parents and grandparents, they generally need to attempt <a href="/is-family-law-mediation-compulsory/">family dispute resolution</a> first. The court will consider whether ongoing contact is in the child's best interests, weighing the strength and significance of the relationship. <a href="/grandparents-rights/">See grandparents' rights for a comparable pathway \u2192</a></p>
"""
 + inline_cta("Blended family separating? Mediation can preserve the relationships that matter. Talk to us today.")
 + """
<h2 id="adoption">Step-parent adoption</h2>
<p>Some step-parents wonder whether adopting their step-child is the way to formalise their role. It's possible, but it's a significant legal step — not a formality. Step-parent adoption permanently changes the child's legal parentage, and because it ends the legal relationship with one of the child's birth parents, courts treat it cautiously and grant it sparingly. It generally requires the consent of the relevant parties, a demonstrated benefit to the child, and court approval, and the rules are governed by state adoption legislation rather than the Family Law Act alone. For most step-parents who simply want to stay meaningfully involved in a child's life, a parenting order is a more proportionate route than adoption. Where adoption genuinely is the right path, specialist advice is essential.</p>

<h2 id="planning">Planning for blended families</h2>
<p>The best time to think about a step-parent's position isn't during a separation — it's while the family is together and things are calm. Blended families can benefit from being clear, early on, about the step-parent's role: how decisions are made, what happens with schooling and health, and what everyone would want for the child if the adults' relationship were ever to end. Documenting intentions — whether through a parenting plan, a family agreement, or simply a shared understanding written down — reduces the risk of painful uncertainty later. It also protects the child, who benefits most from stability and from adults who have thought ahead rather than improvising in a crisis. A mediator can help a blended family have these conversations constructively before any conflict arises. <a href="/parenting-plans-guide/">See how parenting plans work →</a></p>
"""
 + inline_cta("Building a blended family? Getting clear early prevents heartache later. We can help you plan. Reach out today.")
 + """
<h2 id="mediation">How mediation helps</h2>
<p>Step-parent situations are emotionally delicate \u2014 they involve the child's legal parents, the step-parent, and sometimes more than two households. <a href="/family-law-mediation/">Mediation</a> offers a constructive, private way to agree how a step-parent stays involved, keeping the focus on the child rather than on conflict between adults. It's almost always better than a court fight for preserving these relationships. <a href="/parenting-plans-guide/">See parenting plans \u2192</a></p>
"""
 ,
 [("Do step-parents have legal rights in Australia?",
   "Not automatically. Parental responsibility rests with the legal parents. But a step-parent who has played a significant role can apply for parenting orders, decided on the child's best interests."),
  ("Can a step-parent get parental responsibility?",
   "Yes, through a parenting order or, in some cases, adoption. Without one of these, a step-parent generally has no legal decision-making authority for the child."),
  ("Can a step-parent see the child after separation?",
   "There's no automatic right, but a step-parent can seek time. The law recognises a child's right to maintain significant relationships, and the focus is the child's best interests."),
  ("Can a step-parent be ordered to pay child support?",
   "In limited circumstances, yes. While legal parents have the primary obligation, a court can sometimes order a step-parent to contribute, considering the relationship and the child's needs."),
  ("How can a step-parent maintain a relationship with the child?",
   "By agreement through mediation, or by applying for parenting orders (after attempting family dispute resolution). The court weighs whether ongoing contact serves the child's best interests.")],
 [("child-custody-mediation","Child Custody Mediation"),
  ("grandparents-rights","Grandparents' Rights"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("child-support-guide","Child Support Guide"),
  ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=8)
print("stepparent-rights built")

# ---- SURROGACY LAWS (absorbs 1) ----
post("surrogacy-laws",
 "Surrogacy Laws in Australia: What You Need to Know (2026)",
 "Surrogacy laws in Australia: altruistic vs commercial surrogacy, legal parentage, parentage orders, and the rules across states. Plain-English guide.",
 "Legal updates",
 "Surrogacy Laws in Australia: <em>What You Need to Know</em>",
 "Surrogacy law in Australia is complex and varies by state \u2014 but the core principles are consistent: only altruistic surrogacy is allowed, commercial surrogacy is prohibited, and legal parentage transfers through a court order. This guide explains how surrogacy works legally and where to get the right advice.",
 [("overview","How surrogacy law works"),
  ("altruistic","Altruistic vs commercial surrogacy"),
  ("parentage","Legal parentage and parentage orders"),
  ("pathway","The surrogacy pathway step by step"),
  ("agreement","Surrogacy agreements"),
  ("overseas","Overseas surrogacy"),
  ("states","State-by-state differences"),
  ("advice","Getting the right advice")],
 key_takeaway("In Australia, only altruistic surrogacy (where the surrogate isn't paid beyond reasonable expenses) is legal \u2014 commercial surrogacy is prohibited in every state. At birth, the surrogate is the legal mother; intended parents become the legal parents through a court parentage order made after the birth. The detailed rules vary by state, so specialist legal advice is essential.")
 + f"""
<h2 id="overview">How surrogacy law works</h2>
<p>Surrogacy in Australia is governed primarily by <em>state and territory</em> legislation, not the federal {cite("family_law_act")} \u2014 which is why the rules differ depending on where you live. Despite the variation, the foundations are consistent across the country: only altruistic surrogacy is permitted, commercial arrangements are banned, and legal parenthood is transferred through a court order after the child is born.</p>
"""
 + inline_cta("Considering surrogacy and need to understand the legal pathway? Speak with us about getting the right advice.")
 + """
<h2 id="altruistic">Altruistic vs commercial surrogacy</h2>
<p>The central distinction in Australian law:</p>
<ul>
  <li><strong>Altruistic surrogacy</strong> \u2014 legal. The surrogate receives no payment beyond reasonable, verifiable expenses related to the pregnancy.</li>
  <li><strong>Commercial surrogacy</strong> \u2014 prohibited in every Australian state and territory. Paying a surrogate a fee is an offence, and several states also prohibit entering commercial arrangements overseas.</li>
</ul>
<p>This is a serious area of law \u2014 the prohibitions carry real penalties (each state regulates this; see for example the <a href='https://www.fcfcoa.gov.au/' target='_blank' rel='noopener'>Federal Circuit and Family Court</a> on parentage) \u2014 so understanding the boundaries before proceeding is essential.</p>

<h2 id="parentage">Legal parentage and parentage orders</h2>
<p>A crucial point that surprises many intended parents: at birth, the <strong>surrogate</strong> (and her partner, if any) is the legal parent \u2014 not the intended parents, even where the child is genetically theirs. Legal parenthood transfers to the intended parents through a <strong>parentage order</strong> made by a court after the birth, once the relevant criteria and timeframes are met. Until that order is made, the intended parents are not the legal parents.</p>
"""
 + callout("Genetics don't equal legal parenthood",
   "Even if the child is biologically the intended parents', the law still requires a parentage order to make them the legal parents. Getting this step right is non-negotiable.")
 + """
<h2 id="pathway">The surrogacy pathway step by step</h2>
<p>Although the detail varies by state, a compliant altruistic surrogacy in Australia generally moves through a recognisable sequence of steps. Understanding it early helps intended parents and surrogates set realistic expectations about timing and what's required of them.</p>
<ol>
  <li><strong>Counselling and legal advice</strong> — all parties obtain independent counselling and independent legal advice before entering any arrangement.</li>
  <li><strong>Written surrogacy agreement</strong> — the parties document their intentions in a written arrangement.</li>
  <li><strong>Approvals</strong> — depending on the state, an assisted reproduction clinic and/or ethics committee may need to approve the arrangement.</li>
  <li><strong>Conception and pregnancy</strong> — the pregnancy proceeds, with the surrogate as the birth mother.</li>
  <li><strong>Birth</strong> — at birth, the surrogate (and her partner, if any) is the legal parent.</li>
  <li><strong>Parentage order</strong> — after a set period, the intended parents apply to a court to transfer legal parentage to them.</li>
</ol>
<figure class="tbl"><table><caption>Surrogacy in Australia: the essentials</caption>
<thead><tr><th>Question</th><th>Position</th></tr></thead>
<tbody>
<tr><td>Is altruistic surrogacy legal?</td><td>Yes, in all states, with conditions</td></tr>
<tr><td>Is commercial surrogacy legal?</td><td>No — prohibited everywhere, with penalties</td></tr>
<tr><td>Who is the legal parent at birth?</td><td>The surrogate (and her partner, if any)</td></tr>
<tr><td>How do intended parents become legal parents?</td><td>Through a court parentage order after birth</td></tr>
<tr><td>Which law applies?</td><td>State/territory surrogacy legislation</td></tr>
</tbody></table></figure>
"""
 + inline_cta("Planning a surrogacy journey? Getting the sequence right from the start matters. We can point you to specialist advice.")
 + """
<h2 id="agreement">Surrogacy agreements</h2>
<p>Surrogacy arrangements typically involve a written agreement, counselling for all parties, and independent legal advice \u2014 which is generally required before proceeding. While a surrogacy agreement isn't enforceable to compel anyone to hand over a child, it sets out the parties' intentions and is part of the framework courts consider. The emphasis throughout is on informed, freely given consent.</p>
"""
 + inline_cta("Need help understanding a surrogacy agreement or a dispute around one? Talk to us about the right advice.")
 + """
<h2 id="overseas">Overseas surrogacy</h2>
<p>Some intended parents look overseas, where commercial surrogacy may be available. This is an area to approach with real caution. Several Australian states make it an offence for their residents to enter a <em>commercial</em> surrogacy arrangement abroad — meaning conduct that's legal in another country can still expose you to liability at home. Beyond the legal risk, overseas arrangements can create serious complications around the child's citizenship, immigration status, and the recognition of legal parentage when the family returns to Australia. These matters can be difficult and slow to resolve, and the child's interests are always central. Anyone considering surrogacy overseas should get specialist Australian legal advice <em>before</em> proceeding, not after, so they fully understand the consequences in their own state.</p>

<h2 id="states">State-by-state differences</h2>
<p>Because surrogacy is state-regulated, the eligibility rules, required steps, timeframes for parentage orders, and rules about overseas arrangements all vary. What's permitted and how the process runs in one state can differ meaningfully from another. This is the single biggest reason specialist, state-specific legal advice is essential before starting. <a href="/contact-us/">Talk to us about a referral \u2192</a></p>
"""
 + inline_cta("Surrogacy law is complex and state-specific. Get pointed to the right specialist advice \u2014 reach out today.")
 + """
<h2 id="advice">Getting the right advice</h2>
<p>Surrogacy is one of the most legally complex areas of family formation, and mistakes can have profound consequences. Anyone considering surrogacy \u2014 as intended parents or as a surrogate \u2014 should obtain specialist legal advice in their state, complete the required counselling, and ensure every step is properly documented. Where disputes or family law questions arise around a surrogacy arrangement, we can help you find the right path. <a href="/family-law-mediation/">See how we can help \u2192</a></p>
<p class="source-note">Surrogacy law varies by state and changes over time. This is general information only \u2014 obtain specialist legal advice for your circumstances.</p>
"""
 ,
 [("Is surrogacy legal in Australia?",
   "Altruistic surrogacy is legal in all states, where the surrogate receives no payment beyond reasonable expenses. Commercial surrogacy \u2014 paying a fee \u2014 is prohibited everywhere in Australia."),
  ("Who is the legal parent in a surrogacy arrangement?",
   "At birth, the surrogate (and her partner, if any) is the legal parent. Intended parents become the legal parents through a court parentage order made after the birth."),
  ("What is a parentage order?",
   "A court order that transfers legal parenthood from the surrogate to the intended parents after the birth, once the relevant criteria and timeframes are met."),
  ("Is commercial surrogacy allowed in Australia?",
   "No. Commercial surrogacy is prohibited in every state and territory, and several states also prohibit entering commercial arrangements overseas. Penalties apply."),
  ("Do surrogacy laws differ between states?",
   "Yes, significantly. Eligibility, required steps, timeframes and rules on overseas arrangements vary by state, which is why specialist state-specific legal advice is essential.")],
 [("changes-to-family-law-act-2025","Changes to the Family Law Act 2025"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("stepparent-rights","Step-Parent Rights"),
  ("family-law-mediation","Family Law Mediation"),
  ("contact-us","Contact Us")],
 read_min=8)
print("surrogacy-laws built")

# ---- CAN YOU RECORD YOUR EX (absorbs 1) ----
post("can-you-record-your-ex",
 "Can You Record Your Ex Without Permission in Australia?",
 "Can you legally record your ex without consent in Australia? Surveillance and listening device laws, whether recordings can be used in court, and the risks.",
 "Legal updates",
 "Can You Record Your Ex Without Permission in Australia?",
 "It's a common impulse in a heated separation \u2014 secretly record your ex to 'prove' something. But recording someone without consent can be a criminal offence in Australia, and such recordings are often inadmissible in family court. Here's what the law actually says before you hit record.",
 [("short-answer","The short answer"),
  ("laws","Surveillance and listening device laws"),
  ("state-by-state","How the rules vary by state"),
  ("court","Can recordings be used in family court?"),
  ("children","Recording your children"),
  ("messages","Texts, emails and social media"),
  ("risks","The risks of recording"),
  ("instead","What to do instead")],
 key_takeaway("Secretly recording a private conversation is a criminal offence in most Australian states under surveillance and listening device laws, with limited exceptions. Even where a recording exists, family courts are often reluctant to admit it and may view the recording party negatively. Before recording anyone, get legal advice \u2014 the risks usually outweigh any benefit.")
 + """
<h2 id="short-answer">The short answer</h2>
<p>Generally, no \u2014 you should not secretly record your ex. In most Australian states and territories, recording a private conversation without the consent of the parties is a criminal offence under surveillance and listening device laws. There are narrow exceptions, but they're limited, and getting it wrong can expose you to criminal liability and damage your position in family law proceedings. This is an area to get advice on <em>before</em> acting, not after.</p>
"""
 + inline_cta("Tempted to record your ex? Talk to us first \u2014 there are safer, more effective ways to protect yourself.")
 + """
<h2 id="laws">Surveillance and listening device laws</h2>
<p>Each state and territory has its own surveillance devices or listening devices legislation, but the common thread is that secretly recording a <em>private conversation</em> you're not party to \u2014 and in many places, even one you <em>are</em> party to \u2014 is prohibited without consent. The rules differ on whether a participant can record their own conversation, which is exactly why blanket assumptions are dangerous. Penalties can include fines and even imprisonment under state legislation such as the <a href='https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/nsw/consol_act/sda2007210/' target='_blank' rel='noopener'>Surveillance Devices Act</a>.</p>
"""
 + inline_cta("Before you assume a recording will help, get advice on your state's rules. We'll give you a clear answer. Book a consultation.")
 + """
<h2 id="state-by-state">How the rules vary by state</h2>
<p>Because each state and territory has its own legislation, the exact position depends on where you are — which is precisely why you should never rely on what a friend in another state, or a video online, tells you. Some jurisdictions prohibit recording a private conversation outright; others allow a participant to record a conversation they're part of in narrow circumstances, such as to protect their lawful interests. The safest working assumption is that secretly recording is prohibited unless you have specific advice confirming otherwise for your state and your situation.</p>
<figure class="tbl"><table><caption>Key questions that change the answer</caption>
<thead><tr><th>Factor</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Which state or territory you're in</td><td>Each has its own surveillance/listening device law</td></tr>
<tr><td>Whether you're a party to the conversation</td><td>Rules differ for participant vs third-party recording</td></tr>
<tr><td>Whether it's a private conversation</td><td>Private conversations attract the strongest protection</td></tr>
<tr><td>Your purpose in recording</td><td>Some limited exceptions turn on protecting lawful interests</td></tr>
</tbody></table></figure>
<p>Given how much turns on these variables, blanket assumptions are genuinely risky. When in doubt, don't record — ask first.</p>

<h2 id="court">Can recordings be used in family court?</h2>
<p>Even setting aside the criminal question, illegally obtained recordings are frequently <strong>inadmissible</strong> in <a href='https://www.fcfcoa.gov.au/' target='_blank' rel='noopener'>family law proceedings</a> \u2014 and tendering one can backfire. Courts may not only exclude the recording but also take a dim view of a party who resorted to covert surveillance, seeing it as inconsistent with the cooperative, child-focused approach family law encourages. The recording you hoped would help can end up hurting you. <a href="/family-court-process/">See the family court process \u2192</a></p>
"""
 + callout("It can backfire badly",
   "People often assume a secret recording is a trump card. In practice it can be excluded as evidence, expose you to criminal charges, and make you look like the unreasonable party. The downside usually outweighs any upside.")
 + """
<h2 id="children">Recording your children</h2>
<p>Recording children \u2014 or coaching them to record the other parent \u2014 is particularly fraught. Courts are highly protective of children and view involving them in the conflict, including using them to gather 'evidence', very negatively. It can seriously damage your case and, more importantly, your children. Don't do it.</p>
"""
 + inline_cta("Worried about your ex's conduct? There are lawful ways to protect yourself and your children. Let's talk them through.")
 + """
<h2 id="messages">Texts, emails and social media</h2>
<p>People often ask whether the same problems apply to written communication. The picture here is more favourable. Text messages, emails, and other written exchanges that you are a party to are yours — you received them, and keeping them is not the same as covertly recording a conversation. These can be far more useful than a secret recording, because they're a clear, dated record in the other person's own words, obtained without breaching surveillance laws. The same broadly applies to messages sent to you through co-parenting apps. Social media posts that are publicly visible can also sometimes be relevant. What you should not do is hack into an account, guess a password, or access someone's device or messages without permission — that raises its own serious legal problems. Keep what's genuinely yours, obtained lawfully, and let that speak for itself. <a href="/family-court-process/">See how evidence works in family law →</a></p>

<h2 id="risks">The risks of recording</h2>
<ul>
  <li><strong>Criminal liability</strong> \u2014 potential fines or imprisonment under surveillance laws</li>
  <li><strong>Inadmissibility</strong> \u2014 the recording may be excluded as evidence</li>
  <li><strong>Reputational harm</strong> \u2014 courts may view you as the unreasonable party</li>
  <li><strong>Escalation</strong> \u2014 it deepens conflict and erodes any trust that remains</li>
</ul>
"""
 + inline_cta("There are lawful, effective ways to document concerns. We'll show you the right approach. Book a consultation.")
 + """
<h2 id="instead">What to do instead</h2>
<p>If you're worried about your ex's conduct, there are lawful, effective alternatives: keep a written, dated record of events; retain text messages and emails (which you're a party to); use reputable co-parenting apps that log communication; and raise genuine safety concerns with the appropriate authorities. And bring your concerns to <a href="/family-law-mediation/">mediation</a>, where issues can be aired and addressed constructively. If there's a safety risk, see <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>.</p>
"""
 ,
 [("Can I legally record my ex without their consent in Australia?",
   "Generally no. Secretly recording a private conversation is a criminal offence in most states under surveillance and listening device laws, with only limited exceptions."),
  ("Can a secret recording be used in family court?",
   "Often not. Illegally obtained recordings are frequently inadmissible, and tendering one can backfire by making the recording party look unreasonable to the court."),
  ("Is it illegal to record my own conversation with my ex?",
   "It depends on the state \u2014 the rules on whether a participant can record their own conversation vary, which is why you should get legal advice before recording anything."),
  ("Can I record my children with the other parent?",
   "This is highly inadvisable. Courts are very protective of children and view involving them in the conflict to gather evidence extremely negatively. It can seriously damage your case."),
  ("What can I do instead of recording my ex?",
   "Keep a written dated record, retain texts and emails you're party to, use co-parenting apps that log communication, raise genuine safety concerns with authorities, and address issues in mediation.")],
 [("family-court-process","The Family Court Process"),
  ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
  ("high-conflict-mediation","High-Conflict Mediation"),
  ("family-law-mediation","Family Law Mediation"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("mediation-with-a-narcissist","Mediation With a Narcissist")],
 read_min=8)
print("can-you-record-your-ex built")

# ---- BEST DIVORCE LAWYERS SYDNEY (absorbs 2) ----
post("best-divorce-lawyers-sydney",
 "Divorce Lawyers vs Mediators in Sydney: How to Choose",
 "Looking for divorce lawyers in Sydney? When you need a lawyer, when mediation is better, and how to choose the right help for your separation.",
 "Divorce",
 "Best Divorce Lawyers in Sydney: <em>How to Choose the Right Help</em>",
 "Searching for the 'best divorce lawyer in Sydney' is a natural first step \u2014 but it's worth asking whether a lawyer, a mediator, or both is what your situation actually needs. This guide helps you choose the right professional, what to look for, and how to resolve your separation in Sydney without an unnecessary court battle.",
 [("what-need","What kind of help do you need?"),
  ("when-lawyer","When you need a divorce lawyer"),
  ("when-mediator","When mediation is the better path"),
  ("both","Using both together"),
  ("compare","Lawyer vs mediator at a glance"),
  ("questions","Questions to ask before you engage"),
  ("choose","How to choose the right professional"),
  ("sydney","Resolving your separation in Sydney")],
 key_takeaway("The 'best' help depends on your situation. A divorce lawyer is valuable for advice, complex matters, or where one party won't engage. But for most separating couples in Sydney, mediation resolves parenting and property faster, cheaper and more amicably than a lawyer-led court fight. Often the ideal is advice from a lawyer plus mediation to reach the agreement.")
 + """
<h2 id="what-need">What kind of help do you need?</h2>
<p>It's worth pausing before you search for the "best divorce lawyer". The most expensive, most adversarial option isn't always the best one for your situation. The real question is: do you need someone to <em>advise and represent</em> you (a lawyer), someone to <em>help you and your ex reach agreement</em> (a mediator), or a combination? Matching the help to the need can save you enormous time, money and stress.</p>
"""
 + inline_cta("Not sure whether you need a lawyer, a mediator, or both? We'll give you a straight answer. Book a consultation.")
 + """
<h2 id="when-lawyer">When you need a divorce lawyer</h2>
<p>A divorce lawyer genuinely adds value when:</p>
<ul>
  <li>You need advice on your legal position and entitlements</li>
  <li>The matter is complex \u2014 significant assets, a business, trusts</li>
  <li>There's family violence or a serious power imbalance</li>
  <li>Your ex won't engage, won't disclose, or has already gone to court</li>
  <li>You need urgent orders</li>
</ul>
<p>In these situations, good legal advice is an investment, not a luxury. <a href="/mediate-or-litigate/">See when court is genuinely necessary \u2192</a></p>

<h2 id="when-mediator">When mediation is the better path</h2>
<p>For the majority of separating couples \u2014 including in Sydney \u2014 <a href="/family-law-mediation/">mediation</a> is the better first step. It resolves parenting and property faster, at a fraction of the cost, privately, and with far less damage to co-parenting relationships. For parenting matters it's <a href='https://www.fcfcoa.gov.au/fl/fdr' target='_blank' rel='noopener'>required before court</a> anyway. If you and your ex can engage, even imperfectly, mediation usually beats a lawyer-led fight. <a href="/cost-of-divorce-in-australia/">See the cost difference \u2192</a></p>
"""
 + callout("The best lawyers often recommend mediation",
   "A genuinely good family lawyer will frequently steer you toward mediation, because they understand what litigation costs in money and wellbeing. Be wary of anyone who pushes straight for court.")
 + """
<h2 id="both">Using both together</h2>
<p>It's not either/or. Many people get the best outcome by combining the two: legal advice to understand their position and entitlements, then mediation to actually reach the agreement \u2014 with the agreement formalised into <a href="/consent-orders-explained/">consent orders</a>. Some of our mediators are themselves experienced lawyers, so you get both perspectives. <a href="/collaborative-family-lawyers/">See collaborative family law \u2192</a></p>
"""
 + inline_cta("Want advice and a path to agreement in one place? Some of our mediators are experienced lawyers. Book a consultation.")
 + """
<h2 id="compare">Lawyer vs mediator at a glance</h2>
<p>The two roles are complementary rather than competing, but they do different jobs. This comparison helps you see which fits which need.</p>
<figure class="tbl"><table><caption>Divorce lawyer vs family mediator</caption>
<thead><tr><th></th><th>Divorce lawyer</th><th>Family mediator</th></tr></thead>
<tbody>
<tr><td>Main role</td><td>Advises and represents you</td><td>Helps both of you reach agreement</td></tr>
<tr><td>Acts for</td><td>You alone</td><td>The process, impartially</td></tr>
<tr><td>Best when</td><td>Complex, high-conflict, or urgent matters</td><td>You can engage and want to agree</td></tr>
<tr><td>Typical cost</td><td>Higher, especially if it goes to court</td><td>Lower, often shared</td></tr>
<tr><td>Speed</td><td>Slower if litigated</td><td>Usually weeks</td></tr>
<tr><td>Outcome</td><td>Advice; a judge may decide</td><td>An agreement you both own</td></tr>
</tbody></table></figure>

<h2 id="questions">Questions to ask before you engage</h2>
<p>Whether you're speaking to a lawyer or a mediator, a few well-chosen questions quickly reveal whether they're the right fit. Ask how they approach resolution \u2014 do they aim to settle matters or default to litigation? Ask about their accreditation and specific family law experience. Ask how they charge, and whether fixed-fee options are available so you're not exposed to open-ended costs. Ask what your realistic options are, not just the one they happen to offer. And pay attention to how they make you feel: you'll be working closely with this person at a stressful time, so being genuinely heard matters. A professional who prioritises your outcome over the size of the file is the one you want. <a href="/our-fee-structure/">See our transparent fee structure \u2192</a></p>
"""
 + inline_cta("Ask us anything \u2014 approach, accreditation, fees, your realistic options. We'll give you straight answers. Book a Sydney consultation.")
 + """
<h2 id="choose">How to choose the right professional</h2>
<ul>
  <li><strong>Look for accreditation</strong> \u2014 nationally accredited mediators; experienced, specialist family lawyers.</li>
  <li><strong>Ask about their approach</strong> \u2014 do they prioritise resolution or default to litigation?</li>
  <li><strong>Check fees are transparent</strong> \u2014 fixed-fee options reduce uncertainty.</li>
  <li><strong>Make sure you feel heard</strong> \u2014 you'll be working closely with them.</li>
</ul>
"""
 + inline_cta("Get experienced, accredited help that prioritises resolution over conflict. Book a Sydney consultation today.")
 + """
<h2 id="sydney">Resolving your separation in Sydney</h2>
<p>We help people across Sydney resolve separations through mediation \u2014 in person or online \u2014 with nationally accredited mediators (see the <a href='https://msb.org.au/' target='_blank' rel='noopener'>Mediator Standards Board</a>), many of whom are also experienced family lawyers. Whether you need advice, mediation, or both, the goal is the same: a fair outcome reached as quickly and amicably as possible, keeping you out of an unnecessary court battle. <a href="/sydney-mediation/">See mediation in Sydney \u2192</a></p>
"""
 ,
 [("Do I need a divorce lawyer or a mediator in Sydney?",
   "It depends on your situation. A lawyer is valuable for advice, complex matters, or where your ex won't engage. For most couples, mediation resolves parenting and property faster and cheaper."),
  ("When should I use a divorce lawyer?",
   "When you need advice on your entitlements, the matter is complex (significant assets, a business), there's family violence, your ex won't engage or disclose, or you need urgent orders."),
  ("Is mediation better than hiring a divorce lawyer?",
   "For most separating couples, mediation is the better first step \u2014 faster, cheaper, private and less damaging. Complex or high-conflict matters may still need a lawyer's advice."),
  ("Can I use both a lawyer and a mediator?",
   "Yes, and many people get the best outcome doing so \u2014 legal advice to understand their position, then mediation to reach the agreement, formalised through consent orders."),
  ("How do I choose the right family law professional?",
   "Look for accreditation and experience, ask whether they prioritise resolution or litigation, check that fees are transparent, and make sure you feel heard.")],
 [("sydney-mediation","Sydney Mediation"),
  ("family-law-mediation","Family Law Mediation"),
  ("mediate-or-litigate","Mediate or Litigate?"),
  ("cost-of-divorce-in-australia","Cost of Divorce"),
  ("collaborative-family-lawyers","Collaborative Family Lawyers"),
  ("consent-orders-explained","Consent Orders Explained")],
 read_min=8)
print("best-divorce-lawyers-sydney built")
