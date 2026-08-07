#!/usr/bin/env python3
"""Generates /our-team/ index + individual bio pages for Dan Toombs, Farley Tolpen, and Prav Singh-Pillay."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html,
                       org_schema, breadcrumb_schema,
                       DOMAIN, BOOK_URL, PHONE, PHONE_HREF)

OUT = os.path.join(os.path.dirname(__file__), "..")

PAGE_CSS = """<style>
.mediator-hero{padding:60px 0 0;background:var(--sand)}
.mediator-profile{display:grid;grid-template-columns:260px 1fr;gap:48px;align-items:start;padding:48px 0 56px}
.mediator-photo{position:sticky;top:100px}
@media(max-width:720px){.mediator-profile{display:block!important}.mediator-photo{position:static!important;width:100%!important;margin-bottom:32px}.mediator-photo img{width:100%!important;height:280px}.mediator-content{width:100%!important}}
.mediator-photo img{width:100%;height:320px;object-fit:cover;object-position:top;border-radius:16px;display:block;box-shadow:0 8px 32px rgba(0,0,0,.10)}
.cred-table{margin-top:24px;width:100%;border-collapse:collapse;font-size:.85rem}
.cred-table td{padding:7px 0;border-bottom:1px solid var(--sand-deep);vertical-align:top;color:var(--ink-soft)}
.cred-table td:first-child{font-weight:600;color:var(--ink);padding-right:12px;white-space:nowrap}
.mediator-content h2{font-family:var(--serif);font-size:clamp(1.5rem,3vw,2rem);margin:36px 0 12px}
.mediator-content h2:first-child{margin-top:0}
.mediator-content h3{font-size:1.15rem;font-weight:600;margin:28px 0 8px;color:var(--sage-deep)}
.mediator-content p{font-size:1.06rem;color:var(--ink-soft);line-height:1.75;margin-bottom:18px;max-width:68ch}
.mediator-content ul{font-size:1.05rem;color:var(--ink-soft);line-height:1.8;padding-left:1.4em;margin-bottom:18px;max-width:68ch}
.mediator-content .tag-line{font-family:var(--serif);font-size:1.2rem;font-style:italic;color:var(--sage-deep);margin-bottom:32px;display:block}
.mediator-content a{color:var(--sage-deep)}
.booking-strip{background:var(--sage-deep);color:var(--cream);padding:48px 0;text-align:center;margin-top:24px}
.booking-strip h2{font-family:var(--serif);font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:12px}
.booking-strip p{font-size:1.05rem;opacity:.88;max-width:54ch;margin:0 auto 28px}
.team-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:32px;padding:56px 0}
.team-card{background:var(--sand);border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;display:block;transition:box-shadow .2s}
.team-card:hover{box-shadow:0 8px 32px rgba(0,0,0,.12)}
.team-card-photo{height:260px;background-repeat:no-repeat;background-color:var(--sand-deep)}
.team-card-body{padding:24px}
.team-card-name{font-family:var(--serif);font-size:1.3rem;margin-bottom:4px}
.team-card-role{color:var(--sage-deep);font-weight:600;font-size:.92rem;margin-bottom:10px}
.team-card-bio{font-size:.95rem;color:var(--ink-soft);line-height:1.65;margin-bottom:16px}
.team-card-link{font-size:.9rem;font-weight:600;color:var(--terra)}
</style>"""

# ============================================================
# /our-team/ INDEX PAGE
# ============================================================

idx_schema = [org_schema(), breadcrumb_schema([("Home",""),("Our Team","our-team")])]
d = head("Our Team | Mediations Australia",
         "Meet our nationally accredited mediators and lawyers — experienced across family law, property, commercial and workplace disputes. Based across Australia.",
         "our-team", extra_schema=idx_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our team",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:64ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Our Team — <em>accredited, experienced, lawyer-aware</em>
      </h1>
      <p style="font-size:1.1rem;color:var(--ink-soft);max-width:58ch">Our team brings together nationally accredited mediators and experienced family lawyers. Whether you need mediation, legal advice, or both, we have the expertise to help.</p>
    </div>
  </div>
</section>

<section style="background:var(--cream)">
  <div class="wrap">
    <div class="team-grid">

      <a href="/our-team/dan-toombs/" class="team-card">
        <div class="team-card-photo" role="img" aria-label="Dan Toombs — Founder, Lawyer and Mediator" style="background-image:url('/assets/images/Dan-Bio.png');background-size:cover;background-position:center top"></div>
        <div class="team-card-body">
          <p class="team-card-name">Dan Toombs</p>
          <p class="team-card-role">Founder, Lawyer &amp; Mediator</p>
          <p class="team-card-bio">AMDRAS-accredited mediator, multi-award winning lawyer, and published author. Founder of Mediations Australia, National Human Rights Law Award recipient, and Winston Churchill Fellow.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

      <a href="/our-team/farley-tolpen/" class="team-card">
        <div class="team-card-photo" role="img" aria-label="Farley Tolpen — Accredited Mediator and Lawyer" style="background-image:url('/assets/images/Farley-Bio.png');background-size:cover;background-position:center top"></div>
        <div class="team-card-body">
          <p class="team-card-name">Farley Tolpen</p>
          <p class="team-card-role">Accredited Mediator &amp; Lawyer</p>
          <p class="team-card-bio">40+ years of mediation, arbitration and litigation experience across Australia and the United States. Nationally Accredited Mediator (AMDRAS), FDRP, and Family Law Arbitrator. Approximate 4,500+ matters with around a 90% resolution rate.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

      <a href="/our-team/prav-singh-pillay/" class="team-card">
        <div class="team-card-photo" role="img" aria-label="Prav Singh-Pillay — Lawyer and Accredited Mediator" style="background-image:url('/assets/images/Prav-Bio.png');background-size:cover;background-position:center top"></div>
        <div class="team-card-body">
          <p class="team-card-name">Prav Singh-Pillay</p>
          <p class="team-card-role">Lawyer &amp; Accredited Mediator</p>
          <p class="team-card-bio">Family lawyer and accredited mediator with 25+ years of experience across family law, civil litigation, wills and estates. Authorised to issue Section 60I certificates as a registered FDRP.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

    </div>
  </div>
</section>
</main>"""

d += page_end()

out_path = os.path.join(OUT, "our-team")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-team index built")

# ============================================================
# /our-team/dan-toombs/
# ============================================================

dan_schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Our Team","our-team"),("Dan Toombs","our-team/dan-toombs")]),
    {
        "@type": "Person",
        "name": "Dan Toombs",
        "jobTitle": "Founder & Mediator",
        "url": f"{DOMAIN}/our-team/dan-toombs/",
        "image": f"{DOMAIN}/assets/images/Dan-Bio.png",
        "worksFor": {"@id": f"{DOMAIN}/#organization"},
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "name": "AMDRAS Accredited Mediator",
             "credentialCategory": "Professional Accreditation",
             "recognizedBy": {"@type": "Organization", "name": "AMDRAS", "url": "https://amdras.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Winston Churchill Fellowship",
             "credentialCategory": "Fellowship",
             "recognizedBy": {"@type": "Organization", "name": "Churchill Trust Australia", "url": "https://www.churchilltrust.com.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "National Human Rights Law Award",
             "credentialCategory": "Award",
             "recognizedBy": {"@type": "Organization", "name": "Australian Human Rights Commission", "url": "https://humanrights.gov.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Accredited Belbin Team Roles Facilitator",
             "credentialCategory": "Professional Accreditation",
             "recognizedBy": {"@type": "Organization", "name": "Belbin", "url": "https://www.belbin.com/"}},
        ],
        "sameAs": ["https://amdras.au/", "https://www.churchilltrust.com.au/", "https://humanrights.gov.au/"],
    }
]

d = head("Dan Toombs — Founder & Mediator | Mediations Australia",
         "Meet Dan Toombs — Founder of Mediations Australia, AMDRAS-accredited mediator, Winston Churchill Fellow and Human Rights Law Award recipient.",
         "our-team/dan-toombs", extra_schema=dan_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our team","/our-team/"),("Dan Toombs",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:60ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Dan Toombs — <em>Accredited AMDRAS Mediator &amp; Founder</em>
      </h1>
    </div>
  </div>
</section>

<section style="background:var(--cream);padding-bottom:24px">
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/Dan-Bio.png"
             alt="Dan Toombs — Founder and Mediator, Mediations Australia"
             width="260" height="320" loading="eager">
        <table class="cred-table" aria-label="Dan Toombs credentials">
          <tbody>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:12px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Mediation</td></tr>
            <tr><td>Accreditation</td><td><a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS</a> Accredited Mediator</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:12px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Legal</td></tr>
            <tr><td>Lawyer</td><td>Multi-Award-Winning Lawyer</td></tr>
            <tr><td>Publisher</td><td><a href="https://www.thomsonreuters.com.au/en-au.html" target="_blank" rel="noopener">Thomson Reuters</a> — Published Author</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:12px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Leadership &amp; Governance</td></tr>
            <tr><td>Former CEO</td><td>Community Legal Centre</td></tr>
            <tr><td>Former Board</td><td><a href="https://www.legalaid.qld.gov.au/" target="_blank" rel="noopener">Legal Aid Queensland</a></td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:12px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">National Recognition</td></tr>
            <tr><td>Award</td><td><a href="https://humanrights.gov.au/about-us/what-we-do/human-rights-awards-2026" target="_blank" rel="noopener">National Human Rights Law Award</a></td></tr>
            <tr><td>Award</td><td>Queensland Disability Award</td></tr>
            <tr><td>Award</td><td>Australia Leadership Award</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:12px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Behaviour &amp; Leadership</td></tr>
            <tr><td>Accreditation</td><td><a href="https://www.belbin.com/" target="_blank" rel="noopener">Belbin</a> Team Roles Facilitator</td></tr>
            <tr><td>Training</td><td><a href="https://aali.org.au/" target="_blank" rel="noopener">Adaptive Leadership</a> (Harvard framework)</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:12px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">International Experience</td></tr>
            <tr><td>Fellowship</td><td><a href="https://www.churchilltrust.com.au/" target="_blank" rel="noopener">Winston Churchill Fellow</a></td></tr>
            <tr><td>Fellow</td><td><a href="https://www.innovatingjustice.org/" target="_blank" rel="noopener">Center for Justice Innovation</a>, New York</td></tr>
          </tbody>
        </table>

      </aside>

      <div class="mediator-content">
        <h2>Dan Toombs — Founder, Mediations Australia</h2>
        <span class="tag-line">Award-winning lawyer. Nationally accredited mediator. Published author.</span>

        <p>Dan Toombs is the Founder of Mediations Australia and an <a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS-accredited mediator</a>
        who brings an unusual combination of legal expertise, commercial judgment, organisational leadership
        and understanding of human behaviour to the mediation room.</p>

        <p>Throughout his career, Dan has worked in complex situations where law, organisations, relationships
        and human behaviour intersect. His work has required him to understand competing perspectives,
        navigate entrenched positions, build relationships across organisations and find practical ways
        forward when the solution is not obvious. That experience shapes his approach to mediation.</p>

        <p>For Dan, resolving a dispute is rarely just about determining who is right or wrong. It is about
        understanding what is really driving the conflict, what is preventing progress, where interests may
        overlap, and what needs to happen for the parties to reach an outcome that is practical, workable
        and capable of lasting beyond the mediation itself.</p>

        <h3>Navigating Complexity and Finding a Way Forward</h3>
        <p>Dan is a multi-award-winning lawyer published by
        <a href="https://www.thomsonreuters.com.au/en-au.html" target="_blank" rel="noopener">Thomson Reuters</a>,
        one of the world's leading legal publishers. His legal career has included complex disputes,
        legislative reform, access to justice and organisational leadership — much of it in environments
        where progress depended not simply on understanding the law, but on navigating complex legislative
        and policy frameworks, reconciling competing interests and building relationships across institutions.</p>

        <p>This included helping drive significant legislative reform in Australia that improved outcomes
        for people with mental health and intellectual disabilities caught in the criminal justice system
        — work recognised with the <strong>Queensland Disability Award</strong>. Achieving systemic change
        of this kind requires understanding a problem from multiple perspectives, identifying where progress
        is being blocked, and bringing people and institutions towards an outcome capable of producing
        meaningful and enduring change. Those same skills are central to Dan's work as a mediator.</p>

        <h3>Understanding What Sits Beneath a Conflict</h3>
        <p>Disputes are rarely driven by legal issues alone. People may feel unheard or misunderstood.
        Trust can deteriorate. Communication can become defensive. Workplace relationships can fracture.
        Commercial pressures can harden positions. Sometimes the way people have responded to a dispute
        becomes as significant as the issue that caused it in the first place.</p>

        <p>Dan has undertaken specialist training in behaviour, leadership and team dynamics to deepen
        his understanding of these forces. He is an
        <a href="https://www.belbin.com/" target="_blank" rel="noopener">Accredited Belbin Team Roles Facilitator</a>
        — a globally recognised behavioural framework used to understand working relationships,
        communication and team dynamics. He has also trained in
        <a href="https://aali.org.au/" target="_blank" rel="noopener">Adaptive Leadership</a> through the
        Australian Adaptive Leadership Institute, based on the framework developed at Harvard University
        for navigating complex challenges where there is no simple technical solution.</p>

        <p>Dan looks beyond the positions people bring into the mediation room to understand the interests,
        relationships, communication patterns and pressures sitting underneath them — uncovering
        opportunities for resolution that may be difficult to see while the parties remain locked in conflict.</p>

        <h3>Commercial Judgment When the Stakes Are High</h3>
        <p>Dan's experience extends well beyond legal practice. He served as CEO of one of Australia's
        largest community legal centres and as a Board Director of
        <a href="https://www.legalaid.qld.gov.au/" target="_blank" rel="noopener">Legal Aid Queensland</a>.
        As a CEO and organisational leader, Dan has had responsibility for people, strategy, governance,
        competing priorities and difficult decisions. He understands that organisations operate within
        commercial and practical realities — and that a theoretically perfect solution is of little value
        if it cannot work in practice.</p>

        <p>That perspective is particularly important in business and <a href="/workplace-mediation/">workplace mediation</a>,
        where a dispute may have consequences far beyond the immediate disagreement — affecting employees,
        leadership teams, customers, productivity, reputation, finances and important commercial relationships.
        Dan brings that wider perspective to the mediation process, helping parties consider not only the
        dispute in front of them, but also the practical consequences of continuing it and what a workable
        resolution needs to achieve.</p>

        <h3>Connected to the Realities of Professional Practice</h3>
        <p>Alongside his mediation work, Dan is Director of
        <a href="https://www.practiceproof.com/" target="_blank" rel="noopener">Practice Proof</a>,
        where he works with law firms and legal professionals across Australia. That work keeps him
        closely connected to the realities facing professional organisations — leadership, people,
        performance, commercial pressures, changing expectations and the challenges that can arise
        when relationships and organisational objectives do not align.</p>

        <p>Combined with his previous experience as a CEO and Board Director, it gives Dan a perspective
        on workplace and <a href="/commercial-mediation/">commercial conflict</a> that extends beyond legal
        theory. He understands the organisational environment in which disputes arise — and, importantly,
        the environment the parties often need to return to once the mediation is over.</p>

        <h3>National and International Recognition</h3>
        <p>Dan's work has been recognised nationally and internationally. He is the recipient of the
        <a href="https://humanrights.gov.au/about-us/what-we-do/human-rights-awards-2026" target="_blank" rel="noopener">National Human Rights Law Award</a>
        — one of Australia's most prestigious recognitions of leadership in advancing human rights
        through law.</p>

        <p>He is also a <a href="https://www.churchilltrust.com.au/" target="_blank" rel="noopener">Winston Churchill Fellow</a>
        and undertook pioneering work with the
        <a href="https://www.innovatingjustice.org/" target="_blank" rel="noopener">Center for Justice Innovation</a>
        in New York — an internationally recognised institution focused on developing practical
        responses to complex problems across justice, health and community safety. Across this work
        runs a consistent theme: understanding difficult systems and difficult problems, bringing
        together different perspectives, and finding better ways forward.</p>

        <h3>A Leader in Access to Justice</h3>
        <p>Dan's commitment to mediation is grounded in a broader belief about how people should be
        able to resolve disputes. Throughout his career, he has worked to improve access to justice
        — as a lawyer, CEO, Legal Aid Queensland Board Director and through his work in legislative
        and systemic reform. That experience has given him a first-hand understanding of both the
        importance of the legal system and its limitations.</p>

        <p>Litigation will sometimes be necessary. But where a dispute can be resolved without handing
        the decision to a court, mediation can give people something litigation often cannot: the
        opportunity to retain control over the outcome. That philosophy sits behind Mediations Australia
        — where we believe high-quality mediation should be accessible, transparent and focused on
        helping people resolve disputes as efficiently and constructively as the circumstances allow.</p>

        <h3>What This Means for You</h3>
        <p>You may be a business dealing with a <a href="/workplace-mediation/">workplace conflict</a> that
        is beginning to affect a team or organisation. You may be facing a
        <a href="/commercial-mediation/">commercial disagreement</a> in which relationships, money and
        legal issues have become intertwined. You may be dealing with a partnership, contractual or
        organisational dispute that has become increasingly difficult to resolve directly.</p>

        <p>The circumstances will be different, but the challenge is often similar: something is keeping
        the dispute stuck. Dan approaches mediation by working to understand what that is — bringing
        legal expertise where the issues are complex, commercial judgment where practical consequences
        matter, and an understanding of relationships and human behaviour where the conflict goes deeper
        than the positions being argued.</p>

        <p>Mediation cannot guarantee agreement. But with the right process, it can create the conditions
        for people to move beyond entrenched positions, have conversations that have become difficult or
        impossible, and explore outcomes that might otherwise never emerge.</p>

        <a href="{BOOK_URL}" class="btn btn-primary" style="margin-top:8px;font-size:1rem;padding:15px 32px">
          Book a Consultation <span style="margin-left:6px">&#8594;</span>
        </a>
      </div>

    </div>
  </div>
</section>

<div class="booking-strip">
  <div class="wrap">
    <h2>Ready to resolve your dispute <em>without court</em>?</h2>
    <p>Book a free initial consultation and get honest, expert advice on your situation — with no obligation.</p>
    <a href="{BOOK_URL}" class="btn" style="background:var(--cream);color:var(--sage-deep);font-size:1.1rem;padding:18px 38px">
      Book a Free Consultation &#8594;
    </a>
  </div>
</div>
</main>"""

d += page_end()

out_path = os.path.join(OUT, "our-team", "dan-toombs")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-team/dan-toombs built")

# ============================================================
# /our-team/farley-tolpen/
# ============================================================

farley_schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Our Team","our-team"),("Farley Tolpen","our-team/farley-tolpen")]),
    {
        "@type": "Person",
        "name": "Farley Tolpen",
        "jobTitle": "Accredited Mediator & Lawyer",
        "url": f"{DOMAIN}/our-team/farley-tolpen/",
        "image": f"{DOMAIN}/assets/images/Farley-Bio.png",
        "worksFor": {"@id": f"{DOMAIN}/#organization"},
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "name": "NMAS Accredited Mediator",
             "credentialCategory": "Professional Accreditation",
             "recognizedBy": {"@type": "Organization", "name": "AMDRAS", "url": "https://amdras.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Family Dispute Resolution Practitioner",
             "credentialCategory": "Professional Certification"},
            {"@type": "EducationalOccupationalCredential", "name": "Registered Family Law Arbitrator",
             "credentialCategory": "Professional Registration"},
        ],
        "memberOf": [
            {"@type": "Organization", "name": "Queensland Law Society", "url": "https://www.qls.com.au/"},
            {"@type": "Organization", "name": "California State Bar", "url": "https://www.calbar.ca.gov/"},
        ],
    }
]

d = head("Farley Tolpen — Accredited Mediator, FDRP &amp; Lawyer | Mediations Australia",
         "Meet Farley Tolpen — Nationally Accredited Mediator (AMDRAS), certified FDRP, and Family Law Arbitrator with 40+ years experience and approximately 4,500+ matters mediated.",
         "our-team/farley-tolpen", extra_schema=farley_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our team","/our-team/"),("Farley Tolpen",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:60ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Farley Tolpen — <em>Nationally Accredited Mediator (AMDRAS), Certified FDRP &amp; Lawyer</em>
      </h1>
    </div>
  </div>
</section>

<section style="background:var(--cream);padding-bottom:24px">
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/Farley-Bio.png"
             alt="Farley Tolpen — Accredited Mediator and Lawyer, Mediations Australia"
             width="260" height="320" loading="eager">
        <table class="cred-table" aria-label="Farley Tolpen credentials">
          <tbody>
            <tr><td>Accreditation</td><td><a href="https://amdras.au/" target="_blank" rel="noopener">NMAS</a> Accredited Mediator</td></tr>
            <tr><td>Certification</td><td>Family Dispute Resolution Practitioner (FDRP)</td></tr>
            <tr><td>Registration</td><td>Family Law Arbitrator</td></tr>
            <tr><td>Admitted</td><td><a href="https://www.qls.com.au/" target="_blank" rel="noopener">Queensland Law Society</a></td></tr>
            <tr><td>Admitted</td><td>Previous — <a href="https://www.calbar.ca.gov/" target="_blank" rel="noopener">California State Bar</a></td></tr>
            <tr><td>Experience</td><td>40+ years mediation, arbitration &amp; litigation</td></tr>
            <tr><td>Track record</td><td>4,500+ matters · 90% resolution rate</td></tr>
          </tbody>
        </table>
      </aside>

      <div class="mediator-content">
        <h2>Farley Tolpen — Nationally Accredited Mediator (AMDRAS), FDRP, Arbitrator &amp; Lawyer</h2>
        <span class="tag-line">40 years. 4,500 matters mediated. High resolution rate.</span>

        <p>Farley Tolpen brings a depth of experience that is genuinely rare: over four decades of mediating,
        arbitrating and litigating across Australia and the United States, with more than 4,500 matters mediated
        and around a 90% resolution rate. Farley is a Nationally Accredited Mediator, a certified Family Dispute
        Resolution Practitioner, and a registered Family Law Arbitrator — giving clients access to the full range
        of dispute resolution pathways, all under one roof. Farley is widely recognised for being a highly
        experienced professional who is committed to justice and access to fair processes and the best outcomes
        for clients.</p>

        <h3>A Professional Dedicated to Justice and Fairness</h3>
        <p>Over 40 years Farley has brought to his practice a strong commitment to serving vulnerable populations
        and clients. Farley regularly works with matters involving domestic and family violence whereby he creates
        access to mediation that prioritises the needs of his clients. At a State level in 2023, Farley was
        recognised by Queensland Corrective Services for his six years of service as an Official Visitor assisting
        prisoners to manage and resolve their complaints. Prior to this, Farley served as a Lawyer and Board Member
        for a Queensland Community Legal Centre and as a Board Member of community-based organisations for
        the homeless.</p>

        <h3>Four Decades of Frontline Experience</h3>
        <p>Farley has spent his career working at the sharp end of disputes — in courtrooms, arbitration chambers,
        and mediation rooms across two legal systems. That hands-on litigation background means he understands
        exactly what is at stake if a matter proceeds: the costs, the timelines, the risks and the emotional toll
        on each of the parties. It is that knowledge — not just of mediation technique, but of what lies on the
        other side of the table if mediation fails — that shapes how Farley approaches every session.</p>

        <h3>Australia and the United States</h3>
        <p>Farley is a member of the
        <a href="https://www.qls.com.au/" target="_blank" rel="noopener">Queensland Law Society</a> and was
        previously a member of the
        <a href="https://www.calbar.ca.gov/" target="_blank" rel="noopener">California State Bar</a> — a combination
        that gives him a uniquely broad perspective on how legal systems, commercial norms, and dispute resolution
        cultures differ. For clients with cross-border interests, Farley's experience is a practical advantage
        that few mediators in Australia can offer.</p>

        <h3>Specialist Areas</h3>
        <p>Farley's practice spans the full range of disputes that bring people to mediation including but not
        limited to the following:</p>
        <ul>
          <li><a href="/family-law-mediation/">Family law</a> — separations, parenting arrangements, property division and the full complexity of relationship breakdown</li>
          <li><a href="/estate-dispute-mediation/">Estate disputes</a> — will contests, inheritance disagreements, family maintenance provisions, estate claims, and executor conflicts</li>
          <li><a href="/workplace-mediation/">Workplace mediation</a> — employment disputes including allegations of bullying, sexual harassment and racial discrimination, team conflicts and organisational breakdowns</li>
          <li>Commercial and business law — partnership, director and shareholder disputes, contractor disagreements, contract disputes, insurance claims, franchise disputes and business exits</li>
          <li>Real estate and construction — property transactions, commercial and retail shop lease disputes, easement and boundary disputes, development disputes and building contract conflicts</li>
        </ul>

        <h3>What 4,500 Matters Teaches You</h3>
        <p>The resolution rate of around 90% across more than 4,500 matters is not just a statistic — it reflects
        a disciplined understanding of why disputes persist. Farley recognises that the real barriers to resolution
        are rarely the legal issues on paper. They are the non-financial motivations, the strategic objectives of
        the parties and their lawyers, the sunk cost of the litigation process, and the human dynamics that make
        people dig in rather than settle. His job is to understand those dynamics clearly and create the conditions
        in which both sides can move forward.</p>

        <h3>A Practical, Outcomes-Focused Approach</h3>
        <p>Farley does not approach mediation as a procedural exercise. He brings the same rigour and preparation
        to a mediation that he would bring to a trial — understanding the strengths and weaknesses of each party's
        position, the likely range of outcomes at court, and the interests that sit beneath each side's stated
        position. The result is a process that feels substantive, not perfunctory, and resolutions that are durable
        because they reflect what the parties actually need.</p>

        <a href="{BOOK_URL}" class="btn btn-primary" style="margin-top:8px;font-size:1rem;padding:15px 32px">
          Book a Consultation <span style="margin-left:6px">&#8594;</span>
        </a>
      </div>

    </div>
  </div>
</section>

<div class="booking-strip">
  <div class="wrap">
    <h2>Ready to resolve your dispute <em>without court</em>?</h2>
    <p>Book a free initial consultation and get honest, expert advice on your situation — with no obligation.</p>
    <a href="{BOOK_URL}" class="btn" style="background:var(--cream);color:var(--sage-deep);font-size:1.1rem;padding:18px 38px">
      Book a Free Consultation &#8594;
    </a>
  </div>
</div>
</main>"""

d += page_end()

out_path = os.path.join(OUT, "our-team", "farley-tolpen")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-team/farley-tolpen built")

# ============================================================
# /our-team/prav-singh-pillay/
# ============================================================

prav_schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Our Team","our-team"),("Prav Singh-Pillay","our-team/prav-singh-pillay")]),
    {
        "@type": "Person",
        "name": "Prav Singh-Pillay",
        "jobTitle": "Lawyer, Mediator & Family Dispute Resolution Practitioner",
        "url": f"{DOMAIN}/our-team/prav-singh-pillay/",
        "image": f"{DOMAIN}/assets/images/Prav-Bio.png",
        "worksFor": {"@id": f"{DOMAIN}/#organization"},
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "name": "Bachelor of Laws",
             "credentialCategory": "Degree",
             "recognizedBy": {"@type": "Organization", "name": "Griffith University", "url": "https://www.griffith.edu.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Bachelor of Commerce",
             "credentialCategory": "Degree",
             "recognizedBy": {"@type": "Organization", "name": "Griffith University", "url": "https://www.griffith.edu.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Graduate Diploma in Legal Practice",
             "credentialCategory": "Diploma",
             "recognizedBy": {"@type": "Organization", "name": "QUT", "url": "https://www.qut.edu.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Australian Nationally Accredited Mediator",
             "credentialCategory": "Professional Accreditation",
             "recognizedBy": {"@type": "Organization", "name": "AMDRAS", "url": "https://amdras.au/"}},
            {"@type": "EducationalOccupationalCredential", "name": "Family Dispute Resolution Practitioner (FDRP)",
             "credentialCategory": "Professional Certification"},
            {"@type": "EducationalOccupationalCredential", "name": "Independent Children's Lawyer (ICL)",
             "credentialCategory": "Professional Accreditation"},
        ],
        "memberOf": [
            {"@type": "Organization", "name": "Queensland Law Society", "url": "https://www.qls.com.au/"},
            {"@type": "Organization", "name": "Family Law Practitioners Association"},
            {"@type": "Organization", "name": "Family Law Section of the Law Council of Australia"},
        ],
    }
]

d = head("Prav Singh-Pillay — Lawyer, Mediator &amp; FDRP | Mediations Australia",
         "Meet Prav Singh-Pillay — family lawyer, accredited mediator and registered FDRP with 25+ years of experience across family law, civil litigation, wills and estates.",
         "our-team/prav-singh-pillay", extra_schema=prav_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our team","/our-team/"),("Prav Singh-Pillay",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:60ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Prav Singh-Pillay — <em>Lawyer &amp; Accredited Mediator</em>
      </h1>
    </div>
  </div>
</section>

<section style="background:var(--cream);padding-bottom:24px">
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/Prav-Bio.png"
             alt="Prav Singh-Pillay — Lawyer, Mediator and FDRP, Mediations Australia"
             width="260" height="320" loading="eager">
        <table class="cred-table" aria-label="Prav Singh-Pillay credentials">
          <tbody>
            <tr><td>Admitted</td><td><a href="https://www.qls.com.au/" target="_blank" rel="noopener">Queensland Law Society</a> (1997)</td></tr>
            <tr><td>Accreditation</td><td><a href="https://amdras.au/" target="_blank" rel="noopener">Nationally Accredited Mediator</a></td></tr>
            <tr><td>Certification</td><td>Family Dispute Resolution Practitioner (FDRP)</td></tr>
            <tr><td>Accreditation</td><td>Independent Children's Lawyer (ICL)</td></tr>
            <tr><td>Degree</td><td>LLB &amp; BCom, Griffith University</td></tr>
            <tr><td>Diploma</td><td>Grad. Dip. Legal Practice, QUT</td></tr>
            <tr><td>Membership</td><td>Family Law Practitioners Association</td></tr>
            <tr><td>Membership</td><td>Law Council of Australia — Family Law Section</td></tr>
          </tbody>
        </table>
      </aside>

      <div class="mediator-content">
        <h2>Prav Singh-Pillay — Lawyer &amp; Accredited Mediator</h2>
        <span class="tag-line">25 years at the bar. Family law from every angle.</span>

        <p>Prav Singh-Pillay is a family lawyer, nationally accredited mediator, and registered Family Dispute
        Resolution Practitioner with more than 25 years of practice since her admission in 1997. She brings
        a breadth of experience that is rare in a single practitioner — courtroom advocacy, mediation, and
        legal advice — allowing her to guide clients through every stage of a family law matter, whatever form
        that takes.</p>

        <h3>A Career Built Across Multiple Jurisdictions</h3>
        <p>Prav's career has taken her from Brisbane to regional Queensland, from the Gold Coast to
        California — building expertise in family law, criminal defence, civil litigation, employment law,
        wills and estates, and conveyancing across different legal environments. That breadth means she
        understands the full legal context around a family dispute, not just the immediate presenting issue.</p>

        <p>Her experience includes roles at the Director of Public Prosecutions in Brisbane, a general
        practice firm in regional Queensland, an employment law firm in California, and a boutique family
        law firm on the Gold Coast — before founding her own practice, Cornerstone Law Offices, in 2014.</p>

        <h3>Family Law: The Full Spectrum</h3>
        <p>Prav's family law practice covers every aspect of relationship breakdown, including:</p>
        <ul>
          <li><a href="/property-settlement-mediation/">Property settlements</a> and de facto relationship matters</li>
          <li><a href="/parenting-plan-mediation/">Children's arrangements</a> — parenting plans, relocation, and recovery</li>
          <li>Spousal maintenance and <a href="/financial-agreements-mediation/">financial agreements</a> (pre and post-nuptial)</li>
          <li>Same-sex relationships, paternity, and child support</li>
          <li><a href="/divorce-mediation/">Divorce</a> and domestic violence matters</li>
          <li>Consent orders and <a href="/section-60i-certificates/">Section 60I certificates</a></li>
        </ul>

        <h3>Courtroom Experience Across Multiple Jurisdictions</h3>
        <p>Prav is a committed advocate with extensive experience representing clients in the Family Court,
        Federal Circuit Court, Federal Court, State Magistrates Court, and Children's Court. She has
        appeared in bench and jury trials in the Superior Courts and in the Appeal Courts — instructing
        Counsel in complex matters while handling mentions, directions hearings, callovers, and uncomplicated
        interim hearings herself.</p>

        <p>That litigation background is not incidental to her mediation work — it is central to it. Prav
        knows from direct experience what a contested matter costs in money, time, and emotional wellbeing,
        which is why she is committed to helping clients find resolution before it comes to that.</p>

        <h3>Mediation and Section 60I Certificates</h3>
        <p>As both an accredited mediator and a registered FDRP, Prav offers clients a complete dispute
        resolution service. She conducts family dispute resolution for parenting matters and, where
        agreement cannot be reached, is authorised to issue <a href="/section-60i-certificates/">Section 60I
        certificates</a> — the document required before most parenting applications can be filed in the
        Federal Circuit and Family Court of Australia.</p>

        <h3>Beyond Family Law</h3>
        <p>Prav's legal services extend to wills and powers of attorney, estate administration,
        conveyancing, and debt recovery — providing clients with continuity of trusted legal advice
        across the full range of matters that typically arise alongside or following a separation.</p>

        <h3>Community Commitment</h3>
        <p>Prav volunteers at Women's Legal Services and My Community Legal, and has served as both a
        volunteer mediator and committee member at Bayside Community Legal Centre. Her commitment to
        accessible legal services reflects the same values that brought her to family law in the first
        place: that people navigating difficult personal circumstances deserve skilled, practical, and
        genuinely compassionate support.</p>

        <a href="{BOOK_URL}" class="btn btn-primary" style="margin-top:8px;font-size:1rem;padding:15px 32px">
          Book a Consultation <span style="margin-left:6px">&#8594;</span>
        </a>
      </div>

    </div>
  </div>
</section>

<div class="booking-strip">
  <div class="wrap">
    <h2>Ready to resolve your dispute <em>without court</em>?</h2>
    <p>Book a free initial consultation and get honest, expert advice on your situation — with no obligation.</p>
    <a href="{BOOK_URL}" class="btn" style="background:var(--cream);color:var(--sage-deep);font-size:1.1rem;padding:18px 38px">
      Book a Free Consultation &#8594;
    </a>
  </div>
</div>
</main>"""

d += page_end()

out_path = os.path.join(OUT, "our-team", "prav-singh-pillay")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-team/prav-singh-pillay built")
