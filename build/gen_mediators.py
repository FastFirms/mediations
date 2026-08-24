#!/usr/bin/env python3
"""Generates /our-team/ index + individual bio pages for Dan Toombs, Farley Tolpen, and Prav Singh-Pillay."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html,
                       org_schema, breadcrumb_schema, faq_html, faq_schema, cta_band,
                       DOMAIN, BOOK_URL, PHONE, PHONE_HREF)

OUT = os.path.join(os.path.dirname(__file__), "..")

# Shared CSS — index page + bio pages
PAGE_CSS = """<style>
/* ── shared: bio pages ───────────────────────────────────── */
.mediator-hero{padding:60px 0 0;background:var(--sand)}
.mediator-profile{display:grid;grid-template-columns:280px 1fr;gap:48px;align-items:start;padding:48px 0 24px}
@media(max-width:720px){.mediator-profile{display:block!important}.mediator-photo{position:static!important;width:100%!important;margin-bottom:32px}.mediator-photo img{width:100%!important;height:280px}.mediator-content{width:100%!important}}
.mediator-photo img{width:100%;height:320px;object-fit:cover;object-position:top;border-radius:16px;display:block;box-shadow:0 8px 32px rgba(0,0,0,.10)}
.cred-table{margin-top:24px;width:100%;border-collapse:collapse;font-size:.85rem}
.cred-table td{padding:7px 0;border-bottom:1px solid var(--sand-deep);vertical-align:top;color:var(--ink-soft)}
.cred-table td:first-child{font-weight:600;color:var(--ink);padding-right:12px}
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

/* ── index page only ─────────────────────────────────────── */
.ot-hero{padding:56px 0 48px;background:var(--sand)}
.ot-hero-inner{max-width:64ch}
.ot-eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--sage-deep);margin-bottom:10px}
.ot-h1{font-family:var(--serif);font-size:clamp(2rem,5vw,3rem);line-height:1.15;margin-bottom:18px}
.ot-intro{font-size:1.1rem;color:var(--ink-soft);max-width:58ch;line-height:1.7}

/* team cards */
.team-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;padding:0}
@media(max-width:900px){.team-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.team-grid{grid-template-columns:1fr}}
.team-card{background:var(--cream);border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:box-shadow .2s}
.team-card:hover{box-shadow:0 8px 32px rgba(0,0,0,.12)}
.team-card-photo{height:260px;background-repeat:no-repeat;background-color:var(--sand-deep)}
.team-card-body{padding:24px;flex:1;display:flex;flex-direction:column}
.team-card-name{font-family:var(--serif);font-size:1.3rem;margin-bottom:4px}
.team-card-role{color:var(--sage-deep);font-weight:600;font-size:.9rem;margin-bottom:10px;letter-spacing:.02em}
.team-card-bio{font-size:.95rem;color:var(--ink-soft);line-height:1.65;margin-bottom:16px;flex:1}
.team-card-link{font-size:.9rem;font-weight:600;color:var(--terra)}

/* broader capability band */
.ot-network{background:var(--sage-deep);color:var(--cream);padding:80px 0}
.ot-network-inner{max-width:72ch;margin:0 auto;text-align:center}
.ot-network .eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;opacity:.7;margin-bottom:14px}
.ot-network h2{font-family:var(--serif);font-size:clamp(1.8rem,4vw,2.6rem);line-height:1.2;margin-bottom:20px}
.ot-network p{font-size:1.05rem;line-height:1.75;opacity:.88;max-width:62ch;margin:0 auto 20px}
.ot-feature-stmt{font-family:var(--serif);font-size:clamp(1.25rem,2.5vw,1.7rem);font-style:italic;margin:32px auto 36px;line-height:1.35;max-width:50ch;opacity:.95}

/* expertise grid */
.ot-expertise{padding:80px 0;background:var(--sand)}
.ot-exp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
@media(max-width:900px){.ot-exp-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.ot-exp-grid{grid-template-columns:1fr}}
.ot-exp-card{background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:28px 24px;text-decoration:none;color:inherit;display:block;transition:box-shadow .2s}
.ot-exp-card:hover{box-shadow:0 6px 24px rgba(0,0,0,.09)}
.ot-exp-icon{width:42px;height:42px;border-radius:10px;background:var(--sand);display:flex;align-items:center;justify-content:center;color:var(--sage-deep);margin-bottom:16px}
.ot-exp-card h3{font-size:1rem;font-weight:700;margin-bottom:6px;color:var(--ink)}
.ot-exp-card p{font-size:.95rem;color:var(--ink-soft);line-height:1.65;margin:0}

/* matching section */
.ot-matching{padding:80px 0;background:var(--cream)}
.ot-match-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}
@media(max-width:900px){.ot-match-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.ot-match-grid{grid-template-columns:1fr}}
.ot-match-item{display:flex;gap:14px;align-items:flex-start}
.ot-match-dot{width:10px;height:10px;background:var(--sage-deep);border-radius:50%;flex-shrink:0;margin-top:6px}
.ot-match-item h3{font-size:1rem;font-weight:700;margin-bottom:4px}
.ot-match-item p{font-size:.93rem;color:var(--ink-soft);line-height:1.6;margin:0}

/* australia-wide */
.ot-aus{padding:80px 0;background:var(--sand)}
.ot-aus-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px}
@media(max-width:900px){.ot-aus-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){.ot-aus-grid{grid-template-columns:1fr}}
.ot-office{background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:22px 18px}
.ot-office strong{display:block;font-size:.95rem;font-weight:700;color:var(--sage-deep);margin-bottom:6px}
.ot-office span{font-size:.87rem;color:var(--ink-soft);line-height:1.5}

/* mediation vs arbitration */
.ot-mva{padding:80px 0;background:var(--cream)}
.ot-mva-cards{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px}
@media(max-width:640px){.ot-mva-cards{grid-template-columns:1fr}}
.ot-mva-card{background:var(--sand);border:1px solid var(--line);border-radius:16px;padding:36px 28px}
.ot-mva-card h3{font-family:var(--serif);font-size:1.4rem;margin-bottom:14px;color:var(--ink)}
.ot-mva-card p{font-size:.97rem;color:var(--ink-soft);line-height:1.7;margin-bottom:14px}
.ot-mva-sub{text-align:center;margin-top:36px}
.ot-mva-sub p{font-size:1rem;color:var(--ink-soft);margin-bottom:18px}

/* section utility */
.ot-sec-hdr{text-align:center;max-width:62ch;margin:0 auto}
.ot-sec-hdr .eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--sage-deep);margin-bottom:10px}
.ot-sec-hdr h2{font-family:var(--serif);font-size:clamp(1.7rem,3.5vw,2.4rem);margin-bottom:14px;color:var(--ink)}
.ot-sec-hdr p{font-size:1rem;color:var(--ink-soft);line-height:1.7}
</style>"""

# ============================================================
# /our-team/ INDEX PAGE  (9-section rebuild per brief 2026-08)
# ============================================================

TEAM_FAQ = [
    ("Is this the full Mediations Australia team?",
     "Dan Toombs, Farley Tolpen, and Prav Singh-Pillay are the core people behind Mediations Australia. "
     "Depending on the nature and complexity of your matter, Mediations Australia can also draw on a broader network "
     "of mediators, arbitrators, and dispute resolution professionals."),
    ("How do I choose a mediator?",
     "You don't need to choose before speaking with us. When you book a consultation, we discuss the nature of "
     "the dispute, what you're hoping to achieve, and which practitioner is best suited to your matter. "
     "We'll explain who we'd recommend and why."),
    ("Can you help with disputes outside family law?",
     "Yes. Our core team handles family and separation matters, workplace and employment disputes, commercial "
     "and business conflicts, estate and wills disagreements, and property matters. We can also refer to "
     "appropriate specialists in the broader network for matters requiring specific expertise."),
    ("Do you have access to arbitrators?",
     "Farley Tolpen is a registered Family Law Arbitrator and can conduct arbitration for property and financial "
     "matters. For other commercial arbitration needs, we can help identify appropriate practitioners."),
    ("How do I know a practitioner has relevant experience for my dispute?",
     "When you contact us, we ask about the nature of the dispute before recommending a practitioner. "
     "Experience, professional background, and availability are all considered. You can also review "
     "individual team profiles to understand each person's specialist areas and track record."),
    ("Can you help with disputes outside major cities?",
     "Yes. Mediations Australia offers mediation online as well as in person across Sydney, Melbourne, "
     "Brisbane, and Perth. Online mediation is equally effective for most matters and removes the need "
     "for travel entirely."),
    ("Is online mediation as effective as in-person?",
     "For most disputes, online mediation achieves outcomes comparable to in-person sessions. "
     "It removes the need for travel, can reduce costs, and often makes it easier to schedule sessions "
     "across locations. Our practitioners are experienced in conducting online mediation effectively. "
     "<a href='/online-mediation-australia/'>Learn more about online mediation.</a>"),
]

idx_schema = [
    org_schema(),
    breadcrumb_schema([("Home",""),("Our Team","our-team")]),
    faq_schema([(q, a) for q, a in TEAM_FAQ]),
]

d = head("Our Team — Experienced Dispute Resolution | Mediations Australia",
         "Meet the core team at Mediations Australia — Dan Toombs, Farley Tolpen, and Prav Singh-Pillay — "
         "accredited mediators and lawyers handling family, workplace, commercial, estate and property disputes across Australia.",
         "our-team", extra_schema=idx_schema)
d = d.replace("</head>", PAGE_CSS + "</head>")
d += nav()

d += f"""<main id="main">
{crumb_html([("Home",""),("Our team",None)])}

<!-- ①  HERO -->
<section class="ot-hero">
  <div class="wrap">
    <div class="ot-hero-inner">
      <p class="ot-eyebrow">Meet the team</p>
      <h1 class="ot-h1">Our Team — <em>experienced dispute resolution, backed by broader expertise</em></h1>
      <p class="ot-intro">Mediations Australia is built around a core team of nationally accredited mediators and lawyers — Dan Toombs, Farley Tolpen, and Prav Singh-Pillay — each with deep experience across the disputes that matter most to individuals, families, and businesses. Depending on the nature of your matter, we can also draw on a broader network of mediators, arbitrators, and dispute resolution professionals.</p>
    </div>
  </div>
</section>

<!-- ②  CORE TEAM -->
<section style="padding:64px 0;background:var(--cream)">
  <div class="wrap">
    <div class="ot-sec-hdr" style="margin-bottom:0">
      <h2>Meet Our Core Team</h2>
      <p>Our core team brings together extensive experience in mediation, law and dispute resolution.</p>
    </div>
    <div class="team-grid" style="margin-top:48px">

      <a href="/our-team/dan-toombs/" class="team-card">
        <div class="team-card-photo" role="img" aria-label="Dan Toombs — Founder, Lawyer and Mediator"
             style="background-image:url('/assets/images/Dan-Bio.png');background-size:cover;background-position:center top"></div>
        <div class="team-card-body">
          <p class="team-card-name">Dan Toombs</p>
          <p class="team-card-role">Founder, Lawyer &amp; Mediator</p>
          <p class="team-card-bio">AMDRAS-accredited mediator, multi-award winning lawyer, and published author. Founder of Mediations Australia, National Human Rights Law Award recipient, and Winston Churchill Fellow.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

      <a href="/our-team/farley-tolpen/" class="team-card">
        <div class="team-card-photo" role="img" aria-label="Farley Tolpen — Accredited Mediator and Lawyer"
             style="background-image:url('/assets/images/Farley-Bio.png');background-size:cover;background-position:center top"></div>
        <div class="team-card-body">
          <p class="team-card-name">Farley Tolpen</p>
          <p class="team-card-role">Accredited Mediator &amp; Lawyer</p>
          <p class="team-card-bio">40+ years of mediation, arbitration and litigation experience across Australia and the United States. Nationally Accredited Mediator (AMDRAS), FDRP, and registered Family Law Arbitrator.</p>
          <span class="team-card-link">View profile →</span>
        </div>
      </a>

      <a href="/our-team/prav-singh-pillay/" class="team-card">
        <div class="team-card-photo" role="img" aria-label="Prav Singh-Pillay — Lawyer and Accredited Mediator"
             style="background-image:url('/assets/images/Prav-Bio.png');background-size:cover;background-position:center top"></div>
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

<!-- ③  BROADER CAPABILITY -->
<section class="ot-network">
  <div class="wrap">
    <div class="ot-network-inner">
      <p class="eyebrow">Beyond our core team</p>
      <h2>Access to a broader network of mediators and arbitrators</h2>
      <p>Our core team handles a wide range of disputes directly. For matters that require specific expertise — specialist areas of law, particular industry knowledge, or additional practitioners for complex multi-party disputes — Mediations Australia can draw on a broader network of mediators, arbitrators, and dispute resolution professionals.</p>
      <p>We don't claim a specific number. What we offer is honest guidance: when you contact us about a matter, we'll tell you clearly who is best placed to help, whether that's a member of our core team or someone from the broader network — and why.</p>
      <p class="ot-feature-stmt">"Start with the dispute. We can help determine the right way forward."</p>
      <a href="{BOOK_URL}" class="btn" style="background:var(--cream);color:var(--sage-deep);font-size:1rem;padding:15px 32px;font-weight:700">
        Book a Free Consultation →
      </a>
    </div>
  </div>
</section>

<!-- ④  EXPERTISE GRID -->
<section class="ot-expertise">
  <div class="wrap">
    <div class="ot-sec-hdr">
      <p class="eyebrow">Dispute resolution expertise</p>
      <h2>Different disputes require different expertise</h2>
      <p>Mediations Australia and its broader network work across the full range of civil, family, and commercial disputes. The right practitioner depends on the nature of your matter.</p>
    </div>
    <div class="ot-exp-grid">

      <a href="/family-law-mediation/" class="ot-exp-card">
        <div class="ot-exp-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 21s-7-4.5-7-10a4 4 0 017-2.6A4 4 0 0119 11c0 5.5-7 10-7 10z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></div>
        <h3>Family &amp; Separation</h3>
        <p>Parenting arrangements, property settlement, consent orders, financial agreements, and the full range of post-separation decisions.</p>
      </a>

      <a href="/workplace-mediation/" class="ot-exp-card">
        <div class="ot-exp-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="4" y="8" width="16" height="12" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M9 8V6a3 3 0 016 0v2" stroke="currentColor" stroke-width="1.6"/></svg></div>
        <h3>Workplace &amp; Employment</h3>
        <p>Bullying, harassment, unfair dismissal, team conflict, discrimination, and workplace relationship breakdowns.</p>
      </a>

      <a href="/commercial-mediation/" class="ot-exp-card">
        <div class="ot-exp-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="3" y="6" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M8 6V4a4 4 0 018 0v2M9 13l2 2 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <h3>Business &amp; Commercial</h3>
        <p>Partnership disputes, contract conflicts, shareholder disagreements, franchise matters, and commercial relationship breakdowns.</p>
      </a>

      <a href="/real-estate-mediation/" class="ot-exp-card">
        <div class="ot-exp-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M3 21h18M5 21V7l7-4 7 4v14" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><rect x="9" y="13" width="6" height="8" rx="1" stroke="currentColor" stroke-width="1.6"/></svg></div>
        <h3>Property &amp; Construction</h3>
        <p>Neighbour disputes, strata conflicts, real estate transaction disputes, construction defects, and co-owner disagreements.</p>
      </a>

      <a href="/estate-dispute-mediation/" class="ot-exp-card">
        <div class="ot-exp-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 9h16M4 9l2-4h12l2 4M4 9v10a1 1 0 001 1h14a1 1 0 001-1V9" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></div>
        <h3>Estates &amp; Inheritance</h3>
        <p>Contesting wills, executor conflicts, inheritance disputes, family provision claims, and estate distribution disagreements.</p>
      </a>

      <a href="/arbitration-in-family-law/" class="ot-exp-card">
        <div class="ot-exp-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></div>
        <h3>Arbitration</h3>
        <p>Where a binding decision is needed but litigation should be avoided — private arbitration for property, financial, and commercial matters.</p>
      </a>

    </div>
  </div>
</section>

<!-- ⑤  MATCHING -->
<section class="ot-matching">
  <div class="wrap">
    <div class="ot-sec-hdr">
      <p class="eyebrow">Finding the right practitioner</p>
      <h2>You don't need to choose a mediator before speaking with us</h2>
      <p>When you contact us, we discuss the matter and identify who is best placed to help. Here's what we consider.</p>
    </div>
    <div class="ot-match-grid" style="margin-top:48px">

      <div class="ot-match-item">
        <div class="ot-match-dot"></div>
        <div>
          <h3>Nature of the dispute</h3>
          <p>Family, workplace, commercial, estate, property — different disputes call for different experience and sometimes different processes.</p>
        </div>
      </div>

      <div class="ot-match-item">
        <div class="ot-match-dot"></div>
        <div>
          <h3>Professional experience</h3>
          <p>We match the practitioner's professional background to the substance of the dispute — not just their general accreditation.</p>
        </div>
      </div>

      <div class="ot-match-item">
        <div class="ot-match-dot"></div>
        <div>
          <h3>Complexity</h3>
          <p>A two-party parenting matter and a multi-party commercial dispute require different approaches. We scale accordingly.</p>
        </div>
      </div>

      <div class="ot-match-item">
        <div class="ot-match-dot"></div>
        <div>
          <h3>Mediation or arbitration</h3>
          <p>For most disputes, mediation is the right starting point. Where a binding decision is needed, arbitration may be more appropriate — we'll explain the difference.</p>
        </div>
      </div>

      <div class="ot-match-item">
        <div class="ot-match-dot"></div>
        <div>
          <h3>Location</h3>
          <p>We operate in person in Sydney, Melbourne, Brisbane, and Perth, and fully online across Australia. We find a format that works.</p>
        </div>
      </div>

      <div class="ot-match-item">
        <div class="ot-match-dot"></div>
        <div>
          <h3>Availability</h3>
          <p>Some matters are urgent. Where timing matters, we work to find a practitioner who can meet your schedule.</p>
        </div>
      </div>

    </div>
    <div style="text-align:center;margin-top:48px">
      <p style="font-size:1rem;color:var(--ink-soft);margin-bottom:20px">Not sure who you need? Start with a conversation.</p>
      <a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1rem;padding:15px 32px">Speak With Our Team →</a>
    </div>
  </div>
</section>

<!-- ⑥  AUSTRALIA-WIDE -->
<section class="ot-aus">
  <div class="wrap">
    <div class="ot-sec-hdr">
      <p class="eyebrow">Australia-wide</p>
      <h2>Dispute resolution wherever you are</h2>
      <p>Mediations Australia operates in person across four major cities and fully online across Australia. Distance is not a barrier to getting the right practitioner for your matter.</p>
    </div>
    <div class="ot-aus-grid">
      <div class="ot-office"><strong>Sydney</strong><span>Suite 508, 41/464–480 Kent St NSW 2000</span></div>
      <div class="ot-office"><strong>Melbourne</strong><span>Level 23, 727 Collins St VIC 3008</span></div>
      <div class="ot-office"><strong>Brisbane</strong><span>Suite 507, 198 Adelaide St QLD 4000</span></div>
      <div class="ot-office"><strong>Perth</strong><span>Level 25, 108 St Georges Tce WA 6000</span></div>
    </div>
    <div style="text-align:center;margin-top:36px">
      <a href="/online-mediation-australia/" class="btn" style="background:var(--sage-deep);color:var(--cream);font-size:.97rem;padding:14px 30px">
        Online mediation — how it works →
      </a>
    </div>
  </div>
</section>

<!-- ⑦  MEDIATION VS ARBITRATION -->
<section class="ot-mva">
  <div class="wrap">
    <div class="ot-sec-hdr">
      <h2>Mediation or arbitration?</h2>
      <p>The right process depends on the dispute. Here's the difference.</p>
    </div>
    <div class="ot-mva-cards">
      <div class="ot-mva-card">
        <h3>Mediation</h3>
        <p>A confidential, structured process in which an independent mediator helps the parties reach their own agreement. You stay in control of the outcome. The mediator decides nothing — they create the conditions for the parties to resolve the dispute themselves.</p>
        <p>Mediation is suitable for most family, workplace, commercial, estate, and property disputes. It is faster, cheaper, and more private than court — and the agreements reached tend to hold because both parties had a hand in making them.</p>
        <a href="/what-is-mediation-in-family-law/" style="font-size:.92rem;font-weight:700;color:var(--sage-deep)">Learn about mediation →</a>
      </div>
      <div class="ot-mva-card">
        <h3>Arbitration</h3>
        <p>A private process in which a qualified arbitrator hears both sides and makes a binding determination — like a private judge, but faster and more flexible than court. The decision is binding and can be registered with the court.</p>
        <p>Arbitration is appropriate where the parties need a definitive decision, cannot reach agreement through mediation, and want to avoid the cost and delay of litigation. In family law, arbitration is available for property and financial matters only.</p>
        <a href="/arbitration-in-family-law/" style="font-size:.92rem;font-weight:700;color:var(--sage-deep)">Learn about arbitration →</a>
      </div>
    </div>
    <div class="ot-mva-sub">
      <p>Not sure which process is appropriate for your dispute?</p>
      <a href="{BOOK_URL}" class="btn btn-primary" style="font-size:.97rem;padding:14px 30px">Book a Free Consultation →</a>
    </div>
  </div>
</section>

<!-- ⑧  FAQ -->
{faq_html(TEAM_FAQ, heading="Common questions about our team", tag="Questions &amp; answers")}

<!-- ⑨  FINAL CTA -->
<section class="cta-band" id="book">
  <div class="wrap">
    <div class="reveal">
      <p class="sec-tag" style="text-align:center;color:var(--sage);opacity:.8;letter-spacing:.1em">NOT SURE WHO YOU NEED?</p>
      <h2>Start with a conversation</h2>
      <p>Tell us about your dispute and we'll explain who is best placed to help, what process makes sense, and what to expect — with no obligation and no commitment.</p>
      <a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Book a Free Consultation →</a>
      <div style="margin-top:20px">
        <a href="{PHONE_HREF}" style="font-size:1rem;color:var(--cream);opacity:.85;text-decoration:none">or call {PHONE}</a>
      </div>
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

d = head("Dan Toombs — Mediator & Founder | Mediations Australia",
         "Dan Toombs — AMDRAS-accredited mediator, award-winning lawyer, Winston Churchill Fellow and former Member of the Guardianship &amp; Administration Tribunal Qld (now QCAT). Founder of Mediations Australia.",
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
        Dan Toombs — <em>Mediator &amp; Founder, Mediations Australia</em>
      </h1>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="mediator-profile">

      <aside class="mediator-photo">
        <img src="/assets/images/Dan-Bio.png"
             alt="Dan Toombs — Founder and Mediator, Mediations Australia"
             width="260" height="320" loading="eager">
        <p style="font-weight:700;font-size:.85rem;letter-spacing:.04em;text-transform:uppercase;color:var(--sage-deep);margin:20px 0 12px">Credentials &amp; Experience</p>
        <table class="cred-table" aria-label="Dan Toombs credentials">
          <tbody>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:4px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Mediation &amp; Dispute Resolution</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px"><a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS</a> Accredited Mediator</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px">Former Member, Guardianship &amp; Administration Tribunal (Qld)</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:10px">(Jurisdiction now within QCAT)</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:8px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Legal</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px">Multi-Award-Winning Lawyer</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:10px">Published by <a href="https://www.thomsonreuters.com.au/en-au.html" target="_blank" rel="noopener">Thomson Reuters</a></td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:8px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Leadership &amp; Governance</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px">Former CEO, Community Legal Centre</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:10px">Former Board Director, <a href="https://www.legalaid.qld.gov.au/" target="_blank" rel="noopener">Legal Aid Queensland</a></td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:8px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">National Recognition</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px"><a href="https://humanrights.gov.au/about-us/what-we-do/human-rights-awards-2026" target="_blank" rel="noopener">National Human Rights Law Award</a></td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:10px">Queensland Disability Award</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:8px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">Behaviour &amp; Leadership</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px"><a href="https://www.belbin.com/" target="_blank" rel="noopener">Accredited Belbin Team Roles Facilitator</a></td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:10px"><a href="https://aali.org.au/" target="_blank" rel="noopener">Adaptive Leadership</a> Training</td></tr>
            <tr><td colspan="2" style="font-weight:700;color:var(--sage-deep);padding-top:8px;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase">International Experience</td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft);padding-bottom:2px"><a href="https://www.churchilltrust.com.au/" target="_blank" rel="noopener">Winston Churchill Fellow</a></td></tr>
            <tr><td colspan="2" style="color:var(--ink-soft)"><a href="https://www.innovatingjustice.org/" target="_blank" rel="noopener">Center for Justice Innovation</a>, New York</td></tr>
          </tbody>
        </table>

      </aside>

      <div class="mediator-content">
        <h2>Dan Toombs — Mediator &amp; Founder, Mediations Australia</h2>
        <span class="tag-line">Award-winning lawyer. Former Member, Guardianship &amp; Administration Tribunal Qld (now QCAT). Nationally accredited mediator. Published author.</span>

        <p>Dan Toombs is the Founder of Mediations Australia and an <a href="https://amdras.au/" target="_blank" rel="noopener">AMDRAS-accredited mediator</a>
        who brings a distinctive perspective to resolving difficult disputes.</p>

        <p>He has experienced disputes from multiple perspectives: as a lawyer, as a former Tribunal
        Member of the Guardianship and Administration Tribunal (Queensland) (jurisdiction now within QCAT), as an organisational leader, and now as a mediator. That experience has taught
        him that disputes are rarely about the legal issues alone. Relationships, personalities,
        commercial pressures, organisational dynamics and entrenched positions can all determine whether
        a conflict escalates or finds a way forward.</p>

        <p>Dan's approach is to understand what is really keeping a dispute stuck, test what is driving
        the parties' positions, and create the conditions for a practical and enduring resolution.</p>

        <p><em>Because unresolved conflict rarely stands still.</em></p>

        <p>Legal costs increase. Management time is consumed. Relationships deteriorate. Workplace culture
        can suffer. Positions harden. And the longer a dispute continues, the more time and money can be
        spent pursuing an outcome neither party can predict with certainty.</p>

        <p>Mediation offers an opportunity to change that trajectory — while the parties still have
        control over the outcome.</p>

        <h3>Understanding Disputes from the Decision-Maker's Perspective</h3>
        <p>Dan is a multi-award-winning lawyer published by
        <a href="https://www.thomsonreuters.com.au/en-au.html" target="_blank" rel="noopener">Thomson Reuters</a>
        and a former Member of the Guardianship and Administration Tribunal (Queensland) — the jurisdiction
        now within QCAT — where he presided over and determined numerous matters.</p>

        <p>That experience gives him a perspective relatively few mediators possess. He understands the
        difference between how strongly a party may believe in its position and how that position may
        ultimately be assessed by an independent decision-maker. Confidence in a case and certainty of
        outcome are not the same thing.</p>

        <p>Once a dispute is handed to a tribunal or court, someone else decides. Evidence may be
        interpreted differently than expected. Witnesses may perform differently under scrutiny. Legal
        arguments may not carry the weight anticipated. And even a successful outcome can come after
        considerable expenditure of time, money and energy.</p>

        <p>Mediation gives the parties an opportunity to realistically assess those risks — and explore
        an outcome they control rather than having one imposed upon them.</p>

        <h3>Navigating Complexity and Competing Interests</h3>
        <p>Dan's legal career has included complex disputes, legislative reform, access to justice and
        organisational leadership. He helped drive significant legislative reform in Australia that
        improved outcomes for people with mental health and intellectual disabilities caught in the
        criminal justice system — work recognised with the <strong>Queensland Disability Award</strong>.</p>

        <p>Achieving systemic change of this kind required much more than technical legal knowledge. It
        required navigating complex legislative and policy environments, understanding competing
        perspectives, building relationships across institutions, overcoming entrenched positions and
        creating a pathway towards meaningful and enduring change.</p>

        <p>Those same capabilities are central to mediation. The issue being argued about is not always
        the whole problem. Dan looks at the legal issues alongside the interests, relationships,
        organisational pressures and human dynamics beneath the conflict to understand what is preventing
        progress — and where movement may be possible.</p>

        <h3>Understanding People and Organisations</h3>
        <p>Conflict between people can quickly become a problem for an entire organisation. Trust
        deteriorates. Communication becomes defensive. Managers are drawn in. Colleagues take sides.
        Productivity suffers. Good people disengage. What began as a disagreement between two people can
        begin affecting the culture and performance of a wider team.</p>

        <p>Dan has specialist training in behaviour, leadership and team dynamics. He is an
        <a href="https://www.belbin.com/" target="_blank" rel="noopener">Accredited Belbin Team Roles Facilitator</a>
        and has trained in
        <a href="https://aali.org.au/" target="_blank" rel="noopener">Adaptive Leadership</a> through the
        Australian Adaptive Leadership Institute, based on the framework developed at Harvard University.</p>

        <p>He also understands organisational conflict from the perspective of someone who has actually
        led an organisation. Dan served as CEO of one of Australia's largest community legal centres and
        as a Board Director of
        <a href="https://www.legalaid.qld.gov.au/" target="_blank" rel="noopener">Legal Aid Queensland</a>,
        with responsibility spanning people, strategy, governance, organisational culture and difficult
        decisions.</p>

        <p>Today, alongside his mediation practice, Dan is Director of
        <a href="https://www.practiceproof.com/" target="_blank" rel="noopener">Practice Proof</a>,
        working with law firms and legal professionals across Australia. This keeps him closely connected
        to the commercial, leadership and organisational realities facing professional firms. He
        understands not only how disputes arise inside organisations, but something equally important:
        the environment people may need to return to once the mediation is over.</p>

        <h3>National and International Recognition</h3>
        <p>Dan's work has been recognised nationally and internationally. He is the recipient of the
        <a href="https://humanrights.gov.au/about-us/what-we-do/human-rights-awards-2026" target="_blank" rel="noopener">National Human Rights Law Award</a>,
        a <a href="https://www.churchilltrust.com.au/" target="_blank" rel="noopener">Winston Churchill Fellow</a>,
        and has worked with the
        <a href="https://www.innovatingjustice.org/" target="_blank" rel="noopener">Center for Justice Innovation</a>
        in New York on innovative responses to complex justice and social problems.</p>

        <p>Across that work runs a consistent theme: bringing different perspectives together, navigating
        complexity and finding practical ways through difficult problems. It is that experience Dan
        brings to the mediation room.</p>

        <h3>The Cost of Leaving a Dispute Unresolved</h3>
        <p>By the time mediation is being considered, a dispute may already have consumed significant
        time, money and attention. The more important question is: what will it cost if nothing changes?</p>

        <p>More legal fees. More management time. More uncertainty. More stress. More damage to commercial
        relationships or workplace culture. And potentially months or years pursuing an outcome that will
        ultimately be determined by someone else.</p>

        <p>As a former Member of the Guardianship and Administration Tribunal (Queensland) — the jurisdiction now within QCAT — who has presided over and determined disputes, Dan understands
        first-hand that adjudication necessarily involves uncertainty. Mediation offers a different path.
        It creates a structured and independent environment in which the parties can clarify what really
        matters, test assumptions and positions, realistically assess the alternatives to settlement, and
        explore solutions that may not have emerged through negotiation alone.</p>

        <p>Dan brings together four perspectives in that process: the analytical discipline of a lawyer,
        the perspective of a former Tribunal Member (Guardianship &amp; Administration Tribunal Qld, now QCAT), the practical judgment of an experienced
        organisational leader, and the independence of a mediator. The aim is not agreement at any cost.
        It is a resolution that is practical, workable and capable of enduring after the mediation
        is over.</p>

        <h3>Take Back Control of the Dispute</h3>
        <p>Conflict has a way of gathering momentum. The longer it continues, the more money, time and
        emotion become invested in it — and the harder it can become for either side to change course.</p>

        <p>Mediation provides an opportunity to interrupt that trajectory. You do not need to know how the
        dispute will be resolved before you start. You need to decide whether continuing down the current
        path is likely to produce a better outcome.</p>

        <p>If a <a href="/workplace-mediation/">workplace</a>,
        <a href="/commercial-mediation/">business or commercial</a> dispute is consuming time, money or
        management attention — or beginning to affect important relationships, people or workplace culture
        — there is value in exploring mediation before the cost of the conflict grows further.</p>

        <p>Speak confidentially with Dan about what is happening, what is at stake, and whether mediation
        can provide a practical way forward.</p>

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

<section>
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

<section>
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
