"""gen_blog_batch31.py — two new cornerstones.

interim-parenting-orders-australia     — urgent orders, the Recovery Order process,
                                         how interim differs from final, and mediation first
supervised-visitation-australia        — what supervised contact looks like, who provides it,
                                         Children's Contact Services, and moving to unsupervised

Facts checked against the official pages cited inline (10 Nov 2026).
General information only, not legal advice.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ─────────────────────────────────────────────────────────────────────────────
# 1. Interim parenting orders in Australia
# ─────────────────────────────────────────────────────────────────────────────
post(
    "interim-parenting-orders-australia",
    "Interim Parenting Orders in Australia",
    "What interim parenting orders are, when courts grant them, how to apply, costs, timeframes, and why mediation is usually faster.",
    "Parenting",
    "Interim parenting orders <em>in Australia</em>",
    ("When parents separate and cannot agree on where the children will live or how much time they spend "
     "with each parent, an interim parenting order can set temporary arrangements while the case works its "
     "way through the family court system. This guide explains what interim orders are, when they are granted, "
     "how to apply, and why mediation is usually a faster and less costly first step."),
    [("short-answer", "What is an interim parenting order?"),
     ("when-granted", "When courts grant interim orders"),
     ("how-to-apply", "How to apply for interim parenting orders"),
     ("what-court-considers", "What the court considers"),
     ("costs-timeframes", "Costs and timeframes"),
     ("recovery-orders", "Recovery orders: when a child is withheld"),
     ("interim-vs-final", "Interim vs final parenting orders"),
     ("mediation-first", "Why mediation is usually the better first step")],
    key_takeaway("An interim parenting order is a temporary court order that sets out where children live and how "
                 "they spend time with each parent while the case is decided. Courts grant them when there is urgency "
                 "or a risk of harm, not simply because parents disagree. In most cases, mediation and a parenting "
                 "plan or consent orders resolve the dispute faster and at a fraction of the cost.")
    + f"""
<h2 id="short-answer">What is an interim parenting order?</h2>
<p>An interim parenting order is a temporary order made by the {cite('fcfcoa')} that sets out parenting arrangements — where children live, the time they spend with each parent, and sometimes communication arrangements — until the case reaches a final hearing or the parents reach agreement.</p>
<p>The word "interim" simply means "in the meantime." The order is not a preview of the final result. It is designed to keep children safe and to maintain a reasonable status quo while the court considers the full evidence. An interim order can be varied or replaced at any time if circumstances change.</p>
<p>Most interim hearings are short, often one to two hours, and the judge or magistrate works with limited evidence — usually affidavits rather than cross-examination. That means the court is cautious: it leans towards preserving the arrangements the children already know unless there is a good reason not to.</p>
"""
    + inline_cta("Not sure whether you need a court order or just a clear agreement? A free consultation can help you work out the right first step.")
    + f"""
<h2 id="when-granted">When courts grant interim orders</h2>
<p>The court does not grant interim parenting orders simply because one parent asks. There generally needs to be a reason why the matter cannot wait for a final hearing or be resolved by agreement. Common situations include:</p>
<ul>
<li><strong>Safety concerns:</strong> allegations of family violence, drug or alcohol misuse, or neglect that put a child at risk.</li>
<li><strong>One parent withholding the child:</strong> refusing to return a child after a visit, or preventing contact altogether.</li>
<li><strong>Relocation:</strong> a parent planning to move interstate or overseas with the children before a final hearing.</li>
<li><strong>No existing arrangements:</strong> parents have just separated and cannot agree on basic logistics.</li>
<li><strong>Breach of an existing order:</strong> one parent is not following a final or earlier interim order.</li>
</ul>
<p>Where there is no urgency and the children are safe, the court will usually expect the parents to try {cite('fcfcoa_fdr')} before listing the case for an interim hearing.</p>
"""
    + inline_cta("If your situation isn't urgent, mediation can often resolve parenting arrangements in a single session — without the stress and cost of court.")
    + f"""
<h2 id="how-to-apply">How to apply for interim parenting orders</h2>
<p>The process depends on whether you already have a case before the {cite('fcfcoa')} or are starting fresh.</p>
<figure class="tbl"><table><caption>Steps to apply for interim parenting orders</caption>
<thead><tr><th>Step</th><th>What's involved</th><th>Typical timeframe</th></tr></thead>
<tbody>
<tr><td>1. Obtain a Section 60I certificate</td><td>Attend family dispute resolution or qualify for an exemption (e.g. family violence, urgency)</td><td>1–6 weeks (or immediate if exempt)</td></tr>
<tr><td>2. File an Initiating Application</td><td>File via the {cite('comcourts_portal')} with a supporting affidavit setting out the facts</td><td>Same day</td></tr>
<tr><td>3. File an Application in a Case (if existing)</td><td>If proceedings already exist, file an interim application within the existing case</td><td>Same day</td></tr>
<tr><td>4. Serve the other parent</td><td>The other parent must be served and given time to file a response affidavit</td><td>Court rules set the notice period</td></tr>
<tr><td>5. Attend the interim hearing</td><td>Both parties present their case, usually on affidavit evidence only</td><td>Listed 4–8 weeks after filing (varies by registry)</td></tr>
</tbody></table></figure>
<p>In genuinely urgent cases — for example, where a child is at immediate risk — the court can hear an application on the same day or the next, sometimes without notice to the other parent. These are rare and require strong evidence of urgency.</p>
"""
    + inline_cta("Filing feels overwhelming? Many parents find mediation resolves the dispute before papers need to be filed.")
    + f"""
<h2 id="what-court-considers">What the court considers</h2>
<p>The court decides interim parenting orders using the same overarching principle as final orders: the best interests of the child under the {cite('family_law_act')}. In practice, the court pays particular attention to:</p>
<ul>
<li><strong>The child's safety:</strong> Any risk of family violence, abuse or neglect is the court's primary concern. The {cite('fcfcoa_safety_risk')} page explains how this is assessed.</li>
<li><strong>The status quo:</strong> Where has the child been living? What routine are they used to? Courts are reluctant to disrupt a child's day-to-day life unless there is a strong reason.</li>
<li><strong>The child's relationship with each parent:</strong> Maintaining meaningful time with both parents matters, unless safety prevents it.</li>
<li><strong>Practical arrangements:</strong> School proximity, each parent's work schedule, and the child's existing commitments.</li>
<li><strong>Any existing agreements or orders:</strong> A <a href="/parenting-plans-guide/">parenting plan</a> or previous court order carries weight.</li>
</ul>
<p>The court is not hearing the full case at this stage. It works with limited evidence and makes the best temporary decision it can. An interim order does not prejudice the final outcome, although in practice the status quo it creates can be difficult to shift later.</p>
"""
    + inline_cta("Want to shape the outcome rather than leave it to a judge? Mediation gives both parents a voice in the decision.")
    + f"""
<h2 id="costs-timeframes">Costs and timeframes</h2>
<p>Interim hearings are shorter than final hearings, but they are not cheap. Typical costs and timeframes include:</p>
<figure class="tbl"><table><caption>Interim parenting order costs and timeframes (indicative)</caption>
<thead><tr><th>Item</th><th>Indicative cost</th><th>Typical timeframe</th></tr></thead>
<tbody>
<tr><td>Filing fee (Initiating Application)</td><td>$390 (reduced fee available)</td><td>Same day</td></tr>
<tr><td>Lawyer preparation (affidavits, submissions)</td><td>$3,000–$8,000</td><td>1–3 weeks</td></tr>
<tr><td>Barrister for hearing (if briefed)</td><td>$2,500–$6,000</td><td>Hearing day</td></tr>
<tr><td>Waiting time for hearing date</td><td>—</td><td>4–12 weeks depending on registry</td></tr>
<tr><td>Total estimated legal costs per party</td><td>$5,000–$15,000</td><td>—</td></tr>
</tbody></table></figure>
<p class="source-note">Source: {cite('fcfcoa_fees')} for filing fees. Legal costs are indicative only and vary by location and complexity. Reduced fees apply for financial hardship.</p>
<p>Compare that with <a href="/how-much-does-mediation-cost/">mediation</a>, which typically costs $1,500–$4,000 total and can be arranged within one to three weeks. Even where mediation does not fully resolve the dispute, narrowing the issues before an interim hearing saves time and money.</p>
"""
    + inline_cta("Spending $10,000 on an interim hearing? For a fraction of that, mediation could resolve the dispute entirely.")
    + f"""
<h2 id="recovery-orders">Recovery orders: when a child is withheld</h2>
<p>If a parent is refusing to return a child after agreed time, or is withholding a child from the other parent altogether, the court can make a recovery order under the {cite('family_law_act')} (section 67Q). A recovery order directs the Australian Federal Police or state police to find the child and return them to the person named in the order.</p>
<p>Recovery orders are serious. They are usually made urgently and can be applied for at the same time as interim parenting orders. The court needs to be satisfied that the child has been taken or retained, and that making the order is in the child's best interests.</p>
<p>If a child has been taken overseas, the situation involves international law. Read our guide on <a href="/travelling-overseas-with-children-after-separation/">travelling overseas with children after separation</a> for the Hague Convention process and the AFP Family Law Watchlist.</p>
"""
    + inline_cta("Ex withholding contact but the situation isn't dangerous? Mediation can often restore arrangements faster than a court application.")
    + f"""
<h2 id="interim-vs-final">Interim vs final parenting orders</h2>
<p>The difference matters more than most parents realise:</p>
<figure class="tbl"><table><caption>Interim vs final parenting orders</caption>
<thead><tr><th>Feature</th><th>Interim order</th><th>Final order</th></tr></thead>
<tbody>
<tr><td>Duration</td><td>Temporary — until final hearing or agreement</td><td>Ongoing until the child turns 18 (or varied)</td></tr>
<tr><td>Evidence</td><td>Affidavits only, limited hearing time</td><td>Full evidence, cross-examination, family report</td></tr>
<tr><td>Purpose</td><td>Preserve safety and status quo</td><td>Determine the child's best long-term interests</td></tr>
<tr><td>Effect on final result</td><td>Legally none — but the status quo it creates can carry practical weight</td><td>Binding and enforceable</td></tr>
<tr><td>Cost per party</td><td>$5,000–$15,000</td><td>$20,000–$100,000+</td></tr>
<tr><td>Time to obtain</td><td>4–12 weeks from filing</td><td>12–24 months (or longer)</td></tr>
</tbody></table></figure>
<p>Because interim orders set the status quo that courts are reluctant to change, the practical effect is often greater than the legal theory suggests. Getting the interim arrangement right matters, whether through the court or by agreement.</p>
"""
    + inline_cta("An agreement reached in mediation can become consent orders the same week — no interim hearing needed.")
    + f"""
<h2 id="mediation-first">Why mediation is usually the better first step</h2>
<p>Unless there is a genuine safety risk or an emergency, <a href="/child-custody-mediation/">parenting mediation</a> is almost always worth trying before applying for interim orders. The reasons are practical:</p>
<ul>
<li><strong>Speed:</strong> Mediation can be arranged in days. An interim hearing takes weeks or months.</li>
<li><strong>Cost:</strong> A mediation session costs a fraction of an interim hearing. See our <a href="/how-much-does-mediation-cost/">mediation costs guide</a>.</li>
<li><strong>Control:</strong> Parents decide the arrangements, rather than a judge who has seen one affidavit from each side.</li>
<li><strong>Enforceability:</strong> An agreement reached in mediation can be turned into <a href="/consent-orders-explained/">consent orders</a> and is then just as enforceable as a court-imposed order.</li>
<li><strong>Relationship:</strong> Mediation preserves the co-parenting relationship. Contested court applications tend to damage it.</li>
</ul>
<p>Where {cite('fcfcoa_fdr')} is required, attempting mediation also fulfils the <a href="/section-60i-certificate-guide/">Section 60I certificate</a> requirement. If mediation does not resolve everything, narrowing the issues still makes any court process shorter and cheaper.</p>
<p><strong>Safety first.</strong> If there is family violence, threats, or a risk to your child's safety, mediation may not be appropriate and you may be exempt from {cite('fcfcoa_fdr')}. Call <strong>000</strong> in an emergency, or 1800RESPECT on <strong>1800 737 732</strong> ({cite('respect_1800')}). Read our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>
"""
    + inline_cta("Ready to resolve parenting arrangements without court? Book a free consultation with Mediations Australia."),
    [("What is an interim parenting order in Australia?",
      "An interim parenting order is a temporary court order that sets out where children live and how they spend time with each parent while the case is being decided. It is made by the Federal Circuit and Family Court and stays in place until a final order is made or the parents reach agreement."),
     ("How long does it take to get an interim parenting order?",
      "Typically 4 to 12 weeks from filing, depending on the court registry and how busy the list is. In genuinely urgent cases involving safety risks, the court can hear applications within days or even on the same day."),
     ("How much does an interim parenting order cost?",
      "The court filing fee is around $390, but total legal costs including lawyer preparation and the hearing typically run between $5,000 and $15,000 per party. Mediation costs a fraction of this and can often resolve the dispute without court."),
     ("Can I get an interim parenting order without mediation?",
      "In some cases, yes. Exemptions from family dispute resolution apply where there is family violence, child abuse, urgency, or where one party is unable to participate. Otherwise, a Section 60I certificate showing that mediation was attempted or is not appropriate is generally required before filing."),
     ("Do interim parenting orders become permanent?",
      "Not automatically. An interim order is legally temporary and does not prejudice the final outcome. However, the status quo it creates can carry practical weight at a final hearing, so getting the arrangements right from the start matters."),
     ("Can mediation replace an interim parenting order?",
      "Often, yes. If there is no safety emergency, parents can agree arrangements in mediation and have them made into consent orders, which are just as enforceable as court-imposed orders. This is typically faster, cheaper, and less damaging to the co-parenting relationship.")],
    [("child-custody-mediation", "Child custody mediation"),
     ("parenting-plans-guide", "Parenting plans in Australia"),
     ("consent-orders-explained", "Consent orders explained"),
     ("section-60i-certificate-guide", "Section 60I certificate guide"),
     ("how-to-change-parenting-orders", "How to change parenting orders"),
     ("family-court-process-2026", "The family court process (2026)")],
    read_min=9,
)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Supervised visitation in Australia
# ─────────────────────────────────────────────────────────────────────────────
post(
    "supervised-visitation-australia",
    "Supervised Visitation in Australia",
    "How supervised contact works, when courts order it, Children's Contact Services, costs, and moving to unsupervised time.",
    "Parenting",
    "Supervised visitation <em>in Australia</em>",
    ("When there are serious concerns about a child's safety during time with a parent — family violence, "
     "substance misuse, mental health issues or a long absence — a court may order supervised visitation. "
     "This guide explains what supervised contact looks like in practice, who provides it, what it costs, "
     "and how parents move from supervised to unsupervised time."),
    [("short-answer", "What is supervised visitation?"),
     ("when-ordered", "When a court orders supervised contact"),
     ("types", "Types of supervision"),
     ("contact-services", "Children's Contact Services"),
     ("costs", "Costs of supervised visitation"),
     ("what-happens", "What happens during a supervised visit"),
     ("moving-unsupervised", "Moving from supervised to unsupervised time"),
     ("mediation-role", "How mediation helps with supervised contact disputes")],
    key_takeaway("Supervised visitation means a child spends time with a parent while a third person watches to keep "
                 "the child safe. Courts order it when there are genuine safety concerns — not as a punishment. Most "
                 "supervised arrangements are temporary, and parents can work towards unsupervised time by addressing "
                 "the concerns that led to the order. Mediation can help parents agree on supervision arrangements, "
                 "and on the steps needed to move beyond them.")
    + f"""
<h2 id="short-answer">What is supervised visitation?</h2>
<p>Supervised visitation — called "supervised contact" or "supervised time" in Australian family law — means a child spends time with a parent while a third person is present to ensure the child's safety and wellbeing. The supervisor may be a professional at a contact centre, or an agreed family member or friend.</p>
<p>It is not a normal part of separated parenting. Courts order it only where there is a genuine concern about a child's safety during unsupervised time with a parent. Common reasons include allegations of family violence, substance misuse, serious mental health concerns, or situations where a parent and child need to rebuild a relationship after a long absence.</p>
<p>The key point parents often miss: supervised contact is usually a temporary step, not a permanent arrangement. It is designed to keep the child connected with the parent while the concerns are addressed. The goal, in most cases, is to move towards unsupervised time as soon as it is safe to do so.</p>
"""
    + inline_cta("Facing a supervised contact arrangement? A mediator can help both parents agree on the safeguards and the pathway forward.")
    + f"""
<h2 id="when-ordered">When a court orders supervised contact</h2>
<p>The {cite('fcfcoa')} can order supervised contact as part of interim or final parenting orders. The court's primary concern is always the best interests of the child under the {cite('family_law_act')}, with the child's safety as the first consideration.</p>
<p>Common situations where supervised contact is ordered include:</p>
<figure class="tbl"><table><caption>Common reasons for supervised visitation orders</caption>
<thead><tr><th>Concern</th><th>What the court looks at</th><th>Typical supervision</th></tr></thead>
<tbody>
<tr><td>Family violence</td><td>History and risk of physical, emotional or psychological harm to the child or the other parent</td><td>Professional contact centre</td></tr>
<tr><td>Substance misuse</td><td>Current drug or alcohol use, treatment history, <a href="/court-ordered-drug-and-alcohol-testing/">drug and alcohol testing</a> results</td><td>Professional or trusted family member</td></tr>
<tr><td>Mental health</td><td>Untreated conditions that affect parenting capacity</td><td>Varies with severity</td></tr>
<tr><td>Reintroduction</td><td>Parent has had no contact for months or years; child needs gradual reconnection</td><td>Often starts professional, moves to informal</td></tr>
<tr><td>Risk of abduction</td><td>Credible concern a parent may take the child overseas or interstate</td><td>Professional contact centre with security protocols</td></tr>
<tr><td>Child's wishes</td><td>An older child is fearful or reluctant; supervision eases the transition</td><td>Often a trusted third party</td></tr>
</tbody></table></figure>
<p>The court does not order supervision lightly. It restricts the parent-child relationship and is resource-intensive. Where the risk can be managed another way — for example, through conditions on an order, drug testing, or counselling — the court may prefer that less restrictive approach.</p>
"""
    + inline_cta("Concerned about safety but unsure whether supervision is needed? Mediation can identify the right safeguards for your family.")
    + f"""
<h2 id="types">Types of supervision</h2>
<p>Not all supervised contact looks the same. The level of supervision is matched to the level of risk:</p>
<ul>
<li><strong>Professional supervision at a Children's Contact Service (CCS):</strong> A trained worker observes the visit in a purpose-built centre. This is the highest level of supervision and is used where safety concerns are most serious.</li>
<li><strong>Professional supervision in the community:</strong> A qualified supervisor accompanies the parent and child to a park, café or other venue. This is less formal than a centre visit and suits cases where the risk is moderate.</li>
<li><strong>Informal supervision by a nominated person:</strong> A family member, grandparent or family friend agreed by both parents (or named in orders) supervises the visit. This works where the risk is lower and both parents trust the supervisor.</li>
<li><strong>Supported changeover:</strong> The child is handed over at a contact centre or other neutral venue, with staff present, but the actual time with the parent is unsupervised. This addresses changeover conflict rather than visit safety.</li>
</ul>
<p>The type of supervision is usually set out in the court order or parenting agreement. Changing it — for example, moving from a contact centre to informal supervision — generally requires either a new agreement or a variation of the order.</p>
"""
    + inline_cta("Both parents agree on supervision but not the details? A mediator can help you design the right arrangement.")
    + f"""
<h2 id="contact-services">Children's Contact Services</h2>
<p>Children's Contact Services (CCS) are centres funded or approved to provide supervised visits and supported changeovers. They are staffed by trained workers and are specifically designed for families where safety is a concern.</p>
<p>The {cite('ag_fdr')} outlines the government's role in funding family dispute resolution and related services, including Children's Contact Services. The {cite('frc')} website helps families locate their nearest service.</p>
<p>Key points about CCS:</p>
<ul>
<li><strong>Availability:</strong> There are CCS centres in most capital cities and many regional areas, but waitlists can be long — sometimes three to six months in busy areas.</li>
<li><strong>Session length:</strong> Visits are typically one to three hours, depending on the child's age and the centre's capacity.</li>
<li><strong>Observations:</strong> Staff observe and may take notes. In some cases, their observations can be used in court proceedings.</li>
<li><strong>Rules:</strong> Centres have strict rules — no photography, no gifts without approval, no discussing the other parent or the court case with the child.</li>
<li><strong>Not open-ended:</strong> Most CCS have time limits on how long a family can use the service (often 12 months). The expectation is that families work towards a longer-term arrangement.</li>
</ul>
<p>If a CCS has a long waitlist, private supervised contact providers may be an option, though they are more expensive. Your lawyer or mediator can help identify options in your area.</p>
"""
    + inline_cta("Waitlisted for a contact centre? Mediation can help you agree interim informal supervision while you wait.")
    + f"""
<h2 id="costs">Costs of supervised visitation</h2>
<p>The cost depends on who provides the supervision:</p>
<figure class="tbl"><table><caption>Supervised visitation costs (indicative)</caption>
<thead><tr><th>Type of supervision</th><th>Indicative cost per visit</th><th>Who pays?</th></tr></thead>
<tbody>
<tr><td>Government-funded CCS</td><td>Free or low-cost (often $10–$30 per visit)</td><td>Usually the visiting parent</td></tr>
<tr><td>Private contact centre</td><td>$150–$400 per visit</td><td>Usually the visiting parent, or shared by agreement</td></tr>
<tr><td>Private professional supervisor</td><td>$80–$200 per hour</td><td>As agreed or ordered</td></tr>
<tr><td>Informal supervisor (family/friend)</td><td>Free</td><td>N/A</td></tr>
</tbody></table></figure>
<p>Court orders sometimes specify who pays for supervision. Where they do not, it usually falls to the parent whose conduct gave rise to the need for it, but this is negotiable. If cost is a barrier to contact, raise it — the court wants children to see both parents, and creative solutions (such as moving to informal supervision sooner) are common.</p>
"""
    + inline_cta("Supervision costs adding up? Mediation can help you agree a faster pathway to unsupervised time.")
    + f"""
<h2 id="what-happens">What happens during a supervised visit</h2>
<p>A typical supervised visit at a contact centre follows a structured process:</p>
<ul>
<li><strong>Staggered arrival:</strong> Parents arrive and leave at different times so they do not cross paths. The child is brought by the resident parent and handed to staff, who then introduce the visiting parent.</li>
<li><strong>The visit itself:</strong> The parent and child spend time together in a supervised play area. Activities might include drawing, board games, reading, or watching a film — whatever is age-appropriate and natural.</li>
<li><strong>Observation:</strong> A staff member is present throughout and may take notes on the parent-child interaction, the child's mood, and anything of concern.</li>
<li><strong>Ending the visit:</strong> Staff manage the handover back. The visiting parent leaves first, and the resident parent collects the child once the other parent has gone.</li>
</ul>
<p>The experience is designed to feel as natural as possible for the child. Good contact centres have toys, books and outdoor spaces, and staff are trained to put children at ease. For the visiting parent, it can feel awkward and artificial, but the aim is to maintain and strengthen the bond with the child while ensuring safety.</p>
"""
    + inline_cta("Worried about how supervision will feel for your child? Talk to us — our mediators work with families in exactly this situation.")
    + f"""
<h2 id="moving-unsupervised">Moving from supervised to unsupervised time</h2>
<p>Supervised contact is usually a stepping stone, not the destination. Most parents can move towards unsupervised time by addressing the concerns that led to the order. The path depends on the reason for supervision:</p>
<ul>
<li><strong>Substance misuse:</strong> Completing a treatment program, providing negative <a href="/court-ordered-drug-and-alcohol-testing/">drug and alcohol test</a> results over a sustained period, and demonstrating changed behaviour.</li>
<li><strong>Family violence:</strong> Completing a behaviour change program, demonstrating insight, and showing a period of safe behaviour. The other parent's assessment of ongoing risk matters.</li>
<li><strong>Mental health:</strong> Evidence of treatment, medication compliance, and a treating professional's opinion that parenting capacity is not impaired.</li>
<li><strong>Reintroduction:</strong> A gradual increase — from centre visits, to community outings with a supervisor, to short unsupervised visits, to overnight stays — as the child becomes comfortable.</li>
</ul>
<p>Moving from supervised to unsupervised contact usually requires either a new agreement between the parents (which can be formalised as <a href="/consent-orders-explained/">consent orders</a>) or an application to vary the existing order. If the other parent does not agree, the parent seeking the change will need to show the court that circumstances have changed and that unsupervised time is now in the child's best interests.</p>
<p>The strongest applications come with evidence: completion certificates, clean test results, reports from treating professionals, and positive observations from the contact centre. Preparation matters.</p>
"""
    + inline_cta("Ready to move to unsupervised time? Mediation can help both parents agree the steps and the timeline.")
    + f"""
<h2 id="mediation-role">How mediation helps with supervised contact disputes</h2>
<p>Supervised contact disputes are often deeply emotional. One parent feels the other is a danger to their child; the other feels they are being punished. <a href="/child-custody-mediation/">Parenting mediation</a> can help in several ways:</p>
<ul>
<li><strong>Agreeing on supervision arrangements:</strong> Who supervises, where, how often, and for how long — these details matter to both parents and the child, and are better decided by agreement than imposed by a judge on limited evidence.</li>
<li><strong>Designing a transition plan:</strong> A clear, written plan that sets out what the supervised parent needs to do (courses, testing, counselling), what milestones look like, and when supervision steps down.</li>
<li><strong>Avoiding court:</strong> Where the underlying concerns are genuine but manageable, a mediated agreement with safeguards can avoid the cost and delay of contested proceedings.</li>
<li><strong>Shuttle mediation:</strong> Where parents cannot be in the same room — common in family violence cases where an exemption from FDR does not apply — <a href="/shuttle-mediation-guide/">shuttle mediation</a> keeps them apart while a mediator moves between rooms.</li>
</ul>
<p><strong>Safety first.</strong> Mediation is not appropriate in every case. If there is ongoing family violence, coercive control, or a risk of harm, an exemption from {cite('fcfcoa_fdr')} may apply. Call <strong>000</strong> in an emergency, or 1800RESPECT on <strong>1800 737 732</strong> ({cite('respect_1800')}). Read our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>
"""
    + inline_cta("Need help navigating supervised contact? Book a free consultation with Mediations Australia and talk it through with an experienced mediator."),
    [("What is supervised visitation in Australia?",
      "Supervised visitation, or supervised contact, means a child spends time with a parent while a third person is present to ensure the child's safety. The supervisor may be a professional at a contact centre or a trusted family member or friend agreed by both parents."),
     ("How much does supervised visitation cost in Australia?",
      "Government-funded Children's Contact Services are free or low-cost, typically $10 to $30 per visit. Private contact centres charge $150 to $400 per visit, and private professional supervisors charge $80 to $200 per hour. Informal supervision by a family member is free."),
     ("How long does supervised visitation last?",
      "Each visit typically lasts one to three hours at a contact centre. The supervised arrangement overall is usually temporary — most Children's Contact Services have a 12-month limit, and the expectation is that families work towards a longer-term solution."),
     ("Can supervised visitation become unsupervised?",
      "Yes. Most supervised arrangements are designed as a temporary step. Parents can move to unsupervised time by addressing the concerns that led to the order — completing programs, providing clean test results, or rebuilding the relationship gradually. This requires a new agreement or a variation of the court order."),
     ("Can parents agree on supervised visitation without court?",
      "Yes. Parents can agree on supervised contact as part of a parenting plan or consent orders without a judge ordering it. Mediation is an effective way to work out the details — who supervises, where, and the plan for moving to unsupervised time."),
     ("What happens if supervised visitation is breached?",
      "If a parent breaches a court order about supervised contact — for example, by having unsupervised time when the order says supervised — the other parent can apply to the court for contravention proceedings. Consequences can include fines, make-up time, variation of orders, community service, or in serious cases, imprisonment.")],
    [("child-custody-mediation", "Child custody mediation"),
     ("parenting-plans-guide", "Parenting plans in Australia"),
     ("court-ordered-drug-and-alcohol-testing", "Drug and alcohol testing in parenting cases"),
     ("shuttle-mediation-guide", "Shuttle mediation explained"),
     ("domestic-violence-and-family-law", "Domestic violence and family law"),
     ("ex-not-following-parenting-orders", "Ex not following parenting orders")],
    read_min=10,
)
