#!/usr/bin/env python3
"""Batch 4 cornerstone posts at full depth."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- WHAT IS MEDIATION IN FAMILY LAW (absorbs 12) ----
post("what-is-mediation-in-family-law",
 "What Is Mediation in Family Law? A Complete Guide (2026)",
 "What is family law mediation, how does it work, and why does it succeed? A complete 2026 guide to the process, the mediator's role, costs, and how it compares to court.",
 "The process",
 "What Is Mediation in Family Law? <em>A Complete Guide</em>",
 "Family law mediation is a structured, confidential process where a neutral mediator helps separating people reach their own agreement on parenting, property and finances \u2014 without going to court. This guide explains how it works, why it succeeds so often, what it costs, and when it's the right choice.",
 [("what-is","What is family law mediation?"),
  ("how-works","How does the process work?"),
  ("mediator-role","What does the mediator do?"),
  ("why-works","Why mediation works so well"),
  ("what-resolve","What can mediation resolve?"),
  ("cost-time","Cost and time"),
  ("right-for-you","Is mediation right for you?")],
 key_takeaway("Family law mediation is a confidential process in which a neutral, accredited mediator helps separating parties negotiate their own agreement on parenting, property and finances. The mediator guides the conversation but does not decide the outcome. It resolves most disputes in one or two sessions, costs a fraction of court, and for parenting matters is generally a required step before litigation.")
 + f"""
<h2 id="what-is">What is family law mediation?</h2>
<p>Mediation is a form of alternative dispute resolution where an impartial third party \u2014 the mediator \u2014 helps people in conflict reach a mutually acceptable agreement. In a family law context, that means resolving the practical questions of separation: who the children live with, how time is shared, and how property and finances are divided.</p>
<p>Crucially, the mediator doesn't take sides or impose a decision. The agreement is yours. This is the core difference from court, and the {cite("ag_fdr")} promotes it as the preferred way to resolve family disputes wherever it's safe to do so.</p>
"""
 + inline_cta("Curious whether mediation could work for your situation? Find out in a free, no-obligation consultation.")
 + """
<h2 id="how-works">How does the process work?</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 you discuss your situation and the mediator assesses whether mediation is suitable.</li>
  <li><strong>Intake and preparation</strong> \u2014 each party meets the mediator separately; documents and disclosure are gathered.</li>
  <li><strong>The joint session</strong> \u2014 the parties (together or in separate rooms) work through the issues with the mediator's guidance.</li>
  <li><strong>Reaching agreement</strong> \u2014 areas of agreement are recorded in a Heads of Agreement.</li>
  <li><strong>Formalising</strong> \u2014 the agreement is turned into <a href="/consent-orders-explained/">consent orders</a> or a binding agreement.</li>
</ol>
<p><a href="/how-mediation-works/">See the full step-by-step process \u2192</a></p>

<h2 id="mediator-role">What does the mediator do?</h2>
<p>The mediator manages the conversation, keeps it constructive, ensures both people are heard, and helps generate options \u2014 but never decides who's right or imposes a result. A good mediator uses reality-checking, manages high emotion, and keeps the focus on the future rather than re-litigating the past. Many of our mediators are also experienced family lawyers, so the legal framework is understood throughout.</p>
"""
 + callout("Mediation is confidential",
   "What's said in mediation generally can't be used against you in court later. That confidentiality lets people speak frankly and explore options they'd never raise in an adversarial setting.")
 + f"""
<h2 id="why-works">Why mediation works so well</h2>
<p>Mediation has a high success rate for good reasons. People are far more likely to honour an agreement they helped create than one imposed on them. It lowers conflict rather than inflaming it, which matters enormously when you'll keep co-parenting for years. And it's faster and cheaper, so the stress doesn't drag on. Research collated by the {cite("aifs")} consistently supports dispute resolution over litigation for family matters.</p>

<h2 id="what-resolve">What can mediation resolve?</h2>
<ul>
  <li><a href="/parenting-plan-mediation/">Parenting arrangements</a> \u2014 living arrangements, time, decision-making</li>
  <li><a href="/property-settlement-mediation/">Property and financial settlements</a></li>
  <li>Child support and <a href="/spousal-support-mediation/">spousal maintenance</a></li>
  <li>De facto and same-sex relationship disputes</li>
  <li>Even <a href="/estate-dispute-mediation/">estate</a> and <a href="/workplace-mediation/">workplace</a> conflicts</li>
</ul>

<h2 id="cost-time">Cost and time</h2>
<p>Most matters resolve in one or two sessions, often within a few weeks \u2014 versus one to three years in court. Costs are a fraction of litigation and usually shared between parties. <a href="/cost-of-divorce-in-australia/">See the full cost comparison \u2192</a></p>
"""
 + inline_cta("Most disputes settle in one or two sessions. See how quickly yours could resolve \u2014 book today.")
 + """
<h2 id="right-for-you">Is mediation right for you?</h2>
<p>Mediation suits the large majority of separating people \u2014 including those in high conflict, where techniques like <a href="/mediation-with-a-narcissist/">shuttle mediation</a> keep parties apart. It isn't suitable in every case: where there's family violence or a safety risk that can't be managed, other paths exist, and exemptions apply. If you're unsure, an honest assessment in a consultation is the best place to start. <a href="/is-family-law-mediation-compulsory/">Is mediation compulsory? \u2192</a></p>
"""
 ,
 [("What is mediation in family law?",
   "It's a confidential process where a neutral, accredited mediator helps separating people reach their own agreement on parenting, property and finances, without a court imposing a decision."),
  ("Does the mediator decide the outcome?",
   "No. The mediator guides the conversation and helps generate options, but the parties make their own decisions. This is the key difference from a judge."),
  ("Is family law mediation confidential?",
   "Yes. What's said in mediation generally can't be used against you in later court proceedings, which lets people speak openly and explore solutions."),
  ("What can be resolved through mediation?",
   "Parenting arrangements, property and financial settlements, child support, spousal maintenance, de facto disputes, and even estate and workplace conflicts."),
  ("How long and how much does mediation take?",
   "Most matters resolve in one or two sessions, often within weeks, at a fraction of court costs \u2014 usually shared between the parties.")],
 [("how-mediation-works","How Mediation Works"),
  ("family-law-mediation","Family Law Mediation"),
  ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
  ("how-long-does-mediation-take","How Long Does Mediation Take?"),
  ("cost-of-divorce-in-australia","Cost of Divorce"),
  ("preparing-for-mediation","Preparing for Mediation")],
 read_min=10)
print("what-is-mediation-in-family-law built")

# ---- MEDIATE OR LITIGATE (absorbs 13) ----
post("mediate-or-litigate",
 "Mediate or Litigate? How to Choose (Australia 2026)",
 "Mediation or court for your family law dispute? A clear comparison of cost, time, control, privacy and outcomes \u2014 and why mediation is almost always the smarter first step.",
 "The process",
 "Mediate or Litigate? <em>How to Choose</em>",
 "When a relationship ends in dispute, you have a choice: resolve it through mediation, or fight it out in court. They lead to very different outcomes \u2014 in cost, time, stress and control. This guide compares them honestly so you can choose wisely. For the vast majority, mediation is the smarter first step.",
 [("two-paths","Two very different paths"),
  ("comparison","Mediation vs litigation: the comparison"),
  ("cost","The cost difference"),
  ("control","Who controls the outcome?"),
  ("when-court","When is court genuinely necessary?"),
  ("lawyers-allies","Lawyers are allies, not the enemy"),
  ("smart-first-step","The smart first step")],
 key_takeaway("Mediation and litigation lead to very different outcomes. Mediation is faster, cheaper, private, and keeps the decision in your hands; litigation is slow, expensive, public, and hands control to a judge. Court has its place \u2014 for genuine safety issues or where one party won't engage \u2014 but for most disputes, mediation is the smarter, less damaging first step.")
 + """
<h2 id="two-paths">Two very different paths</h2>
<p>It helps to be clear-eyed about what each path actually involves. Litigation is adversarial by design: each side argues its case, and a judge imposes a binding decision. Mediation is collaborative: a neutral mediator helps you reach your own agreement. The villain here isn't lawyers or the courts \u2014 it's <em>unnecessary</em> litigation, the kind that drains finances and poisons co-parenting when a calmer path was available.</p>
"""
 + inline_cta("Not sure which path fits your situation? Get honest guidance in a free consultation \u2014 we'll tell you straight.")
 + f"""
<h2 id="comparison">Mediation vs litigation: the comparison</h2>
<figure class="tbl"><table><caption>Mediation vs litigation at a glance</caption>
<thead><tr><th>Factor</th><th>Mediation</th><th>Litigation</th></tr></thead>
<tbody>
<tr><td>Time</td><td>Weeks</td><td>1\u20133 years</td></tr>
<tr><td>Cost</td><td>Few thousand (shared)</td><td>Tens of thousands per side</td></tr>
<tr><td>Who decides</td><td>You and your ex</td><td>A judge</td></tr>
<tr><td>Privacy</td><td>Confidential</td><td>Public record</td></tr>
<tr><td>Relationship impact</td><td>Preserves co-parenting</td><td>Often damages it</td></tr>
<tr><td>Flexibility</td><td>High \u2014 tailored agreement</td><td>Limited \u2014 court's orders</td></tr>
</tbody></table></figure>

<h2 id="cost">The cost difference</h2>
<p>This is the starkest contrast. A contested case can cost each party tens of thousands of dollars \u2014 money that usually comes straight out of the asset pool you're dividing (see the <a href="https://www.fcfcoa.gov.au/fl/fees/fl-fees" target="_blank" rel="noopener">court fee schedule</a>). Mediation typically resolves the same dispute for a few thousand dollars in total. <a href="/cost-of-divorce-in-australia/">See the full cost breakdown \u2192</a></p>

<h2 id="control">Who controls the outcome?</h2>
<p>In court, you hand the most important decisions of your life to a stranger in a robe, bound by legal rules and limited time. In mediation, you keep that control \u2014 you craft arrangements that actually fit your family. People consistently report higher satisfaction with agreements they shaped themselves.</p>
"""
 + callout("Court outcomes rarely leave anyone happy",
   "After a long contested case, research shows neither party tends to be satisfied with the result \u2014 and both have spent heavily to get there. Mediation's agreed outcomes hold up better precisely because both sides chose them.")
 + f"""
<h2 id="when-court">When is court genuinely necessary?</h2>
<p>Honesty matters: court has a legitimate place. Litigation may be necessary where there is family violence or a serious safety risk, where one party refuses to participate or disclose, where urgent orders are needed, or where there's a genuine legal question only a court can decide. The {cite("fcfcoa")} exists for exactly these situations. The point isn't to avoid court at all costs \u2014 it's to avoid <em>unnecessary</em> court.</p>

<h2 id="lawyers-allies">Lawyers are allies, not the enemy</h2>
<p>Good family lawyers often steer clients <em>toward</em> mediation \u2014 because they know what litigation costs in money and wellbeing. Many of our own mediators are experienced lawyers. The best results often combine both: legal advice to understand your position, and mediation to reach the agreement. <a href="/collaborative-family-lawyers/">See collaborative family law \u2192</a></p>
"""
 + inline_cta("Want the benefits of legal insight and a settlement without the court war? That's exactly what we do.")
 + """
<h2 id="smart-first-step">The smart first step</h2>
<p>For most people, the sequence is simple: try mediation first. It's faster, cheaper and less damaging, and for parenting matters it's generally required before court anyway under the <a href="https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution" target="_blank" rel="noopener">family dispute resolution framework</a>. If mediation resolves things \u2014 as it usually does \u2014 you've saved years and tens of thousands. If it doesn't fully resolve, it narrows the issues so any remaining court process is shorter. Either way, starting with mediation is the wise move. <a href="/family-law-mediation/">Start with mediation \u2192</a></p>
"""
 ,
 [("Should I mediate or go to court?",
   "For most family law disputes, mediation is the smarter first step \u2014 faster, cheaper, private and less damaging. Court is best reserved for safety issues, urgent orders, or where one party won't engage."),
  ("Is mediation cheaper than going to court?",
   "Far cheaper. Mediation usually costs a few thousand dollars shared between parties, versus tens of thousands per side for contested litigation."),
  ("When is court necessary?",
   "Where there's family violence or a safety risk, urgent orders are needed, one party refuses to participate or disclose, or a genuine legal question requires a judge."),
  ("Will my lawyer be against mediation?",
   "Usually the opposite. Good family lawyers often recommend mediation because they understand the cost and toll of litigation. Many mediators are themselves experienced lawyers."),
  ("What if mediation doesn't work?",
   "Even partial mediation narrows the issues, making any later court process shorter and cheaper. Nothing invested in mediation is wasted.")],
 [("family-law-mediation","Family Law Mediation"),
  ("what-is-mediation-in-family-law","What Is Mediation?"),
  ("cost-of-divorce-in-australia","Cost of Divorce"),
  ("collaborative-family-lawyers","Collaborative Family Lawyers"),
  ("how-mediation-works","How Mediation Works"),
  ("family-law-arbitration","Family Law Arbitration")],
 read_min=10)
print("mediate-or-litigate built")

# ---- CHILD CUSTODY MEDIATION (absorbs 8) ----
post("child-custody-mediation",
 "Child Custody Mediation in Australia: How It Works (2026)",
 "How does child custody mediation work in Australia? What the law says about 'custody', the best-interests test, 50/50 care, and how mediation helps parents agree. 2026 guide.",
 "Parenting",
 "Child Custody Mediation in Australia: <em>How It Works</em>",
 "In Australia, 'custody' is an outdated term \u2014 the law focuses on parental responsibility and the child's best interests. Child custody mediation helps separated parents agree on living arrangements and time without a court battle. Here's how it works and what the law actually says.",
 [("custody-term","'Custody' isn't the legal term"),
  ("best-interests","The best-interests test"),
  ("how-works","How custody mediation works"),
  ("5050","Is care always 50/50?"),
  ("fathers-mothers","Do mothers or fathers get preference?"),
  ("childrens-voice","Does the child get a say?"),
  ("when-court","When court may be needed")],
 key_takeaway("Australian family law no longer uses 'custody' \u2014 it focuses on parental responsibility and what's in the child's best interests. There's no automatic 50/50 and no preference for mothers or fathers. Mediation (family dispute resolution) is generally a required first step and helps parents agree on arrangements, with a Section 60I certificate needed before going to court.")
 + f"""
<h2 id="custody-term">'Custody' isn't the legal term</h2>
<p>Many parents still search for "custody", but Australian law moved away from that language years ago. Under the {cite("family_law_act")}, the focus is on <strong>parental responsibility</strong> (decision-making about major issues) and the arrangements for who a child <strong>lives with</strong> and <strong>spends time with</strong>. The shift is deliberate: children aren't possessions to be "won".</p>
"""
 + inline_cta("Working out arrangements for your children? A child-focused mediator can help you agree. Book a consultation.")
 + f"""
<h2 id="best-interests">The best-interests test</h2>
<p>Every parenting decision is governed by one principle: the best interests of the child. The {cite("family_law_act")} sets out the factors a court (and therefore a mediator) considers \u2014 above all, the benefit of a meaningful relationship with both parents, balanced against the need to protect the child from harm. Where those two collide, safety always wins. Reforms that took effect in 2024 streamlined these factors and placed the child's safety and needs at the centre.</p>
<figure class="tbl"><table><caption>What the best-interests test weighs</caption>
<thead><tr><th>Factor</th><th>What it looks at</th></tr></thead>
<tbody>
<tr><td>Safety</td><td>Protecting the child from family violence, abuse or neglect \u2014 the overriding consideration</td></tr>
<tr><td>The child's views</td><td>What the child wants, weighed for their age and maturity</td></tr>
<tr><td>Developmental needs</td><td>The child's emotional, psychological and developmental needs</td></tr>
<tr><td>Capacity to provide</td><td>Each parent's ability to meet those needs</td></tr>
<tr><td>Benefit of both parents</td><td>The value of a meaningful relationship with each parent, where safe</td></tr>
</tbody></table></figure>

<h2 id="how-works">How custody mediation works</h2>
<p>Child custody mediation is a form of <a href="/family-law-mediation/">family dispute resolution</a>. A neutral mediator helps both parents work through living arrangements, time-sharing, holidays, schooling and communication, keeping the focus on the children. If agreement is reached, it's recorded in a <a href="/parenting-plans-guide/">parenting plan</a> and can be formalised as <a href="/consent-orders-explained/">consent orders</a>. For most parenting disputes, this {cite("fcfcoa_fdr")} step is <em>required</em> before you can apply to court. <a href="/section-60i-certificates/">You'll need a Section 60I certificate \u2192</a></p>
"""
 + callout("Family dispute resolution is usually compulsory",
   "Except where exemptions apply (such as family violence or urgency), parents must attempt family dispute resolution and obtain a Section 60I certificate before filing a parenting application in court.")
 + """
<h2 id="5050">Is care always 50/50?</h2>
<p>No. There is no automatic right to equal (50/50) time. While the law supports children maintaining meaningful relationships with both parents where safe, the actual arrangement depends entirely on the child's best interests and what's practical \u2014 distance, work, the child's age and routine all matter. Mediation lets you design an arrangement that genuinely fits your family rather than a one-size-fits-all formula.</p>
<figure class="tbl"><table><caption>Common care arrangements parents agree in mediation</caption>
<thead><tr><th>Pattern</th><th>How it works</th><th>Often suits</th></tr></thead>
<tbody>
<tr><td>Week-about</td><td>Alternating full weeks with each parent</td><td>School-age children, parents living nearby</td></tr>
<tr><td>5-2-2-5</td><td>Fixed weekdays with each parent, alternating weekends</td><td>Younger children needing frequent contact</td></tr>
<tr><td>Alternate weekends</td><td>One parent primary, the other every second weekend plus some weeknights</td><td>Where distance or work limits midweek changeovers</td></tr>
<tr><td>Tailored</td><td>Any pattern that fits the child's routine and the family's logistics</td><td>Most families \u2014 the point of mediation</td></tr>
</tbody></table></figure>

<h2 id="fathers-mothers">Do mothers or fathers get preference?</h2>
<p>The law gives no preference based on gender. Both parents start on equal footing, and outcomes turn on the children's best interests and each parent's circumstances \u2014 not on whether they're mum or dad. <a href="/fathers-rights/">See fathers' rights after separation \u2192</a></p>
"""
 + inline_cta("Worried the system is stacked against you? It isn't \u2014 and mediation keeps the focus where it belongs.")
 + """
<h2 id="childrens-voice">Does the child get a say?</h2>
<p>Children's views can be taken into account in a way that's appropriate to their age and maturity \u2014 they're never asked to "choose". Child-inclusive mediation, where a specialist consults the child and feeds their perspective back into the process, is one way to ensure children are heard without being burdened with the decision.</p>

<h2 id="when-court">When court may be needed</h2>
<p>If mediation can't resolve matters \u2014 or where there's family violence, abuse or a serious safety concern \u2014 court may be necessary, and exemptions from the mediation requirement apply. Even then, mediation often narrows the issues first. If safety is a concern, tell us, and we'll advise the safest path. <a href="/domestic-violence-and-family-law/">See domestic violence and family law \u2192</a></p>
"""
 ,
 [("Is 'custody' still used in Australia?",
   "No. Australian law focuses on parental responsibility and who a child lives with and spends time with, guided by the child's best interests \u2014 not 'custody'."),
  ("Is child custody always shared 50/50?",
   "No. There's no automatic right to equal time. Arrangements depend on the child's best interests and practical factors like distance, age and routine."),
  ("Do mothers get preference over fathers?",
   "No. The law gives no gender preference. Both parents start equal, and outcomes turn on the child's best interests and each parent's circumstances."),
  ("Do I have to try mediation before court for custody?",
   "Generally yes. Family dispute resolution is required and you need a Section 60I certificate before filing a parenting application, unless an exemption (such as family violence) applies."),
  ("Does my child get to choose who they live with?",
   "Children are never asked to choose. Their views may be considered in an age-appropriate way, sometimes through child-inclusive mediation.")],
 [("parenting-plan-mediation","Parenting Plan Mediation"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("section-60i-certificates","Section 60I Certificates"),
  ("fathers-rights","Fathers' Rights"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("domestic-violence-and-family-law","Domestic Violence & Family Law")],
 read_min=10)
print("child-custody-mediation built")

# ---- DOMESTIC VIOLENCE & FAMILY LAW (absorbs 9) ----
post("domestic-violence-and-family-law",
 "Domestic Violence and Family Law in Australia (2026 Guide)",
 "How domestic violence affects family law in Australia: AVOs/DVOs, safety during separation, mediation exemptions, and how the courts protect families. Support resources included.",
 "Safety",
 "Domestic Violence and Family Law in Australia",
 "If you're experiencing family violence, your safety comes first \u2014 always. This guide explains how domestic violence intersects with family law: protection orders, how it affects parenting and property, when mediation is and isn't appropriate, and where to get help right now.",
 [("safety-first","If you're in danger right now"),
  ("what-is-fv","What counts as family violence?"),
  ("protection-orders","Protection orders: AVOs and DVOs"),
  ("parenting","How it affects parenting matters"),
  ("mediation-exempt","Mediation and family violence"),
  ("property","Does it affect property settlement?"),
  ("support","Where to get support")],
 key_takeaway("Family violence is treated very seriously in Australian family law. Protection orders (AVOs/DVOs) can keep you safe, and family violence affects parenting decisions, where the child's safety overrides other considerations. It's also a recognised exemption from compulsory mediation. If you're in immediate danger, call 000. For support, 1800RESPECT is available 24/7.")
 + f"""
<h2 id="safety-first">If you're in danger right now</h2>
<p>If you or your children are in immediate danger, call <strong>000</strong> now. For confidential counselling and support at any hour, contact {cite("respect_1800")} (1800 737 732), the national family and domestic violence service. Your safety is the priority \u2014 everything else can follow.</p>
"""
 + inline_cta("If it's safe to do so, talk to us confidentially about protecting yourself and your children.")
 + """
<h2 id="what-is-fv">What counts as family violence?</h2>
<p>Family violence is broader than physical harm. It includes behaviour that makes a family member fear for their safety or wellbeing, such as: physical or sexual assault; threats and intimidation; emotional or psychological abuse; financial control or deprivation; coercive control; stalking; and exposing children to any of these. Recognising the full scope matters, because non-physical abuse is just as relevant in family law.</p>

<h2 id="protection-orders">Protection orders: AVOs and DVOs</h2>
<p>Protection orders go by different names across states \u2014 Apprehended Violence Orders (AVOs) in NSW, Domestic Violence Orders (DVOs) in Queensland, Intervention Orders in Victoria and SA \u2014 but they do the same thing: legally restrict an abusive person's behaviour to protect you. Breaching one is a criminal offence. These orders operate alongside family law proceedings and can shape parenting arrangements.</p>
"""
 + callout("Protection orders and parenting orders interact",
   "A protection order can affect existing or proposed parenting arrangements. Courts work to ensure parenting orders don't expose anyone to violence \u2014 the two systems are designed to work together for safety.")
 + f"""
<h2 id="parenting">How it affects parenting matters</h2>
<p>In any parenting decision, the {cite("family_law_act")} makes protecting the child from harm a primary consideration \u2014 and where the benefit of a relationship with both parents conflicts with safety, <strong>safety prevails</strong>. Family violence can affect who a child lives with, whether time is supervised, and how changeovers happen. The court can order supervised contact or, where necessary, no contact.</p>

<h2 id="mediation-exempt">Mediation and family violence</h2>
<p>Mediation requires both parties to participate safely and on a relatively even footing \u2014 which family violence can make impossible. That's why family violence is a recognised <strong>exemption</strong> from the usual requirement to attempt family dispute resolution before court, under the {cite("fcfcoa_fdr")} framework. Where mediation does proceed in sensitive cases, shuttle or online formats can keep parties entirely separate. We always assess safety before recommending mediation. <a href="/mediation-with-a-narcissist/">See mediation in high-conflict situations \u2192</a></p>
"""
 + inline_cta("Not sure whether mediation is safe in your situation? We'll give you an honest assessment, confidentially.")
 + """
<h2 id="property">Does it affect property settlement?</h2>
<p>It can. Where family violence has made contributions significantly more difficult \u2014 for example, where abuse affected a person's ability to work or participate \u2014 this can be relevant to how contributions are assessed in a property settlement. Financial abuse in particular is increasingly recognised. <a href="/property-settlement-after-separation/">See how property settlement works \u2192</a></p>

<h2 id="support">Where to get support</h2>
<p>You don't have to navigate this alone. Beyond 000 in an emergency, 1800RESPECT offers 24/7 confidential support, and specialist family violence services operate in every state. When you're ready and it's safe, we can help you understand your legal options and the safest path forward \u2014 including protection, parenting and property. <a href="/contact-us/">Reach out confidentially \u2192</a></p>
<p class="source-note">If you are in immediate danger, call 000. Support: 1800RESPECT (1800 737 732), available 24 hours.</p>
"""
 ,
 [("What counts as family violence in Australia?",
   "More than physical harm \u2014 it includes threats, emotional and psychological abuse, financial control, coercive control, stalking, and exposing children to violence."),
  ("What is the difference between an AVO and a DVO?",
   "They're the same kind of protection order under different state names \u2014 AVO in NSW, DVO in Queensland, Intervention Order in Victoria and SA. All legally restrict an abusive person's behaviour."),
  ("Do I have to attend mediation if there's family violence?",
   "No. Family violence is a recognised exemption from compulsory family dispute resolution. Where mediation does occur, shuttle or online formats can keep parties separate."),
  ("Does domestic violence affect parenting orders?",
   "Yes. Protecting the child from harm is a primary consideration, and safety overrides the benefit of a relationship with both parents. Courts can order supervised or no contact."),
  ("Where can I get help for family violence?",
   "Call 000 in an emergency. 1800RESPECT (1800 737 732) offers 24/7 confidential support, and specialist services operate in every state.")],
 [("mediation-with-a-narcissist","High-Conflict Mediation"),
  ("parenting-plan-mediation","Parenting Plan Mediation"),
  ("property-settlement-after-separation","Property Settlement"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("family-law-mediation","Family Law Mediation"),
  ("contact-us","Contact Us")],
 read_min=10)
print("domestic-violence-and-family-law built")
