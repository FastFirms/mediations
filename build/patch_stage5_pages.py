#!/usr/bin/env python3
"""SEO recovery stage 5 (brief §5.2, §5.5): strengthen two hand-maintained workplace pages in place.

/conflict-resolution-in-the-workplace/ and /ngo-not-for-profit-mediation/ have no live generator, so the
built HTML is the source of truth. Idempotent (marker comment). Workplace prices come only from
workplace_pricing. Dan's details use only the source-checked wording in brief §5.6.
DRAFT — legal/editorial review before publication.
"""
import os, re, json, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from workplace_pricing import price_block, faq_answers

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
MARK = "<!-- seo-recovery-stage5 -->"
WFAQ = faq_answers()

DAN_CARD = ('<div style="display:flex;gap:1.25rem;align-items:flex-start;flex-wrap:wrap;padding:1.25rem;border:1px solid var(--line);'
            'border-radius:12px;background:var(--cream);margin:1rem 0">'
            '<img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder and Mediator, Mediations Australia" width="88" height="88" '
            'loading="lazy" style="border-radius:50%;object-fit:cover;width:88px;height:88px;flex-shrink:0">'
            '<div style="flex:1;min-width:220px"><p style="margin:0 0 .5rem">Dan Toombs is an <strong>AMDRAS-accredited mediator</strong>. '
            'He has led a community legal centre as <strong>CEO</strong> and served as a <strong>Board Director of Legal Aid Queensland</strong>, '
            'and is a former <strong>Member of the Guardianship and Administration Tribunal (Queensland)</strong>, whose jurisdiction is now within QCAT. '
            'Dan has mediated workplace disputes across professional services, healthcare, education, construction, and the not-for-profit sector.</p>'
            '<p style="margin:0"><a href="/our-team/dan-toombs/">View Dan\'s profile →</a> Who mediates a matter depends on suitability and availability.</p></div></div>')


def load(slug):
    p = os.path.join(ROOT, slug, "index.html")
    return p, open(p, encoding="utf-8").read()


def set_meta(h, title=None, desc=None):
    if desc:
        h = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*(")',
                   lambda m: m.group(1) + desc + m.group(2), h)
    if title:
        h = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', h)
        h = re.sub(r'(<meta (?:property|name)="(?:og:title|twitter:title)" content=")[^"]*(")',
                   lambda m: m.group(1) + title + m.group(2), h)
    return h


def finish(p, h):
    h = re.sub(r'"dateModified": "[^"]*"', f'"dateModified": "{TODAY}"', h)
    h = h.replace("</body>", MARK + "\n</body>", 1)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        json.loads(b)
    open(p, "w", encoding="utf-8").write(h)


def must(h, old, new, count=1):
    assert h.count(old) >= 1, old[:80]
    return h.replace(old, new) if count == 0 else h.replace(old, new, count)


# ─────────────────────────────────────────────────────────────────────────────
# §5.2 Workplace conflict resolution
# ─────────────────────────────────────────────────────────────────────────────
def conflict():
    slug = "conflict-resolution-in-the-workplace"
    p, h = load(slug)
    if MARK in h:
        print(slug, "already patched"); return
    h = set_meta(h, title="Workplace Conflict Resolution: Practical Australian Guide",
                 desc="Learn how to identify workplace conflict, use practical early-resolution steps and recognise when independent mediation or a formal process is needed.")
    h = re.sub(r'<h1([^>]*)>.*?</h1>', r'<h1\1>Workplace conflict resolution: practical steps and mediation</h1>', h, count=1, flags=re.S)
    h = must(h, "<p>Workplace conflict is costing Australian businesses between $6 and $12 billion every year. Managers are spending roughly 30 per cent of their time dealing with disputes instead of driving productivity, and half of all Australian workers report experiencing at least one serious incident of workplace conflict.</p>",
             "<p>Workplace conflict resolution starts by identifying the issue, the people affected and whether it is safe and appropriate to address it informally. Clear roles, respectful discussion and agreed next steps can help. Where people cannot work through the dispute themselves, independent mediation may assist; serious allegations or safety concerns may require a different response first.</p>")
    h = must(h, "<li><strong>Billions in lost productivity:</strong> Workplace conflict is estimated to cost the Australian economy between $6 and $12 billion annually through lost productivity, absenteeism, and staff turnover.</li>",
             "<li><strong>Lost productivity:</strong> unresolved conflict can contribute to absence, disengagement and staff turnover.</li>")
    h = h.replace("there are clear, proven pathways to resolution", "there are practical pathways to resolution")
    h = h.replace("8 Proven Conflict Resolution Strategies for Australian Workplaces", "Eight practical conflict resolution strategies")
    h = must(h, '<p>The cost of workplace mediation varies depending on the complexity of the dispute, the number of parties involved, and the duration of the session. However, mediation is consistently a fraction of the cost of formal legal proceedings. For detailed information on pricing, visit our <a href="/costs-of-mediation/">costs of mediation</a> page.</p>',
             f'<p>{WFAQ["cost"]} See <a href="/workplace-mediation-cost/">workplace mediation cost</a>.</p>')
    inserts = [
        ("8-proven-conflict-resolution-strategies-for-austra", "triage", "Triage: work out what kind of problem you have", """
<p>Before trying to resolve a conflict, take a few minutes to work out what you are dealing with. The right response depends on the answers.</p>
<table>
<thead><tr><th>Question</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Is anyone unsafe?</td><td>Threats, violence, sexual harassment or serious bullying need a safety response and may trigger legal obligations. Do not start with an informal chat.</td></tr>
<tr><td>Are rights or deadlines involved?</td><td>Some claims have short time limits (unfair dismissal applications, for example, must be made within 21 days). Get advice promptly.</td></tr>
<tr><td>Is it about facts or the relationship?</td><td>Disputed allegations may need an investigation to establish facts. Relationship and working-style problems are usually better suited to conversation or mediation.</td></tr>
<tr><td>Can the people involved talk safely?</td><td>If not, a structured process with a neutral third party may be needed.</td></tr>
</tbody>
</table>
"""),
        ("when-to-use-mediation-for-workplace-conflict", "staged-conversation", "A practical staged conversation", """
<p>For everyday disagreements that are safe to address directly, a simple structure helps:</p>
<ol>
<li><strong>Prepare.</strong> Note specific events and their effect. Choose a private time and place.</li>
<li><strong>Listen first.</strong> Ask for the other person's view and summarise it back before giving yours.</li>
<li><strong>Name the issue.</strong> Describe behaviour and impact, not character (&#8220;the handover notes were missing twice this week&#8221;, not &#8220;you're careless&#8221;).</li>
<li><strong>Explore options.</strong> Generate a few practical options together before choosing.</li>
<li><strong>Agree actions.</strong> Write down who will do what, by when.</li>
<li><strong>Review.</strong> Set a date to check whether it is working.</li>
</ol>
<h3>Example: manager and employee (fictional)</h3>
<p>A team member feels their workload is unfair; their manager feels deadlines are being missed. Using the steps above, they agree a weekly ten-minute priorities check and a clear process for flagging overload early, and review it after a month.</p>
<h3>Example: two co-workers (fictional)</h3>
<p>Two colleagues who share a role keep redoing each other's work. They map who owns which tasks, agree a handover note format, and ask their manager to confirm the split.</p>
<h3>Manager preparation checklist</h3>
<ul>
<li>Have I checked for safety concerns or legal obligations?</li>
<li>Do I know whether a formal complaint has been made, and what our policy requires?</li>
<li>Have I written down specific, observable examples?</li>
<li>Have I planned a private, unhurried time to talk?</li>
<li>Do I know what support (EAP, HR, external mediation) is available if this does not work?</li>
</ul>
"""),
        ("mediation-vs-litigation-why-mediation-is-the-smart", "choose-process", "Choosing mediation, investigation or formal advice", """
<table>
<thead><tr><th>Situation</th><th>Usually start with</th></tr></thead>
<tbody>
<tr><td>Working-relationship breakdown, both willing to talk</td><td><a href="/workplace-mediation/">Workplace mediation</a></td></tr>
<tr><td>Serious allegations that need findings of fact</td><td>An <a href="/workplace-investigations-grievance-mediation/">investigation</a>, then possibly mediation to rebuild relationships</td></tr>
<tr><td>Safety risk, violence or sexual harassment</td><td>Immediate safety steps and specialist or legal advice</td></tr>
<tr><td>Possible legal claim or deadline</td><td>Legal advice straight away</td></tr>
<tr><td>A whole team in conflict</td><td><a href="/team-conflict-facilitation/">Team conflict facilitation</a></td></tr>
</tbody>
</table>
<p>Not sure? Our <a href="/is-mediation-right-for-workplace-dispute/">suitability guide</a> walks through the questions. Mediation can help many disputes, but it is not a guaranteed outcome and it does not replace an investigation or legal obligations.</p>
"""),
    ]
    for before_id, new_id, label, html in inserts:
        anchor = f'<h2 id="{before_id}"'
        assert h.count(anchor) == 1, before_id
        h = h.replace(anchor, f'<h2 id="{new_id}">{label}</h2>\n{html}\n' + anchor)
        h = h.replace(f'<li><a href="#{before_id}">', f'<li><a href="#{new_id}">{label}</a></li><li><a href="#{before_id}">')
    faq_id, end_id = "frequently-asked-questions-conflict-resolution-in-", "take-the-first-step-toward-resolution"
    extra = [
        ("How do you resolve conflict at work?", "Start by checking safety and any deadlines, then work out whether the issue is about facts or the working relationship. For relationship issues, a private, structured conversation with agreed actions and a review date often helps. If that fails, consider mediation."),
        ("What if an informal discussion fails?", "Escalate deliberately rather than letting it drift. Options include involving HR, using your organisation's grievance procedure, or engaging an independent mediator. If serious allegations are involved, an investigation may be needed first."),
        ("Is a grievance the same as mediation?", "No. A grievance procedure is an internal process for raising and responding to a complaint, which may lead to an investigation and findings. Mediation is voluntary and helps the people involved reach their own agreement; it does not make findings."),
        ("Can mediation replace an investigation?", "No. Where serious allegations need findings of fact, or there are safety or legal obligations, an investigation or other formal process usually comes first. Mediation can help rebuild working relationships afterwards."),
    ]
    end = f'<h2 id="{end_id}"'
    h = h.replace(end, "".join(f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in extra) + end, 1)
    a = h.index(f'<h2 id="{faq_id}"'); b = h.index(end, a)
    clean = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).replace('&amp;', '&').replace('&#8217;', '’').strip()
    pairs = [(clean(q), clean(x)) for q, x in re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>', h[a:b], re.S)]
    schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": x}} for q, x in pairs]}
    h = h.replace("</head>", f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n</head>', 1)
    finish(p, h); print(slug, "patched,", len(pairs), "FAQs")


# ─────────────────────────────────────────────────────────────────────────────
# §5.5 NGO / not-for-profit
# ─────────────────────────────────────────────────────────────────────────────
def ngo():
    slug = "ngo-not-for-profit-mediation"
    p, h = load(slug)
    if MARK in h:
        print(slug, "already patched"); return
    h = set_meta(h, title="Workplace Mediation for NGOs &amp; Not-for-Profits",
                 desc="Independent mediation for NGO and charity workplace disputes, including leadership conflict, grievances and repairing working relationships after investigation.")
    h = h.replace("<h1>Workplace mediation for <em>NGOs and not-for-profits</em>.</h1>", "<h1>Workplace mediation for <em>NGOs and not-for-profits</em></h1>")
    old_online = "Online mediation is equally effective for most workplace disputes."
    new_online = "Many workplace mediations can be conducted online; whether online suits a particular dispute is assessed at intake."
    h = must(h, old_online, new_online, count=0)
    sections = f"""
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

<h2 id="ngo-fees">Fees</h2>
{price_block()}
<p>See <a href="/workplace-mediation-cost/">workplace mediation cost</a> for examples with additional parties. Team-wide work is quoted on request; see <a href="/team-conflict-facilitation/">team conflict facilitation</a>.</p>
"""
    anchor = '<h2 id="our-mediators">'
    h = must(h, anchor, sections + anchor)
    h = must(h, '<h2 id="our-mediators">Experienced Australian workplace mediators</h2>',
             '<h2 id="our-mediators">Experienced Australian workplace mediators</h2>\n' + DAN_CARD)
    extra = [
        ("Who authorises an NGO mediation?", "Usually the HR lead, CEO or board. Where the CEO or a board member is a party, the board chair or a delegated committee normally commissions the mediation so that the process is not controlled by someone involved in the dispute."),
        ("Can mediation help a conflict between the CEO and the board?", "It can, where both are willing and there are no safety or governance issues that need a different process first. Commissioning is usually delegated to a committee, and the focus is often on roles and decision-making protocols."),
        ("Should we investigate first?", "Where serious allegations need findings of fact, or there are safety or legal obligations, an investigation usually comes first. Mediation can help rebuild working relationships after it concludes."),
        ("Who receives the outcome of the mediation?", "Only what is agreed in writing before intake. Often that is whether mediation went ahead and any agreed actions the participants consent to share with the organisation."),
    ]
    det = "".join(f'<details class="faq"><summary>{q}<span class="ico">+</span></summary><div class="ans"><p>{a}</p></div></details>' for q, a in extra)
    i = h.index('<div class="faq-wrap reveal">'); j = h.rindex('</details>', i, h.index('</section>', i)) + len('</details>')
    h = h[:j] + det + h[j:]

    def add_schema(m):
        j = json.loads(m.group(1))
        nodes = j.get("@graph", [j]) if isinstance(j, dict) else j
        for n in nodes:
            if isinstance(n, dict) and n.get("@type") == "FAQPage":
                for q in n["mainEntity"]:
                    q["acceptedAnswer"]["text"] = q["acceptedAnswer"]["text"].replace(old_online, new_online)
                n["mainEntity"] += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in extra]
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, indent=2) + '</script>'
    h = re.sub(r'<script type="application/ld\+json">(.*?"FAQPage".*?)</script>', add_schema, h, count=1, flags=re.S)
    finish(p, h); print(slug, "patched")


conflict()
ngo()
