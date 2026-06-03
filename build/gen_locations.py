#!/usr/bin/env python3
"""Generate deep, substantive location pages (~1500+ words) with verified local detail."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN, OFFICES, SERVICES)
from location_data import LOCATION_DATA

OUT = "/home/claude/mediations/site"
NEAREST = {"NSW":"Sydney","VIC":"Melbourne","QLD":"Brisbane","WA":"Perth",
           "SA":"Melbourne","ACT":"Sydney","TAS":"Melbourne","NT":"Brisbane"}

def localservice_schema(city, state, slug):
    return {"@type":"LegalService","name":f"Mediations Australia - {city}",
            "description":f"Nationally accredited mediators serving {city} and {state}, resolving family, property, workplace and commercial disputes without court.",
            "url":f"{DOMAIN}/{slug}/","telephone":PHONE,
            "parentOrganization":{"@id":f"{DOMAIN}/#organization"},
            "areaServed":{"@type":"City","name":city},
            "priceRange":"Fixed-fee consultations"}

# Keyword-first H1s: target phrase leads, persuasive tail varies by state.
# Primary ranking phrase "{City} Mediation" appears at the very start of every H1.
H1S = {
 "NSW":"{c} Mediation — <em>resolve disputes without court</em>.",
 "VIC":"{c} Mediation that <em>keeps you out of court</em>.",
 "QLD":"{c} Mediation — <em>a faster way to resolve disputes</em>.",
 "WA":"{c} Mediation — <em>expert resolution, not litigation</em>.",
 "SA":"{c} Mediation that <em>puts you in control</em>.",
 "ACT":"{c} Mediation — <em>resolve it without the courtroom</em>.",
 "TAS":"{c} Mediation — <em>settle disputes without the battle</em>.",
 "NT":"{c} Mediation — <em>resolution without the courtroom</em>.",
}

def build(slug, city, state, own_reg, reg_desc, circuit, regions, has_office,
          office_addr, context, state_note, court_ref):
    nearest = NEAREST[state]
    h1 = H1S.get(state, "{c} mediation that resolves disputes <em>without court</em>.").format(c=esc(city))
    title = f"{city} Mediation | Accredited Family Mediators {city}"
    desc = (f"Nationally accredited {city} mediators resolve family, property and workplace "
            f"disputes without court — faster and cheaper. Free consultation. Call {PHONE}.")
    if has_office:
        office_line = f"Our {city} office is located at {office_addr}, and we also offer secure online mediation across {state}."
    else:
        office_line = (f"While our nearest office is in {nearest}, we regularly serve {city} clients "
                       f"both in person by arrangement and through secure online mediation — giving you "
                       f"the same nationally accredited mediators wherever you are in {state}.")

    qa = [
     (f"How much does mediation cost in {city}?",
      f"In {city} you start with a fixed-fee consultation, so there are no billing surprises. Mediation typically costs a fraction of a contested court case — often the difference between a few hundred to a few thousand dollars shared between the parties, versus tens of thousands per side in litigation. Most matters resolve in one or two sessions."),
     (f"Where do you provide mediation in {city}?",
      f"We serve {regions}. {office_line}"),
     (f"Do {city} family law matters have to go to court?",
      f"Usually not. For most parenting matters you must attempt family dispute resolution first, and around 90% of the disputes we mediate resolve without a judge. A matter would only proceed to {court_ref} if it genuinely cannot be resolved by agreement."),
     (f"How long does mediation take in {city}?",
      f"Most {city} mediations resolve within one to two sessions, often in a single day. By contrast, a contested matter through {court_ref} can take one to three years to reach a final hearing."),
     (f"Can I do {city} mediation online?",
      f"Yes. We offer secure online mediation to all {city} and {state} clients, which is especially convenient for regional areas and removes any need to travel. Online agreements are just as binding once formalised."),
     ("Are your mediators nationally accredited?",
      "Yes. Our mediators are accredited under the Australian Mediator and Dispute Resolution Accreditation Standards (AMDRAS), the national benchmark, and many are also experienced family lawyers."),
     (f"What types of disputes can be mediated in {city}?",
      f"We mediate family and separation matters, property settlements, parenting arrangements, workplace and employment disputes, commercial and business disputes, estate and inheritance disputes, and personal injury claims across {city} and {state}."),
    ]

    schema = [org_schema(),
              breadcrumb_schema([("Home",""),(f"{city} Mediation",slug)]),
              localservice_schema(city, state, slug),
              faq_schema(qa)]
    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += f"""<main id="main">
{crumb_html([("Home",""),(f"{city} Mediation",None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>Serving {esc(city)} &amp; {esc(state)} · Nationally accredited</span>
    <h1>{h1}</h1>
    <p class="lede">Mediation in {esc(city)} gives individuals, families and businesses a faster, more affordable and less stressful way to resolve disputes. Our nationally accredited mediators help you reach a lasting agreement — and keep the decision in your hands, not a judge's.</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> Mediations Australia provides nationally accredited mediation in {esc(city)}, resolving family, property, workplace and commercial disputes faster and at a fraction of the cost of court. We serve {esc(regions)}, in person and through secure online mediation across {esc(state)}, with a 90% resolution rate and fixed-fee consultations.</p></div></div>
<article class="body"><div class="wrap-narrow reveal">

<h2>Why choose mediation in {esc(city)}?</h2>
<p>When a relationship breaks down — whether between separating partners, business owners, employer and employee, or family members — the instinct is often to engage lawyers and prepare for court. But for the overwhelming majority of {esc(city)} disputes, litigation is the slowest, most expensive and most stressful path available. {esc(context)}</p>
<p>Mediation offers a fundamentally different approach. Instead of handing control to a judge, you and the other party work with a neutral, nationally accredited mediator to reach your own agreement. The mediator doesn't take sides or impose a decision — their role is to guide a structured, confidential conversation that cuts through conflict and finds workable solutions. Sometimes court is genuinely necessary, and a good lawyer will tell you when. But trying mediation first almost always saves time, money and stress, whatever happens next.</p>

<h2>{esc(city)} mediation vs going to court: an honest comparison</h2>
<p>It's worth being clear-eyed about the difference between the two paths, because for most people in {esc(city)} the contrast is stark:</p>
<ul>
  <li><strong>Time.</strong> Most {esc(city)} mediations resolve in one or two sessions, often within weeks. A contested matter through {esc(court_ref)} can take one to three years to reach a final hearing.</li>
  <li><strong>Cost.</strong> Mediation starts with a fixed fee and is usually shared between the parties. Litigation can consume tens or even hundreds of thousands of dollars per side — frequently a significant share of the very assets in dispute.</li>
  <li><strong>Control.</strong> In mediation you design the outcome. In court, a judge who has known your situation for hours decides matters you've lived for years.</li>
  <li><strong>Privacy.</strong> Mediation is confidential and conducted on a "without prejudice" basis. Court proceedings are part of the public record.</li>
  <li><strong>Relationships.</strong> Litigation is adversarial by design. Mediation is collaborative, which matters enormously when you'll continue to co-parent, share a business, or move in the same circles.</li>
</ul>

<h2>How the {esc(city)} court system fits in</h2>
<p>{esc(reg_desc)}. {esc(circuit)} {esc(state_note)} Understanding where your matter would otherwise be heard matters, because it shows just how much mediation can save you. Rather than waiting for a listing at {esc(court_ref)}, you can often resolve your dispute within weeks — and if you do reach agreement, we can formalise it so it carries the same legal weight as a court order.</p>

<div class="callout">
  <h3>Can't get to an office? Mediate online.</h3>
  <p>Our <a href="/online-divorce/">secure online mediation</a> gives {esc(city)} and {esc(state)} clients access to the same nationally accredited mediators from anywhere — no travel, same structured process, same binding outcomes. It's especially valuable for clients outside the {esc(city)} CBD or in surrounding regional areas.</p>
</div>

<h2>What we resolve for {esc(city)} clients</h2>
<p>Our {esc(city)} mediators work across the full spectrum of dispute resolution. Whatever you're facing, there is almost always a path through it that doesn't begin in a courtroom:</p>
<ul>
  <li><strong><a href="/family-law-mediation/">Family law and separation</a></strong> — the practical and emotional work of separating, including divorce, without an adversarial court fight.</li>
  <li><strong><a href="/property-settlement-mediation/">Property settlements</a></strong> — dividing assets, debts, the family home and superannuation fairly and finally.</li>
  <li><strong><a href="/parenting-plan-mediation/">Parenting arrangements</a></strong> — child-focused plans covering living arrangements, time with each parent and decision-making.</li>
  <li><strong><a href="/workplace-mediation/">Workplace and employment disputes</a></strong> — resolving conflict, dismissals and complaints before they reach the Fair Work Commission.</li>
  <li><strong>Commercial and business disputes</strong> — contracts, partnerships and shareholder disagreements settled quickly and privately.</li>
  <li><strong>Estate and inheritance disputes</strong> — contested wills and family disagreements resolved with dignity.</li>
</ul>

<h2>What to expect from {esc(city)} mediation</h2>
<p>The process is designed to be calm, clear and free of jargon. You begin with a fixed-fee consultation, where we listen to your situation and give you an honest view of whether mediation can help. You're then matched with an accredited mediator suited to your matter. The mediation itself can be conducted with everyone in the same room, or in separate rooms with the mediator moving between you — known as "shuttle" mediation — which is useful where there is high conflict or a safety concern. Where agreement is reached, we help you formalise it through <a href="/consent-orders/">consent orders</a> or a <a href="/financial-agreements-mediation/">binding financial agreement</a> so it is legally enforceable. You can <a href="/how-mediation-works/">read our full step-by-step guide to how mediation works</a> for more detail.</p>

<h2>Why {esc(city)} clients choose Mediations Australia</h2>
<p>Our mediators are nationally accredited under AMDRAS, and many are also experienced family lawyers — so the legal realities of your matter are understood from the outset. We're early-resolution focused, we work alongside your existing lawyer where you have one, and many of the people we help are in fact referred to us by the very solicitors advising them. With a 90% resolution rate across thousands of matters, fixed-fee consultations and both in-person and online options, {esc(city)} clients get genuine expertise and a real alternative to litigation. <a href="/about-mediations-australia/">Learn more about Mediations Australia →</a></p>

<h2>{esc(city)} family lawyers <em>and</em> mediators</h2>
<p>If you were searching for "{esc(city)} family lawyers", you're in the right place. Our team includes accredited family lawyers — but the way we work is different. Rather than starting with the assumption that your matter belongs in court, we start with the question of whether it needs to. For the vast majority of separations, the answer is no: mediation resolves matters faster, far more cheaply, and with less damage to the family. We give you the legal insight of a family lawyer and the resolution focus of a mediator, in one place. <a href="/mediate-or-litigate/">See why mediation usually beats litigation →</a></p>

</div></article>"""
    # service cards
    cards = "".join(
        f'<article class="card"><h3>{esc(n)}</h3><p>{esc(d)}</p>'
        f'<a class="more" href="/{s}/">Learn more <span class="arr">→</span></a></article>'
        for s, n, d in SERVICES[:6])
    doc += f"""<section class="sec" style="padding-top:0"><div class="wrap">
<div class="reveal"><p class="sec-tag">Services in {esc(city)}</p>
<h2 class="sec-title">Every kind of dispute, <em>resolved locally</em>.</h2></div>
<div class="cards reveal" style="margin-top:46px">{cards}</div></div></section>"""
    doc += faq_html(qa, heading=f"{city} mediation FAQs")
    doc += cta_band(f"Resolve your {esc(city)} dispute, <em>starting today</em>.",
        f"Book a fixed-fee consultation with a nationally accredited {esc(city)} mediator and find out how mediation can help — in person or online.")
    doc += "</main>" + page_end()
    path = os.path.join(OUT, slug); os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)
    # word count
    import re
    text = re.sub(r'<[^>]+>',' ', doc)
    return slug, len(text.split())

results = [build(*row) for row in LOCATION_DATA]
print("Deep location pages built:")
for s,w in results: print(f"  {s}: ~{w} words")
