#!/usr/bin/env python3
"""/ngo-not-for-profit-mediation/ — built on the shared service-page template
(gen_services_v2.service_page), the same layout as /commercial-mediation/.

Content carried over from the live page, including the stage-5 additions previously
applied by patch_stage5_pages.ngo(). Fees come from workplace_pricing (workplace URL only).
Run from repo root:  python3 build/gen_ngo_mediation.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_services_v2 import inline_cta, key_takeaway, service_page
from authority_sources import cite
from workplace_pricing import price_block, offers_schema

DAN_CARD = ('<div style="display:flex;gap:1.25rem;align-items:flex-start;flex-wrap:wrap;padding:1.25rem;border:1px solid var(--line);'
            'border-radius:12px;background:var(--cream);margin:1rem 0">'
            '<img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder and Mediator, Mediations Australia" width="88" height="88" '
            'loading="lazy" style="border-radius:50%;object-fit:cover;width:88px;height:88px;flex-shrink:0">'
            '<div style="flex:1;min-width:220px"><p style="margin:0 0 .5rem">Dan Toombs is an <strong>AMDRAS-accredited mediator</strong>. '
            'He has led a community legal centre as <strong>CEO</strong> and served as a <strong>Board Director of Legal Aid Queensland</strong>, '
            'and is a former <strong>Member of the Guardianship and Administration Tribunal (Queensland)</strong>, whose jurisdiction is now within QCAT. '
            'Dan has mediated workplace disputes across professional services, healthcare, education, construction, and the not-for-profit sector.</p>'
            '<p style="margin:0"><a href="/our-team/dan-toombs/">View Dan\'s profile →</a> Who mediates a matter depends on suitability and availability.</p></div></div>')

SLUG = "ngo-not-for-profit-mediation"
CTA = dict(btn="Speak to a Workplace Mediator", href="/book-a-consultation/")

service_page(
    slug=SLUG,
    title="Workplace Mediation for NGOs &amp; Not-for-Profits",
    desc="Independent mediation for NGO and charity workplace disputes, including leadership conflict, grievances and repairing working relationships after investigation.",
    breadcrumb_label="NGO &amp; Not-for-Profit Mediation",
    eyebrow="Workplace &amp; Employment Mediation",
    h1_html="Workplace mediation for <em>NGOs and not-for-profits</em>",
    lede=("Conflict within a not-for-profit can extend well beyond the people directly involved, affecting staff, culture, "
          "service delivery and the organisation's ability to fulfil its purpose. Mediations Australia provides independent, "
          "confidential mediation for NGOs, charities and community organisations across Australia."),
    toc_items=[
        ("why-harder", "Why conflict is harder in not-for-profits"),
        ("disputes", "Disputes we can assist with"),
        ("mediation-vs-investigation", "Mediation or workplace investigation?"),
        ("post-investigation", "When the investigation is over"),
        ("senior-leadership", "Senior leadership and executive conflict"),
        ("why-external", "Why NGOs use external mediators"),
        ("who-commissions", "Who can commission mediation"),
        ("confidentiality-scope", "Consent, confidentiality and reporting"),
        ("scenarios", "Illustrative scenarios"),
        ("process-map", "How the process works"),
        ("ngo-fees", "Fees"),
        ("our-mediators", "Our workplace mediators"),
    ],
    takeaway=key_takeaway(
        "NGOs and not-for-profits often face workplace conflicts that are difficult to resolve internally, because the people "
        "involved are senior, the organisational stakes are high, or an investigation has concluded but the relationship hasn't "
        "been repaired. An independent external mediator provides the neutrality, confidentiality and structure needed to address "
        "these disputes constructively."
    ),
    body_html=f"""
<h2 id="why-harder">Why conflict is harder to resolve in not-for-profits</h2>
<p>Not-for-profit organisations can be particularly complex workplaces. Employees and leaders are often deeply committed to the organisation's mission, which means disputes can carry a moral or values dimension that makes resolution harder, not easier.</p>
<p>Roles frequently involve significant emotional demands, limited resources, complex stakeholder relationships and strong views about how the organisation should operate. When workplace relationships deteriorate in this environment, the conflict can quickly become something management or HR cannot resolve internally.</p>
<p>This is especially true when the dispute involves:</p>
<ul>
<li><strong>Senior executives</strong>, whose seniority limits the pool of independent internal actors</li>
<li><strong>The board and the executive</strong>, where formal governance lines make internal mediation inappropriate</li>
<li><strong>Values or mission disagreements</strong> that have become entangled in a personal conflict</li>
<li>A situation where an <strong>internal process has already been tried</strong> and failed</li>
</ul>
<p>An external mediator sits outside the organisation's hierarchy, holds no allegiances, and provides a structured process independent of internal politics.</p>
{inline_cta("Not sure whether an internal or external process fits? A confidential conversation can help.", **CTA)}

<h2 id="disputes">Disputes we can assist with</h2>
<p>Mediations Australia can assist with NGO and not-for-profit workplace conflicts involving:</p>
<ul>
<li>CEOs and senior executives</li>
<li>Managers and employees</li>
<li>Two or more senior employees</li>
<li>Executive leadership teams</li>
<li>Board and executive relationships</li>
<li>Interpersonal workplace conflict</li>
<li>Grievances and formal complaints</li>
<li>Allegations of bullying or inappropriate behaviour (see <a href="/workplace-bullying-harassment-mediation/">bullying and grievance mediation</a>)</li>
<li>Conflict following organisational change or restructure</li>
<li>Damaged relationships following a workplace investigation</li>
<li>Employees who must continue working together</li>
</ul>
<p>Our role is not to determine who has "won" the dispute. Mediation provides a structured and confidential process in which the people involved can identify the issues between them, understand different perspectives and explore whether an agreed way forward can be reached.</p>

<h2 id="mediation-vs-investigation">Mediation or workplace investigation?</h2>
<p>One of the most important questions for an organisation dealing with serious workplace conflict is determining the right process. An investigation and a mediation serve fundamentally different purposes.</p>
<figure class="tbl"><table>
<thead><tr><th>Process</th><th>Purpose</th><th>Focus</th></tr></thead>
<tbody>
<tr><td><strong>Workplace investigation</strong></td><td>Establish facts: determine what occurred</td><td>The past</td></tr>
<tr><td><strong>Workplace mediation</strong></td><td>Resolve conflict: determine how to move forward</td><td>The future</td></tr>
</tbody></table></figure>
<p>In some situations an investigation is necessary before mediation is considered. In others, the central problem is not determining what happened but repairing a relationship that has broken down. There are also circumstances where mediation will not be appropriate.</p>
<p>Mediations Australia can discuss the circumstances of a workplace dispute with an authorised representative of the organisation and help identify whether mediation is suitable, and when.</p>
{inline_cta("Talk through which process fits your situation, in confidence.", **CTA)}

<h2 id="post-investigation">When the investigation is over but the conflict isn't</h2>
<p>A workplace investigation may determine whether particular allegations are substantiated. It does not necessarily repair the relationship between the people involved.</p>
<p>Employees may still need to work together. A manager may need to continue managing an employee who made a complaint. Senior executives may need to rebuild trust after a difficult process. Teams may remain divided by what occurred.</p>
<p>Post-investigation mediation provides an opportunity to address the future working relationship separately from the investigation itself. The focus moves from what happened to what is required for a workable professional relationship going forward.</p>
<p>This is one of the most common reasons NGOs and not-for-profits engage Mediations Australia: the formal process has concluded, but the human problem remains.</p>

<h2 id="senior-leadership">Senior leadership and executive conflict</h2>
<p>Conflict involving senior leaders presents a particular challenge for not-for-profit organisations. The dispute may involve a CEO and another executive, two members of the leadership team, a senior employee and the board, or individuals whose roles make any internal intervention inherently compromised.</p>
<p>The more senior the people involved, the fewer genuinely independent people exist within the organisation to facilitate the conversation. An external mediator provides independence from the organisation's internal hierarchy and a structured, confidential process for addressing the issues directly.</p>
<p>Early intervention matters. A senior leadership dispute that remains unresolved can extend beyond the individuals involved, affecting teams, decision-making and the broader organisation's ability to function.</p>
{inline_cta("Senior leadership dispute? Speak with a mediator independent of your organisation.", **CTA)}

<h2 id="why-external">Why NGOs use external mediators</h2>
<p>An independent external mediator does not carry the organisational history, reporting relationships or perceived allegiances that can make internal facilitation ineffective or inappropriate.</p>
<ul>
<li><strong>Independence.</strong> The mediator sits entirely outside the organisation and is not part of its management or HR structure.</li>
<li><strong>Confidentiality.</strong> Mediation is a confidential process. What is said generally cannot be used in subsequent proceedings.</li>
<li><strong>Neutrality.</strong> The mediator represents neither party and has no stake in the outcome beyond a workable resolution.</li>
<li><strong>Structure.</strong> A clear process enables issues that have become difficult to discuss directly to be addressed constructively.</li>
<li><strong>Focus on resolution.</strong> Where appropriate, mediation moves the conversation toward what is needed for the parties and organisation to move forward.</li>
<li><strong>Mission awareness.</strong> We understand that people in NGO conflicts often remain deeply committed to the organisation's purpose, even in significant conflict with each other.</li>
</ul>

<h2 id="who-commissions">Who can commission mediation</h2>
<p>Mediation is usually commissioned by someone with authority to act for the organisation: the HR lead, the CEO, or the board. Where the CEO or a board member is one of the people in the dispute, the board chair or a delegated committee normally commissions it instead, so the process is not controlled by a party. We confirm who is commissioning, and who has authority to agree practical changes, before intake.</p>

<h2 id="confidentiality-scope">Consent, confidentiality and reporting</h2>
<p>Everyone who takes part must agree to participate. Before intake, the organisation and participants agree in writing what, if anything, will be reported back (often only whether mediation went ahead and any actions the participants agree to share), how records are handled, and the limits of confidentiality, such as safety risks or legal and governance obligations. We do not promise absolute confidentiality.</p>

<h2 id="scenarios">Illustrative scenarios</h2>
<p>The scenarios below are <strong>illustrative only</strong>. They are not client case studies.</p>
<ul>
<li><strong>Program team after a restructure.</strong> Two program managers whose roles now overlap are in open conflict, affecting service delivery. Mediation focuses on role boundaries and handovers.</li>
<li><strong>CEO and board chair.</strong> Disagreement about strategy has become personal. The board delegates commissioning to a committee, and mediation focuses on decision-making protocols.</li>
<li><strong>After an investigation.</strong> An investigation has concluded, but the team remains divided. Mediation helps people agree how they will work together from here; it does not revisit the findings.</li>
</ul>

<h2 id="process-map">How the process works</h2>
<ol>
<li><strong>Confidential enquiry</strong> with the person commissioning, about suitability, safety and any formal process underway.</li>
<li><strong>Decide the pathway:</strong> mediation, an investigation first, team facilitation, or another process.</li>
<li><strong>Agree scope and reporting</strong> in writing.</li>
<li><strong>Separate intake</strong> with each participant (included in the fee).</li>
<li><strong>Mediation session</strong>, online or in person.</li>
<li><strong>Agreed actions</strong> written down, with a review if useful.</li>
</ol>
{inline_cta("Ready to start? An authorised representative can contact us confidentially.", **CTA)}

<h2 id="ngo-fees">Fees</h2>
{price_block()}
<p>See <a href="/workplace-mediation-cost/">workplace mediation cost</a> for examples with additional parties. Team-wide work is quoted on request; see <a href="/team-conflict-facilitation/">team conflict facilitation</a>.</p>

<h2 id="our-mediators">Experienced Australian workplace mediators</h2>
{DAN_CARD}
<p>Mediations Australia provides mediation services throughout Australia. Our workplace mediators are nationally accredited and experienced in resolving complex disputes in organisations where the stakes extend beyond the individuals involved.</p>
<p>We understand that NGO and not-for-profit workplace disputes can involve sensitive employment issues, reputational considerations, organisational governance and people who remain deeply committed to the organisation despite being in significant conflict with each other.</p>
<p>Mediation can be conducted online or, where appropriate, in person across all Australian states and territories. For statutory workplace matters, see the {cite('fair_work')}.</p>
<p>See also: <a href="/workplace-mediation/">workplace mediation</a>, <a href="/high-conflict-mediation/">high-conflict mediation</a> and <a href="/online-mediation-australia/">online mediation</a>.</p>
""",
    faq_items=[
        ("What types of NGO workplace conflicts can mediation resolve?",
         "Mediation can address disputes between CEOs and boards, senior executives, managers and employees, and teams divided by grievances, allegations or organisational change. It works best where the parties have an ongoing relationship and a shared interest in the organisation's mission."),
        ("When is mediation not appropriate for an NGO conflict?",
         "Mediation is generally not appropriate where there are serious safety risks, where one party refuses to participate, or where a formal investigation is required to establish facts before the working relationship can be addressed. We can discuss your circumstances confidentially and help identify the right process."),
        ("Can mediation happen after a workplace investigation?",
         "Yes. Post-investigation mediation focuses on the future working relationship rather than the facts determined by the investigation. It gives the parties a structured opportunity to address what is needed for a workable professional relationship going forward."),
        ("How confidential is NGO workplace mediation?",
         "Mediation is a confidential process. What is said in mediation generally cannot be used in subsequent legal proceedings. Mediations Australia also treats all organisational information shared with us in confidence."),
        ("Can mediation be conducted online for regional or national NGOs?",
         "Yes. We regularly conduct workplace mediation online, which is particularly suited to organisations with staff in different locations. Many workplace mediations can be conducted online; whether online suits a particular dispute is assessed at intake."),
        ("How do we start the process?",
         "An authorised representative of your organisation can contact us confidentially to discuss the circumstances. You do not need to know whether mediation is appropriate before calling; that is part of what we help you work out."),
        ("Who authorises an NGO mediation?",
         "Usually the HR lead, CEO or board. Where the CEO or a board member is a party, the board chair or a delegated committee normally commissions the mediation so that the process is not controlled by someone involved in the dispute."),
        ("Can mediation help a conflict between the CEO and the board?",
         "It can, where both are willing and there are no safety or governance issues that need a different process first. Commissioning is usually delegated to a committee, and the focus is often on roles and decision-making protocols."),
        ("Should we investigate first?",
         "Where serious allegations need findings of fact, or there are safety or legal obligations, an investigation usually comes first. Mediation can help rebuild working relationships after it concludes."),
        ("Who receives the outcome of the mediation?",
         "Only what is agreed in writing before intake. Often that is whether mediation went ahead and any agreed actions the participants consent to share with the organisation."),
    ],
    related_items=[
        ("workplace-mediation", "Workplace Mediation"),
        ("workplace-mediation-cost", "Workplace Mediation Cost"),
        ("team-conflict-facilitation", "Team Conflict Facilitation"),
        ("workplace-bullying-harassment-mediation", "Bullying &amp; Grievance Mediation"),
        ("workplace-mediation-guide", "Workplace Mediation: Complete Guide"),
        ("how-much-does-mediation-cost", "Mediation Costs"),
    ],
    offers=offers_schema(SLUG),
    bg_image="/assets/images/hero-workplace-investigations-mediation.jpg",
    bg_pos="center 50%",
)
