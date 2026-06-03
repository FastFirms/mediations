#!/usr/bin/env python3
"""Generate all service pages with unique, substantive, AEO-optimised content."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def phero(eyebrow, h1, lede):
    return f"""<main id="main">
{crumb_html([("Home",""),(h1.split(" that ")[0].split(",")[0],None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""

def answer(text):
    return f'<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {text}</p></div></div>'

def body(blocks):
    return f'<article class="body"><div class="wrap-narrow reveal">{blocks}</div></article>'

def build(slug, title, desc, eyebrow, h1, lede, ans, blocks, qa, crumb_name, cta_h, cta_p):
    schema = [org_schema(),
              breadcrumb_schema([("Home",""),(crumb_name,slug)]),
              service_schema(crumb_name, desc, slug),
              faq_schema(qa)]
    html_doc = head(title, desc, slug, extra_schema=schema)
    html_doc += nav()
    # rebuild phero with correct crumb
    phero_html = f"""<main id="main">
{crumb_html([("Home",""),(crumb_name,None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""
    html_doc += phero_html
    html_doc += answer(ans)
    html_doc += body(blocks)
    html_doc += faq_html(qa, heading=f"{crumb_name} FAQs")
    html_doc += cta_band(cta_h, cta_p)
    html_doc += "</main>" + page_end()
    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(html_doc)
    return slug

# ============================================================
# SERVICE PAGE CONTENT — unique, substantive, answer-first
# ============================================================

build(
 "property-settlement-mediation",
 "Property Settlement Mediation | Divide Assets, No Court",
 "Resolve your property settlement through mediation — divide assets, debts and super fairly without court. Accredited mediators, fixed-fee, formalised in consent orders.",
 "Property &amp; financial settlements",
 "Property Settlement Mediation — divide assets <em>fairly and finally</em>.",
 "Separating means untangling a shared financial life — the home, savings, super, debts and businesses. Mediation lets you divide it all by agreement, quickly and privately, instead of handing the decision to a court after years of legal fees.",
 "Property settlement mediation is a process where separating partners agree on how to divide assets, debts and superannuation with the help of a neutral mediator, then formalise it through consent orders or a binding financial agreement. It typically resolves in one or two sessions and costs a fraction of litigation.",
 """
 <h2>How is a property settlement <em>actually</em> decided?</h2>
 <p>Australian family law follows a four-step approach to dividing property, and mediation works within exactly the same framework — so your agreement reflects what a court would likely consider fair:</p>
 <ol>
   <li><strong>Identify the asset pool</strong> — everything you own and owe, together and separately: property, savings, superannuation, vehicles, businesses and debts.</li>
   <li><strong>Assess contributions</strong> — financial contributions (income, assets brought in) and non-financial ones (homemaking, parenting, renovations).</li>
   <li><strong>Consider future needs</strong> — earning capacity, age, health, and who cares for the children.</li>
   <li><strong>Check it's just and equitable</strong> — that the overall split is fair in the circumstances.</li>
 </ol>
 <p>In mediation, your mediator helps you work through each step openly, so the outcome is grounded in the same principles a judge would apply — but reached in days, not years.</p>

 <h2>What can be included in a property settlement?</h2>
 <ul>
   <li>The family home and any investment properties</li>
   <li>Superannuation (which can be split between partners)</li>
   <li>Savings, shares and investments</li>
   <li>Vehicles, furniture and personal property</li>
   <li>Business interests and trusts</li>
   <li>Debts, mortgages and liabilities</li>
 </ul>

 <div class="callout">
   <h3>You have time limits — but you have options</h3>
   <p>After a divorce you generally have 12 months to finalise property matters, and de facto couples have two years from separation. Mediation is the fastest way to reach agreement within those windows. <a href="/de-facto-mediation/">See de facto property disputes →</a></p>
 </div>

 <h2>Why mediate rather than litigate your settlement?</h2>
 <p>Because a contested property case can consume a meaningful share of the very asset pool you're fighting over. Mediation keeps the money where it belongs — with you and your family — and lets you craft creative solutions a court can't, like staggered payouts or keeping the home until children finish school. Many family lawyers recommend it as the sensible first step. <a href="/property-settlement-mediation/">Once you agree, we formalise it in consent orders.</a></p>
 """,
 [("How long do I have to finalise a property settlement?",
   "After divorce you generally have 12 months to apply for property orders; de facto couples have two years from the date of separation. Mediation is the fastest way to reach a binding agreement inside these limits."),
  ("Can superannuation be divided in mediation?",
   "Yes. Superannuation is treated as property under Australian family law and can be split between partners. Your mediation agreement can include a superannuation split, formalised through consent orders."),
  ("Is a mediated property agreement legally binding?",
   "It becomes binding once formalised — either as consent orders approved by the court or as a binding financial agreement. We handle that step so your settlement is enforceable."),
  ("What if we can't agree on the value of an asset?",
   "Independent valuations (for property, businesses or super) are commonly used. The mediator helps you agree on a valuation process so the division is based on fair, agreed figures.")],
 "Property Settlement Mediation",
 "Settle your property matters <em>this month</em>, not next year.",
 "Book a fixed-fee consultation and get a clear, honest view of how mediation can divide your assets fairly — without the cost and delay of court.")

build(
 "parenting-plan-mediation",
 "Parenting Plan Mediation | Custody Agreements, No Court",
 "Create a workable parenting plan through mediation. Agree on living arrangements, time and decisions for your children — faster and cheaper than a custody court battle.",
 "Parenting &amp; children's arrangements",
 "Parenting Plan Mediation — built around <em>your children</em>.",
 "The hardest part of separating is working out arrangements for the kids. Mediation gives you a calm, structured way to agree on living arrangements, time with each parent and how decisions get made — putting your children first and keeping the choice in your hands.",
 "Parenting plan mediation helps separated parents agree on living arrangements, time-sharing and decision-making for their children, guided by a neutral mediator. It is child-focused, faster and far less costly than a contested parenting case, and for most families it is a required step before court.",
 """
 <h2>What does a parenting plan cover?</h2>
 <p>A parenting plan is a written agreement that sets out the practical arrangements for raising your children after separation. A thorough plan usually covers:</p>
 <ul>
   <li>Where the children live and how time is shared between parents</li>
   <li>How handovers, holidays and special occasions work</li>
   <li>How major long-term decisions (school, health, religion) are made</li>
   <li>How parents will communicate and resolve future disagreements</li>
   <li>Arrangements for travel, including overseas</li>
 </ul>

 <h2>Is a parenting plan legally binding?</h2>
 <p>A parenting plan itself is not legally enforceable, but it carries real weight — a court will consider it if a dispute later arises. If you want a binding outcome, your agreement can be turned into <a href="/consent-orders/">consent orders</a>, which are enforceable. Many families start with a parenting plan and formalise it once arrangements have settled.</p>

 <div class="callout">
   <h3>Children do better when parents agree</h3>
   <p>Research consistently shows children adjust best to separation when conflict is low and both parents stay involved. Mediation is designed to lower conflict — which is exactly what protects your children long term.</p>
 </div>

 <h2>Do we have to mediate before going to court?</h2>
 <p>For most parenting matters, yes. Under the Family Law Act you must make a genuine attempt at family dispute resolution before applying for parenting orders, unless an exemption applies. You'll need a <a href="/section-60i-certificates/">Section 60I certificate</a> to file — which we can issue as part of your mediation.</p>
 """,
 [("Is a parenting plan legally enforceable?",
   "A parenting plan is not directly enforceable, but a court will take it into account in any later dispute. To make arrangements binding, they can be formalised as consent orders, which are enforceable."),
  ("What's the difference between a parenting plan and consent orders?",
   "A parenting plan is a flexible written agreement signed by both parents. Consent orders are approved by the court and legally binding. Many parents start with a plan and convert it to consent orders later."),
  ("Do both parents have to agree to mediation?",
   "Mediation is voluntary, but both parents are strongly encouraged to attend, and a genuine attempt is generally required before court. If one parent refuses, the other can still obtain a Section 60I certificate."),
  ("Can children have a say in the parenting plan?",
   "Where appropriate, child-inclusive practices can ensure children's views are heard in an age-appropriate way, without putting them in the middle of the dispute.")],
 "Parenting Plan Mediation",
 "Put your children first — <em>starting today</em>.",
 "Book a fixed-fee consultation and let an accredited family mediator help you build a parenting plan that works for everyone who matters most.")

build(
 "section-60i-certificates",
 "Section 60I Certificate | Family Dispute Resolution Australia",
 "Need a Section 60I certificate before family court? Our accredited practitioners conduct mediation and issue Section 60I certificates so you can meet your legal obligations.",
 "Required before parenting court action",
 "Section 60I Certificates — issued by <em>accredited practitioners</em>.",
 "Before you can apply to court for parenting orders, the law requires you to attempt family dispute resolution first — and prove it with a Section 60I certificate. We conduct the mediation and issue the certificate, so you meet your obligations and genuinely try to resolve things at once.",
 "A Section 60I certificate is a document issued by an accredited Family Dispute Resolution Practitioner confirming you attempted mediation before applying to court for parenting orders. Under the Family Law Act 1975 it is generally required to file a parenting application, unless an exemption (such as family violence or urgency) applies.",
 """
 <h2>When do you need a Section 60I certificate?</h2>
 <p>You generally need one before filing any application for parenting orders in the Federal Circuit and Family Court of Australia. It proves you made a genuine effort to resolve the dispute through family dispute resolution before asking a court to decide.</p>

 <h2>What are the five types of Section 60I certificate?</h2>
 <p>An accredited practitioner can issue a certificate stating that:</p>
 <ul>
   <li>The other party did not attend, despite being invited</li>
   <li>Both parties attended and made a genuine effort to resolve the dispute</li>
   <li>Both parties attended but one or both did not make a genuine effort</li>
   <li>The practitioner decided the matter was not appropriate for mediation</li>
   <li>Mediation started but the practitioner decided it was not appropriate to continue</li>
 </ul>

 <div class="callout">
   <h3>When a certificate isn't required</h3>
   <p>Exemptions apply in cases of family violence, child abuse risk, genuine urgency, or where a party is unable to participate. If this is your situation, tell us in your consultation and we'll advise the safest, correct path.</p>
 </div>

 <h2>How do you get a Section 60I certificate?</h2>
 <p>You attend family dispute resolution with an accredited practitioner. If the matter resolves, you may not need to go to court at all. If it doesn't, the practitioner issues the certificate so you can file. Either way you've moved forward. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
 """,
 [("How long is a Section 60I certificate valid?",
   "A Section 60I certificate is generally valid for 12 months from the date of issue. If you don't file within that time, you may need to attend family dispute resolution again."),
  ("Who can issue a Section 60I certificate?",
   "Only an accredited Family Dispute Resolution Practitioner can issue one. Our practitioners are accredited and issue certificates as part of the mediation process."),
  ("Do I need a certificate for property matters?",
   "No. Section 60I certificates relate to parenting matters. Property and financial disputes don't require one, though mediation is still strongly encouraged."),
  ("What if the other parent won't attend?",
   "If the other parent is invited but doesn't attend, the practitioner can issue a certificate to that effect, allowing you to proceed to court.")],
 "Section 60I Certificates",
 "Meet your obligations — and maybe avoid court <em>entirely</em>.",
 "Book a consultation with an accredited Family Dispute Resolution Practitioner. We'll conduct your mediation and issue your Section 60I certificate if you need it.")

build(
 "financial-agreements-mediation",
 "Binding Financial Agreements (BFA) Mediation | Protect Assets",
 "Negotiate a binding financial agreement (BFA) through mediation — before, during or after a relationship. Protect assets with accredited mediators and proper legal advice.",
 "Binding financial agreements",
 "Financial Agreement Mediation — <em>protect what matters</em>.",
 "A binding financial agreement sets out how assets and finances are handled if a relationship ends. Mediation is the calm way to negotiate one — whether you're entering a relationship, already in one, or separating — so the terms are genuinely agreed rather than fought over.",
 "A binding financial agreement (BFA) is a private contract between partners that sets out how property, finances and support will be divided if they separate. Mediation helps couples negotiate fair terms, which are then formalised with independent legal advice to make the agreement binding under the Family Law Act.",
 """
 <h2>When can you make a binding financial agreement?</h2>
 <p>BFAs can be made at any stage of a relationship:</p>
 <ul>
   <li><strong>Before</strong> a marriage or de facto relationship (sometimes called a prenup)</li>
   <li><strong>During</strong> the relationship, to clarify financial arrangements</li>
   <li><strong>After</strong> separation, to finalise property and support</li>
 </ul>

 <h2>What makes a financial agreement legally binding?</h2>
 <p>For a BFA to be binding under Australian law, strict requirements must be met — most importantly, each party must receive independent legal advice before signing. Mediation handles the hard part (reaching fair terms everyone accepts); the formal legal steps then make it enforceable. We guide you through both.</p>

 <div class="callout">
   <h3>BFA or consent orders — which is right for you?</h3>
   <p>Both can finalise property matters, but they work differently. Consent orders are approved by a court; BFAs are private contracts. We'll help you choose. <a href="/consent-orders/">Compare consent orders →</a></p>
 </div>

 <h2>Why mediate a financial agreement?</h2>
 <p>Because financial agreements negotiated adversarially breed resentment and are more likely to be challenged later. Terms reached through mediation tend to be fairer, better understood by both parties, and more durable. <a href="/spousal-support-mediation/">See spousal maintenance →</a></p>
 """,
 [("What is a binding financial agreement?",
   "A BFA is a private contract between partners setting out how assets, finances and support are handled if they separate. It can be made before, during or after a relationship."),
  ("Do both people need their own lawyer for a BFA?",
   "Yes. For a BFA to be binding, each party must receive independent legal advice before signing. Mediation reaches the agreed terms; independent advice makes it enforceable."),
  ("Can a binding financial agreement be overturned?",
   "A BFA can be set aside in limited circumstances — for example fraud, non-disclosure, or if proper procedures weren't followed. Agreements reached fairly through mediation are far less likely to be challenged."),
  ("Is a BFA the same as a prenup?",
   "A prenup is simply a BFA made before marriage or a de facto relationship. The same legal framework applies.")],
 "Binding Financial Agreements",
 "Protect your future, <em>without the conflict</em>.",
 "Book a fixed-fee consultation to negotiate a fair financial agreement through mediation — with the legal formalisation that makes it binding.")

build(
 "spousal-support-mediation",
 "Spousal Maintenance Mediation | Fair Support, No Court",
 "Resolve spousal maintenance through mediation. Agree on fair, sustainable support without court — accredited mediators, fixed-fee, formalised properly.",
 "Spousal &amp; partner maintenance",
 "Spousal Maintenance Mediation, settled <em>fairly and respectfully</em>.",
 "When one partner can't adequately support themselves after separation, the other may be required to help. Mediation lets you agree on fair, realistic maintenance — based on genuine need and capacity to pay — without a draining court fight.",
 "Spousal maintenance is financial support one partner pays the other after separation when that partner cannot reasonably meet their own needs. Mediation helps couples agree on the amount and duration based on need and capacity to pay, then formalise it in consent orders or a financial agreement.",
 """
 <h2>Who is entitled to spousal maintenance?</h2>
 <p>Spousal maintenance isn't automatic. It depends on two things: one partner's genuine need for support, and the other partner's capacity to pay. A court (or your mediation) weighs factors such as:</p>
 <ul>
   <li>Age, health and ability to earn an income</li>
   <li>Care of children and its effect on earning capacity</li>
   <li>The standard of living that's reasonable in the circumstances</li>
   <li>The length of the relationship and its financial impact</li>
 </ul>

 <h2>How is spousal maintenance different from child support?</h2>
 <p>Child support is for the costs of raising children and is usually assessed by Services Australia. Spousal maintenance supports a former partner directly. They're separate — and you may deal with both. <a href="/child-support-mediation/">See child support mediation →</a></p>

 <div class="callout">
   <h3>Maintenance can be a lump sum or periodic</h3>
   <p>Mediation lets you design arrangements that genuinely fit — a one-off lump sum, periodic payments for a fixed time, or support while a partner retrains. A court order is often more rigid.</p>
 </div>

 <h2>Why mediate spousal maintenance?</h2>
 <p>Because these arrangements work best when both people understand and accept them. Mediation produces sustainable agreements rather than imposed obligations that breed missed payments and return trips to court. <a href="/property-settlement-mediation/">Often it's resolved alongside your property settlement.</a></p>
 """,
 [("Am I automatically entitled to spousal maintenance?",
   "No. Entitlement depends on one partner's genuine need and the other's capacity to pay. Mediation helps you assess both fairly and agree on a realistic arrangement."),
  ("How long does spousal maintenance last?",
   "It varies. Maintenance can be a lump sum, or periodic payments for a fixed period — for example while a partner retrains or returns to work. Mediation lets you tailor the duration."),
  ("Is spousal maintenance the same as child support?",
   "No. Child support covers the costs of raising children; spousal maintenance supports a former partner. They are assessed separately and you may address both."),
  ("Can a spousal maintenance agreement be made binding?",
   "Yes, through consent orders or a binding financial agreement. We help you formalise whatever you agree in mediation.")],
 "Spousal Maintenance Mediation",
 "Reach a fair arrangement, <em>without the fight</em>.",
 "Book a fixed-fee consultation to resolve spousal maintenance through mediation — fairly, sustainably and without court.")

build(
 "child-support-mediation",
 "Child Support Mediation Australia | Resolve It Privately",
 "Resolve child support disputes through mediation. Agree on private arrangements, departures from assessment and special expenses — without court, with accredited mediators.",
 "Child support arrangements",
 "Child Support Mediation — resolved <em>privately and fairly</em>.",
 "Child support disagreements can poison co-parenting. Mediation gives you a private, practical way to agree on arrangements — including private agreements that go beyond the standard formula — so your children are properly supported and the conflict ends.",
 "Child support mediation helps separated parents resolve disagreements about supporting their children — including private child support agreements, departures from the standard assessment, and how special expenses are shared. It keeps decisions private and cooperative rather than adversarial.",
 """
 <h2>How is child support normally calculated?</h2>
 <p>In Australia, child support is usually assessed by Services Australia using a formula based on both parents' incomes, the care arrangements, and the costs of children. But the formula doesn't fit every family — and that's where mediation helps.</p>

 <h2>What can child support mediation resolve?</h2>
 <ul>
   <li>Private child support agreements that suit your circumstances</li>
   <li>How school fees, medical costs and extracurricular expenses are shared</li>
   <li>Disagreements about the assessment or a change in circumstances</li>
   <li>Arrangements that work alongside your parenting plan</li>
 </ul>

 <div class="callout">
   <h3>A binding child support agreement</h3>
   <p>Parents can make a binding child support agreement that departs from the formula — for example covering private school fees directly. As with a BFA, each parent needs independent legal advice. We guide you through it.</p>
 </div>

 <h2>Why not just rely on the assessment?</h2>
 <p>The formula is a starting point, not a complete solution — it rarely addresses big-ticket items like private schooling or significant medical needs. Mediation lets you build a complete, tailored arrangement that actually reflects your children's lives. <a href="/parenting-plan-mediation/">Pairs naturally with a parenting plan.</a></p>
 """,
 [("Can we agree on child support privately instead of using the formula?",
   "Yes. Parents can make a private or binding child support agreement that departs from the standard assessment. Mediation helps you negotiate fair terms; a binding agreement requires independent legal advice."),
  ("Does child support mediation replace Services Australia?",
   "Not entirely — Services Australia still administers assessments. Mediation helps you resolve disputes and reach agreements that can sit alongside or depart from the assessment."),
  ("Can mediation cover school fees and medical costs?",
   "Yes. These 'special expenses' are a common focus of child support mediation, since the standard formula often doesn't address them adequately."),
  ("What if the other parent won't pay what was assessed?",
   "Mediation can address the underlying disagreement and create a workable plan. Enforcement remains available through Services Australia, but resolving the conflict often prevents the problem recurring.")],
 "Child Support Mediation",
 "Support your children — <em>without the standoff</em>.",
 "Book a fixed-fee consultation to resolve child support through mediation, with arrangements that genuinely fit your family.")

build(
 "de-facto-mediation",
 "De Facto Relationship Mediation Australia | Same Rights",
 "Resolve de facto relationship disputes through mediation — property, finances and parenting. De facto partners have similar rights to married couples. No court required.",
 "De facto &amp; same-sex relationships",
 "De Facto Mediation — <em>same rights, same clarity</em>.",
 "De facto and same-sex partners have substantially the same rights as married couples when a relationship ends. Mediation resolves property, financial and parenting matters the same way — quickly, privately and without court — once your relationship qualifies under the law.",
 "De facto relationship mediation resolves property, financial and parenting disputes for unmarried couples, including same-sex partners. De facto partners have similar rights to married couples under the Family Law Act, and mediation offers the same fast, private, out-of-court path to resolution.",
 """
 <h2>What counts as a de facto relationship?</h2>
 <p>You're generally considered de facto if you've lived together on a genuine domestic basis. Courts look at factors including the length of the relationship, whether you lived together, financial interdependence, a shared residence, and whether you have children together. Same-sex relationships are treated identically.</p>

 <h2>Do de facto partners have the same rights as married couples?</h2>
 <p>Largely, yes. When a qualifying de facto relationship ends, partners can seek property settlements, superannuation splits and spousal maintenance — much like divorcing couples. The main differences are in time limits and the threshold of proving the relationship existed.</p>

 <div class="callout">
   <h3>Time limit: two years</h3>
   <p>De facto partners generally have two years from separation to apply for property or maintenance orders. Mediation is the fastest way to reach a binding agreement within that window. <a href="/property-settlement-mediation/">See property settlement →</a></p>
 </div>

 <h2>Why mediation suits de facto disputes</h2>
 <p>De facto separations often involve disentangling finances that were never formally combined, which can get contentious fast. Mediation provides the neutral structure to sort it out fairly — and avoids the added cost of first proving the relationship's existence in court. <a href="/financial-agreements-mediation/">A financial agreement can also protect both partners.</a></p>
 """,
 [("Do de facto couples have the same rights as married couples?",
   "Largely yes. Qualifying de facto partners can seek property settlements, superannuation splits and maintenance under the Family Law Act, similar to married couples, with some differences in time limits and proving the relationship."),
  ("How long do de facto partners have to make a claim?",
   "Generally two years from the date of separation. Mediation is the fastest way to reach a binding agreement within that limit."),
  ("Are same-sex relationships treated the same?",
   "Yes. Same-sex de facto relationships have the same status and rights under Australian family law."),
  ("How do we prove we were in a de facto relationship?",
   "Courts consider factors like living together, the length of the relationship, financial interdependence and shared children. Mediation can proceed by agreement without a contested court finding.")],
 "De Facto Relationship Mediation",
 "Same rights. Same fairness. <em>Far less stress.</em>",
 "Book a fixed-fee consultation to resolve your de facto dispute through mediation — property, finances and parenting, all without court.")

build(
 "grandparents-mediation",
 "Grandparents' Rights Mediation | See Your Grandchildren",
 "Grandparents can use mediation to keep seeing grandchildren after family breakdown. Resolve contact arrangements respectfully, without court. Accredited mediators.",
 "Grandparents &amp; extended family",
 "Grandparents' Rights Mediation — <em>stay part of the family</em>.",
 "When families break down, grandparents can lose contact with grandchildren they love. Australian law recognises children's right to a relationship with people significant to their care — including grandparents — and mediation is the gentlest way to restore and protect that bond.",
 "Grandparents' mediation helps grandparents reach agreement about spending time with their grandchildren after a separation or family conflict. The Family Law Act recognises children's right to maintain relationships with grandparents and other significant people, and mediation resolves this without a contested court case.",
 """
 <h2>Do grandparents have legal rights to see grandchildren?</h2>
 <p>The law focuses on the child's right to maintain meaningful relationships with people significant to their welfare — which expressly includes grandparents. Grandparents can apply for orders to spend time with grandchildren, but mediation is almost always the better first step: it's less adversarial and far easier on the children.</p>

 <h2>When does grandparent mediation help?</h2>
 <ul>
   <li>After a parental separation that has cut off contact</li>
   <li>When a family conflict has damaged relationships</li>
   <li>Where a parent has passed away and contact is at risk</li>
   <li>When grandparents are providing significant care and need certainty</li>
 </ul>

 <div class="callout">
   <h3>The children come first — always</h3>
   <p>Mediation keeps the focus where it belongs: on what's best for the children, not on adult grievances. That child-centred approach is exactly why it works where confrontation fails.</p>
 </div>

 <h2>Why mediate rather than litigate?</h2>
 <p>Court action against your own children or their former partners can permanently fracture a family. Mediation rebuilds communication instead of destroying it — giving you the best chance of a lasting relationship with your grandchildren. <a href="/parenting-plan-mediation/">Arrangements can be included in a parenting plan.</a></p>
 """,
 [("Do grandparents have a legal right to see their grandchildren?",
   "The law recognises a child's right to maintain relationships with significant people including grandparents. Grandparents can apply for time with grandchildren, but mediation is usually the better first step."),
  ("Can grandparents apply for parenting orders?",
   "Yes. Grandparents can apply for orders about spending time with or caring for grandchildren, though mediation is encouraged before court."),
  ("Do grandparents need a Section 60I certificate?",
   "If applying for parenting orders, grandparents generally need to attempt family dispute resolution first, the same as parents. We can conduct this and issue the certificate."),
  ("What if a parent refuses any contact?",
   "Mediation provides a neutral space to address the parent's concerns and rebuild trust. It succeeds in many cases where direct conversations have broken down.")],
 "Grandparents' Mediation",
 "Don't lose the bond — <em>rebuild it</em>.",
 "Book a fixed-fee consultation to restore contact with your grandchildren through respectful, child-focused mediation.")

build(
 "consent-orders",
 "Consent Orders Australia | Make Your Agreement Legally Binding",
 "Turn your mediated agreement into legally binding consent orders. We prepare and lodge consent orders for parenting and property — no court hearing required.",
 "Formalising your agreement",
 "Consent Orders — make your agreement <em>legally binding</em>.",
 "Reaching agreement is the hard part — consent orders make it stick. They turn what you've agreed into legally enforceable court orders, usually without anyone setting foot in a courtroom. We prepare and lodge them for you.",
 "Consent orders are written agreements approved by the Federal Circuit and Family Court of Australia that make your parenting or property arrangements legally binding. You don't attend a hearing — the court reviews your agreement on the papers and, if it's fair, makes it into enforceable orders.",
 """
 <h2>What can consent orders cover?</h2>
 <ul>
   <li><strong>Parenting</strong> — living arrangements, time with each parent, decision-making</li>
   <li><strong>Property</strong> — division of assets, debts and superannuation</li>
   <li><strong>Spousal maintenance</strong> — ongoing financial support</li>
 </ul>

 <h2>How do consent orders work?</h2>
 <p>Once you reach agreement (often through mediation), an application for consent orders is prepared and lodged with the court. A registrar reviews it to ensure parenting arrangements are in the children's best interests and property division is just and equitable. If satisfied, the court makes the orders — no hearing, no appearance. For a step-by-step walkthrough of the process, costs and timeframes, see our <a href="/consent-orders-explained/">consent orders explained guide</a>.</p>

 <div class="callout">
   <h3>Consent orders vs a parenting plan vs a BFA</h3>
   <p>Consent orders are court-approved and enforceable. A <a href="/parenting-plan-mediation/">parenting plan</a> is flexible but not directly enforceable. A <a href="/financial-agreements-mediation/">binding financial agreement</a> is a private contract for financial matters. We help you choose the right instrument.</p>
 </div>

 <h2>Why mediate first, then formalise?</h2>
 <p>Because consent orders only work when you actually agree — the court won't impose terms in a consent application. Mediation gets you to that agreement efficiently; consent orders lock it in. It's the complete path from dispute to durable resolution. <a href="/property-settlement-mediation/">Start with property settlement →</a></p>
 """,
 [("Do I have to go to court for consent orders?",
   "No. Consent orders are reviewed by the court on the papers. If your agreement is fair, the court makes the orders without anyone attending a hearing."),
  ("Are consent orders legally binding?",
   "Yes. Once approved, consent orders are enforceable court orders, the same as if a judge had made them after a hearing."),
  ("How long do consent orders take?",
   "Once lodged, processing times vary, but it's far faster than contested litigation. The slow part is reaching agreement — which mediation accelerates."),
  ("Can consent orders be changed later?",
   "Property orders are generally final. Parenting orders can be changed if circumstances significantly change and it's in the children's best interests, ideally by agreement through mediation.")],
 "Consent Orders",
 "Lock in your agreement — the <em>right way</em>.",
 "Book a consultation. We'll help you reach agreement through mediation and prepare the consent orders that make it legally binding.")

build(
 "online-divorce",
 "Online Divorce &amp; Mediation Australia | Separate From Anywhere",
 "Resolve your separation online with accredited mediators — parenting, property and finances by secure video. Online mediation across all of Australia, including regional areas.",
 "Online &amp; remote mediation",
 "Online Divorce Mediation — <em>wherever you are in Australia</em>.",
 "You don't need to be in the same room — or even the same state — to resolve a separation. Our secure online mediation handles parenting, property and financial matters by video, making expert dispute resolution available across all of Australia, including regional and remote areas.",
 "Online divorce mediation lets separating couples resolve parenting, property and financial matters by secure video conference with an accredited mediator. It offers the same structured process and binding outcomes as in-person mediation, available anywhere in Australia.",
 """
 <h2>How does online mediation work?</h2>
 <p>It mirrors in-person mediation, conducted over secure video. You can be in the same virtual room, or in separate virtual rooms with the mediator moving between you ('shuttle' mediation) — useful where there's high conflict or a safety concern. Documents are shared and signed electronically.</p>

 <h2>Is online mediation as effective as in person?</h2>
 <p>Yes — and often more convenient. Online mediation removes travel, reduces cost, and lets people participate from a place where they feel safe and comfortable. Outcomes are just as binding once formalised in <a href="/consent-orders/">consent orders</a> or a financial agreement.</p>

 <div class="callout">
   <h3>Built for regional and remote Australia</h3>
   <p>If you're far from a capital city, online mediation gives you access to the same nationally accredited mediators as anyone in Sydney or Melbourne — no long drives, no relocating.</p>
 </div>

 <h2>What can be resolved online?</h2>
 <ul>
   <li>Parenting arrangements and parenting plans</li>
   <li>Property settlements and superannuation splits</li>
   <li>Spousal maintenance and child support</li>
   <li>Section 60I certificates for parenting matters</li>
 </ul>
 <p><a href="/family-law-mediation/">See our full family law mediation service →</a></p>
 """,
 [("Is online mediation legally valid?",
   "Yes. Agreements reached through online mediation are just as valid as in-person ones and can be formalised into binding consent orders or financial agreements."),
  ("What technology do I need?",
   "A device with a camera and microphone, and an internet connection. We use secure video conferencing and guide you through the setup beforehand."),
  ("Can we do online mediation if there's conflict or safety concerns?",
   "Yes. Online 'shuttle' mediation keeps parties in separate virtual rooms with the mediator moving between them, which can feel safer and less confronting."),
  ("Is online mediation available in regional areas?",
   "Yes. Online mediation is available anywhere in Australia with an internet connection, giving regional and remote clients the same access as those in capital cities.")],
 "Online Divorce Mediation",
 "Resolve it from home — <em>anywhere in Australia</em>.",
 "Book a fixed-fee online consultation and resolve your separation by secure video, with the same accredited mediators and binding outcomes as in person.")

build(
 "workplace-mediation",
 "Workplace Mediation Australia | Resolve Disputes Fast",
 "Resolve workplace disputes through mediation — unfair dismissal, bullying, contracts and conflict. Faster and cheaper than the Fair Work Commission. Accredited mediators.",
 "Workplace &amp; employment disputes",
 "Workplace Mediation — <em>resolve disputes before they escalate</em>.",
 "Workplace conflict is costly, stressful and contagious. Mediation resolves disputes — from unfair dismissal claims to bullying complaints — early and confidentially, before they become expensive battles at the Fair Work Commission, so everyone can get back to work.",
 "Workplace mediation is a confidential process where a neutral mediator helps employers and employees resolve disputes — such as unfair dismissal, bullying, harassment or contract disagreements — without proceeding to the Fair Work Commission or court. It's faster, cheaper and helps preserve working relationships.",
 """
 <h2>What workplace disputes can be mediated?</h2>
 <ul>
   <li>Unfair dismissal and termination disputes</li>
   <li>Bullying, harassment and discrimination complaints</li>
   <li>Employment contract and entitlement disagreements</li>
   <li>Interpersonal conflict between colleagues or with management</li>
   <li>Restructure, redundancy and return-to-work disputes</li>
 </ul>

 <h2>Why mediate workplace disputes early?</h2>
 <p>Because unresolved conflict spreads — it damages morale, productivity and reputation, and can end up at the Fair Work Commission or in court. Early mediation contains the cost and keeps the matter private. For businesses, it's risk management; for employees, it's a fair hearing without a drawn-out fight.</p>

 <div class="callout">
   <h3>Good for business, good for people</h3>
   <p>Mediation delivers neutral, safe conversations where both sides are heard, structured discussion focused on solutions rather than blame, and practical agreements that get workplaces back on track.</p>
 </div>

 <h2>How does workplace mediation work?</h2>
 <p>A neutral mediator meets with the parties (together or separately), helps each side be heard, identifies the real issues, and guides everyone toward a practical agreement. It's confidential and 'without prejudice', so people can speak openly. Where useful, the outcome can be documented in a binding agreement.</p>
 """,
 [("Is workplace mediation confidential?",
   "Yes. Workplace mediation is conducted on a 'without prejudice' basis, meaning discussions generally can't be used later in legal proceedings, which lets both sides speak openly."),
  ("Can mediation prevent a Fair Work claim?",
   "Often, yes. Resolving a dispute early through mediation can prevent it escalating to the Fair Work Commission, saving both time and significant cost."),
  ("Who pays for workplace mediation?",
   "Arrangements vary. Employers often cover the cost as part of resolving a dispute, though it can be shared. You'll have fee clarity from the outset."),
  ("Is the outcome of workplace mediation binding?",
   "The mediation itself is voluntary, but any agreement reached can be documented and made binding, for example as a deed of settlement.")],
 "Workplace Mediation",
 "Resolve it early — <em>before it costs more</em>.",
 "Book a fixed-fee consultation to resolve a workplace dispute through confidential mediation, before it reaches the Fair Work Commission.")

print("\nService pages built.")
import subprocess
print(subprocess.run(["ls","/home/claude/mediations/site"],capture_output=True,text=True).stdout)
