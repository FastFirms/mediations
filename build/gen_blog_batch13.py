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
  ("online-vs-inperson","Online vs in-person vs shuttle mediation"),
  ("preparing-for-each-stage","Preparing for each stage of mediation"),
  ("mediators-role","The mediator's role in detail"),
  ("good-faith","What good faith participation looks like"),
  ("parenting-process","Parenting-specific mediation process"),
  ("property-process","Property-specific mediation process"),
  ("timeline","How long does family mediation take?"),
  ("costs","Cost breakdown by stage"),
  ("court-mediation","Family court mediation: what is different"),
  ("after-mediation","After mediation: implementing the agreement"),
  ("if-no-agreement","What happens if mediation fails"),
  ("not-appropriate","When mediation is not appropriate"),
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

<h2 id="online-vs-inperson">Online vs In-Person vs Shuttle Mediation: Full Comparison</h2>

<p>Mediation in Australia is no longer confined to a conference room. Since 2020, online and
telephone mediation have been formally accepted under the {cite('amdras')} accreditation framework
and the {cite('family_law_act')}. The right format depends on your specific circumstances, not
simply convenience.</p>

<table>
  <thead>
    <tr>
      <th>Format</th>
      <th>How it works</th>
      <th>Key advantages</th>
      <th>Key disadvantages</th>
      <th>Best suited to</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>In-person (joint)</strong></td>
      <td>Both parties and the mediator in the same room; usually separate waiting areas</td>
      <td>Richer non-verbal communication; mediator can manage energy in the room; harder to disengage mid-session</td>
      <td>Requires travel; can feel confrontational; harder to arrange around work and children</td>
      <td>Parties with a reasonable working relationship; complex multi-issue matters; situations where non-verbal cues matter</td>
    </tr>
    <tr>
      <td><strong>Online (Zoom / Teams)</strong></td>
      <td>All parties on a video platform; mediator uses breakout rooms for private caucuses</td>
      <td>No travel; flexible scheduling; reduces geographic barriers; parties in their own environment can feel safer; lower cost</td>
      <td>Technology failures; harder to read body language; easier to disengage or multi-task; not suitable where one party is unsafe at home</td>
      <td>Interstate or regional parties; matters where travel is a genuine barrier; parties with young children; lower-conflict situations</td>
    </tr>
    <tr>
      <td><strong>Shuttle mediation</strong></td>
      <td>Parties never meet directly; mediator moves between them (separate rooms or separate video calls) carrying proposals</td>
      <td>Safe where there is family violence history or significant power imbalance; removes face-to-face tension entirely; allows each party to speak openly to the mediator</td>
      <td>Slower; information can be filtered or softened in transit; higher mediator time required; may cost more</td>
      <td>Family violence history; highly entrenched conflict; situations where one party is intimidated by direct contact; where a party has significant anxiety around seeing the other person</td>
    </tr>
    <tr>
      <td><strong>Hybrid</strong></td>
      <td>One party in-person, one online; or joint session in-person with shuttle phases via separate rooms</td>
      <td>Accommodates different circumstances; maximum flexibility</td>
      <td>Can create imbalance between parties; technology must be tested in advance</td>
      <td>Interstate parties where one can attend; situations where one party requires more support</td>
    </tr>
  </tbody>
</table>

<h3>How Zoom mediation actually works</h3>
<p>Online mediation follows the same 10-step process as in-person sessions. The practical
differences are in how the mediator manages the space. Before the session begins, the mediator
sends each party a link, verifies their identity, and confirms they are in a private location
where they cannot be overheard. During the session, the mediator uses breakout rooms for
private caucuses — the equivalent of asking one party to step out into the corridor.</p>
<p>A well-run Zoom mediation uses three "rooms": a main room for joint discussion, and individual
breakout rooms for each party. The mediator moves between them. Most platforms allow the
mediator to see who is in each room and to lock breakout rooms so parties cannot accidentally
enter the wrong space.</p>
<p>One important practical note: if you are at home, make sure your children are not nearby,
your door is locked, and you have headphones. Confidentiality applies equally online — if your
partner or flatmate can hear the session, that is a problem.</p>

<h2 id="preparing-for-each-stage">Preparing for Each Stage of Mediation</h2>

<p>Preparation is one of the most under-used advantages in mediation. Parties who prepare
thoroughly almost always reach better outcomes in less time. Here is what preparation looks
like at each stage.</p>

<h3>Documents to prepare</h3>
<p>For <strong>property and financial matters</strong>, gather the following before your intake call:</p>
<ul>
  <li>Bank and savings account statements (last 12 months for all accounts)</li>
  <li>Superannuation statements (all funds for both parties)</li>
  <li>Mortgage statements and current property valuation (online estimate or formal valuation)</li>
  <li>Investment account statements (shares, managed funds, crypto)</li>
  <li>Business financials if either party owns a business (last 2 years of tax returns and financial statements)</li>
  <li>Statements for all debts: credit cards, personal loans, car loans, HECS/HELP</li>
  <li>Any existing financial agreements or binding financial agreements</li>
</ul>
<p>For <strong>parenting matters</strong>, prepare:</p>
<ul>
  <li>A written summary of the current parenting arrangement (days, nights, school pickup)</li>
  <li>School and activity schedules for the children</li>
  <li>Any existing parenting orders or parenting plans</li>
  <li>Notes on any specific concerns you have about the children's welfare or needs</li>
  <li>A proposed parenting arrangement — not as a fixed demand, but as your starting point</li>
</ul>

<h3>How to prepare emotionally</h3>
<p>Mediation is not therapy, and it is not court. The mediator is not there to hear your
grievances or validate your position — they are there to help you both reach an agreement.
Clients who do well in mediation share a few common traits: they arrive knowing what outcome
they are genuinely trying to achieve (not just what they want to "win"), they are willing to
hear the other party speak without interrupting, and they have a realistic sense of what a
court would likely decide if mediation fails.</p>
<p>Practical emotional preparation:</p>
<ul>
  <li>Talk to a counsellor or trusted friend before the session — not to vent during it</li>
  <li>Write down your three most important outcomes and your three most flexible issues</li>
  <li>Read the {cite('aifs')} research on outcomes for children after separation — it often reframes what matters</li>
  <li>Accept that the other party will say things that frustrate you; plan how you will manage that</li>
  <li>If you are still in acute grief or anger, consider whether a brief delay is better than attending before you are ready</li>
</ul>

<h3>What not to say in mediation</h3>
<p>Mediation is confidential, but what you say still shapes the session. Avoid:</p>
<ul>
  <li><strong>"I know what you're going to do"</strong> — accusations about the other party's intentions close down rather than open up discussion</li>
  <li><strong>"My lawyer says I'll win"</strong> — this is almost always unhelpful and often inaccurate; it signals you are not genuinely engaging</li>
  <li><strong>"The children want to live with me full-time"</strong> — unless this has been formally assessed, using children as leverage is counterproductive and may concern the mediator</li>
  <li><strong>"I'm only here because I have to be"</strong> — this is the clearest signal of bad faith and may lead to a Type 3 certificate (see the good faith section below)</li>
  <li><strong>Ultimatums in the opening stage</strong> — positions stated as non-negotiable before the interest exploration phase have a way of becoming the obstacle the whole session breaks on</li>
</ul>

<h2 id="mediators-role">The Mediator's Role in Detail</h2>

<p>Understanding what a mediator can and cannot do prevents mismatched expectations that
derail sessions before they get started.</p>

<h3>What a mediator can do</h3>
<ul>
  <li>Facilitate communication between both parties in a structured, safe environment</li>
  <li>Help each party articulate their interests (what they actually need) behind their positions (what they initially demand)</li>
  <li>Use reality-testing questions to help both parties consider whether their position is realistic</li>
  <li>Suggest options and frameworks that neither party has considered</li>
  <li>Conduct private sessions (caucuses) with each party to explore issues that are difficult to raise jointly</li>
  <li>Draft a written summary of any agreement reached</li>
  <li>Issue a Section 60I certificate under the {cite('fcfcoa_fdr')} framework if required</li>
  <li>Terminate the session if it is unsafe to continue or if one party is not participating genuinely</li>
</ul>

<h3>What a mediator cannot do</h3>
<ul>
  <li><strong>Give legal advice</strong> — the mediator is neutral; providing legal advice to either party would destroy that neutrality. This is why each party needs their own solicitor for legal review</li>
  <li><strong>Make decisions for the parties</strong> — unlike a judge or arbitrator, the mediator has no power to impose an outcome</li>
  <li><strong>Guarantee confidentiality in all circumstances</strong> — disclosures of serious harm to a child or imminent risk to life must be reported; the mediator explains these limits at the opening</li>
  <li><strong>Compel either party to agree</strong> — mediation requires voluntary participation; the mediator cannot force an outcome</li>
  <li><strong>Provide relationship counselling</strong> — if one or both parties need therapeutic support, that is a separate professional service</li>
</ul>

<h3>How mediators handle one party dominating</h3>
<p>An experienced mediator has a toolkit for managing power imbalances. When one party speaks
over, dismisses, or intimidates the other, the mediator uses structured speaking turns, direct
redirection ("I'd like to hear from [party] now without interruption"), and private caucuses
to give the quieter party space to speak freely. In shuttle mediation, the parties never meet
directly, removing the dynamic entirely.</p>
<p>If the imbalance is so severe that the mediator cannot manage it within the session — for
example, where one party becomes aggressive, threatening, or deliberately stonewalls — the
mediator may suspend or terminate the session. Termination is not a failure; it is the
mediator exercising their professional duty.</p>

<h3>What happens when someone becomes distressed</h3>
<p>Mediation covers emotionally significant territory. It is not unusual for a party to become
upset, to need a break, or to struggle to continue. A skilled mediator normalises this and
offers to pause. The session can be suspended for the day and resumed later. There is no
requirement to complete a session in a single sitting.</p>
<p>If a party discloses serious distress — for example, indicating thoughts of self-harm —
the mediator will stop the mediation process and ensure the person has access to support
before anything else continues. The mediator's duty of care to each party as a person
precedes the process.</p>

<h2 id="good-faith">What Good Faith Participation Looks Like</h2>

<p>The {cite('family_law_act')} requires that parties attend Family Dispute Resolution with a
genuine willingness to try to resolve the matter. "Good faith" is not simply showing up — it
is a standard of conduct the mediator assesses throughout the session.</p>

<h3>Good faith conduct includes</h3>
<ul>
  <li>Attending the intake assessment and the scheduled session</li>
  <li>Providing financial disclosure before the session (for property matters)</li>
  <li>Listening to the other party's perspective without constant interruption</li>
  <li>Engaging with options and proposals rather than refusing all discussion</li>
  <li>Being willing to consider compromise, even where the final position is firm</li>
  <li>Communicating through the mediator when direct communication breaks down</li>
</ul>

<h3>What the court considers "not genuine" — Type 3 certificate territory</h3>
<p>A mediator may issue a Type 3 certificate — which notes that a party attended but did not
make a genuine attempt at resolution — in situations including:</p>
<ul>
  <li>Attending but refusing to engage at all (sitting silently, giving monosyllabic answers)</li>
  <li>Making clearly unreasonable demands with no explanation and refusing to discuss them</li>
  <li>Explicitly stating they have no intention of agreeing to anything regardless of outcome</li>
  <li>Using the session as an opportunity to make allegations or litigate past events rather than engage with resolution</li>
  <li>Leaving the session without reasonable cause before the process has been completed</li>
  <li>Attending under the influence of substances or in a state that prevents genuine participation</li>
</ul>
<p>A Type 3 certificate does not prevent the issuing party from filing with the {cite('fcfcoa')},
but the court is informed that one party did not participate genuinely. This is a significant
factor in any subsequent costs application. Judges take a dim view of parties who treat the
mediation requirement as a box to tick rather than a genuine obligation.</p>

{callout("Costs and bad faith",
"Under the Family Law Act, the court can order a party to pay the other's legal costs where their conduct has been unreasonable. A Type 3 certificate — combined with a pattern of non-engagement — is the kind of conduct that attracts cost orders. The financial penalty for strategic non-participation can easily exceed the cost of genuine engagement.")}

<h2 id="parenting-process">Parenting-Specific Mediation Process</h2>

<p>Parenting mediation and property mediation share the same 10-step framework but differ
significantly in their focus, the information required, and the way agreements are structured.</p>

<h3>How parenting mediation differs from property mediation</h3>
<p>Property mediation is fundamentally about dividing assets — a quantifiable exercise, even
when the numbers are contested. Parenting mediation is about designing a future working
relationship between two people who will co-parent for the next decade or longer. The
emotional stakes are different. The mediator's focus shifts from "what is fair" to "what
works for the children."</p>
<p>Under the {cite('family_law_act')}, the paramount consideration in all parenting matters is
the best interests of the child — not the preferences of either parent. An experienced
parenting mediator frames every discussion through this lens. When a parent says "I want the
children every weekend," the mediator's reality-testing question is "how does that arrangement
serve the children's relationship with both parents?"</p>

<h3>Child-inclusive mediation</h3>
<p>In child-inclusive mediation, a child consultant — a trained child psychologist or specialist
— meets separately with the children to understand their needs, concerns, and preferences.
The consultant does not advocate for a particular outcome and does not report verbatim what
the children said. Instead, they provide the parents with a general picture of how the
children are experiencing the separation and what they need from both parents.</p>
<p>Child-inclusive mediation is not appropriate in all cases. It is most useful where:</p>
<ul>
  <li>Children are old enough to express meaningful preferences (generally 5 years and older)</li>
  <li>Both parents are willing to hear information that may be difficult</li>
  <li>The dispute centres on arrangements the children have strong feelings about</li>
  <li>Children have expressed distress about the current arrangements</li>
</ul>
<p>The {cite('aifs')} research consistently shows that children's wellbeing is better served
when they know their voice has been heard, even where the outcome does not perfectly match
their stated preference.</p>

<h3>When a family report is ordered instead</h3>
<p>A family report is different from child-inclusive mediation. It is a formal court-ordered
assessment conducted by a family consultant (a social worker or psychologist) who assesses
each parent, the children, and the family dynamics, and then reports to the court with
recommendations about parenting arrangements.</p>
<p>Family reports are ordered by the {cite('fcfcoa')} when the court needs an independent
expert opinion — typically in high-conflict matters, where there are welfare concerns, or
where the parties have been unable to agree through mediation. A family report is not part
of the mediation process; it is a court-based assessment that occurs when mediation has
not resolved the matter. Family reports can take 3–6 months and typically cost A$3,000–6,000.</p>

<h2 id="property-process">Property-Specific Mediation Process</h2>

<h3>The financial disclosure process in detail</h3>
<p>The duty of full and frank financial disclosure under the {cite('fcfcoa_disclosure')} rules
requires both parties to disclose all assets, liabilities, and financial resources — not just
the ones they want to negotiate over. This applies equally in mediated property settlements
as it does in court proceedings.</p>
<p>In practice, both parties are typically asked to complete a financial statement before the
mediation session begins. This document should include:</p>
<ul>
  <li>All real property (including investment properties and interstate or overseas properties)</li>
  <li>All bank accounts, term deposits, and savings vehicles in any name or jointly held</li>
  <li>Superannuation balances for all funds</li>
  <li>Shares, managed funds, cryptocurrency, and other investments</li>
  <li>Business interests, including shares in private companies and trusts</li>
  <li>Vehicles, boats, and other valuable personal property</li>
  <li>All debts: mortgages, personal loans, credit cards, tax debts, HECS</li>
  <li>Any inheritances received or expected</li>
</ul>
<p>The mediator is not a forensic accountant and cannot verify the figures. Both parties sign
statutory declarations confirming the accuracy of their disclosure. If it later emerges that
disclosure was incomplete, any agreement reached may be set aside by the court.</p>

<h3>What happens when one party hides assets</h3>
<p>Non-disclosure is a serious legal matter. If you suspect the other party is concealing assets,
there are several options before and during mediation:</p>
<ul>
  <li><strong>Request subpoenas through the court</strong> — prior to commencing mediation, if you have evidence of concealment, you can seek orders from the {cite('fcfcoa')} requiring financial institutions or the ATO to produce records</li>
  <li><strong>Request formal undertakings</strong> — the mediator can record undertakings from both parties to provide complete disclosure before the session proceeds</li>
  <li><strong>Engage a forensic accountant</strong> — in matters involving complex business structures, a forensic accountant can prepare a business valuation and identify inconsistencies</li>
  <li><strong>Adjourn the mediation</strong> — if non-disclosure becomes apparent during the session, a responsible mediator will pause proceedings until it is addressed</li>
</ul>
<p>A mediator who proceeds with a mediation where one party's disclosure is clearly incomplete
is not acting in the interests of either party. Any agreement reached on incomplete information
is vulnerable to challenge.</p>

<h3>Valuations</h3>
<p>Property valuations are often contested in mediation. Each party may have obtained their
own valuation, and those valuations may differ significantly. There are three approaches
commonly used:</p>
<ol>
  <li><strong>Agreed single valuation</strong> — both parties agree to engage a single independent valuer whose figure both accept. This is the most cost-effective approach.</li>
  <li><strong>Two valuations averaged</strong> — each party obtains their own valuation and the parties agree to use the average of the two figures.</li>
  <li><strong>Range negotiation</strong> — where the parties cannot agree on a single figure, the mediator helps them negotiate within a range, accepting that neither party's valuation is definitive.</li>
</ol>
<p>For superannuation splitting, the mediator will recommend both parties obtain superannuation
interest statements and, where self-managed super funds are involved, seek specialist advice
on the valuation and splitting mechanism before the session.</p>

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

<h2 id="after-mediation">After Mediation: Implementing the Agreement</h2>

<p>Reaching agreement in the mediation room is not the end of the process — it is the end of
the negotiation phase. Implementing that agreement correctly is what makes it durable and
legally enforceable.</p>

<h3>What happens week by week after you reach agreement</h3>

<table>
  <thead>
    <tr>
      <th>Timeframe</th>
      <th>What happens</th>
      <th>Who is responsible</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Day 1–3</td>
      <td>Mediator provides written summary of agreed terms; both parties initial the document</td>
      <td>Mediator drafts; both parties sign</td>
    </tr>
    <tr>
      <td>Week 1–2</td>
      <td>Each party takes the summary to their own solicitor for independent legal advice</td>
      <td>Each party independently</td>
    </tr>
    <tr>
      <td>Week 2–3</td>
      <td>Solicitors draft the formal consent orders or parenting plan based on the mediated summary</td>
      <td>Usually one solicitor drafts; the other reviews</td>
    </tr>
    <tr>
      <td>Week 3–4</td>
      <td>Both parties sign the consent orders application; solicitor files with the {cite('fcfcoa_consent_orders')}</td>
      <td>Solicitors file via the {cite('comcourts_portal')}</td>
    </tr>
    <tr>
      <td>Weeks 4–12</td>
      <td>Court reviews and approves consent orders (property) or registers parenting plan</td>
      <td>FCFCOA registry</td>
    </tr>
    <tr>
      <td>Post-approval</td>
      <td>Property transfers, superannuation splits, and account closures are executed</td>
      <td>Solicitors and financial institutions</td>
    </tr>
  </tbody>
</table>

<h3>Who drafts consent orders?</h3>
<p>The mediator drafts the summary of agreement — a plain-language record of what was decided.
This is not a legal document. Converting it into court-ready consent orders is the job of
a solicitor, not the mediator. In practice, one party's solicitor usually prepares the first
draft of the consent orders, which the other party's solicitor reviews and amends. Both
parties must sign the consent orders application before it is filed.</p>
<p>The consent orders application for property matters requires a cover sheet, the proposed
orders, and a financial statement. For the {cite('fcfcoa')} to approve consent orders without
a hearing, the court must be satisfied that the arrangement is just and equitable — the court
does review the substance, not merely the form.</p>

<h3>How long does court approval take?</h3>
<p>For consent orders filed with the {cite('fcfcoa')}, approval typically takes 4–10 weeks from
the date of filing, depending on the complexity of the matter and the court's current workload.
The court does not schedule a hearing for consent orders in most cases — the registrar reviews
the application on the papers. If the court has questions or requires additional information,
the parties' solicitors are contacted by the registry.</p>
<p>Parenting plans do not require court approval — they become binding once both parties sign.
However, if the parties want the parenting arrangement to have the force of a court order
(enforceable as contempt), they should file for consent orders rather than relying on a
parenting plan alone.</p>

<h3>Superannuation splitting after mediation</h3>
<p>Superannuation splitting is a separate step that follows the approval of consent orders.
The trustee of the superannuation fund must be served with a copy of the order and a
"splitting notice." The trustee then has 28 days to respond. Most super splits are processed
within 60–90 days of the consent orders being approved. Each fund has its own forms and
processes — your solicitor should liaise directly with the fund trustee.</p>

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

<h2 id="not-appropriate">When Mediation Is Not Appropriate</h2>

<p>Mediation is not suitable for every family law matter. Accredited mediators are required
under the {cite('ag_fdr')} framework to assess suitability at intake and to decline to conduct
mediation where the process would not be safe or appropriate. Understanding these limits
protects both parties.</p>

<h3>Family violence indicators</h3>
<p>The presence of family violence does not automatically preclude mediation, but it requires
very careful assessment. The {cite('amdras')} accreditation standards require mediators to
screen for family violence at intake and to consider whether the affected party can
participate safely and voluntarily.</p>
<p>Mediation is generally not appropriate where:</p>
<ul>
  <li>There is a current apprehended violence order (AVO) or domestic violence order (DVO)</li>
  <li>The violence is recent, ongoing, or escalating</li>
  <li>The affected party is in fear of the other party and that fear would prevent genuine participation</li>
  <li>The power imbalance created by the violence is so severe that the affected party cannot advocate for their own interests</li>
</ul>
<p>Where there has been historical family violence that is not ongoing, and where the affected
party genuinely wants to try mediation, shuttle mediation (no direct contact) can be
considered. The mediator should involve a family violence support worker and assess the
matter at each stage. If you have experienced family violence, contact {cite('frc')} or
a specialist family violence service before attending any mediation session.</p>

<h3>Power imbalance</h3>
<p>Family violence is the most acute form of power imbalance, but it is not the only one.
Mediation may also not be appropriate where one party has significantly greater financial
sophistication, legal knowledge, or negotiating experience than the other, and where that
imbalance cannot be adequately managed within the mediation process. A well-resourced party
who has taken extensive legal advice prior to mediation, negotiating against a party who has
had none, is a situation a responsible mediator will flag at intake.</p>

<h3>Mental health considerations</h3>
<p>A diagnosed mental health condition does not preclude participation in mediation. Many
people manage significant mental health challenges and can participate fully and genuinely
in a structured mediation process. The relevant question is not diagnosis but capacity:
can this person understand the process, make decisions freely, and engage with the other
party in a way that is safe?</p>
<p>Where capacity is genuinely in doubt, the mediator may recommend that the party obtain
a letter from their treating professional confirming capacity to participate, or may
recommend that a support person with appropriate qualifications be present. Matters
involving a party who lacks legal capacity to enter into agreements should not proceed
through mediation without specialist advice.</p>

<h3>The mediator's duty to end a session</h3>
<p>An accredited mediator has both the right and the professional obligation to terminate a
mediation session at any point where continuing would be unsafe or counterproductive. This
includes situations where:</p>
<ul>
  <li>A party becomes threatening or aggressive toward the other party or the mediator</li>
  <li>A disclosure is made that creates a mandatory reporting obligation</li>
  <li>The mediator forms a view that one party is not capable of genuine participation</li>
  <li>The power imbalance becomes so severe that the process cannot be managed fairly</li>
  <li>A party discloses a safety crisis that requires immediate support</li>
</ul>
<p>Terminating a session is not a neutral act — the mediator records the reason and, in the
case of FDR for parenting matters, issues the appropriate Section 60I certificate reflecting
the circumstances. Where a session is terminated due to safety concerns, the mediator may
make referrals to appropriate services.</p>

{callout("If you are concerned about safety",
"If you are worried that mediation may not be safe for you, contact the mediator before the intake call and explain your concerns. A responsible mediator will adjust the process, offer shuttle mediation, or advise you that court is a more appropriate pathway. You are not obliged to proceed with mediation if you have genuine safety concerns — the Section 60I exemption for family violence exists for exactly this reason.")}

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
   "Both document agreed parenting arrangements. A parenting plan is a written agreement signed by both parents — it is enforceable but not a court order, so breach cannot be punished as contempt of court. Consent orders are filed with and approved by the FCFCOA, making them court orders. Breach of consent orders is a more serious legal matter. For high-conflict situations, consent orders provide stronger protection."),
  ("Can I do mediation online if my ex lives in another state?",
   "Yes. Online mediation via video conference is fully accepted under the NMAS framework and the Family Law Act. Most accredited mediators, including Mediations Australia, offer Zoom mediation for interstate parties. The process is identical to in-person mediation — the mediator uses breakout rooms for private caucuses and conducts each stage in the same order. Interstate location is not a reason to delay starting the mediation process."),
  ("How much financial information do I need to bring to property mediation?",
   "Both parties have a legal duty of full and frank financial disclosure. Before your first mediation session you should prepare: bank account statements (last 12 months), superannuation statements for all funds, mortgage statements and a property valuation, investment and share account statements, any business financial statements if relevant, and a list of all debts. The mediator is not there to audit you, but any agreement reached on incomplete disclosure is vulnerable to being set aside by the court later."),
  ("What happens after mediation if we reach an agreement — is it immediately legally binding?",
   "No. The mediator's written summary of your agreement is not immediately legally binding. It is a record of what you agreed that both parties initial. To make it enforceable, property agreements must be converted to consent orders and filed with the FCFCOA (a process that takes 4–10 weeks). Parenting agreements can be formalised as a signed parenting plan (binding but not a court order) or also filed as consent orders for stronger enforceability. Your solicitor handles the formalisation step."),
  ("What if only some issues get resolved in mediation — can I get a certificate and go to court for the rest?",
   "Yes. Partial agreements are common and valuable. If you resolve parenting arrangements but not property, or agree on most assets but not one contested item, the mediator can document what was agreed and issue a Section 60I certificate confirming a genuine attempt was made on the unresolved parenting issues. You can then apply to the court for a determination on only the outstanding matters. The court will generally build on what was agreed rather than re-litigating resolved issues.")],
 [("how-mediation-works","How Mediation Works"),
  ("family-law-mediation","Family Law Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce in Australia"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("property-settlement-mediation-guide","Property Settlement Mediation")],
 read_min=22
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
  ("why-they-refuse","Why people refuse mediation — and what it usually means"),
  ("section-60i","How to get a Section 60I certificate"),
  ("fdr-contact-process","The FDR provider's contact process in detail"),
  ("all-certificate-types","All 8 types of Section 60I certificate explained"),
  ("options","Your four options when mediation is refused"),
  ("applying-to-court","Applying to court after getting your certificate"),
  ("urgent-applications","Urgent applications without a certificate"),
  ("first-court-hearing","What happens at the first court hearing"),
  ("court-without","Going to court without completing mediation"),
  ("making-them","Can you make your ex attend mediation?"),
  ("cost-comparison","Cost comparison: mediation vs litigation when ex refuses"),
  ("changing-their-mind","Strategies that sometimes change a reluctant ex's mind"),
  ("property-mediation","When your ex refuses property mediation"),
  ("childrens-perspectives","Children's perspectives and views in parenting proceedings"),
  ("case-studies","Real scenarios: three case studies"),
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

<h2 id="why-they-refuse">Why People Refuse Mediation — and What It Usually Means</h2>
<p>Understanding why your former partner is refusing to participate can help you choose the
most effective response. Refusal rarely means they have a strong legal position — it almost
always reflects something else entirely.</p>

<h3>Fear of direct confrontation</h3>
<p>Many people who refuse mediation are not being strategic — they are anxious. The prospect of
sitting in a room (or on a video call) with an ex-partner, discussing painful topics, can feel
genuinely overwhelming. This type of refusal often dissolves when the format is adjusted:
shuttle mediation (no direct contact, mediator moves between rooms or calls), online-only
sessions, or the option to have a support person present. If you suspect anxiety is the real
issue, offering a shuttle format through the FDR provider may be all it takes.</p>

<h3>Poor or adversarial legal advice</h3>
<p>Some solicitors still advise clients to avoid mediation, particularly early in a matter.
The reasoning — that mediation might lock in a bad outcome before all financial information is
gathered — is sometimes valid but is often used reflexively. A party whose solicitor has told
them "don't go to mediation yet" may not realise they are still required to attempt FDR for
parenting matters regardless of where their property matter stands. When a solicitor writes to
the FDR provider on your ex's behalf explaining they are not yet ready, that is still a form
of non-participation — and the certificate can still be issued.</p>

<h3>Using delay as a tactic</h3>
<p>In high-conflict separations, delay is sometimes a deliberate tactic. Refusing mediation
extends the period during which current arrangements continue — if your ex has the children
more than you do, dragging out the process preserves that advantage. This is one of the clearest
reasons the law allows a certificate to be issued on the basis of refusal: the legislature
recognised that one party could weaponise the mediation requirement to delay the other party
accessing court. The solution is to contact an FDR provider immediately and begin the clock
running on the contact attempts.</p>

<h3>Genuine safety concerns</h3>
<p>Sometimes a refusal to participate in standard joint mediation is entirely reasonable. Where
there has been family violence, coercive control, or a significant power imbalance, your former
partner may be refusing standard joint mediation while remaining willing to participate in a
modified format — shuttle mediation, having an independent support person, or using a provider
with specialist family violence training. If this is the situation, it is worth exploring
whether a {cite('frc')}-referred provider with family violence protocols can make mediation work
before taking the certificate route. The {cite('aifs')} research consistently shows that
mediated agreements produce better long-term compliance than court orders, particularly for
parenting matters — so even where participation is reluctant, the effort to find a workable
format is worth making.</p>

<h3>They simply have not engaged</h3>
<p>In some cases there is no deep reason — your ex has not responded to calls, changed phone
numbers, or moved without telling you. The law allows for this. The FDR provider documents
their contact attempts, and if your ex is genuinely uncontactable after a reasonable effort,
a certificate is issued on that basis. You are not required to locate your former partner
yourself before the certificate can be issued.</p>

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

<h2 id="fdr-contact-process">The FDR Provider's Contact Process in Detail</h2>
<p>Many people are uncertain about what happens after they call an FDR provider. The process
is more structured than most people expect, and understanding it helps you set realistic
timelines and know what to follow up on.</p>

<h3>Step 1: Your intake call (Day 1–3)</h3>
<p>When you contact an accredited FDR provider, the first step is an intake assessment — usually
a phone call lasting 30–60 minutes. The provider will ask about your situation: the nature of
the dispute (parenting, property, or both), whether there are any safety concerns, whether you
are aware of your ex's current contact details, and what outcome you are hoping for. This call
is also when the provider assesses whether mediation is suitable or whether an exemption applies.
You will be asked to provide your ex's phone number and/or email address.</p>

<h3>Step 2: The provider contacts your ex (Day 3–7)</h3>
<p>The FDR provider makes contact with your former partner. This is typically done by phone first,
followed by a written communication (letter or email) if there is no response. The communication
from the provider is neutral — it explains what FDR is, that the other party has requested an
attempt at mediation, and invites them to participate in their own separate intake call. The
provider does not take sides, does not repeat what you have told them, and does not pressure
your ex. The contact is designed to feel as low-threat as possible.</p>

<h3>Step 3: Allowing a reasonable response period (Day 7–14)</h3>
<p>Under the {cite('ag_fdr')} framework, the provider must allow a reasonable period for your
ex to respond. In practice this is typically 7–14 days from the date of first contact. If your
ex responds and is willing to participate, the provider schedules their own intake call and
begins the process of arranging a joint session. If your ex responds but declines, the provider
can issue the certificate almost immediately. If your ex does not respond at all after two or
three documented contact attempts over 10–14 days, the provider issues a "not contactable"
certificate.</p>

<h3>What counts as a "reasonable attempt"</h3>
<p>The {cite('fcfcoa_fdr')} guidelines indicate that a reasonable attempt generally includes at
least two separate contact methods (phone and written/email) on at least two separate occasions,
with a reasonable interval between attempts. Providers document every contact attempt — date,
time, method, and result — because this documentation may need to be provided to the court.
If you give an outdated phone number for your ex, the provider will note this and may ask
you to supply updated contact details or an address for a letter to be sent.</p>

<h3>What happens if your ex agrees at the last minute</h3>
<p>It is not uncommon for a former partner to initially refuse or ignore contact from the FDR
provider, and then agree to participate at the last minute — sometimes after receiving advice
from their own solicitor about the cost implications of continued refusal. Providers are accustomed
to this. If your ex agrees to participate before the certificate is issued, the process continues
to a joint session. If they agree after the certificate has been issued, the certificate is still
valid — but you and your ex can choose to attempt mediation anyway, which may make the court
look more favourably on both parties at the first hearing.</p>

<h2 id="all-certificate-types">All 8 Types of Section 60I Certificate Explained</h2>
<p>The {cite('family_law_act')} and the Family Law (Family Dispute Resolution Practitioners)
Regulations 2008 provide for eight distinct certificate types. Each tells the court something
specific about what happened in the FDR process.</p>

<table>
  <thead>
    <tr>
      <th>Certificate type</th>
      <th>Circumstances</th>
      <th>Court implications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Type 1</strong></td>
      <td>The other party refused to participate in FDR</td>
      <td>Court will proceed with the application; may note refusal at costs hearing</td>
    </tr>
    <tr>
      <td><strong>Type 2</strong></td>
      <td>The other party was not contactable despite reasonable attempts</td>
      <td>Court proceeds; may order substituted service or skip notice requirements</td>
    </tr>
    <tr>
      <td><strong>Type 3</strong></td>
      <td>The applicant party (you) decided not to continue with FDR</td>
      <td>Court may inquire into your reasons; rarely used, can raise questions about good faith</td>
    </tr>
    <tr>
      <td><strong>Type 4</strong></td>
      <td>Both parties attended and a genuine attempt was made, but no agreement was reached</td>
      <td>Standard pathway to court; no adverse inference against either party</td>
    </tr>
    <tr>
      <td><strong>Type 5</strong></td>
      <td>Both parties attended but one (named) did not make a genuine effort</td>
      <td>Very significant — the party named as not genuine may face adverse costs orders</td>
    </tr>
    <tr>
      <td><strong>Type 6</strong></td>
      <td>The FDR practitioner decided it was not appropriate to continue (safety or conduct grounds)</td>
      <td>Court proceeds; practitioner's reasons are documented and may be relevant</td>
    </tr>
    <tr>
      <td><strong>Type 7</strong></td>
      <td>FDR was not appropriate to begin with (assessed at intake as unsuitable)</td>
      <td>Court accepts the certificate; no adverse inference against either party</td>
    </tr>
    <tr>
      <td><strong>Type 8</strong></td>
      <td>Agreement was reached on some but not all issues</td>
      <td>Court is provided with the partial agreement; proceedings address only unresolved issues</td>
    </tr>
  </tbody>
</table>

<p>The most common certificates in the context of a refusing former partner are <strong>Type 1</strong>
(explicit refusal) and <strong>Type 2</strong> (not contactable). Type 5 — where one party
attended but was not genuine — is rarer but powerful: a judge reading a Type 5 certificate
knows that the refusing or disengaged party wasted everyone's time, and this carries real weight
in the costs discussion.</p>

{callout("Certificate validity period",
"A Section 60I certificate does not expire, but courts look unfavourably on long delays between obtaining a certificate and filing a court application. If you obtain a certificate and then do nothing with it for 12 months, the court may ask why — and the circumstances may have changed enough that the court directs parties back to FDR. Use your certificate promptly once issued.")}

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
<h2 id="applying-to-court">Applying to Court After Getting Your Certificate</h2>
<p>Once you have your Section 60I certificate in hand, you can file an initiating application
for parenting orders in the {cite('fcfcoa')}. This section explains what that process looks like
in practice.</p>

<h3>Which court to file in</h3>
<p>The {cite('fcfcoa')} handles all federal family law matters across Australia except Western
Australia. If you are in Western Australia, parenting applications are filed in the
{cite('family_court_wa')}. Applications can be filed online through the
{cite('comcourts_portal')} or in person at a family law registry. The portal allows you to file
and pay fees online without attending a registry.</p>

<h3>What forms to complete</h3>
<p>For a parenting application you will need to file:</p>
<ul>
  <li><strong>Initiating Application (Family Law):</strong> sets out the orders you are seeking and attaches your Section 60I certificate</li>
  <li><strong>Financial Statement</strong> (if seeking property orders at the same time)</li>
  <li><strong>Affidavit in support</strong> (required for interim hearings — your sworn written statement of the facts)</li>
  <li><strong>Notice of Child Abuse, Family Violence or Risk:</strong> must be filed if any of these are present</li>
</ul>
<p>Filing fees apply: as at 2026, the standard filing fee for an initiating application in the
{cite('fcfcoa_fees')} is $190 (reduced fee) or $380 (general fee), depending on whether you
meet financial hardship criteria. Fees for hearing dates are additional.</p>

<h3>What to ask for (the orders you seek)</h3>
<p>Your application should specify the orders you are seeking. For interim orders (to cover the
period until a final hearing) you will ask for:</p>
<ul>
  <li>Specific time arrangements — which days/nights the children spend with each parent</li>
  <li>Communication arrangements — phone calls, video calls</li>
  <li>Handover arrangements — where and how handovers occur</li>
  <li>Any other urgent orders — for example, an order that neither parent relocate with the children pending the final hearing</li>
</ul>
<p>Interim orders are not final — they are put in place to provide stability while the full
matter is resolved. The court makes interim orders quickly (often within a few weeks of filing)
so that children's lives are not in limbo during litigation.</p>

<h3>Service on the other party</h3>
<p>Once you file, the court stamps your application and you must serve a copy on your former
partner within a set timeframe (generally 28 days). Service must be carried out by a process
server or another adult who is not a party to the proceedings — you cannot serve your ex yourself.
Proof of service must be filed with the court before the first hearing date.</p>

<h2 id="urgent-applications">Urgent Applications Without a Certificate</h2>
<p>The most important thing to know about urgent applications is that they are genuinely for
urgent situations — not for cases where you are frustrated by delay or want to move faster.
Courts deal harshly with parties who file urgent applications on non-urgent grounds.</p>

<h3>What qualifies as urgent</h3>
<p>Under the {cite('family_law_act')}, you may file a parenting application without a Section 60I
certificate where:</p>
<ul>
  <li>There is a risk of harm to a child — physical, sexual, or psychological abuse</li>
  <li>A child has been, or is likely to be, removed from Australia without consent</li>
  <li>A child has been retained in Australia contrary to an existing order</li>
  <li>A parent's safety is at immediate risk (family violence)</li>
  <li>A parent is about to relocate with the children without notice</li>
</ul>
<p>Where urgency is claimed, the court can list the matter for a hearing within days. The
registrar or judge will consider whether the urgency is genuine before listing — filing an
urgent application that is not actually urgent will result in it being referred back to the
standard list and a note being made of the false urgency claim.</p>

<h3>Preparing your affidavit for an urgent application</h3>
<p>An affidavit for an urgent application needs to do three things clearly:</p>
<ol>
  <li><strong>Establish the facts:</strong> what happened, when, with dates and specifics. Do not generalise — "he has been violent" is not as useful as "on [date] he [specific act]."</li>
  <li><strong>Establish the risk:</strong> why the situation is urgent right now, not just in general. What will happen if orders are not made this week?</li>
  <li><strong>Explain why you did not attempt FDR:</strong> your grounds for the exemption from the Section 60I requirement.</li>
</ol>
<p>If you have a solicitor, they will draft the affidavit. If you are self-represented, the
{cite('fcfcoa')} website has guidance on how affidavits should be structured. Family law duty
lawyers at the registry can also assist with urgent matters on the day of filing.</p>

{callout("Without notice applications",
"In extreme cases — where serving notice of the application on your ex would itself create a risk (for example, they might immediately relocate the children) — you can apply for a without-notice (ex parte) order. The court grants these very rarely and only on strong evidence. If granted, the other party is notified after the order is made and has the right to apply for it to be varied.")}

<h2 id="first-court-hearing">What Happens at the First Court Hearing</h2>
<p>If you have never been to a family law hearing, the first one can feel daunting. Understanding
what actually happens removes much of the fear.</p>

<h3>Before the hearing: what both parties must file</h3>
<p>By the first return date, both parties should have filed:</p>
<ul>
  <li>Their respective court documents (Initiating Application, Response to Application, Financial Statements if applicable)</li>
  <li>Affidavits in support of any interim orders sought</li>
  <li>The Section 60I certificate (filed with the original application)</li>
  <li>Any parenting plan or existing agreement that is already in place</li>
</ul>
<p>If your former partner has not yet filed a Response by the first hearing, the registrar
will note this and may give them a short extension — usually 14–28 days — before the interim
hearing proceeds. Courts are reluctant to make final or significant interim orders without
giving the other party an opportunity to be heard.</p>

<h3>What happens in the courtroom</h3>
<p>The first hearing in the {cite('fcfcoa')} is typically before a Judicial Registrar rather
than a judge. It is usually short — 15–30 minutes — and is not a trial. The registrar will:</p>
<ul>
  <li>Confirm both parties' details and check that all documents have been filed</li>
  <li>Hear brief oral submissions from each party (or their lawyers) on what interim orders are needed</li>
  <li>Make interim parenting orders — or adjourn to a longer interim hearing if the matters are contested</li>
  <li>Make procedural orders about what happens next: family report, further mediation, disclosure requirements</li>
  <li>Set dates for the next event (a further interim hearing, a mention, or a final hearing allocation)</li>
</ul>

<h3>Typical orders made at a first hearing</h3>
<p>At a first return date, the court commonly makes:</p>
<ul>
  <li>Interim parenting orders setting a temporary schedule for the children</li>
  <li>An order that the parties attempt further FDR before the next hearing (if they have not already done so in good faith)</li>
  <li>An order for a family report — an independent assessment of the family by a family consultant</li>
  <li>Disclosure orders — requiring both parties to exchange documents</li>
  <li>Directions about filing further affidavits</li>
</ul>

<h3>How long until the matter is resolved</h3>
<p>The {cite('fcfcoa')} publishes current performance data. For matters that resolve by consent
(agreement) at or after the first hearing, the median time from filing to finalisation is
approximately 3–6 months. For matters that proceed to a final contested hearing, the median
time is 18–24 months. This stark difference is one of the strongest practical arguments for
using the FDR process — even an ex who initially refuses often comes around once they
understand what years of litigation actually involve.</p>

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

<h2 id="cost-comparison">Cost Comparison: Mediation vs Litigation When Your Ex Refuses</h2>
<p>Understanding the financial reality of each path is important. The numbers below are estimates
based on typical matters; your specific situation may differ significantly depending on complexity,
whether you have lawyers, and how the other party behaves.</p>

<table>
  <thead>
    <tr>
      <th>Stage</th>
      <th>Mediation route (ex eventually agrees)</th>
      <th>Contested litigation route</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FDR intake and certificate</td>
      <td>A$300–600 (your share)</td>
      <td>A$300–600 (certificate still required)</td>
    </tr>
    <tr>
      <td>FDR joint session(s)</td>
      <td>A$800–2,000 (your share, 1–3 sessions)</td>
      <td>Not applicable (ex refuses)</td>
    </tr>
    <tr>
      <td>Solicitor advice on mediated agreement</td>
      <td>A$500–1,500</td>
      <td>Not applicable</td>
    </tr>
    <tr>
      <td>Consent orders filing</td>
      <td>A$175–380 court fee + A$500–1,500 solicitor</td>
      <td>Not applicable</td>
    </tr>
    <tr>
      <td>Initiating Application filing</td>
      <td>Not applicable</td>
      <td>A$190–380 court fee</td>
    </tr>
    <tr>
      <td>Solicitor to prepare and file Application</td>
      <td>Not applicable</td>
      <td>A$3,000–8,000</td>
    </tr>
    <tr>
      <td>Interim hearing preparation and attendance</td>
      <td>Not applicable</td>
      <td>A$3,000–7,000 per hearing</td>
    </tr>
    <tr>
      <td>Family report (if ordered)</td>
      <td>Not applicable (or optional in mediation)</td>
      <td>A$3,000–8,000 (court-ordered)</td>
    </tr>
    <tr>
      <td>Final hearing preparation</td>
      <td>Not applicable</td>
      <td>A$15,000–40,000</td>
    </tr>
    <tr>
      <td>Final hearing (each day)</td>
      <td>Not applicable</td>
      <td>A$5,000–15,000 per day</td>
    </tr>
    <tr>
      <td><strong>Typical total (your costs only)</strong></td>
      <td><strong>A$2,500–6,000</strong></td>
      <td><strong>A$30,000–100,000+</strong></td>
    </tr>
  </tbody>
</table>

<p>The {cite('fcfcoa_fees')} notes that contested parenting matters that proceed to a final hearing
take on average 18–24 months from filing and cost both parties combined well over A$100,000.
Even in the scenario where your ex refuses mediation and you are forced to file, if they come
to their senses and agree to mediate <em>before</em> the final hearing (which is the most common
outcome), you are still looking at significantly lower costs than a full trial.</p>
<p>The lesson is this: do not let your former partner's refusal to mediate translate into your
own abandonment of the mediation pathway. Maintain the pressure through the certificate process,
file in court, and continue to communicate willingness to mediate. Most matters settle. The
question is whether they settle early or late — and that question has a A$50,000–90,000 answer.</p>
"""
 + inline_cta("Want to understand the likely cost of your specific matter? Our mediators can assess your situation and explain what the FDR pathway looks like from here.")
 + f"""
<h2 id="changing-their-mind">Strategies That Sometimes Change a Reluctant Ex's Mind</h2>
<p>Before accepting that litigation is inevitable, it is worth trying a few approaches that
have a reasonable track record of bringing reluctant former partners to the table.</p>

<h3>A solicitor's letter on costs</h3>
<p>A formal letter from your solicitor — not aggressive, but factual — setting out the estimated
costs of litigation and the fact that a court may award costs against a party who unreasonably
refused to mediate has changed the minds of many initially resistant former partners. The letter
should reference the specific certificate that has been (or will be) issued and note that it
will be before the court. Numbers are persuasive. A brief letter estimating A$80,000–150,000
in combined litigation costs often focusses the mind.</p>

<h3>Offering shuttle or online mediation</h3>
<p>If your former partner's stated objection is having to be in the same room as you, a simple
adjustment to the format may resolve it. Shuttle mediation (separate rooms, mediator moves
between parties) and online-only mediation with separate video calls are both fully accepted
under the {cite('ag_fdr')} framework. Making this offer through the FDR provider — and having
the provider document that you offered it — is both tactically sound and demonstrates good
faith if the matter later goes to court.</p>

<h3>Changing the mediator</h3>
<p>Sometimes the resistance is to a specific mediator — perceived bias, prior contact with one
party, or simply a personality clash. Offering to use a different accredited provider, or
asking the existing provider to assign a different practitioner, costs little and may unblock
the process. The {cite('frc')} maintains a searchable directory of accredited FDR providers
across Australia that you can use to propose alternatives.</p>

<h3>Involving a family consultant at the FCFCOA</h3>
<p>If you have already filed in court, the {cite('fcfcoa')} offers a Child Dispute Service where
a family consultant can meet with both parties and any children before a hearing. This is a
different process from mediation but sometimes opens communication channels that have been
completely closed. Family consultants are experienced in working with high-conflict situations
and can reframe the conversation from positions ("I want more time") to the children's needs
("the children need stability and contact with both of you").</p>

<h3>Waiting for the right moment</h3>
<p>Timing matters. A former partner who flatly refuses in the immediate aftermath of separation
may be much more open six months later, when the emotional intensity has settled and the
financial reality of litigation has had time to register. There is no rule requiring you to
push for immediate court action once you have a certificate — filing is at your discretion.
Sometimes the most effective strategy is to obtain the certificate (starting your clock), make
it clear you are willing to mediate, and give your former partner time to reconsider with the
certificate as a concrete reminder that court is the next step.</p>

<h2 id="property-mediation">When Your Ex Refuses Property Mediation (Not Parenting)</h2>
<p>Property settlement disputes operate under different rules. There is no Section 60I certificate
requirement for property matters — you do not need to attempt mediation before filing a property
application with the {cite('fcfcoa')}. However, the practical and costs consequences of not
attempting mediation are significant.</p>

<h3>The direct court application route</h3>
<p>For property matters, you can file an Application for Property Orders directly with the
{cite('fcfcoa')} without any certificate or prior mediation attempt. You will need to file a
Financial Statement setting out your assets, liabilities, income, and contributions. Your
former partner must do the same under the {cite('fcfcoa_disclosure')} duty of full and frank
disclosure.</p>

<h3>Time limits for property applications</h3>
<p>This is critical: for married couples, you must file a property application within 12 months
of the date your divorce becomes final. For de facto couples, the limit is 2 years from the
date of separation. These time limits are strictly applied — getting an extension requires
demonstrating hardship, and courts grant extensions reluctantly. If your ex is refusing to
mediate and the time limit is approaching, file the application first and negotiate second.</p>

<h3>Property mediation even without agreement</h3>
<p>Even if your ex refuses to engage with mediation before you file, the court will almost
certainly direct the parties to mediation (or a conciliation conference) before allocating
a final hearing date for a property matter. The court's mediation service and private FDR
providers both handle court-referred property mediations. The difference is that at the
court-directed stage, both parties have already spent money on lawyers to get to that point
— money that could have been saved by mediating earlier.</p>

{callout("Superannuation splitting",
"Property mediation — even when court-referred — is the most efficient way to resolve superannuation splitting. Super splitting orders require consent of both parties or a court determination. A mediated agreement on super splitting is then formalised as consent orders filed with the FCFCOA. If your ex refuses to engage on super splitting, filing in court is the only other option.")}

<h2 id="childrens-perspectives">Children's Perspectives and Views in Parenting Proceedings</h2>
<p>When parenting arrangements are disputed and your ex has refused mediation, the court will
eventually need to understand what the children themselves need and, where appropriate, what
they want. The {cite('family_law_act')} requires the court to give weight to the child's views
having regard to their age and maturity. There are several formal mechanisms for this.</p>

<h3>Independent Children's Lawyers (ICLs)</h3>
<p>In contested parenting matters, the court can appoint an Independent Children's Lawyer — a
solicitor whose client is the interests of the child, not either parent. The ICL meets with the
children, reviews all relevant evidence, and makes submissions to the court about what orders
would best serve the children's interests. ICLs are appointed in cases involving allegations
of abuse, high conflict, or where the children are old enough to have genuine views about
their living arrangements. The ICL's role is not to simply advocate for what the children say
they want — it is to advocate for what is in their best interests, which may be different.</p>

<h3>Family reports</h3>
<p>A family report is prepared by a family consultant — typically a psychologist or social
worker with specialist family law experience — who interviews both parents, the children, and
sometimes other relevant parties (teachers, grandparents). The report addresses each parent's
capacity to care for the children, the children's views and emotional needs, and makes
recommendations about parenting arrangements. Family reports are often ordered at the first
hearing of a contested matter. They take 2–4 months to complete and the cost is shared between
the parties (typically A$3,000–8,000 depending on the number of children and complexity).</p>

<h3>Child-inclusive mediation</h3>
<p>Child-inclusive mediation is an FDR format in which a specialist child consultant meets
separately with the children and then provides the mediator (not the parents) with a summary
of the children's perspective and needs. The mediator uses this information to inform the
mediation session — not by repeating what the children said, but by helping parents understand
the impact of conflict on their children and what the children most need from both parents.
The {cite('aifs')} research shows that child-inclusive mediation has significantly better
outcomes for both agreement rates and long-term parental cooperation than standard mediation.
If your ex is reluctant to mediate but open to considering the children's perspective, proposing
a child-inclusive process may be a way to bring them to the table.</p>

<h2 id="case-studies">Real Scenarios: Three Case Studies</h2>
<p>The following case studies are fictional composites designed to illustrate how these
pathways play out in practice. Names and details are invented.</p>

<h3>Scenario 1: The ex who refuses and then agrees at the last minute</h3>
<p><strong>Background:</strong> Sarah and Mark separated in March after a 9-year marriage with
two children aged 6 and 9. Mark moved out and the children continued living with Sarah during
the week, spending weekends with Mark. After three months, Mark began refusing to return the
children on Sunday afternoons, claiming the children did not want to go back. Sarah contacted
an FDR provider in June.</p>
<p><strong>What happened:</strong> The FDR provider contacted Mark by phone and email. Mark
initially responded through his solicitor, saying he was not ready to mediate and needed time
to "get advice." The FDR provider documented this response and waited 14 days. Mark's solicitor
did not provide any further instructions. The FDR provider issued a Type 1 certificate in early
July.</p>
<p>Sarah's solicitor filed an Initiating Application and served it on Mark in late July. Three
days before the first return date in September, Mark's solicitor contacted Sarah's solicitor
and proposed mediation. Both parties agreed and the hearing was adjourned by consent. They
mediated two weeks later, reached agreement in a single session, and filed consent orders.
Total elapsed time from first FDR contact to consent orders: 5 months. Sarah's total costs:
approximately A$7,000 (FDR, solicitor for the application, mediation, consent orders).</p>

<h3>Scenario 2: The ex who is overseas and uncontactable</h3>
<p><strong>Background:</strong> James and Wei separated after a 5-year de facto relationship
with one child aged 3. Wei returned to her family overseas six months after separation,
taking the child. James had agreed to this temporary stay but Wei had not returned after
12 months and was not responding to his messages. James had no current address for Wei.</p>
<p><strong>What happened:</strong> James contacted an FDR provider and provided the last
known contact details — a phone number and email address. The FDR provider made three contact
attempts over 10 days. There was no response. The FDR provider issued a Type 2 certificate
(other party not contactable) and documented all attempts.</p>
<p>James filed in the {cite('fcfcoa')} for parenting orders and, separately, for a recovery order
under the Hague Convention on International Child Abduction. The Section 60I certificate
was included with the filing. The court made urgent orders without notice to Wei because
service might have caused Wei to take further steps to prevent the child's return. James's
matter was significantly more complex than a domestic refusal, but the certificate process was
the same — the FDR provider's role was to make documented attempts at contact, not to resolve
the international dimension.</p>

<h3>Scenario 3: The family violence exemption in practice</h3>
<p><strong>Background:</strong> Lisa separated from her husband David after he was charged with
assault following a domestic violence incident. There was an active apprehended violence order
(AVO) prohibiting David from contacting Lisa. They had three children aged 4, 7, and 11. David
was seeking contact with the children. Lisa needed parenting orders urgently but was not able
to attend mediation with David due to the AVO.</p>
<p><strong>What happened:</strong> Lisa applied for a Section 60I exemption on the grounds of
family violence. The exemption was noted on her Initiating Application along with the AVO
documentation. The court accepted the exemption without requiring Lisa to attempt FDR. At the
first hearing, the registrar made interim orders providing David with supervised contact with
the children through a contact centre, pending a family report. The family report was ordered
and completed over the following three months. Lisa was never required to be in the same
space as David at any point in the process.</p>
<p>This scenario illustrates an important point: the exemption from the FDR requirement is not
a shortcut to a better outcome — it is a safety valve. The court still followed the same
framework (interim orders, family report, final hearing allocation), but Lisa did not have to
navigate a mediation process with someone against whom she had a protection order.</p>

<h2 id="costs">How Refusal Affects Legal Costs</h2>
<p>In family law proceedings, the general rule is that each party bears their own costs. However,
the {cite('family_law_act')} allows the court to make costs orders against a party whose conduct
has been unreasonable. Refusing to participate in FDR — particularly where the court ordered
it — is the kind of conduct that can attract a costs order.</p>
<p>In practice: a party who refuses mediation, forces the other party to litigate, and then
reaches an agreement at the courthouse steps (which happens frequently) may find themselves
ordered to pay the other party's legal costs for the period of the unnecessary litigation.</p>
<p>The most significant costs implications arise when:</p>
<ul>
  <li>A party refuses FDR, the other party files, and then the refusing party agrees to the same terms they were offered before filing — the court takes a dim view of this sequence</li>
  <li>A Type 5 certificate has been issued, identifying one party as not making a genuine effort — this document follows the matter into court and is directly relevant to costs</li>
  <li>A party engages in repeated delaying tactics in court after refusing FDR — the cumulative picture of obstruction is relevant to any costs application</li>
</ul>

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
   "Mediation is confidential — what was said during the sessions cannot be used as evidence. However, the fact that mediation was attempted (or refused) and any agreements reached are relevant. If you reached a partial agreement in mediation, the court will generally build on that rather than start from scratch. Courts also look favourably on parties who genuinely tried to resolve matters before litigating."),
  ("My ex has told the FDR provider they are willing to mediate but then keeps postponing. How long do I have to wait?",
   "You do not have to wait indefinitely. If your ex has indicated willingness but continues to postpone without genuine reason, the FDR provider has the discretion to issue a certificate on the basis that the other party is not making a genuine attempt. Discuss the pattern of postponements with the FDR provider and ask them to document it. After two or three documented postponements without valid explanation, a certificate can typically be issued."),
  ("What is the difference between a Type 1 and Type 5 Section 60I certificate, and which is better for my case?",
   "A Type 1 certificate is issued when your ex refused to attend at all. A Type 5 is issued when your ex attended but the FDR practitioner assessed they were not making a genuine effort to resolve the matter. From a court perspective, a Type 5 is actually more powerful because it proves your ex wasted everyone's time and resources by going through the motions without genuine intent. A Type 1 simply records refusal. Both allow you to proceed to court, but a Type 5 has more direct relevance when you later seek a costs order."),
  ("Can my ex get a Section 60I certificate against me if they say I am not genuinely trying?",
   "Yes. The certificate process works both ways. If you attend mediation but the FDR practitioner assesses that you are not making a genuine effort, they can issue a Type 5 certificate naming you as the non-genuine party. This is why it is essential to engage genuinely with any FDR process you participate in, even if you believe the other party will not. Going through the motions can backfire significantly."),
  ("I have an AVO against my ex. Do I still have to try mediation?",
   "Not in the standard format. Where there is an active AVO or domestic violence order, you are entitled to claim the family violence exemption from the Section 60I requirement. You note this on your Initiating Application when you file. You do not need to attend mediation with someone against whom you have a protection order, and no FDR provider should require you to. Shuttle or online mediation may still be possible if you are willing to consider it, but it is your choice — not an obligation."),
  ("My ex lives overseas. Can I still get a Section 60I certificate?",
   "Yes. The FDR provider will make contact attempts using whatever details you provide — international phone number, email address, last known address. If your ex responds and is willing to participate, online mediation via video conference is fully accepted. If they do not respond, the provider documents the attempts and issues a Type 2 (not contactable) certificate. The overseas location does not prevent you from obtaining the certificate or filing in the FCFCOA — though if children are overseas, additional international law considerations apply."),
  ("What happens if we reach a partial agreement in mediation — some issues resolved, some not?",
   "This is very common and is handled well by the process. The FDR provider issues a Type 8 certificate noting that agreement was reached on some but not all issues. You can file in court for orders on the unresolved issues only, while the agreed matters are formalised separately (as a parenting plan or consent orders). Courts strongly prefer to work with partial agreements rather than start from scratch — it saves time and money for everyone.")],
 [("family-mediation-process-guide","Family Mediation Process"),
  ("how-mediation-works","How Mediation Works"),
  ("family-law-mediation","Family Law Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("parenting-mediation","Parenting Mediation")],
 read_min=22
)
