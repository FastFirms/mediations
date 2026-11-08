"""gen_blog_batch30.py — two new cornerstones.

travelling-overseas-with-children-after-separation — consent, passports, the Family Law Watchlist,
                                                     and agreeing a travel plan without court
who-pays-school-fees-after-separation               — private school fees, child support, change of
                                                     assessment, non-agency credits and agreements

Facts checked against the official pages cited inline (8 Nov 2026).
General information only, not legal advice.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ─────────────────────────────────────────────────────────────────────────────
# 1. Travelling overseas with children after separation
# ─────────────────────────────────────────────────────────────────────────────
post(
    "travelling-overseas-with-children-after-separation",
    "Travelling Overseas With Children After Separation",
    "Can you take your child overseas after separating? Consent, passports, the Family Law Watchlist, and how to agree a travel plan without going to court.",
    "Parenting",
    "Travelling overseas with children <em>after separation</em>",
    ("A family holiday, a visit to grandparents abroad, a wedding overseas: after separation, international travel "
     "with children needs the other parent's agreement, and sometimes the Court's. This guide explains when consent "
     "is legally required, how passports and the Family Law Watchlist work, and how to agree a travel plan calmly, "
     "before tickets are booked."),
    [("short-answer", "Can you take your child overseas?"),
     ("when-consent", "When written consent is legally required"),
     ("passports", "Child passports and parental consent"),
     ("watchlist", "The Family Law Watchlist"),
     ("worried", "If you are worried a child won't come back"),
     ("travel-plan", "What a good travel agreement covers"),
     ("mediation", "Agreeing travel through mediation"),
     ("court", "When you need the Court")],
    key_takeaway("If a parenting order is in force or family law proceedings are underway, taking a child out of Australia "
                 "without the written consent of everyone with a parenting order, or a court order, is a criminal offence. "
                 "Even without orders, a child passport generally needs the consent of everyone with parental responsibility. "
                 "The practical answer is the same in every case: agree the trip in writing first, ideally with dates, "
                 "itinerary and contact arrangements spelled out.")
    + f"""
<h2 id="short-answer">Can you take your child overseas after separation?</h2>
<p>Usually yes, with the other parent's agreement. Most overseas trips after separation go ahead without difficulty because both parents agree on the dates, the destination and how the child will stay in touch with the parent at home. Problems arise when one parent books first and asks later, or when there is a genuine fear that the child may not return.</p>
<p>Three separate systems are in play, and it helps to keep them apart:</p>
<ul>
<li><strong>The criminal law in the {cite('family_law_act')}</strong>, which makes it an offence to take a child overseas without consent or a court order once parenting orders exist or proceedings are pending.</li>
<li><strong>The passport rules</strong>, which generally require the consent of every person with parental responsibility before a child passport is issued.</li>
<li><strong>The Family Law Watchlist</strong>, run by the Australian Federal Police, which can stop a child leaving the country at the airport.</li>
</ul>
<p>Knowing which applies to you tells you what you need before you travel. None of it should replace a direct, respectful conversation with your co-parent, which is still the fastest route to a trip that goes ahead.</p>
"""
    + inline_cta("Planning a trip and not sure your co-parent will agree? A short mediation session can turn a tense email chain into a written travel plan.")
    + f"""
<h2 id="when-consent">When written consent is legally required</h2>
<p>The {cite('family_law_act')} (sections 65Y and 65Z) makes it a criminal offence to take or send a child out of Australia without the written consent of each person with a parenting order for the child, or an order of the Court, in two situations: where a parenting order is in force, and where proceedings for a parenting order are pending. The maximum penalty is three years' imprisonment.</p>
<figure class="tbl"><table><caption>What you need before a child leaves Australia</caption>
<thead><tr><th>Your situation</th><th>What the law requires</th><th>Practical step</th></tr></thead>
<tbody>
<tr><td>No parenting orders, no court proceedings</td><td>No specific travel offence, but passport consent rules still apply</td><td>Get the other parent's agreement in writing anyway; it protects everyone</td></tr>
<tr><td>Parenting orders in force</td><td>Written consent of each person with a parenting order, or a court order</td><td>Signed, dated consent naming the destination and travel dates</td></tr>
<tr><td>Parenting proceedings pending</td><td>Written consent of each party to the proceedings, or a court order</td><td>Consent in writing, or apply to the Court for permission</td></tr>
<tr><td>Orders that restrain travel or a Watchlist listing</td><td>A court order permitting the travel</td><td>Seek a consent order varying the restriction, or apply to the Court</td></tr>
</tbody></table></figure>
<p class="source-note">Source: Family Law Act 1975 (Cth), ss 65Y and 65Z. Check your own orders: many contain specific travel clauses that add notice periods or conditions.</p>
<p>Read your existing orders or <a href="/parenting-plans-guide/">parenting plan</a> carefully. Many already say how much notice must be given, what information must be provided and whether the other parent can unreasonably refuse. Following those clauses exactly is the simplest way to avoid a dispute.</p>
"""
    + inline_cta("Your orders say nothing about overseas travel? Mediation can add clear travel clauses before the next school holidays.")
    + f"""
<h2 id="passports">Child passports and parental consent</h2>
<p>Separately from family law, the Australian Passport Office generally needs the consent of everyone with parental responsibility for the child before it issues a passport. Its guidance on {cite('passports_consent')} explains that where full consent is not available, there are other routes: certain court orders, or an application to be assessed under "special circumstances".</p>
<ul>
<li><strong>Special circumstances are not guaranteed.</strong> The Passport Office cannot promise a passport will issue, and these applications typically take six to eight weeks or longer.</li>
<li><strong>A separate form is needed</strong> for each person with parental responsibility who does not consent.</li>
<li><strong>A family violence order does not, by itself, change</strong> who has parental responsibility for passport purposes.</li>
<li><strong>If proceedings are underway</strong> that could affect parental responsibility or travel, the Passport Office may expect you to seek the Court's direction first.</li>
</ul>
<p>A parent who is worried a passport may be issued without their knowledge can lodge a Child Alert Request with the Passport Office. That is a prevention tool, not a punishment, and it is often worth discussing openly with the other parent rather than lodging quietly.</p>
"""
    + inline_cta("Stuck on passport consent? Mediators help parents agree the safeguards that make signing the form feel safe.")
    + f"""
<h2 id="watchlist">The Family Law Watchlist</h2>
<p>The {cite('afp_watchlist')} (formerly known as the airport watch list) lets the Australian Federal Police stop a child from leaving Australia through an international port. A child can be placed on it where a court order restrains the child's travel overseas, or where an application for such an order has been filed.</p>
<p>A few practical points parents often miss:</p>
<ul>
<li>A Watchlist listing usually needs a court order or a filed application; it is not something the AFP will do on a phone call alone.</li>
<li>Once listed, a child generally cannot leave Australia until the Court orders otherwise or the order expires, even for a holiday both parents now support.</li>
<li>If you later agree a trip, you will need a court order (often by consent) permitting the travel or removing the listing. Leave plenty of time.</li>
</ul>
<p>Watchlist orders have an important place in genuine abduction risk. In most families, though, a detailed written agreement with safeguards achieves the same reassurance without locking the child out of every overseas trip.</p>
"""
    + inline_cta("Want reassurance without a Watchlist order? Mediation can build safeguards both parents trust into a written agreement.")
    + f"""
<h2 id="worried">If you are worried a child won't come back</h2>
<p>Sometimes the concern is not the holiday but the return. If you believe there is a real risk your child will be taken overseas and not returned, get legal advice <strong>urgently</strong>. A family lawyer can apply for orders restraining travel and for a Watchlist listing, sometimes on the same day.</p>
<p>If a child has already been taken to, or kept in, another country, the {cite('ag_child_abduction')} page explains the role of the Australian Central Authority. Australia is a party to the Hague Convention on the Civil Aspects of International Child Abduction, which provides a process for seeking a child's return from other member countries. Not every country is a member, which is one reason prevention matters so much.</p>
<p><strong>Safety first.</strong> If there is family violence, threats, or a risk to your child's safety, mediation may not be appropriate. Call <strong>000</strong> in an emergency, or 1800RESPECT on <strong>1800 737 732</strong> ({cite('respect_1800')}). Read our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a> for the exemptions that apply.</p>
"""
    + inline_cta("No safety concerns, just a trust gap? Mediation is designed to close it with clear, checkable commitments.")
    + f"""
<h2 id="travel-plan">What a good travel agreement covers</h2>
<p>Most refusals come from uncertainty, not opposition. The more detail you provide up front, the easier it is for the other parent to say yes. A good travel agreement, whether in a parenting plan or <a href="/consent-orders-explained/">consent orders</a>, usually covers:</p>
<figure class="tbl"><table><caption>Travel agreement checklist</caption>
<thead><tr><th>Item</th><th>Why it helps</th></tr></thead>
<tbody>
<tr><td>Notice period (e.g. 60 days before departure)</td><td>Avoids last-minute pressure and lets the other parent plan</td></tr>
<tr><td>Full itinerary: flights, addresses, contact numbers</td><td>The parent at home knows where the child is at all times</td></tr>
<tr><td>Return ticket provided before departure</td><td>The single most reassuring safeguard</td></tr>
<tr><td>Video or phone contact schedule</td><td>Keeps the child's relationship with both parents going</td></tr>
<tr><td>Make-up time for missed days</td><td>Shows the trip is not a loss for the other parent</td></tr>
<tr><td>Who holds the passport between trips</td><td>Removes a common flashpoint</td></tr>
<tr><td>Destination limits (e.g. Hague Convention countries)</td><td>Addresses abduction worries in a measured way</td></tr>
<tr><td>Consent not to be unreasonably withheld</td><td>Sets the tone for future trips</td></tr>
</tbody></table></figure>
<p>Agreeing these terms once, for all future travel, saves having the same negotiation every holiday. It also means a child can say yes to a cousin's wedding overseas without waiting on a court date.</p>
"""
    + inline_cta("Want a travel clause that works for every future holiday? Agree it once, in mediation, and stop renegotiating each trip.")
    + f"""
<h2 id="mediation">Agreeing travel through mediation</h2>
<p>Travel disputes are well suited to <a href="/family-law-mediation/">family law mediation</a>. The issues are concrete (dates, places, safeguards), the stakes are emotional rather than financial, and both parents usually want the child to have the experience if they feel secure about the return.</p>
<p>In a typical session, a mediator helps each parent say what they actually need: one parent wants their child to meet overseas family; the other wants to know the child will be home for the start of term. From there, the conversation moves quickly to safeguards. Where parents have filed in court about parenting, {cite('fcfcoa_fdr')} is generally expected first, unless an exemption applies.</p>
<p>If you reach agreement, you can record it in a parenting plan, or ask your lawyers to turn it into consent orders so the travel terms are enforceable. Many of our mediators are also family lawyers, and we work alongside your own lawyers rather than instead of them.</p>
"""
    + inline_cta("Holiday coming up? Book mediation now so the travel plan is settled well before departure.")
    + f"""
<h2 id="court">When you need the Court</h2>
<p>Court has its place, and some travel situations need it:</p>
<ul>
<li>A real risk of abduction, or a destination where return would be difficult to enforce.</li>
<li>A parent refuses consent after genuine attempts to agree, and the trip is time-sensitive.</li>
<li>A Watchlist listing or travel restraint needs to be lifted or varied.</li>
<li>A proposed long stay overseas starts to look like a <a href="/relocation-with-children-after-separation/">relocation</a> rather than a holiday.</li>
</ul>
<p>Where a court decides, the question is what is in the child's best interests under the {cite('family_law_act')}. Even then, an application usually goes more smoothly when both parents have already tried to agree and can show the Court a reasonable, detailed proposal.</p>
"""
    + inline_cta("Not sure whether your situation needs a lawyer, a mediator, or both? Book a free consultation and we will help you work out the right first step."),
    [("Can I take my child overseas without the other parent's permission in Australia?",
      "If a parenting order is in force or parenting proceedings are pending, taking a child out of Australia without the written consent of each person with a parenting order, or a court order, is a criminal offence under the Family Law Act. Even without orders, a child passport generally needs the consent of everyone with parental responsibility. Always get written agreement first."),
     ("What should a written travel consent include?",
      "The child's name, the destination, departure and return dates, flight details, where the child will stay, contact arrangements while away, and both parents' signatures and the date. If your orders set out a notice period or other conditions, follow them exactly."),
     ("Can I get my child a passport if my ex won't sign?",
      "Possibly. The Australian Passport Office can consider an application under special circumstances, or issue a passport where a court order permits it. Special circumstances applications take longer and are not guaranteed, so it is usually quicker to try to agree first, for example through mediation."),
     ("How do I stop my ex taking our child overseas?",
      "If you have a genuine concern, get urgent legal advice. A court can make orders restraining travel and the child can be placed on the AFP Family Law Watchlist. You can also lodge a Child Alert Request with the Passport Office. Where the worry is about safeguards rather than real risk, a mediated travel agreement may be enough."),
     ("Can we sort out overseas travel in mediation?",
      "Yes. Travel is one of the most common issues resolved in parenting mediation. Parents agree notice periods, itineraries, contact while away and safeguards such as return tickets, and can then record the agreement in a parenting plan or consent orders."),
     ("Does the Family Law Watchlist stop all travel?",
      "Generally, yes. A child on the Watchlist cannot leave Australia through an international port until the Court orders otherwise or the order expires. If you later agree to a trip, you will need a court order permitting the travel, so allow plenty of time.")],
    [("relocation-with-children-after-separation", "Relocation with children after separation"),
     ("parenting-plans-guide", "Parenting plans in Australia"),
     ("consent-orders-explained", "Consent orders explained"),
     ("how-to-change-parenting-orders", "How to change parenting orders"),
     ("christmas-parenting-arrangements-after-separation", "Holiday parenting arrangements"),
     ("co-parenting-mediation", "Co-parenting mediation")],
    read_min=9,
)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Who pays school fees after separation
# ─────────────────────────────────────────────────────────────────────────────
post(
    "who-pays-school-fees-after-separation",
    "Who Pays School Fees After Separation in Australia?",
    "Does child support cover private school fees? How the formula treats school costs, change of assessment, fee credits, agreements, and agreeing without court.",
    "Child support",
    "Who pays school fees <em>after separation</em>",
    ("School fees are one of the biggest, most predictable costs of raising children, and one of the most common "
     "flashpoints after separation. This guide explains what the child support formula does and does not cover, the "
     "three main ways private school fees are shared, and how parents can agree a fair arrangement without going to court."),
    [("short-answer", "The short answer"),
     ("formula", "What the child support formula covers"),
     ("options", "Four ways school fees get shared"),
     ("change-of-assessment", "Change of assessment for school fees"),
     ("credits", "Paying fees directly: non-agency credits"),
     ("agreements", "Child support agreements and school fees"),
     ("choosing-school", "Who decides which school?"),
     ("mediation", "Agreeing school costs in mediation")],
    key_takeaway("The standard child support formula does not automatically include private school fees. Parents can share "
                 "them by agreement (ideally a written child support agreement), Services Australia can change an assessment "
                 "where a child is being educated in the way both parents intended, and a paying parent who pays fees directly "
                 "may get partial credit. Agreeing the split, and which school, is usually faster and cheaper than any formal route.")
    + f"""
<h2 id="short-answer">Who pays school fees after separation? The short answer</h2>
<p>There is no automatic rule that private school fees are split 50/50, or that the parent paying child support also pays the fees. What happens depends on what the parents agree, what the children's schooling looked like before separation, and whether either parent asks Services Australia or the Court to step in.</p>
<p>In practice, most separated parents with children at private school end up in one of four places: an informal agreement, a formal child support agreement, a change of assessment, or (rarely) a court order. The earlier you talk about it, the more options you keep open, and the less likely a term invoice becomes the trigger for a bigger dispute.</p>
"""
    + inline_cta("School invoice arriving and no plan for who pays? A mediator can help you agree a split before it becomes a dispute.")
    + f"""
<h2 id="formula">What the child support formula covers</h2>
<p>A child support assessment from {cite('services_australia_cs')} uses a formula based on both parents' incomes, the number and ages of the children, and how much care each parent has. The formula is designed to cover the general costs of raising children, including ordinary schooling costs. It is not designed to cover private school fees, which vary enormously from school to school.</p>
<p>That gap matters. A family whose children were at a private school before separation can find the assessed amount falls well short of the real cost of keeping them there, while a parent paying child support may feel they are being asked to pay twice. Both views are understandable, and neither is resolved by the formula alone.</p>
"""
    + inline_cta("Formula and fees not lining up? Mediation lets you look at the whole picture, not just the assessment.")
    + f"""
<h2 id="options">Four ways school fees get shared</h2>
<figure class="tbl"><table><caption>Options for sharing school fees after separation</caption>
<thead><tr><th>Option</th><th>How it works</th><th>Binding?</th><th>Best suited to</th></tr></thead>
<tbody>
<tr><td>Informal agreement</td><td>Parents agree a split (e.g. by income share) and pay the school directly</td><td>No</td><td>Low-conflict parents with steady incomes</td></tr>
<tr><td>Child support agreement</td><td>A limited or binding agreement registered with Services Australia, which can include school fees</td><td>Yes, once accepted</td><td>Parents who want certainty for several years</td></tr>
<tr><td>Change of assessment</td><td>A parent applies to Services Australia to adjust the assessment for education costs</td><td>Yes, as part of the assessment</td><td>Where both parents intended private schooling but cannot agree the split</td></tr>
<tr><td>Court orders</td><td>Orders about decision-making on schooling, or departure orders for child support</td><td>Yes</td><td>Entrenched disputes after other options have failed</td></tr>
</tbody></table></figure>
<p class="source-note">Sources: Services Australia child support guidance; Family Law Act 1975 (Cth). Rules change, so check current details before relying on them.</p>
<p>Many families combine options: an informal agreement for this year's fees while they work towards a formal agreement covering the rest of the children's schooling.</p>
"""
    + inline_cta("Not sure which option suits your family? Book a free consultation and talk it through with an experienced family mediator.")
    + f"""
<h2 id="change-of-assessment">Change of assessment for school fees</h2>
<p>If parents cannot agree, either parent can ask Services Australia to change the assessment because of special circumstances. According to {cite('sa_change_assessment')}, one of the recognised reasons is that the costs of raising the child are significantly affected because the child is being cared for, educated or trained in the way both parents intended. Attending a private school is the classic example.</p>
<p>The key words are <strong>both parents intended</strong>. Evidence that helps includes enrolment decisions made together before separation, years of attendance at the school, emails or messages discussing schooling, and the family's financial position when the decision was made. A child enrolled at an expensive school by one parent after separation, over the other's objection, is a very different case.</p>
<p>The application is free, but it takes time, and the outcome is not guaranteed. Either parent can object to a decision, and the process can become adversarial if it is used as a first step rather than a fallback.</p>
"""
    + inline_cta("Rather agree the split than wait on a decision? Mediation can get you there in a single session.")
    + f"""
<h2 id="credits">Paying fees directly: non-agency credits</h2>
<p>Sometimes the paying parent pays the school directly instead of, or as well as, paying child support. Services Australia can treat some of these payments as "prescribed non-agency payments". Its guidance on {cite('sa_non_agency')} explains the key conditions:</p>
<ul>
<li>The paying parent must have <strong>less than 14% care</strong> of the children.</li>
<li>The paying parent must be paying at least <strong>70% of their monthly child support</strong> on time.</li>
<li>The credit is capped at <strong>30% of the monthly liability</strong>, and unused credit can carry forward.</li>
<li>Eligible items include school fees, uniforms and books, and certain child care and essential medical and dental costs.</li>
<li>Keep receipts and send proof of payment, or the credit may not be applied.</li>
</ul>
<p>These credits are a safety net, not a plan. They rarely match the full cost of private school fees, and they can create friction if the receiving parent did not expect them. Agreeing in advance how direct payments will be treated avoids that surprise.</p>
"""
    + inline_cta("Paying the school directly and worried it won't count? Agree how it is credited before the next term starts.")
    + f"""
<h2 id="agreements">Child support agreements and school fees</h2>
<p>A child support agreement lets parents set their own arrangement and register it with Services Australia. There are two types:</p>
<ul>
<li><strong>Limited child support agreements</strong> need a child support assessment in place and must provide at least the assessed amount. They suit parents who want to add school fees on top of the formula.</li>
<li><strong>Binding child support agreements</strong> can set any amount, including payments made directly to the school instead of periodic payments. Each parent must get independent legal advice before signing, and the lawyers sign certificates confirming it.</li>
</ul>
<p>A well-drafted agreement deals with the details that cause later disputes: which school (or what happens if the child changes schools), which costs are included (tuition, levies, camps, uniforms, devices), each parent's share, when payments are made, and what happens if a parent's income changes significantly. Our <a href="/child-support-guide/">child support guide</a> explains how agreements sit alongside assessments.</p>
"""
    + inline_cta("Want school fees locked in for the years ahead? Mediation is a practical way to agree the terms your lawyers then formalise.")
    + f"""
<h2 id="choosing-school">Who decides which school?</h2>
<p>The fee question often hides a bigger one: which school the child should attend. Choosing a school is a major long-term decision about the child. Unless orders say otherwise, both parents generally have parental responsibility, and under the {cite('family_law_act')} parenting orders can set out whether major long-term decisions such as education are made jointly or by one parent. Since the May 2024 reforms there is no presumption of equal shared parental responsibility; the focus is the child's best interests.</p>
<p>Fairness usually means discussing affordability and the child's needs together, before a decision is made. Where one parent wants a private school and the other cannot afford a share, options include a lower-fee school, a contribution in proportion to income, grandparent help, or a staged approach such as public primary and private secondary.</p>
<p>If you cannot agree, a court can decide, but it will look at the child's best interests and the family's circumstances, and the process is slow and expensive compared with a negotiated outcome. Before filing for parenting orders, {cite('fcfcoa_fdr')} is generally required unless an exemption applies.</p>
"""
    + inline_cta("Disagree about which school, not just who pays? Mediation can work through both questions together.")
    + f"""
<h2 id="mediation">Agreeing school costs in mediation</h2>
<p>School fee disputes are usually about money and values at once. One parent sees a private education as part of the life the children already have; the other sees a bill they did not choose and cannot easily meet. <a href="/child-support-mediation/">Child support mediation</a> gives both parents room to say that, and then to move to numbers.</p>
<p>A typical mediation covers each parent's income and budget, the true annual cost of the school (not just tuition), possible splits, how fee increases and extras are handled, and a review point if circumstances change. Agreements can then be recorded in a parenting plan, a child support agreement, or consent orders with your lawyers' help.</p>
<p>Court has its place, but rarely as the best place to start a conversation about a school invoice. Most parents would rather spend the money on the fees.</p>
"""
    + inline_cta("Ready to settle school fees for good? Book a free consultation with Mediations Australia."),
    [("Does child support cover private school fees in Australia?",
      "Not automatically. The child support formula covers the general costs of raising children but is not designed for private school fees. Parents can agree to share them, or a parent can apply to Services Australia for a change of assessment where the child is being educated in the way both parents intended."),
     ("Do I have to pay half of my child's private school fees?",
      "There is no automatic 50/50 rule. What you pay depends on any agreement, any change of assessment Services Australia makes, and any court orders. Many parents agree to share fees in proportion to their incomes."),
     ("Can my ex enrol our child in a private school and make me pay?",
      "Not unilaterally. Choosing a school is generally a major long-term decision, and a change of assessment for school fees focuses on whether both parents intended that education. If one parent enrols the child over the other's objection, a claim for a contribution is much weaker."),
     ("If I pay school fees directly, does it count as child support?",
      "Sometimes. Services Australia can credit prescribed non-agency payments such as school fees, generally up to 30% of the monthly liability, if you have less than 14% care and are paying at least 70% of your child support on time. Keep receipts and send proof of payment."),
     ("Can school fees be included in a child support agreement?",
      "Yes. Limited and binding child support agreements can include school fees. Binding agreements require independent legal advice for each parent before signing."),
     ("Can mediation help us agree on school fees?",
      "Yes. Mediation helps parents agree which school, the true annual cost, each parent's share and how increases are handled, and the agreement can then be formalised in a child support agreement or consent orders.")],
    [("child-support-guide", "Child support in Australia"),
     ("parenting-plans-guide", "Parenting plans in Australia"),
     ("co-parenting-mediation", "Co-parenting mediation"),
     ("who-pays-bills-during-separation", "Who pays the bills during separation?"),
     ("consent-orders-explained", "Consent orders explained"),
     ("what-is-mediation-in-family-law", "What is mediation in family law?")],
    read_min=9,
)
