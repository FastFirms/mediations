#!/usr/bin/env python3
"""Additional service + fee pages, keyword-first H1s, full schema."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build(slug,title,desc,eyebrow,h1,lede,ans,blocks,qa,crumb,cta_h,cta_p):
    schema=[org_schema(),breadcrumb_schema([("Home",""),(crumb,slug)]),
            service_schema(crumb,desc,slug),faq_schema(qa)]
    d=head(title,desc,slug,extra_schema=schema)+nav()
    d+=f"""<main id="main">
{crumb_html([("Home",""),(crumb,None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
<h1>{h1}</h1><p class="lede">{lede}</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {ans}</p></div></div>
<article class="body"><div class="wrap-narrow reveal">{blocks}</div></article>"""
    d+=faq_html(qa,heading=f"{crumb} FAQs")+cta_band(cta_h,cta_p)+"</main>"+page_end()
    p=os.path.join(OUT,slug); os.makedirs(p,exist_ok=True)
    open(os.path.join(p,"index.html"),"w").write(d)
    import re; return slug,len(re.sub(r'<[^>]+>',' ',d).split())

# ---- ESTATE DISPUTES ----
build("estate-dispute-mediation",
 "Estate Dispute Mediation | Contested Wills Without Court",
 "Resolve contested wills and inheritance disputes through mediation. Faster, private and cheaper than litigation. Nationally accredited mediators.",
 "Estate &amp; inheritance disputes",
 "Estate Dispute Mediation",
 "Few disputes are as painful as a family fight over a will or estate. Mediation offers a private, dignified way to resolve inheritance disputes — preserving family relationships and a fraction of the cost of contesting an estate in court.",
 "Estate dispute mediation helps families resolve contested wills, inheritance claims and executor disputes with a neutral mediator, without going to court. It is private, far cheaper than litigation, and helps preserve family relationships at an already difficult time.",
 """
 <h2>What estate disputes can be mediated?</h2>
 <ul>
   <li>Contested wills and challenges to a will's validity</li>
   <li>Family provision claims (where someone feels inadequately provided for)</li>
   <li>Disputes between executors and beneficiaries</li>
   <li>Disagreements over the distribution or valuation of estate assets</li>
   <li>Conflicts over the administration of a deceased estate</li>
 </ul>
 <h2>Why mediate an estate dispute instead of litigating?</h2>
 <p>Because contesting an estate in court is slow, public, and expensive — and the legal costs often come out of the very estate being fought over, shrinking what's left for everyone. Worse, litigation tends to permanently fracture families already grieving a loss. Mediation resolves the dispute privately, usually in a single session, and gives the family a chance to preserve relationships that a courtroom would destroy.</p>
 <div class="callout"><h3>Many courts now expect mediation first</h3>
 <p>In estate and family provision matters, courts across Australia frequently require or strongly encourage mediation before a contested hearing. Resolving it early saves the estate — and the family — enormous cost and strain.</p></div>
 <h2>How estate mediation works</h2>
 <p>A neutral, accredited mediator brings the parties together — in person or online, jointly or in separate rooms — to work through the issues and reach agreement. Where a resolution is reached, it can be formalised into a binding settlement. Many of our mediators are also experienced lawyers, so the legal realities of estate law are understood from the outset. <a href="/how-mediation-works/">See how mediation works →</a></p>
 """,
 [("Can a contested will be resolved without going to court?",
   "Yes. Most contested wills and family provision claims can be resolved through mediation, which is private, faster and far cheaper than litigation. Courts frequently require mediation before a contested hearing."),
  ("Who pays for estate dispute mediation?",
   "Costs are usually shared between the parties or met from the estate, and are a small fraction of contested litigation, where legal fees can significantly reduce the estate's value."),
  ("What is a family provision claim?",
   "It's a claim by an eligible person (such as a spouse, child or dependant) who believes they were not adequately provided for in a will. These claims are well suited to mediation."),
  ("Can mediation preserve family relationships?",
   "That's one of its greatest strengths. Unlike adversarial litigation, mediation is collaborative and private, giving grieving families the best chance of resolving the dispute without permanent damage.")],
 "Estate Dispute Mediation",
 "Resolve it privately — <em>and keep the family together</em>.",
 "Book a free initial consultation to resolve a contested will or estate dispute through dignified, private mediation.")

# ---- COLLABORATIVE FAMILY LAWYERS ----
build("collaborative-family-lawyers",
 "Collaborative Family Lawyers | Resolve Without Court",
 "Collaborative family lawyers resolve separation respectfully, out of court. A team-based approach focused on agreement, not litigation.",
 "Collaborative practice",
 "Collaborative Family Lawyers",
 "Collaborative law is a structured, out-of-court approach where both parties and their lawyers commit in writing to reaching agreement without litigation. It's a respectful, team-based path through separation that works hand in hand with mediation.",
 "Collaborative family law is a process where separating partners and their lawyers sign an agreement to resolve matters without going to court, working together in a series of meetings. It prioritises respectful, durable agreements and pairs naturally with mediation.",
 """
 <h2>How does collaborative family law work?</h2>
 <p>Each person has their own collaboratively-trained lawyer, and everyone signs a participation agreement committing to resolve the matter without court. You then work through the issues in a series of round-table meetings, often with neutral experts (like financial specialists) brought in as needed. If the process breaks down and litigation begins, the collaborative lawyers step aside — which gives everyone a powerful incentive to reach agreement.</p>
 <h2>Collaborative law vs mediation — what's the difference?</h2>
 <p>In <a href="/family-law-mediation/">mediation</a>, a single neutral mediator guides you to your own agreement. In collaborative law, each party has their own lawyer advocating for them within a no-court framework. Many separations use both: mediation to resolve the core issues, with collaborative lawyers providing advice alongside. We help you choose the right mix.</p>
 <div class="callout"><h3>Best of both worlds</h3>
 <p>Collaborative practice combines legal advice with a commitment to staying out of court — ideal for those who want their own lawyer in the room but don't want a litigation war.</p></div>
 <h2>Is collaborative law right for you?</h2>
 <p>It suits separating couples who want a respectful, dignified process, who value their own legal advice, and who are committed to reaching agreement rather than fighting. <a href="/property-settlement-mediation/">It works well for property settlements</a> and <a href="/parenting-plan-mediation/">parenting arrangements</a> alike.</p>
 """,
 [("What is collaborative family law?",
   "It's a process where separating partners and their own lawyers sign an agreement to resolve matters without court, working through issues in round-table meetings. If it fails and litigation starts, the collaborative lawyers must withdraw."),
  ("How is it different from mediation?",
   "Mediation uses one neutral mediator; collaborative law gives each party their own lawyer within a no-court framework. Many separations use both approaches together."),
  ("What happens if collaborative law doesn't work?",
   "If the process breaks down and a party chooses to litigate, the collaborative lawyers must step aside and new lawyers take over — a strong incentive for everyone to reach agreement."),
  ("Is collaborative law cheaper than court?",
   "Generally yes. While each party has their own lawyer, the focus on agreement rather than litigation usually makes it far less costly than a contested court case.")],
 "Collaborative Family Lawyers",
 "Resolve separation <em>respectfully</em>.",
 "Book a consultation to find out whether collaborative family law, mediation, or a combination is the right path for your separation.")

# ---- FAMILY LAW ARBITRATORS ----
build("family-law-arbitration",
 "Family Law Arbitration | Binding Decisions Without Court",
 "Family law arbitration: a binding decision on property and finances, faster and more privately than court. Nationally accredited arbitrators.",
 "Arbitration",
 "Family Law Arbitration",
 "When you need a definitive decision but want to avoid the cost and delay of court, arbitration is the answer. A qualified arbitrator hears both sides and makes a binding determination on property and financial matters — like a private judge, but faster.",
 "Family law arbitration is a process where a qualified arbitrator hears a property or financial dispute and makes a legally binding decision, privately and far faster than court. It suits parties who can't reach agreement through mediation but want to avoid lengthy litigation.",
 """
 <h2>How is arbitration different from mediation?</h2>
 <p>In <a href="/family-law-mediation/">mediation</a>, you and the other party reach your own agreement and the mediator decides nothing. In arbitration, you present your case and the arbitrator makes a binding decision for you — much like a judge, but in a private, streamlined process you control the timing of. Arbitration is ideal when mediation hasn't fully resolved a financial matter but you still want to avoid court.</p>
 <h2>What can be arbitrated?</h2>
 <ul>
   <li>Property settlements and the division of assets</li>
   <li>Superannuation splitting</li>
   <li>Spousal maintenance and financial support</li>
   <li>Financial aspects of de facto separations</li>
 </ul>
 <p>Note that arbitration in Australia is used for property and financial matters — parenting disputes are not arbitrated.</p>
 <div class="callout"><h3>Faster and private</h3>
 <p>An arbitrated decision can be reached in a fraction of the time a contested court hearing takes, on a timetable you help set, and entirely out of the public eye.</p></div>
 <h2>Is an arbitration decision binding?</h2>
 <p>Yes. An arbitral award on financial matters can be registered with the court and is then enforceable like a court order. It brings genuine finality. Often the best path is mediation first, with arbitration reserved for any issues that remain. <a href="/how-mediation-works/">Learn how the process works →</a></p>
 """,
 [("What is family law arbitration?",
   "It's a process where a qualified arbitrator hears a property or financial dispute and makes a legally binding decision, privately and faster than court. It's used for financial matters, not parenting disputes."),
  ("Is an arbitrator's decision legally binding?",
   "Yes. An arbitral award on financial matters can be registered with the court and enforced like a court order, bringing genuine finality to the dispute."),
  ("Can parenting matters be arbitrated?",
   "No. In Australia, arbitration is available for property and financial matters only. Parenting disputes are resolved through mediation or, if necessary, the court."),
  ("Should I try mediation or arbitration first?",
   "Most people start with mediation, since it lets you keep control of the outcome. Arbitration is ideal for resolving any financial issues that remain unresolved, without going to court.")],
 "Family Law Arbitration",
 "Get a binding decision — <em>without the wait</em>.",
 "Book a consultation to find out whether arbitration can give you the finality you need, faster and more privately than court.")

# ---- DIVORCE COUNSELLING ----
build("divorce-counselling",
 "Divorce Counselling Australia | Support Through Separation",
 "Divorce and separation counselling to help you cope with the emotional side of separation. Compassionate support alongside practical mediation.",
 "Emotional support",
 "Divorce Counselling",
 "Separation isn't only a legal process — it's one of life's most stressful events. Divorce counselling provides emotional support to help you and your children navigate the transition, working alongside mediation so both the practical and personal sides are cared for.",
 "Divorce counselling provides emotional and psychological support to individuals and families going through separation. It helps people process the emotional impact, communicate better, and make clearer decisions — complementing the practical work of mediation.",
 """
 <h2>Why consider counselling during separation?</h2>
 <p>Because the emotional weight of separation affects everything — including your ability to negotiate calmly and make sound decisions about your future. Counselling gives you space to process grief, anger and anxiety, so you can approach mediation and the practical decisions ahead with a clearer head. It's especially valuable where children are involved.</p>
 <h2>How counselling supports the mediation process</h2>
 <p>When people feel heard and emotionally steadier, mediation works better. Counselling and <a href="/family-law-mediation/">mediation</a> are complementary: counselling tends to the emotional recovery, while mediation resolves the practical and legal questions. Together they help you move forward intact.</p>
 <div class="callout"><h3>Supporting children through separation</h3>
 <p>Children feel separation deeply. Counselling can help them understand and adjust to the changes, and help parents support them — which is exactly what child-focused <a href="/parenting-plan-mediation/">parenting arrangements</a> are designed to protect.</p></div>
 <h2>A note on safety and crisis support</h2>
 <p>If you or someone in your family is in crisis or immediate danger, please contact emergency services or a support line right away. Counselling is for emotional support through separation; it is not a substitute for urgent mental health or safety assistance.</p>
 """,
 [("Is divorce counselling the same as mediation?",
   "No. Counselling supports your emotional wellbeing through separation, while mediation resolves practical and legal matters. They complement each other — many people benefit from both."),
  ("Can counselling help my children cope with separation?",
   "Yes. Counselling can help children understand and adjust to the changes, and help parents support them through the transition in age-appropriate ways."),
  ("Does counselling help with the mediation process?",
   "Often, yes. Feeling emotionally steadier helps people communicate and negotiate more clearly, which can make mediation more productive."),
  ("When should I seek counselling during separation?",
   "Whenever you feel the emotional weight is affecting your wellbeing or decision-making. There's no wrong time — and earlier support often makes the whole process easier.")],
 "Divorce Counselling",
 "Care for the <em>whole</em> of separation, not just the paperwork.",
 "Get in touch to learn how counselling and mediation together can help you and your family move forward.")

# ---- COMMERCIAL MEDIATION ----
build("commercial-mediation",
 "Commercial Mediation | Business Disputes Australia",
 "Resolve commercial and business disputes through mediation. Faster, private and cheaper than litigation. Nationally accredited mediators.",
 "Business &amp; commercial disputes",
 "Commercial Mediation",
 "Business disputes are expensive — in legal fees, management distraction, and damaged relationships. Commercial mediation resolves partnership conflicts, contract disagreements, franchise disputes and more in a single session, privately and without litigation.",
 "Commercial mediation helps Australian businesses resolve disputes — including partnership and shareholder conflicts, contract disagreements, franchise disputes and business exits — quickly, privately and at a fraction of the cost of commercial litigation.",
 """
 <h2>What commercial disputes can be mediated?</h2>
 <p>Mediation is available for the full range of business disputes. The most common matters we resolve include:</p>
 <ul>
   <li><strong>Partnership and co-founder disputes</strong> — disagreements over direction, profit sharing, decision-making authority, or a partner's exit</li>
   <li><strong>Director and shareholder conflicts</strong> — deadlock, minority shareholder oppression, dividend disputes, and director removal</li>
   <li><strong>Contractor and subcontractor disagreements</strong> — scope creep, payment disputes, defective work and contract termination</li>
   <li><strong>Contract disputes</strong> — breach of contract, interpretation disputes, enforcement, variation and termination claims</li>
   <li><strong>Insurance claim disputes</strong> — where an insurer and policyholder disagree on entitlement, scope or quantum</li>
   <li><strong>Franchise disputes</strong> — franchisee and franchisor conflicts under the <a href="https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct" target="_blank" rel="noopener">Franchising Code of Conduct</a>, which requires mediation before many disputes can proceed to court</li>
   <li><strong>Business exits and buyouts</strong> — valuation disputes, earn-out disagreements, and the terms of a departing partner's payout</li>
 </ul>

 <h2>Why mediate commercial disputes instead of litigating?</h2>
 <p>Commercial litigation in Australia is expensive, slow and public. A disputed contract matter in the Federal Court or a Supreme Court can take two to four years and cost each party $100,000–$500,000 or more in legal fees — often exceeding the value of the dispute itself. The process is also entirely public, which means confidential business information, pricing, and relationship details become part of the court record.</p>
 <p>Mediation resolves the same disputes in a single day, privately, at a fixed and shared cost. The business keeps operating. The relationship — often between people who will continue to deal with each other — has a chance of surviving.</p>

 <figure class="tbl"><table><caption>Commercial mediation vs commercial litigation</caption>
 <thead><tr><th></th><th>Mediation</th><th>Commercial litigation</th></tr></thead>
 <tbody>
 <tr><td>Time to resolution</td><td>1 day</td><td>2–4 years</td></tr>
 <tr><td>Typical cost per party</td><td>$1,500–$4,000</td><td>$100,000–$500,000+</td></tr>
 <tr><td>Confidential</td><td>Yes — protected by law</td><td>No — public record</td></tr>
 <tr><td>Who decides the outcome</td><td>The parties</td><td>A judge</td></tr>
 <tr><td>Business relationship preserved</td><td>Possible — collaborative process</td><td>Rarely — adversarial process</td></tr>
 <tr><td>Management distraction</td><td>One session</td><td>Years of discovery, affidavits, hearings</td></tr>
 </tbody></table></figure>

 <h2>Shareholder and director disputes — a closer look</h2>
 <p>Disputes between co-directors or shareholders are among the most damaging business disputes because the parties are bound together — you can't simply walk away. Common triggers include deadlock on a major decision, one director's conduct damaging the company, disagreement over whether to sell the business, or a minority shareholder who feels oppressed by the majority.</p>
 <p>Mediation creates the space for an honest commercial conversation about what each party actually wants — which is often quite different from the legal position they've taken. Most director disputes resolve around either a restructured operating agreement, a buyout at an agreed valuation, or a structured exit. A mediator helps the parties get to that conversation without the expense and destruction of a winding-up application or oppression claim.</p>

 <h2>Franchise disputes — mediation is often required first</h2>
 <p>The <a href="https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct" target="_blank" rel="noopener">Franchising Code of Conduct</a> (mandatory under Australian Consumer Law) requires franchisors and franchisees to attempt mediation before most disputes can proceed to litigation or arbitration. Our mediators are experienced in the franchise context — understanding the power imbalances, disclosure obligations, and specific Code requirements that shape these disputes. Early mediation resolves most franchise conflicts before they become entrenched.</p>

 <div class="callout">
   <h3>Commercial mediation agreements are binding</h3>
   <p>Any settlement reached in commercial mediation can be documented as a deed of settlement — a legally binding contract enforceable in court. You leave the session with a signed agreement, not a promise. The confidentiality of what was said in mediation is protected under Australian law.</p>
 </div>

 <h2>Business exits and valuation disputes</h2>
 <p>Business exits generate disputes even between people who started as friends and partners. The common flashpoints: how the business should be valued, what goodwill is worth, the terms of earn-out payments, non-compete obligations, and who keeps key clients or staff. These disputes are often more emotional than technical — the numbers are the battleground, but the real issue is fairness and recognition.</p>
 <p>Mediation works well here because a skilled mediator separates the commercial questions (which a valuation expert can inform) from the relational ones (which negotiation must resolve). We bring both to the table. <a href="/our-fee-structure/">See our fee structure →</a></p>
 """,
 [("What commercial disputes can be resolved through mediation?",
   "Partnership conflicts, shareholder and director disputes, contract disagreements, contractor claims, insurance disputes, franchise conflicts under the Franchising Code, and business exits can all be mediated."),
  ("Is a mediated commercial settlement legally binding?",
   "Yes. Any agreement reached in commercial mediation can be documented as a deed of settlement — a legally binding contract enforceable in court."),
  ("Does the Franchising Code of Conduct require mediation?",
   "Yes. The Franchising Code of Conduct (mandatory under Australian Consumer Law) requires parties to attempt mediation before most franchise disputes can proceed to litigation or arbitration."),
  ("How long does commercial mediation take?",
   "Most commercial disputes resolve in a single half-day or full-day session. Complex multi-party matters may need two sessions."),
  ("How much does commercial mediation cost?",
   "Our commercial mediation is fixed-fee, typically $3,000–$4,500 for the full session, shared equally between the parties.")],
 "Commercial Mediation",
 "Resolve the dispute — and keep the business moving.",
 "Book a free consultation to discuss your commercial dispute. We respond within one business day.")

# ---- REAL ESTATE & CONSTRUCTION MEDIATION ----
build("real-estate-mediation",
 "Real Estate & Construction Mediation Australia",
 "Resolve property and construction disputes through mediation. Lease conflicts, building disputes, easement claims and development disagreements resolved privately.",
 "Property &amp; construction disputes",
 "Real Estate & Construction Mediation",
 "Property and construction disputes can freeze transactions, stall developments, and trap parties in costly litigation for years. Mediation resolves lease conflicts, building disputes, boundary disagreements and development stalemates in a single session — privately, without court.",
 "Real estate and construction mediation resolves property transaction disputes, commercial and retail lease conflicts, easement and boundary disagreements, development disputes and building contract claims — faster, more privately and far more cheaply than litigation.",
 """
 <h2>What property and construction disputes can be mediated?</h2>
 <ul>
   <li><strong>Property transaction disputes</strong> — disputes arising from the sale or purchase of property, including misrepresentation, failure to complete, and deposit disagreements</li>
   <li><strong>Commercial lease disputes</strong> — rent reviews, lease renewals, make-good obligations, outgoings, and landlord/tenant conflicts</li>
   <li><strong>Retail shop lease disputes</strong> — disputes governed by state retail leases legislation, where mediation is often a mandatory step before litigation</li>
   <li><strong>Easement and right-of-way disputes</strong> — access, maintenance obligations, and claims that easements are being blocked or exceeded</li>
   <li><strong>Boundary disputes</strong> — encroachments, fencing disputes, and disputes about survey results</li>
   <li><strong>Development disputes</strong> — between developers, landowners, neighbours, and councils, including objections, conditions, and development agreement terms</li>
   <li><strong>Building contract conflicts</strong> — defective work, variations, payment claims, time delays and contract termination under residential and commercial building contracts</li>
   <li><strong>Strata and owners corporation disputes</strong> — between lot owners, between owners and the strata manager, and disputes about by-laws and levies</li>
 </ul>

 <h2>Retail shop leases — mediation is often mandatory</h2>
 <p>Each state and territory has its own retail leases legislation, and most require landlords and tenants to attempt mediation before a dispute can proceed to tribunal or court. In NSW, the <a href="https://www.smallbusiness.nsw.gov.au/retail-leases" target="_blank" rel="noopener">Retail Leases Act 1994</a> provides a mediation pathway through the NSW Small Business Commissioner. In Victoria, the <a href="https://www.vsbc.vic.gov.au/" target="_blank" rel="noopener">Victorian Small Business Commission</a> administers retail lease disputes. Our mediators are familiar with the procedural requirements across all major jurisdictions.</p>

 <h2>Building and construction disputes — why early mediation matters</h2>
 <p>Building disputes are notoriously expensive to litigate because they require expert evidence — structural engineers, quantity surveyors, building consultants — that accumulates cost quickly. A disputed defects claim worth $80,000 can cost both parties that amount again in legal and expert fees before it gets to hearing.</p>
 <p>Early mediation resolves most building disputes in a single session. The mediator doesn't determine who is right on the technical question; they help the parties find a practical resolution both can accept. Most building contract disputes settle around an agreed scope of remedial works, a negotiated deduction from the contract price, or a combination of both.</p>

 <figure class="tbl"><table><caption>Common building disputes and typical resolution in mediation</caption>
 <thead><tr><th>Dispute type</th><th>Common resolution</th></tr></thead>
 <tbody>
 <tr><td>Defective work</td><td>Agreed scope of rectification, or a price reduction reflecting the defects</td></tr>
 <tr><td>Variation claim</td><td>Agreed value for authorised variations; disputed ones written off or reduced</td></tr>
 <tr><td>Delay / liquidated damages</td><td>Agreed extension of time, partial waiver, or structured payment plan</td></tr>
 <tr><td>Incomplete works</td><td>Agreed completion timeline or buyout of incomplete scope</td></tr>
 <tr><td>Payment dispute</td><td>Undisputed amounts paid; disputed claims mediated to an agreed figure</td></tr>
 </tbody></table></figure>

 <div class="callout">
   <h3>Strata and neighbours — the value of an early conversation</h3>
   <p>Neighbour and strata disputes that go to tribunal often leave parties living next door to each other in permanent hostility. Mediation achieves a practical resolution — fencing, noise, access, by-law compliance — before the relationship is permanently poisoned. It's usually over in a single afternoon.</p>
 </div>

 <h2>Can mediation be used during active court or tribunal proceedings?</h2>
 <p>Yes. Courts and tribunals regularly refer property and construction disputes to mediation — and parties can choose private mediation at any stage of proceedings, including after claims have been filed. A mediated resolution at any stage saves the remaining cost of the litigation and gives the parties control over the outcome. <a href="/commercial-mediation/">See commercial mediation →</a> or <a href="/estate-dispute-mediation/">estate dispute mediation →</a></p>
 """,
 [("What property disputes can be resolved through mediation?",
   "Property transaction disputes, commercial and retail lease conflicts, easement and boundary claims, development disputes, building contract defects and payment claims, and strata disputes can all be mediated."),
  ("Is mediation compulsory for retail shop lease disputes?",
   "In most states and territories, yes — retail leases legislation requires mediation before a dispute can proceed to tribunal or court. We can advise on the correct pathway for your jurisdiction."),
  ("How much does real estate mediation cost?",
   "Property and construction mediation is fixed-fee — typically $3,000–$4,500 for the session, shared equally. Far less than a disputed building matter litigated to hearing."),
  ("Can mediation resolve a dispute already in NCAT or court?",
   "Yes. Mediation can be used at any stage of proceedings. Courts regularly refer property matters to mediation, and private mediation can resolve the dispute before the next hearing."),
  ("What happens if we reach agreement in mediation?",
   "The settlement is documented as a deed of settlement or consent orders — legally binding and enforceable. For court proceedings, the terms can be filed to formally resolve the case.")],
 "Real Estate & Construction Mediation",
 "Resolve your property dispute — without the litigation.",
 "Book a free consultation to discuss your property or construction dispute.")

# ---- ELDER MEDIATION ----
build("elder-mediation",
 "Elder Mediation | Family Care Arrangements Australia",
 "Resolve family decisions about ageing parents through mediation. Care arrangements, living situations and financial agreements — decided together, before they fracture the family.",
 "Elder &amp; family care",
 "Elder Mediation",
 "Decisions about where an ageing parent lives, who provides care, how costs are shared, and questions about granny flats or early inheritance can quietly divide siblings at the hardest time. Elder mediation brings the family together to make these decisions respectfully — before they fracture.",
 "Elder mediation helps families resolve care arrangements, living situations and financial agreements for ageing parents — including granny flat arrangements, early inheritance questions and disputes about who bears the cost of care — without family conflict or legal proceedings.",
 """
 <h2>What is elder mediation?</h2>
 <p>Elder mediation is a structured conversation, facilitated by a neutral mediator, that helps families make decisions about the care, living arrangements and financial affairs of an ageing parent or family member. Unlike family law mediation — which resolves the aftermath of a breakdown — elder mediation is most effective <em>before</em> the family fractures, when the decisions are still genuinely open and the relationships are still intact.</p>
 <p>These conversations are hard to have without structure. Each sibling has a different relationship with the parent, different capacity to provide care, different financial circumstances, and different views on what the right thing to do looks like. A mediator creates a safe, structured environment where all of those differences can be heard and addressed — without a family dinner turning into a war.</p>

 <h2>What decisions can elder mediation help with?</h2>
 <ul>
   <li><strong>Care arrangements</strong> — who provides care, how responsibilities are shared, what professional care is appropriate, and how to manage a parent's transition from independence to supported living</li>
   <li><strong>Living situations</strong> — whether a parent moves in with a child, moves to residential aged care, downsizes, or stays in the family home with support</li>
   <li><strong>Granny flat arrangements</strong> — the financial and practical terms of a parent moving into a child's property, including the Centrelink and tax implications that need legal advice alongside the family conversation</li>
   <li><strong>Cost sharing</strong> — how the costs of care (in-home support, residential aged care, medical expenses) are shared between siblings, particularly where financial circumstances differ</li>
   <li><strong>Early inheritance and financial gifts</strong> — whether and how assets are transferred to children now, and how to do so in a way the whole family accepts as fair</li>
   <li><strong>Enduring power of attorney and guardianship</strong> — who holds these, how decisions are made, and how disagreements between attorneys are resolved</li>
   <li><strong>Existing family conflict</strong> — where past grievances are making it impossible to make decisions together, and a neutral facilitator is needed to move forward</li>
 </ul>

 <h2>Why these decisions need structure</h2>
 <p>Unstructured decision-making under stress creates resentment, suspicion and misunderstanding that escalates. One sibling who provides the most care quietly accumulates grievances. Another who contributes financially doesn't understand why the carer feels undervalued. A parent who wants input into their own future feels sidelined by children who think they're helping.</p>
 <p>Elder mediation creates the structure that prevents this. It brings everyone to the table with a clear agenda, a neutral facilitator, and a commitment to reach decisions the whole family can support — with the parent's voice at the centre.</p>

 <figure class="tbl"><table><caption>Common elder mediation scenarios and what resolution looks like</caption>
 <thead><tr><th>Scenario</th><th>What mediation produces</th></tr></thead>
 <tbody>
 <tr><td>Parent needs care — siblings disagree on the right arrangement</td><td>A care plan all siblings endorse, with clear roles, review points and a shared cost schedule</td></tr>
 <tr><td>Parent wants to move in with one child — others have concerns</td><td>A granny flat agreement (for legal advice) covering terms, financial contribution, and exit provisions</td></tr>
 <tr><td>One sibling is providing care and feels unsupported</td><td>Recognition of the carer's contribution, rebalanced responsibilities, and a financial arrangement that reflects the unequal input</td></tr>
 <tr><td>Parent wants to give money to one child — others concerned about fairness</td><td>A family agreement on the gift, documented in a way that reduces estate conflict later</td></tr>
 <tr><td>Siblings cannot agree on who holds power of attorney</td><td>A co-attorney arrangement or a decision-making protocol that gives each sibling confidence</td></tr>
 </tbody></table></figure>

 <div class="callout">
   <h3>The parent's voice matters most</h3>
   <p>Elder mediation keeps the older person's wishes at the centre of every decision. Where a parent has capacity, they participate directly. Where capacity is limited, the mediator ensures their known wishes and values are heard and respected. These are decisions about someone's life — they deserve more than a family argument.</p>
 </div>

 <h2>When is the right time for elder mediation?</h2>
 <p>The best time is before a crisis forces a rushed decision — a fall, a hospitalisation, a diagnosis that suddenly makes independent living impossible. At that point, the family is under maximum stress and decisions are made reactively, often poorly.</p>
 <p>But mediation is also effective after conflict has begun — after siblings have stopped speaking, after a disputed care decision has fractured the family, or after a parent's estate has become the subject of competing claims. It is never too late to have a structured, facilitated conversation.</p>

 <h2>Does elder mediation involve lawyers?</h2>
 <p>The mediator is not a lawyer and cannot provide legal advice. For matters involving granny flat arrangements, gifts of property, or powers of attorney, we strongly recommend each family member take independent legal advice before signing any formal agreement. The mediator's role is to reach agreed terms; the lawyers make those terms binding and legally sound. <a href="/family-law-mediation/">See family law mediation →</a> or <a href="/estate-dispute-mediation/">estate dispute mediation →</a></p>
 """,
 [("What is elder mediation?",
   "Elder mediation is a facilitated family conversation that helps families make decisions about the care, living arrangements and financial affairs of an ageing parent — before or after family conflict has begun."),
  ("What decisions can elder mediation help with?",
   "Care arrangements, living situations (including granny flats), cost sharing between siblings, early inheritance, enduring power of attorney arrangements, and family conflict about how to support an ageing parent."),
  ("Does the parent participate in elder mediation?",
   "Yes, where they have capacity — their wishes are at the centre of every decision. Where capacity is limited, the mediator ensures their known wishes are heard and respected throughout the process."),
  ("When is the right time for elder mediation?",
   "Before a crisis if possible — while decisions are still open and the family is still communicating. But mediation is also effective after conflict has begun, even after siblings have stopped speaking."),
  ("Do we need lawyers for elder mediation?",
   "The mediator is not a lawyer. For granny flat arrangements, property gifts or powers of attorney, we recommend independent legal advice before formalising any agreement.")],
 "Elder Mediation",
 "Bring the family together — before the decisions pull it apart.",
 "Book a free consultation to discuss how elder mediation can help your family.")

# ---- FEE STRUCTURE ----
build("our-fee-structure",
 "Mediation Fees & Pricing | Mediations Australia",
 "Transparent, fixed-fee mediation pricing for family law, property, workplace and commercial disputes. Free initial consultation. No surprise bills.",
 "Pricing &amp; fees",
 "Our Fee Structure",
 "We believe you should know what things cost before you commit. Every matter starts with a free initial consultation, and all pricing is agreed upfront — no open-ended hourly billing, no surprises.",
 "Mediations Australia charges transparent, fixed fees for mediation. The initial consultation is free. Fees are current as at 2026 and are typically shared equally between the parties.",
 """
<style>
.fee-table{width:100%;border-collapse:collapse;margin:28px 0 36px}
.fee-table th{text-align:left;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft);padding:0 16px 10px 0;border-bottom:2px solid var(--sage-deep)}
.fee-table td{padding:16px 16px 16px 0;border-bottom:1px solid var(--line);vertical-align:top;font-size:.97rem;color:var(--ink-soft)}
.fee-table td:first-child{color:var(--ink)}
.fee-table td:last-child{font-weight:700;color:var(--ink);white-space:nowrap;text-align:right;padding-right:0}
.fee-table tr:last-child td{border-bottom:none}
.fee-section-head{font-family:var(--serif);font-size:1.35rem;margin:44px 0 4px;color:var(--ink)}
.fee-note{font-size:.9rem;color:var(--ink-soft);margin:4px 0 0;max-width:64ch}
</style>

<p style="font-size:1.05rem;color:var(--ink-soft);max-width:66ch;margin-bottom:8px">All fees are <strong>+GST</strong> and current as at 2026. Mediation fees are commonly split equally between the parties — your share is typically <strong>half the figure shown</strong>. The initial consultation is always free.</p>

<h2 class="fee-section-head">Initial Consultation</h2>
<table class="fee-table">
  <thead><tr><th style="width:30%">Service</th><th>What's included</th><th>Fee</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Initial Consultation</strong></td>
      <td>We discuss your dispute, assess whether mediation is suitable, and give you an honest view of your options — with no obligation to proceed.</td>
      <td>Free</td>
    </tr>
  </tbody>
</table>

<h2 class="fee-section-head">Family Law &amp; Separation</h2>
<p class="fee-note">Parenting arrangements, property settlement, de facto disputes, separation agreements.</p>
<table class="fee-table">
  <thead><tr><th style="width:30%">Service</th><th>What's included</th><th>Fee</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Half-Day Mediation</strong><br><small style="color:var(--ink-soft)">Up to 4 hours</small></td>
      <td>Pre-mediation intake sessions, preparation, mediation session (9:30am–1:30pm or 1:00pm–5:00pm). Overtime at $400/hr.</td>
      <td>$3,000</td>
    </tr>
    <tr>
      <td><strong>Full-Day Mediation</strong><br><small style="color:var(--ink-soft)">Up to 8 hours</small></td>
      <td>Pre-mediation intake sessions, preparation, mediation session (9:30am–5:00pm). Overtime after 5:00pm at $400/hr.</td>
      <td>$4,500</td>
    </tr>
    <tr>
      <td><strong>Invitation to Mediate</strong></td>
      <td>Formal written invitation to the other party to participate in mediation.</td>
      <td>$400</td>
    </tr>
  </tbody>
</table>

<h2 class="fee-section-head">Property &amp; Estate Disputes</h2>
<p class="fee-note">Property settlements, estate and inheritance disputes, trust disputes, co-ownership disagreements.</p>
<table class="fee-table">
  <thead><tr><th style="width:30%">Service</th><th>What's included</th><th>Fee</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Half-Day Mediation</strong><br><small style="color:var(--ink-soft)">Up to 4 hours</small></td>
      <td>Pre-mediation intake, preparation, mediation session. Overtime at $400/hr.</td>
      <td>$3,000</td>
    </tr>
    <tr>
      <td><strong>Full-Day Mediation</strong><br><small style="color:var(--ink-soft)">Up to 8 hours</small></td>
      <td>Pre-mediation intake, preparation, full-day mediation session. Overtime after 5:00pm at $400/hr.</td>
      <td>$4,500</td>
    </tr>
  </tbody>
</table>

<h2 class="fee-section-head">Workplace &amp; Commercial Disputes</h2>
<p class="fee-note">Workplace conflicts, employment disputes, commercial disagreements, shareholder and business partner disputes.</p>
<table class="fee-table">
  <thead><tr><th style="width:30%">Service</th><th>What's included</th><th>Fee</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Half-Day Mediation</strong><br><small style="color:var(--ink-soft)">Up to 4 hours</small></td>
      <td>Pre-mediation intake, preparation, mediation session. Overtime at $400/hr.</td>
      <td>$3,000</td>
    </tr>
    <tr>
      <td><strong>Full-Day Mediation</strong><br><small style="color:var(--ink-soft)">Up to 8 hours</small></td>
      <td>Pre-mediation intake, preparation, full-day mediation session. Overtime after 5:00pm at $400/hr.</td>
      <td>$4,500</td>
    </tr>
    <tr>
      <td><strong>Multi-Party / Complex</strong></td>
      <td>Three or more parties, or commercially complex matters. Quoted individually after initial consultation.</td>
      <td>POA</td>
    </tr>
  </tbody>
</table>

<h2 class="fee-section-head">Online Mediation</h2>
<p class="fee-note">Same service as in-person, conducted by secure video. Available anywhere in Australia.</p>
<table class="fee-table">
  <thead><tr><th style="width:30%">Service</th><th>What's included</th><th>Fee</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Online Half-Day</strong></td>
      <td>Pre-mediation intake, preparation, secure video session up to 4 hours. Overtime at $400/hr.</td>
      <td>$3,000</td>
    </tr>
    <tr>
      <td><strong>Online Full-Day</strong></td>
      <td>Pre-mediation intake, preparation, secure video session up to 8 hours. Overtime at $400/hr.</td>
      <td>$4,500</td>
    </tr>
  </tbody>
</table>

<h2 class="fee-section-head">Additional Items</h2>
<table class="fee-table">
  <thead><tr><th style="width:30%">Item</th><th>Notes</th><th>Fee</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Room Hire</strong></td>
      <td>A suitable venue is required for all in-person sessions. We can arrange a room or you may use your own. Prices range from $200 to $400 depending on location.</td>
      <td>$200–$400</td>
    </tr>
    <tr>
      <td><strong>Overtime</strong></td>
      <td>Per hour beyond the scheduled session end time, applicable to all session types.</td>
      <td>$400/hr</td>
    </tr>
    <tr>
      <td><strong>Interstate Travel</strong></td>
      <td>Where a mediator travels to a regional or interstate venue outside our four office cities.</td>
      <td>At cost</td>
    </tr>
  </tbody>
</table>

<div class="callout">
  <h3>Fees are usually shared — your share is roughly half</h3>
  <p>In most mediations the fee is split equally between the two parties. A full-day mediation at $4,500 +GST typically costs each person around $2,475 all up — compared with $30,000–$150,000+ per side in contested litigation. We confirm the cost-sharing arrangement at your free initial consultation.</p>
</div>

<h2>How does this compare with going to court?</h2>
<p>A contested family law or commercial matter typically costs <strong>$30,000–$150,000+ per side</strong> in legal fees, takes one to three years, and offers no certainty of outcome. A full-day mediation shared between two parties costs each person around $2,475 — and around 90% of disputes we mediate resolve on the day. <a href="/costs-of-going-to-court/">See the full cost comparison →</a></p>
""",
 [("How much does mediation cost at Mediations Australia?",
   "A half-day mediation is $3,000 +GST and a full-day is $4,500 +GST. These fees are typically split equally between the parties, so your share is around $1,650–$2,475. The initial consultation is always free."),
  ("Is the mediation fee shared between parties?",
   "Yes, in most cases the fee is split equally between both parties. Sharing the cost makes mediation significantly more affordable than each party funding their own litigation."),
  ("Do you charge the same fees for all dispute types?",
   "Yes — our half-day and full-day rates apply across family law, property, estate, workplace and commercial disputes. Multi-party or complex commercial matters are quoted individually after the free initial consultation."),
  ("Are there any hidden fees?",
   "No. All fees are fixed and agreed upfront. Overtime is charged at $400/hr if a session runs long, and room hire or travel may apply in some cases — these are always disclosed in advance."),
  ("Is the initial consultation really free?",
   "Yes, completely free with no obligation. It's how we assess your matter, explain your options, and give you an honest view of whether mediation is right for you.")],
 "Our Fee Structure",
 "Know the cost <em>before</em> you commit.",
 "Book a free initial consultation and get complete clarity on what resolving your dispute will cost.")

build("costs-of-going-to-court",
 "The Real Cost of Going to Court in Australia | 2026 Guide",
 "What does it actually cost to go to court in Australia? Filing fees, legal fees, barrister costs, lost time — and why mediation resolves most disputes for a fraction of the price.",
 "Court vs mediation costs",
 "The real cost of going to court in Australia.",
 "Court is rarely cheap, fast or predictable. This guide breaks down every cost you'll face — from filing fees to barrister briefs — and shows why most Australians who try mediation first resolve their dispute without ever needing a courtroom.",
 "Going to court in Australia typically costs between $30,000 and $150,000+ per side in legal fees for a contested matter, takes one to three years, and offers no certainty of outcome. Mediation resolves most disputes in one to two sessions for a fraction of the cost — typically $1,500–$2,500 per person shared.",
 """
<style>
.cost-table{width:100%;border-collapse:collapse;margin:24px 0 36px}
.cost-table th{text-align:left;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft);padding:0 0 10px;border-bottom:2px solid var(--sage-deep)}
.cost-table td{padding:14px 16px 14px 0;border-bottom:1px solid var(--line);vertical-align:top;font-size:.97rem;color:var(--ink-soft)}
.cost-table td:first-child{color:var(--ink);font-weight:600;width:38%}
.cost-table td:last-child{font-weight:700;color:var(--ink);white-space:nowrap;text-align:right;padding-right:0}
.cost-table tr:last-child td{border-bottom:none}
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin:32px 0}
.compare-col{border-radius:14px;padding:28px}
.compare-col-court{background:#fff3f3;border:1px solid #ffc8c8}
.compare-col-med{background:var(--sage-light);border:1px solid var(--sage)}
.compare-col h3{font-family:var(--serif);font-size:1.2rem;margin-bottom:16px}
.compare-col ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px;font-size:.95rem}
.compare-col li{display:flex;gap:10px;align-items:flex-start}
@media(max-width:640px){.compare-grid{grid-template-columns:1fr}}
</style>

<h2>Why court costs so much more than people expect</h2>
<p>Most people underestimate what litigation costs because they only see the headline legal fee. The real cost adds up across multiple stages — and each stage requires a lawyer's time, often a barrister's time, and sometimes expert witnesses too. Unlike mediation, litigation is billed by the hour, so the longer the other party disputes, the larger your bill grows.</p>

<h2>The full cost breakdown</h2>
<table class="cost-table">
  <thead><tr><th>Cost item</th><th>Notes</th><th>Typical range</th></tr></thead>
  <tbody>
    <tr>
      <td>Court filing fees</td>
      <td>Federal Circuit and Family Court of Australia fees for initiating proceedings. Varies by matter type and applicant income.</td>
      <td>$1,000–$4,500</td>
    </tr>
    <tr>
      <td>Solicitor fees</td>
      <td>Legal advice, drafting, correspondence, court documents and preparation. Billed by the hour throughout the matter.</td>
      <td>$350–$600/hr</td>
    </tr>
    <tr>
      <td>Barrister brief fees</td>
      <td>Required for contested hearings. Brief fees cover preparation and the hearing day; a trial can require multiple days.</td>
      <td>$5,000–$25,000+</td>
    </tr>
    <tr>
      <td>Expert witnesses</td>
      <td>Family reports, valuations, accounting experts. Each expert charges for preparation and giving evidence.</td>
      <td>$3,000–$15,000+</td>
    </tr>
    <tr>
      <td>Subpoenas &amp; disclosure</td>
      <td>Costs of obtaining documents, subpoenas to third parties, compliance with discovery obligations.</td>
      <td>$500–$5,000</td>
    </tr>
    <tr>
      <td>Mediation (court-ordered)</td>
      <td>Most courts require parties to attempt dispute resolution before a final hearing anyway — often at a later stage when costs have already escalated.</td>
      <td>$1,500–$4,000</td>
    </tr>
    <tr>
      <td>Lost income &amp; time</td>
      <td>Court hearings, lawyer meetings, document review. A contested matter typically consumes dozens of hours of your personal time over 1–3 years.</td>
      <td>Significant</td>
    </tr>
    <tr>
      <td><strong>Total per side — contested matter</strong></td>
      <td>For a contested family law or commercial dispute that proceeds to a final hearing.</td>
      <td><strong>$30,000–$150,000+</strong></td>
    </tr>
  </tbody>
</table>

<div class="callout">
  <h3>Courts usually require mediation first anyway</h3>
  <p>For most family law parenting matters, you are legally required to attempt Family Dispute Resolution before you can file. For property matters and commercial disputes, courts increasingly expect parties to have genuinely attempted to resolve the matter before consuming court time. Mediation first is not just cheaper — it's often mandatory.</p>
</div>

<h2>Court vs mediation — a direct comparison</h2>
<div class="compare-grid">
  <div class="compare-col compare-col-court">
    <h3 style="color:#c0392b">Going to court</h3>
    <ul>
      <li><span>✗</span> $30,000–$150,000+ per side in legal fees</li>
      <li><span>✗</span> 1–3 years to resolution</li>
      <li><span>✗</span> No certainty of outcome — a judge decides</li>
      <li><span>✗</span> Public record and adversarial process</li>
      <li><span>✗</span> Damages relationships permanently</li>
      <li><span>✗</span> Significant personal time and stress</li>
      <li><span>✗</span> Often ordered to attempt mediation anyway</li>
    </ul>
  </div>
  <div class="compare-col compare-col-med">
    <h3 style="color:var(--sage-deep)">Mediation first</h3>
    <ul>
      <li><span>✓</span> $1,500–$2,500 per person (shared fee)</li>
      <li><span>✓</span> 1–2 sessions, often resolved same day</li>
      <li><span>✓</span> You control the outcome</li>
      <li><span>✓</span> Completely confidential</li>
      <li><span>✓</span> Preserves working relationships</li>
      <li><span>✓</span> Minimal time away from work and family</li>
      <li><span>✓</span> ~90% of disputes we mediate resolve</li>
    </ul>
  </div>
</div>

<h2>What if mediation doesn't work?</h2>
<p>If mediation doesn't resolve your dispute, you are no worse off — and in most cases better off. You will have a clearer picture of the real issues, a better understanding of the other party's position, and often a narrowed set of disputes to take to court. Many matters that don't fully resolve at mediation still settle shortly after, once both parties see their positions clearly. You lose nothing by trying mediation first and gain the chance to avoid litigation entirely.</p>

<h2>How much does mediation cost by comparison?</h2>
<p>A full-day mediation at Mediations Australia is $4,500 +GST, typically split equally between the parties — meaning your share is around $2,475 all up. That's a single fixed fee covering intake, preparation, and a full day of mediation with a nationally accredited mediator. <a href="/our-fee-structure/">See our full fee schedule →</a></p>
""",
 [("How much does it cost to go to court in Australia?",
   "A contested court matter typically costs between $30,000 and $150,000+ per side in solicitor and barrister fees, filing fees, and expert witness costs. Matters that proceed to a final hearing are at the higher end of this range and can take one to three years to resolve."),
  ("What are the filing fees for court in Australia?",
   "Federal Circuit and Family Court of Australia filing fees range from approximately $1,000 to $4,500 depending on the type of matter and whether you qualify for a reduced fee based on income. Filing fees are just the starting point — legal representation typically adds tens of thousands on top."),
  ("Is mediation cheaper than going to court?",
   "Yes, significantly. A full-day mediation typically costs each party around $2,000–$2,500, compared with $30,000–$150,000+ per side in a contested court matter. Around 90% of disputes mediated at Mediations Australia resolve without ever reaching court."),
  ("Do I have to try mediation before going to court?",
   "For most family law parenting matters, yes — you are legally required to attempt Family Dispute Resolution before filing. For property and commercial matters, courts increasingly expect parties to have genuinely attempted resolution before consuming court time and resources."),
  ("What happens if mediation fails?",
   "If mediation doesn't resolve your dispute you are not worse off — you retain all rights to proceed to court. In most cases you will have a clearer picture of the issues and a narrower set of disputes, which reduces the cost and time of any subsequent litigation.")],
 "Costs of Going to Court",
 "Mediation costs a <em>fraction</em> of litigation.",
 "Start with a free consultation and find out how mediation can resolve your dispute without the cost and delay of court.")

print("Additional service pages built.")
