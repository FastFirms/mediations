#!/usr/bin/env python3
"""Belbin Team Roles Training service page."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

slug  = "belbin-team-roles-training"
title = "Belbin Team Roles Training Australia | Mediations Australia"
desc  = "Accredited Belbin Team Roles training with Dan Toombs. Prevent workplace conflict by building balanced teams and giving everyone a shared language for difference."
crumb = "Belbin Team Roles Training"
eyebrow = "Team development &amp; conflict prevention"
h1    = "Belbin Team Roles Training — <em>build balanced teams before disputes start</em>."
lede  = ("Most workplace disputes are not personality clashes — they are role problems. "
         "Belbin Team Roles training gives your people a proven, research-backed framework "
         "for understanding how they contribute, where friction is likely, and how to design "
         "it out before a conflict ever lands on a manager's desk.")
ans   = ("Belbin Team Roles training is a research-backed team development programme that identifies each person's natural behavioural contribution, balances your team's role mix, and gives everyone a shared non-personal language for difference — preventing the role confusion and conflict that WHS psychosocial hazard law requires you to manage.")

qa = [
    ("What are Belbin Team Roles?",
     "Belbin Team Roles is a framework developed by Dr Meredith Belbin, based on nine years of research at Henley Management College. It identifies nine clusters of behavioural contributions — Plant, Monitor Evaluator, Specialist, Co-ordinator, Teamworker, Resource Investigator, Shaper, Implementer, and Completer Finisher — and shows how balanced teams outperform unbalanced ones regardless of individual talent."),
    ("How does Belbin training prevent workplace disputes?",
     "Role confusion and role conflict are formally recognised psychosocial hazards under Australia's Work Health and Safety framework. When people don't understand each other's contributions, or responsibilities overlap without clarity, conflict is close to inevitable. Belbin training replaces ambiguity with a shared language, so everyday difference is understood as complementary behaviour rather than personal friction."),
    ("Who facilitates Belbin training at Mediations Australia?",
     "Training is facilitated by Dan Toombs, an Accredited Belbin Team Roles Facilitator and the founder of Mediations Australia. Dan combines the Belbin framework with his background as a Nationally Accredited (AMDRAS) mediator — a pairing that grounds the training in what actually causes and resolves disputes, not just theory."),
    ("What does a Belbin engagement include?",
     "A typical engagement includes Belbin Self-Perception Inventories and Observer Assessments for each participant, an Individual Report and a Team Report, a facilitated workshop interpreting the team's profile and gaps, manager training in applying the framework, and optional integration with workplace mediation where a team has already experienced conflict."),
    ("Is Belbin training available online?",
     "Yes. Belbin training is available in person or via secure video conferencing, Australia-wide."),
    ("How does Belbin training relate to our WHS obligations?",
     "Safe Work Australia formally lists role ambiguity and role conflict as psychosocial hazards that a PCBU must identify and control. Belbin training is a direct, evidence-based control measure — it clarifies roles, builds shared understanding, and addresses the root cause rather than the symptom. Engaging in proactive team development also demonstrates a business is taking its psychosocial risk obligations seriously."),
]

blocks = """
<h2>Most workplace disputes are role problems in disguise</h2>
<p>When conflict surfaces between colleagues, it usually looks personal. But working with organisations
on team dynamics, a pattern emerges: the argument on the surface is rarely the
real problem. Underneath it sits confusion about who is responsible for what, who decides,
and whose contribution actually counts.</p>

<p>Australia's work health and safety regulators now formally recognise this. Safe Work
Australia identifies <strong>role ambiguity</strong> and <strong>role conflict</strong> as
distinct psychosocial hazards — ones a PCBU has a positive duty to identify and control.
Belbin training is the most direct, evidence-based control measure available: it replaces
ambiguity with clarity before any dispute arises.</p>

<div class="callout">
  <h3>The pipeline regulators have mapped</h3>
  <p>Safe Work Australia is explicit: unclear roles lead to relationship conflict, which can
  lead to psychological harm and bullying complaints. Belbin training attacks the problem at
  the start of that pipeline — not the end.</p>
</div>

<h2>What the research shows: balance beats brilliance</h2>
<p>Belbin Team Roles was developed by Dr Meredith Belbin and his team through nearly a decade
of study at Henley Management College, observing real management teams competing in business
simulations. The central finding was counter-intuitive: teams assembled from high-intellect
individuals often underperformed, while <em>balanced</em> teams — those combining the right
mix of behavioural contributions — consistently outperformed them.</p>

<p>The nine roles Belbin identified fall into three families:</p>

<figure class="tbl">
<table>
<caption>The nine Belbin Team Roles</caption>
<thead><tr><th>Family</th><th>Role</th><th>Contribution</th></tr></thead>
<tbody>
  <tr><td rowspan="3">Thinking</td><td>Plant</td><td>Creative, original ideas and novel solutions</td></tr>
  <tr><td>Monitor Evaluator</td><td>Strategic, discerning; weighs options accurately</td></tr>
  <tr><td>Specialist</td><td>In-depth expertise in a narrow field</td></tr>
  <tr><td rowspan="3">Social</td><td>Co-ordinator</td><td>Clarifies goals, delegates, builds consensus</td></tr>
  <tr><td>Teamworker</td><td>Co-operative, diplomatic, averts friction</td></tr>
  <tr><td>Resource Investigator</td><td>Explores opportunities, builds external contacts</td></tr>
  <tr><td rowspan="3">Action</td><td>Shaper</td><td>Drives the team through obstacles under pressure</td></tr>
  <tr><td>Implementer</td><td>Turns ideas into reliable, practical action</td></tr>
  <tr><td>Completer Finisher</td><td>Polishes, perfects, catches errors at the end</td></tr>
</tbody>
</table>
</figure>

<p>Belbin's core recommendation: all nine roles should be present in a team, and no relevant
role should be missing. Too many Shapers competing to lead produces friction; a team of pure
Teamworkers avoids hard conversations until they explode.</p>

<h2>What a Belbin engagement involves</h2>

<h3>1. Assessments</h3>
<p>Each participant completes the Belbin Self-Perception Inventory, combined with Observer
Assessments from colleagues — a 360-degree view that shows how each person sees their own
behaviour versus how the team experiences it. This produces an Individual Report for each
person and a Team Report showing the group's full role distribution and gaps.</p>

<h3>2. Team Report Interpretation Workshop</h3>
<p>A facilitated session reads the team's profile aloud: where the team is strong, which
roles are missing or duplicated, and where predictable friction sits. "We keep having the
same argument" becomes "we have four Shapers and no Completer Finisher."</p>

<h3>3. A shared, non-personal language</h3>
<p>The most durable outcome of Belbin work is depersonalisation. When a colleague's constant
questioning is understood as Monitor Evaluator rigour rather than obstructionism, and another's
attention to detail as Completer Finisher care rather than nit-picking, the emotional charge
drains out of everyday difference. This is precisely the shift a skilled mediator creates in
the room — Belbin sustains it long after the session ends.</p>

<h3>4. Manager training</h3>
<p>We equip managers and team leaders to apply Belbin principles in ongoing practice: designing
balanced teams, allocating work to strengths, structuring meetings so every necessary perspective
is heard, and recognising role-based friction before it escalates into a formal complaint.</p>

<h3>5. Integration with dispute resolution</h3>
<p>Where a team has already experienced conflict, Belbin training pairs naturally with our
<a href="/workplace-mediation/">workplace mediation</a> service — closing the loop from
resolution back to prevention. For teams emerging from a dispute, it is often the most
important next step.</p>

<h2>The logical pathway: resolve, diagnose, prevent</h2>
<p>Mediations Australia sees conflict resolution and conflict prevention as two ends of the
same pathway.</p>
<ul>
  <li><strong>Stage 1 — Reactive:</strong> a dispute has already happened. <a href="/workplace-mediation/">Workplace mediation</a> resolves it fast and privately.</li>
  <li><strong>Stage 2 — Diagnostic:</strong> mediation often exposes a deeper pattern — overlapping responsibilities, imbalanced teams, unclear decision-making.</li>
  <li><strong>Stage 3 — Proactive:</strong> Belbin training designs the problem out before it recurs.</li>
</ul>
<p>Belbin training lets an organisation start at Stage 3 — before a single grievance is ever lodged.</p>

<h2>Who benefits</h2>
<ul>
  <li><strong>Leadership teams</strong> wanting to understand why decisions stall or why the same tensions recur</li>
  <li><strong>Newly formed or restructured teams</strong> where a previously balanced group has lost its mix</li>
  <li><strong>Fast-growing organisations</strong> adding people quickly and unintentionally stacking the same roles</li>
  <li><strong>HR and people-and-culture teams</strong> meeting psychosocial hazard obligations under WHS law</li>
  <li><strong>Teams emerging from a dispute</strong> who want to make sure it does not happen again</li>
</ul>
"""

schema = [
    org_schema(),
    breadcrumb_schema([("Home", ""), (crumb, slug)]),
    service_schema(crumb, desc, slug),
    faq_schema(qa),
]
BELBIN_FORM_FIELDS = """
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;opacity:0" aria-hidden="true">
    <input type="hidden" name="_subject" value="Belbin Team Roles Training Enquiry — Mediations Australia">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
      <div class="form-row">
        <label for="b-name">Your name</label>
        <input id="b-name" name="name" type="text" required autocomplete="name" placeholder="Full name" class="belbin-field">
      </div>
      <div class="form-row">
        <label for="b-org">Organisation</label>
        <input id="b-org" name="organisation" type="text" required placeholder="Company or team name" class="belbin-field">
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
      <div class="form-row">
        <label for="b-email">Email</label>
        <input id="b-email" name="email" type="email" required autocomplete="email" placeholder="you@company.com" class="belbin-field">
      </div>
      <div class="form-row">
        <label for="b-phone">Phone</label>
        <input id="b-phone" name="phone" type="tel" autocomplete="tel" placeholder="0400 000 000" class="belbin-field">
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
      <div class="form-row">
        <label for="b-size">Number of people</label>
        <select id="b-size" name="team_size" required class="belbin-field">
          <option value="" disabled selected>Select…</option>
          <option value="1–5">1–5</option>
          <option value="6–10">6–10</option>
          <option value="11–20">11–20</option>
          <option value="21–50">21–50</option>
          <option value="50+">50+</option>
        </select>
      </div>
      <div class="form-row">
        <label for="b-delivery">Preferred delivery</label>
        <select id="b-delivery" name="delivery" required class="belbin-field">
          <option value="" disabled selected>Select…</option>
          <option value="In person">In person</option>
          <option value="Online">Online</option>
          <option value="Either">Either works</option>
        </select>
      </div>
    </div>
    <div class="form-row">
      <label for="b-context">What's prompting this? (optional)</label>
      <textarea id="b-context" name="context" rows="3" placeholder="e.g. recurring conflict, a restructure, building a new leadership group…" class="belbin-field"></textarea>
    </div>
    <button type="submit" id="belbin-submit" class="btn btn-primary" style="width:100%;justify-content:center;font-size:1rem;padding:15px 20px">Send Enquiry <span class="arr">→</span></button>
    <p style="font-size:.82rem;color:var(--ink-soft);margin:0">No obligation. We'll respond within one business day.</p>
"""

BELBIN_SCRIPT = """
<script>
document.getElementById('belbin-form').addEventListener('submit',async function(e){
  e.preventDefault();
  var btn=document.getElementById('belbin-submit');
  btn.disabled=true;btn.textContent='Sending…';
  var data=new FormData(this);
  try{
    var r=await fetch('https://formspree.io/f/xwvgjnve',{method:'POST',body:data,headers:{Accept:'application/json'}});
    if(r.ok){window.location.href='/thank-you/';}
    else{btn.disabled=false;btn.innerHTML='Send Enquiry <span class="arr">→</span>';alert('Something went wrong. Please try again or call us directly.');}
  }catch(err){btn.disabled=false;btn.innerHTML='Send Enquiry <span class="arr">→</span>';alert('Something went wrong. Please try again or call us directly.');}
});
</script>
"""

d = head(title, desc, slug, extra_schema=schema) + nav()
d += f"""<main id="main">
{crumb_html([("Home", ""), (crumb, None)])}
<style>
.belbin-hero{{display:grid;grid-template-columns:1fr 480px;gap:64px;align-items:start;padding:72px 0 80px}}
.belbin-field{{width:100%;padding:13px 16px;border:1.5px solid var(--line);border-radius:10px;font-size:1rem;background:var(--cream);color:var(--ink);font-family:var(--sans);box-sizing:border-box;outline:none;transition:border-color .2s}}
.belbin-field:focus{{border-color:var(--sage-deep)}}
.belbin-form-card{{background:var(--cream);border:1.5px solid var(--line);border-radius:16px;padding:32px;box-shadow:0 4px 24px rgba(0,0,0,.07)}}
@media(max-width:900px){{.belbin-hero{{grid-template-columns:1fr;gap:40px;padding:48px 0 56px}}.belbin-form-card{{padding:24px}}}}
@media(max-width:600px){{.belbin-hero [style*="grid-template-columns:1fr 1fr"]{{grid-template-columns:1fr!important}}}}
</style>
<section style="background:var(--sand)">
<div class="wrap">
<div class="belbin-hero">
  <div>
    <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
    <h1 style="margin-top:16px">{h1}</h1>
    <p class="lede" style="margin-bottom:32px">{lede}</p>
    <div class="answer" style="margin:0"><p><strong>In short:</strong> {ans}</p></div>
    <div style="margin-top:32px;display:flex;flex-direction:column;gap:10px;font-size:.92rem;color:var(--ink-soft)">
      <span>&#10003; Accredited Belbin Team Roles Facilitator</span>
      <span>&#10003; In person or online, Australia-wide</span>
      <span>&#10003; Tailored to your team — no obligation</span>
    </div>
  </div>
  <div>
    <div class="belbin-form-card">
      <p style="font-weight:700;font-size:1.05rem;margin:0 0 4px">Enquire about Belbin training</p>
      <p style="font-size:.88rem;color:var(--ink-soft);margin:0 0 20px">Tell us about your team and we'll send a tailored proposal.</p>
      <form id="belbin-form" novalidate style="display:flex;flex-direction:column;gap:12px">
        {BELBIN_FORM_FIELDS}
      </form>
    </div>
    <a href="{PHONE_HREF}" style="display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-weight:600;font-size:.95rem;margin-top:16px">
      <span style="width:36px;height:36px;border-radius:50%;background:var(--sage-light);display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--sage-deep)">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M6.6 10.8a15.2 15.2 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      Or call {PHONE}
    </a>
  </div>
</div>
</div>
</section>
<article class="body"><div class="wrap-narrow reveal">{blocks}</div></article>"""
d += faq_html(qa, heading=f"{crumb} FAQs")
d += cta_band(
    "Ready to build a stronger team?",
    "Book a free conversation with Dan Toombs — Accredited Belbin Facilitator and Nationally Accredited Mediator."
)
d += BELBIN_SCRIPT
d += "</main>" + page_end()

p = os.path.join(OUT, slug)
os.makedirs(p, exist_ok=True)
open(os.path.join(p, "index.html"), "w").write(d)
print(f"Built: /{slug}/")
