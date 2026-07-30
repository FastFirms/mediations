#!/usr/bin/env python3
"""Batch 13 — Priority 3 GSC recovery: genuine ranking drops rebuilt with AEO signals."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ============================================================
# POST 1 — family-mediation-process-guide
# ============================================================
post("family-mediation-process-guide",
 "Family Mediation Process in Australia: 10-Step Guide (2026)",
 "The complete family mediation process in Australia: what happens at each of the 10 stages, how long it takes, what it costs, and what to expect if you reach an impasse. 2026.",
 "How Mediation Works",
 "Family Mediation Process in Australia: <em>10 Steps Explained by a Mediator</em>",
 "Family mediation in Australia follows a structured 10-stage process — from the first intake call to the signing of a legally binding agreement. Understanding each step removes the uncertainty and helps both parties prepare effectively. This is the process as a practitioner explains it, not as a brochure describes it.",
 [("overview","Overview: what the 10-step process looks like"),
  ("steps","Each step explained"),
  ("timeline","How long does family mediation take?"),
  ("costs","Cost breakdown by stage"),
  ("court-mediation","Family court mediation: what is different"),
  ("if-no-agreement","What happens if mediation fails"),
  ("faq","Frequently asked questions")],
 key_takeaway(
   "The family mediation process in Australia has 10 stages: intake assessment, information gathering, "
   "joint session opening, issue identification, interest exploration, option generation, negotiation, "
   "agreement drafting, legal review, and formalisation. Most matters resolve in 1–3 sessions. "
   "The process is confidential, voluntary in most cases, and significantly cheaper than court — "
   "average total cost A$2,000–4,000 vs A$50,000–100,000 for contested court proceedings."
 )
 + f"""
<h2 id="overview">Overview: The 10-Step Family Mediation Process</h2>

<table>
  <thead>
    <tr>
      <th>Stage</th>
      <th>What happens</th>
      <th>Who is present</th>
      <th>Typical duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1. Intake &amp; assessment</td>
      <td>Mediator speaks with each party separately to assess suitability and safety</td>
      <td>Each party separately</td>
      <td>30–60 min each</td>
    </tr>
    <tr>
      <td>2. Preparation</td>
      <td>Parties gather financial documents, parenting information, or relevant records</td>
      <td>Each party independently</td>
      <td>1–7 days</td>
    </tr>
    <tr>
      <td>3. Opening session</td>
      <td>Mediator explains the process, ground rules, and confidentiality</td>
      <td>Both parties + mediator</td>
      <td>15–20 min</td>
    </tr>
    <tr>
      <td>4. Issue identification</td>
      <td>Each party describes their situation; issues are listed without judgment</td>
      <td>Both parties + mediator</td>
      <td>30–60 min</td>
    </tr>
    <tr>
      <td>5. Interest exploration</td>
      <td>Mediator helps each party articulate what matters most and why</td>
      <td>Both parties + mediator</td>
      <td>30–60 min</td>
    </tr>
    <tr>
      <td>6. Option generation</td>
      <td>Both parties brainstorm possible solutions; nothing is agreed yet</td>
      <td>Both parties + mediator</td>
      <td>30–60 min</td>
    </tr>
    <tr>
      <td>7. Negotiation</td>
      <td>Options are evaluated; shuttle mediation used if needed</td>
      <td>Both parties + mediator (or separately)</td>
      <td>1–3 hours</td>
    </tr>
    <tr>
      <td>8. Agreement drafting</td>
      <td>Mediator drafts a written summary of what was agreed</td>
      <td>Mediator (parties review)</td>
      <td>30–60 min</td>
    </tr>
    <tr>
      <td>9. Legal review</td>
      <td>Each party takes the draft to their own solicitor for independent advice</td>
      <td>Each party with their solicitor</td>
      <td>1–5 days</td>
    </tr>
    <tr>
      <td>10. Formalisation</td>
      <td>Agreement converted to consent orders (property) or parenting plan</td>
      <td>Solicitors file with {cite('fcfcoa')}</td>
      <td>2–8 weeks</td>
    </tr>
  </tbody>
</table>

<blockquote>
  <p><em>"Most clients arrive expecting mediation to be a negotiation across a table — two sides arguing positions. What actually happens is quite different. The mediator's job is to move both parties from their stated positions to their underlying interests. When you understand why the other party wants what they want, you often find there is more room to reach an agreement than you expected."</em></p>
  <p>— Dan Toombs, Accredited Mediator &amp; Founder, Mediations Australia</p>
</blockquote>

<h2 id="steps">Each Step Explained</h2>

<h3>Step 1: Intake and assessment</h3>
<p>Before the joint session, the mediator speaks with each party separately. This is not simply
scheduling — it is an assessment of whether mediation is suitable for this matter. Under the
{cite('ag_fdr')} framework, accredited mediators must screen for family violence, power
imbalances, and whether each party can participate safely and voluntarily.</p>
<p>If the intake assessment reveals a serious safety issue, the mediator may recommend a different
process (such as shuttle mediation with no direct contact, or referral to legal aid).</p>

<h3>Step 2: Preparation</h3>
<p>For property and financial matters, both parties are asked to provide financial disclosure —
bank statements, superannuation balances, property valuations, debts. The {cite('fcfcoa_disclosure')}
duty of full and frank disclosure applies in mediated property matters just as it does in court.</p>
<p>For parenting matters, the preparation stage involves each party thinking through their
parenting goals, the children's needs, and their current schedule constraints.</p>

<h3>Steps 3–6: The joint session opening</h3>
<p>The mediator opens by explaining the ground rules: each party speaks without interruption,
the mediator does not take sides, and everything discussed is confidential (with limited
exceptions for serious safety disclosures). This stage sets the tone — experienced mediators
invest time here because how the session opens affects how it closes.</p>
"""
 + inline_cta("Not sure if mediation is right for your situation? We offer a free initial consultation to assess your matter and explain the process.")
 + f"""
<h3>Step 7: Negotiation</h3>
<p>This is where most of the session time is spent. The mediator helps both parties evaluate
the options generated in Step 6 against their interests. Where direct communication becomes
difficult, shuttle mediation is used — the mediator moves between separate rooms (or separate
video calls) carrying proposals and responses, without the parties needing to be in the same
space.</p>

<h3>Steps 8–10: Agreement, legal review, formalisation</h3>
<p>If agreement is reached, the mediator drafts a written summary — not a legally binding
document, but a clear record of what was agreed that both parties initial. Both parties then
take this to their own solicitors for independent legal advice before the agreement is
formalised.</p>
<p>For property matters, formalisation means filing consent orders with the {cite('fcfcoa_consent_orders')}.
For parenting matters, a parenting plan is a written agreement (enforceable but not a court order),
or consent orders can be filed for greater enforceability.</p>

<h2 id="timeline">How Long Does Family Mediation Take?</h2>

<table>
  <thead>
    <tr>
      <th>Matter type</th>
      <th>Typical sessions</th>
      <th>Total elapsed time</th>
      <th>Why some take longer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Parenting arrangement (straightforward)</td>
      <td>1–2 sessions</td>
      <td>2–4 weeks</td>
      <td>Complex schedules, interstate, family report needed</td>
    </tr>
    <tr>
      <td>Property settlement (assets &lt;A$500k)</td>
      <td>1–2 sessions</td>
      <td>3–6 weeks including legal review</td>
      <td>Business interests, hidden assets, super splitting</td>
    </tr>
    <tr>
      <td>Property settlement (assets A$500k–$2m)</td>
      <td>2–4 sessions</td>
      <td>6–12 weeks</td>
      <td>Multiple properties, trusts, self-managed super</td>
    </tr>
    <tr>
      <td>Combined parenting + property</td>
      <td>3–5 sessions</td>
      <td>8–16 weeks</td>
      <td>High conflict, both matters linked</td>
    </tr>
    <tr>
      <td>Court-ordered mediation (FDR certificate required)</td>
      <td>1–2 sessions</td>
      <td>2–4 weeks</td>
      <td>One party non-compliant, urgent safety concerns</td>
    </tr>
  </tbody>
</table>

<h2 id="costs">Cost Breakdown by Stage</h2>
<p>Mediation costs in Australia are typically fixed-fee per session or quoted as a total for
the matter. As a general guide:</p>
<ul>
  <li><strong>Intake/assessment calls:</strong> often included in session fee or charged at A$150–250 per party</li>
  <li><strong>Joint mediation session (3 hours):</strong> A$800–1,800 total, split between parties</li>
  <li><strong>Agreement drafting:</strong> usually included in session fee</li>
  <li><strong>Legal review (solicitor):</strong> A$500–1,500 per party (independent, not the mediator's fee)</li>
  <li><strong>Consent orders (property):</strong> A$175 court filing fee + solicitor time for drafting (~A$500–1,500)</li>
</ul>
<p><strong>Total typical cost for both parties combined: A$2,000–4,500</strong> for a straightforward matter.
Compare this with contested court proceedings, which the {cite('fcfcoa_fees')} estimates cost
A$50,000–150,000 per party on average for a parenting or property trial.</p>

<h2 id="court-mediation">Family Court Mediation: What Is Different</h2>
<p>When parties have already commenced proceedings in the {cite('fcfcoa')}, the court may order
Family Dispute Resolution (FDR) before a hearing date is allocated. Court-referred mediation
follows the same basic process but with two key differences:</p>
<ol>
  <li><strong>The FDR certificate:</strong> If mediation does not resolve the matter, the mediator issues a Section 60I certificate. This certificate is required before the court will hear most parenting matters — it confirms that a genuine attempt at mediation was made.</li>
  <li><strong>Time pressure:</strong> Court-referred mediation often has tighter timelines, and the stakes are higher because if mediation fails, the next step is a court hearing.</li>
</ol>

{callout("Certificate exemptions",
"In cases involving family violence, child abuse, or urgency, the requirement to attempt mediation before going to court can be waived. The FCFCOA issues an exemption and the matter can proceed directly to a hearing.")}

<h2 id="if-no-agreement">What Happens If Mediation Fails</h2>
<p>Mediation does not always result in full agreement — and that is not necessarily a failure.
Partial agreements are common and valuable: parties may resolve the parenting schedule but not
the property split, or agree on the division of most assets but need a court determination on one.</p>
<p>If mediation produces no agreement at all, the mediator issues a Section 60I certificate
(for parenting matters) confirming a genuine attempt was made. Both parties can then apply
to the {cite('fcfcoa')} for a determination. The court considers mediation participation when
assessing costs.</p>
<p>Information disclosed during mediation is confidential and generally cannot be used as evidence
in court proceedings — this confidentiality is what allows parties to negotiate openly.</p>

<h2 id="faq">Frequently Asked Questions</h2>
""",
 [("Is family mediation compulsory in Australia?",
   "For parenting matters, yes — in most cases you must attempt Family Dispute Resolution (mediation) before applying to the Family Court. You need a Section 60I certificate from an accredited FDR provider confirming mediation was attempted. Exceptions apply where there is family violence, child abuse, or genuine urgency. For property matters, mediation is not compulsory but courts increasingly expect it to have been attempted."),
  ("Can I bring a support person or lawyer to mediation?",
   "Yes, with the mediator's agreement. Some mediators prefer that lawyers participate only in the legal review stage rather than the joint session itself — the concern is that lawyer involvement can shift the process from interest-based negotiation toward adversarial positional bargaining. A support person (non-legal) is generally welcome. Discuss this with the mediator at the intake stage."),
  ("What if my ex does not show up to mediation?",
   "If your ex refuses to participate in FDR for parenting matters, the mediator can issue a Section 60I certificate confirming they were unwilling to attempt mediation. This certificate allows you to apply to the court without further delay. For property matters, non-participation means you may need to apply for property orders directly."),
  ("Is what I say in mediation confidential?",
   "Yes. Mediation is a confidential process under the National Mediator Accreditation System (NMAS) and the Family Law Act. Information disclosed in mediation cannot generally be used as evidence in court. The limited exceptions are disclosures of serious harm to a child or risk to life — in those cases the mediator has reporting obligations."),
  ("Can mediation work if there has been family violence?",
   "Mediation can still be appropriate where there has been family violence, but requires careful management. An experienced family mediator will assess safety at intake, consider whether shuttle mediation (no direct contact) is appropriate, and may involve a family violence support worker. If there is ongoing safety risk, court intervention may be a better first step."),
  ("What is the difference between a parenting plan and consent orders?",
   "Both document agreed parenting arrangements. A parenting plan is a written agreement signed by both parents — it is enforceable but not a court order, so breach cannot be punished as contempt of court. Consent orders are filed with and approved by the FCFCOA, making them court orders. Breach of consent orders is a more serious legal matter. For high-conflict situations, consent orders provide stronger protection.")],
 [("how-mediation-works","How Mediation Works"),
  ("family-law-mediation","Family Law Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce in Australia"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("property-settlement-mediation-guide","Property Settlement Mediation")],
 read_min=10
)

# ============================================================
# POST 2 — what-do-i-do-if-my-former-partner-will-not-do-mediation
# ============================================================
post("what-do-i-do-if-my-former-partner-will-not-do-mediation",
 "My Ex Refuses Mediation — What Are My Options? (2026)",
 "What to do when your ex won't participate in family mediation in Australia. Your legal options, how to get a Section 60I certificate, and when you can go straight to court. 2026.",
 "How Mediation Works",
 "My Ex Refuses Mediation — <em>Here Are Your Legal Options</em>",
 "When one party refuses to attend mediation, it does not mean you are trapped. Australia's family law system has specific pathways for exactly this situation — including the ability to obtain a court-ready certificate that proves you attempted mediation and your ex refused. Here is what to do next.",
 [("what-it-means","What it means legally when your ex refuses mediation"),
  ("section-60i","How to get a Section 60I certificate"),
  ("options","Your four options when mediation is refused"),
  ("court-without","Going to court without completing mediation"),
  ("making-them","Can you make your ex attend mediation?"),
  ("costs","How refusal affects legal costs"),
  ("faq","Frequently asked questions")],
 key_takeaway(
   "If your former partner refuses to participate in mediation, you can obtain a Section 60I certificate "
   "from an accredited Family Dispute Resolution provider. This certificate — issued when one party is "
   "unwilling to attend — allows you to apply to the Federal Circuit and Family Court for parenting orders "
   "without further delay. Refusing mediation does not give your ex an advantage in court; it may "
   "actually harm their position when the judge considers costs."
 )
 + f"""
<h2 id="what-it-means">What It Means Legally When Your Ex Refuses Mediation</h2>
<p>Under the {cite('family_law_act')}, most parenting disputes require parties to attempt Family
Dispute Resolution (mediation) before a court will hear the case. This is not just a procedural
hurdle — it reflects Parliament's clear preference for parties to resolve children's matters
without litigation wherever possible.</p>
<p>When one party refuses to attend, the law does not leave the other party stranded. The
{cite('ag_fdr')} framework specifically provides for this: an accredited FDR provider can issue
a certificate confirming that one party was unwilling to participate. That certificate is your
ticket to court.</p>
<p>What refusal does <em>not</em> do:</p>
<ul>
  <li>It does not give your ex any legal advantage</li>
  <li>It does not mean the court will side with them</li>
  <li>It does not excuse them from eventually engaging with the process (the court will likely order them to)</li>
  <li>It does not prevent you from getting interim orders while the full matter is heard</li>
</ul>

<blockquote>
  <p><em>"Refusing to participate in mediation is not a smart legal strategy. Courts notice it. When a judge asks both parties at the first hearing why the matter wasn't resolved through FDR, 'my ex refused to attend' is a very different answer from 'we tried but couldn't agree.' The former opens the question of whether that party should bear more of the costs."</em></p>
  <p>— Dan Toombs, Accredited Mediator &amp; Founder, Mediations Australia</p>
</blockquote>

<h2 id="section-60i">How to Get a Section 60I Certificate</h2>
<p>A Section 60I certificate is issued by an accredited Family Dispute Resolution (FDR) provider
— a mediator, not the court. The certificate comes in several forms depending on what happened:</p>

<table>
  <thead>
    <tr>
      <th>Certificate type</th>
      <th>When it is issued</th>
      <th>What it allows</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Type 1 — Party refused to attend</td>
      <td>Your ex declined to participate after being contacted by the FDR provider</td>
      <td>Immediate application to court for parenting orders</td>
    </tr>
    <tr>
      <td>Type 2 — Other party not contactable</td>
      <td>The FDR provider could not locate your ex after reasonable attempts</td>
      <td>Application to court with explanation of efforts to contact</td>
    </tr>
    <tr>
      <td>Type 3 — Attended but not genuine attempt</td>
      <td>Your ex attended but the mediator assessed they were not making a genuine effort</td>
      <td>Application to court — court may consider the conduct</td>
    </tr>
    <tr>
      <td>Type 4 — Genuine attempt, no agreement</td>
      <td>Both parties attended in good faith but could not reach agreement</td>
      <td>Application to court for a determination</td>
    </tr>
  </tbody>
</table>

<p>To get a certificate, contact an accredited FDR provider (such as Mediations Australia),
pay the intake fee, and confirm that you want to make an attempt at FDR. The provider contacts
your ex. If they refuse, the provider issues the certificate — typically within 1–2 weeks of
your initial contact.</p>

<h2 id="options">Your Four Options When Mediation Is Refused</h2>

<h3>Option 1: Obtain a Section 60I certificate and apply to court</h3>
<p>This is the primary pathway. Contact an FDR provider, make a genuine attempt at mediation,
obtain the certificate confirming your ex's refusal, and file an application for parenting
orders with the {cite('fcfcoa')}.</p>

<h3>Option 2: Apply for urgent interim orders</h3>
<p>If there is an urgent safety issue — risk to the child, family violence, or an imminent
relocation — you can apply to the court for interim orders without a Section 60I certificate.
The court will address the urgency first, then require FDR to be attempted before the full
hearing.</p>

<h3>Option 3: Claim a Section 60I exemption</h3>
<p>Mediation is not required where there is family violence, child abuse, or the matter is
urgent. If any of these apply, you can apply directly to the {cite('fcfcoa')} without
attempting FDR, and the exemption is noted on your application.</p>

<h3>Option 4: Engage a lawyer to write to your ex</h3>
<p>Sometimes a letter from a solicitor — explaining the legal consequences of refusing to
participate in FDR — prompts a change of mind. This is not always effective but it is low-cost
and worth trying before committing to litigation. The letter should note that refusal to
participate may be raised at a costs hearing.</p>
"""
 + inline_cta("If your ex is refusing mediation and you need a Section 60I certificate quickly, contact us. We can contact your ex and issue the certificate, typically within 2 weeks.")
 + f"""
<h2 id="court-without">Going to Court Without Completing Mediation</h2>
<p>You can file a parenting application in the {cite('fcfcoa')} without a Section 60I certificate
only in the following circumstances:</p>
<ol>
  <li>The matter is urgent (risk to the child or a parent)</li>
  <li>There has been family violence or child abuse</li>
  <li>One party is unable to participate in FDR (e.g. incapacity)</li>
  <li>The matter involves enforcement of an existing parenting order</li>
</ol>
<p>If none of these apply and you file without the certificate, the court will likely dismiss
your application or adjourn it and direct you to complete FDR first. This adds delay and cost
without advancing your position.</p>

{callout("Property matters are different",
"The Section 60I certificate requirement applies only to parenting matters. For property settlement disputes, mediation is strongly encouraged but not legally required before filing a court application. However, courts expect parties to have made genuine attempts to resolve property matters before litigation.")}

<h2 id="making-them">Can You Make Your Ex Attend Mediation?</h2>
<p>No — not directly. Mediation is voluntary, and a court will not order someone to participate
in good faith (you can lead a horse to water). However:</p>
<ul>
  <li>The court can and does make orders that mediation be <em>attempted</em> before a matter proceeds</li>
  <li>The court considers each party's conduct, including refusal to engage in FDR, when deciding costs</li>
  <li>Many people who initially refuse mediation change their mind after receiving advice from their own solicitor about the cost and time involved in litigation</li>
</ul>

<h2 id="costs">How Refusal Affects Legal Costs</h2>
<p>In family law proceedings, the general rule is that each party bears their own costs. However,
the {cite('family_law_act')} allows the court to make costs orders against a party whose conduct
has been unreasonable. Refusing to participate in FDR — particularly where the court ordered
it — is the kind of conduct that can attract a costs order.</p>
<p>In practice: a party who refuses mediation, forces the other party to litigate, and then
reaches an agreement at the courthouse steps (which happens frequently) may find themselves
ordered to pay the other party's legal costs for the period of the unnecessary litigation.</p>

<h2 id="faq">Frequently Asked Questions</h2>
""",
 [("My ex says they will only communicate through lawyers. Do I still need to try mediation?",
   "Yes, if it is a parenting matter. The requirement to attempt FDR applies regardless of whether the parties are communicating directly. Your ex's decision to communicate only through lawyers does not exempt either party from the Section 60I requirement. Contact an FDR provider and ask them to make contact — the provider can communicate with your ex's solicitor."),
  ("How long does it take to get a Section 60I certificate when my ex refuses?",
   "Typically 1–3 weeks from the time you first contact the FDR provider. The provider must make a genuine attempt to contact your ex and allow reasonable time for a response. If your ex explicitly refuses in writing, the certificate can be issued faster. If your ex is simply not responding, allow 2–3 weeks of documented contact attempts before the certificate is issued."),
  ("My ex lives interstate. Does that affect mediation?",
   "No. Online and telephone mediation are fully accepted under the NMAS framework and the Family Law Act. Most accredited mediators offer video conferencing. Interstate location is not a reason to avoid FDR or to claim it is impractical."),
  ("Can I apply for child support if my ex won't do mediation?",
   "Yes — child support is administered by Services Australia and is separate from the FDR requirement. You can apply for a child support assessment through Services Australia regardless of whether parenting orders are in place or mediation has been attempted."),
  ("What if my ex agrees to mediation but then cancels or does not show up?",
   "This counts as non-participation. The FDR provider can issue a certificate noting that the other party agreed to participate but failed to attend. Repeated cancellations are recorded. The certificate allows you to apply to court, and the pattern of behaviour is relevant to any costs application."),
  ("Does mediation affect what the court will decide about parenting arrangements?",
   "Mediation is confidential — what was said during the sessions cannot be used as evidence. However, the fact that mediation was attempted (or refused) and any agreements reached are relevant. If you reached a partial agreement in mediation, the court will generally build on that rather than start from scratch. Courts also look favourably on parties who genuinely tried to resolve matters before litigating.")],
 [("family-mediation-process-guide","Family Mediation Process"),
  ("how-mediation-works","How Mediation Works"),
  ("family-law-mediation","Family Law Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("parenting-mediation","Parenting Mediation")],
 read_min=10
)
