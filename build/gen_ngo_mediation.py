#!/usr/bin/env python3
"""Hub page: Workplace Mediation for NGOs & Not-for-Profits.

Slug: ngo-not-for-profit-mediation

Designed as a pillar/hub page — sub-pages on specific topics anchor from
the 'Explore further' grid at the bottom. Sub-page slugs are listed in
SUBTOPICS; build those as they are written.

Run from build/:
    python3 gen_ngo_mediation.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)
from authority_sources import cite

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SLUG   = "ngo-not-for-profit-mediation"
TITLE  = "NGO & Not-for-Profit Workplace Mediation"
DESC   = ("Independent workplace mediation for NGOs, charities and not-for-profits across Australia. "
          "Resolve executive conflict, board disputes and post-investigation breakdown confidentially.")
H1     = "Workplace mediation for <em>NGOs and not-for-profits</em>."
LEDE   = ("Conflict within a not-for-profit can extend well beyond the people directly involved — "
          "affecting staff, culture, service delivery and the organisation's ability to fulfil its purpose. "
          "Mediations Australia provides independent, confidential mediation for NGOs, charities and "
          "community organisations across Australia.")

# ── Sub-topics: hub links to these pages (build them as separate generators) ──
SUBTOPICS = [
    ("board-executive-conflict-mediation",
     "Board & Executive Conflict",
     "When the relationship between a board and the executive team breaks down."),
    ("post-investigation-workplace-mediation",
     "Post-Investigation Mediation",
     "The investigation is over — but the workplace relationship still needs repair."),
    ("ngo-senior-leadership-mediation",
     "Senior Leadership Conflict",
     "Disputes between CEOs, directors and senior leaders require independent intervention."),
    ("ngo-ceo-conflict-mediation",
     "CEO & Executive Disputes",
     "Confidential mediation when the most senior relationships in the organisation fracture."),
    ("charity-workplace-investigation",
     "Mediation vs Investigation",
     "Understanding which process fits your situation — and when to use both."),
    ("ngo-bullying-grievance-mediation",
     "Bullying & Grievance Mediation",
     "Structured resolution for allegations of bullying or inappropriate workplace behaviour."),
]

FAQ = [
    ("What types of NGO workplace conflicts can mediation resolve?",
     "Mediation can address disputes between CEOs and boards, senior executives, managers and employees, "
     "and teams divided by grievances, allegations or organisational change. It works best where the "
     "parties have an ongoing relationship and a shared interest in the organisation's mission."),
    ("When is mediation not appropriate for an NGO conflict?",
     "Mediation is generally not appropriate where there are serious safety risks, where one party "
     "refuses to participate, or where a formal investigation is required to establish facts before "
     "the working relationship can be addressed. We can discuss your circumstances confidentially "
     "and help identify the right process."),
    ("Can mediation happen after a workplace investigation?",
     "Yes. Post-investigation mediation focuses on the future working relationship rather than the "
     "facts determined by the investigation. It gives the parties a structured opportunity to address "
     "what is needed for a workable professional relationship going forward."),
    ("How confidential is NGO workplace mediation?",
     "Mediation is a confidential process. What is said in mediation generally cannot be used in "
     "subsequent legal proceedings. Mediations Australia also treats all organisational information "
     "shared with us in confidence."),
    ("Can mediation be conducted online for regional or national NGOs?",
     "Yes. We regularly conduct workplace mediation online, which is particularly suited to "
     "organisations with staff in different locations. Online mediation is equally effective for "
     "most workplace disputes."),
    ("How do we start the process?",
     "An authorised representative of your organisation can contact us confidentially to discuss "
     "the circumstances. You do not need to know whether mediation is appropriate before calling — "
     "that is part of what we help you work out."),
]

schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Workplace Mediation","workplace-mediation-guide"),(TITLE, None)]),
    service_schema(TITLE, DESC, SLUG),
    faq_schema([(q, a) for q, a in FAQ]),
]

d = head(TITLE, DESC, SLUG, extra_schema=schema) + nav()

# ── Hero ──────────────────────────────────────────────────────────────────────
d += f"""<main id="main">
{crumb_html([("Home",""),("Workplace Mediation","workplace-mediation-guide"),(esc(TITLE),None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Workplace &amp; Employment Mediation</span>
<h1>{H1}</h1>
<p class="lede">{LEDE}</p>
<div class="phero-cta">
  <a href="{BOOK_URL}" class="btn btn-primary">Speak to a Workplace Mediator <span class="arr">→</span></a>
  <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
</div>
</div></section>

<!-- Answer box -->
<div class="wrap-narrow" style="padding-top:0">
<div class="answer reveal">
<p><strong>In short:</strong> NGOs and not-for-profits often face workplace conflicts that are difficult to
resolve internally — because the people involved are senior, the organisational stakes are high, or because
an investigation has concluded but the relationship hasn't been repaired. An independent external mediator
provides the neutrality, confidentiality and structure needed to address these disputes constructively.</p>
</div>
</div>

<article class="body">
<div class="wrap-narrow">

<h2 id="why-complex">Why conflict is harder to resolve in not-for-profits</h2>
<p>Not-for-profit organisations can be particularly complex workplaces. Employees and leaders are often
deeply committed to the organisation's mission — which means disputes can carry a moral or values dimension
that makes resolution harder, not easier.</p>
<p>Roles frequently involve significant emotional demands, limited resources, complex stakeholder relationships
and strong views about how the organisation should operate. When workplace relationships deteriorate in this
environment, the conflict can quickly become something management or HR cannot resolve internally.</p>
<p>This is especially true when the dispute involves:</p>
<ul>
  <li>Senior executives — whose seniority limits the pool of independent internal actors</li>
  <li>The board and the executive — where formal governance lines make internal mediation inappropriate</li>
  <li>Values or mission disagreements that have become entangled in a personal conflict</li>
  <li>A situation where an internal process has already been tried and failed</li>
</ul>
<p>An external mediator sits outside the organisation's hierarchy, holds no allegiances, and provides
a structured process independent of internal politics.</p>

<h2 id="disputes-we-assist">Disputes we can assist with</h2>
<p>Mediations Australia can assist with NGO and not-for-profit workplace conflicts involving:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 2rem;margin:1.5rem 0">
<ul>
  <li>CEOs and senior executives</li>
  <li>Managers and employees</li>
  <li>Two or more senior employees</li>
  <li>Executive leadership teams</li>
  <li>Board and executive relationships</li>
  <li>Interpersonal workplace conflict</li>
</ul>
<ul>
  <li>Grievances and formal complaints</li>
  <li>Allegations of bullying or inappropriate behaviour</li>
  <li>Conflict following organisational change or restructure</li>
  <li>Damaged relationships following a workplace investigation</li>
  <li>Employees who must continue working together</li>
</ul>
</div>
<p>Our role is not to determine who has "won" the dispute. Mediation provides a structured and confidential
process in which the people involved can identify the issues between them, understand different perspectives
and explore whether an agreed way forward can be reached.</p>

<h2 id="mediation-vs-investigation">Mediation or workplace investigation?</h2>
<p>One of the most important questions for an organisation dealing with serious workplace conflict is
determining the right process. An investigation and a mediation serve fundamentally different purposes.</p>

<table style="width:100%;border-collapse:collapse;margin:1.5rem 0 2rem">
<thead>
<tr style="border-bottom:2px solid var(--sage-deep)">
  <th style="text-align:left;padding:10px 16px 10px 0;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-soft)">Process</th>
  <th style="text-align:left;padding:10px 16px 10px 0;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-soft)">Purpose</th>
  <th style="text-align:left;padding:10px 0;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-soft)">Focus</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--line)">
  <td style="padding:14px 16px 14px 0;font-weight:600">Workplace Investigation</td>
  <td style="padding:14px 16px 14px 0">Establish facts — determine what occurred</td>
  <td style="padding:14px 0;color:var(--ink-soft)">The past</td>
</tr>
<tr>
  <td style="padding:14px 16px 14px 0;font-weight:600">Workplace Mediation</td>
  <td style="padding:14px 16px 14px 0">Resolve conflict — determine how to move forward</td>
  <td style="padding:14px 0;color:var(--ink-soft)">The future</td>
</tr>
</tbody>
</table>

<p>In some situations an investigation is necessary before mediation is considered. In others, the central
problem is not determining what happened but repairing a relationship that has broken down. There are
also circumstances where mediation will not be appropriate.</p>
<p>Mediations Australia can discuss the circumstances of a workplace dispute with an authorised representative
of the organisation and help identify whether mediation is suitable — and when.</p>
<p><a href="/charity-workplace-investigation/" style="font-weight:600">Read more: Mediation vs investigation — which process fits your situation →</a></p>

<h2 id="post-investigation">When the investigation is over but the conflict isn't</h2>
<p>A workplace investigation may determine whether particular allegations are substantiated. It does not
necessarily repair the relationship between the people involved.</p>
<p>Employees may still need to work together. A manager may need to continue managing an employee who made
a complaint. Senior executives may need to rebuild trust after a difficult process. Teams may remain
divided by what occurred.</p>
<p>Post-investigation mediation provides an opportunity to address the future working relationship separately
from the investigation itself. The focus moves from what happened to what is required for a workable
professional relationship going forward.</p>
<p>This is one of the most common reasons NGOs and not-for-profits engage Mediations Australia — the formal
process has concluded, but the human problem remains.</p>
<p><a href="/post-investigation-workplace-mediation/" style="font-weight:600">Read more: Post-investigation mediation — repairing the working relationship →</a></p>

<h2 id="senior-leadership">Senior leadership and executive conflict</h2>
<p>Conflict involving senior leaders presents a particular challenge for not-for-profit organisations.
The dispute may involve a CEO and another executive, two members of the leadership team, a senior employee
and the board, or individuals whose roles make any internal intervention inherently compromised.</p>
<p>The more senior the people involved, the fewer genuinely independent people exist within the organisation
to facilitate the conversation. An external mediator provides independence from the organisation's internal
hierarchy and a structured, confidential process for addressing the issues directly.</p>
<p>Early intervention matters. A senior leadership dispute that remains unresolved can extend beyond the
individuals involved — affecting teams, decision-making and the broader organisation's ability to function.</p>
<p><a href="/ngo-senior-leadership-mediation/" style="font-weight:600">Read more: Senior leadership and executive conflict in NGOs →</a></p>

<h2 id="why-external">Why NGOs use external mediators</h2>
<p>An independent external mediator does not carry the organisational history, reporting relationships or
perceived allegiances that can make internal facilitation ineffective or inappropriate.</p>

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:2rem 0">
  <div style="padding:22px 24px;border-radius:12px;border:1.5px solid var(--line);background:#fff">
    <p style="font-weight:700;margin:0 0 8px;color:var(--sage-deep)">Independence</p>
    <p style="margin:0;font-size:.92rem;color:var(--ink-soft);line-height:1.6">The mediator sits entirely outside the organisation and is not part of its management or HR structure.</p>
  </div>
  <div style="padding:22px 24px;border-radius:12px;border:1.5px solid var(--line);background:#fff">
    <p style="font-weight:700;margin:0 0 8px;color:var(--sage-deep)">Confidentiality</p>
    <p style="margin:0;font-size:.92rem;color:var(--ink-soft);line-height:1.6">Mediation is a confidential process. What is said generally cannot be used in subsequent proceedings.</p>
  </div>
  <div style="padding:22px 24px;border-radius:12px;border:1.5px solid var(--line);background:#fff">
    <p style="font-weight:700;margin:0 0 8px;color:var(--sage-deep)">Neutrality</p>
    <p style="margin:0;font-size:.92rem;color:var(--ink-soft);line-height:1.6">The mediator represents neither party and has no stake in the outcome beyond a workable resolution.</p>
  </div>
  <div style="padding:22px 24px;border-radius:12px;border:1.5px solid var(--line);background:#fff">
    <p style="font-weight:700;margin:0 0 8px;color:var(--sage-deep)">Structure</p>
    <p style="margin:0;font-size:.92rem;color:var(--ink-soft);line-height:1.6">A clear process enables issues that have become difficult to discuss directly to be addressed constructively.</p>
  </div>
  <div style="padding:22px 24px;border-radius:12px;border:1.5px solid var(--line);background:#fff">
    <p style="font-weight:700;margin:0 0 8px;color:var(--sage-deep)">Focus on resolution</p>
    <p style="margin:0;font-size:.92rem;color:var(--ink-soft);line-height:1.6">Where appropriate, mediation moves the conversation toward what is needed for the parties and organisation to move forward.</p>
  </div>
  <div style="padding:22px 24px;border-radius:12px;border:1.5px solid var(--line);background:#fff">
    <p style="font-weight:700;margin:0 0 8px;color:var(--sage-deep)">Mission awareness</p>
    <p style="margin:0;font-size:.92rem;color:var(--ink-soft);line-height:1.6">We understand that people in NGO conflicts often remain deeply committed to the organisation's purpose — even in significant conflict with each other.</p>
  </div>
</div>

<h2 id="our-mediators">Experienced Australian workplace mediators</h2>
<p>Mediations Australia provides mediation services throughout Australia. Our workplace mediators are
nationally accredited and experienced in resolving complex disputes in organisations where the stakes
extend beyond the individuals involved.</p>
<p>We understand that NGO and not-for-profit workplace disputes can involve sensitive employment issues,
reputational considerations, organisational governance and people who remain deeply committed to the
organisation despite being in significant conflict with each other.</p>
<p>Mediation can be conducted online or, where appropriate, in person across all Australian states and territories.
{cite("fair_work")}</p>

<h2 id="explore-further" style="margin-top:3rem">Explore further</h2>
<p>The following guides go deeper on specific situations within NGO and not-for-profit workplace conflict.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;margin:1.5rem 0 2.5rem">
"""

for sub_slug, sub_title, sub_blurb in SUBTOPICS:
    d += (f'<a href="/{sub_slug}/" '
          f'style="display:grid;grid-template-columns:1fr auto;gap:4px 12px;padding:20px 22px;'
          f'background:#fff;border:1.5px solid var(--line);border-radius:12px;'
          f'text-decoration:none;color:var(--ink);transition:all .15s" '
          f'onmouseover="this.style.borderColor=\'var(--sage)\';this.style.boxShadow=\'0 4px 16px rgba(0,0,0,.08)\'" '
          f'onmouseout="this.style.borderColor=\'var(--line)\';this.style.boxShadow=\'none\'">'
          f'<span style="font-weight:600;font-size:.97rem;grid-column:1;line-height:1.4">{esc(sub_title)}</span>'
          f'<span style="font-size:.86rem;color:var(--ink-soft);line-height:1.55;grid-column:1;margin-top:4px">{esc(sub_blurb)}</span>'
          f'<span style="grid-column:2;grid-row:1/3;color:var(--sage-deep);align-self:center;opacity:.4;font-size:1.1rem">→</span>'
          f'</a>\n')

d += f"""</div>

<p style="font-size:.92rem;color:var(--ink-soft);border-top:1px solid var(--line);padding-top:1.5rem;margin-top:1rem">
Related: <a href="/workplace-mediation-guide/">Workplace Mediation in Australia</a> ·
<a href="/high-conflict-mediation/">High-Conflict Mediation</a> ·
<a href="/how-much-does-mediation-cost/">Mediation Costs</a> ·
<a href="/online-mediation-australia/">Online Mediation</a>
</p>

</div>
</article>
"""

d += faq_html(FAQ, heading="NGO &amp; Not-for-Profit Mediation: Common Questions")
d += cta_band(
    "Dealing with a difficult workplace conflict?",
    "Speak confidentially with Mediations Australia. You don't need to know whether mediation "
    "is the right step — that is part of what we help you work out."
)
d += "</main>" + page_end()

out_dir = os.path.join(OUT, SLUG)
os.makedirs(out_dir, exist_ok=True)
open(os.path.join(out_dir, "index.html"), "w").write(d)
print(f"Built: /{SLUG}/  ({len(d):,} chars)")
