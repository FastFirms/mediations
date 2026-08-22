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
<article class="body"><div class="wrap-narrow">{blocks}</div></article>"""
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
 "Mediation Fees, Clearly Explained | Mediations Australia",
 "Standard and Access Mediation fees for family law, property and workplace disputes. Per-participant pricing from $1,500 + GST. Free initial consultation.",
 "MEDIATION FEES",
 "Mediation fees, clearly explained.",
 "You should know what mediation is likely to cost before you commit. Your initial consultation is free. If you decide to proceed, we confirm the applicable fee before the mediation is booked.",
 "The standard individual contribution is $1,500 + GST for a session of up to 4 hours, or $2,250 + GST for up to 8 hours. Fees are commonly shared equally between two participants. The initial consultation is always free. A reduced-contribution Access Mediation pathway is available for eligible participants.",
 """
<style>
.fee-hero-note{font-size:.93rem;color:var(--ink-soft);max-width:62ch;margin:0 0 8px}
.fee-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px;margin:32px 0 24px}
.fee-card{background:#fff;border:1.5px solid var(--line,rgba(13,34,24,.14));border-radius:16px;padding:30px 28px}
.fee-card-duration{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft);margin-bottom:12px}
.fee-card-price{font-size:2.6rem;font-weight:800;color:var(--sage-deep,#1e6040);line-height:1}
.fee-card-unit{font-size:.85rem;color:var(--ink-soft);margin:4px 0 12px}
.fee-card-total{font-size:.9rem;color:var(--ink-soft);margin-bottom:12px;padding-bottom:12px;border-bottom:1px solid var(--line,rgba(13,34,24,.14))}
.fee-card-total strong{color:var(--ink)}
.fee-card-includes{font-size:.83rem;color:var(--ink-soft);line-height:1.55}
.fee-share-note{font-size:.85rem;color:var(--ink-soft);background:var(--sage-pale,#f1f5f1);border-radius:8px;padding:12px 16px;margin:4px 0 20px;line-height:1.5}
.access-strip{background:var(--sage-deep,#1e6040);color:#fff;border-radius:14px;padding:28px 28px 24px;margin:32px 0}
.access-strip h2{color:#fff;margin:0 0 8px;font-size:1.35rem}
.access-strip p{color:#fff!important;margin:0 0 6px;font-size:.93rem;line-height:1.55}
.access-strip-price{font-size:1.7rem;font-weight:800;color:#fff;margin:12px 0 6px;line-height:1}
.access-strip-sub{font-size:.83rem;color:rgba(255,255,255,.75);margin:0 0 18px}
.access-strip .btn-access{display:inline-flex;align-items:center;gap:8px;background:#fff;color:var(--sage-deep,#1e6040);border:none;border-radius:100px;padding:12px 24px;font-weight:700;font-size:.93rem;text-decoration:none;transition:opacity .2s;cursor:pointer}
.access-strip .btn-access:hover{opacity:.9;color:var(--sage-deep,#1e6040)}
.access-strip-meta{font-size:.78rem;color:rgba(255,255,255,.7)!important;margin-top:10px}
.fee-includes{margin:32px 0}
.fee-includes h2{margin-bottom:12px}
.fee-includes ul{margin:0 0 14px;padding-left:22px}
.fee-includes li{margin-bottom:7px;font-size:.93rem;color:var(--ink-soft);line-height:1.5}
.dispute-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:20px 0 8px}
.dispute-card{border:1.5px solid var(--line,rgba(13,34,24,.14));border-radius:10px;padding:16px 18px;background:#fff}
.dispute-card h3{margin:0 0 5px;font-size:.95rem;color:var(--ink)}
.dispute-card p{margin:0;font-size:.8rem;color:var(--ink-soft);line-height:1.45}
.online-note{background:var(--sage-pale,#f1f5f1);border-radius:10px;padding:18px 20px;margin:20px 0 12px;font-size:.9rem;color:var(--ink-soft);line-height:1.55}
.add-table{width:100%;border-collapse:collapse;margin:16px 0 8px;font-size:.9rem}
.add-table th{text-align:left;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft);padding:0 12px 8px 0;border-bottom:2px solid var(--sage-deep,#1e6040)}
.add-table td{padding:13px 12px 13px 0;border-bottom:1px solid var(--line,rgba(13,34,24,.14));vertical-align:top;color:var(--ink-soft);line-height:1.45}
.add-table td:last-child{font-weight:700;color:var(--ink);white-space:nowrap}
.add-table tr:last-child td{border-bottom:none}
.invite-note{background:var(--sage-pale,#f1f5f1);border-radius:8px;padding:14px 18px;margin:14px 0;font-size:.88rem;line-height:1.55;color:var(--ink-soft)}
.access-full{margin:40px 0 20px}
.access-full .eyebrow-tag{display:inline-block;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--sage-deep,#1e6040);background:var(--sage-pale,#f1f5f1);border-radius:100px;padding:4px 12px;margin-bottom:14px}
.access-assist-box{border:1.5px solid var(--sage-deep,#1e6040);border-radius:12px;padding:20px 22px;margin:20px 0;background:#fff}
.ast-row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--line,rgba(13,34,24,.14));font-size:.93rem}
.ast-row:last-child{border-bottom:none;font-weight:700;color:var(--sage-deep,#1e6040);padding-top:11px}
.band-table{width:100%;border-collapse:collapse;margin:16px 0 8px;font-size:.9rem}
.band-table th{text-align:left;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft);padding:0 12px 8px 0;border-bottom:2px solid var(--sage-deep,#1e6040)}
.band-table td{padding:11px 12px 11px 0;border-bottom:1px solid var(--line,rgba(13,34,24,.14));vertical-align:top;color:var(--ink-soft)}
.band-table td:last-child{font-weight:700;color:var(--ink)}
.band-table tr:last-child td{border-bottom:none}
.band-note{font-size:.8rem;color:var(--ink-soft);margin:4px 0 16px;font-style:italic}
.acc-how-step{display:flex;gap:16px;align-items:flex-start;margin-bottom:20px}
.acc-how-num{width:32px;height:32px;border-radius:50%;background:var(--sage-deep,#1e6040);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;margin-top:2px}
.acc-how-body h3{margin:0 0 4px;font-size:.97rem}
.acc-how-body p{margin:0;font-size:.87rem;color:var(--ink-soft);line-height:1.55}
.privacy-list{list-style:none;padding:0;margin:12px 0}
.privacy-list li{padding-left:24px;position:relative;margin-bottom:8px;font-size:.92rem;color:var(--ink-soft);line-height:1.45}
.privacy-list li::before{content:"\2717";position:absolute;left:0;color:var(--sage-deep,#1e6040);font-weight:700}
.fdr-note{background:var(--sage-pale,#f1f5f1);border-left:4px solid var(--sage-deep,#1e6040);border-radius:0 10px 10px 0;padding:16px 20px;margin:16px 0;font-size:.9rem;line-height:1.6;color:var(--ink-soft)}
.followup-table{width:100%;border-collapse:collapse;margin:14px 0;font-size:.88rem}
.followup-table th{text-align:left;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft);padding:0 12px 8px 0;border-bottom:2px solid var(--sage-deep,#1e6040)}
.followup-table td{padding:10px 12px 10px 0;border-bottom:1px solid var(--line,rgba(13,34,24,.14));color:var(--ink-soft)}
.followup-table td:last-child{font-weight:700;color:var(--ink)}
.followup-table tr:last-child td{border-bottom:none}
.dual-cta{display:flex;flex-wrap:wrap;gap:12px;margin:20px 0 8px}
.section-sep{border:none;border-top:1px solid var(--line,rgba(13,34,24,.12));margin:48px 0}
@media(max-width:600px){
  .fee-card-price{font-size:2rem}
  .fee-cards,.dispute-grid{grid-template-columns:1fr}
  .dual-cta{flex-direction:column}
  .dual-cta a{width:100%;justify-content:center;text-align:center}
  .access-strip{padding:22px 18px 20px}
  .add-table td,.add-table th{font-size:.82rem}
}
</style>

<p class="fee-hero-note">For most two-participant mediations, the standard fee is shared equally. Your initial consultation is always free.</p>

<h2>Standard Mediation Fees</h2>
<div class="fee-cards">
  <div class="fee-card">
    <div class="fee-card-duration">Up to 4 hours</div>
    <div class="fee-card-price">$1,500 <span style="font-size:1rem;font-weight:500">+ GST</span></div>
    <div class="fee-card-unit">usually per participant</div>
    <div class="fee-card-total"><strong>$3,000 + GST total</strong> when shared equally between two participants</div>
    <div class="fee-card-includes">Includes pre-mediation administration, preparation and the scheduled mediation session.</div>
  </div>
  <div class="fee-card">
    <div class="fee-card-duration">Up to 8 hours</div>
    <div class="fee-card-price">$2,250 <span style="font-size:1rem;font-weight:500">+ GST</span></div>
    <div class="fee-card-unit">usually per participant</div>
    <div class="fee-card-total"><strong>$4,500 + GST total</strong> when shared equally between two participants</div>
    <div class="fee-card-includes">Suitable where more time is appropriate because of the number or complexity of issues.</div>
  </div>
</div>
<p class="fee-share-note">A 50/50 division is common, but not compulsory. Participants may agree to divide the fee differently. Paying a larger share does not give a participant greater influence over the mediator or outcome.</p>
<div class="dual-cta">
  <a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation <span class="arr">&#8594;</span></a>
  <a href="/access-mediation/" class="btn btn-ghost">Can&#8217;t afford the standard fee? &#8594;</a>
</div>

<div class="access-strip" id="access-rescue">
  <h2>Can&#8217;t comfortably afford the standard fee?</h2>
  <p>You may qualify for Access Mediation. We reserve a limited amount of mediation capacity for people who can contribute toward private mediation but would experience genuine difficulty paying the standard fee.</p>
  <div class="access-strip-price">From $495 <span style="font-size:1rem;font-weight:500">+ GST per person</span></div>
  <div class="access-strip-sub">Each participant is assessed separately and privately.</div>
  <a href="/access-mediation/" class="btn-access">Check My Access Contribution &#8594;</a>
  <div class="access-strip-meta">Takes about 60 seconds &middot; No obligation &middot; No documents required</div>
</div>

<div class="fee-includes">
  <h2>What your fee includes</h2>
  <p>Our standard mediation fee generally includes:</p>
  <ul>
    <li>pre-mediation contact and administration;</li>
    <li>individual intake processes where required;</li>
    <li>ordinary mediator preparation;</li>
    <li>the scheduled mediation session;</li>
    <li>ordinary post-mediation administration.</li>
  </ul>
  <p>We confirm what is included before you proceed.</p>
  <p><strong>No surprise additional charges.</strong> If room hire, travel or additional mediation time may be required, we explain the applicable cost before it is incurred.</p>
</div>

<h2>Mediation across a range of disputes</h2>
<div class="dispute-grid">
  <div class="dispute-card"><h3>Family Law &amp; Separation</h3><p>Parenting arrangements, property settlement, de facto disputes and separation-related disagreements.</p></div>
  <div class="dispute-card"><h3>Property &amp; Estate</h3><p>Property settlements, estate and inheritance disputes, trust disputes and ownership disagreements.</p></div>
  <div class="dispute-card"><h3>Workplace &amp; Commercial</h3><p>Workplace conflict, employment disputes, commercial disagreements and business-partner disputes.</p></div>
  <div class="dispute-card"><h3>Online Mediation</h3><p>Private mediation conducted online throughout Australia at the same pricing.</p></div>
</div>
<p style="font-size:.85rem;color:var(--ink-soft);margin-top:6px">Online mediation follows the same pricing. The appropriate format and duration depend on the circumstances — we can discuss this at the free initial consultation.</p>

<hr class="section-sep">

<h2>Additional costs</h2>
<table class="add-table">
  <thead><tr><th style="width:28%">Item</th><th>When it may apply</th><th>Fee</th></tr></thead>
  <tbody>
    <tr><td><strong>Room hire</strong></td><td>Where a suitable private venue is required for in-person sessions.</td><td>Approx. $200&#8211;$400 + GST</td></tr>
    <tr><td><strong>Additional mediation time</strong></td><td>Agreed time beyond the standard booking where both participants wish to continue.</td><td>$400 + GST / hour</td></tr>
    <tr><td><strong>Interstate / regional travel</strong></td><td>Where a mediator travels outside the usual service area.</td><td>At cost, confirmed beforehand</td></tr>
  </tbody>
</table>
<p style="font-size:.83rem;color:var(--ink-soft)">Any room, travel or material additional-time cost is discussed before it is incurred.</p>

<hr class="section-sep">
<h2>Invitation to Mediate</h2>
<p>If you want Mediations Australia to formally approach another person about participating, we can arrange an Invitation to Mediate.</p>
<p><strong>Standard matters: $400 + GST</strong></p>
<div class="invite-note">For <strong>Access Mediation</strong>, ordinary invitation administration is included in the confirmed Access contribution. The $400 standard invitation charge does not apply separately.</div>

<hr class="section-sep">
<div class="access-full" id="access-mediation-fees">
  <span class="eyebrow-tag">ACCESS MEDIATION</span>
  <h2>Private mediation when the standard fee is out of reach.</h2>
  <p>We believe financial circumstances should not determine whether someone has a meaningful opportunity to resolve a dispute through mediation.</p>
  <p>Access Mediation is a reduced-contribution pathway for people who can contribute toward private mediation but would experience genuine difficulty paying the standard private fee.</p>
  <p><strong>Contributions start from $495 + GST per person.</strong> Your contribution is based on your own financial circumstances. The other participant is assessed separately.</p>
  <div class="dual-cta">
    <a href="/access-mediation/" class="btn btn-primary">Check My Access Contribution <span class="arr">&#8594;</span></a>
  </div>
  <p style="font-size:.8rem;color:var(--ink-soft);margin-top:4px">Indicative result in about 60 seconds &middot; No obligation</p>

  <h3 style="margin-top:28px">What does Access assistance mean?</h3>
  <p>Access Mediation does not reduce the professional value of the service. It reduces the amount an eligible participant personally contributes.</p>
  <div class="access-assist-box">
    <div class="ast-row"><span>Standard individual contribution</span><span>$1,500 + GST</span></div>
    <div class="ast-row"><span>Access assistance (example, Band 1)</span><span>&#8722;$1,005</span></div>
    <div class="ast-row"><span>Your contribution</span><span>$495 + GST</span></div>
  </div>

  <h3 style="margin-top:28px">Access contributions &#8212; up to 3 hours</h3>
  <table class="band-table">
    <thead><tr><th>Gross personal income</th><th>Indicative contribution</th></tr></thead>
    <tbody>
      <tr><td>$0 &#8211; $50,000</td><td>$495 + GST</td></tr>
      <tr><td>$50,001 &#8211; $75,000</td><td>$695 + GST</td></tr>
      <tr><td>$75,001 &#8211; $100,000</td><td>$895 + GST</td></tr>
      <tr><td>$100,001 &#8211; $125,000</td><td>$1,095 + GST</td></tr>
      <tr><td>$125,001 &#8211; $150,000</td><td>$1,295 + GST</td></tr>
      <tr><td>More than $150,000</td><td>Standard contribution, subject to exceptional hardship review</td></tr>
    </tbody>
  </table>
  <p class="band-note">Accessible financial resources, dependants and exceptional hardship may affect the final contribution.</p>

  <h3>What if the matter needs longer?</h3>
  <p>If assessed as requiring a longer mediation, eligible participants may be offered up to six hours. Complexity determines the appropriate duration, not the financial-capacity band.</p>
  <table class="band-table">
    <thead><tr><th>Gross personal income</th><th>Indicative 6-hour contribution</th></tr></thead>
    <tbody>
      <tr><td>$0 &#8211; $50,000</td><td>$745 + GST</td></tr>
      <tr><td>$50,001 &#8211; $75,000</td><td>$995 + GST</td></tr>
      <tr><td>$75,001 &#8211; $100,000</td><td>$1,295 + GST</td></tr>
      <tr><td>$100,001 &#8211; $125,000</td><td>$1,595 + GST</td></tr>
      <tr><td>$125,001 &#8211; $150,000</td><td>$1,895 + GST</td></tr>
      <tr><td>More than $150,000</td><td>Standard contribution, subject to exceptional hardship review</td></tr>
    </tbody>
  </table>

  <h3 style="margin-top:28px">How Access Mediation works</h3>
  <div class="acc-how-step"><div class="acc-how-num">1</div><div class="acc-how-body"><h3>Check your indicative contribution</h3><p>Complete a short private questionnaire about your individual financial circumstances. Takes about 60 seconds.</p></div></div>
  <div class="acc-how-step"><div class="acc-how-num">2</div><div class="acc-how-body"><h3>Each participant is assessed separately</h3><p>One participant&#8217;s financial circumstances do not determine what the other participant pays.</p></div></div>
  <div class="acc-how-step"><div class="acc-how-num">3</div><div class="acc-how-body"><h3>We confirm your contribution</h3><p>The calculator is indicative. We primarily rely on information provided and may request limited clarification where genuinely required.</p></div></div>
  <div class="acc-how-step"><div class="acc-how-num">4</div><div class="acc-how-body"><h3>We arrange the appropriate pathway</h3><p>Financial eligibility does not determine suitability. Normal intake, safety, suitability and availability requirements apply.</p></div></div>

  <h3>Your financial assessment is private</h3>
  <p>We do not provide the other participant with your:</p>
  <ul class="privacy-list">
    <li>income band;</li>
    <li>asset information;</li>
    <li>concession status;</li>
    <li>hardship information;</li>
    <li>reasons for your contribution;</li>
    <li>Access assistance amount.</li>
  </ul>
  <p>Participants may have different contributions. The financial basis remains private.</p>

  <div class="fdr-note" style="margin-top:20px"><strong>Section 60I certificates are not automatically included</strong> with Access Mediation. If obtaining a certificate may be important to you, tell us before booking so we can identify the appropriate service. If unsure, speak with our team or obtain independent legal advice. <a href="/contact/" style="color:var(--sage-deep,#1e6040)">Talk to our team about FDR &#8594;</a></div>

  <p style="font-size:.85rem;color:var(--ink-soft);margin-top:12px">Common questions about Access — eligibility, bank statements, the other participant&#8217;s income, hardship, cancellations and what happens after mediation — are answered in the FAQ below.</p>

  <div class="dual-cta" style="margin-top:28px">
    <a href="/book-a-consultation/" class="btn btn-primary">Book a Free Consultation <span class="arr">&#8594;</span></a>
    <a href="/access-mediation/" class="btn btn-ghost">Check My Access Contribution <span class="arr">&#8594;</span></a>
  </div>
  <p style="font-size:.78rem;color:var(--ink-soft);margin-top:8px">Free initial consultation &middot; Clear fees before you proceed &middot; Online or in person &middot; Australia-wide</p>
</div>
""",
 [("How much does mediation cost?",
   "A session of up to 4 hours is $3,000 + GST total, usually $1,500 + GST per participant when shared equally. A session of up to 8 hours is $4,500 + GST total, usually $2,250 + GST per participant. The initial consultation is always free."),
  ("Is the initial consultation free?",
   "Yes, completely free with no obligation. It is how we assess your matter, explain your options, and give you an honest view of whether mediation is right for you."),
  ("Is the fee shared between participants?",
   "In most cases, yes. A 50/50 split is common but not compulsory. Participants may agree to divide the fee differently. Paying a larger share does not give any participant greater influence over the mediator or outcome."),
  ("Do you charge the same fees for all dispute types?",
   "The standard fee structure applies broadly across family law, property, workplace and commercial disputes. Matters with three or more parties or exceptional complexity may be quoted individually after the initial consultation."),
  ("Are there any hidden fees?",
   "No. All fees are fixed and agreed upfront. If room hire, travel or additional mediation time may apply, we discuss the cost before it is incurred."),
  ("What is Access Mediation?",
   "Access Mediation is a limited reduced-contribution pathway for eligible participants who would experience genuine difficulty paying the standard fee. Contributions are assessed individually based on personal income, assets, dependants and hardship circumstances, starting from $495 + GST per person for a 3-hour session."),
  ("Can I qualify if the other participant earns more?",
   "Yes. Each participant is assessed individually. One participant's financial circumstances do not determine what the other pays."),
  ("Can both participants qualify for Access Mediation?",
   "Yes. Both participants can be assessed separately and may both receive a reduced contribution if eligible."),
  ("Will the other participant know I receive Access assistance?",
   "No. Your income band, asset information, concession status, hardship circumstances and contribution are never disclosed to the other participant. The financial basis for each assessment is kept private."),
  ("Do I need to provide bank statements?",
   "Not ordinarily. The Access assessment is primarily self-declared. Limited supporting information may be requested where clarification is genuinely required. Please do not send financial documents unless asked."),
  ("Does Access Mediation change the quality of the service?",
   "No. Access Mediation does not reduce the professional standard of the service, mediator qualifications, or our obligations. It reduces the amount an eligible participant personally contributes."),
  ("Is a section 60I certificate included with Access Mediation?",
   "Not automatically. A section 60I certificate is issued following a recognised Family Dispute Resolution process. If obtaining a certificate may be important to you, tell us before booking so we can help identify the appropriate service and practitioner."),
  ("What if the other participant will not agree to mediate?",
   "Mediation requires the voluntary participation of all parties. If the other participant declines, we can issue a formal Invitation to Mediate and, if they still decline, provide documentation confirming a genuine attempt was made."),
  ("Is mediation cheaper than going to court?",
   "For most people, yes. Mediation involves a fixed, known fee agreed before you proceed. Court proceedings involve ongoing legal costs that are difficult to predict and can extend for months or years. We recommend obtaining independent legal advice about your specific circumstances.")],
 "Our Fee Structure",
 "READY TO TAKE THE NEXT STEP?",
 "Know the cost before you commit.")


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

# ---- WORKPLACE SUB-PAGES ----

build(
 "unfair-dismissal-termination-mediation",
 "Unfair Dismissal & Termination Mediation | Mediations Australia",
 "Resolve unfair dismissal and termination disputes through mediation. 21-day deadline — act fast. Faster, private and cheaper than a Fair Work Commission hearing.",
 "Workplace &amp; employment disputes",
 "Unfair Dismissal &amp; Termination Dispute Mediation",
 "Losing a job is one of the most stressful things that can happen. When a termination is challenged, both sides face a formal claim, legal costs and months of uncertainty. Mediation offers a faster, private and less adversarial path to a resolution that everyone can live with — but the 21-day deadline cannot be missed.",
 "An unfair dismissal dispute arises when a former employee believes their dismissal was harsh, unjust or unreasonable, and seeks a remedy such as compensation or reinstatement. In the national system, these claims are made to the Fair Work Commission, which then offers the parties a chance to resolve the matter by conciliation before it ever reaches a formal hearing.",
 """
 <div class="callout" style="border-left:4px solid var(--terra)">
   <p><strong>The 21-day deadline you cannot miss.</strong> An unfair dismissal application must be lodged with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> within 21 days after the dismissal takes effect. Extensions are only granted in exceptional circumstances. Do not let the clock run while you decide what to do.</p>
 </div>

 <h2>Who can bring an unfair dismissal claim?</h2>
 <p>Under the <a href="https://www.legislation.gov.au/Details/C2009A00028" target="_blank" rel="noopener">Fair Work Act 2009 (Cth)</a>, a person generally needs to meet all of the following:</p>
 <ul>
   <li>They were <strong>dismissed</strong> (including being forced to resign — constructive dismissal)</li>
   <li>They completed the <strong>minimum employment period</strong> — 6 months, or 12 months if the employer has fewer than 15 employees</li>
   <li>They earn <strong>below the high-income threshold</strong>, or are covered by a modern award or enterprise agreement</li>
   <li>The dismissal was <strong>not a genuine redundancy</strong>, and where a small business is involved, the employer did not comply with the Small Business Fair Dismissal Code</li>
 </ul>

 <h2>How conciliation and mediation resolve these disputes</h2>
 <p>When an unfair dismissal application is lodged, the Fair Work Commission usually offers a conciliation — an informal, confidential discussion run by an impartial conciliator. The conciliator does not decide who is right; they help the parties explore a settlement. Around three in four unfair dismissal cases are resolved at this stage, without ever reaching a Commission Member for a decision.</p>

 <p>Because the parties design the outcome themselves, a settlement can include things a tribunal cannot order:</p>
 <ul>
   <li>an agreed <strong>compensation payment</strong></li>
   <li>an agreed <strong>statement of service</strong> or reference</li>
   <li>a <strong>non-disparagement</strong> agreement</li>
   <li>a <strong>mutual release</strong>, ending the dispute for good</li>
   <li><strong>confidentiality</strong> over the terms</li>
 </ul>
 <p>Private mediation with Mediations Australia can run alongside or instead of the Commission's own process, giving you more time, more privacy and a mediator matched specifically to your matter.</p>

 <figure class="tbl"><table><caption>Mediation vs a contested Fair Work hearing</caption>
 <thead><tr><th></th><th>Mediation</th><th>Formal FWC hearing</th></tr></thead>
 <tbody>
 <tr><td>Timeframe</td><td>Weeks — often one session</td><td>Months to over a year</td></tr>
 <tr><td>Cost</td><td>Fixed, shared, transparent</td><td>Legal fees + preparation + witnesses</td></tr>
 <tr><td>Outcome control</td><td>Parties decide</td><td>Commissioner decides</td></tr>
 <tr><td>Confidential</td><td>Yes — without prejudice</td><td>No — decisions are published</td></tr>
 <tr><td>Remedies available</td><td>Flexible — agreed terms</td><td>Capped compensation or reinstatement</td></tr>
 </tbody></table></figure>

 <h2>When to be cautious</h2>
 <p>If a dismissal is bound up with allegations of serious misconduct, discrimination or bullying, there may be additional legal avenues and different time limits to consider. A general protections claim has a much shorter lodgement window in dismissal cases — see our <a href="/general-protections-discrimination-mediation/">general protections and discrimination guide</a>. Getting early advice ensures you choose the right pathway and do not inadvertently give up a right.</p>

 <div class="callout">
   <h3>Support and further help</h3>
   <p><strong><a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a></strong> — unfair dismissal process and forms<br>
   <strong><a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a></strong> — workplace rights and entitlements<br>
   <strong><a href="https://www.legalaid.nsw.gov.au/" target="_blank" rel="noopener">Legal Aid NSW</a></strong> — free legal help for eligible people<br>
   <strong>Lifeline</strong>: 13 11 14 &middot; <strong>Beyond Blue</strong>: 1300 22 4636</p>
 </div>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. For personalised guidance, please consult a qualified legal professional or accredited mediator.</p>
 """,
 [("How long do I have to lodge an unfair dismissal claim?",
   "You have 21 days from the date the dismissal takes effect to lodge with the Fair Work Commission. Extensions are only granted in exceptional circumstances, so act quickly."),
  ("Will I have to face my employer in person?",
   "Not necessarily. Fair Work conciliations are usually held by telephone, and private mediation can be run in a shuttle format where the mediator moves between separate rooms so the parties never have to be face to face."),
  ("What sort of compensation might be agreed?",
   "Settlements vary widely depending on the circumstances, length of service and the strength of the claim. Because the outcome is negotiated, it can also include non-financial terms such as a reference or an agreed statement of service."),
  ("Do I need a lawyer?",
   "It is not mandatory. Many people resolve these matters without a lawyer present. However, given the tight deadlines and the money often at stake, early legal advice is strongly advisable."),
  ("Can the agreement be made binding?",
   "Yes. A mediated settlement is typically recorded in a deed of settlement, creating an enforceable legal agreement that ends the dispute.")],
 "Unfair Dismissal Mediation",
 "Act fast — <em>the 21-day deadline cannot be missed</em>.",
 "Book a free consultation now. Whether you have been dismissed or are facing a claim, mediation gives you a faster, private path to resolution.")

build(
 "workplace-bullying-harassment-mediation",
 "Workplace Bullying & Harassment Mediation | Mediations Australia",
 "Mediation for workplace bullying and harassment — resolve complaints early, confidentially and constructively. Honest about when mediation is and isn't appropriate.",
 "Workplace &amp; employment disputes",
 "Workplace Bullying &amp; Harassment Mediation",
 "Being bullied or harassed at work takes a real toll — on your health, your confidence and your ability to do your job. Handled early and well, many of these situations can be resolved through mediation. Handled badly, or where the conduct is serious, they can escalate into tribunal applications, safety regulator involvement and lasting harm. This guide explains where mediation helps, and where it does not.",
 "Workplace bullying is repeated, unreasonable behaviour directed at a worker or group of workers that creates a risk to health and safety. The key elements are that the behaviour is repeated and unreasonable, and that it creates a health and safety risk. Harassment overlaps with bullying but also includes conduct connected to a protected attribute such as sex, race or disability, and sexual harassment, which is regulated separately and treated very seriously under Australian law.",
 """
 <div class="callout" style="border-left:4px solid var(--terra)">
   <p><strong>If you are in immediate danger, call 000.</strong> For confidential counselling and support, contact 1800RESPECT on 1800 737 732 or Lifeline on 13 11 14.</p>
 </div>

 <h2>How the law treats bullying and harassment</h2>
 <p>Workplace bullying is a regulated legal risk with direct consequences for employers. Two important avenues exist alongside internal complaint processes:</p>
 <ul>
   <li><strong>Stop-bullying orders.</strong> A worker can apply to the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> for an order to stop bullying at work. The Commission can only make such an order where there is a risk that the bullying will continue — it cannot order a payment of money. It aims to contact the parties within about two weeks and resolve most cases within around 16 weeks, often beginning with voluntary conciliation.</li>
   <li><strong>Work health and safety duties.</strong> Employers have a positive duty to manage the risk of bullying and harassment. <a href="https://www.safeworkaustralia.gov.au/" target="_blank" rel="noopener">Safe Work Australia</a> publishes national guidance on preventing and responding to these risks.</li>
 </ul>
 <p>Depending on the conduct, other pathways may also apply — such as a general protections claim or a discrimination complaint, each with their own time limits. We cover those in our <a href="/general-protections-discrimination-mediation/">general protections and discrimination guide</a>.</p>

 <h2>Where mediation helps</h2>
 <p>Many bullying and harassment complaints stem from breakdowns in communication, unclear expectations, or interpersonal conflict that has been allowed to fester. In these situations — where both people can participate safely and freely — mediation can be genuinely effective. A skilled mediator can:</p>
 <ul>
   <li>give each person a structured, safe space to be heard</li>
   <li>surface the underlying issues rather than just the surface conflict</li>
   <li>rebuild a workable professional relationship where the parties must continue working together</li>
   <li>produce a clear, practical agreement about future conduct and expectations</li>
 </ul>
 <p>For employers, offering mediation early can resolve a complaint before it becomes a stop-bullying application or a safety-regulator matter, while demonstrating the organisation took the complaint seriously.</p>

 <h2>When mediation is NOT appropriate</h2>
 <p>This is the part that matters most, and where we will always be honest with you. Mediation depends on both people being able to take part safely and on an equal enough footing. It is often not the right first step where:</p>
 <ul>
   <li>the conduct involves <strong>violence, threats, or serious sexual harassment</strong></li>
   <li>there is a <strong>serious power imbalance</strong> — for example between a senior manager and a junior worker — that cannot be safely managed</li>
   <li>a party feels <strong>unsafe, intimidated, or fears reprisal</strong> for speaking honestly</li>
   <li>the behaviour is <strong>ongoing and needs to be stopped urgently</strong>, which may call for a stop-bullying application or a report to the work health and safety regulator first</li>
   <li>the matter genuinely requires an <strong>independent investigation</strong> to establish what happened</li>
 </ul>
 <p>Pushing two people into a room together can cause real harm when the conditions are not right. A responsible mediator will screen for these issues before proceeding and will tell you plainly if mediation is not suitable — and what to do instead.</p>

 <h2>What to do if you are being bullied or harassed</h2>
 <ol>
   <li><strong>Prioritise your safety.</strong> If you are in immediate danger, call 000. If you are distressed, reach out to one of the support services below.</li>
   <li><strong>Use internal processes where it is safe to do so.</strong> Many workplaces have bullying and grievance policies. The Fair Work Commission encourages workers to use these first, where safe.</li>
   <li><strong>Keep records.</strong> Note dates, times, what was said or done, and any witnesses.</li>
   <li><strong>Get advice early.</strong> Different avenues have different time limits, and some depend on the risk continuing. Early advice protects your options.</li>
   <li><strong>Consider mediation once safety is assured.</strong> Where the conditions are right, mediation can resolve the situation faster and more constructively than a formal process.</li>
 </ol>

 <div class="callout">
   <h3>Support and further help</h3>
   <p><strong>In an emergency:</strong> 000<br>
   <strong>1800RESPECT</strong> (sexual assault, domestic and family violence): 1800 737 732<br>
   <strong>Lifeline</strong> (24-hour crisis support): 13 11 14<br>
   <strong>Beyond Blue</strong> (mental health support): 1300 22 4636<br>
   <strong><a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a></strong> — stop-bullying applications<br>
   <strong><a href="https://www.safeworkaustralia.gov.au/" target="_blank" rel="noopener">Safe Work Australia</a></strong> — work health and safety guidance</p>
 </div>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. Workplace bullying, harassment and safety matters can be serious and time-sensitive. For personalised guidance, consult a qualified legal professional, accredited mediator, or the relevant regulator.</p>
 """,
 [("Is mediation always the answer for bullying?",
   "No. Mediation can be very effective for interpersonal conflict where both parties can participate safely. It is often not appropriate where there is violence, serious harassment, a serious power imbalance, or where the behaviour needs to be stopped urgently. Safety comes first."),
  ("What is a stop-bullying order?",
   "It is an order from the Fair Work Commission requiring behaviour to stop. The Commission can only make one where there is a risk the bullying will continue, and it cannot order any payment of money. It is aimed at fixing an active situation rather than compensating for past conduct."),
  ("Can my employer make me attend mediation?",
   "Mediation is voluntary. You should never feel pressured into a process that does not feel safe. If you have concerns about safety or power imbalance, raise them — a good mediator will screen for exactly these issues."),
  ("Will it be confidential?",
   "Yes. Mediation is a confidential, without-prejudice process, which is part of what allows people to speak openly and reach a genuine resolution.")],
 "Bullying &amp; Harassment Mediation",
 "Honest about when mediation helps — <em>and when it doesn't</em>.",
 "Book a free consultation. We will give you an honest assessment of whether mediation is right for your situation, and what to do if it is not.")

build(
 "general-protections-discrimination-mediation",
 "General Protections & Discrimination Claim Mediation | Mediations Australia",
 "Mediation for general protections and discrimination claims — adverse action, workplace rights, protected attributes. 21-day deadline applies where dismissal is involved.",
 "Workplace &amp; employment disputes",
 "General Protections &amp; Discrimination Claim Mediation",
 "Some of the most serious workplace disputes are not about performance or redundancy, but about whether someone was treated badly because of who they are, or because they exercised a right at work. Mediation and conciliation resolve the large majority of these matters — faster, more privately and less painfully than a contested court case.",
 "A general protections claim alleges that an employer took adverse action against a person because that person had, or exercised, a workplace right or a protected attribute. Adverse action includes things like dismissing someone, refusing to employ them, or altering their position to their disadvantage. The protections are set out in the Fair Work Act 2009 (Cth) and enforced through the Fair Work Commission.",
 """
 <div class="callout" style="border-left:4px solid var(--terra)">
   <p><strong>Time limits are strict and short.</strong> Where the adverse action involved a dismissal, a general protections application must generally be lodged with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> within <strong>21 days</strong> of the dismissal taking effect. Act immediately to protect your rights.</p>
 </div>

 <h2>What are general protections and discrimination claims?</h2>
 <p>Workplace rights protected under the <a href="https://www.legislation.gov.au/Details/C2009A00028" target="_blank" rel="noopener">Fair Work Act 2009 (Cth)</a> include things like being entitled to a benefit under a workplace law, or making a complaint or inquiry about your employment. Protected attributes include race, sex, age, disability, religion, pregnancy, carer's responsibilities and more. Discrimination claims can also be pursued through federal and state anti-discrimination bodies, which run their own conciliation processes.</p>

 <figure class="tbl"><table><caption>Time limits at a glance</caption>
 <thead><tr><th>Type of claim</th><th>Where lodged</th><th>Deadline</th></tr></thead>
 <tbody>
 <tr><td>General protections — dismissal involved</td><td><a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a></td><td><strong>21 days</strong> from dismissal</td></tr>
 <tr><td>General protections — no dismissal</td><td>Fair Work Commission</td><td>Longer — act promptly</td></tr>
 <tr><td>Federal discrimination complaint</td><td><a href="https://humanrights.gov.au/" target="_blank" rel="noopener">Australian Human Rights Commission</a></td><td>Separate deadlines apply</td></tr>
 <tr><td>State discrimination complaint</td><td>State anti-discrimination body</td><td>Separate deadlines apply</td></tr>
 </tbody></table></figure>

 <h2>How these disputes are resolved without a trial</h2>
 <p>When a general protections dismissal claim is lodged, the Fair Work Commission will usually convene a conference — a confidential, without-prejudice discussion led by an impartial Commission Member. Anti-discrimination bodies similarly run conciliation before any matter proceeds to a tribunal or court. In both systems, the design intention is the same: resolve by agreement wherever possible.</p>

 <p>Private mediation with Mediations Australia complements these processes. It can be used:</p>
 <ul>
   <li><strong>Before you lodge</strong> — to attempt an early resolution and avoid the formal process</li>
   <li><strong>Alongside a lodged claim</strong> — to reach a settlement on your own terms and timetable</li>
   <li><strong>To craft outcomes a court could not order</strong> — such as an agreed reference, a policy change, an apology, or confidential settlement terms</li>
 </ul>

 <h2>Why mediation suits these matters particularly well</h2>
 <ul>
   <li><strong>Sensitivity.</strong> Discrimination claims are personal and often painful. A private process spares both sides the exposure of a public hearing.</li>
   <li><strong>Speed and cost.</strong> Fully litigated cases can be lengthy and expensive. A negotiated outcome avoids that.</li>
   <li><strong>Creative remedies.</strong> Because the parties design the outcome, a settlement can address what actually matters — recognition, change, a reference — not just a number.</li>
   <li><strong>Preserving reputation.</strong> For employers, resolving privately avoids a published finding and the associated reputational and cultural fallout.</li>
   <li><strong>Control and certainty.</strong> Litigation outcomes are uncertain and imposed. Mediated outcomes are agreed, and therefore predictable.</li>
 </ul>

 <h2>When to take extra care</h2>
 <p>Discrimination and general protections matters can involve serious conduct, significant power imbalances, and sometimes overlap with bullying, harassment or safety issues — see our <a href="/workplace-bullying-harassment-mediation/">bullying and harassment guide</a>. Where a person does not feel safe or able to negotiate freely, mediation may not be the right first step, and a formal process or independent advice may be needed instead. A responsible mediator screens for these issues before proceeding.</p>

 <div class="callout">
   <h3>Support and further help</h3>
   <p><strong><a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a></strong> — general protections process<br>
   <strong><a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a></strong> — workplace rights and protections<br>
   <strong><a href="https://humanrights.gov.au/" target="_blank" rel="noopener">Australian Human Rights Commission</a></strong> — federal discrimination complaints<br>
   <strong><a href="https://www.legalaid.nsw.gov.au/" target="_blank" rel="noopener">Legal Aid NSW</a></strong> — free legal help for eligible people<br>
   <strong>Lifeline</strong>: 13 11 14 &middot; <strong>Beyond Blue</strong>: 1300 22 4636</p>
 </div>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. For personalised guidance, please consult a qualified legal professional or accredited mediator.</p>
 """,
 [("What is the difference between a general protections claim and an unfair dismissal claim?",
   "An unfair dismissal claim asks whether a dismissal was harsh, unjust or unreasonable. A general protections claim asks whether adverse action was taken because the person had or exercised a workplace right or a protected attribute. They have different tests, different remedies, and you generally cannot pursue both for the same dismissal."),
  ("How long do I have to lodge?",
   "If a dismissal is involved, generally 21 days from when it took effect. Where no dismissal is involved, a longer period usually applies. Anti-discrimination complaints have their own separate deadlines. Act quickly to protect your rights."),
  ("Can these claims really be resolved by mediation?",
   "Yes. Both the Fair Work Commission and anti-discrimination bodies are built around conciliation, and the majority of matters settle without a formal hearing. Private mediation can resolve them even more flexibly."),
  ("Will the outcome be confidential?",
   "A mediated or conciliated settlement is generally confidential. A litigated outcome, by contrast, is usually public.")],
 "General Protections Mediation",
 "Deadlines are as short as 21 days — <em>act quickly</em>.",
 "Book a free consultation. These disputes are time-sensitive — the sooner you get advice, the more options you have.")

build(
 "partnership-executive-exit-mediation",
 "Partnership & Executive Exit Dispute Mediation | Mediations Australia",
 "Mediation for business partnership breakdowns and executive exit disputes. Private, fast and commercially focused — resolves ownership, entitlements, restraints and reputation in one process.",
 "Workplace &amp; employment disputes",
 "Partnership &amp; Executive Exit Dispute Mediation",
 "When a business partnership breaks down, or a senior executive's departure turns sour, the stakes are unusually high. These disputes threaten not just individual careers but the business itself — its clients, its staff, its value and its reputation. Mediation is frequently the smartest way through: private, fast and focused on preserving value rather than destroying it.",
 "Partnership and executive exit disputes arise when business partners, directors or senior executives separate — whether through a falling-out, a forced departure, or a negotiated exit — and disagree about the terms. They sit at the intersection of employment, commercial and sometimes corporate law, which is what makes them complex and what makes a skilled mediator so valuable.",
 """
 <h2>Common flashpoints in these disputes</h2>
 <ul>
   <li><strong>Partner and shareholder fallouts</strong> — disagreements over strategy, contribution, drawings, or the division of a business when one person wants out</li>
   <li><strong>Executive exits</strong> — a senior leader being managed out, or negotiating their own departure, with disputes over notice, entitlements, bonuses, equity and reputation</li>
   <li><strong>Restraints of trade and confidentiality</strong> — arguments over what a departing person can and cannot do next</li>
   <li><strong>Handover and communication</strong> — how the departure is announced to staff, clients and the market</li>
 </ul>

 <h2>Why litigation is such a poor fit here</h2>
 <p>Taking a partnership or executive dispute to court is often the worst available option, because the litigation itself damages the very thing being fought over:</p>

 <figure class="tbl"><table><caption>Court vs mediation for partnership and executive disputes</caption>
 <thead><tr><th></th><th>Mediation</th><th>Litigation</th></tr></thead>
 <tbody>
 <tr><td>Privacy</td><td>Fully private — without prejudice</td><td>Court files and judgments are public</td></tr>
 <tr><td>Business impact</td><td>Contained and confidential</td><td>Public conflict spooks clients and staff</td></tr>
 <tr><td>Speed</td><td>Weeks — often a single intensive day</td><td>Commercial litigation can take years</td></tr>
 <tr><td>Cost</td><td>Fixed, transparent, shared</td><td>Document-heavy; legal fees run high on both sides</td></tr>
 <tr><td>Outcome</td><td>Parties design the resolution</td><td>Judge decides; remedies are constrained</td></tr>
 <tr><td>Relationship aftermath</td><td>Built to let everyone move forward</td><td>Reputations and relationships often in ruins</td></tr>
 </tbody></table></figure>

 <h2>What mediation can achieve that a court cannot</h2>
 <p>Because the parties design the outcome, mediation can resolve the whole tangle at once — the legal, the financial and the human. A mediated settlement might address:</p>
 <ul>
   <li>the <strong>financial terms</strong> of the exit — buyout, entitlements, bonuses, equity</li>
   <li><strong>restraints and confidentiality</strong> going forward, agreed rather than litigated</li>
   <li>a <strong>clean division of clients, assets or responsibilities</strong></li>
   <li>an <strong>agreed narrative</strong> — how the departure is communicated to staff, clients and the market, protecting everyone's reputation</li>
   <li>a <strong>full mutual release</strong>, drawing a line under the dispute for good</li>
 </ul>
 <p>Many of our mediators are also experienced lawyers, which matters here: they understand the commercial and legal architecture of these deals, not just the interpersonal dynamics.</p>

 <h2>How the process works for high-stakes exits</h2>
 <ol>
   <li><strong>Confidential consultation.</strong> We help you understand your position and whether mediation is the right vehicle.</li>
   <li><strong>The right mediator.</strong> Our mediators are experienced in commercial and executive disputes — you work directly with our own team.</li>
   <li><strong>Careful preparation.</strong> Each side is spoken with privately. In high-conflict matters, sessions are often run in shuttle format, with the mediator moving between separate rooms.</li>
   <li><strong>The session.</strong> Often a single, intensive day — in person or online — focused on a global settlement rather than point-scoring.</li>
   <li><strong>A binding deed.</strong> The outcome is formalised into an enforceable settlement deed, so the terms — including restraints and releases — actually hold.</li>
 </ol>

 <h2>When to get additional advice</h2>
 <p>Partnership and executive disputes frequently involve overlapping legal questions — corporate governance, shareholder agreements, directors' duties, and sometimes general protections issues. See our <a href="/general-protections-discrimination-mediation/">general protections and discrimination guide</a> where a departure is bound up with a protected right. Mediation resolves the dispute, but you should also have your own legal and, where relevant, accounting advice on the substance of any deal.</p>

 <div class="callout">
   <h3>Support and further help</h3>
   <p><strong><a href="https://asic.gov.au/" target="_blank" rel="noopener">ASIC</a></strong> — company and directors' obligations<br>
   <strong><a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a></strong> — employment entitlements<br>
   <strong><a href="https://www.asbfeo.gov.au/" target="_blank" rel="noopener">Australian Small Business and Family Enterprise Ombudsman</a></strong> — small business dispute support<br>
   <strong>Lifeline</strong>: 13 11 14 &middot; <strong>Beyond Blue</strong>: 1300 22 4636</p>
 </div>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. For personalised guidance, please consult a qualified legal professional or accredited mediator.</p>
 """,
 [("Can mediation handle a dispute that is both commercial and personal?",
   "Yes — that is exactly its strength. A single mediated settlement can resolve the financial terms, the restraints, the client division and the reputational narrative all at once, which separate legal proceedings struggle to do."),
  ("Is it confidential?",
   "Yes. Mediation is private and without prejudice. This is a major advantage over litigation, where filings and judgments are generally public and can expose sensitive commercial information."),
  ("What if we cannot agree on the value of the business?",
   "Valuation disagreements are common and can be worked through in mediation, sometimes with the help of an agreed independent expert. The flexibility of the process is well suited to bridging these gaps."),
  ("Will the agreement be enforceable?",
   "Yes. Outcomes are formalised into a binding settlement deed, which can include enforceable restraints, releases and payment terms.")],
 "Partnership &amp; Executive Exit",
 "Private, fast and commercially focused — <em>before it costs you the business</em>.",
 "Book a free consultation. Resolve a partnership or executive exit dispute privately, before it becomes a public, value-destroying court battle.")

build(
 "redundancy-restructure-mediation",
 "Redundancy & Restructure Dispute Mediation | Mediations Australia",
 "When a restructure is challenged as unfair — the genuine redundancy test, consultation obligations, and how mediation resolves these disputes without a Fair Work hearing.",
 "Workplace &amp; employment disputes",
 "Redundancy &amp; Restructure Dispute Mediation",
 "A restructure can be a legitimate business decision. It can also be challenged — and increasingly is. When an employee believes a redundancy was not genuine, or that the consultation process fell short of what the law requires, a formal claim can follow quickly. Mediation offers both sides a faster, private path to resolution before the dispute reaches a hearing.",
 "A genuine redundancy under the Fair Work Act 2009 (Cth) requires three things: the job no longer exists, the employer has complied with any applicable consultation obligations under a modern award or enterprise agreement, and it was not reasonable to redeploy the person into another role. Where any of these elements is absent, the dismissal may be found to be unfair rather than a genuine redundancy.",
 """
 <div class="callout" style="border-left:4px solid var(--terra)">
   <p><strong>The 21-day deadline applies.</strong> An unfair dismissal application — including one challenging a purported redundancy — must be lodged with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> within 21 days after the dismissal takes effect. Do not wait.</p>
 </div>

 <h2>What makes a redundancy challengeable?</h2>
 <p>The most common grounds for challenging a redundancy are:</p>
 <ul>
   <li><strong>Failure to consult.</strong> Many modern awards and enterprise agreements require employers to consult meaningfully with affected employees before a final decision is made. A tick-the-box process, or no process at all, is a frequent basis for challenge.</li>
   <li><strong>The role was not genuinely eliminated.</strong> If the same or substantially similar duties continue to be performed — by the same person, a contractor, or a new hire — the redundancy may not be genuine.</li>
   <li><strong>Redeployment was not properly considered.</strong> Employers must consider whether redeployment within the business or an associated entity was reasonable. Overlooking a suitable vacancy is a common error.</li>
   <li><strong>Targeting.</strong> A redundancy that coincides with a complaint, a general protections matter or a period of absence can attract scrutiny beyond the unfair dismissal framework.</li>
 </ul>

 <h2>How mediation resolves redundancy disputes</h2>
 <p>When an unfair dismissal application is lodged over a purported redundancy, the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> will typically offer a conciliation before any hearing. Around three in four unfair dismissal matters — including redundancy challenges — settle at this stage. Private mediation with Mediations Australia can run earlier and on your own timetable, giving you more control over the process and the outcome.</p>

 <p>A mediated settlement in a redundancy dispute can include:</p>
 <ul>
   <li>an agreed <strong>compensation payment</strong></li>
   <li>an agreed <strong>statement of service</strong> or reference</li>
   <li>a <strong>non-disparagement agreement</strong> on both sides</li>
   <li><strong>confidentiality</strong> over the terms</li>
   <li>a <strong>mutual release</strong>, drawing a line under the matter</li>
 </ul>

 <figure class="tbl"><table><caption>Mediation vs a contested Fair Work hearing on redundancy</caption>
 <thead><tr><th></th><th>Mediation</th><th>Formal FWC hearing</th></tr></thead>
 <tbody>
 <tr><td>Timeframe</td><td>Weeks</td><td>Months to over a year</td></tr>
 <tr><td>Cost</td><td>Fixed, shared</td><td>Legal fees + preparation</td></tr>
 <tr><td>Outcome control</td><td>Parties decide</td><td>Commissioner decides</td></tr>
 <tr><td>Confidential</td><td>Yes</td><td>No — decisions are published</td></tr>
 <tr><td>Remedies available</td><td>Flexible agreed terms</td><td>Capped compensation or reinstatement</td></tr>
 </tbody></table></figure>

 <h2>For employers: getting restructures right</h2>
 <p>Mediation is not only for after a claim is lodged. Employers facing a significant restructure can use facilitated conversation to manage the process more constructively — giving affected employees a genuine voice, reducing the risk of challenge, and preserving goodwill where ongoing relationships matter. A mediator experienced in employment law can help structure the consultation process itself, not just resolve disputes that arise from it.</p>

 <div class="callout">
   <h3>Support and further help</h3>
   <p><strong><a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a></strong> — unfair dismissal and redundancy process<br>
   <strong><a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a></strong> — redundancy pay and entitlements<br>
   <strong><a href="https://www.legalaid.nsw.gov.au/" target="_blank" rel="noopener">Legal Aid NSW</a></strong> — free legal help for eligible people<br>
   <strong>Lifeline</strong>: 13 11 14 &middot; <strong>Beyond Blue</strong>: 1300 22 4636</p>
 </div>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. For personalised guidance, please consult a qualified legal professional or accredited mediator.</p>
 """,
 [("What is a genuine redundancy?",
   "Under the Fair Work Act, a genuine redundancy requires that the job no longer exists, the employer complied with any consultation obligations, and redeployment elsewhere in the business was not reasonable. Where any element is missing, a dismissed employee may have grounds for an unfair dismissal claim."),
  ("Can I challenge a redundancy if I was the only person let go?",
   "Yes. The number of employees affected is not determinative. A single redundancy can still be challenged if the process was flawed, the role continued in substance, or redeployment was not genuinely considered."),
  ("How long do I have to lodge a claim?",
   "21 days from the date the dismissal takes effect. Extensions are only granted in exceptional circumstances — do not wait."),
  ("Can mediation resolve a redundancy dispute before a claim is lodged?",
   "Yes. Private mediation can be used at any point — before a formal application, alongside one, or to resolve a dispute that the Commission's conciliation process did not settle."),
  ("What can a settlement include?",
   "Because the parties design the outcome, a settlement can include compensation, an agreed reference, a non-disparagement agreement, and confidential terms — things a tribunal cannot order.")],
 "Redundancy &amp; Restructure Mediation",
 "Resolve it before the 21-day deadline — <em>and before it escalates</em>.",
 "Book a free consultation. Whether you are an employee challenging a redundancy or an employer managing a restructure, early advice protects your options.")

build(
 "workplace-investigations-grievance-mediation",
 "Workplace Investigations & Grievance Mediation | Mediations Australia",
 "When to investigate, when to mediate, and how to resolve workplace grievances and repair a team without a drawn-out formal process.",
 "Workplace &amp; employment disputes",
 "Workplace Investigations &amp; Grievance Resolution",
 "A complaint has been made. Someone has raised a grievance. A formal investigation is under way — or being demanded. Getting this step right matters enormously. The wrong process can escalate a manageable situation into a protracted legal dispute, damage the entire team, and expose the organisation to significant liability. The right process resolves the complaint, restores the working environment and keeps everyone's dignity intact.",
 "A workplace grievance is a formal complaint by an employee about something at work — conduct, a decision, a working condition, or how they have been treated. A workplace investigation is the process by which a complaint is examined, evidence is gathered, and findings are made. Mediation is the process by which the underlying dispute is resolved. These three things are distinct, and knowing when to use which is the critical first decision.",
 """
 <h2>When to investigate — and when not to</h2>
 <p>Not every complaint requires a formal investigation, and not every investigation should lead straight to mediation. The right pathway depends on what the complaint is about, what the person making it actually wants, and what the organisation needs to do to meet its legal obligations.</p>

 <p>A formal investigation is generally appropriate where:</p>
 <ul>
   <li>the conduct alleged is serious — misconduct, serious harassment, fraud or safety breaches</li>
   <li>the organisation needs a factual finding to take disciplinary action or protect itself</li>
   <li>the alleged conduct may give rise to criminal liability</li>
   <li>a regulator requires one</li>
 </ul>

 <p>Mediation — rather than, or alongside, an investigation — is often more appropriate where:</p>
 <ul>
   <li>the complaint arises from a breakdown in communication or a relationship conflict rather than clear misconduct</li>
   <li>both parties want to continue working together</li>
   <li>the person making the complaint primarily wants to be heard, not to have someone punished</li>
   <li>an investigation would be disproportionate to what actually happened</li>
   <li>a swift, constructive resolution would better serve the working environment</li>
 </ul>

 <h2>Common mistakes organisations make</h2>
 <ul>
   <li><strong>Investigating when they should mediate.</strong> A heavy-handed investigation for what is essentially an interpersonal conflict entrenches positions, damages morale and rarely produces a workable outcome.</li>
   <li><strong>Mediating when they should investigate.</strong> Where serious misconduct is alleged, skipping a proper process to "sort it out quickly" can expose the organisation to claims that it failed in its duty of care.</li>
   <li><strong>Delaying.</strong> Unresolved complaints fester. The longer a grievance sits without a response, the more it costs — in productivity, in culture, and eventually in legal exposure.</li>
   <li><strong>Using internal managers as mediators.</strong> A manager who is seen as aligned with the organisation cannot provide the neutrality that effective resolution requires. An independent external mediator changes the dynamic.</li>
 </ul>

 <h2>How mediation resolves grievances</h2>
 <p>Where mediation is the right step, our mediators work with both sides to surface the real issues beneath the complaint, give each person a structured opportunity to be heard, and guide the parties toward a practical agreement about how things will work going forward. The agreement might cover communication protocols, working arrangements, an apology, or simply a shared understanding of what happened and why.</p>
 <p>For employers, early mediation of a grievance demonstrates that the complaint was taken seriously — which matters both to the employee and, if things escalate, to a regulator or tribunal. It is also substantially cheaper and faster than an investigation that leads to a contested termination.</p>

 <div class="callout">
   <h3>Support and further help</h3>
   <p><strong><a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a></strong> — workplace rights and dispute processes<br>
   <strong><a href="https://www.safeworkaustralia.gov.au/" target="_blank" rel="noopener">Safe Work Australia</a></strong> — psychosocial hazards and workplace safety<br>
   <strong><a href="https://humanrights.gov.au/" target="_blank" rel="noopener">Australian Human Rights Commission</a></strong> — discrimination and harassment<br>
   <strong>1800RESPECT</strong>: 1800 737 732 &middot; <strong>Lifeline</strong>: 13 11 14 &middot; <strong>Beyond Blue</strong>: 1300 22 4636</p>
 </div>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. For personalised guidance, please consult a qualified legal professional or accredited mediator.</p>
 """,
 [("Do we have to investigate every complaint?",
   "No. The obligation is to respond appropriately, which depends on the nature of the complaint. Some complaints are better handled through mediation or facilitated conversation than a formal investigation — and choosing the wrong process can make things worse."),
  ("Can mediation happen alongside an investigation?",
   "Yes. In some cases an investigation establishes the facts while mediation addresses the relationship and working environment. The two processes can run in sequence or, where appropriate, in parallel."),
  ("What if the person making the complaint doesn't want to mediate?",
   "Mediation is voluntary. A mediator will not pressure anyone into the process. Where mediation is not suitable or not wanted, we can advise on alternative approaches."),
  ("Who should act as mediator — someone internal or external?",
   "An independent external mediator is almost always preferable in a workplace grievance. An internal person — even a trained HR professional — carries the perception of organisational alignment, which undermines the neutrality the process depends on."),
  ("How quickly can a grievance be resolved through mediation?",
   "Most workplace grievance mediations are booked within a few weeks and completed in a single session. Compare this with a formal investigation and disciplinary process, which can take months and leave the working environment worse than before.")],
 "Investigations &amp; Grievances",
 "Get the process right from the start — <em>before it becomes something harder to resolve</em>.",
 "Book a free consultation. We will help you choose the right process — investigation, mediation, or both — and move quickly.")

print("Additional service pages built.")
