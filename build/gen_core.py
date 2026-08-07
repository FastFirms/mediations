#!/usr/bin/env python3
"""Generate core pages: About, Contact, How Mediation Works, Preparing for Mediation."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF, OFFICES, DOMAIN,
                       SERVICES, SERVICE_GROUPS, contact_form_fields)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
      <a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
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
doc += phero("A clearer path through a difficult time",
 "How Mediation Works",
 "No jargon, no surprises. Mediation is a structured conversation led by a neutral, accredited mediator who helps everyone reach an agreement — and you decide whether to accept it. Here's exactly what happens, from first call to binding outcome.",
 [("Home",""),("How Mediation Works",None)])
doc += '<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> Mediation is a structured negotiation led by a neutral, accredited mediator who helps everyone reach their own agreement. Unlike a judge, the mediator imposes nothing — you stay in control. It typically resolves in one to two sessions, costs a fraction of court, and the agreement can be made legally binding.</p></div></div>'
doc += """<article class="body"><div class="wrap-narrow reveal">
<h2>The five steps of mediation</h2>
<ol>
  <li><strong>Book your consultation.</strong> You start with a free initial consultation — clear advice on your options and whether mediation suits your matter, with no runaway costs and no obligation.</li>
  <li><strong>Our own mediators.</strong> You work directly with a nationally accredited mediator from our team who understands both the legal framework and the human side of your dispute.</li>
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

<h2>Face-to-face, online, and shuttle mediation</h2>
<p>Mediation isn't one-size-fits-all. There are three common formats, and the right one depends on your situation:</p>
<ul>
  <li><strong>Face-to-face mediation</strong> — both parties sit in the same room with the mediator. Best when communication is workable and both parties are comfortable being together.</li>
  <li><strong>Online mediation</strong> — conducted over video call, with the mediator managing the session remotely. Just as effective as in-person for most matters, and far more convenient if parties are in different cities.</li>
  <li><strong>Shuttle mediation</strong> — parties are in separate rooms (or separate video calls) and the mediator moves between them. Used where direct contact is uncomfortable, where there is a history of conflict, or where one party finds the other intimidating. <a href="/shuttle-mediation-guide/">See how shuttle mediation works →</a></li>
</ul>

<h2>What kinds of disputes can be mediated?</h2>
<p>Mediation works across a wide range of disputes. The most common matters handled include:</p>
<ul>
  <li><a href="/family-law-mediation/">Family law disputes</a> — separation, parenting arrangements, property and financial agreements</li>
  <li><a href="/workplace-mediation/">Workplace disputes</a> — grievances, performance disputes, team breakdowns</li>
  <li><a href="/property-settlement-mediation/">Property and financial settlements</a> — asset division, consent orders, binding financial agreements</li>
  <li>Estate and succession disputes — contested wills, executor disputes, family provision claims</li>
  <li>Commercial and business disputes — partnership breakdowns, contract disagreements, neighbour disputes</li>
</ul>

<h2>What happens if no agreement is reached?</h2>
<p>Mediation is voluntary and confidential. If the session does not produce agreement, you are free to pursue other options — including court. For parenting matters, the mediator will issue a <a href="/section-60i-certificates/">Section 60I certificate</a> confirming that family dispute resolution was attempted, which is required before applying to court. Nothing said in mediation can be used as evidence if the matter proceeds to litigation — confidentiality is protected by law. <a href="/mediate-or-litigate/">Compare mediation and court →</a></p>
</div></article>"""
doc += faq_html(qa_how, heading="How mediation works — FAQs")
doc += cta_band("Ready to take the <em>first step</em>?",
 "Book a free initial consultation and we'll explain exactly how mediation would work for your situation — with no obligation.")
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
doc += phero("We exist because the courts fail most people",
 "About Mediations Australia",
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
 "Book a free initial consultation and find out why thousands of Australians chose mediation over litigation.")
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
doc += phero("Go in prepared — it makes a real difference",
 "Preparing for Mediation",
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
 "Book a free initial consultation and we'll walk you through exactly what to expect, so you arrive prepared and confident.")
doc += "</main>" + page_end()
write("preparing-for-mediation", doc)

# ============================================================
# CONTACT
# ============================================================
office_cards = "".join(f"""<article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 21s-7-4.5-7-10a7 7 0 0114 0c0 5.5-7 10-7 10z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="11" r="2.5" stroke="currentColor" stroke-width="1.6"/></svg></div>
<h3>{esc(c)}</h3><p>{esc(a)}</p></article>""" for c, a in OFFICES)

doc = head(
 "Contact Mediations Australia | 1800 952 380",
 "Book a free initial consultation with Mediations Australia. Offices in Sydney, Melbourne, Brisbane and Perth, plus online mediation nationwide.",
 "contact-us",
 extra_schema=[org_schema(),
               breadcrumb_schema([("Home",""),("Contact","contact-us")])])
doc += nav()
_contact_form = contact_form_fields(prefix="c", subject="New contact — Mediations Australia")
doc += f"""<main id="main">
{crumb_html([("Home",""),("Contact",None)])}

<section style="background:var(--sand);padding:72px 0 80px">
<style>
.contact-wrap{{display:grid;grid-template-columns:1fr 380px;gap:64px;align-items:start}}
.contact-field{{width:100%;padding:13px 16px;border:1.5px solid var(--line);border-radius:10px;font-size:1rem;background:var(--cream);color:var(--ink);font-family:var(--sans);box-sizing:border-box;outline:none;transition:border-color .2s}}
.contact-field:focus{{border-color:var(--sage-deep)}}
@media(max-width:860px){{.contact-wrap{{grid-template-columns:1fr}}.contact-sidebar{{display:none}}}}
</style>
<div class="wrap">
  <div class="contact-wrap">

    <div>
      <p class="sec-tag">Get in touch</p>
      <h1 style="font-family:var(--serif);font-size:clamp(2.2rem,5vw,3.4rem);line-height:1.15;margin-bottom:16px">Let's talk about <em>resolving it</em>.</h1>
      <p style="font-size:1.05rem;color:var(--ink-soft);max-width:54ch;margin-bottom:36px">Tell us about your dispute and we'll give you an honest view of whether mediation can help — and how it fits with any legal advice you already have.</p>

      <form id="contact-form" novalidate style="display:flex;flex-direction:column;gap:16px">
        {_contact_form}
        <p style="font-size:.85rem;color:var(--ink-soft);margin:0">No obligation. We'll respond within one business day.</p>
      </form>

      <div style="display:flex;gap:28px;flex-wrap:wrap;margin-top:36px;padding-top:32px;border-top:1px solid var(--line);align-items:center">
        <a href="{PHONE_HREF}" style="display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-weight:600;font-size:1.05rem">
          <span style="width:40px;height:40px;border-radius:50%;background:var(--sage-light);display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--sage-deep)">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none"><path d="M6.6 10.8a15.2 15.2 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          {PHONE}
        </a>
        <span style="color:var(--ink-soft);font-size:.92rem">Mon–Fri, 8:30am–5:30pm AEST</span>
      </div>
    </div>

    <div class="contact-sidebar" style="position:sticky;top:100px">
      <div style="background:var(--sage-deep);border-radius:20px;overflow:hidden;color:var(--cream)">
        <img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia"
          style="width:100%;height:260px;object-fit:cover;object-position:center 15%;display:block">
        <div style="padding:28px">
          <p style="font-family:var(--serif);font-size:1.25rem;margin-bottom:4px">Dan Toombs</p>
          <p style="font-size:.85rem;opacity:.75;margin-bottom:16px">Founder &amp; Mediator</p>
          <p style="font-size:.95rem;line-height:1.72;opacity:.92;margin-bottom:22px;font-style:italic">"We built Mediations Australia because most disputes don't need a courtroom — they need a skilled mediator and a structured process. Tell us what's happening and we'll be honest about whether we can help."</p>
          <div style="display:flex;flex-direction:column;gap:9px;font-size:.88rem;opacity:.88">
            <span>✓ Free initial consultation</span>
            <span>✓ Confidential &amp; no obligation</span>
            <span>✓ Nationally accredited mediators</span>
            <span>✓ In person or online</span>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>
</section>

<section class="sec reveal" style="padding-top:64px;padding-bottom:64px">
  <div class="wrap">
    <p class="sec-tag">Our offices</p>
    <h2 class="sec-title" style="margin-bottom:36px">Find us across <em>Australia</em>.</h2>
    <div class="cards">{office_cards}</div>
    <p style="margin-top:26px;color:var(--ink-soft);max-width:60ch">Can't make it to an office? Our <a href="/online-mediation-australia/" style="color:var(--sage-deep);text-decoration:underline">online mediation</a> is available anywhere in Australia, including regional and remote areas.</p>
  </div>
</section>"""

doc += cta_band("Take the <em>first step</em> today.",
 "The first conversation costs nothing but a phone call. Tell us what you're facing and we'll tell you honestly how mediation can help.", note=True)
doc += "</main>" + page_end()
doc += """<script>
document.getElementById('contact-form').addEventListener('submit',async function(e){
  e.preventDefault();
  var btn=this.querySelector('button[type=submit]');
  btn.disabled=true;btn.textContent='Sending…';
  var data=new FormData(this);
  try{
    var r=await fetch('https://formspree.io/f/xwvgjnve',{method:'POST',body:data,headers:{Accept:'application/json'}});
    if(r.ok){window.location.href='/thank-you/';}
    else{btn.disabled=false;btn.innerHTML='Book a Free Consultation <span class="arr">→</span>';alert('Something went wrong. Please try again or call us directly.');}
  }catch(err){btn.disabled=false;btn.innerHTML='Book a Free Consultation <span class="arr">→</span>';alert('Something went wrong. Please try again or call us directly.');}
});
</script>"""
write("contact-us", doc)

# ── Thank You ────────────────────────────────────────────────────────────────
doc = head(
 "Thank You | Mediations Australia",
 "We've received your enquiry and will be in touch very shortly.",
 "thank-you",
 extra_schema=[org_schema(), breadcrumb_schema([("Home",""),("Thank You","thank-you")])])
doc += nav()
doc += f"""<main id="main">
{crumb_html([("Home",""),("Thank You",None)])}
<section style="background:var(--sand);padding:80px 0 100px;min-height:60vh;display:flex;align-items:center">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 400px;gap:64px;align-items:center;max-width:960px;margin:0 auto">

      <div>
        <span style="display:inline-block;width:56px;height:56px;border-radius:50%;background:var(--sage-light);display:flex;align-items:center;justify-content:center;margin-bottom:24px">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5" stroke="var(--sage-deep)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <h1 style="font-family:var(--serif);font-size:clamp(2.2rem,5vw,3.4rem);line-height:1.15;margin-bottom:20px">We've received <em>your message.</em></h1>
        <p style="font-size:1.15rem;color:var(--ink-soft);line-height:1.75;max-width:50ch;margin-bottom:28px">Thank you for reaching out. We'll be in contact very promptly — typically within a few hours during business hours.</p>
        <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:36px">
          <div style="display:flex;align-items:center;gap:12px;font-size:1rem">
            <span style="width:8px;height:8px;border-radius:50%;background:var(--sage-deep);flex-shrink:0"></span>
            One of our mediators will review your enquiry personally
          </div>
          <div style="display:flex;align-items:center;gap:12px;font-size:1rem">
            <span style="width:8px;height:8px;border-radius:50%;background:var(--sage-deep);flex-shrink:0"></span>
            We'll give you an honest view of whether mediation can help
          </div>
          <div style="display:flex;align-items:center;gap:12px;font-size:1rem">
            <span style="width:8px;height:8px;border-radius:50%;background:var(--sage-deep);flex-shrink:0"></span>
            No obligation — just a straightforward conversation
          </div>
        </div>
        <div style="display:flex;gap:16px;flex-wrap:wrap">
          <a href="/" class="btn btn-primary">Back to home <span class="arr">→</span></a>
          <a href="{PHONE_HREF}" class="btn btn-ghost">{PHONE}</a>
        </div>
      </div>

      <div style="background:var(--sage-deep);border-radius:24px;overflow:hidden;color:var(--cream)">
        <img src="/assets/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia"
          style="width:100%;height:280px;object-fit:cover;object-position:center 15%;display:block">
        <div style="padding:28px 30px">
          <p style="font-family:var(--serif);font-size:1.2rem;margin-bottom:4px">Dan Toombs</p>
          <p style="font-size:.85rem;opacity:.72;margin-bottom:16px">Founder &amp; Mediator</p>
          <p style="font-size:.95rem;line-height:1.72;opacity:.92;font-style:italic">"Every enquiry is reviewed personally. We'll be in touch shortly and give you a straight answer about how we can help."</p>
        </div>
      </div>

    </div>
  </div>
</section>
<style>
@media(max-width:700px){{
  .ty-grid{{grid-template-columns:1fr!important}}
  .ty-sidebar{{display:none}}
}}
</style>
</main>""" + page_end()
write("thank-you", doc)

# ============================================================
# HOW WE HELP
# ============================================================
svc_lookup = {s: (n, d) for s, n, d in SERVICES}

# Additional services not in SERVICES list
extra_services = [
    ("accredited-family-law-mediators", "Our Mediators", "Nationally accredited, FDRP-registered practitioners"),
    ("divorce-counselling", "Divorce Counselling", "Emotional support alongside legal resolution"),
    ("online-mediation-australia", "Online Mediation", "Mediate from anywhere in Australia"),
]

qa_hwh = [
    ("What types of disputes can Mediations Australia resolve?",
     "We resolve family law disputes (separation, parenting, property), workplace disputes, estate and inheritance conflicts, de facto relationship matters, and online mediation for parties anywhere in Australia. If you're unsure whether your matter suits mediation, book a free initial consultation and we'll advise honestly."),
    ("Do I need a lawyer to use your services?",
     "No. A lawyer is not required to attend mediation, though legal advice beforehand is often helpful for complex matters. Many of our mediators are also experienced lawyers, so legal insight is already in the room."),
    ("How quickly can we get a mediation session?",
     "For most matters we aim to complete intake and schedule a session within two to three weeks of first contact. Where urgency is required — for example, a time-critical parenting or property matter — we can often move faster."),
    ("Is mediation legally binding?",
     "Mediation itself is voluntary and confidential, but the agreements reached can be formalised into legally binding outcomes — consent orders through the court, binding financial agreements (BFAs), or deeds of settlement. Your mediator will explain which option suits your matter."),
    ("Can you help with matters outside the major cities?",
     "Yes. We offer online mediation across all of Australia, including regional and remote areas. For in-person sessions, we have offices in Sydney, Melbourne, Brisbane, and Perth."),
    ("What is the difference between mediation and arbitration?",
     "In mediation, you and the other party shape your own agreement — nothing is imposed. In arbitration, an arbitrator hears both sides and makes a binding decision, like a private judge. Mediation keeps control in your hands and is almost always the better first step for family and workplace disputes."),
]

# SVG icons keyed by slug — reuse homepage icon set
ICONS = {
    "family-law-mediation":         '<path d="M12 2C9.79 2 8 3.79 8 6s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 12c-5.33 0-8 2.67-8 4v2h16v-2c0-1.33-2.67-4-8-4z" fill="currentColor"/>',
    "divorce-mediation":            '<path d="M12 2a10 10 0 100 20A10 10 0 0012 2zm1 14.93V17a1 1 0 00-2 0v-.07A8.001 8.001 0 014.07 11H5a1 1 0 000-2h-.93A8.001 8.001 0 0111 4.07V5a1 1 0 002 0v-.93A8.001 8.001 0 0119.93 9H19a1 1 0 000 2h.93A8.001 8.001 0 0113 16.93z" fill="currentColor"/>',
    "property-settlement-mediation":'<rect x="4" y="8" width="16" height="12" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M9 8V6a3 3 0 016 0v2" stroke="currentColor" stroke-width="1.6"/>',
    "parenting-plan-mediation":     '<path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z" fill="currentColor"/>',
    "section-60i-certificates":     '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "financial-agreements-mediation":'<path d="M12 1v22M17 5H9.5a3.5 3.5 0 100 7h5a3.5 3.5 0 110 7H6" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    "spousal-support-mediation":    '<path d="M12 21.593c-5.63-5.539-11-10.297-11-14.402C1 3.08 3.71 1 6.5 1c1.973 0 3.963.75 5.5 2.3C13.537 1.75 15.527 1 17.5 1 20.29 1 23 3.08 23 7.191c0 4.105-5.37 8.863-11 14.402z" fill="currentColor"/>',
    "child-support-mediation":      '<path d="M12 2C9.79 2 8 3.79 8 6s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 10c-4 0-8 2-8 4v2h16v-2c0-2-4-4-8-4z" fill="currentColor"/>',
    "de-facto-mediation":           '<path d="M4 4h16a2 2 0 012 2v12a2 2 0 01-2 2H4a2 2 0 01-2-2V6a2 2 0 012-2z" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M22 6l-10 7L2 6" stroke="currentColor" stroke-width="1.6" fill="none"/>',
    "grandparents-mediation":       '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    "consent-orders":               '<path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "online-divorce":               '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/>',
    "workplace-mediation":          '<path d="M20 7H4a2 2 0 00-2 2v10a2 2 0 002 2h16a2 2 0 002-2V9a2 2 0 00-2-2z" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="currentColor" stroke-width="1.6" fill="none"/>',
    "belbin-team-roles-training":   '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    "estate-dispute-mediation":     '<path d="M4 9h16M4 9l2-4h12l2 4M4 9v10a1 1 0 001 1h14a1 1 0 001-1V9" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/>',
    "accredited-family-law-mediators":'<path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
    "divorce-counselling":          '<path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "online-mediation-australia":   '<path d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
}
DEFAULT_ICON = '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M12 8v4l3 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" fill="none"/>'

def make_card(slug, name, desc):
    icon = ICONS.get(slug, DEFAULT_ICON)
    return f"""<article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none">{icon}</svg></div><h3>{esc(name)}</h3><p>{esc(desc)}</p><a class="more" href="/{slug}/">{esc(name)} <span class="arr">→</span></a></article>"""

# Page-specific grouping — differs from SERVICE_GROUPS (which drives the nav megamenu)
# Estate and workplace get their own section here
HWH_GROUPS = [
    ("Family & separation", ["family-law-mediation", "divorce-mediation", "online-divorce", "de-facto-mediation"]),
    ("Property & finances", ["property-settlement-mediation", "financial-agreements-mediation", "spousal-support-mediation", "consent-orders"]),
    ("Parenting", ["parenting-plan-mediation", "child-support-mediation", "section-60i-certificates", "grandparents-mediation"]),
    ("Estate & workplace disputes", ["estate-dispute-mediation", "workplace-mediation", "belbin-team-roles-training"]),
]

group_html = ""
for group_name, slugs in HWH_GROUPS:
    cards = "".join(make_card(s, *svc_lookup[s]) for s in slugs if s in svc_lookup)
    group_html += f"""<div class="hwh-group">
  <h2 class="hwh-group-title">{esc(group_name)}</h2>
  <div class="cards">{cards}</div>
</div>"""

extra_cards = "".join(make_card(s, name, desc) for s, name, desc in extra_services)
group_html += f"""<div class="hwh-group">
  <h2 class="hwh-group-title">Supporting services</h2>
  <div class="cards">{extra_cards}</div>
</div>"""

hwh_styles = """<style>
.hwh-intro{max-width:680px;margin:0 auto 48px;text-align:center}
.hwh-group{margin:0 0 52px}
.hwh-group-title{font-size:.9rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-soft);margin:0 0 18px;padding-bottom:10px;border-bottom:1px solid var(--line)}
.hwh-why{background:var(--sage-light);border-radius:var(--r);padding:40px 44px;margin:48px 0}
.hwh-why h2{margin-top:0;margin-bottom:24px}
.hwh-why-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px 36px}
.hwh-why-grid div{display:flex;flex-direction:column;gap:4px}
.hwh-why-grid strong{font-size:1rem;font-weight:700;color:var(--ink)}
.hwh-why-grid span{font-size:.92rem;color:var(--ink-soft);line-height:1.5}
@media(max-width:640px){.hwh-why{padding:28px 24px}.hwh-why-grid{grid-template-columns:1fr}}
</style>"""

doc = head(
    "How We Help | Mediation Services — Mediations Australia",
    "Mediation services for family law, property, parenting, workplace, estate and de facto disputes. Accredited mediators, fixed fees, Australia-wide. Free consultation.",
    "how-we-help",
    extra_schema=[
        org_schema(),
        breadcrumb_schema([("Home", ""), ("How We Help", "how-we-help")]),
        article_schema("How We Help — Mediation Services", "All mediation and dispute resolution services offered by Mediations Australia."),
        faq_schema(qa_hwh),
    ]
)
doc += nav()
doc += phero(
    "Every dispute type we resolve",
    "How We Help",
    "Mediations Australia resolves family law, property, parenting, workplace, estate, and de facto disputes through accredited mediation. Browse every service area below, or book a free consultation and we'll point you to the right one.",
    [("Home", ""), ("How We Help", None)]
)
doc += f"""<div class="wrap">
{hwh_styles}
<div class="hwh-intro">
  <p>We resolve disputes — privately, efficiently, and without court — across the full range of family, workplace, and civil matters. Every mediator is nationally accredited. Every service comes with a free initial consultation.</p>
</div>
{group_html}
<div class="hwh-why reveal">
  <h2>Why resolve it through mediation?</h2>
  <div class="hwh-why-grid">
    <div><strong>Cheaper.</strong><span>Litigation runs $30,000–$150,000 per side. Mediation resolves most disputes for a fraction of that.</span></div>
    <div><strong>Faster.</strong><span>Court takes one to three years. Most matters resolve in a single 1-day session.</span></div>
    <div><strong>Confidential.</strong><span>Nothing reaches the public record. What's said in mediation is protected by law.</span></div>
    <div><strong>You decide.</strong><span>No outcome is imposed. Agreements you shape yourself are more likely to hold — and be liveable.</span></div>
  </div>
  <p style="margin:24px 0 0"><a href="/how-mediation-works/">See exactly how the process works →</a></p>
</div>
</div>"""
doc += faq_html(qa_hwh, heading="Common questions about our services")
doc += cta_band(
    "Not sure which service fits your situation?",
    "Book a free 20-minute consultation and we'll tell you exactly which pathway makes sense — with no obligation."
)
doc += "</main>" + page_end()
write("how-we-help", doc)

print("Core pages built: how-mediation-works, about, preparing-for-mediation, contact-us, thank-you, how-we-help")
