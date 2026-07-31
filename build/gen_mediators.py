#!/usr/bin/env python3
"""Generates /our-mediators/ index + individual bio pages for Dan Toombs and Farley Tolpen."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html,
                       org_schema, breadcrumb_schema,
                       DOMAIN, BOOK_URL, PHONE, PHONE_HREF)

OUT = os.path.join(os.path.dirname(__file__), "..")

PAGE_CSS = """<style>
.mediator-hero{padding:60px 0 0;background:var(--sand)}
.mediator-profile{display:grid;grid-template-columns:260px 1fr;gap:48px;align-items:start;padding:48px 0 56px}
@media(max-width:720px){.mediator-profile{grid-template-columns:1fr}}
.mediator-photo{position:sticky;top:100px}
.mediator-photo img{width:100%;height:320px;object-fit:cover;object-position:top;border-radius:16px;display:block;box-shadow:0 8px 32px rgba(0,0,0,.10)}
.cred-table{margin-top:24px;width:100%;border-collapse:collapse;font-size:.85rem}
.cred-table td{padding:7px 0;border-bottom:1px solid var(--sand-deep);vertical-align:top;color:var(--ink-soft)}
.cred-table td:first-child{font-weight:600;color:var(--ink);padding-right:12px;white-space:nowrap}
.mediator-content h2{font-family:var(--serif);font-size:clamp(1.5rem,3vw,2rem);margin:36px 0 12px}
.mediator-content h2:first-child{margin-top:0}
.mediator-content h3{font-size:1.15rem;font-weight:600;margin:28px 0 8px;color:var(--sage-deep)}
.mediator-content p{font-size:1.06rem;color:var(--ink-soft);line-height:1.75;margin-bottom:18px;max-width:68ch}
.mediator-content .tag-line{font-family:var(--serif);font-size:1.2rem;font-style:italic;color:var(--sage-deep);margin-bottom:32px;display:block}
.mediator-content a{color:var(--sage-deep)}
.booking-strip{background:var(--sage-deep);color:var(--cream);padding:48px 0;text-align:center;margin-top:24px}
.booking-strip h2{font-family:var(--serif);font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:12px}
.booking-strip p{font-size:1.05rem;opacity:.88;max-width:54ch;margin:0 auto 28px}
.team-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:32px;padding:56px 0}
.team-card{background:var(--sand);border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;display:block;transition:box-shadow .2s}
.team-card:hover{box-shadow:0 8px 32px rgba(0,0,0,.12)}
.team-card img{width:100%;height:260px;object-fit:cover;object-position:center 15%;display:block}
.team-card-body{padding:24px}
.team-card-name{font-family:var(--serif);font-size:1.3rem;margin-bottom:4px}
.team-card-role{color:var(--sage-deep);font-weight:600;font-size:.92rem;margin-bottom:10px}
.team-card-bio{font-size:.95rem;color:var(--ink-soft);line-height:1.65;margin-bottom:16px}
.team-card-link{font-size:.9rem;font-weight:600;color:var(--terra)}
</style>"""

# ============================================================
# /our-mediators/ INDEX PAGE
# ============================================================

idx_schema = [org_schema(), breadcrumb_schema([("Home",""),("Our Mediators","our-mediators")])]
d = head("Our Mediators | Mediations Australia",
         "Meet the nationally accredited mediators at Mediations Australia — dual-qualified lawyers with decades of experience across family law, property, commercial, and workplace disputes.",
         "our-mediators", extra_schema=idx_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our mediators",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:64ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Our Mediators — <em>accredited, experienced, lawyer-aware</em>
      </h1>
      <p style="font-size:1.1rem;color:var(--ink-soft);max-width:58ch">Every mediator at Mediations Australia is nationally accredited. Many are also practising or formerly-practising lawyers — so the legal realities of your matter are understood from the very first conversation.</p>
    </div>
  </div>
</section>

<section style="background:var(--cream)">
  <div class="wrap">
    <div class="team-grid">

      <a href="/our-mediators/dan-toombs/" class="team-card">
        <img src="/assets/images/DanT.png" alt="Dan Toombs — Founder and Accredited Mediator" loading="eager">
        <div class="team-card-body">
          <p class="team-card-name">Dan Toombs</p>
          <p class="team-card-role">Founder &amp; Accredited Mediator</p>
          <p class="team-card-bio">Multi-award winning lawyer, Winston Churchill Fellow, and National Human Rights Law Award recipient. Over two decades resolving complex family, property and workplace disputes.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

      <a href="/our-mediators/farley-tolpen/" class="team-card">
        <img src="/assets/images/FarleyT.png" alt="Farley Tolpen — Accredited Mediator and Lawyer" loading="lazy">
        <div class="team-card-body">
          <p class="team-card-name">Farley Tolpen</p>
          <p class="team-card-role">Accredited Mediator &amp; Lawyer</p>
          <p class="team-card-bio">Dual-qualified in Australia and the United States with over 40 years of mediation, arbitration and litigation experience. More than 4,500 matters mediated with a 90% resolution rate.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

    </div>
  </div>
</section>
</main>"""

d += page_end()

out_path = os.path.join(OUT, "our-mediators")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-mediators index built")

# ============================================================
# /our-mediators/dan-toombs/
# ============================================================

dan_schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Our Mediators","our-mediators"),("Dan Toombs","our-mediators/dan-toombs")]),
    {
        "@type": "Person",
        "name": "Dan Toombs",
        "jobTitle": "Founder & Accredited Mediator",
        "url": f"{DOMAIN}/our-mediators/dan-toombs/",
        "image": f"{DOMAIN}/assets/images/DanT.png",
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

d = head("Dan Toombs — Founder & Accredited Mediator | Mediations Australia",
         "Meet Dan Toombs — Founder of Mediations Australia, AMDRAS-accredited mediator, National Human Rights Law Award recipient, and Winston Churchill Fellow.",
         "our-mediators/dan-toombs", extra_schema=dan_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our mediators","/our-mediators/"),("Dan Toombs",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:60ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Dan Toombs — <em>Founder &amp; Accredited Mediator</em>
      </h1>
    </div>
  </div>
</section>

<section style="background:var(--cream);padding-bottom:24px">
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/DanT.png"
             alt="Dan Toombs — Founder and Accredited Mediator, Mediations Australia"
             width="260" height="320" loading="eager">
        <table class="cred-table" aria-label="Dan Toombs credentials">
          <tbody>
            <tr><td>Accreditation</td><td><a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS</a> Accredited Mediator</td></tr>
            <tr><td>Fellowship</td><td><a href="https://www.churchilltrust.com.au/" target="_blank" rel="noopener">Winston Churchill Fellow</a></td></tr>
            <tr><td>Award</td><td><a href="https://humanrights.gov.au/about-us/what-we-do/human-rights-awards-2026" target="_blank" rel="noopener">National Human Rights Law Award</a></td></tr>
            <tr><td>Award</td><td>Queensland Disability Award</td></tr>
            <tr><td>Publisher</td><td><a href="https://www.thomsonreuters.com.au/en-au.html" target="_blank" rel="noopener">Thomson Reuters</a> — published legal author</td></tr>
            <tr><td>Accreditation</td><td><a href="https://www.belbin.com/" target="_blank" rel="noopener">Belbin</a> Team Roles Facilitator</td></tr>
            <tr><td>Leadership</td><td><a href="https://aali.org.au/" target="_blank" rel="noopener">Adaptive Leadership</a> (Harvard framework)</td></tr>
            <tr><td>Fellowship</td><td><a href="https://www.innovatingjustice.org/" target="_blank" rel="noopener">Center for Justice Innovation</a>, New York</td></tr>
          </tbody>
        </table>
      </aside>

      <div class="mediator-content">
        <h2>Dan Toombs — Founder, Mediations Australia</h2>
        <span class="tag-line">Multi-award winning lawyer. Published author. Systemic reformer. Mediator.</span>

        <p>Dan Toombs is the Founder of Mediations Australia. An <a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS-accredited mediator</a>,
        Dan brings to every session a rare combination of legal expertise, systemic reform experience, and a deep
        understanding of the human realities behind every dispute.</p>

        <h3>A Multi-Award Winning Lawyer and Published Author</h3>
        <p>Dan is a Multi-Award Winning Lawyer published by
        <a href="https://www.thomsonreuters.com.au/en-au.html" target="_blank" rel="noopener">Thomson Reuters</a> —
        one of the world's most respected legal publishers. His legal career has been defined not only by practice,
        but by meaningful reform. He has spearheaded major legislative change in Australia, including reform that
        delivered substantially improved outcomes for people with mental health and intellectual disabilities who
        become caught in the criminal justice system — work recognised with the <strong>Queensland Disability Award</strong>.</p>

        <h3>National and International Recognition</h3>
        <p>Dan is the recipient of the
        <a href="https://humanrights.gov.au/about-us/what-we-do/human-rights-awards-2026" target="_blank" rel="noopener">National Human Rights Law Award</a>
        — one of Australia's most prestigious recognitions of leadership in the advancement of human rights through law.</p>

        <p>Dan is a <a href="https://www.churchilltrust.com.au/" target="_blank" rel="noopener">Winston Churchill Fellow</a>,
        undertaking pioneering work with the
        <a href="https://www.innovatingjustice.org/" target="_blank" rel="noopener">Center for Justice Innovation</a>
        in New York — an internationally recognised institution dedicated to solving complex problems across justice,
        health, and community safety.</p>

        <h3>Leadership, Behavioural Intelligence, and Team Dynamics</h3>
        <p>Dan is an <a href="https://www.belbin.com/" target="_blank" rel="noopener">Accredited Belbin Team Roles Facilitator</a>
        — a globally recognised behavioural framework that, in a mediation context, gives Dan a sophisticated lens
        through which to read group dynamics, identify communication breakdowns, and create conditions where all
        parties feel heard and able to contribute constructively to resolution.</p>

        <p>Dan is also trained in
        <a href="https://aali.org.au/" target="_blank" rel="noopener">Adaptive Leadership</a> through the Australian
        Adaptive Leadership Institute — a framework developed at Harvard University that equips leaders to navigate
        complex, high-stakes challenges where no simple technical fix exists.</p>

        <h3>A Leader in Access to Justice</h3>
        <p>Dan served as CEO of one of Australia's largest community legal centres, bringing leadership, strategic
        vision, and a fierce commitment to equitable access to justice. He has also worked alongside
        <a href="https://www.brockovich.com/" target="_blank" rel="noopener">Erin Brockovich</a> on systemic
        environmental and public health campaigns in the United States — collaborating on some of the most complex,
        community-affecting disputes imaginable.</p>

        <h3>Building Across the Legal Ecosystem</h3>
        <p>Dan's work has always sat at the intersection of law, access to justice, and practical reform. That
        belief has shaped not just his practice but the businesses he has founded — each addressing a different
        part of how people find, experience, and benefit from legal services.</p>

        <p><a href="https://www.bestsolicitors.com.au/" target="_blank" rel="noopener"><strong>Best Solicitors</strong></a>
        is an independent legal rankings publisher covering eight jurisdictions. Rankings are transparent,
        client-led, and use a published methodology — they cannot be influenced by payment. It is a direct
        expression of Dan's belief that legal reputation should be earned, not bought.</p>

        <p><a href="https://www.practiceproof.com/" target="_blank" rel="noopener"><strong>Practice Proof</strong></a>
        provides strategy, branding, marketing and growth services for law firms — helping practices communicate
        their value clearly and build sustainable client relationships in a rapidly changing market.</p>

        <p>Mediations Australia exists within that same philosophy: that legal services should be genuinely
        accessible, transparently priced, and focused on outcomes that actually improve people's lives. The
        profession is entering one of the most significant periods of change in its history — AI, digital trust,
        and reputation systems are reshaping how legal services are found, delivered, and valued. Dan's work
        across all three ventures reflects his conviction that the practitioners best placed to serve clients
        well are those who engage with that change honestly.</p>

        <h3>What This Means for You</h3>
        <p>Dan approaches every mediation — whether a <a href="/property-settlement-mediation/">property settlement</a>,
        a <a href="/parenting-plan-mediation/">parenting plan dispute</a>, an estate conflict,
        a <a href="/workplace-mediation/">workplace dispute</a>, or a commercial matter — with both emotional
        intelligence and clear-eyed commercial awareness. His singular focus is on helping people reach durable,
        workable, and fair resolutions: faster, more cost-effectively, and with far less collateral damage than
        litigation.</p>

        <a href="{BOOK_URL}" class="btn btn-primary" style="margin-top:8px;font-size:1rem;padding:15px 32px">
          Book a consultation with Dan <span style="margin-left:6px">&#8594;</span>
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

out_path = os.path.join(OUT, "our-mediators", "dan-toombs")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-mediators/dan-toombs built")

# ============================================================
# /our-mediators/farley-tolpen/
# ============================================================

farley_schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Our Mediators","our-mediators"),("Farley Tolpen","our-mediators/farley-tolpen")]),
    {
        "@type": "Person",
        "name": "Farley Tolpen",
        "jobTitle": "Accredited Mediator & Lawyer",
        "url": f"{DOMAIN}/our-mediators/farley-tolpen/",
        "image": f"{DOMAIN}/assets/images/FarleyT.png",
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

d = head("Farley Tolpen — Accredited Mediator &amp; Lawyer | Mediations Australia",
         "Meet Farley Tolpen — dual-qualified mediator and lawyer in Australia and the United States, with over 40 years experience and more than 4,500 matters mediated.",
         "our-mediators/farley-tolpen", extra_schema=farley_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our mediators","/our-mediators/"),("Farley Tolpen",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:60ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Farley Tolpen — <em>Accredited Mediator &amp; Lawyer</em>
      </h1>
    </div>
  </div>
</section>

<section style="background:var(--cream);padding-bottom:24px">
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/FarleyT.png"
             alt="Farley Tolpen — Accredited Mediator and Lawyer, Mediations Australia"
             width="260" height="320" loading="eager">
        <table class="cred-table" aria-label="Farley Tolpen credentials">
          <tbody>
            <tr><td>Accreditation</td><td><a href="https://amdras.au/" target="_blank" rel="noopener">NMAS</a> Accredited Mediator</td></tr>
            <tr><td>Certification</td><td>Family Dispute Resolution Practitioner (FDRP)</td></tr>
            <tr><td>Registration</td><td>Family Law Arbitrator</td></tr>
            <tr><td>Admitted</td><td><a href="https://www.qls.com.au/" target="_blank" rel="noopener">Queensland Law Society</a></td></tr>
            <tr><td>Admitted</td><td><a href="https://www.calbar.ca.gov/" target="_blank" rel="noopener">California State Bar</a></td></tr>
            <tr><td>Experience</td><td>40+ years mediation, arbitration &amp; litigation</td></tr>
            <tr><td>Track record</td><td>4,500+ matters · 90% resolution rate</td></tr>
          </tbody>
        </table>
      </aside>

      <div class="mediator-content">
        <h2>Farley Tolpen — Accredited Mediator &amp; Lawyer</h2>
        <span class="tag-line">40 years. Two continents. 4,500 matters resolved.</span>

        <p>Farley Tolpen brings a depth of experience that is genuinely rare: over four decades of mediating,
        arbitrating and litigating across Australia and the United States, with more than 4,500 matters resolved
        and a 90% settlement rate. Dual-qualified in both jurisdictions, Farley is an accredited National Mediator,
        a certified Family Dispute Resolution Practitioner, and a registered Family Law Arbitrator — giving clients
        access to the full range of dispute resolution pathways, all under one roof.</p>

        <h3>Four Decades of Frontline Experience</h3>
        <p>Farley has spent his career working at the sharp end of disputes — in courtrooms, arbitration chambers,
        and mediation rooms across two legal systems. That hands-on litigation background means he understands
        exactly what is at stake if a matter proceeds: the costs, the timelines, the emotional toll, and the
        unpredictability of a judge's decision. It is that knowledge — not just of mediation technique, but of
        what lies on the other side of the table if mediation fails — that shapes how Farley approaches every
        session.</p>

        <h3>Dual-Qualified: Australia and the United States</h3>
        <p>Farley is a member of both the
        <a href="https://www.qls.com.au/" target="_blank" rel="noopener">Queensland Law Society</a> and the
        <a href="https://www.calbar.ca.gov/" target="_blank" rel="noopener">California State Bar</a> — a combination
        that gives him a uniquely broad perspective on how legal systems, commercial norms, and dispute resolution
        cultures differ. For clients with cross-border interests, or matters that touch on US law, that
        dual qualification is a practical advantage that few mediators in Australia can offer.</p>

        <h3>Specialist Areas</h3>
        <p>Farley's practice spans the full range of disputes that bring people to mediation:</p>
        <ul style="color:var(--ink-soft);line-height:1.8;font-size:1.05rem;padding-left:1.4em;margin-bottom:18px">
          <li><a href="/family-law-mediation/">Family law</a> — separations, parenting arrangements, and the full complexity of relationship breakdown</li>
          <li><a href="/estate-dispute-mediation/">Estate disputes</a> — will contests, inheritance disagreements, and executor conflicts</li>
          <li><a href="/workplace-mediation/">Workplace mediation</a> — employment disputes, team conflicts, and organisational breakdowns</li>
          <li>Commercial and business law — partnership disputes, contractor disagreements, and business exits</li>
          <li>Real estate and construction — property transactions, development disputes, and building contract conflicts</li>
        </ul>

        <h3>What 4,500 Matters Teaches You</h3>
        <p>The 90% resolution rate across more than 4,500 matters is not just a statistic — it reflects a
        disciplined understanding of why disputes persist. Farley recognises that the real barriers to resolution
        are rarely the legal issues on paper. They are the non-financial motivations, the strategic objectives
        of the parties and their lawyers, the sunk cost of the litigation process, and the human dynamics that
        make people dig in rather than settle. His job is to understand those dynamics clearly and create the
        conditions in which both sides can move.</p>

        <h3>A Practical, Outcomes-Focused Approach</h3>
        <p>Farley does not approach mediation as a procedural exercise. He brings the same rigour and
        preparation to a mediation that he would bring to a trial — understanding the strengths and weaknesses
        of each party's position, the likely range of outcomes at court, and the interests that sit beneath
        each side's stated position. The result is a process that feels substantive, not perfunctory, and
        resolutions that are durable because they reflect what the parties actually need.</p>

        <a href="{BOOK_URL}" class="btn btn-primary" style="margin-top:8px;font-size:1rem;padding:15px 32px">
          Book a consultation with Farley <span style="margin-left:6px">&#8594;</span>
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

out_path = os.path.join(OUT, "our-mediators", "farley-tolpen")
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)
print("our-mediators/farley-tolpen built")
