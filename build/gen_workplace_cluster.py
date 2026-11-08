#!/usr/bin/env python3
"""Workplace cluster service pages (brief §5.3, §5.4).

  /employment-dispute-mediation/  — private mediation for employment disputes, vs Fair Work processes
  /team-conflict-facilitation/    — multi-party team facilitation (quoted on request)

Pricing comes only from workplace_pricing. Dan's details use only the source-checked wording in
brief §5.6. DRAFT — employment-law statements need legal review before publication.
Run:  python3 build/gen_workplace_cluster.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_services_v2 import inline_cta, key_takeaway, service_page
from authority_sources import cite
from workplace_pricing import price_block, offers_schema

CTA_HREF = "/contact-us/"

DAN_LINE = ('<p><strong>About the mediator.</strong> Dan Toombs is an AMDRAS-accredited mediator and a former Member of '
            'the Guardianship and Administration Tribunal (Queensland), whose jurisdiction is now within QCAT. He has '
            'mediated workplace disputes across professional services, healthcare, education, construction, and the '
            'not-for-profit sector. <a href="/our-team/dan-toombs/">View Dan\'s profile</a>. Who mediates a particular '
            'matter depends on suitability and availability.</p>')

# ─────────────────────────────────────────────────────────────────────────────
# Employment dispute mediation
# ─────────────────────────────────────────────────────────────────────────────
service_page(
    slug="employment-dispute-mediation",
    title="Employment Dispute Mediation in Australia | Mediations Australia",
    desc="Explore independent mediation for employment disputes, how it differs from Fair Work processes and what to clarify before choosing a pathway.",
    breadcrumb_label="Employment Dispute Mediation",
    eyebrow="Employment disputes",
    h1_html="Employment dispute <em>mediation</em>",
    lede=("Employment dispute mediation helps the people involved explore an agreed resolution without asking the mediator "
          "to decide legal liability. It can sit alongside legal advice or formal procedures. Check any statutory deadline "
          "or required dispute procedure promptly: arranging private mediation does not stop a filing deadline or replace "
          "a regulator's role."),
    toc_items=[
        ("disputes", "Which employment disputes fit"),
        ("pathways", "Private mediation, the Commission and the Ombudsman"),
        ("before", "Before you refer a matter"),
        ("intake", "Intake and representation"),
        ("outcomes", "Possible outcomes and legal review"),
        ("fees", "Fees and suitability"),
    ],
    takeaway=key_takeaway(
        "Employment dispute mediation is a private, voluntary process in which an independent mediator helps an employer and "
        "employee, or colleagues, work towards their own agreement. Mediations Australia is not part of the Fair Work system, "
        "and private mediation does not pause statutory deadlines: unfair dismissal applications, for example, must be made "
        "to the Fair Work Commission within 21 days of the dismissal."
    ),
    body_html=f"""
<h2 id="disputes">Which employment disputes fit</h2>
<p>Private mediation tends to suit disputes where both sides are willing to talk and want more control over the outcome than a formal process offers:</p>
<ul>
  <li><strong>Working-relationship disputes</strong> between an employee and a manager, or between colleagues.</li>
  <li><strong>Grievances</strong> that have been raised but where both sides would prefer an agreed resolution, once any required investigation has been dealt with.</li>
  <li><strong>Exit discussions</strong>, where an employment relationship is ending and both sides want to agree terms. Each party should have independent legal advice.</li>
</ul>
<p>Mediation is not a substitute for a statutory claim where one is needed, and it is not appropriate where safety concerns or serious allegations need a different response first. See our <a href="/is-mediation-right-for-workplace-dispute/">suitability guide</a>.</p>
""" + inline_cta("Not sure whether private mediation fits your employment dispute?", btn="Ask whether mediation fits", href=CTA_HREF) + f"""

<h2 id="pathways">Private mediation, the Commission and the Ombudsman</h2>
<figure class="tbl"><table><caption>Three different pathways</caption>
<thead><tr><th></th><th>Private mediation</th><th>Fair Work Commission</th><th>Fair Work Ombudsman</th></tr></thead>
<tbody>
<tr><td>What it is</td><td>A private service arranged by agreement</td><td>The national workplace relations tribunal</td><td>The regulator for workplace rights and entitlements</td></tr>
<tr><td>How it starts</td><td>Employer and/or employee contact a mediator</td><td>Usually an application is lodged</td><td>An enquiry or request for help</td></tr>
<tr><td>Who decides</td><td>The parties, by agreement</td><td>Conciliation by agreement; some matters can be determined</td><td>Does not determine unfair dismissal claims</td></tr>
<tr><td>Deadlines</td><td>Does not stop statutory time limits</td><td>Strict filing deadlines for some claims</td><td>Depends on the issue</td></tr>
</tbody></table></figure>
<p>The Fair Work Ombudsman says it does not investigate unfair dismissal complaints, and that people who think they have been unfairly dismissed apply to the Commission <strong>within 21 days</strong> of the dismissal ({cite("fwo_unfair_dismissal")}). For the Commission's own processes, see the {cite("fair_work")}. Mediations Australia is a private provider and has no affiliation with either body.</p>

<h2 id="before">Before you refer a matter</h2>
<ul>
  <li><strong>Check deadlines first.</strong> If a statutory claim may apply, get advice immediately; do not wait for mediation.</li>
  <li><strong>Check your policies and agreements.</strong> An enterprise agreement, award or workplace policy may set out a required dispute procedure.</li>
  <li><strong>Get legal advice</strong> on your rights and options, especially before exit or settlement discussions.</li>
  <li><strong>Confirm authority to settle.</strong> The person attending for the employer needs authority to agree to practical changes or terms.</li>
</ul>

<h2 id="intake">Intake and representation</h2>
<p>The mediator meets each party separately before the session to understand the dispute, any safety or power-imbalance concerns, and who will attend. Whether lawyers, union representatives or support people attend is discussed and agreed in advance, so everyone knows who will be in the room. Intake with each party is included in the fee.</p>

<h2 id="outcomes">Possible outcomes and legal review</h2>
<p>If agreement is reached, the practical terms are written down. Whether an agreement is legally binding, and how it is enforced, depends on its terms and the formalities followed; there is no universal answer. Where an agreement settles legal claims or ends employment, each party should have it reviewed by their own lawyer before signing. If agreement is not reached, the parties keep their other options.</p>
""" + inline_cta("Want to talk through an employment dispute in confidence?", btn="Ask whether mediation fits", href=CTA_HREF) + f"""

<h2 id="fees">Fees and suitability</h2>
{price_block()}
<p>See <a href="/workplace-mediation-cost/">workplace mediation cost</a> for examples with additional parties. The first step is a confidential conversation about whether mediation suits the dispute.</p>
{DAN_LINE}
<p>Related: <a href="/unfair-dismissal-termination-mediation/">unfair dismissal and termination</a> · <a href="/general-protections-discrimination-mediation/">general protections and discrimination</a> · <a href="/workplace-dispute-guide/">workplace dispute guide</a>.</p>
""",
    faq_items=[
        ("Is Mediations Australia part of Fair Work?",
         "No. Mediations Australia is a private mediation provider. It is not part of, or affiliated with, the Fair Work Commission or the Fair Work Ombudsman."),
        ("Does mediation pause Fair Work deadlines?",
         "No. Arranging private mediation does not stop statutory time limits. For example, unfair dismissal applications must be made to the Fair Work Commission within 21 days of the dismissal. Get advice promptly if a claim may apply."),
        ("Who can refer an employment dispute?",
         "An employer, an employee, or both together. Everyone must agree to take part. Where one party makes contact, we ask the other whether they are willing to participate."),
        ("Can lawyers or union representatives attend?",
         "Often, yes. Who attends, and in what role, is discussed at intake and agreed before the session so that everyone knows who will be present."),
        ("Is a mediated agreement enforceable?",
         "It depends on the agreement's terms and the formalities followed; there is no universal answer. Where an agreement settles legal claims or ends employment, each party should have it reviewed by their own lawyer before signing."),
    ],
    related_items=[
        ("workplace-mediation", "Workplace Mediation"),
        ("workplace-dispute-guide", "Workplace Dispute Guide"),
        ("unfair-dismissal-termination-mediation", "Unfair Dismissal & Termination"),
        ("general-protections-discrimination-mediation", "General Protections & Discrimination"),
        ("workplace-mediation-cost", "Workplace Mediation Cost"),
    ],
    offers=offers_schema("employment-dispute-mediation"),
)

# ─────────────────────────────────────────────────────────────────────────────
# Team conflict facilitation (quoted on request — no numeric price)
# ─────────────────────────────────────────────────────────────────────────────
service_page(
    slug="team-conflict-facilitation",
    title="Team Conflict Facilitation for Australian Workplaces",
    desc="Facilitated sessions for teams in conflict: how multi-party facilitation differs from two-party mediation, what it involves, and how it is scoped and quoted.",
    breadcrumb_label="Team Conflict Facilitation",
    eyebrow="Team and group conflict",
    h1_html="Team conflict facilitation for <em>Australian workplaces</em>",
    lede=("When conflict involves a whole team rather than two people, a facilitated process designed for the group usually "
          "works better than standard mediation. Team conflict facilitation helps a team talk about what is getting in the way "
          "and agree practical ways of working. It is scoped for each team and quoted on request."),
    toc_items=[
        ("difference", "Team facilitation vs two-party mediation"),
        ("scope", "Commissioning and scope"),
        ("intake", "Separate intake"),
        ("session", "Session design and psychological safety"),
        ("practices", "Agreed team practices and follow-up"),
        ("pricing", "How it is quoted"),
    ],
    takeaway=key_takeaway(
        "Team conflict facilitation is a structured, multi-party process for teams whose working relationships have broken down. "
        "It starts with agreeing scope with the organisation, includes separate intake conversations, and aims for agreed team "
        "practices with a follow-up review. It is not an investigation or a personality assessment, and it is quoted on request."
    ),
    body_html=f"""
<h2 id="difference">Team facilitation vs two-party mediation</h2>
<p>Two-party mediation focuses on a dispute between two people. Team facilitation works with a group: several relationships, shared ways of working, and often a history that different people experienced differently. It usually involves more preparation, a different session structure, and agreements that the whole team owns. If the core issue is really between two people, standard <a href="/workplace-mediation/">workplace mediation</a> may be the better starting point.</p>

<h2 id="scope">Commissioning and scope</h2>
<p>The organisation commissioning the work (often HR, a senior leader or the board) agrees with the facilitator what the process is for, who will take part, what is in and out of scope, and what, if anything, will be reported back. Facilitation is not used to resolve allegations that need investigation, and it does not replace safety or legal obligations.</p>

<h2 id="intake">Separate intake</h2>
<p>Before any group session, the facilitator speaks with team members individually. This surfaces the issues people are willing to raise, any safety concerns, and whether a group session is appropriate at all. Individual conversations are handled according to the confidentiality terms agreed at the start.</p>
""" + inline_cta("Leading a team where conflict is affecting the work? Start with a confidential scoping conversation.", btn="Discuss your team", href=CTA_HREF) + f"""

<h2 id="session">Session design and psychological safety</h2>
<p>Sessions are designed around the team: ground rules everyone agrees to, a structure that gives quieter members a voice, and attention to power differences between roles. The focus is on behaviour, working practices and what the team needs to work well, not on diagnosing personalities. Where it helps, frameworks such as <a href="/belbin-team-roles-training/">Belbin Team Roles</a> can give the team a shared, non-personal language for differences in how people contribute.</p>

<h2 id="practices">Agreed team practices and follow-up</h2>
<p>The aim is a short set of agreed practices: how the team communicates, makes decisions, hands over work and raises problems early. A follow-up session checks what is working and what needs adjusting. Absent members are considered in the design, so the agreement does not depend on people who were not part of it.</p>
<p><strong>About the facilitator.</strong> Dan Toombs is an Accredited Belbin Team Roles Facilitator and has trained in Adaptive Leadership through the Australian Adaptive Leadership Institute. He is also an AMDRAS-accredited mediator. <a href="/our-team/dan-toombs/">View Dan's profile</a>. Allocation depends on availability.</p>

<h2 id="pricing">How it is quoted</h2>
<p>Group and team facilitation is <strong>quoted on request</strong>, because the work depends on team size, intake, session design and follow-up. It is not priced as the two-party mediation fee plus extra parties. For two-party disputes, see <a href="/workplace-mediation-cost/">workplace mediation cost</a>.</p>
""",
    faq_items=[
        ("Who attends a team facilitation session?",
         "Usually the members of the team involved, agreed with the commissioning organisation during scoping. Whether a manager or leader attends, and in what role, is decided deliberately because it affects how safe people feel to speak."),
        ("What is reported back to the organisation?",
         "Only what is agreed in writing at the start. Often that is whether sessions went ahead and any team practices the group agrees to share. The limits of confidentiality, such as safety risks or legal obligations, are explained in advance."),
        ("What if some team members won't take part?",
         "Participation should be voluntary. The facilitator considers absent members when designing the process, so the team's agreements do not depend on people who were not part of them."),
        ("Is there follow-up?",
         "Usually, yes. A follow-up session reviews which agreed practices are working and what needs to change. Whether follow-up is included is set out in the scope agreed when the work is quoted."),
    ],
    related_items=[
        ("workplace-mediation", "Workplace Mediation"),
        ("belbin-team-roles-training", "Belbin Team Roles Training"),
        ("workplace-mediation-cost", "Workplace Mediation Cost"),
        ("conflict-resolution-in-the-workplace", "Workplace Conflict Resolution"),
    ],
)
print("built employment-dispute-mediation, team-conflict-facilitation")
