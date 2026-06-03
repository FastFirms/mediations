#!/usr/bin/env python3
"""Four pages that were in the original URL inventory but not yet built:
   /our-mediators/  /memberships/  /mediation-podcast/  /books/
All built with proper structure + on-brand copy + clearly-marked placeholders
where firm-specific facts would otherwise be invented."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)
OUT = "/home/claude/mediations/site"

# ====================================================================
# OUR MEDIATORS
# ====================================================================
title = "Our Mediators | Nationally Accredited Family Mediators"
desc = "Meet the nationally accredited mediators at Mediations Australia. Many are also experienced family lawyers, with deep expertise in family, property and workplace disputes."
schema = [org_schema(), breadcrumb_schema([("Home",""),("Our Mediators","our-mediators")])]
d = head(title, desc, "our-mediators", extra_schema=schema) + nav()
d += f"""<main id="main">
{crumb_html([("Home",""),("Our Mediators",None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Our team</span>
<h1>Our Mediators — <em>accredited, experienced, lawyer-aware</em>.</h1>
<p class="lede">Every mediator at Mediations Australia is nationally accredited under AMDRAS. Many are also experienced family lawyers — so the legal realities of your matter are understood from the very first conversation.</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>

<section class="sec"><div class="wrap-narrow">
<h2>What sets our mediators apart</h2>
<p>Our mediators combine three things that matter when you're working through a separation or dispute: <strong>accreditation</strong> (every one of them is nationally recognised under the Australian Mediator and Dispute Resolution Accreditation Standards), <strong>legal awareness</strong> (many are practising or formerly-practising family lawyers, so they understand exactly what a court would do with your matter), and <strong>resolution focus</strong> (their job isn't to take sides — it's to help you reach an agreement that holds up).</p>

<p>That combination is unusual. Many mediators don't have legal training; many family lawyers don't have mediation training. Bringing both together is the difference between a process that wanders and one that gets to a fair, durable outcome quickly.</p>

<div class="callout"><h3>Nationally Accredited Mediators</h3>
<p>AMDRAS accreditation requires formal training, supervised practice, and ongoing professional development. It's the recognised national standard for mediators in Australia, and it's the bar every one of our mediators meets.</p></div>

<!-- ========================================================== -->
<!-- TEAM PROFILE PLACEHOLDERS                                   -->
<!-- ========================================================== -->
<!-- Replace these with real team profiles. For each mediator:    -->
<!--   - Name                                                    -->
<!--   - Photo (square, ~400px, alt text with their name)         -->
<!--   - Role / specialisation (e.g. "Family Law Mediator")       -->
<!--   - Short bio (2-3 sentences)                                -->
<!--   - Qualifications (NMAS, FDRP, law degree, etc.)            -->
<!-- Each profile should also have its own Person JSON-LD schema  -->
<!-- for E-E-A-T strength.                                        -->
<!-- ========================================================== -->

<h2 style="margin-top:50px">Meet the team</h2>
<p style="background:rgba(198,106,63,.08);border-left:3px solid var(--terra);padding:18px 22px;border-radius:8px;color:var(--ink-soft);font-size:.95rem"><strong>Note for the team:</strong> this section is awaiting team profiles. Add each mediator's name, photo, role, short bio and qualifications below using the template structure in the source HTML.</p>

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:24px;margin-top:30px">
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:24px">
    <div style="width:100%;aspect-ratio:1;background:var(--sage-light);border-radius:10px;margin-bottom:18px;display:flex;align-items:center;justify-content:center;color:var(--sage-deep);font-style:italic;font-size:.9rem">Photo placeholder</div>
    <h3 style="margin-bottom:4px;font-size:1.2rem">[Mediator Name]</h3>
    <p style="color:var(--sage-deep);font-weight:600;font-size:.92rem;margin-bottom:10px">[Role / Specialisation]</p>
    <p style="font-size:.95rem;color:var(--ink-soft);margin-bottom:12px">[Short 2–3 sentence bio describing their background, what they specialise in, and the kinds of matters they handle.]</p>
    <p style="font-size:.85rem;color:var(--ink-soft);font-style:italic">[Qualifications, e.g. NMAS Accredited Mediator, Family Dispute Resolution Practitioner, LLB]</p>
  </article>
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:24px">
    <div style="width:100%;aspect-ratio:1;background:var(--sage-light);border-radius:10px;margin-bottom:18px;display:flex;align-items:center;justify-content:center;color:var(--sage-deep);font-style:italic;font-size:.9rem">Photo placeholder</div>
    <h3 style="margin-bottom:4px;font-size:1.2rem">[Mediator Name]</h3>
    <p style="color:var(--sage-deep);font-weight:600;font-size:.92rem;margin-bottom:10px">[Role / Specialisation]</p>
    <p style="font-size:.95rem;color:var(--ink-soft);margin-bottom:12px">[Short bio]</p>
    <p style="font-size:.85rem;color:var(--ink-soft);font-style:italic">[Qualifications]</p>
  </article>
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:24px">
    <div style="width:100%;aspect-ratio:1;background:var(--sage-light);border-radius:10px;margin-bottom:18px;display:flex;align-items:center;justify-content:center;color:var(--sage-deep);font-style:italic;font-size:.9rem">Photo placeholder</div>
    <h3 style="margin-bottom:4px;font-size:1.2rem">[Mediator Name]</h3>
    <p style="color:var(--sage-deep);font-weight:600;font-size:.92rem;margin-bottom:10px">[Role / Specialisation]</p>
    <p style="font-size:.95rem;color:var(--ink-soft);margin-bottom:12px">[Short bio]</p>
    <p style="font-size:.85rem;color:var(--ink-soft);font-style:italic">[Qualifications]</p>
  </article>
</div>

<h2 style="margin-top:50px">Qualifications &amp; standards</h2>
<p>Our mediators hold qualifications that include:</p>
<ul>
  <li><strong>National Mediator Accreditation</strong> (NMAS) under AMDRAS</li>
  <li><strong>Family Dispute Resolution Practitioner (FDRP)</strong> registration, where applicable, for matters requiring a Section 60I certificate</li>
  <li><strong>Legal qualifications</strong> (LLB or JD) for those mediators who are also practising or formerly-practising lawyers</li>
  <li><strong>Specialist training</strong> in areas such as high-conflict mediation, child-inclusive practice, and complex financial matters</li>
</ul>
<p>Continuing professional development is a requirement of accreditation — our mediators stay current with developments in family law (including the 2025 Family Law Act reforms), best practice in dispute resolution, and emerging issues around family violence and child welfare. <a href="/changes-to-family-law-act-2025/">See the 2025 Family Law Act changes →</a></p>

<h2>Working with your lawyer</h2>
<p>If you already have a lawyer, our mediators work alongside them — not against them. Many of the people we help are referred to us by the very solicitors advising them, because experienced family lawyers know what years of litigation costs in money and wellbeing. If you don't have a lawyer, that's fine too — many of our clients work directly with us and use mediation as the path to a fair, binding agreement. <a href="/collaborative-family-lawyers/">See collaborative family lawyers →</a></p>
</div></section>
"""
d += cta_band("Ready to work with an <em>accredited mediator</em>?",
              "Book a fixed-fee consultation and we'll match you with a mediator suited to your matter.")
d += "</main>" + page_end()
os.makedirs(os.path.join(OUT,"our-mediators"), exist_ok=True)
open(os.path.join(OUT,"our-mediators","index.html"),"w").write(d)
print("our-mediators built")

# ====================================================================
# MEMBERSHIPS
# ====================================================================
title = "Memberships &amp; Accreditations | Mediations Australia"
desc = "Mediations Australia mediators are nationally accredited under AMDRAS and hold memberships with leading mediation, family law and dispute resolution bodies in Australia."
schema = [org_schema(), breadcrumb_schema([("Home",""),("Memberships","memberships")])]
d = head(title, desc, "memberships", extra_schema=schema) + nav()
d += f"""<main id="main">
{crumb_html([("Home",""),("Memberships",None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Accreditation &amp; standards</span>
<h1>Memberships &amp; Accreditations — <em>the standards we uphold</em>.</h1>
<p class="lede">Our mediators meet — and exceed — the national standards for dispute resolution in Australia. Below are the bodies and frameworks that hold us accountable.</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>

<section class="sec"><div class="wrap-narrow">
<h2>National accreditation</h2>
<p>Every mediator at Mediations Australia is nationally accredited under the <strong>Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS)</strong>. AMDRAS is the recognised national framework for mediators in Australia, requiring formal training, supervised practice, a code of conduct, and ongoing professional development.</p>

<p>For more on the standard, see the <a href="https://msb.org.au/" target="_blank" rel="noopener">Mediator Standards Board</a>, the independent body that maintains the framework.</p>

<div class="callout"><h3>Why accreditation matters</h3>
<p>Mediation is a powerful but unregulated word — anyone can call themselves a mediator. Accreditation under AMDRAS means a mediator has been formally trained, assessed, and is bound by an enforceable code of conduct. It's the difference between a recognised professional and someone with a website.</p></div>

<h2>Family Dispute Resolution Practitioner (FDRP)</h2>
<p>For parenting matters that may proceed to court, mediators must be registered as Family Dispute Resolution Practitioners (FDRPs) to issue the <a href="/section-60i-certificates/">Section 60I certificate</a> the court requires. Our FDRPs are registered under the framework administered by the <a href="https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution" target="_blank" rel="noopener">Attorney-General's Department</a>.</p>

<!-- ========================================================== -->
<!-- ADDITIONAL MEMBERSHIPS PLACEHOLDER                          -->
<!-- ========================================================== -->
<!-- Add the firm's actual additional memberships and             -->
<!-- accreditations here. Common bodies family-law mediation      -->
<!-- practices belong to include:                                 -->
<!--   - Resolution Institute                                     -->
<!--   - Law Society of NSW / Vic / Qld / WA (where mediators     -->
<!--     are also practising solicitors)                          -->
<!--   - Family Law Section of the Law Council of Australia       -->
<!--   - Australian Institute of Family Law Arbitrators and       -->
<!--     Mediators (AIFLAM)                                       -->
<!-- For each one, add: logo (or list item), name, what it is,    -->
<!--                    and link to the body's own site.          -->
<!-- ========================================================== -->

<h2>Additional memberships</h2>
<p style="background:rgba(198,106,63,.08);border-left:3px solid var(--terra);padding:18px 22px;border-radius:8px;color:var(--ink-soft);font-size:.95rem"><strong>Note for the team:</strong> list the firm's other professional memberships here (e.g. Resolution Institute, Law Society memberships for mediator-lawyers, AIFLAM, Family Law Section of the Law Council of Australia, etc.). For each, name the body and link to its website.</p>

<ul>
  <li><strong>[Membership name]</strong> — [Brief description of the body and what membership signifies]. <a href="#">[Body website]</a></li>
  <li><strong>[Membership name]</strong> — [Description]. <a href="#">[Body website]</a></li>
  <li><strong>[Membership name]</strong> — [Description]. <a href="#">[Body website]</a></li>
</ul>

<h2>Code of conduct &amp; ethics</h2>
<p>All accredited mediators in Australia are bound by the <strong>Practice Standards</strong> that accompany AMDRAS — covering impartiality, confidentiality, competence, and the avoidance of conflicts of interest. These standards protect you as a client and give you a clear basis for raising any concern about how mediation has been conducted.</p>

<h2>Continuing professional development</h2>
<p>Accreditation isn't a one-off achievement — it requires ongoing learning. Our mediators complete continuing professional development each year to stay current with family law reform (including the substantial changes that took effect in 2024–2025), evolving best practice in dispute resolution, and emerging considerations around family violence and child welfare.</p>
</div></section>
"""
d += cta_band("Work with an <em>accredited</em> mediator.",
              "Book a consultation with a mediator who meets — and exceeds — the national standards.")
d += "</main>" + page_end()
os.makedirs(os.path.join(OUT,"memberships"), exist_ok=True)
open(os.path.join(OUT,"memberships","index.html"),"w").write(d)
print("memberships built")

# ====================================================================
# MEDIATION PODCAST
# ====================================================================
title = "Mediation Podcast | Mediations Australia"
desc = "Listen to the Mediations Australia podcast — practical conversations on mediation, family law, separation, and resolving disputes without court. Free to stream."
schema = [org_schema(), breadcrumb_schema([("Home",""),("Podcast","mediation-podcast")])]
d = head(title, desc, "mediation-podcast", extra_schema=schema) + nav()
d += f"""<main id="main">
{crumb_html([("Home",""),("Podcast",None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Listen &amp; learn</span>
<h1>The Mediations Australia Podcast — <em>conversations on resolution</em>.</h1>
<p class="lede">Practical, accessible conversations on mediation, separation and family law — for people navigating it now, and for the professionals who work alongside them.</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>

<section class="sec"><div class="wrap-narrow">

<!-- ========================================================== -->
<!-- PODCAST LISTENING LINKS PLACEHOLDER                         -->
<!-- ========================================================== -->
<!-- Replace the # placeholders below with the actual show URLs   -->
<!-- on each platform once available. If the podcast no longer    -->
<!-- exists, delete this whole page and remove the link from the  -->
<!-- nav/footer/sitemap.                                          -->
<!-- ========================================================== -->

<h2>Listen wherever you find your podcasts</h2>
<p style="background:rgba(198,106,63,.08);border-left:3px solid var(--terra);padding:18px 22px;border-radius:8px;color:var(--ink-soft);font-size:.95rem"><strong>Note for the team:</strong> add the real podcast URLs below (Spotify, Apple Podcasts, Google Podcasts, RSS) once confirmed. If the podcast is no longer active, delete this page rather than leave it stale.</p>

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin-top:24px">
  <a href="#" style="background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:20px;text-decoration:none;color:var(--ink);font-weight:600;text-align:center;transition:transform .3s,box-shadow .3s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='var(--shadow)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
    <div style="font-size:1.6rem;margin-bottom:6px">▶</div>Spotify
  </a>
  <a href="#" style="background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:20px;text-decoration:none;color:var(--ink);font-weight:600;text-align:center">
    <div style="font-size:1.6rem;margin-bottom:6px">▶</div>Apple Podcasts
  </a>
  <a href="#" style="background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:20px;text-decoration:none;color:var(--ink);font-weight:600;text-align:center">
    <div style="font-size:1.6rem;margin-bottom:6px">▶</div>YouTube
  </a>
  <a href="#" style="background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:20px;text-decoration:none;color:var(--ink);font-weight:600;text-align:center">
    <div style="font-size:1.6rem;margin-bottom:6px">▶</div>RSS
  </a>
</div>

<h2 style="margin-top:50px">What we talk about</h2>
<ul>
  <li>How mediation actually works — what to expect at each stage</li>
  <li>The realities of separation: property, parenting and the financial side</li>
  <li>Mediating in high-conflict situations</li>
  <li>Recent family law reforms and what they mean for separating couples</li>
  <li>Conversations with mediators, family lawyers and other professionals</li>
</ul>

<h2>Episodes</h2>
<p style="background:rgba(198,106,63,.08);border-left:3px solid var(--terra);padding:18px 22px;border-radius:8px;color:var(--ink-soft);font-size:.95rem"><strong>Note for the team:</strong> add episode cards below — title, guest, date, short description, and the platform links. For SEO, also consider adding a transcript per episode (Google indexes transcripts and they help discovery).</p>

<div style="display:flex;flex-direction:column;gap:16px;margin-top:24px">
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:24px">
    <span style="background:var(--sage-light);color:var(--sage-deep);padding:4px 12px;border-radius:100px;font-size:.78rem;font-weight:600">Episode [#]</span>
    <h3 style="margin:10px 0 6px;font-size:1.2rem">[Episode title]</h3>
    <p style="color:var(--ink-soft);font-size:.9rem;margin-bottom:10px">[Date] · [Guest, if any] · [Duration]</p>
    <p style="color:var(--ink-soft);font-size:.98rem">[Episode description — 2–3 sentences describing what's covered.]</p>
  </article>
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:24px">
    <span style="background:var(--sage-light);color:var(--sage-deep);padding:4px 12px;border-radius:100px;font-size:.78rem;font-weight:600">Episode [#]</span>
    <h3 style="margin:10px 0 6px;font-size:1.2rem">[Episode title]</h3>
    <p style="color:var(--ink-soft);font-size:.9rem;margin-bottom:10px">[Date] · [Duration]</p>
    <p style="color:var(--ink-soft);font-size:.98rem">[Description]</p>
  </article>
</div>

<h2 style="margin-top:50px">Prefer to read?</h2>
<p>Many of the topics covered in the podcast are also written up in depth in our <a href="/guides/">free guides library</a> — 42 comprehensive articles on mediation, family law, property settlement, parenting, and more.</p>
</div></section>
"""
d += cta_band("Listening is great — <em>talking</em> is better.",
              "When you're ready to talk about your situation, book a free, confidential consultation.")
d += "</main>" + page_end()
os.makedirs(os.path.join(OUT,"mediation-podcast"), exist_ok=True)
open(os.path.join(OUT,"mediation-podcast","index.html"),"w").write(d)
print("mediation-podcast built")

# ====================================================================
# BOOKS
# ====================================================================
title = "Books on Mediation &amp; Family Law | Mediations Australia"
desc = "Books and recommended reading on mediation, separation, and family law in Australia. Authored and curated by the team at Mediations Australia."
schema = [org_schema(), breadcrumb_schema([("Home",""),("Books","books")])]
d = head(title, desc, "books", extra_schema=schema) + nav()
d += f"""<main id="main">
{crumb_html([("Home",""),("Books",None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Reading list</span>
<h1>Books on Mediation &amp; Family Law — <em>further reading</em>.</h1>
<p class="lede">Books we've written, contributed to, and recommend — for people going through separation, professionals working in the field, and anyone curious about a better way to resolve disputes.</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>

<section class="sec"><div class="wrap-narrow">

<!-- ========================================================== -->
<!-- BOOKS PLACEHOLDER                                           -->
<!-- ========================================================== -->
<!-- Replace this section with actual books authored or           -->
<!-- recommended by the firm. For each book, include:             -->
<!--   - Cover image (alt text with title + author)               -->
<!--   - Title and author                                         -->
<!--   - Publication year                                         -->
<!--   - Short summary (2-4 sentences)                            -->
<!--   - Where to buy (link to bookstore, publisher, or Amazon)   -->
<!-- Consider Book JSON-LD schema for each one.                   -->
<!-- If the firm has no books and doesn't plan to curate, delete  -->
<!-- this page and remove from nav/footer/sitemap.                -->
<!-- ========================================================== -->

<h2>Books from our team</h2>
<p style="background:rgba(198,106,63,.08);border-left:3px solid var(--terra);padding:18px 22px;border-radius:8px;color:var(--ink-soft);font-size:.95rem"><strong>Note for the team:</strong> populate the cards below with real books authored or contributed to by the firm. If the firm has no published books, consider either deleting this page (and the nav/footer links to it) or repurposing it as a "Recommended Reading" curated list.</p>

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:24px;margin-top:30px">
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:24px">
    <div style="width:100%;aspect-ratio:2/3;background:var(--sage-light);border-radius:8px;margin-bottom:18px;display:flex;align-items:center;justify-content:center;color:var(--sage-deep);font-style:italic;font-size:.9rem">Book cover</div>
    <h3 style="margin-bottom:4px;font-size:1.15rem">[Book Title]</h3>
    <p style="color:var(--sage-deep);font-size:.9rem;margin-bottom:10px">[Author] · [Year]</p>
    <p style="font-size:.95rem;color:var(--ink-soft);margin-bottom:14px">[Short summary — 2–4 sentences on what the book covers and who it's for.]</p>
    <a href="#" class="btn btn-ghost" style="font-size:.9rem;padding:10px 18px">Where to buy →</a>
  </article>
  <article style="background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:24px">
    <div style="width:100%;aspect-ratio:2/3;background:var(--sage-light);border-radius:8px;margin-bottom:18px;display:flex;align-items:center;justify-content:center;color:var(--sage-deep);font-style:italic;font-size:.9rem">Book cover</div>
    <h3 style="margin-bottom:4px;font-size:1.15rem">[Book Title]</h3>
    <p style="color:var(--sage-deep);font-size:.9rem;margin-bottom:10px">[Author] · [Year]</p>
    <p style="font-size:.95rem;color:var(--ink-soft);margin-bottom:14px">[Summary]</p>
    <a href="#" class="btn btn-ghost" style="font-size:.9rem;padding:10px 18px">Where to buy →</a>
  </article>
</div>

<h2 style="margin-top:50px">Free in-depth guides</h2>
<p>If you're not ready to buy a book but want substantive, well-researched material on mediation and family law, our <a href="/guides/">guides library</a> contains 42 free in-depth articles covering separation, property settlement, parenting, financial agreements, and more. Each one is written by the same team responsible for this firm's mediation work.</p>
</div></section>
"""
d += cta_band("Reading is a great start — <em>talking is better</em>.",
              "When you're ready to talk about your own situation, book a free, confidential consultation.")
d += "</main>" + page_end()
os.makedirs(os.path.join(OUT,"books"), exist_ok=True)
open(os.path.join(OUT,"books","index.html"),"w").write(d)
print("books built")
