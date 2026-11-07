#!/usr/bin/env python3
"""SEO recovery stage 4 (brief §4.2, §4.3): strengthen two imported WordPress posts in place.

These pages have no live generator (gen_imported_posts.py fetched them once from the old
WordPress site and skips slugs that exist), so the built HTML is the source of truth.
This script patches it idempotently: re-running it is a no-op (marker comment).

Facts used are from fcfcoa.gov.au pages (fees, consent orders guide, checked 8 Nov 2026)
and the Family Law Act. DRAFT pending legal review.
"""
import os, re, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
MARK = "<!-- seo-recovery-stage4 -->"


def _faq_pairs(h, faq_id, end_id):
    a = h.index(f'<h2 id="{faq_id}"'); b = h.index(f'<h2 id="{end_id}"', a)
    sec = h[a:b]
    pairs = re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>', sec, re.S)
    clean = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).replace('&#8217;', '’').replace('&amp;', '&').strip()
    return [(clean(q), clean(x)) for q, x in pairs]


def patch(slug, desc, inserts, faq_id, faq_end_id, faqs_add, replaces=(), title=None, h1=None):
    path = os.path.join(ROOT, slug, "index.html")
    h = open(path, encoding="utf-8").read()
    if MARK in h:
        print(f"{slug}: already patched"); return
    for old, new in replaces:
        assert h.count(old) >= 1, f"{slug}: missing {old[:60]}"
        h = h.replace(old, new)
    h = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*(")',
               lambda m: m.group(1) + desc + m.group(2), h)
    if title:
        h = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', h)
        h = re.sub(r'(<meta (?:property|name)="(?:og:title|twitter:title)" content=")[^"]*(")',
                   lambda m: m.group(1) + title + m.group(2), h)
    if h1:
        h = re.sub(r'<h1([^>]*)>.*?</h1>', lambda m: f'<h1{m.group(1)}>{h1}</h1>', h, count=1, flags=re.S)
    for before_id, new_id, label, html in inserts:
        anchor = f'<h2 id="{before_id}"'
        assert h.count(anchor) == 1, f"{slug}: anchor {before_id}"
        h = h.replace(anchor, f'<h2 id="{new_id}">{label}</h2>\n{html}\n' + anchor)
        h = h.replace(f'<li><a href="#{before_id}">', f'<li><a href="#{new_id}">{label}</a></li><li><a href="#{before_id}">')
    end = f'<h2 id="{faq_end_id}"'
    extra = "".join(f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_add)
    h = h.replace(end, extra + end, 1)
    pairs = _faq_pairs(h, faq_id, faq_end_id)
    schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}
    h = h.replace("</head>", f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n</head>', 1)
    h = re.sub(r'"dateModified": "[^"]*"', f'"dateModified": "{TODAY}"', h)
    h = h.replace("</body>", MARK + "\n</body>", 1)
    open(path, "w", encoding="utf-8").write(h)
    print(f"{slug}: patched, {len(pairs)} FAQs in schema")


FCFCOA_FEES = '<a href="https://www.fcfcoa.gov.au/fl/fees/fl-fees" target="_blank" rel="noopener">FCFCOA fee schedule</a>'
FCFCOA_CONSENT = '<a href="https://www.fcfcoa.gov.au/hdi/apply-consent-orders" target="_blank" rel="noopener">Court&#8217;s consent orders guide</a>'
FLA = '<a href="https://www.legislation.gov.au/C2004A00275/latest/text" target="_blank" rel="noopener">Family Law Act 1975</a>'

# ─────────────────────────────────────────────────────────────────────────────
# §4.2 Family lawyer costs
# ─────────────────────────────────────────────────────────────────────────────
patch(
    "how-much-does-a-family-lawyer-cost-in-australia",
    "Understand family-law fee structures, disbursements and quote questions, and see how mediation can fit alongside independent legal advice.",
    inserts=[
        ("what-does-a-family-lawyer-usually-charge-for", "fee-types", "Fee types: fixed scope, hourly, GST and disbursements", """
<p>Before comparing numbers, compare <strong>how</strong> each lawyer charges. Two quotes with the same headline figure can cover very different work.</p>
<table>
<thead><tr><th>Fee type</th><th>How it works</th><th>What to check</th></tr></thead>
<tbody>
<tr><td>Fixed fee (fixed scope)</td><td>An agreed price for a defined task, such as an initial advice session or reviewing an agreement</td><td>Exactly what is included, and what triggers extra charges</td></tr>
<tr><td>Hourly rate</td><td>Time is billed in units at each person's rate</td><td>Rates for each person who may work on the file, including junior staff</td></tr>
<tr><td>Staged estimate</td><td>A cost estimate for each stage (advice, negotiation, court steps)</td><td>The assumptions behind each stage and when the estimate will be revised</td></tr>
<tr><td>GST</td><td>Legal professional fees generally attract GST</td><td>Whether quoted figures include or exclude GST</td></tr>
<tr><td>Disbursements</td><td>Out-of-pocket costs such as court filing fees, barristers, valuers and experts</td><td>Which disbursements are expected, and whether they are in the estimate</td></tr>
</tbody>
</table>
<h3>What is often excluded</h3>
<p>Quotes commonly exclude barrister fees, expert reports (such as valuations), court filing fees, and extra work caused by how the other party runs the matter. Ask for exclusions in writing. Legal cost-disclosure obligations are set by each state and territory, so the form of estimate you receive can differ between jurisdictions.</p>
"""),
        ("should-you-still-get-legal-advice-first", "quote-worksheet", "A quote-comparison worksheet", """
<p>Ask every lawyer the same questions so you can compare quotes like for like.</p>
<table>
<thead><tr><th>Question</th><th>Lawyer A</th><th>Lawyer B</th></tr></thead>
<tbody>
<tr><td>What exactly is in scope, and out of scope?</td><td></td><td></td></tr>
<tr><td>Which stages are estimated, and on what assumptions?</td><td></td><td></td></tr>
<tr><td>Fixed fee, hourly, or a mix? Who does the work, at what rates?</td><td></td><td></td></tr>
<tr><td>Which disbursements are expected, and are they included?</td><td></td><td></td></tr>
<tr><td>Do figures include GST?</td><td></td><td></td></tr>
<tr><td>What would change the estimate, and how will I be told?</td><td></td><td></td></tr>
<tr><td>How and when will I be billed?</td><td></td><td></td></tr>
</tbody>
</table>
"""),
        ("why-mediation-is-often-the-better-cost-decision", "legal-advice-and-mediation", "Paying for legal advice alongside mediation", f"""
<p>Mediation and legal advice do different jobs. A mediator helps the parties negotiate and reach their own agreement, but does not give either person legal advice or represent them. A lawyer advises you on your rights and on whether a proposed agreement is appropriate. The {FCFCOA_CONSENT} says it is advisable to get legal advice before deciding what to agree on or applying to court.</p>
<p>Many people keep costs down by paying for <strong>targeted</strong> legal advice at key points, such as before mediation and to review an agreement afterwards, rather than having a lawyer run every step of the negotiation. Ask lawyers whether they offer limited-scope or fixed-fee advice for this.</p>
<h3>Free and low-cost legal help</h3>
<p>The Court notes that the Australian Government funds legal assistance services, including <strong>Legal Aid Commissions</strong> and <strong>Community Legal Centres</strong>, which offer free and low-cost advice. Eligibility varies. The Family Relationship Advice Line (1800 050 321) can also point you to services.</p>
"""),
        ("when-mediation-may-not-be-appropriate", "unpredictable-costs", "When litigation costs cannot be predicted", """
<p>Contested court costs are hard to predict. The total depends on how many issues stay in dispute, whether experts are needed, how the other party conducts the case, and how long it takes to reach a final hearing. Treat any single &#8220;average cost&#8221; figure with caution, and ask instead for a staged estimate with clear assumptions that is updated as the matter changes.</p>
"""),
    ],
    replaces=[
        ("many family lawyers in Australia charge somewhere in the broad range of about <strong>$300 to $750+ per hour</strong>, plus GST.",
         "there is no single national rate. Ask each lawyer for their rates in writing, including for any junior lawyers or paralegals who may work on your matter, and whether figures include GST."),
        ("<p>A limited advice-only matter might cost only hundreds or a few thousand dollars. A negotiated parenting or property matter can cost many thousands. A court-based dispute that runs for a long time can cost tens of thousands of dollars per party, and sometimes far more.</p>",
         "<p>The scope of work drives the total. A limited advice-only engagement, a negotiated agreement and a contested court case are very different pieces of work, and no reliable national figure describes all of them. Ask for a written estimate for your matter and the assumptions behind it.</p>"),
        ("<p>If you are considering litigation, it is worth checking the current Federal Circuit and Family Court of Australia fee schedule directly rather than relying on outdated blog posts or copied tables. Filing fees are often modest compared with the total legal bill, but they are still part of the overall cost picture.</p>",
         f"""<p>Court filing fees are set by the Court and usually change on 1 July each year. Selected fees from the {FCFCOA_FEES} (from 1 July 2026; GST does not apply to court fees):</p>
<table>
<thead><tr><th>Application</th><th>Fee</th></tr></thead>
<tbody>
<tr><td>Application for divorce</td><td>$1,170 ($390 reduced fee if eligible)</td></tr>
<tr><td>Application for consent orders</td><td>$215</td></tr>
<tr><td>Initiating Application (parenting OR financial, final only)</td><td>$455</td></tr>
<tr><td>Initiating Application (parenting AND financial, final only)</td><td>$740</td></tr>
<tr><td>Conciliation conference</td><td>$510</td></tr>
<tr><td>Setting down for hearing (defended matter)</td><td>$820 (Div 2) / $1,115 (Div 1)</td></tr>
</tbody>
</table>
<p>Filing fees are separate from your lawyer's professional fees and are usually passed on as disbursements.</p>"""),
    ],
    faq_id="frequently-asked-questions", faq_end_id="conclusion",
    faqs_add=[
        ("Can I use a lawyer just to review an agreement?",
         "Many family lawyers offer limited-scope work, such as reviewing an agreement reached at mediation, sometimes for a fixed fee. Ask what the review covers, whether it includes advice on whether the agreement suits you, and what happens if changes are needed."),
        ("Are court filing fees included in a lawyer's quote?",
         "Not always. Court filing fees are disbursements set by the Court, such as $215 to file consent orders or $1,170 for a divorce application from 1 July 2026. Ask whether your quote includes them."),
        ("Is mediation a substitute for legal advice?",
         "No. A mediator helps you negotiate but does not advise either party. The Court recommends getting legal advice before deciding what to agree on. Many people combine mediation with targeted legal advice to keep total costs down."),
        ("Where can I ask about free legal advice?",
         "Legal Aid Commissions and Community Legal Centres offer free and low-cost advice, subject to eligibility. The Family Relationship Advice Line (1800 050 321) can also help you find services."),
    ],
)

# ─────────────────────────────────────────────────────────────────────────────
# §4.3 My partner wants me out (not on the title)
# ─────────────────────────────────────────────────────────────────────────────
patch(
    "my-partner-wants-me-out-understanding-your-rights-when-youre-not-on-the-title",
    "Understand why title, loan liability, occupation and property settlement are different questions, and when to get urgent advice after separation.",
    title="Partner Owns the House: Your Rights After Separation",
    h1="My partner owns the house and wants me out",
    inserts=[
        ("understanding-property-rights-vs-legal-title-in-au", "four-questions", "Title, mortgage, occupation and settlement are four different questions", f"""
<p>Being absent from the title does not by itself answer every family law property question. People often run four separate issues together:</p>
<div style="overflow-x:auto"><table>
<thead><tr><th>Question</th><th>What it is about</th><th>Where the answer comes from</th></tr></thead>
<tbody>
<tr><td>Title</td><td>Who is registered as owner</td><td>The land titles register in your state or territory</td></tr>
<tr><td>Mortgage</td><td>Who the lender can pursue for repayments</td><td>The loan contract: anyone who signed as a borrower or guarantor may be liable</td></tr>
<tr><td>Occupation</td><td>Who may live in the home right now</td><td>The circumstances, any court orders and, where relevant, protection orders</td></tr>
<tr><td>Property settlement</td><td>How the overall property pool is divided after separation</td><td>Agreement between you, or the Court applying the {FLA}</td></tr>
</tbody>
</table></div>
<p>Your relationship, your circumstances, any existing orders and the applicable law all matter. Get legal advice before moving out, signing documents, or assuming either of you can decide the outcome alone.</p>
"""),
        ("immediate-protections-available-now", "asked-to-leave", "If you are asked to leave urgently", """
<p><strong>Safety comes first.</strong> If you or your children are in danger, call <strong>000</strong>. For confidential support, contact <a href="https://www.1800respect.org.au/" target="_blank" rel="noopener">1800RESPECT</a> on 1800 737 732. Police and courts can make protection orders that affect who may live in the home.</p>
<p>If there is no immediate danger but you are being pressured to go, try not to make decisions on the spot. Get independent legal advice about your position before you move out, hand over keys or sign anything. Do not ignore any court order that applies to you; if an order says you must leave or stay away, follow it and get advice.</p>
"""),
        ("long-term-resolution-options", "take-to-a-lawyer", "What to take to a lawyer", """
<p>A first appointment is more useful (and often cheaper) if you bring:</p>
<ul>
<li>the property address and any title or council rates documents you can access;</li>
<li>mortgage or loan statements, and whether your name is on the loan;</li>
<li>a timeline: when you met, moved in, married (if applicable) and separated;</li>
<li>evidence of contributions, both financial (payments, renovations) and non-financial (caring for children, running the home);</li>
<li>bank, superannuation and debt information for both of you, as far as you know it;</li>
<li>copies of any court orders, protection orders or agreements;</li>
<li>any safety concerns, so advice can take them into account.</li>
</ul>
"""),
        ("how-courts-determine-property-division", "no-standard-split", "There is no standard 50/50 split", """
<p>There is no automatic 50/50 division and no fixed entitlement that comes simply from how long you were together. The Court considers what is <strong>just and equitable</strong> in the particular circumstances, looking at the property pool, contributions and future needs. Outcomes vary widely, which is why personalised advice matters.</p>
<h3>Married or de facto: why it matters</h3>
<p>Married couples and de facto couples both fall under the Family Law Act for property matters, but de facto couples must meet eligibility requirements and apply within two years of separation, while married couples generally apply within 12 months of a divorce becoming final. <strong>Western Australia</strong> is different: de facto property matters there are dealt with under WA law by the Family Court of Western Australia. Get advice about which rules apply to you.</p>
"""),
        ("special-circumstances-and-protections", "mediation-practical", "How mediation can help (without deciding your rights)", """
<p>Mediation does not decide who owns the house or what your legal entitlements are; only an agreement between you, or the Court, can do that. What mediation can do is give you both a structured, safer way to discuss practical arrangements: who stays in the home for now, how the mortgage and bills are paid in the meantime, and how you will exchange financial information. Many people get legal advice first, then use mediation to negotiate. See our <a href="/property-settlement-mediation-guide/">property settlement mediation guide</a>.</p>
"""),
    ],
    replaces=[
        ("Conclusion: You Have More Rights Than You Think</h2>", "Conclusion: get advice before you act</h2>"),
        ('Conclusion: You Have More Rights Than You Think</a>', 'Conclusion: get advice before you act</a>'),
        ("Married Couples: Strongest Protection</h3>", "Married couples</h3>"),
    ],
    faq_id="frequently-asked-questions", faq_end_id="conclusion-you-have-more-rights-than-you-think",
    faqs_add=[
        ("Does not being on the title mean I receive nothing?",
         "Not necessarily. Title records who owns the property, but a family law property settlement looks at the whole property pool, contributions and future needs. Whether you have a claim, and what it might be, depends on your relationship and circumstances, so get legal advice."),
        ("Am I liable if my name is on the mortgage?",
         "If you signed the loan as a borrower or guarantor, the lender may be able to pursue you for repayments even if you are not on the title or no longer live there. Check your loan documents and get legal and financial advice."),
        ("Should I move out before getting advice?",
         "If you are unsafe, leave and call 000. Otherwise, try to get independent legal advice before moving out, signing documents or handing over keys, because these steps can have practical consequences. Always follow any court order that applies to you."),
        ("Can mediation decide who owns the house?",
         "No. A mediator does not decide legal rights or ownership. Mediation helps you both discuss options and reach your own agreement, which can then be formalised with legal advice, for example through consent orders."),
    ],
)
