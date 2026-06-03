#!/usr/bin/env python3
"""Batch 6: is-mediation-compulsory, fathers-rights, superannuation, high-conflict."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- IS FAMILY LAW MEDIATION COMPULSORY (absorbs 7) ----
post("is-family-law-mediation-compulsory",
 "Is Family Law Mediation Compulsory in Australia? (2026)",
 "Is mediation compulsory before family court in Australia? When family dispute resolution and a Section 60I certificate are required, the exemptions, and what happens if your ex refuses.",
 "The process",
 "Is Family Law Mediation Compulsory in Australia?",
 "For most parenting disputes, yes \u2014 you must genuinely attempt family dispute resolution before you can apply to court, and you'll need a Section 60I certificate to prove it. This guide explains exactly when mediation is required, the exemptions, and what to do if your former partner refuses to take part.",
 [("short-answer","The short answer"),
  ("parenting","When it's required: parenting matters"),
  ("section-60i","The Section 60I certificate"),
  ("property","What about property matters?"),
  ("exemptions","Exemptions from the requirement"),
  ("refuses","What if my ex refuses?"),
  ("genuine","What counts as a genuine attempt?")],
 key_takeaway("For parenting disputes, attempting family dispute resolution (mediation) is generally compulsory before you can file in court \u2014 and you need a Section 60I certificate to prove you tried. Exemptions exist for family violence, urgency, and certain other situations. For property matters mediation isn't strictly mandatory, but courts strongly expect genuine pre-action efforts to resolve.")
 + f"""
<h2 id="short-answer">The short answer</h2>
<p>For parenting matters, mediation is effectively compulsory: under the {cite("family_law_act")}, you must make a genuine effort to resolve the dispute through family dispute resolution before applying to court, unless an exemption applies. For financial and property matters it isn't strictly mandatory, but the courts expect you to have made genuine attempts to settle before litigating.</p>
"""
 + inline_cta("Need to satisfy the pre-court mediation requirement? We're nationally accredited to help. Book a consultation.")
 + f"""
<h2 id="parenting">When it's required: parenting matters</h2>
<p>If you want to apply for a parenting order, you generally must first attend family dispute resolution. This requirement, set out in the {cite("ag_fdr")} framework, reflects a clear policy: children's matters should be resolved cooperatively wherever safe, not fought out in court. Only after a genuine attempt (or a valid exemption) can you file.</p>

<h2 id="section-60i">The Section 60I certificate</h2>
<p>A Section 60I certificate is the document that proves you attempted family dispute resolution. It's issued by an accredited practitioner and can state, among other things, that both parties attended and made a genuine effort, that one party refused to attend, or that the matter wasn't appropriate for mediation. You attach it to your court application. <a href="/section-60i-certificates/">See our Section 60I certificate service \u2192</a></p>
"""
 + callout("No certificate, no filing (usually)",
   "Without a Section 60I certificate or a valid exemption, the court will generally not accept a parenting application. Getting the mediation step right is therefore essential before any court process.")
 + """
<h2 id="property">What about property matters?</h2>
<p>For financial and property disputes, there's no Section 60I requirement \u2014 but don't assume mediation is optional. Courts impose pre-action procedures expecting parties to genuinely try to resolve matters first, including through negotiation or mediation, and can take a dim view (including on costs) of those who rush to litigate. In practice, <a href="/property-settlement-mediation/">property settlement mediation</a> is both expected and sensible.</p>

<h2 id="exemptions">Exemptions from the requirement</h2>
<p>You may be exempt from the family dispute resolution requirement where:</p>
<ul>
  <li>There is family violence or a risk of it</li>
  <li>There is child abuse or a risk of abuse</li>
  <li>The matter is urgent</li>
  <li>A party is unable to participate effectively (e.g. incapacity, or location)</li>
  <li>There has been a serious breach of an existing order</li>
</ul>
<p>If any of these apply, you may be able to go straight to court. <a href="/domestic-violence-and-family-law/">See family violence and family law \u2192</a></p>
"""
 + inline_cta("Unsure whether an exemption applies to you? We'll assess your situation honestly \u2014 book a consultation.")
 + """
<h2 id="refuses">What if my ex refuses?</h2>
<p>If your former partner won't attend, that doesn't trap you. The practitioner can issue a Section 60I certificate stating the other party refused or failed to attend, which lets you proceed to court. That said, refusal is often a negotiating posture rather than a final position \u2014 a skilled mediator can sometimes bring a reluctant party to the table. <a href="/what-is-mediation-in-family-law/">Learn how mediation actually works \u2192</a></p>

<h2 id="genuine">What counts as a genuine attempt?</h2>
<p>Turning up isn't enough on its own \u2014 you're expected to participate in good faith: to listen, to consider options, and to genuinely try to reach agreement. The good news is that genuine participation is also what makes mediation succeed, so the requirement and your interests point the same way. <a href="/preparing-for-mediation/">See how to prepare \u2192</a></p>
"""
 ,
 [("Is mediation compulsory before family court in Australia?",
   "For parenting matters, generally yes \u2014 you must attempt family dispute resolution and obtain a Section 60I certificate before filing, unless an exemption applies. For property matters it isn't strictly mandatory but is strongly expected."),
  ("What is a Section 60I certificate?",
   "A document issued by an accredited practitioner proving you attempted family dispute resolution. It's required to file most parenting applications in court."),
  ("What are the exemptions from compulsory mediation?",
   "Family violence or risk of it, child abuse or risk, urgency, inability to participate effectively, or a serious breach of an existing order."),
  ("What if my ex refuses to attend mediation?",
   "The practitioner can issue a certificate stating the other party refused, allowing you to proceed to court. A skilled mediator can sometimes bring a reluctant party to the table."),
  ("Do I need to attempt mediation for a property settlement?",
   "There's no Section 60I requirement for property, but courts expect genuine pre-action attempts to resolve, so mediation is both expected and sensible.")],
 [("section-60i-certificates","Section 60I Certificates"),
  ("what-is-mediation-in-family-law","What Is Mediation?"),
  ("family-law-mediation","Family Law Mediation"),
  ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("child-custody-mediation","Child Custody Mediation")],
 read_min=9)
print("is-family-law-mediation-compulsory built")

# ---- FATHERS' RIGHTS (absorbs 2) ----
post("fathers-rights",
 "Fathers' Rights After Separation in Australia (2026 Guide)",
 "Fathers' rights in Australia explained: the truth about 50/50 care, parental responsibility, the best-interests test, and how dads can secure meaningful time with their children.",
 "Parenting",
 "Fathers' Rights After Separation in Australia",
 "The law gives fathers and mothers equal standing \u2014 there's no built-in preference for either parent. What matters is the child's best interests. This guide clears up the myths about fathers' rights, explains parental responsibility, and shows how fathers can secure genuine, meaningful time with their children.",
 [("equal-footing","Do fathers have equal rights?"),
  ("responsibility","Parental responsibility explained"),
  ("5050","The truth about 50/50 care"),
  ("best-interests","What the court actually considers"),
  ("secure-time","How fathers can secure time"),
  ("alienation","When you're being shut out"),
  ("mediation","Why mediation helps fathers")],
 key_takeaway("Australian family law gives fathers and mothers equal standing \u2014 there is no legal preference for either parent. Decisions are based on the child's best interests, with a focus on a meaningful relationship with both parents balanced against safety. There's no automatic 50/50, but fathers have every right to seek substantial, meaningful time, and mediation is usually the most effective path.")
 + f"""
<h2 id="equal-footing">Do fathers have equal rights?</h2>
<p>Yes. Despite a persistent perception that the system favours mothers, the {cite("family_law_act")} contains no preference based on gender. Both parents begin on equal footing, and outcomes turn on the children's best interests and each parent's circumstances \u2014 not on whether you're the mother or the father.</p>
"""
 + inline_cta("Worried you won't get fair time with your kids? Talk to a mediator who'll help you build a strong case.")
 + """
<h2 id="responsibility">Parental responsibility explained</h2>
<p>"Parental responsibility" means the duties, powers and authority parents have in relation to their children \u2014 including making major long-term decisions about schooling, health and religion. Separation doesn't strip a father of parental responsibility. Both parents usually retain it and are expected to consult on major decisions, regardless of who the child primarily lives with.</p>

<h2 id="5050">The truth about 50/50 care</h2>
<p>There is no automatic right to equal time \u2014 for either parent. The law supports children maintaining a meaningful relationship with both parents where safe, but the actual split depends on the child's best interests and practical realities like work, distance, the child's age and routine. Equal time is one possible outcome, not a default. <a href="/child-custody-mediation/">See how care arrangements are decided \u2192</a></p>
"""
 + callout("Meaningful time matters more than a magic number",
   "Fixating on '50%' can distract from what counts: a stable, meaningful relationship with your children. Sometimes an arrangement that isn't a perfect even split serves the kids \u2014 and your relationship with them \u2014 better.")
 + f"""
<h2 id="best-interests">What the court actually considers</h2>
<p>Under the best-interests test, the court weighs factors including the benefit of a meaningful relationship with both parents, the need to protect the child from harm, the child's views (age-appropriate), each parent's capacity to provide for the child's needs, and the practical circumstances. Safety always takes priority where it conflicts with contact. The {cite("frc")} provides useful guidance for parents navigating this.</p>

<h2 id="secure-time">How fathers can secure meaningful time</h2>
<ol>
  <li><strong>Stay involved</strong> \u2014 consistent, reliable involvement in your children's lives matters.</li>
  <li><strong>Propose a workable plan</strong> \u2014 a realistic <a href="/parenting-plans-guide/">parenting plan</a> shows you're focused on the children.</li>
  <li><strong>Keep conflict away from the kids</strong> \u2014 courts and mediators notice who keeps things child-focused.</li>
  <li><strong>Document your involvement</strong> \u2014 school events, medical appointments, day-to-day care.</li>
  <li><strong>Use mediation</strong> \u2014 it's faster, cheaper, and lets you negotiate directly rather than leaving it to a judge.</li>
</ol>
"""
 + inline_cta("Ready to put a fair parenting proposal on the table? We'll help you do it the right way. Book today.")
 + """
<h2 id="alienation">When you're being shut out</h2>
<p>If your ex is withholding the children or undermining your relationship with them, that's serious \u2014 and the law takes a dim view of a parent who frustrates the children's relationship with the other parent without good reason. Document what's happening, avoid retaliating, and seek help early. Mediation can often re-open communication; where it can't, the court can make and enforce orders. <a href="/domestic-violence-and-family-law/">If there are safety allegations, read this \u2192</a></p>

<h2 id="mediation">Why mediation helps fathers</h2>
<p>Mediation is frequently a father's best friend. Rather than leaving your time with your children to a judge's limited hearing, it lets you negotiate a meaningful arrangement directly, keeps costs down, and \u2014 by keeping things constructive \u2014 builds the kind of co-parenting relationship that serves your children for years. <a href="/parenting-plan-mediation/">See parenting plan mediation \u2192</a></p>
"""
 ,
 [("Do fathers have equal rights in Australia?",
   "Yes. The law contains no preference based on gender. Both parents start equal, and outcomes turn on the child's best interests and each parent's circumstances."),
  ("Is there an automatic right to 50/50 care?",
   "No. There's no automatic equal-time right for either parent. The arrangement depends on the child's best interests and practical factors like work, distance and the child's age."),
  ("Does separation remove a father's parental responsibility?",
   "No. Both parents usually retain parental responsibility after separation and are expected to consult on major long-term decisions, regardless of who the child lives with."),
  ("What can I do if my ex won't let me see the kids?",
   "Document what's happening, keep conflict away from the children, and seek help early. Mediation can re-open communication; if it can't, courts can make and enforce orders."),
  ("How can a father get more time with his children?",
   "Stay consistently involved, propose a realistic parenting plan, keep things child-focused, document your involvement, and use mediation to negotiate directly.")],
 [("child-custody-mediation","Child Custody Mediation"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("parenting-plan-mediation","Parenting Plan Mediation"),
  ("mothers-rights","Mothers' Rights"),
  ("grandparents-rights","Grandparents' Rights"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=9)
print("fathers-rights built")

# ---- SUPERANNUATION & DIVORCE (absorbs 2) ----
post("superannuation-and-divorce",
 "Superannuation and Divorce in Australia: How Splitting Works (2026)",
 "How is superannuation split in a divorce in Australia? Super is treated as property and can be divided. Learn how super splitting works, valuation, and how to do it without court.",
 "Property &amp; finances",
 "Superannuation and Divorce: <em>How Splitting Works</em>",
 "Superannuation is treated as property under Australian family law, which means it can be split between partners when a relationship ends. For many couples it's one of the largest assets \u2014 and overlooking it is a costly mistake. Here's how super splitting works and how to do it without going to court.",
 [("is-property","Is superannuation property?"),
  ("how-split","How does super splitting work?"),
  ("valuation","How super is valued"),
  ("why-matters","Why it matters \u2014 especially for carers"),
  ("self-managed","Self-managed super funds"),
  ("formalise","How to formalise a super split")],
 key_takeaway("Superannuation is treated as property under the Family Law Act and can be split between partners on separation. A super split doesn't convert to cash \u2014 it stays in super \u2014 but it rebalances retirement savings. Splitting is formalised through consent orders or a binding financial agreement. It's especially important where one partner has a much smaller balance from time out of the workforce.")
 + f"""
<h2 id="is-property">Is superannuation property?</h2>
<p>Yes. Under the {cite("family_law_act")}, superannuation is treated as property that can be divided as part of a settlement \u2014 even though you generally can't access it until retirement. This is one of the most under-appreciated parts of a property settlement, and missing it can leave one partner significantly worse off in retirement.</p>
"""
 + inline_cta("Not sure how your super (or your ex's) factors into the split? Get clarity in a fixed-fee consultation.")
 + """
<h2 id="how-split">How does super splitting work?</h2>
<p>A superannuation split reallocates part of one partner's super to the other. Importantly, it doesn't turn super into cash \u2014 the split amount is transferred into the receiving partner's super (or sometimes a new account) and remains subject to normal preservation rules until retirement. It's a rebalancing of retirement savings, not an early payout. The split is part of the overall <a href="/property-settlement-after-separation/">property settlement</a>, considered alongside the rest of the asset pool.</p>

<h2 id="valuation">How super is valued</h2>
<p>Accumulation accounts are usually straightforward \u2014 the balance is the value. Defined benefit schemes (common in government and some older funds) are more complex and often need an actuarial valuation, because their value isn't simply the current balance. Getting an accurate value matters, since it affects the whole division. Full disclosure of super interests is part of each party's <a href="/property-settlement-after-separation/">duty of disclosure</a>.</p>
"""
 + callout("Don't trade away super too cheaply",
   "A common mistake is one partner keeping the house while the other 'keeps their super' \u2014 without properly comparing values. Super is real wealth. Weigh it carefully against other assets rather than treating it as an afterthought.")
 + """
<h2 id="why-matters">Why it matters \u2014 especially for carers</h2>
<p>Super splitting is particularly important where one partner has a much smaller balance because they reduced paid work to raise children or run the household. Without a split, that partner can be left with far less retirement security despite years of non-financial contribution. The law recognises this, and a fair settlement often includes a super split to address it. <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">See how contributions are assessed \u2192</a></p>

<h2 id="self-managed">Self-managed super funds</h2>
<p>Self-managed super funds (SMSFs) add complexity, especially where the fund holds property or both partners are members and trustees. Splitting an SMSF requires care to comply with <a href="https://www.ato.gov.au/individuals-and-families/super" target="_blank" rel="noopener">superannuation law</a> and to deal with any illiquid assets. This is an area where professional guidance and a negotiated, mediated outcome are especially valuable. <a href="/financial-agreements-mediation/">See financial agreements mediation \u2192</a></p>
"""
 + inline_cta("Complex super, or a self-managed fund in the mix? We'll help you divide it fairly and correctly.")
 + """
<h2 id="formalise">How to formalise a super split</h2>
<p>A super split must be formalised \u2014 you can't just agree it informally. It's done through <a href="/consent-orders-explained/">consent orders</a> or a <a href="/binding-financial-agreements-guide/">binding financial agreement</a>, which the super fund then implements. Reaching the agreement through <a href="/property-settlement-mediation/">mediation</a> first is the fastest, least costly route \u2014 then you simply formalise what you've agreed.</p>
"""
 ,
 [("Is superannuation split in a divorce?",
   "Yes. Super is treated as property under the Family Law Act and can be split between partners as part of a settlement, though it remains in super rather than becoming cash."),
  ("Does a super split become cash?",
   "No. The split amount is transferred into the receiving partner's super and remains subject to normal preservation rules until retirement. It rebalances retirement savings."),
  ("How is superannuation valued in a divorce?",
   "Accumulation accounts are usually valued at their balance. Defined benefit schemes are more complex and often need an actuarial valuation."),
  ("Why is super splitting important for stay-at-home parents?",
   "Because a partner who reduced paid work to care for children often has a much smaller balance. A super split addresses that imbalance and protects their retirement security."),
  ("How do I formalise a superannuation split?",
   "Through consent orders or a binding financial agreement, which the super fund then implements. Reaching the agreement via mediation first is the fastest route.")],
 [("property-settlement-after-separation","Property Settlement"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("binding-financial-agreements-guide","Binding Financial Agreements"),
  ("financial-agreements-mediation","Financial Agreements Mediation")],
 read_min=9)
print("superannuation-and-divorce built")

# ---- HIGH-CONFLICT MEDIATION (absorbs 2) ----
post("high-conflict-mediation",
 "High-Conflict Family Law Mediation: Does It Work? (2026)",
 "Can mediation work in high-conflict separations? Yes \u2014 with the right techniques. How shuttle mediation, structure and skilled mediators resolve even bitter disputes without court.",
 "High-conflict",
 "High-Conflict Family Law Mediation: <em>Does It Work?</em>",
 "When emotions run high and trust is gone, court can feel like the only option \u2014 but it's often the worst one. High-conflict mediation, run by an experienced mediator using techniques like shuttle mediation, resolves even bitter disputes faster, cheaper and with less damage than litigation. Here's how.",
 [("can-work","Can mediation work in high conflict?"),
  ("shuttle","Shuttle mediation: staying apart"),
  ("techniques","Techniques that defuse conflict"),
  ("vs-court","Why court usually makes it worse"),
  ("prepare","How to prepare for a tough mediation"),
  ("when-not","When mediation isn't suitable")],
 key_takeaway("High-conflict mediation absolutely can work \u2014 often better than court. Experienced mediators use structure, firm ground rules and shuttle techniques (keeping parties in separate rooms) to neutralise hostility and keep the focus on resolution. It's faster, cheaper and less damaging than litigation. The exception is where family violence or a genuine safety risk makes mediation unsafe.")
 + """
<h2 id="can-work">Can mediation work in high conflict?</h2>
<p>It's a fair question \u2014 if you and your ex can barely be in the same room, how can you negotiate? The answer is that high-conflict mediation is a recognised, structured discipline, not a hopeful chat. An experienced mediator expects hostility and is trained to manage it: setting ground rules, controlling the pace, and keeping the conversation anchored to the issues rather than the grievances. Counterintuitively, the structure of mediation often contains conflict better than the adversarial free-for-all of litigation.</p>
"""
 + inline_cta("Think your situation is too heated for mediation? It's probably not. Talk to a high-conflict specialist.")
 + """
<h2 id="shuttle">Shuttle mediation: staying apart</h2>
<p>The key tool for high-conflict matters is shuttle mediation. You and your ex are placed in separate rooms \u2014 or separate video calls \u2014 and the mediator moves between you, carrying offers and information back and forth. You never have to face each other directly. This removes intimidation, lowers the emotional temperature, and lets each person think clearly. It's remarkably effective even where the parties genuinely cannot be together. <a href="/mediation-with-a-narcissist/">See mediation with a controlling ex \u2192</a></p>

<h2 id="techniques">Techniques that defuse conflict</h2>
<ul>
  <li><strong>Firm ground rules</strong> \u2014 agreed at the outset and enforced throughout.</li>
  <li><strong>Reality-checking</strong> \u2014 anchoring discussion to documents and facts, not accusations.</li>
  <li><strong>Reframing</strong> \u2014 turning positions ("I want the house") into interests ("I need stability for the kids").</li>
  <li><strong>Caucusing</strong> \u2014 private sessions with each party to explore options candidly.</li>
  <li><strong>Future focus</strong> \u2014 steering away from re-litigating the past toward workable arrangements.</li>
</ul>
"""
 + callout("Emotion is expected, not a dealbreaker",
   "A good high-conflict mediator doesn't need you to be calm and reasonable at all times. Managing strong emotion is part of the job \u2014 what matters is willingness to reach a resolution.")
 + f"""
<h2 id="vs-court">Why court usually makes it worse</h2>
<p>Litigation is adversarial by design \u2014 it pits you against each other and can reward whoever fights hardest and longest. For high-conflict personalities, it offers a public stage and endless opportunities to prolong the battle. It's also slow and ruinously expensive. The {cite("fcfcoa")} itself encourages dispute resolution over contested hearings wherever possible. Mediation, by contrast, drains the conflict of its oxygen and gets to an outcome faster. <a href="/mediate-or-litigate/">Compare mediation and court \u2192</a></p>

<h2 id="prepare">How to prepare for a tough mediation</h2>
<p>Preparation makes all the difference: know your goals and your bottom lines in advance, gather your documents, decide to stay factual rather than reactive, and consider support from a <a href="/divorce-counselling/">counsellor</a> beforehand. Going in clear-headed denies a combative ex the reactions they may be seeking. <a href="/preparing-for-mediation/">See how to prepare \u2192</a></p>
"""
 + inline_cta("Preparation is everything in a high-conflict mediation. We'll get you ready. Book a confidential consultation.")
 + """
<h2 id="when-not">When mediation isn't suitable</h2>
<p>Honesty matters: high conflict alone doesn't rule out mediation, but genuine safety risk does. Where there is family violence, an unmanageable power imbalance, or a real risk to safety, mediation may not be appropriate, and exemptions exist. If you're in immediate danger, contact emergency services or <a href="https://www.1800respect.org.au/" target="_blank" rel="noopener">1800RESPECT</a>. If you're unsure whether your situation is safe to mediate, tell us and we'll give you an honest assessment. <a href="/domestic-violence-and-family-law/">See domestic violence and family law \u2192</a></p>
"""
 ,
 [("Can mediation work in a high-conflict separation?",
   "Yes, often better than court. Experienced mediators use structure, ground rules and shuttle techniques to manage hostility and keep the focus on resolution."),
  ("What is shuttle mediation?",
   "A format where you and your ex stay in separate rooms (or video calls) and the mediator moves between you. You never face each other directly \u2014 ideal for high conflict."),
  ("Isn't court better when there's a lot of conflict?",
   "Usually not. Court is adversarial and can reward prolonged fighting, while being slow and expensive. Mediation defuses conflict and resolves matters faster."),
  ("How do I prepare for a high-conflict mediation?",
   "Know your goals and limits, gather documents, commit to staying factual rather than reactive, and consider counselling beforehand to build resilience."),
  ("When is high-conflict mediation not appropriate?",
   "Where there's family violence, an unmanageable power imbalance, or a genuine safety risk. Exemptions apply, and if you're in danger you should contact emergency services.")],
 [("mediation-with-a-narcissist","Mediation With a Narcissist"),
  ("mediate-or-litigate","Mediate or Litigate?"),
  ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("family-law-mediation","Family Law Mediation"),
  ("divorce-counselling","Divorce Counselling")],
 read_min=9)
print("high-conflict-mediation built")
