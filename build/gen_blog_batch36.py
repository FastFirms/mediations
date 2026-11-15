"""gen_blog_batch36.py — two new parenting cornerstones:
1. child-refuses-to-see-other-parent — what to do when a child won't go to the other parent
2. parallel-parenting-australia — parallel parenting for high-conflict separations
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ─────────────────────────────────────────────────────────────────────────────
# 1. Child refuses to see the other parent
# ─────────────────────────────────────────────────────────────────────────────
body1 = (
  key_takeaway("If your child refuses to see their other parent, do not ignore it and do not force it. "
               "Find out why, keep the other parent informed, and agree a plan together, ideally through "
               "family mediation. Under parenting orders, a child's refusal alone is not usually a reasonable "
               "excuse for not complying, so act early and get advice, unless there is a genuine safety risk.")
  + f"""
<h2 id="why">Why children refuse to see a parent</h2>
<p>It is one of the most distressing moments after separation: handover day arrives and your child says they will not go. Sometimes it is tears at the door; sometimes it is a teenager who simply stops answering the other parent's calls. Before deciding what to do, it helps to understand that refusal is almost always a signal, not a final decision. The common reasons are ordinary and fixable more often than parents expect.</p>
<ul>
  <li><strong>Practical friction.</strong> A long drive, missing friends or sport on weekends, no space of their own, or a household routine that feels unfamiliar.</li>
  <li><strong>Loyalty conflict.</strong> Children who sense that one parent is hurt or angry may refuse the other parent to protect them. This is very common and often unspoken.</li>
  <li><strong>A new partner or blended family.</strong> Resentment of a new partner, step-siblings or a move to a new home.</li>
  <li><strong>Age and independence.</strong> Teenagers naturally want more say over their weekends, and rigid schedules made when they were younger can stop fitting.</li>
  <li><strong>A specific incident.</strong> An argument, a harsh punishment, or feeling unheard by the other parent.</li>
  <li><strong>Genuine fear or harm.</strong> In some cases the refusal reflects family violence, abuse, or exposure to conflict. This must be taken seriously and treated differently (see the safety section below).</li>
</ul>
<p>Research from the {cite('aifs')} has consistently found that it is ongoing conflict between parents, not separation itself, that does children the most harm. How the adults respond to refusal matters more than the refusal itself.</p>
"""
  + inline_cta("Not sure why your child is refusing? A mediator can help both parents get to the bottom of it, together.")
  + f"""
<h2 id="the-law">What the law says about a child refusing contact</h2>
<p>Under the {cite('family_law_act')}, the child's best interests are the paramount consideration in every parenting decision. Since the May 2024 reforms, the court weighs a simplified set of best-interests factors, which include the child's safety, their views, their developmental and emotional needs, and the benefit of a relationship with both parents where it is safe.</p>
<p>A child's views are therefore relevant, but they are not decisive. There is no fixed age at which a child can choose which parent to see. The weight given to their views depends on their age, maturity and the reasons behind them. A considered view from a mature 15-year-old will carry far more weight than a reluctant 7-year-old who would rather stay home with their games console. We explain this in more detail in <a href="/what-age-can-a-child-choose-which-parent-to-live-with/">what age a child can choose which parent to live with</a>.</p>
<p>If there are <strong>parenting orders</strong> in place, both parents must comply with them. The parent the child lives with is generally expected to take reasonable, positive steps to encourage the child to go, not simply leave the decision to the child. A child's refusal on its own is not usually accepted as a reasonable excuse for breaching an order, although a genuine and reasonable belief that the child would be at risk can be.</p>
"""
  + inline_cta("Worried you could be in breach of parenting orders? Talk to us about resolving it before it reaches court.")
  + """
<h2 id="orders-vs-plan">Parenting orders, parenting plans, or nothing in writing</h2>
<p>What you are obliged to do depends heavily on what kind of arrangement you have. This is the single most important thing to check before you respond.</p>
<figure class="tbl"><table><caption>How refusal plays out under different arrangements</caption>
<thead><tr><th>Arrangement</th><th>Is it legally enforceable?</th><th>What to do if the child refuses</th></tr></thead>
<tbody>
<tr><td>Parenting orders (court or consent orders)</td><td>Yes. Contravention can lead to court consequences</td><td>Encourage the child to attend, keep records, tell the other parent, and seek mediation or legal advice quickly if refusal continues</td></tr>
<tr><td>Parenting plan (signed and dated)</td><td>No, but a court can take it into account</td><td>Talk to the other parent and agree changes; a mediator can help you update the plan</td></tr>
<tr><td>Informal arrangement</td><td>No</td><td>Agree a short-term plan with the other parent and consider formalising arrangements</td></tr>
<tr><td>Any arrangement, with a safety risk</td><td>Safety comes first</td><td>Protect the child, contact police on 000 if in danger, and get urgent legal advice</td></tr>
</tbody></table></figure>
<p class="source-note">General information only. Your obligations depend on the exact wording of your orders or plan. If you have orders, get legal advice before changing arrangements.</p>
<p>If you are unsure which applies, read our guide to <a href="/parenting-plans-guide/">parenting plans</a> and our explainer on <a href="/consent-orders-explained/">consent orders</a>.</p>
"""
  + inline_cta("Have a parenting plan that no longer fits? We can help you update it without court.")
  + """
<h2 id="first-steps">What to do in the first few weeks</h2>
<p>The early response sets the tone. Children notice whether their refusal causes a crisis, and parents who stay calm and consistent tend to see the problem settle faster.</p>
<ol>
  <li><strong>Stay calm with your child.</strong> Listen without interrogating. Ask open questions such as "what's the hardest part about going to Dad's?" rather than "did something happen?"</li>
  <li><strong>Encourage the time, positively.</strong> Speak well of the other parent, help pack the bag, and make clear that you want them to have a good time. Avoid offering competing treats on handover days.</li>
  <li><strong>Tell the other parent promptly and neutrally.</strong> A short, factual message is best: what happened, what your child said, and that you would like to work on it together. Do not use the refusal as leverage.</li>
  <li><strong>Keep a simple record.</strong> Dates, what was said, and steps you took. This protects both parents if things escalate.</li>
  <li><strong>Try small adjustments.</strong> Shorter visits, a different handover location, a daytime activity instead of an overnight, or the other parent attending a sports game.</li>
  <li><strong>Do not let it drift.</strong> A few missed weekends can quickly become months of estrangement that is far harder to repair.</li>
</ol>
"""
  + inline_cta("Want help agreeing a short-term plan that gets contact back on track? Book a free consultation.")
  + f"""
<h2 id="other-parent">If you are the parent being refused</h2>
<p>Being rejected by your own child is painful, and the instinct to push back hard is understandable. The most effective responses, though, are patient and child-focused.</p>
<ul>
  <li><strong>Do not blame the child.</strong> Keep calls, messages and birthday cards going, without pressure or guilt.</li>
  <li><strong>Look honestly at your side.</strong> Is there something about time at your home that could change, such as more one-on-one time, letting them bring a friend, or less screen-time conflict?</li>
  <li><strong>Avoid assuming alienation.</strong> True <a href="/parental-alienation-australia/">parental alienation</a> does happen, but most refusal has more ordinary causes. Leading with accusations tends to entrench conflict.</li>
  <li><strong>Propose mediation early.</strong> A family dispute resolution practitioner can bring both parents together, and in child-inclusive mediation a qualified consultant can hear the child's views safely, without placing them in the middle.</li>
</ul>
<p>You can find information about family dispute resolution and services near you through {cite('frol_fdr')}. If refusal persists despite reasonable efforts and there are orders in place, see our guide on what to do when an <a href="/ex-not-following-parenting-orders/">ex is not following parenting orders</a>.</p>
"""
  + inline_cta("Feeling shut out by your child? Mediation is often the fastest way to rebuild time together.")
  + f"""
<h2 id="mediation">How mediation helps when a child refuses</h2>
<p>Court can make orders, but it cannot make a reluctant child want to visit. Litigation over refusal often takes many months, involves family reports and lawyers on both sides, and can deepen the very conflict that sits behind the refusal. That is why court has its place, but it is rarely the best place to start.</p>
<p>Mediation works differently. A neutral, accredited mediator helps both parents:</p>
<ul>
  <li>share what each has seen and heard, without blame;</li>
  <li>agree a gradual return plan, for example daytime visits first, then a single overnight, then the usual schedule;</li>
  <li>adjust the schedule to fit the child's age, school and activities;</li>
  <li>agree how both parents will talk to the child about the plan, using the same message;</li>
  <li>decide whether counselling or a family therapist would help; and</li>
  <li>record the agreement in an updated parenting plan or, if appropriate, consent orders.</li>
</ul>
<p>Before most parenting applications can be filed, parents must attempt family dispute resolution and obtain a section 60I certificate, unless an exemption applies ({cite('fcfcoa_fdr')}). Starting with mediation is therefore usually required anyway, and it is often where the problem is actually solved.</p>
<figure class="tbl"><table><caption>Mediation compared with court for contact refusal</caption>
<thead><tr><th></th><th>Family mediation</th><th>Court proceedings</th></tr></thead>
<tbody>
<tr><td>Typical time to first session or hearing</td><td>1 to 3 weeks</td><td>Months, with a final hearing often 12 months or more away</td></tr>
<tr><td>Child's voice</td><td>Child-inclusive options with a qualified consultant</td><td>Usually through a family report writer or Independent Children's Lawyer</td></tr>
<tr><td>Flexibility</td><td>Gradual, tailored return plans</td><td>Orders that may be harder to adapt</td></tr>
<tr><td>Effect on co-parenting</td><td>Builds communication</td><td>Often increases conflict</td></tr>
</tbody></table></figure>
"""
  + inline_cta("Ready to resolve it together? Our accredited mediators work with parents across Australia, online or in person.")
  + f"""
<h2 id="safety">When refusal is about safety</h2>
<p>If your child's refusal reflects fear, disclosures of harm, or exposure to family violence, the priority is protecting the child, not maintaining the schedule. In an emergency, call <strong>000</strong>. For confidential support, contact {cite('respect_1800')} on <strong>1800 737 732</strong>. Children and young people can call Kids Helpline on 1800 55 1800.</p>
<p>Mediation may not be appropriate where there is family violence or a risk to a child, and exemptions from family dispute resolution apply. Get urgent legal advice about protecting the child and, if there are orders, about your options. The court's approach to risk is explained in {cite('fcfcoa_safety_risk')}, and our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a> sets out your options.</p>
"""
  + callout("A note on teenagers", "Older teenagers often vote with their feet. Rather than fighting the schedule, many families do better agreeing a flexible arrangement that respects the young person's commitments while protecting their relationship with both parents.")
  + """
<h2 id="long-term">Rebuilding the relationship long term</h2>
<p>Most refusal is temporary when both parents respond consistently. The families who come through it best tend to share a few habits: they keep the child out of adult disputes, they review arrangements as the child grows, and they get help early rather than waiting for positions to harden.</p>
<p>Consider building a regular review into your parenting plan, for example at the start of each school year, so the arrangement keeps pace with your child. If communication between you is difficult, our guides to <a href="/co-parenting-mediation/">co-parenting mediation</a> and <a href="/high-conflict-family-law-mediation/">high-conflict mediation</a> explain approaches that reduce friction, including shuttle mediation where you do not need to be in the same room.</p>
"""
  + inline_cta("Want a plan that grows with your child? Speak with an accredited family mediator today.")
)

post(
    "child-refuses-to-see-other-parent",
    "Child Refuses to See Other Parent? What to Do",
    "When a child won't see their other parent: why it happens, what the law expects under parenting orders, and how mediation helps rebuild time safely.",
    "Parenting",
    "Child refusing to see a parent <em>without court</em>",
    "When a child refuses to go to their other parent, both parents can feel helpless. This guide explains why it happens, what Australian family law expects of each parent, and the calm, practical steps that usually get things back on track without court.",
    [("why", "Why children refuse to see a parent"),
     ("the-law", "What the law says"),
     ("orders-vs-plan", "Orders, plans, or nothing in writing"),
     ("first-steps", "What to do in the first few weeks"),
     ("other-parent", "If you are the parent being refused"),
     ("mediation", "How mediation helps"),
     ("safety", "When refusal is about safety"),
     ("long-term", "Rebuilding the relationship long term")],
    body1,
    [("Can a child refuse to see a parent in Australia?",
      "There is no age at which a child can legally decide. A child's views are one of the best-interests factors, and their weight increases with age and maturity, but parents remain responsible for complying with any parenting orders."),
     ("Am I in breach of parenting orders if my child refuses to go?",
      "Possibly. The parent the child lives with is generally expected to take reasonable, positive steps to encourage the child to attend. A child's refusal alone is not usually a reasonable excuse, although a genuine, reasonable belief that the child is at risk can be. Get legal advice if refusal continues."),
     ("Should I force my child to see their other parent?",
      "Physically forcing a child is rarely helpful. Encourage the time positively, find out what is behind the refusal, and agree adjustments with the other parent, ideally through mediation. If there is a safety concern, protect the child first."),
     ("Can a mediator speak to my child?",
      "In child-inclusive mediation, a qualified child consultant can meet the child separately and share their views with the parents in a safe, age-appropriate way, so the child is heard without being put in the middle."),
     ("What if my child refuses because of family violence?",
      "Safety comes first. Call 000 in an emergency or 1800RESPECT on 1800 737 732 for support. Mediation may not be appropriate and exemptions from family dispute resolution apply. Seek urgent legal advice.")],
    [("what-age-can-a-child-choose-which-parent-to-live-with", "When a child can choose where to live"),
     ("ex-not-following-parenting-orders", "Ex not following parenting orders"),
     ("parental-alienation-australia", "Parental alienation in Australia"),
     ("co-parenting-mediation", "Co-parenting mediation"),
     ("how-to-change-parenting-orders", "How to change parenting orders"),
     ("child-custody-mediation", "Child custody mediation")],
    read_min=9,
)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Parallel parenting
# ─────────────────────────────────────────────────────────────────────────────
body2 = (
  key_takeaway("Parallel parenting is a structured way of raising children after separation where each parent "
               "runs their own household with minimal direct contact, and communication is limited, written and "
               "child-focused. It suits high-conflict separations where co-parenting keeps breaking down, and works "
               "best when the rules are agreed in a detailed parenting plan, often through mediation.")
  + f"""
<h2 id="what-is">What is parallel parenting?</h2>
<p>Parallel parenting is an approach for separated parents who cannot yet communicate without conflict. Instead of trying to co-parent closely, attending events together, making decisions over the phone and negotiating every change, each parent takes responsibility for the children during their own time and the two households run largely independently.</p>
<p>The aim is simple: <strong>take the children out of the line of fire</strong>. Research from the {cite('aifs')} has long shown that children are harmed most by ongoing, unresolved conflict between their parents. Parallel parenting reduces the number of moments where that conflict can happen, while still allowing children to have a meaningful relationship with both parents.</p>
<p>It is not a legal category in the {cite('family_law_act')}. It is a practical way of structuring a parenting plan or parenting orders, and courts and mediators in Australia regularly use its building blocks.</p>
"""
  + inline_cta("Every conversation with your ex turning into an argument? A mediator can help you set up a structure that works.")
  + """
<h2 id="vs-co-parenting">Parallel parenting vs co-parenting</h2>
<p>Co-parenting is the ideal many families aim for, but it relies on parents being able to cooperate flexibly. Parallel parenting is often a stage on the way there, not a permanent label.</p>
<figure class="tbl"><table><caption>Co-parenting compared with parallel parenting</caption>
<thead><tr><th></th><th>Co-parenting</th><th>Parallel parenting</th></tr></thead>
<tbody>
<tr><td>Communication</td><td>Frequent, flexible, often by phone or in person</td><td>Limited, written, business-like, usually via an app or email</td></tr>
<tr><td>Household rules</td><td>Broadly consistent across both homes</td><td>Each parent sets their own day-to-day rules</td></tr>
<tr><td>Handovers</td><td>At either home, often with a chat</td><td>At school, childcare or a neutral place, kept brief</td></tr>
<tr><td>School and sports events</td><td>Both attend together</td><td>Attend separately or alternate</td></tr>
<tr><td>Changes to the schedule</td><td>Negotiated informally</td><td>Rare, requested in writing with notice</td></tr>
<tr><td>Best suited to</td><td>Low-conflict separations</td><td>High-conflict or recently separated parents</td></tr>
</tbody></table></figure>
<p>Our guide to <a href="/co-parenting-mediation/">co-parenting mediation</a> explains how families often move from parallel parenting back towards cooperative co-parenting as emotions settle.</p>
"""
  + inline_cta("Not sure which approach suits your family? Talk it through in a free consultation.")
  + """
<h2 id="when">When parallel parenting is the right choice</h2>
<p>Parallel parenting suits families where both parents are capable and loving, but where contact between the adults keeps escalating. Common signs include:</p>
<ul>
  <li>handovers regularly end in arguments, often in front of the children;</li>
  <li>text messages quickly turn hostile or are used to relitigate the relationship;</li>
  <li>children are being used to carry messages between homes;</li>
  <li>every small change to the schedule becomes a dispute;</li>
  <li>one or both parents feel unable to attend school events while the other is there.</li>
</ul>
<p>It is especially useful in the first year or two after separation, when hurt and anger are at their highest. Parents who have been described as "high conflict" are often simply in the rawest stage of separation, and structure gives them space to recover. Our guide to <a href="/high-conflict-family-law-mediation/">high-conflict family law mediation</a> explains how mediators manage these situations.</p>
"""
  + inline_cta("Handovers turning into arguments? Let's agree arrangements that keep the children out of the middle.")
  + """
<h2 id="plan">What a parallel parenting plan should include</h2>
<p>Because parallel parenting relies on minimal negotiation, the plan has to do the work. The more detail it contains, the fewer decisions you need to make together later. A good plan covers:</p>
<ol>
  <li><strong>The schedule.</strong> A clear, repeating pattern of time, plus school holidays, Christmas, birthdays, Mother's Day and Father's Day.</li>
  <li><strong>Handovers.</strong> Where, when and how, ideally at school or childcare so parents rarely meet, with a neutral backup location.</li>
  <li><strong>Communication rules.</strong> One agreed channel (for example a co-parenting app or email), expected response times, and a rule that messages are about the children only.</li>
  <li><strong>Decision-making.</strong> Which major long-term issues, such as schooling, health and religion, require joint consultation, and how disagreements will be resolved.</li>
  <li><strong>Day-to-day authority.</strong> Confirmation that each parent makes routine decisions during their own time.</li>
  <li><strong>Information sharing.</strong> Both parents can contact schools and doctors directly, and urgent medical matters are reported promptly.</li>
  <li><strong>Events.</strong> How school concerts, sport and parent-teacher interviews will be shared or alternated.</li>
  <li><strong>Review and dispute resolution.</strong> A date to review the plan and an agreement to return to mediation before going to court.</li>
</ol>
<p>Our <a href="/parenting-plans-guide/">parenting plans guide</a> explains the legal status of a plan and when it is worth turning it into consent orders.</p>
"""
  + inline_cta("Want a detailed parenting plan that leaves less room for argument? Our mediators can help you build one.")
  + f"""
<h2 id="communication">Communication rules that actually work</h2>
<p>Most parallel parenting succeeds or fails on communication. A few simple habits make a large difference:</p>
<ul>
  <li><strong>Use one written channel.</strong> A dedicated co-parenting app keeps a time-stamped record, holds a shared calendar and can track expenses. See our round-up of the <a href="/best-apps-for-separated-parents/">best apps for separated parents</a>.</li>
  <li><strong>Keep it brief, informative, friendly and firm.</strong> State the fact, the request and the deadline. Leave out commentary on the past.</li>
  <li><strong>Agree response times.</strong> For example, within 48 hours for routine matters and the same day for urgent ones.</li>
  <li><strong>Never use the children as messengers.</strong> Even small messages put children in a loyalty bind.</li>
  <li><strong>Pause before replying.</strong> If a message makes you angry, wait before you answer. You do not need to respond to every provocation.</li>
</ul>
<p>Written communication also creates a reliable record if a dispute does arise later, which tends to keep both parents' messages more measured. Free information and referrals are available through {cite('frc')}.</p>
"""
  + inline_cta("Communication still breaking down? Shuttle mediation means you never need to be in the same room.")
  + f"""
<h2 id="mediation">How mediation helps set up parallel parenting</h2>
<p>Parents in high conflict often assume they cannot mediate. In practice, mediation is often where parallel parenting begins. An accredited family dispute resolution practitioner can run the process as <a href="/shuttle-mediation-guide/">shuttle mediation</a>, moving between separate rooms or separate online sessions, so you never have to deal with each other directly.</p>
<p>In mediation you can agree the schedule, handover logistics, communication rules and decision-making framework in one structured process, then record it as a parenting plan or, if you want it to be enforceable, as consent orders. Before most parenting applications can be filed, separated parents must also attempt family dispute resolution and obtain a section 60I certificate, unless an exemption applies ({cite('fcfcoa_fdr')}).</p>
<p>Court has its place, particularly where safety is at risk or one parent will not engage at all. But a contested parenting case can take well over a year to reach a final hearing and usually increases conflict. Mediation is rarely the slower or more expensive option, and it lets you design arrangements that suit your family rather than having them imposed.</p>
"""
  + inline_cta("Ready to agree a parallel parenting plan? Book a free consultation with an accredited family mediator.")
  + f"""
<h2 id="not-suitable">When parallel parenting is not appropriate</h2>
<p>Parallel parenting is designed for conflict between two safe parents. It is <strong>not a solution to family violence, coercive control or child abuse</strong>. Where there is violence or a risk to children, the focus must shift to safety: supervised arrangements, protection orders and specialist legal advice.</p>
<p>Mediation may not be appropriate where there is family violence, and exemptions from family dispute resolution apply. If you are in danger, call <strong>000</strong>. For confidential support, contact {cite('respect_1800')} on <strong>1800 737 732</strong>. Our guides to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a> and <a href="/supervised-visitation-australia/">supervised visitation</a> explain the options, and the court's approach to risk is set out in {cite('fcfcoa_safety_risk')}.</p>
"""
  + callout("Is parallel parenting forever?", "Usually not. Many families start with a parallel structure and, as trust slowly returns, relax the rules: a shared event here, a phone call there. Building a review date into the plan makes that transition easier.")
  + """
<h2 id="moving-on">Moving from parallel parenting to co-parenting</h2>
<p>For many families, parallel parenting is a bridge. Once handovers have been calm for several months and written communication has settled into a predictable rhythm, parents often find they can loosen the structure, for example by both attending a school concert, agreeing small schedule swaps by message, or sitting down together at a review mediation.</p>
<p>There is no deadline for this, and some families stay with a parallel model until the children are grown, which is perfectly fine. What matters is that the children experience two stable homes and are no longer caught in the middle. If your arrangements need updating as your children get older, see our guide on <a href="/how-to-change-parenting-orders/">how to change parenting orders</a> without going back to court.</p>
"""
  + inline_cta("Ready to review your arrangements as the children grow? We can help you update them, calmly.")
)

post(
    "parallel-parenting-australia",
    "Parallel Parenting in Australia: How It Works",
    "Parallel parenting for high-conflict separations: how it differs from co-parenting, what the plan should include, and how mediation helps set it up.",
    "Parenting",
    "Parallel parenting <em>after high conflict</em>",
    "When every handover becomes an argument, parallel parenting gives children two stable homes while keeping parents' contact to a minimum. This guide explains how it works in Australia, what to put in the plan, and how to agree it without court.",
    [("what-is", "What is parallel parenting?"),
     ("vs-co-parenting", "Parallel parenting vs co-parenting"),
     ("when", "When it is the right choice"),
     ("plan", "What the plan should include"),
     ("communication", "Communication rules that work"),
     ("mediation", "How mediation helps"),
     ("not-suitable", "When it is not appropriate"),
     ("moving-on", "Moving towards co-parenting")],
    body2,
    [("What is the difference between parallel parenting and co-parenting?",
      "Co-parenting involves frequent, flexible cooperation between parents. Parallel parenting keeps direct contact to a minimum: each parent runs their own household, communication is written and limited to the children, and handovers happen at school or a neutral place."),
     ("Is parallel parenting recognised by Australian courts?",
      "It is not a separate legal category, but its elements, such as handovers at school, communication via an app and clear decision-making rules, are commonly included in parenting plans and consent orders."),
     ("Can we mediate if we can't be in the same room?",
      "Yes. Shuttle mediation lets the mediator move between separate rooms or online sessions, so you can agree a parallel parenting plan without dealing with each other directly."),
     ("Is parallel parenting bad for children?",
      "No. For high-conflict families it is often better for children than attempting close co-parenting, because it reduces their exposure to conflict while preserving their relationship with both parents."),
     ("Is parallel parenting suitable if there is family violence?",
      "No. Parallel parenting is for conflict between safe parents. Where there is violence or risk to children, safety measures and specialist legal advice come first, and exemptions from family dispute resolution apply.")],
    [("co-parenting-mediation", "Co-parenting mediation"),
     ("high-conflict-family-law-mediation", "High-conflict family law mediation"),
     ("shuttle-mediation-guide", "Shuttle mediation guide"),
     ("best-apps-for-separated-parents", "Best apps for separated parents"),
     ("parenting-plans-guide", "Parenting plans guide"),
     ("child-refuses-to-see-other-parent", "When a child refuses to see a parent")],
    read_min=9,
)
