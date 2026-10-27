#!/usr/bin/env python3
"""Build-time check: HARD RULE — blog H1s are short, single-phrase titles.

Fails (exit 1) if a blog post's H1 is over 60 visible characters, has a
subtitle after ':' / ' — ' / ' – ' / ' - ', or a second sentence after '?'.
LEGACY lists posts published before the rule; they warn until shortened.
"""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
SITE = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX = 60

src = open(os.path.join(os.path.dirname(__file__), "check_authority.py")).read()
BLOG = re.findall(r"'([a-z0-9-]+)'", src[src.index("BLOG="):src.index("def content_only")])

LEGACY = {
    "cost-of-divorce-in-australia",
    "mediation-with-a-narcissist",
    "consent-orders-explained",
    "property-settlement-after-separation",
    "how-to-get-a-divorce-in-australia-a-step-by-step-guide",
    "binding-financial-agreements-guide",
    "parenting-plans-guide",
    "mediate-or-litigate",
    "child-custody-mediation",
    "separation-guide",
    "spousal-maintenance-guide",
    "child-support-guide",
    "superannuation-and-divorce",
    "high-conflict-mediation",
    "grandparents-rights",
    "shuttle-mediation-guide",
    "conciliation-vs-mediation",
    "workplace-mediation-guide",
    "property-settlement-mediation-guide",
    "family-court-process",
    "divorce-without-a-lawyer",
    "how-much-does-mediation-cost",
    "arbitration-in-family-law",
    "pets-and-family-law",
    "changes-to-family-law-act-2025",
    "stepparent-rights",
    "surrogacy-laws",
    "best-divorce-lawyers-sydney",
    "parental-alienation-australia",
    "who-pays-for-mediation",
    "private-vs-free-mediation",
    "divorce-mediator-vs-divorce-lawyer",
    "what-happens-if-mediation-fails",
    "what-is-in-the-property-pool",
    "delaying-property-settlement",
    "co-parenting-mediation",
    "online-mediation-australia",
    "victorian-right-to-work-from-home",
    "estate-inheritance-dispute-mediation",
    "my-ex-wont-sign-divorce-papers",
    "cant-afford-mediation",
    "is-family-mediation-free-australia",
    "low-cost-family-mediation-australia",
    "does-mediation-have-to-be-paid-50-50",
    "asset-rich-cash-poor-mediation",
    "family-relationship-centre-vs-private-mediation",
    "legal-aid-vs-private-mediation",
    "consent-orders-2026-update",
    "family-court-process-2026",
    "high-conflict-family-law-mediation",
    "executor-dispute-mediation",
    "property-settlement-timeline",
    "contesting-a-will-nsw",
    "elder-care-guardianship-disputes",
    "health-complaints-medical-negligence",
    "section-60i-certificate-guide",
    "relocation-with-children-after-separation",
    "what-age-can-a-child-choose-which-parent-to-live-with",
    "hiding-assets-in-divorce",
    "christmas-parenting-arrangements-after-separation",
    "how-to-change-parenting-orders",
    "who-is-responsible-for-debts-after-separation",
    "buying-out-your-ex-family-home-australia",
    "inheritance-in-property-settlement-australia",
}


def problems(t):
    out = []
    if len(t) > MAX:
        out.append(f"{len(t)} chars (max {MAX})")
    if re.search(r":\s| [—–-] ", t):
        out.append("has a subtitle")
    if re.search(r"\?\s+\S", t):
        out.append("second sentence after '?'")
    return out


fails, legacy = [], []
for slug in BLOG:
    p = os.path.join(SITE, slug, "index.html")
    if not os.path.exists(p):
        continue
    m = re.search(r"<h1[^>]*>(.*?)</h1>", open(p).read(), re.S)
    if not m:
        fails.append((slug, "no H1", ""))
        continue
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    pr = problems(t)
    if pr:
        (legacy if slug in LEGACY else fails).append((slug, "; ".join(pr), t))

print(f"=== BLOG TITLE RULE (≤{MAX} chars, one phrase) ===")
for s, why, t in legacy:
    print(f"  [LEGACY] {s}: {why}")
for s, why, t in fails:
    print(f"  [FAIL] {s}: {why}\n         \"{t}\"")
if fails:
    print("TITLE RULE FAILED — shorten the H1 (put the extra angle in the dek)")
    sys.exit(1)
print(f"ALL NEW TITLES PASS ({len(legacy)} legacy titles still to shorten)")
