#!/usr/bin/env python3
"""Additional service + fee pages, keyword-first H1s, full schema."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
OUT="/home/claude/mediations/site"

def build(slug,title,desc,eyebrow,h1,lede,ans,blocks,qa,crumb,cta_h,cta_p):
    schema=[org_schema(),breadcrumb_schema([("Home",""),(crumb,slug)]),
            service_schema(crumb,desc,slug),faq_schema(qa)]
    d=head(title,desc,slug,extra_schema=schema)+nav()
    d+=f"""<main id="main">
{crumb_html([("Home",""),(crumb,None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
<h1>{h1}</h1><p class="lede">{lede}</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
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
 "Estate Dispute Mediation Australia | Contested Wills Without Court",
 "Resolve contested wills and inheritance disputes through mediation. Faster, private and far cheaper than litigation. Nationally accredited mediators. Free consultation.",
 "Estate &amp; inheritance disputes",
 "Estate Dispute Mediation — resolve contested wills <em>without court</em>.",
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
 "Book a fixed-fee consultation to resolve a contested will or estate dispute through dignified, private mediation.")

# ---- COLLABORATIVE FAMILY LAWYERS ----
build("collaborative-family-lawyers",
 "Collaborative Family Lawyers Australia | Resolve Without Court",
 "Collaborative family lawyers help you resolve separation respectfully, out of court. A team-based approach focused on agreement, not litigation. Free consultation.",
 "Collaborative practice",
 "Collaborative Family Lawyers — separation <em>without the courtroom</em>.",
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
 "Family Law Arbitration Australia | Binding Decisions Without Court",
 "Family law arbitration gives you a binding decision on property and financial matters, faster and more privately than court. Nationally accredited arbitrators. Free consultation.",
 "Arbitration",
 "Family Law Arbitration — a binding decision, <em>without court delays</em>.",
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
 "Divorce and separation counselling to help you and your family cope with the emotional side of separation. Compassionate support alongside practical mediation. Get in touch.",
 "Emotional support",
 "Divorce Counselling — support for the <em>human side</em> of separation.",
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

# ---- FEE STRUCTURE ----
build("our-fee-structure",
 "Our Fee Structure | Transparent, Fixed-Fee Mediation Costs",
 "Transparent, fixed-fee mediation pricing with no surprises. Understand exactly what mediation costs and why it's a fraction of litigation. Free initial consultation.",
 "Pricing &amp; fees",
 "Our Fee Structure — <em>transparent, fixed and fair</em>.",
 "We believe you should know what things cost before you commit. Our mediation services start with a fixed-fee consultation and clear, upfront pricing — so there are no open-ended bills and no surprises, just a fraction of the cost of litigation.",
 "Mediations Australia uses transparent, fixed-fee pricing. You start with a fixed-fee consultation, and mediation costs are agreed upfront and usually shared between the parties — typically a small fraction of the tens of thousands per side that contested litigation can cost.",
 """
 <h2>How does mediation pricing work?</h2>
 <p>You begin with a fixed-fee consultation, where we assess your matter and explain your options with no obligation. From there, the cost of mediation is agreed in advance, so you always know where you stand. Mediation fees are commonly shared between the parties, making it more affordable for everyone.</p>
 <h2>Why is mediation so much cheaper than court?</h2>
 <p>Because it resolves matters in one or two sessions rather than over one to three years of legal fees billed by the hour. A contested court case can cost tens or even hundreds of thousands of dollars per side; mediation typically costs a small fraction of that — and protects the assets you'd otherwise spend fighting. <a href="/family-law-mediation/">See family law mediation →</a></p>
 <div class="callout"><h3>No surprises — ever</h3>
 <p>Fixed-fee means exactly that. You'll never receive an open-ended bill that grows the longer your matter takes. The certainty is part of why mediation is less stressful than litigation.</p></div>
 <h2>What's included</h2>
 <ul>
   <li>A fixed-fee initial consultation to assess your matter</li>
   <li>Clear, agreed pricing for the mediation itself</li>
   <li>Guidance on formalising your agreement into <a href="/consent-orders/">consent orders</a> or a binding agreement</li>
   <li>The option of in-person or <a href="/online-divorce/">online mediation</a> at the same transparent rates</li>
 </ul>
 """,
 [("How much does mediation cost?",
   "You start with a fixed-fee consultation, then agree the cost of mediation upfront. It's typically a small fraction of litigation — often hundreds to a few thousand dollars shared between parties, versus tens of thousands per side in court."),
  ("Is the cost shared between parties?",
   "Usually, yes. Mediation fees are commonly shared between the parties, which makes the process more affordable for everyone involved."),
  ("Are there any hidden fees?",
   "No. Our pricing is fixed and transparent. You'll know what mediation costs before you commit, with no open-ended hourly billing."),
  ("Is the initial consultation really fixed-fee?",
   "Yes. The initial consultation is a fixed fee with no obligation, so you can understand your options and the likely cost before deciding how to proceed.")],
 "Our Fee Structure",
 "Know the cost <em>before</em> you commit.",
 "Book a fixed-fee consultation and get complete clarity on what resolving your dispute will cost.")

print("Additional service pages built.")
