"""gen_blog_batch40.py: child-support-arrears-australia, family-report-explained.
Facts checked against Family Law Act 1975 (Cth) as amended by the Family Law
Amendment Act 2023 (in force 6 May 2024), Child Support (Assessment) Act 1989,
Child Support (Registration and Collection) Act 1988, and s 11F Family Law Act
(family reports / family consultants, Nov 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite

# ── POST 1: child-support-arrears-australia ─────────────────────────────────

csa_body = (
  key_takeaway("If your ex is not paying child support, Services Australia can enforce payment through "
               "tax refund interception, employer withholding, departure prohibition orders and even "
               "court-imposed penalties. You do not have to chase arrears yourself. Where the dispute "
               "is about the amount, not the obligation, mediation can resolve it faster and cheaper "
               "than a change-of-assessment application.")
  + f"""
<h2 id="how-child-support-works">How child support collection works in Australia</h2>
<p>Child support in Australia is administered by the Child Support Agency, which sits within {cite('services_australia_cs')}. Parents can choose one of two collection methods:</p>
<ul>
  <li><strong>Agency collect (Child Support Collect).</strong> Services Australia calculates the amount and collects it from the paying parent, forwarding payments to the receiving parent. If the payer falls behind, the agency has broad enforcement powers.</li>
  <li><strong>Private collect (self-manage).</strong> Parents transfer payments directly between themselves. If the payer stops, the receiving parent can ask Services Australia to switch to agency collect and recover up to three months of arrears, or nine months in special circumstances.</li>
</ul>
<p>Most enforcement tools are only available under agency collect. If you are privately collecting and your ex stops paying, the first step is usually to contact Services Australia and ask to move to agency collect.</p>
"""
  + inline_cta("Struggling with unpaid child support? We can help you understand your options before you escalate.")
  + f"""
<h2 id="enforcement-powers">How Services Australia enforces unpaid child support</h2>
<p>Services Australia has some of the strongest debt-recovery powers of any government agency. Under the Child Support (Registration and Collection) Act 1988, enforcement options include:</p>
<figure class="tbl"><table><caption>Child support enforcement powers (2026)</caption>
<thead><tr><th>Enforcement tool</th><th>How it works</th><th>When it is used</th></tr></thead>
<tbody>
<tr><td>Employer withholding</td><td>Services Australia directs the payer's employer to deduct child support from wages before they are paid</td><td>Default method under agency collect</td></tr>
<tr><td>Tax refund interception</td><td>The ATO redirects part or all of the payer's tax refund to cover arrears</td><td>When arrears exist at tax-return time</td></tr>
<tr><td>Departure prohibition order (DPO)</td><td>Prevents the payer from leaving Australia until the debt is paid or a payment plan is agreed</td><td>Persistent non-payment and a risk of flight</td></tr>
<tr><td>Lump-sum payment order</td><td>A court orders the payer to make a lump-sum payment from an asset, such as a property or investment</td><td>Where the payer has assets but claims no income</td></tr>
<tr><td>Third-party debt notice</td><td>Services Australia directs a bank or other third party to pay the debt from the payer's account</td><td>When other methods have failed</td></tr>
<tr><td>Court-ordered penalties</td><td>A court can impose fines or, in extreme cases, imprisonment for persistent non-compliance</td><td>Last resort after all other methods</td></tr>
</tbody></table></figure>
<p class="source-note">Based on the Child Support (Registration and Collection) Act 1988 (Cth). General information only, not legal advice.</p>
<p>The {cite('services_australia_cs')} website explains each option and how to request enforcement action. In most cases, you do not need a lawyer to trigger enforcement — Services Australia does it on your behalf.</p>
"""
  + inline_cta("Not sure which enforcement path fits your situation? Book a free consultation to talk it through.")
  + f"""
<h2 id="switching-to-agency-collect">Switching from private collect to agency collect</h2>
<p>If you have been privately collecting child support and your ex falls behind, you can ask Services Australia to take over collection. When you switch:</p>
<ul>
  <li>Services Australia can recover up to <strong>three months of arrears</strong> that accrued under private collect, or up to nine months if special circumstances apply.</li>
  <li>Future payments are collected through employer withholding or direct deduction, so you no longer have to chase your ex.</li>
  <li>Any arrears older than three months (or nine months in special cases) under private collect are written off — they cannot be recovered through the agency.</li>
</ul>
<p>This three-month limit is one of the most common traps for parents who privately collect. If your ex is weeks behind, do not wait months to act — the sooner you switch, the more you can recover.</p>
"""
  + inline_cta("Thinking about switching to agency collect? Get advice on timing and what you can recover.")
  + f"""
<h2 id="departure-prohibition-orders">Departure prohibition orders explained</h2>
<p>A departure prohibition order (DPO) is one of the most powerful tools available. It prevents the paying parent from leaving Australia — their passport is effectively flagged at the border. Services Australia can issue a DPO without a court order if:</p>
<ul>
  <li>the payer has an outstanding child support debt;</li>
  <li>the payer has persistently failed to pay; and</li>
  <li>there is a reasonable belief the payer may leave Australia.</li>
</ul>
<p>The payer can have the DPO lifted by paying the debt in full, entering into a satisfactory payment arrangement, or providing security (such as a bank guarantee) for the debt. A DPO does not affect the payer's ability to work in Australia, only their ability to travel overseas.</p>
<p>DPOs are more common than many parents realise. If your ex regularly travels internationally while owing child support, raising this with Services Australia can prompt swift action.</p>
"""
  + inline_cta("Is your ex travelling while owing child support? Find out what enforcement options you have.")
  + f"""
<h2 id="change-of-assessment">When the dispute is about the amount, not the payment</h2>
<p>Sometimes the real issue is not that a parent refuses to pay, but that the assessed amount does not reflect reality. The paying parent may have lost a job, started a new business, or had another child. The receiving parent may believe the payer's income is higher than assessed. In these cases, either parent can apply to Services Australia for a {cite('sa_change_assessment')}.</p>
<p>A change-of-assessment application is decided by a Senior Case Officer. Grounds include:</p>
<ul>
  <li>the payer's income is significantly higher or lower than the tax return suggests;</li>
  <li>the payer's earning capacity is not being used (e.g. choosing not to work);</li>
  <li>there are high costs of contact, such as interstate travel for visits;</li>
  <li>there are special needs of the child, such as medical or educational expenses;</li>
  <li>the assessment is otherwise unfair because of special circumstances.</li>
</ul>
<p>The process takes 6–12 weeks on average and can be stressful. Where both parents are willing to negotiate, mediation can often resolve the underlying disagreement about income, expenses or care far more quickly.</p>
"""
  + inline_cta("Disputing the child support amount? Mediation resolves it in weeks, not months.")
  + f"""
<h2 id="non-agency-payments">Non-agency payments and credits</h2>
<p>Some paying parents provide support directly — school fees, sports registrations, clothing, medical bills — and expect credit against their child support liability. Under {cite('sa_non_agency')}, certain direct payments can count as child support if both parents agree in writing or if the payment falls within prescribed categories such as:</p>
<ul>
  <li>child care fees;</li>
  <li>school fees and school uniforms;</li>
  <li>essential medical and dental costs; and</li>
  <li>housing costs where the child resides.</li>
</ul>
<p>Up to 30% of the assessed liability can be credited through non-agency payments. If you are paying directly for things the child needs, it is important to get the credit arrangement right — otherwise you may still owe the full assessed amount.</p>
"""
  + inline_cta("Paying school fees but still getting chased for arrears? A mediator can help you sort the credits.")
  + f"""
<h2 id="binding-agreements">Child support agreements as an alternative</h2>
<p>Parents who cannot agree through the formula process can enter a binding child support agreement or a limited child support agreement. A binding agreement overrides the formula entirely and requires both parents to have independent legal advice. A limited agreement must be for at least the formula amount and can be ended by either parent after three years.</p>
<p>Agreements are especially useful where:</p>
<ul>
  <li>one parent wants to pay more than the formula in exchange for certainty;</li>
  <li>parents want to include non-cash items such as school fees, mortgage contributions or health insurance;</li>
  <li>there is a property settlement that takes child support into account; or</li>
  <li>the parents want to avoid the stress of annual reassessments.</li>
</ul>
<p>A binding child support agreement, unlike a limited agreement, can only be set aside by a court. Our <a href="/child-support-guide/">child support guide</a> explains both types in detail. The {cite('family_law_act')} sets out the requirements for each.</p>
"""
  + inline_cta("Want certainty on child support? A binding agreement, agreed in mediation, can deliver it.")
  + f"""
<h2 id="mediation-for-child-support">How mediation resolves child support disputes</h2>
<p>Child support disputes are some of the most emotionally charged in family law. The numbers feel personal — they represent what each parent believes the child needs and what they can afford. Court processes and change-of-assessment applications can deepen the conflict.</p>
<p>Mediation lets both parents:</p>
<ul>
  <li>discuss the child's actual needs openly, with a neutral third party;</li>
  <li>explore creative solutions like direct payment of school fees, shared health insurance, or lump-sum top-ups;</li>
  <li>agree on how to handle future changes (new jobs, new partners, school transitions) without relitigating;</li>
  <li>put the agreement in writing as a child support agreement or as part of broader consent orders; and</li>
  <li>use shuttle mediation if direct conversation is too difficult.</li>
</ul>
<p>The {cite('ag_fdr')} explains the role of family dispute resolution across all family law matters. If you are experiencing family and domestic violence, confidential support is available through 1800RESPECT on 1800 737 732. If you are in immediate danger, call 000.</p>
"""
  + inline_cta("Resolve the child support dispute, not just the debt. Book a free, confidential consultation.")
)

csa_qa = [
 ("What happens if my ex doesn't pay child support?",
  "If you are on agency collect, Services Australia can enforce payment through employer withholding, tax refund interception, departure prohibition orders and court action. If you are on private collect, you can ask to switch to agency collect and recover up to three months of arrears."),
 ("Can my ex go to jail for not paying child support?",
  "In extreme cases, yes. A court can impose a term of imprisonment for persistent, deliberate non-compliance after all other enforcement methods have been exhausted. It is rare and always a last resort."),
 ("How far back can child support arrears be collected?",
  "Under agency collect, there is no time limit — arrears accumulate and remain enforceable. Under private collect, if you switch to agency collect, Services Australia can recover up to three months of arrears, or nine months in special circumstances."),
 ("Can child support be changed if my ex earns more now?",
  "Yes. Either parent can apply to Services Australia for a change of assessment in special circumstances, or you can agree a new arrangement through mediation and formalise it as a child support agreement."),
 ("Can a departure prohibition order stop my ex from travelling?",
  "Yes. Services Australia can issue a DPO that prevents the paying parent from leaving Australia until the debt is paid, a payment plan is agreed, or security is provided."),
]

post(
  "child-support-arrears-australia",
  "Child Support Arrears Australia: Enforcement Guide",
  "What to do when your ex won't pay child support. Enforcement powers, departure prohibition orders, switching to agency collect, and how mediation resolves disputes.",
  "Parenting",
  "Child support arrears in Australia: <em>your enforcement options</em>",
  "Services Australia has broad powers to enforce unpaid child support, from employer withholding to departure prohibition orders. Here is how enforcement works, what you can recover, and when mediation resolves the underlying dispute faster.",
  [("how-child-support-works", "How child support collection works"),
   ("enforcement-powers", "Enforcement powers"),
   ("switching-to-agency-collect", "Switching to agency collect"),
   ("departure-prohibition-orders", "Departure prohibition orders"),
   ("change-of-assessment", "Disputes about the amount"),
   ("non-agency-payments", "Non-agency payments and credits"),
   ("binding-agreements", "Child support agreements"),
   ("mediation-for-child-support", "How mediation resolves it")],
  csa_body, csa_qa,
  [("child-support-guide", "Child Support in Australia"),
   ("property-settlement-after-separation", "Property Settlement After Separation"),
   ("consent-orders-explained", "Consent Orders Explained"),
   ("who-pays-school-fees-after-separation", "Who Pays School Fees After Separation"),
   ("co-parenting-mediation", "Co-Parenting Mediation"),
   ("how-much-does-mediation-cost", "How Much Does Mediation Cost?")],
  read_min=9,
)
print("child-support-arrears-australia built")

# ── POST 2: family-report-explained ────────────────────────────────────────

fr_body = (
  key_takeaway("A family report is a written assessment by a family consultant (usually a psychologist "
               "or social worker) ordered by the court in parenting disputes. The consultant interviews "
               "both parents and the children, observes interactions, and makes recommendations about "
               "what parenting arrangements are in the child's best interests. Family reports carry "
               "significant weight with judges. Understanding the process, and preparing well, can "
               "make a real difference to the outcome.")
  + f"""
<h2 id="what-is-a-family-report">What is a family report?</h2>
<p>A family report is an independent, expert assessment prepared under section 11F of the {cite('family_law_act')}. The court orders a family report when it needs an objective view of the family's circumstances before making parenting orders. The report is prepared by a <strong>family consultant</strong> — a qualified psychologist, social worker or counsellor appointed by the court.</p>
<p>The report typically covers:</p>
<ul>
  <li>each parent's relationship with the child;</li>
  <li>the child's wishes, expressed in age-appropriate ways;</li>
  <li>each parent's capacity to provide for the child's needs;</li>
  <li>any risks, including family violence, substance misuse or mental health concerns;</li>
  <li>the child's developmental, emotional and educational needs; and</li>
  <li>recommendations about living arrangements, time and decision-making.</li>
</ul>
<p>Family reports are used in both interim (temporary) and final hearings. They are one of the most influential pieces of evidence in parenting proceedings — judges rely heavily on the consultant's professional assessment.</p>
"""
  + inline_cta("Facing a family report? Talk to a mediator first — many parents settle before it's needed.")
  + f"""
<h2 id="when-ordered">When does the court order a family report?</h2>
<p>The court can order a family report at any stage of parenting proceedings, but it most commonly happens:</p>
<ul>
  <li>at the first court event (such as a case assessment conference or procedural hearing), when the judge identifies that the dispute needs expert input;</li>
  <li>where there are allegations of family violence, abuse or risk to the child;</li>
  <li>where parents have very different accounts of the child's wishes or needs;</li>
  <li>where a child has special needs, a disability or complex health issues; and</li>
  <li>where there is a significant dispute about relocation or sole parental responsibility.</li>
</ul>
<p>The {cite('fcfcoa')} manages the family report process through its Child Dispute Services. Court-ordered family reports are prepared at no cost to the parties — they are funded by the court. If you want a report outside the court process, you can commission a private family report from an independent psychologist, but these cost $5,000–$15,000 or more.</p>
"""
  + inline_cta("A family report adds months and stress. See if mediation can resolve your dispute first.")
  + f"""
<h2 id="the-process">What happens during a family report assessment</h2>
<p>The family report process typically follows these steps:</p>
<ol>
  <li><strong>Court order.</strong> The judge orders the report and specifies the issues it should address.</li>
  <li><strong>Appointment scheduling.</strong> Child Dispute Services contacts both parents to arrange interviews, usually within 4–8 weeks of the order.</li>
  <li><strong>Individual interviews.</strong> The consultant meets each parent separately for 1–2 hours. They ask about your relationship with the child, your concerns, your proposed arrangements, and your view of the other parent's strengths and weaknesses.</li>
  <li><strong>Child interview.</strong> The consultant speaks to the child (if old enough) in a child-friendly setting, using play, drawing or conversation to understand the child's experience.</li>
  <li><strong>Observation sessions.</strong> The consultant may observe each parent interacting with the child, often at the court's premises.</li>
  <li><strong>Collateral contacts.</strong> The consultant may speak to teachers, GPs, therapists or other relevant people, with the parents' consent.</li>
  <li><strong>Report writing.</strong> The consultant writes the report and files it with the court. Both parties receive a copy, usually 4–8 weeks after the last interview.</li>
</ol>
<figure class="tbl"><table><caption>Family report process: typical timeline (2026)</caption>
<thead><tr><th>Stage</th><th>Typical timeframe</th></tr></thead>
<tbody>
<tr><td>Court order to first interview</td><td>4 – 8 weeks</td></tr>
<tr><td>Interview process (all sessions)</td><td>2 – 6 weeks</td></tr>
<tr><td>Report writing and filing</td><td>4 – 8 weeks</td></tr>
<tr><td><strong>Total: order to report</strong></td><td><strong>10 – 22 weeks</strong></td></tr>
</tbody></table></figure>
<p class="source-note">Indicative timeframes only. Wait times vary by court location and consultant availability.</p>
"""
  + inline_cta("The family report process takes months. Mediation can resolve your dispute in weeks.")
  + f"""
<h2 id="how-to-prepare">How to prepare for a family report interview</h2>
<p>Your interview with the family consultant is not a test, but it is an opportunity to show that you are a thoughtful, child-focused parent. Practical preparation includes:</p>
<ul>
  <li><strong>Focus on the child.</strong> Talk about your child's needs, routine, friendships, school and interests — not just the conflict with the other parent.</li>
  <li><strong>Be honest.</strong> Consultants are trained to spot exaggeration. Acknowledge your own imperfections and the other parent's strengths where they exist.</li>
  <li><strong>Stay calm and respectful.</strong> How you present matters. Anger, hostility towards the other parent, or badmouthing them will be noted.</li>
  <li><strong>Bring evidence quietly.</strong> If there are safety concerns (family violence, substance misuse), bring police reports, intervention orders or medical records. Do not dump a folder of trivial complaints.</li>
  <li><strong>Prepare your proposed arrangements.</strong> Be ready to explain what schedule you want, why it suits the child, and how you would handle transitions, holidays and decision-making.</li>
  <li><strong>Do not coach your child.</strong> Consultants can tell when a child has been coached, and it reflects badly on the parent who did it. Let your child speak freely.</li>
</ul>
<p>If your child is seeing a psychologist or counsellor, let the consultant know — with consent, they may contact that professional for context.</p>
"""
  + inline_cta("Want to be fully prepared? A mediator can help you clarify your position before the interview.")
  + f"""
<h2 id="what-consultants-assess">What the family consultant is looking for</h2>
<p>The consultant assesses the family against the best-interests factors in section 60CC of the {cite('family_law_act')}. Since the 2024 amendments, the primary consideration is:</p>
<ul>
  <li><strong>Safety.</strong> The safety of the child and of each parent or carer. Family violence, abuse and risk come first.</li>
</ul>
<p>Additional considerations include:</p>
<ul>
  <li>the views of the child, given weight according to their age and maturity;</li>
  <li>the developmental, psychological, emotional and cultural needs of the child;</li>
  <li>the capacity of each parent to provide for those needs;</li>
  <li>the benefit to the child of a relationship with both parents, where it is safe;</li>
  <li>each parent's attitude to the child's relationship with the other parent; and</li>
  <li>anything else that is relevant.</li>
</ul>
<p>Consultants also look for <strong>patterns</strong> rather than isolated incidents: a parent who has consistently attended school events, medical appointments and extracurricular activities demonstrates involvement more credibly than one who starts doing so only after proceedings begin.</p>
"""
  + inline_cta("Understanding what the consultant looks for can help you present your best case. Talk to us.")
  + f"""
<h2 id="challenging-a-family-report">Can you challenge a family report?</h2>
<p>A family report is evidence, not a court order. It carries significant weight, but it is not binding. If you disagree with the report's findings or recommendations, you can:</p>
<ul>
  <li><strong>Cross-examine the consultant</strong> at the hearing. Your lawyer (or you, if self-represented) can ask the consultant to explain their methodology, challenge their conclusions, and test whether they considered all the evidence.</li>
  <li><strong>Commission a private report</strong> from an independent psychologist. The court may give it less weight than its own report, but it provides an alternative expert view.</li>
  <li><strong>Present other evidence</strong> that contradicts the report, such as school records, medical evidence, or testimony from people who know the family well.</li>
  <li><strong>Ask the court for a supplementary report</strong> if there has been a significant change in circumstances since the original report was prepared.</li>
</ul>
<p>Challenging a family report is expensive and difficult. Courts start from a position of trusting their own consultants. It is worth challenging only if there is a genuine error or if the consultant missed something important — not simply because the report favours the other parent.</p>
<p>See our guide to the <a href="/family-court-process/">family court process</a> for how the report fits into the broader proceedings. The {cite('fcfcoa_safety_risk')} page explains how the court assesses safety and risk in children's matters.</p>
"""
  + inline_cta("Unhappy with a family report? A mediator can help you negotiate despite it.")
  + f"""
<h2 id="private-family-reports">Private family reports</h2>
<p>Parents sometimes commission a private family report (also called a single expert report) outside the court process. This can be useful if:</p>
<ul>
  <li>you are in mediation and want an independent expert view to inform the negotiation;</li>
  <li>you want to understand what a court-ordered report might say before you decide whether to litigate;</li>
  <li>there is a specific clinical question, such as the impact of a parent's mental health on the child.</li>
</ul>
<figure class="tbl"><table><caption>Court-ordered vs private family reports (2026)</caption>
<thead><tr><th>Feature</th><th>Court-ordered report</th><th>Private report</th></tr></thead>
<tbody>
<tr><td>Cost</td><td>Free (court-funded)</td><td>$5,000 – $15,000+</td></tr>
<tr><td>Ordered by</td><td>The court</td><td>One or both parents</td></tr>
<tr><td>Consultant</td><td>Court-appointed family consultant</td><td>Independent psychologist chosen by the parties</td></tr>
<tr><td>Weight in court</td><td>High — the court trusts its own process</td><td>Varies — less weight if only one parent participated</td></tr>
<tr><td>Timeframe</td><td>10 – 22 weeks</td><td>4 – 12 weeks (depending on the expert)</td></tr>
</tbody></table></figure>
<p class="source-note">Indicative only. Private report costs depend on the expert and the complexity of the case.</p>
<p>A private report is strongest when both parents agree to participate. A report based on only one parent's interview and the child's interview carries less weight because the consultant has not assessed the other parent.</p>
"""
  + inline_cta("Considering a private report? Discuss your options with a mediator first.")
  + f"""
<h2 id="avoiding-a-family-report">Settling in mediation to avoid a family report altogether</h2>
<p>A family report is only necessary when parents cannot agree. If you can resolve your parenting dispute in mediation, you avoid the report entirely — and the months of waiting, the stress of being assessed, and the risk of an unfavourable recommendation.</p>
<p>Mediation lets you:</p>
<ul>
  <li>design parenting arrangements that reflect your child's actual needs, not a consultant's snapshot;</li>
  <li>address the concerns that would otherwise be raised in a report — safety, communication, routine — directly;</li>
  <li>use shuttle mediation if you cannot be in the same room as the other parent;</li>
  <li>agree a parenting plan or draft consent orders that become binding once filed; and</li>
  <li>include review points so the arrangement evolves as your child grows.</li>
</ul>
<p>The {cite('ag_fdr')} explains the role of family dispute resolution before parenting applications. Even if proceedings have started, it is never too late to mediate — many parents settle after a family report is ordered but before it is completed. If you are experiencing family and domestic violence, confidential support is available through 1800RESPECT on 1800 737 732. If you are in immediate danger, call 000.</p>
"""
  + inline_cta("Avoid the stress of a family report. Book a free, confidential mediation consultation today.")
)

fr_qa = [
 ("What is a family report in Australian family law?",
  "A family report is an independent assessment by a court-appointed family consultant — usually a psychologist or social worker — who interviews both parents and the children and makes recommendations about parenting arrangements in the child's best interests."),
 ("How long does a family report take?",
  "From the court order to the finished report, expect 10 to 22 weeks. Wait times depend on court location and consultant availability."),
 ("Does a family report decide the outcome?",
  "No, the report is evidence, not a decision. However, judges give it significant weight because it represents an independent expert assessment. It is one of the most influential documents in parenting proceedings."),
 ("Can I challenge a family report I disagree with?",
  "Yes. You can cross-examine the consultant at the hearing, commission a private report, or present other evidence. However, challenging a court report is expensive and courts trust their own process, so it is worth doing only if there is a genuine error or omission."),
 ("How much does a private family report cost?",
  "A private report from an independent psychologist typically costs $5,000 to $15,000 or more, depending on the expert and the complexity of the case. Court-ordered reports are free."),
 ("Can I avoid a family report by settling in mediation?",
  "Yes. A family report is only needed when parents cannot agree. If you resolve your dispute in mediation, you skip the report entirely and can formalise your agreement as a parenting plan or consent orders."),
]

post(
  "family-report-explained",
  "Family Reports Explained: What to Expect (2026)",
  "What a family report is in Australian family law, when courts order one, the interview process, how to prepare, and how mediation can help you avoid it.",
  "Parenting",
  "Family reports explained: <em>the assessment that shapes parenting orders</em>",
  "A family report is one of the most influential documents in a parenting dispute. Here is what happens during the assessment, how to prepare, and why settling in mediation can mean you never need one.",
  [("what-is-a-family-report", "What is a family report?"),
   ("when-ordered", "When the court orders one"),
   ("the-process", "The assessment process"),
   ("how-to-prepare", "How to prepare"),
   ("what-consultants-assess", "What consultants look for"),
   ("challenging-a-family-report", "Challenging a family report"),
   ("private-family-reports", "Private family reports"),
   ("avoiding-a-family-report", "Settling to avoid one")],
  fr_body, fr_qa,
  [("family-court-process", "The Family Court Process"),
   ("child-custody-mediation", "Child Custody Mediation"),
   ("sole-parental-responsibility-australia", "Sole Parental Responsibility"),
   ("domestic-violence-and-family-law", "Domestic Violence and Family Law"),
   ("parenting-plans-guide", "Parenting Plans Guide"),
   ("how-much-does-mediation-cost", "How Much Does Mediation Cost?")],
  read_min=9,
)
print("family-report-explained built")
