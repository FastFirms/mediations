#!/usr/bin/env python3
"""Generate core pages: About, Contact, How Mediation Works, Preparing for Mediation."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF, OFFICES, DOMAIN)

OUT = "/home/claude/mediations/site"

def write(slug, doc):
    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)

def phero(eyebrow, h1, lede, crumb):
    return f"""<main id="main">
{crumb_html(crumb)}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""

# ============================================================
# HOW MEDIATION WORKS
# ============================================================
qa_how = [
 ("How long does mediation take?",
  "Most disputes resolve in one to two sessions, often within a single day, compared with court matters that can run for one to three years."),
 ("What happens if we don't reach agreement?",
  "Even a partial agreement narrows the issues and saves time and cost if you proceed to court. You remain free to take the matter further, and any Section 60I certificate needed for parenting matters can be issued."),
 ("Is mediation confidential?",
  "Yes. Mediation is conducted on a 'without prejudice' basis, meaning what's said generally can't be used later in court. That confidentiality is what lets everyone speak openly."),
 ("Do I need a lawyer at mediation?",
  "No. A lawyer isn't required, though legal advice can help in complex matters. Many of our mediators are also experienced lawyers, so legal insight is already in the room."),
]
doc = head(
 "How Mediation Works in Australia | The Process, Step by Step",
 "A clear, step-by-step guide to how mediation works in Australia — from booking a consultation to a legally binding agreement. Faster and cheaper than court.",
 "how-mediation-works",
 extra_schema=[org_schema(),
               breadcrumb_schema([("Home",""),("How Mediation Works","how-mediation-works")]),
               article_schema("How Mediation Works in Australia","A step-by-step guide to the mediation process."),
               faq_schema(qa_how)])
doc += nav()
doc += phero("The mediation process",
 "How mediation works, <em>step by step</em>.",
 "No jargon, no surprises. Mediation is a structured conversation led by a neutral, accredited mediator who helps everyone reach an agreement — and you decide whether to accept it. Here's exactly what happens, from first call to binding outcome.",
 [("Home",""),("How Mediation Works",None)])
doc += '<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> Mediation is a structured negotiation led by a neutral, accredited mediator who helps everyone reach their own agreement. Unlike a judge, the mediator imposes nothing — you stay in control. It typically resolves in one to two sessions, costs a fraction of court, and the agreement can be made legally binding.</p></div></div>'
doc += """<article class="body"><div class="wrap-narrow reveal">
<h2>The five steps of mediation</h2>
<ol>
  <li><strong>Book your consultation.</strong> You start with a fixed-fee consultation — clear advice on your options and whether mediation suits your matter, with no runaway costs and no obligation.</li>
  <li><strong>We match your mediator.</strong> You're paired with a nationally accredited mediator who understands both the legal framework and the human side of your dispute.</li>
  <li><strong>The session runs.</strong> In person or online, together in one room or in separate rooms with the mediator moving between you ('shuttle' mediation) — whatever feels safe and productive.</li>
  <li><strong>Agreement is reached.</strong> In around 90% of the matters we mediate, the dispute resolves then and there, on terms everyone has chosen.</li>
  <li><strong>We make it binding.</strong> Your agreement is formalised into an enforceable outcome — <a href="/consent-orders/">consent orders</a>, a <a href="/financial-agreements-mediation/">binding financial agreement</a>, or a deed of settlement.</li>
</ol>

<h2>What is mediation, exactly?</h2>
<p>Mediation is a form of alternative dispute resolution where a neutral third party helps people in conflict reach their own agreement. The mediator doesn't take sides, give legal advice, or decide who's right — their role is to manage the conversation, defuse tension, and help both sides find common ground. It's used across <a href="/family-law-mediation/">family</a>, <a href="/workplace-mediation/">workplace</a>, commercial, property and estate disputes.</p>

<h2>What's the difference between mediation and arbitration?</h2>
<p>In mediation, you and the other party reach your own agreement — nothing is imposed. In arbitration, an arbitrator hears both sides and makes a binding decision, more like a private judge. Mediation keeps control in your hands, which is why it's usually the better first step.</p>

<div class="callout">
  <h3>Mediation is encouraged by every court in Australia</h3>
  <p>Mediation is actively supported across the Australian justice system, including the Federal Circuit and Family Court of Australia. For most parenting matters, attempting it first is a legal requirement, not just a recommendation.</p>
</div>

<h2>Why does mediation work when conversations have failed?</h2>
<p>Because structure changes everything. A skilled mediator creates a safe, neutral space, keeps discussions focused on solutions rather than blame, and helps each person feel genuinely heard. That's why mediation resolves disputes that direct conversation couldn't. <a href="/preparing-for-mediation/">Learn how to prepare for your session →</a></p>
</div></article>"""
doc += faq_html(qa_how, heading="How mediation works — FAQs")
doc += cta_band("Ready to take the <em>first step</em>?",
 "Book a fixed-fee consultation and we'll explain exactly how mediation would work for your situation — with no obligation.")
doc += "</main>" + page_end()
write("how-mediation-works", doc)

# ============================================================
# ABOUT
# ============================================================
qa_about = [
 ("Are your mediators nationally accredited?",
  "Yes. Our mediators are accredited under the Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS), the national benchmark for mediator accreditation in Australia."),
 ("Are your mediators also lawyers?",
  "Many are. Our team brings together nationally accredited mediators and experienced family lawyers, so the legal realities of your matter are understood from the start."),
 ("Where do you offer mediation?",
  "We have offices in Sydney, Melbourne, Brisbane and Perth, and offer online mediation across all of Australia, including regional and remote areas."),
 ("What types of disputes do you handle?",
  "We resolve family law, property, workplace, commercial, estate and personal injury disputes — across the full spectrum of dispute resolution."),
]
doc = head(
 "About Mediations Australia | Dispute Resolution Specialists",
 "Nationally accredited mediators and experienced family lawyers resolving disputes faster, fairer and without court, Australia-wide. Call 1800 952 380.",
 "about-mediations-australia",
 extra_schema=[org_schema(),
               breadcrumb_schema([("Home",""),("About","about-mediations-australia")]),
               faq_schema(qa_about)])
doc += nav()
doc += phero("About us",
 "We believe the way disputes are resolved is <em>broken</em>. So we fixed it.",
 "Mediations Australia exists because litigation fails most people who enter it — slower, costlier and more painful than it needs to be. We bring together nationally accredited mediators and experienced family lawyers with one shared philosophy: resolve early, resolve fairly, and keep people out of court wherever possible.",
 [("Home",""),("About",None)])
doc += '<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> Mediations Australia is a national dispute resolution firm of nationally accredited mediators and experienced family lawyers. We help individuals, families and businesses resolve disputes faster and at a fraction of the cost of court, with offices in Sydney, Melbourne, Brisbane and Perth, and online mediation Australia-wide.</p></div></div>'
doc += """<article class="body"><div class="wrap-narrow reveal">
<h2>Why we exist</h2>
<p>Australia's courts are overwhelmed with litigation, and the people inside that system pay the price — in time, in money, and in stress. In family law especially, when matters become adversarial they tend to grow more complicated, more emotionally charged and far more expensive. Sometimes court is genuinely unavoidable, and a good lawyer will tell you when. But for the vast majority of disputes, there's a better first step.</p>
<p>That conviction is why Mediations Australia was founded. We're early-resolution focused, and our mediators and lawyers share that same philosophy.</p>

<h2>Who we are</h2>
<p>We bring together practitioners experienced across every facet of dispute resolution — nationally accredited mediators, family lawyers and arbitrators. That blend matters: it means we understand both how to guide a productive conversation and what the legal realities of your matter actually are.</p>

<div class="callout">
  <h3>Nationally accredited under AMDRAS</h3>
  <p>Our mediators are accredited under the Australian Mediator and Dispute Resolution Accreditation Standards — the national benchmark. With a 90% resolution rate across thousands of matters, our approach works.</p>
</div>

<h2>How we work with your lawyer</h2>
<p>We're not here to replace good legal advice — we work alongside it. Many of the people we help are referred to us by the very solicitors advising them, because experienced lawyers know that mediation usually serves their clients better than a courtroom. If you already have a lawyer, we'll work with them. If you don't, many of our mediators are lawyers themselves.</p>

<h2>What we resolve</h2>
<p>From the deeply personal to the purely commercial: <a href="/family-law-mediation/">family separation</a>, <a href="/property-settlement-mediation/">property settlements</a>, <a href="/workplace-mediation/">workplace conflict</a>, business disputes, contested estates and personal injury claims. Whatever the matter, our goal is the same — a practical, lasting resolution that keeps you out of court.</p>
</div></article>"""
doc += faq_html(qa_about, heading="About Mediations Australia — FAQs")
doc += cta_band("See the difference for <em>yourself</em>.",
 "Book a fixed-fee consultation and find out why thousands of Australians chose mediation over litigation.")
doc += "</main>" + page_end()
write("about-mediations-australia", doc)

# ============================================================
# PREPARING FOR MEDIATION
# ============================================================
qa_prep = [
 ("What should I bring to a mediation session?",
  "Bring any relevant documents (financial records for property matters, a list of issues you want to cover, and any proposals you've considered), plus an open mind and a focus on outcomes rather than blame."),
 ("How should I prepare emotionally for mediation?",
  "Acknowledge that it may be difficult, focus on your goals rather than past grievances, and consider what you genuinely need versus what you'd merely prefer. A clear sense of priorities helps enormously."),
 ("Can I bring a support person?",
  "Often yes, depending on the type of mediation. Discuss it beforehand so suitable arrangements can be made that keep the process balanced and productive."),
 ("What if I'm worried about facing the other person?",
  "Tell us in advance. 'Shuttle' mediation keeps you in separate rooms with the mediator moving between you, so you never have to be face to face."),
]
doc = head(
 "Preparing for Mediation | What to Expect & How to Get Ready",
 "How to prepare for mediation: what to bring, how to think about your goals, and what to expect on the day. A practical guide from accredited mediators.",
 "preparing-for-mediation",
 extra_schema=[org_schema(),
               breadcrumb_schema([("Home",""),("Preparing for Mediation","preparing-for-mediation")]),
               article_schema("Preparing for Mediation","A practical guide to getting ready for a mediation session."),
               faq_schema(qa_prep)])
doc += nav()
doc += phero("Resources",
 "Preparing for mediation: <em>everything you need to know</em>.",
 "Walking into mediation prepared makes a real difference to the outcome. This practical guide covers what to bring, how to think about what you want, and exactly what to expect on the day — so you arrive calm, clear and ready to resolve things.",
 [("Home",""),("Resources",None),("Preparing for Mediation",None)])
doc += '<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> To prepare for mediation, get clear on your goals and priorities, gather any relevant documents, think about realistic outcomes rather than positions, and arrive ready to focus on solutions instead of blame. Good preparation is one of the biggest predictors of a successful mediation.</p></div></div>'
doc += """<article class="body"><div class="wrap-narrow reveal">
<h2>What is mediation, and why prepare?</h2>
<p>Mediation is a collaborative process where you and the other parties work together, with a neutral mediator, to reach an agreement. Because <em>you</em> shape the outcome, the effort you put in beforehand directly affects what you walk away with. Preparation turns a stressful unknown into a process you can steer.</p>

<h2>Before the day: get clear on your goals</h2>
<ul>
  <li>Separate what you genuinely <strong>need</strong> from what you'd merely <strong>prefer</strong>.</li>
  <li>Think about the other person's likely concerns — understanding them helps you find solutions.</li>
  <li>Consider realistic outcomes, not just your opening position.</li>
  <li>Jot down the key issues you want to cover so nothing gets missed.</li>
</ul>

<h2>What to bring</h2>
<ul>
  <li>Relevant documents — for property matters, financial records, valuations and statements.</li>
  <li>A written list of the issues and any proposals you've thought about.</li>
  <li>For parenting matters, a sense of the arrangements that would work for your children.</li>
</ul>

<div class="callout">
  <h3>If you're anxious about facing the other person</h3>
  <p>That's completely normal — and easily managed. Tell us in advance and we can run 'shuttle' mediation, keeping you in separate rooms with the mediator moving between you. You never have to be face to face.</p>
</div>

<h2>On the day: how to get the best outcome</h2>
<p>Focus on the future, not on re-litigating the past. Listen as much as you speak. Stay open to creative solutions you hadn't considered — mediation often produces options a court never could. And remember the mediator is neutral: they're there to help everyone reach agreement, not to judge.</p>

<h2>A note on safety</h2>
<p>If your situation involves family violence or concerns about safety, mediation may not be appropriate, and other steps may be needed first. If you're in a crisis or immediate danger, contact emergency services. Tell us about any safety concerns in your consultation and we'll advise the right path. <a href="/section-60i-certificates/">Some matters qualify for exemptions →</a></p>
</div></article>"""
doc += faq_html(qa_prep, heading="Preparing for mediation — FAQs")
doc += cta_band("Feel ready. <em>Resolve it.</em>",
 "Book a fixed-fee consultation and we'll walk you through exactly what to expect, so you arrive prepared and confident.")
doc += "</main>" + page_end()
write("preparing-for-mediation", doc)

# ============================================================
# CONTACT
# ============================================================
office_cards = "".join(f"""<article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 21s-7-4.5-7-10a7 7 0 0114 0c0 5.5-7 10-7 10z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="11" r="2.5" stroke="currentColor" stroke-width="1.6"/></svg></div>
<h3>{esc(c)}</h3><p>{esc(a)}</p></article>""" for c, a in OFFICES)

doc = head(
 "Contact Mediations Australia | Book a Consultation · 1800 952 380",
 "Contact Mediations Australia to book a mediation consultation. Offices in Sydney, Melbourne, Brisbane and Perth, plus online mediation Australia-wide. Call 1800 952 380.",
 "contact-us",
 extra_schema=[org_schema(),
               breadcrumb_schema([("Home",""),("Contact","contact-us")])])
doc += nav()
doc += phero("Get in touch",
 "Let's talk about <em>resolving it</em>.",
 "Tell us about your dispute and we'll give you an honest view of whether mediation can help — and how it fits with any legal advice you already have. Call us, book online, or reach out and we'll come back to you quickly.",
 [("Home",""),("Contact",None)])
doc += f"""<section class="sec" style="padding-top:20px"><div class="wrap">
<div class="reveal" style="display:flex;gap:18px;flex-wrap:wrap;margin-bottom:50px">
  <a href="{PHONE_HREF}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 36px">Call {PHONE} <span class="arr">→</span></a>
  <a href="{BOOK_URL}" class="btn btn-ghost" style="font-size:1.1rem;padding:18px 36px">Book online</a>
</div>
<div class="reveal">
  <p class="sec-tag">Our offices</p>
  <h2 class="sec-title" style="margin-bottom:30px">Find us across <em>Australia</em>.</h2>
  <div class="cards">{office_cards}</div>
  <p style="margin-top:26px;color:var(--ink-soft);max-width:60ch">Can't make it to an office? Our <a href="/online-divorce/" style="color:var(--sage-deep);text-decoration:underline">online mediation</a> is available anywhere in Australia, including regional and remote areas.</p>
</div>
</div></section>"""
doc += cta_band("Take the <em>first step</em> today.",
 "The first conversation costs nothing but a phone call. Tell us what you're facing and we'll tell you honestly how mediation can help.", note=True)
doc += "</main>" + page_end()
write("contact-us", doc)

print("Core pages built: how-mediation-works, about, preparing-for-mediation, contact-us")
