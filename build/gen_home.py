#!/usr/bin/env python3
"""Rebuild homepage + family law page on the shared design/template system."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pre-launch staging guard: the homepage is intentionally kept out of search
# indexes while the site is on the staging domain. head() always emits
# "index, follow", so we force the homepage back to noindex on every build to
# avoid silently exposing staging. REMOVE this guard at launch (set to False)
# when the homepage should be indexable on the production domain.
HOMEPAGE_NOINDEX = os.environ.get("MED_HOMEPAGE_INDEX") != "1"

def write(slug, doc):
    if slug == "":
        path = OUT
        if HOMEPAGE_NOINDEX:
            doc = doc.replace(
                '<meta name="robots" content="index, follow, max-image-preview:large">',
                '<meta name="robots" content="noindex, nofollow">')
    else:
        path = os.path.join(OUT, slug); os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)

# SVG helpers
X = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" stroke="rgba(251,248,242,.4)" stroke-width="1.5"/><path d="M7 7l6 6M13 7l-6 6" stroke="rgba(251,248,242,.6)" stroke-width="1.5" stroke-linecap="round"/></svg>'
TICK = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" stroke="#a8c89f" stroke-width="1.5"/><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ============================================================
# HOMEPAGE
# ============================================================
qa_home = [
 ("What is mediation, and how is it different from going to court?",
  "Mediation is a structured negotiation led by a neutral, accredited mediator who helps everyone reach an agreement. Unlike a judge, the mediator imposes nothing — you stay in control of the outcome. It's faster, far cheaper, and completely private."),
 ("Do I need a lawyer to attend mediation?",
  "No — a lawyer isn't required to mediate. Legal advice before or after can be wise for complex matters, and many of our mediators are also experienced lawyers, so legal insight is already in the room."),
 ("How much does mediation cost?",
  "You begin with a fixed-fee consultation, so there are no billing surprises. Mediation typically costs a fraction of litigation, and parties usually share the fee. Most disputes resolve in one to two sessions rather than years of court."),
 ("How long does mediation take?",
  "Most disputes are resolved within one to two sessions — often in a single day — compared with court matters that can run for one to three years."),
 ("Is everything discussed in mediation confidential?",
  "Yes. Mediation is conducted on a 'without prejudice' basis, meaning what's said generally can't be used later in court. That confidentiality is exactly what lets everyone speak openly and reach a deal."),
 ("Can a mediation agreement be made legally binding?",
  "Yes. Once you reach agreement it can be formalised into a legally enforceable outcome — through consent orders, a binding financial agreement or court-approved documents. We handle that process for you."),
]

doc = head(
 "Mediation Australia | Resolve Any Dispute Before It Reaches Court",
 "Nationally accredited mediators resolve family, business, workplace and estate disputes faster and without court — 90% success rate. Book a free consultation.",
 "",
 extra_schema=[org_schema(),
               {"@type":"WebSite","@id":f"{DOMAIN}/#website","url":f"{DOMAIN}/",
                "name":"Mediations Australia","publisher":{"@id":f"{DOMAIN}/#organization"}},
               faq_schema(qa_home)])
doc += nav()
doc += f"""<main id="main">
<section class="hero" style="padding:clamp(56px,9vw,116px) 0 clamp(64px,8vw,104px);overflow:hidden;position:relative">
  <div class="phero-blob" style="width:480px;height:480px;top:-140px;right:-120px;opacity:.5"></div>
  <div class="phero-blob" style="width:380px;height:380px;bottom:-160px;left:-100px;opacity:.4;background:#f0d9c8"></div>
  <div class="wrap" style="position:relative;z-index:2">
    <span class="eyebrow reveal-load d1"><span class="pulse"></span>Nationally accredited mediators · 90% success rate</span>
    <h1 class="reveal-load d2" style="font-size:clamp(2.6rem,6.4vw,5rem);max-width:15ch;margin-bottom:24px">Most disputes never need a <em>courtroom.</em></h1>
    <p class="lede reveal-load d3" style="font-size:clamp(1.1rem,1.7vw,1.32rem);color:var(--ink-soft);max-width:56ch;margin-bottom:36px">Whether it's a family separation, a business breakdown or a contested estate, mediation can resolve it faster, for less, and with you in control. Often it's the first step your own lawyer would recommend — and we work alongside them, not instead of them.</p>
    <div class="phero-cta reveal-load d4">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="/how-mediation-works/" class="btn btn-ghost">See how it works</a>
    </div>
    <div class="stats reveal-load d5" style="margin-top:50px">
      <div class="stat"><span class="num"><em>90%</em></span><div class="lbl">resolved at mediation</div></div>
      <div class="stat"><span class="num">Days</span><div class="lbl">not years in court</div></div>
      <div class="stat"><span class="num">100%</span><div class="lbl">you choose the outcome</div></div>
    </div>
  </div>
</section>

<section class="sec reveal" style="background:var(--ink);color:var(--cream);border-radius:38px;margin:0 16px" aria-labelledby="wedge-h">
  <div class="wrap">
    <div style="text-align:center;max-width:60ch;margin:0 auto 50px">
      <h2 id="wedge-h" style="font-size:clamp(2rem,4vw,3.2rem);color:var(--cream);margin-bottom:16px">Two ways through a dispute.<br>One is almost always <em style="font-style:italic;color:#e0a87f">quicker.</em></h2>
      <p style="color:rgba(251,248,242,.72);font-size:1.1rem">Sometimes court is genuinely necessary — and a good lawyer will tell you when. But for most disputes, mediation gets you there sooner, for less, and with far less strain. Here's the honest comparison.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr auto 1fr;gap:0;align-items:stretch;max-width:920px;margin:0 auto" class="compare">
      <div style="padding:36px 32px;opacity:.92">
        <h3 style="font-size:1.45rem;margin-bottom:22px;color:var(--cream)">The court path</h3>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:15px">
          <li style="display:flex;gap:12px;color:var(--cream)">{X}1–3 years of waiting and uncertainty</li>
          <li style="display:flex;gap:12px;color:var(--cream)">{X}Tens or hundreds of thousands in fees</li>
          <li style="display:flex;gap:12px;color:var(--cream)">{X}A judge decides the outcome, not you</li>
          <li style="display:flex;gap:12px;color:var(--cream)">{X}Adversarial by design — harder on relationships</li>
          <li style="display:flex;gap:12px;color:var(--cream)">{X}Public record, on the court's calendar</li>
        </ul>
      </div>
      <div style="width:1px;background:linear-gradient(180deg,transparent,rgba(251,248,242,.18),transparent);position:relative" class="divider">
        <span style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--terra);color:var(--cream);width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:var(--serif);font-style:italic;font-size:1.1rem">vs</span>
      </div>
      <div style="padding:36px 32px">
        <h3 style="font-size:1.45rem;margin-bottom:22px;color:#a8c89f">Mediation first</h3>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:15px">
          <li style="display:flex;gap:12px">{TICK}Resolved in days — often a single session</li>
          <li style="display:flex;gap:12px">{TICK}A fraction of the cost, fixed-fee to start</li>
          <li style="display:flex;gap:12px">{TICK}You design the outcome you can live with</li>
          <li style="display:flex;gap:12px">{TICK}Collaborative — relationships can be preserved</li>
          <li style="display:flex;gap:12px">{TICK}Completely private and confidential</li>
        </ul>
      </div>
    </div>
    <div style="text-align:center;margin-top:46px">
      <p style="font-size:1.2rem;font-family:var(--serif);font-style:italic;color:var(--cream);max-width:52ch;margin:0 auto 26px">"Court has its place — but it's rarely the best place to start. Trying mediation first can save everyone time, money and stress, whatever happens next."</p>
      <a href="{BOOK_URL}" class="btn btn-primary">Start with a free consultation <span class="arr">→</span></a>
    </div>
  </div>
</section>

<section class="sec" id="how">
  <div class="wrap">
    <div class="reveal">
      <p class="sec-tag">How mediation works</p>
      <h2 class="sec-title">A calm, clear path to <em>agreement</em>.</h2>
      <p class="sec-intro">No jargon, no surprises. A neutral, accredited mediator guides everyone toward a solution — and you decide whether to accept it.</p>
    </div>
    <div class="cards reveal" style="margin-top:50px;grid-template-columns:repeat(auto-fit,minmax(210px,1fr))">
      <article class="card"><h3 style="font-family:var(--serif);color:var(--sage);font-size:2rem;opacity:.5">01</h3><h3>Book your consult</h3><p>Start with a fixed-fee consultation. Clear advice, no runaway costs, no obligation.</p></article>
      <article class="card"><h3 style="font-family:var(--serif);color:var(--sage);font-size:2rem;opacity:.5">02</h3><h3>Meet your mediator</h3><p>Paired with an accredited specialist who understands the law and the human side.</p></article>
      <article class="card"><h3 style="font-family:var(--serif);color:var(--sage);font-size:2rem;opacity:.5">03</h3><h3>The session runs</h3><p>In person or online, together or in separate rooms — whatever feels right.</p></article>
      <article class="card"><h3 style="font-family:var(--serif);color:var(--sage);font-size:2rem;opacity:.5">04</h3><h3>Agreement reached</h3><p>Around 90% of matters resolve then and there, on terms you've chosen.</p></article>
      <article class="card"><h3 style="font-family:var(--serif);color:var(--sage);font-size:2rem;opacity:.5">05</h3><h3>Made binding</h3><p>We turn your agreement into an enforceable outcome — consent orders or a contract.</p></article>
    </div>
    <div class="reveal" style="margin-top:30px"><a href="/how-mediation-works/" class="btn btn-ghost">Read the full process <span class="arr">→</span></a></div>
  </div>
</section>

<section class="sec" id="disputes" style="padding-top:0">
  <div class="wrap">
    <div class="reveal">
      <p class="sec-tag">What we resolve</p>
      <h2 class="sec-title">If there's a dispute, there's a <em>better way</em> through it.</h2>
      <p class="sec-intro">From the deeply personal to the purely commercial, almost every conflict can be mediated. These are the matters we resolve every week.</p>
    </div>
    <div class="cards reveal" style="margin-top:50px">
      <article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 21s-7-4.5-7-10a4 4 0 017-2.6A4 4 0 0119 11c0 5.5-7 10-7 10z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></div><h3>Family &amp; separation</h3><p>Parenting plans, property settlements and divorce — resolved with dignity, decisions kept in your hands.</p><a class="more" href="/family-law-mediation/">Family law mediation <span class="arr">→</span></a></article>
      <article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect x="4" y="8" width="16" height="12" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M9 8V6a3 3 0 016 0v2" stroke="currentColor" stroke-width="1.6"/></svg></div><h3>Property settlement</h3><p>Divide assets, debts and superannuation fairly and finally — without losing it to legal fees.</p><a class="more" href="/property-settlement-mediation/">Property settlement <span class="arr">→</span></a></article>
      <article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7l8-4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></div><h3>Workplace &amp; employment</h3><p>Dismissals, contracts and bullying claims handled fast and fairly — before the Fair Work Commission.</p><a class="more" href="/workplace-mediation/">Workplace mediation <span class="arr">→</span></a></article>
      <article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="9" cy="8" r="3.5" stroke="currentColor" stroke-width="1.6"/><path d="M3 20c0-3.5 2.7-5.5 6-5.5s6 2 6 5.5" stroke="currentColor" stroke-width="1.6"/><path d="M16 5a3.5 3.5 0 010 6.5M18 20c0-2.5-1-4.2-2.5-5" stroke="currentColor" stroke-width="1.6"/></svg></div><h3>Parenting &amp; children</h3><p>Build a parenting plan around what your children need — calm, child-focused and lasting.</p><a class="more" href="/parenting-plan-mediation/">Parenting plans <span class="arr">→</span></a></article>
      <article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 9h16M4 9l2-4h12l2 4M4 9v10a1 1 0 001 1h14a1 1 0 001-1V9" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></div><h3>Estate &amp; inheritance</h3><p>Contested wills and family disagreements resolved privately — preserving relationships at the hardest time.</p><a class="more" href="/contact-us/">Estate disputes <span class="arr">→</span></a></article>
      <article class="card"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 13h4l2 5 4-12 2 7h4" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/></svg></div><h3>Online &amp; remote</h3><p>Resolve everything by secure video, anywhere in Australia — including regional and remote areas.</p><a class="more" href="/online-divorce/">Online mediation <span class="arr">→</span></a></article>
    </div>
  </div>
</section>

<section class="sec reveal" id="why" style="background:var(--sand-deep);border-radius:38px;margin:0 16px" aria-labelledby="why-h">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center" class="why-grid">
      <div>
        <p class="sec-tag">Why Mediations Australia</p>
        <h2 class="sec-title" id="why-h">Legal expertise, on the <em>resolution</em> side.</h2>
        <p class="sec-intro">Many of our mediators are also experienced lawyers, so the legal realities of your matter are understood from the start. We work alongside your own lawyer too — many of the people we help are referred to us by the very solicitors advising them.</p>
        <div style="display:flex;flex-direction:column;gap:24px;margin-top:32px">
          <div style="display:flex;gap:16px"><span style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:var(--cream);display:flex;align-items:center;justify-content:center;color:var(--sage-deep)"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 2l2.5 6.5L21 9l-5 4.5L17.5 21 12 17l-5.5 4L8 13.5 3 9l6.5-.5L12 2z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></span><div><h3 style="font-size:1.16rem;margin-bottom:4px">Nationally accredited</h3><p style="font-size:.98rem;color:var(--ink-soft)">Certified under the Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS).</p></div></div>
          <div style="display:flex;gap:16px"><span style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:var(--cream);display:flex;align-items:center;justify-content:center;color:var(--sage-deep)"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/><path d="M8 12l2.5 2.5L16 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><div><h3 style="font-size:1.16rem;margin-bottom:4px">Fixed-fee, no surprises</h3><p style="font-size:.98rem;color:var(--ink-soft)">You'll always know what things cost — clarity on your options without an open-ended bill.</p></div></div>
          <div style="display:flex;gap:16px"><span style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:var(--cream);display:flex;align-items:center;justify-content:center;color:var(--sage-deep)"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/><path d="M3 12h18M12 3a15 15 0 010 18 15 15 0 010-18" stroke="currentColor" stroke-width="1.5"/></svg></span><div><h3 style="font-size:1.16rem;margin-bottom:4px">Nationwide &amp; online</h3><p style="font-size:.98rem;color:var(--ink-soft)">Offices in Sydney, Melbourne, Brisbane and Perth — and online mediation Australia-wide.</p></div></div>
        </div>
      </div>
      <aside style="background:var(--sage-deep);color:var(--cream);border-radius:28px;padding:46px 40px;box-shadow:var(--shadow-lg)">
        <div style="font-family:var(--serif);font-size:4.5rem;line-height:1;margin-bottom:8px">90<span style="color:#e0a87f">%</span></div>
        <p style="color:rgba(251,248,242,.82);margin-bottom:28px">of disputes we mediate are resolved — without ever reaching a courtroom.</p>
        <div style="display:flex;flex-direction:column;gap:16px;border-top:1px solid rgba(251,248,242,.18);padding-top:24px">
          <div style="display:flex;align-items:center;gap:12px">{TICK}Thousands of matters resolved</div>
          <div style="display:flex;align-items:center;gap:12px">{TICK}Family, commercial, workplace &amp; estate</div>
          <div style="display:flex;align-items:center;gap:12px">{TICK}In person or online</div>
        </div>
      </aside>
    </div>
  </div>
</section>"""
doc += faq_html(qa_home, heading="Everything you might be <em>wondering</em>.", tag="Common questions")
doc += cta_band("The first step costs <em>nothing</em> but a phone call.",
 "Tell us about your dispute. We'll give you an honest view of whether mediation can help — and how it fits alongside any legal advice you're already getting.")
doc += "</main>" + page_end()
write("", doc)

# ============================================================
# FAMILY LAW MEDIATION (rebuilt on system)
# ============================================================
qa_fam = [
 ("Is family mediation compulsory before going to court?",
  "For most parenting matters, yes. Under Section 60I of the Family Law Act 1975 you must attempt family dispute resolution and obtain a certificate before applying to court — unless an exemption applies, such as family violence or genuine urgency."),
 ("What is a Section 60I certificate?",
  "It's a certificate issued by an accredited Family Dispute Resolution Practitioner confirming you attempted mediation. It's generally required before you can file parenting proceedings. We can issue these as part of your mediation."),
 ("Can property and financial matters be mediated?",
  "Yes. Property settlements, superannuation splits and spousal maintenance can all be mediated, then formalised through consent orders or a binding financial agreement so the outcome is legally enforceable."),
 ("What if there's been family violence?",
  "Your safety comes first. Where there are concerns, mediation may not be required, and where it does proceed it can run 'shuttle' style in separate rooms. Tell us in your consultation and we'll advise the safest path."),
 ("How much does family mediation cost?",
  "You begin with a fixed-fee consultation, so there are no surprises. Family mediation typically costs a small fraction of a contested court case, and the cost is usually shared between the parties."),
]
doc = head(
 "Family Law Mediation Australia | Family Mediators",
 "Family law mediation with accredited family mediators — settle parenting and property faster and cheaper than court. Section 60I certificates. Free consult.",
 "family-law-mediation",
 og_type="article",
 extra_schema=[org_schema(),
               breadcrumb_schema([("Home",""),("Family Law Mediation","family-law-mediation")]),
               service_schema("Family Law Mediation","Mediation for parenting and property disputes in Australia.","family-law-mediation"),
               faq_schema(qa_fam)])
doc += nav()
doc += f"""<main id="main">
{crumb_html([("Home",""),("Family Law Mediation",None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>Family Dispute Resolution · Section 60I certificates</span>
    <h1>Family Law Mediation — keep decisions <em>in your hands</em>.</h1>
    <p class="lede">Separation is hard enough without a courtroom making it harder. Our nationally accredited family mediators help you settle parenting and property matters faster, more affordably, and on terms you choose together — not ones a judge imposes.</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="/how-mediation-works/" class="btn btn-ghost">How mediation works</a>
    </div>
  </div>
</section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> Family law mediation (also called Family Dispute Resolution) is a confidential process where a neutral, accredited practitioner helps separating couples agree on parenting and property arrangements without going to court. For most parenting matters it's a legal requirement before you can file — and around 90% of the disputes we mediate are resolved without a judge.</p></div></div>
<article class="body"><div class="wrap-narrow reveal">
<h2>Why mediate family matters <em>before</em> court?</h2>
<p>Because the court process is slow and costly, and it places the most important decisions of your life in a judge's hands rather than your own. A contested family law matter can take one to three years and cost tens of thousands of dollars per side. Mediation offers a gentler path: it's usually resolved in one or two sessions, costs a fraction as much, and leaves you in control of the outcome. It's also the step most family lawyers recommend trying first.</p>
<p>It's better for the people who matter most, too. When parents reach their own agreement rather than having one imposed, arrangements tend to last longer and the co-parenting relationship survives — which is what children need most.</p>

<h2>Is family mediation <em>compulsory</em> before going to court?</h2>
<p>For most parenting disputes, yes. Under Section 60I of the <em>Family Law Act 1975</em>, you must make a genuine attempt at family dispute resolution before applying for parenting orders. There are exemptions — family violence, child safety concerns, or genuine urgency — but for most separating parents, mediation is the required first step. <a href="/section-60i-certificates/">Learn about Section 60I certificates →</a></p>

<h2>What family matters can be mediated?</h2>
<ul>
  <li><a href="/parenting-plan-mediation/">Parenting plans</a> — living arrangements, time with each parent, and decision-making</li>
  <li><a href="/divorce-mediation/">Divorce mediation</a> — resolving everything that comes with separating</li>
  <li><a href="/property-settlement-mediation/">Property settlements</a> — dividing assets, debts and the family home</li>
  <li>Superannuation splitting and <a href="/spousal-support-mediation/">spousal maintenance</a></li>
  <li><a href="/financial-agreements-mediation/">Binding financial agreements (BFAs)</a></li>
  <li><a href="/child-support-mediation/">Child support</a> arrangements and disputes</li>
  <li><a href="/de-facto-mediation/">De facto and same-sex relationship</a> disputes</li>
</ul>

<h2>Family mediators who understand the law</h2>
<p>Many of our family mediators are also experienced family lawyers. That means our family mediation services give you a clear-eyed view of where you'd likely land in court — and a process designed to get you there faster, for far less, without ever filing. We provide family mediation right across Australia, in person and by secure video, so wherever you are you can work with an accredited family mediator. If you're separating specifically, our dedicated <a href="/divorce-mediation/">divorce mediation</a> service covers parenting, property and finances together; and you can see exactly <a href="/how-much-does-mediation-cost/">what family mediation costs</a> before you commit.</p>

<h2>How family law mediation works, step by step</h2>
<p>The process is structured but never rigid, and it's designed to keep things calm:</p>
<ol>
  <li><strong>Fixed-fee consultation</strong> — you explain your situation and we give an honest view of whether mediation can help and how it works alongside any legal advice.</li>
  <li><strong>Intake, separately</strong> — each party meets the family mediator on their own so concerns and safety can be assessed before anyone is in the same room.</li>
  <li><strong>Preparation</strong> — financial disclosure is gathered for property matters, and the issues to resolve are agreed and put in order.</li>
  <li><strong>The mediation</strong> — guided by the mediator, you work through each issue, together or in separate rooms ('shuttle' mediation) where there's high conflict.</li>
  <li><strong>Agreement and formalising</strong> — what you agree is recorded, then turned into <a href="/consent-orders/">consent orders</a> or a binding financial agreement so it's enforceable.</li>
</ol>

<h2>Family law mediation vs going to court</h2>
<p>For most separating families the contrast is stark — which is why mediation is the step most family lawyers suggest trying first:</p>
<figure class="tbl"><table><caption>Family law mediation compared with a contested court case</caption>
<thead><tr><th></th><th>Family law mediation</th><th>Contested court</th></tr></thead>
<tbody>
<tr><td>Typical time</td><td>Weeks — one or two sessions</td><td>One to three years</td></tr>
<tr><td>Typical cost</td><td>Fixed fee, usually shared</td><td>Tens of thousands per side</td></tr>
<tr><td>Who decides</td><td>You and your former partner</td><td>A judge</td></tr>
<tr><td>Privacy</td><td>Confidential</td><td>Public process</td></tr>
<tr><td>Effect on co-parenting</td><td>Preserved where possible</td><td>Often strained</td></tr>
</tbody></table></figure>
<p>The aim isn't to avoid court at any cost — it's to avoid <em>unnecessary</em> court. Where there's a genuine safety risk or a legal question only a judge can decide, litigation has its place. <a href="/mediate-or-litigate/">See when mediation beats litigation →</a></p>

<h2>When family mediation may not be the right path</h2>
<p>We're honest about the limits. Mediation depends on both people being able to negotiate safely and openly, so it isn't suitable in every case — particularly where there is family violence, a serious safety risk, or where one party won't participate or disclose honestly. In those situations you may be <a href="/section-60i-certificates/">exempt</a> from the usual requirement to attempt family dispute resolution, and court protection may be the right first step. If you're in immediate danger, call <strong>000</strong>; for confidential support, <strong>1800RESPECT (1800 737 732)</strong> is available 24/7. See our guidance on <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>

<h2>How much does family mediation cost?</h2>
<p>You start with a fixed-fee consultation, so you know exactly where you stand before committing to anything. From there, family mediation typically costs a small fraction of a contested court case, and the fee is usually shared between the parties. Compared with two sets of lawyers billing by the hour for years, the saving is substantial — and the emotional cost is lower too. <a href="/how-much-does-mediation-cost/">See a full breakdown of what mediation costs →</a></p>

<h2>Why choose accredited family mediators?</h2>
<p>Not all mediation is equal. Our family mediators are nationally accredited under the Australian Mediator and Dispute Resolution Accreditation Standard (AMDRAS), and many are also experienced family lawyers — so you get both the legal insight to understand where your matter would land and the resolution focus to get you there without a fight. We work alongside any lawyer you already have rather than replacing them; in fact, much of our work comes referred from the very solicitors advising separating clients. With fixed-fee consultations, in-person and secure online options, and family mediation services available right across Australia, you get genuine expertise and a real alternative to litigation. <a href="/about-mediations-australia/">Learn more about Mediations Australia →</a></p>

<h2>Making your agreement <em>legally binding</em></h2>
<p>Reaching agreement is the hard part — we make the rest simple. Once you've settled, we help formalise it into a legally enforceable outcome: <a href="/consent-orders/">consent orders</a> for parenting and property, or a binding financial agreement where appropriate. You walk away with certainty, not just a handshake. Wherever you are — <a href="/sydney-mediation/">Sydney</a>, Melbourne, Brisbane or Perth — you can start with a free consultation.</p>
</div></article>"""
doc += faq_html(qa_fam, heading="Family mediation FAQs")
doc += cta_band("Talk to a family mediator <em>this week</em>.",
 "Tell us what you're facing. We'll give you an honest view of whether mediation can help — and how it works alongside any legal advice you already have.")
doc += "</main>" + page_end()
write("family-law-mediation", doc)

print("Homepage + family law page rebuilt on shared system.")
