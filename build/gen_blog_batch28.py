"""gen_blog_batch28.py — New cornerstones:
ex-not-following-parenting-orders — contravention of parenting orders: options, remedies, mediation first
new-partner-after-separation — dating, moving in, children and money after separation
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


post(
    "ex-not-following-parenting-orders",
    "Ex Not Following Parenting Orders? Your Options",
    "If your ex is ignoring parenting orders, you have options beyond court. How contravention works, what a court can do, and when mediation is the smarter step.",
    "Parenting",
    "Ex not following parenting orders <em>your options</em>",
    ("When parenting orders are made, you expect them to be followed. When your ex stops following them, it is "
     "stressful, and it is tempting to head straight back to court. Sometimes that is necessary. Often there is "
     "a calmer, faster and cheaper first step. This guide explains what counts as a contravention, what a court "
     "can do, what you should record, and where mediation fits."),
    [("what-counts", "What counts as not following orders"),
     ("first-steps", "First steps before any application"),
     ("options", "Your options compared"),
     ("contravention", "Contravention applications explained"),
     ("excuse", "Reasonable excuse and what courts consider"),
     ("mediation", "Why mediation is often the smarter first step"),
     ("safety", "When safety comes first"),
     ("evidence", "Keeping a clear, calm record")],
    key_takeaway("If your ex is not following parenting orders, document what has happened, raise it in writing, and try family dispute "
                 "resolution first. If that fails or is unsafe, you can file a contravention application, where the court can order make-up time, "
                 "bonds, costs, fines or in serious cases imprisonment.")
    + f"""
<h2 id="what-counts">What counts as not following orders</h2>
<p>Parenting orders made by a court, including consent orders, are legally binding. A contravention is a breach of those orders. Common examples include not handing over a child at the agreed time, keeping a child longer than ordered, cancelling time without a reason, refusing to attend a changeover, or ignoring orders about schooling, communication or travel.</p>
<p>It helps to separate three different situations. A <strong>parenting plan</strong> is a written agreement that is not a court order, so it cannot be enforced in the same way. A one-off late arrival caused by traffic is rarely a contravention worth litigating. A <strong>repeated pattern</strong> of missed or withheld time is quite different. The {cite('family_law_act')} sets out how the court treats breaches, and the {cite('fcfcoa')} publishes guidance for people in this position.</p>
"""
    + inline_cta("Not sure whether what is happening is a genuine breach or a communication problem? A free consultation can help you sort the two apart.")
    + f"""
<h2 id="first-steps">First steps before any application</h2>
<p>Courts expect parents to try to resolve problems sensibly before filing. A measured first response also strengthens your position if you do end up in court later.</p>
<ol>
<li><strong>Read the orders carefully.</strong> Check exactly what they say about dates, times, locations and who does what.</li>
<li><strong>Write down what happened.</strong> Note dates, times and what was said or sent.</li>
<li><strong>Raise it once, in writing, calmly.</strong> A short message that quotes the order and asks for the arrangement to be followed is enough.</li>
<li><strong>Offer a practical fix.</strong> Make-up time or a changed handover location can end a dispute quickly.</li>
<li><strong>Suggest mediation.</strong> A neutral practitioner can help both parents agree on what happens next.</li>
</ol>
<p>Avoid retaliating by withholding time yourself. Two breaches rarely help either parent, and they hurt the children most.</p>
"""
    + inline_cta("A short, calm message and an offer of mediation is usually the strongest first move. We can help you take it.")
    + f"""
<h2 id="options">Your options compared</h2>
<p>There is a range of responses, from informal to formal. The right one depends on how serious and how repeated the breach is, and whether it is safe to talk.</p>
<figure class="tbl"><table><caption>Responding to a breach of parenting orders</caption>
<thead><tr><th>Option</th><th>Best when</th><th>Typical speed</th><th>Cost level</th></tr></thead>
<tbody>
<tr><td>Direct, written request</td><td>First or minor breach</td><td>Days</td><td>Nil</td></tr>
<tr><td>Family dispute resolution (mediation)</td><td>Ongoing friction, orders need adjusting</td><td>Weeks</td><td>Low to moderate</td></tr>
<tr><td>Lawyer's letter</td><td>Repeated breaches, no response</td><td>Days to weeks</td><td>Moderate</td></tr>
<tr><td>Contravention application</td><td>Serious or repeated breaches</td><td>Months</td><td>High</td></tr>
<tr><td>Police assistance</td><td>Recovery order in place, or child at risk</td><td>Immediate</td><td>Nil</td></tr>
</tbody></table></figure>
<p class="source-note">Indicative only. Timeframes and costs vary by registry, complexity and the parties involved.</p>
<p>Police generally do not enforce ordinary parenting orders, but they can act on a recovery order and in emergencies. If a child is at immediate risk, call <strong>000</strong>.</p>
"""
    + inline_cta("Comparing your options? We can talk through which step suits your situation before you spend money on court.")
    + f"""
<h2 id="contravention">Contravention applications explained</h2>
<p>If informal steps fail, you can ask the court to deal with the breach by filing a contravention application. The court first asks whether the orders were breached and whether the other parent had a reasonable excuse. If the contravention is proved without excuse, the court has a range of responses, scaled to how serious the breach is.</p>
<figure class="tbl"><table><caption>What a court can do after a proven contravention</caption>
<thead><tr><th>Response</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Parenting education</td><td>Attending a program to improve compliance</td></tr>
<tr><td>Make-up time</td><td>Compensating time with the child that was lost</td></tr>
<tr><td>Bond</td><td>A financial promise to comply in future</td></tr>
<tr><td>Costs and compensation</td><td>Paying the other parent's legal costs or expenses</td></tr>
<tr><td>Community service or fine</td><td>For more serious or repeated breaches</td></tr>
<tr><td>Imprisonment</td><td>A last resort for the most serious breaches</td></tr>
</tbody></table></figure>
<p>Court is the right option for some situations, but it is slow and adversarial. A contravention application also tends to harden positions, which can make co-parenting harder in the long run. Many parents find that the outcome they actually want, reliable and predictable time with their child, is better reached by agreement. Our guide to <a href="/how-to-change-parenting-orders/">changing parenting orders without court</a> explains how.</p>
"""
    + inline_cta("If you want the arrangements to work in practice, not just on paper, mediation is built for that. Book a free consultation.")
    + f"""
<h2 id="excuse">Reasonable excuse and what courts consider</h2>
<p>A parent is not penalised for a breach if the court is satisfied they had a <strong>reasonable excuse</strong>. This commonly arises where a parent genuinely believed, on reasonable grounds, that complying would put a child's health or safety at risk, or where the breach was outside their control, such as illness or a transport failure. The excuse must be reasonable and the breach must have been no longer than necessary to protect the child.</p>
<p>Courts also look at the pattern, the child's age and wishes, the harm caused and what each parent did to try to fix it. The {cite('aifs')} has published research showing that children cope best when both parents keep arrangements predictable. If you have a genuine safety concern, raise it through proper channels rather than simply stopping time, and get advice quickly.</p>
"""
    + inline_cta("Worried that a breach may have a reasonable explanation? Mediation lets both sides explain without a judge deciding blame.")
    + f"""
<h2 id="mediation">Why mediation is often the smarter first step</h2>
<p>Court has its place, but it is rarely the best place to start. A breach often signals that the orders no longer fit: school hours have changed, a parent has moved, a teenager has different needs, or work shifts make handovers impossible. Mediation lets both parents fix the cause rather than punish the symptom.</p>
<ul>
<li><strong>Faster:</strong> sessions can be arranged in days or weeks, not months.</li>
<li><strong>Cheaper:</strong> a fraction of the cost of contested court proceedings.</li>
<li><strong>Flexible:</strong> new arrangements can be tailored and then formalised as consent orders.</li>
<li><strong>Less damaging:</strong> it preserves the working relationship you will need for years.</li>
</ul>
<p>Registered family dispute resolution practitioners can also issue a section 60I certificate if mediation does not work, which is generally required before filing parenting applications. See the {cite('ag_fdr')} overview and our <a href="/section-60i-certificate-guide/">section 60I certificate guide</a>. Family lawyers and mediators work well together here, and your lawyer can review any agreement before you sign.</p>
"""
    + inline_cta("Ready to try a structured conversation? Our accredited practitioners can arrange a session quickly.")
    + f"""
<h2 id="safety">When safety comes first</h2>
<p>Mediation is not appropriate in every case. If there is family violence, a safety risk to you or the children, or a refusal to engage in good faith, the court process may be the right path, and exemptions from family dispute resolution can apply. In an emergency, call <strong>000</strong>. For confidential support, contact <strong>1800RESPECT on 1800 737 732</strong> ({cite('respect_1800')}). Read more in our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>.</p>
<p>Where it is safe but conflict is high, <a href="/shuttle-mediation-guide/">shuttle mediation</a> keeps parents in separate rooms while a practitioner moves between them.</p>
"""
    + inline_cta("High conflict does not always rule out mediation. Ask us whether a shuttle format could work.", btn="Talk to us confidentially")
    + f"""
<h2 id="evidence">Keeping a clear, calm record</h2>
<p>Whatever path you take, a clear record helps. Keep it factual and short.</p>
<ul>
<li>A dated log of missed, late or cancelled handovers.</li>
<li>Copies of messages, kept in the original format.</li>
<li>Any make-up time you offered and the reply.</li>
<li>Notes of the effect on the children, described neutrally.</li>
</ul>
<p>Stick to facts and keep your tone civil. A judge, a mediator or a lawyer will all respond better to a measured record than to an angry one. Do not secretly record conversations without checking the law first; see <a href="/can-you-record-your-ex/">can you record your ex</a>. If you want to avoid repeat problems, a clear <a href="/parenting-plans-guide/">parenting plan</a> or updated consent orders can help.</p>
"""
    + inline_cta("Let's turn a messy breakdown in arrangements into a clear plan both parents can follow. Book a free consultation."),
    [
        ("What can I do if my ex is not following parenting orders?",
         "Record what has happened, raise it in writing, and try family dispute resolution. If that fails or is unsafe, "
         "you can file a contravention application, and the court can respond with make-up time, bonds, costs, fines or, rarely, imprisonment."),
        ("Can the police enforce parenting orders?",
         "Generally not, but police can act on a recovery order and in emergencies where a child is at risk. Call 000 if a child is in immediate danger."),
        ("Is a parenting plan enforceable?",
         "No. A parenting plan is not a court order, so it cannot be enforced through a contravention application. Turning it into consent orders makes it enforceable."),
        ("Do I have to try mediation before filing a contravention application?",
         "Mediation is strongly encouraged and is generally required before filing new parenting applications, but exceptions apply. Get advice on your specific situation."),
        ("What is a reasonable excuse for breaching parenting orders?",
         "A court may accept an honest and reasonable belief that complying would put a child's health or safety at risk, or a breach outside the parent's control. It must be reasonable and no longer than necessary."),
        ("Can mediation fix repeated breaches?",
         "Often, yes. Breaches commonly signal that the arrangements no longer fit. Mediation lets parents change them by agreement, which can then be made binding as consent orders."),
    ],
    [
        ("how-to-change-parenting-orders", "How to Change Parenting Orders"),
        ("parenting-plans-guide", "Parenting Plans in Australia"),
        ("section-60i-certificate-guide", "Section 60I Certificate Guide"),
        ("co-parenting-mediation", "Co-Parenting Mediation"),
        ("child-custody-mediation", "Child Custody Mediation"),
        ("domestic-violence-and-family-law", "Domestic Violence and Family Law"),
    ],
    read_min=8,
)


post(
    "new-partner-after-separation",
    "New Partner After Separation: Law and Children",
    "Dating or moving in after separation? How a new partner affects property settlement, child support and the kids, and how to agree the ground rules.",
    "Separation",
    "New partner after separation <em>and your kids</em>",
    ("Meeting someone new after a separation is common and does not have to derail anything. But a new relationship "
     "can raise questions about property, child support, parenting time and how the children cope. This guide "
     "explains what the law says, where problems tend to arise, and how mediation helps former partners agree sensible ground rules."),
    [("legal-position", "Is dating before divorce allowed?"),
     ("property", "Effect on property settlement"),
     ("child-support", "Effect on child support"),
     ("children", "Introducing a new partner to the children"),
     ("living-together", "Moving in together"),
     ("table", "What changes and what does not"),
     ("disputes", "Common disputes and how to avoid them"),
     ("mediation", "How mediation helps")],
    key_takeaway("A new partner does not cancel your property rights or your ex's, and dating before a divorce is final is not unlawful. "
                 "Moving in together can affect child support, benefits and negotiations, so agree ground rules for the children early, ideally in mediation.")
    + f"""
<h2 id="legal-position">Is dating before divorce allowed?</h2>
<p>Yes. Australia has no-fault divorce, so the only ground is that the marriage has broken down irretrievably, shown by 12 months' separation. Starting a new relationship during that period is not unlawful and does not, by itself, affect the divorce. See the {cite('fcfcoa')} for the divorce process and our guide on <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">how to get a divorce in Australia</a>.</p>
<p>Where it matters is practical. A new relationship can complicate how you describe the date of separation, how finances are shared, and how the children and your ex react.</p>
"""
    + inline_cta("Unsure how a new relationship interacts with your separation? Book a free, confidential chat.")
    + f"""
<h2 id="property">Effect on property settlement</h2>
<p>Property is divided based on the contributions of each partner, future needs and what is just and equitable, under the {cite('family_law_act')}. The question is not who left or who met someone new, and the court generally does not penalise either party for the breakdown of the marriage.</p>
<p>Some points to watch:</p>
<ul>
<li><strong>Spending on a new partner:</strong> money spent on a new partner from the pool, such as gifts, holidays or paying their debts, may be treated as wasted or added back.</li>
<li><strong>Contributions after separation:</strong> a new partner's contributions generally do not form part of your pool, but your financial circumstances may be considered under future needs.</li>
<li><strong>Time limits:</strong> there are strict limits for applying to court after divorce or separation, so do not delay property negotiations. See <a href="/delaying-property-settlement/">delaying property settlement</a>.</li>
</ul>
"""
    + inline_cta("Finalise property early so a new relationship does not muddy the numbers. Mediation is a practical way to do it.")
    + f"""
<h2 id="child-support">Effect on child support</h2>
<p>Child support is calculated from each parent's income and the care each provides, not from the new partner's income. However, a new partner can still affect arrangements indirectly. If your care percentage changes, or a new baby is born, the assessment can be updated. Parents can agree to a private arrangement or use the {cite('services_australia_cs')} formula assessment.</p>
<p>See our <a href="/child-support-guide/">child support guide</a> for how assessments work. A new partner's income is generally not counted, but a parent's ability to earn and their living costs can matter in limited situations.</p>
"""
    + inline_cta("Questions about how new circumstances change your child support? We can help you plan the conversation.")
    + f"""
<h2 id="children">Introducing a new partner to the children</h2>
<p>This is often the most sensitive part. There is no legal rule about when to introduce a new partner, but children generally cope best when changes are gradual. The {cite('aifs')} highlights the importance of stable routines and low conflict between parents for children's wellbeing.</p>
<ol>
<li><strong>Wait until the relationship is established</strong> before introducing a partner as part of the children's lives.</li>
<li><strong>Tell the other parent first</strong>, briefly and respectfully, so it does not come as a shock via the children.</li>
<li><strong>Start with short, low-key meetings</strong>, not big occasions.</li>
<li><strong>Keep parenting roles clear.</strong> A new partner supports; they do not replace a parent.</li>
<li><strong>Do not ask children to keep secrets</strong> from the other parent.</li>
</ol>
<p>Our guide to <a href="/stepparent-rights/">stepparent rights</a> explains how a new partner's role is viewed in law.</p>
"""
    + inline_cta("Agreeing how and when to introduce a new partner prevents many later disputes. Mediation gives you a neutral place to do it.")
    + f"""
<h2 id="living-together">Moving in together</h2>
<p>Living with a new partner can have financial consequences, and it is worth thinking before acting. Moving in may affect government payments and living costs, and it can start a de facto relationship in law after the relevant period or in particular circumstances such as a child of the relationship or significant contributions. See <a href="/de-facto-relationships-guide/">de facto relationships</a>.</p>
<p>If you are receiving spousal maintenance, a new de facto relationship or marriage can affect it. See <a href="/spousal-maintenance-guide/">spousal maintenance</a>. If you have unfinished property matters, protecting the pool before combining finances is sensible. Check the information at {cite('moneysmart')} on joint finances.</p>
"""
    + inline_cta("Planning to move in with someone new before settlement? Talk to us first about protecting your position.")
    + f"""
<h2 id="table">What changes and what does not</h2>
<figure class="tbl"><table><caption>Effect of a new relationship</caption>
<thead><tr><th>Area</th><th>Usually changes?</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Divorce eligibility</td><td>No</td><td>12 months' separation still applies</td></tr>
<tr><td>Property entitlement</td><td>Not directly</td><td>Wasteful spending on a partner may be added back</td></tr>
<tr><td>Child support</td><td>Not directly</td><td>Based on parents' incomes and care time</td></tr>
<tr><td>Spousal maintenance</td><td>Possibly</td><td>May end on marriage or affect need</td></tr>
<tr><td>Parenting time</td><td>Only if it affects the child</td><td>Child's best interests remain the focus</td></tr>
<tr><td>Government payments</td><td>Possibly</td><td>Depends on relationship status</td></tr>
</tbody></table></figure>
<p class="source-note">General information only. Check your own circumstances with a family lawyer or mediator.</p>
"""
    + inline_cta("Not sure which of these affects you? Let's walk through your situation in a free consultation.")
    + f"""
<h2 id="disputes">Common disputes and how to avoid them</h2>
<ul>
<li><strong>"Not around my kids":</strong> one parent objects to the other's partner. Courts rarely control who a parent dates unless there is a real risk to the child.</li>
<li><strong>Discipline and parenting roles:</strong> disagreement over what a new partner may do. Agree the boundaries in writing.</li>
<li><strong>Social media and gossip:</strong> avoid posting about the separation or the new partner, and avoid negative comments about your ex.</li>
<li><strong>Money:</strong> disputes over who pays for what when the pool is not yet settled.</li>
</ul>
<p>Court is a blunt tool for these issues and rarely the best place to start. If there has been family violence or abuse, safety must come first. Call <strong>000</strong> in an emergency or contact <strong>1800RESPECT on 1800 737 732</strong> ({cite('respect_1800')}), and see <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>.</p>
"""
    + inline_cta("Small disagreements are easier to settle early. Mediation can help before they become big ones.")
    + f"""
<h2 id="mediation">How mediation helps</h2>
<p>A new partner can bring out strong feelings, even when the separation was amicable. Mediation provides a neutral space to agree on introductions, parenting roles and communication, and to settle property and support so that new relationships do not cloud the old ones. Agreements can be recorded in a <a href="/parenting-plans-guide/">parenting plan</a> or formalised through <a href="/consent-orders-explained/">consent orders</a>.</p>
<p>Family lawyers and mediators work well together, and we encourage you to have your lawyer review any final agreement. Explore our <a href="/co-parenting-mediation/">co-parenting mediation</a> service for more.</p>
"""
    + inline_cta("Move forward with clarity for you and your children. Book a free consultation today."),
    [
        ("Can I start a new relationship before my divorce is final?",
         "Yes. Australian divorce is no-fault and requires 12 months' separation. A new relationship during that period is not unlawful and does not stop the divorce."),
        ("Does a new partner affect my property settlement?",
         "Not directly. Property is divided by contributions and future needs, not fault. Spending pool money on a new partner may be treated as wasteful and added back."),
        ("Does my new partner's income count for child support?",
         "Generally no. Child support is based on the parents' incomes and care arrangements, though changes such as a new baby can affect the assessment."),
        ("When should I introduce my new partner to my children?",
         "There is no legal rule, but children usually cope best when the relationship is established and the introduction is gradual. Tell the other parent first."),
        ("Can my ex stop my new partner being around the children?",
         "Courts rarely restrict who a parent dates unless there is a genuine risk to the child. Disagreements are better settled by agreement, for example in mediation."),
        ("Can moving in with a new partner affect spousal maintenance?",
         "Possibly. A new marriage can end entitlement and a new de facto relationship may reduce need, so get advice before you move in."),
    ],
    [
        ("separation-guide", "Separation in Australia: Complete Guide"),
        ("stepparent-rights", "Stepparent Rights"),
        ("de-facto-relationships-guide", "De Facto Relationships Guide"),
        ("child-support-guide", "Child Support Guide"),
        ("property-settlement-after-separation", "Property Settlement After Separation"),
        ("how-to-tell-children-about-separation", "How to Tell Children About Separation"),
    ],
    read_min=8,
)
