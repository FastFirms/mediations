#!/usr/bin/env python3
"""/workplace-mediation-cost/ — dedicated workplace pricing page (brief §5, §5.7 item 3).

All figures come from workplace_pricing.WORKPLACE (Dan-approved 7 Nov 2026). Workplace only:
never link family/FDR pricing here, and never reuse this page's figures on family URLs.
Run:  python3 build/gen_workplace_cost.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_services_v2 import inline_cta, key_takeaway, service_page
from workplace_pricing import WORKPLACE as W, inc, money, price_block, offers_schema, faq_answers

H, F, X = W["half_day_ex"], W["full_day_ex"], W["extra_party_ex"]
FAQ = faq_answers()
SLUG = "workplace-mediation-cost"

service_page(
    slug=SLUG,
    title="How Much Does Workplace Mediation Cost? | Mediations Australia",
    desc=f"Workplace mediation is {money(H)} + GST for a half day or {money(F)} + GST for a full day for two parties, with intake included. See extra-party and travel costs.",
    breadcrumb_label="Workplace Mediation Cost",
    eyebrow="Workplace mediation pricing",
    h1_html="How much does workplace mediation <em>cost?</em>",
    lede=(f"Mediations Australia charges {money(H)} + GST for a half-day workplace mediation or {money(F)} + GST for a full day. "
          f"The standard fee covers two parties and includes an intake session with each party and the mediation session. "
          f"Each extra party is {money(X)} + GST; travel is quoted separately. Group or team facilitation is quoted on request."),
    toc_items=[
        ("prices", "Prices at a glance"),
        ("half-or-full", "Half day or full day?"),
        ("included", "What the fee includes"),
        ("extra-parties", "Extra parties and travel"),
        ("group", "Group and team facilitation"),
        ("compare", "Comparing quotes across the market"),
        ("who-pays", "Who pays?"),
    ],
    takeaway=key_takeaway(
        f"Workplace mediation with Mediations Australia costs {money(H)} + GST ({money(inc(H))} including GST) for a half day "
        f"or {money(F)} + GST ({money(inc(F))}) for a full day. That is a total for two parties, not per person, and includes "
        f"an intake session with each party plus the mediation session. Each additional party is {money(X)} + GST."
    ),
    body_html=f"""
<h2 id="prices">Prices at a glance</h2>
{price_block()}

<h2 id="half-or-full">Half day or full day?</h2>
<p>The difference is the length of the mediation session. A half day suits many two-person disputes where the issues are reasonably contained. A full day gives more time where there are several issues, a longer history, or where the mediator expects to work with participants separately for part of the session. We recommend an option after the suitability conversation, and you can ask why.</p>

<h2 id="included">What the fee includes</h2>
<ul>
  <li><strong>Two parties</strong> as standard.</li>
  <li><strong>An intake session with each party</strong>, held separately, before the mediation.</li>
  <li><strong>The mediation session</strong> itself (half day or full day).</li>
</ul>
<p>Prices are engagement totals. They are not per-person rates, and they do not depend on whether a joint session or separate-room format is used.</p>
""" + inline_cta("Want to check whether mediation suits your dispute before committing?", btn="Discuss your workplace dispute", href="/contact-us/") + f"""

<h2 id="extra-parties">Extra parties and travel</h2>
<p>Each additional participating party is <strong>{money(X)} + GST ({money(inc(X))} including GST)</strong>, and intake with that party is still included.</p>
<figure class="tbl"><table><caption>Examples before any travel</caption>
<thead><tr><th>Parties</th><th>Half day</th><th>Full day</th></tr></thead>
<tbody>
<tr><td>2 (standard)</td><td>{money(H)} + GST</td><td>{money(F)} + GST</td></tr>
<tr><td>3</td><td>{money(H + X)} + GST</td><td>{money(F + X)} + GST</td></tr>
<tr><td>4</td><td>{money(H + 2 * X)} + GST</td><td>{money(F + 2 * X)} + GST</td></tr>
</tbody></table></figure>
<p><strong>Travel is extra and quoted separately</strong>, so you will know the figure before you book.</p>

<h2 id="group">Group and team facilitation</h2>
<p>Where a dispute involves a whole team or a larger group, the work is designed differently from two-party mediation: commissioning scope, intake, session design and follow-up all depend on the group. Group and team facilitation is <strong>quoted on request</strong> rather than priced as the standard fee plus extra parties.</p>

<h2 id="compare">Comparing quotes across the market</h2>
<p>When comparing providers, compare the full scope rather than a headline session fee. Check how many parties are included, whether intake is included, the session format and length, whether GST is included, and how travel is charged. The figures on this page are Mediations Australia's fees, not an industry-wide average.</p>

<h2 id="who-pays">Who pays?</h2>
<p>Payment arrangements are agreed for each matter. Most workplace mediations are paid for by the employer, but that is not automatic. Whoever pays, the mediator remains independent of all participants and does not take instructions about the outcome.</p>
<p>See how the process works on our <a href="/workplace-mediation/">workplace mediation</a> page.</p>
""",
    faq_items=[
        ("How much does workplace mediation cost?", FAQ["cost"]),
        ("Who pays for workplace mediation?",
         "Payment arrangements are agreed for each matter and are not automatically split equally. Most often the employer pays. Whoever pays, the mediator stays independent of all participants."),
        ("Does the fee include intake?", FAQ["intake"]),
        ("Are prices per person?", FAQ["per_person"]),
        ("What if there are more than two parties?", FAQ["more_parties"]),
        ("Is travel included?", FAQ["travel"]),
    ],
    related_items=[
        ("workplace-mediation", "Workplace Mediation"),
        ("is-mediation-right-for-workplace-dispute", "Is Mediation Right for a Workplace Dispute?"),
        ("workplace-mediation-guide", "Workplace Mediation: Complete Guide"),
        ("ngo-not-for-profit-mediation", "NGO & Not-for-Profit Mediation"),
    ],
    offers=offers_schema(SLUG),
)
print(f"built /{SLUG}/")
