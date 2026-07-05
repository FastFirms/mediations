#!/usr/bin/env python3
"""Generates /our-mediators/ — Dan Toombs bio page."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html,
                       org_schema, breadcrumb_schema,
                       DOMAIN, BOOK_URL, PHONE, PHONE_HREF)

OUT = os.path.join(os.path.dirname(__file__), "..")

TITLE = "Our Mediators | Mediations Australia"
DESC  = ("Meet Dan Toombs — Founder of Mediations Australia, AMDRAS-accredited mediator, "
         "National Human Rights Law Award recipient, and Winston Churchill Fellow.")
SLUG  = "our-mediators"

person_schema = {
    "@type": "Person",
    "name": "Dan Toombs",
    "jobTitle": "Founder & Accredited Mediator",
    "url": f"{DOMAIN}/our-mediators/",
    "image": f"{DOMAIN}/assets/images/dan-toombs.jpg",
    "worksFor": {"@id": f"{DOMAIN}/#organization"},
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "AMDRAS Accredited Mediator",
         "credentialCategory": "Professional Accreditation",
         "recognizedBy": {"@type": "Organization", "name": "AMDRAS", "url": "https://amdras.au/"}},
        {"@type": "EducationalOccupationalCredential", "name": "Winston Churchill Fellowship",
         "credentialCategory": "Fellowship",
         "recognizedBy": {"@type": "Organization", "name": "Churchill Trust Australia",
                          "url": "https://www.churchilltrust.com.au/"}},
        {"@type": "EducationalOccupationalCredential", "name": "National Human Rights Law Award",
         "credentialCategory": "Award",
         "recognizedBy": {"@type": "Organization", "name": "Australian Human Rights Commission",
                          "url": "https://humanrights.gov.au/"}},
        {"@type": "EducationalOccupationalCredential", "name": "Accredited Belbin Team Roles Facilitator",
         "credentialCategory": "Professional Accreditation",
         "recognizedBy": {"@type": "Organization", "name": "Belbin", "url": "https://www.belbin.com/"}},
    ],
    "sameAs": [
        "https://amdras.au/",
        "https://www.churchilltrust.com.au/",
        "https://humanrights.gov.au/",
    ],
}

schema = [org_schema(), breadcrumb_schema([("Home",""),("Our Mediators",SLUG)]), person_schema]

PAGE_CSS = """<style>
.mediator-hero{padding:60px 0 0;background:var(--sand)}
.mediator-profile{display:grid;grid-template-columns:260px 1fr;gap:48px;align-items:start;padding:48px 0 56px}
@media(max-width:720px){.mediator-profile{grid-template-columns:1fr}}
.mediator-photo{position:sticky;top:100px}
.mediator-photo img{width:100%;border-radius:16px;display:block;box-shadow:0 8px 32px rgba(0,0,0,.10)}
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
</style>"""

d = head(TITLE, DESC, SLUG, extra_schema=schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our mediators",None)])}
<section class="mediator-hero">
  <div class="wrap">
    <div style="max-width:60ch">
      <p class="sec-tag">Meet the team</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2rem,5vw,3.2rem);line-height:1.15;margin-bottom:16px">
        Our Mediators — <em>experience that resolves disputes</em>
      </h1>
    </div>
  </div>
</section>

<section style="background:var(--cream);padding-bottom:24px">
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/dan-toombs.jpg"
             alt="Dan Toombs — Founder and Accredited Mediator, Mediations Australia"
             width="260" height="260" loading="eager">
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

        <p>Dan Toombs is the Founder of Mediations Australia and one of Australia's most credentialled and
        reform-minded mediators. An <a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS-accredited mediator</a>,
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
    <p>Book a fixed-fee consultation with Dan and get honest, expert advice on your situation — with no obligation.</p>
    <a href="{BOOK_URL}" class="btn" style="background:var(--cream);color:var(--sage-deep);font-size:1.1rem;padding:18px 38px">
      Book your free consultation &#8594;
    </a>
  </div>
</div>
</main>"""

d += page_end()

out_path = os.path.join(OUT, SLUG)
os.makedirs(out_path, exist_ok=True)
with open(os.path.join(out_path, "index.html"), "w") as f:
    f.write(d)

print("our-mediators built")
