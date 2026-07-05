#!/usr/bin/env python3
"""
Import blog posts from the live WordPress site.
Fetches each URL, extracts article content, generates a static HTML page
wrapped in the site's design system. Skips slugs that already exist.
"""
import os, sys, re, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(__file__))
from templates import head, nav, page_end, esc, BOOK_URL, PHONE, PHONE_HREF, DOMAIN, org_schema, breadcrumb_schema

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

URLS = [
    "https://mediationsaustralia.com.au/what-is-alimony-in-australia/",
    "https://mediationsaustralia.com.au/how-much-does-a-family-lawyer-cost-in-australia/",
    "https://mediationsaustralia.com.au/separated-under-one-roof/",
    "https://mediationsaustralia.com.au/mediation-who-pays/",
    "https://mediationsaustralia.com.au/section-79-of-the-family-law-act-1975/",
    "https://mediationsaustralia.com.au/property-settlement-after-separation/",
    "https://mediationsaustralia.com.au/mediation-with-a-narcissist/",
    "https://mediationsaustralia.com.au/family-mediation/",
    "https://mediationsaustralia.com.au/parenting-plans-example/",
    "https://mediationsaustralia.com.au/consent-orders-example/",
    "https://mediationsaustralia.com.au/who-gets-the-dog-how-mediation-resolves-pet-disputes-after-separation/",
    "https://mediationsaustralia.com.au/online-mediation-australia/",
    "https://mediationsaustralia.com.au/strata-neighbour-dispute-mediation/",
    "https://mediationsaustralia.com.au/estate-inheritance-dispute-mediation/",
    "https://mediationsaustralia.com.au/right-to-disconnect-workplace-mediation/",
    "https://mediationsaustralia.com.au/shareholder-partnership-dispute-mediation/",
    "https://mediationsaustralia.com.au/commercial-lease-dispute-mediation-australia/",
    "https://mediationsaustralia.com.au/why-your-employee-mediation-fails-how-to-make-it-work/",
    "https://mediationsaustralia.com.au/conflict-resolution-in-the-workplace/",
    "https://mediationsaustralia.com.au/contesting-a-will-in-australia-can-mediation-avoid-a-court-battle/",
    "https://mediationsaustralia.com.au/workplace-discrimination-mediation-your-options-in-australia/",
    "https://mediationsaustralia.com.au/franchise-disputes-in-australia-mediation-under-the-franchising-code-of-conduct/",
    "https://mediationsaustralia.com.au/workplace-bullying-complaints-how-mediation-can-help/",
    "https://mediationsaustralia.com.au/online-mediation-how-virtual-sessions-work-and-why-theyre-effective/",
    "https://mediationsaustralia.com.au/redundancy-and-restructuring-disputes-how-mediation-can-help/",
    "https://mediationsaustralia.com.au/how-employers-can-use-mediation-to-reduce-workplace-conflict-costs/",
    "https://mediationsaustralia.com.au/how-mediation-exposes-workplace-issues-and-how-belbin-team-roles-can-help/",
    "https://mediationsaustralia.com.au/why-workplace-conflicts-really-happen-how-mediation-resolves-them/",
    "https://mediationsaustralia.com.au/why-arbitration-might-be-the-best-way-to-resolve-your-complex-family-law-dispute/",
    "https://mediationsaustralia.com.au/shinohara-how-the-2025-family-law-changes-abolished-add-backs/",
    "https://mediationsaustralia.com.au/how-to-separate-from-your-spouse-or-partner-in-australia/",
    "https://mediationsaustralia.com.au/binding-child-support-agreements-in-australia-important-2026-update/",
    "https://mediationsaustralia.com.au/what-happens-when-property-values-change-before-your-divorce-settlement-in-australia/",
    "https://mediationsaustralia.com.au/de-facto-relationships/",
    "https://mediationsaustralia.com.au/five-things-to-do-before-uttering-i-want-a-divorce/",
    "https://mediationsaustralia.com.au/kennon-v-spry/",
    "https://mediationsaustralia.com.au/workplace-disputes-are-surging-why-early-mediation-is-the-smarter-path-forward/",
    "https://mediationsaustralia.com.au/consent-orders-2025-update/",
    "https://mediationsaustralia.com.au/50-years-of-the-family-law-act-how-mediation-has-changed-the-landscape/",
    "https://mediationsaustralia.com.au/contesting-a-will-with-mediation/",
    "https://mediationsaustralia.com.au/understanding-family-conflict-and-why-mediation-is-your-best-path-forward/",
    "https://mediationsaustralia.com.au/why-going-to-court-for-your-family-law-dispute-is-a-mistake/",
    "https://mediationsaustralia.com.au/abc-expose-the-hidden-cost-of-family-court-battles/",
    "https://mediationsaustralia.com.au/are-mediation-agreements-legally-binding/",
    "https://mediationsaustralia.com.au/binding-financial-agreement/",
    "https://mediationsaustralia.com.au/avoid-these-mistakes-with-a-binding-financial-agreement/",
    "https://mediationsaustralia.com.au/binding-financial-agreement-v-consent-orders/",
    "https://mediationsaustralia.com.au/why-mediation-works-the-science-behind-it/",
    "https://mediationsaustralia.com.au/how-long-does-mediation-take/",
    "https://mediationsaustralia.com.au/estate-dispute-mediation/",
    "https://mediationsaustralia.com.au/preparing-for-mediation/",
    "https://mediationsaustralia.com.au/binding-financial-agreement-what-you-need-to-know/",
    "https://mediationsaustralia.com.au/how-to-lodge-a-caveat-over-property-in-family-law-matters/",
    "https://mediationsaustralia.com.au/preparing-for-property-settlement-when-youre-financially-vulnerable/",
    "https://mediationsaustralia.com.au/ex-delaying-property-settlement/",
    "https://mediationsaustralia.com.au/my-partner-wants-me-out-understanding-your-rights-when-youre-not-on-the-title/",
    "https://mediationsaustralia.com.au/the-role-of-fair-work-australia-and-workplace-mediation/",
    "https://mediationsaustralia.com.au/what-is-workplace-mediation-2023-important-update/",
    "https://mediationsaustralia.com.au/what-is-section-79a-of-family-law-act/",
    "https://mediationsaustralia.com.au/divorce-fees-in-australia/",
    "https://mediationsaustralia.com.au/fathers-rights-after-separation/",
    "https://mediationsaustralia.com.au/what-is-the-difference-between-mediation-and-family-dispute-resolution/",
    "https://mediationsaustralia.com.au/conciliation-in-family-law/",
    "https://mediationsaustralia.com.au/difference-between-mediation-conciliation/",
    "https://mediationsaustralia.com.au/create-parenting-plan-that-works/",
    "https://mediationsaustralia.com.au/what-factors-do-property-settlement-lawyers-consider-when-dividing-assets/",
    "https://mediationsaustralia.com.au/property-settlement-mediation-most-effective-strategies-for-resolving-property-settlement-disputes/",
    "https://mediationsaustralia.com.au/12-essential-things-to-know-about-binding-financial-agreements-in-australia/",
    "https://mediationsaustralia.com.au/family-mediation-process-guide/",
    "https://mediationsaustralia.com.au/mediation-in-family-law-a-comprehensive-guide/",
    "https://mediationsaustralia.com.au/what-is-a-prenup-agreement-in-2024/",
    "https://mediationsaustralia.com.au/how-to-resolve-your-property-settlement-with-mediation-in-australia/",
    "https://mediationsaustralia.com.au/what-hannahs-law-means/",
    "https://mediationsaustralia.com.au/court-ordered-drug-and-alcohol-testing/",
    "https://mediationsaustralia.com.au/can-my-ex-wife-claim-money-after-divorce-in-australia/",
    "https://mediationsaustralia.com.au/what-do-i-do-if-my-former-partner-will-not-do-mediation/",
    "https://mediationsaustralia.com.au/best-apps-for-separated-parents/",
    "https://mediationsaustralia.com.au/my-ex-wont-sign-divorce-papers/",
    "https://mediationsaustralia.com.au/are-gifts-included-in-property-settlements-in-australia/",
    "https://mediationsaustralia.com.au/how-do-de-facto-couples-split-assets/",
    "https://mediationsaustralia.com.au/cryptocurrency-and-digital-assets-in-property-settlements/",
    "https://mediationsaustralia.com.au/whats-the-difference-between-a-de-facto-relationship-and-marriage/",
    "https://mediationsaustralia.com.au/de-facto-relationships-and-prenups-what-you-have-to-know/",
    "https://mediationsaustralia.com.au/changes-to-the-family-law-act-2025-you-must-know/",
    "https://mediationsaustralia.com.au/investment-property-division-in-family-law-disputes/",
    "https://mediationsaustralia.com.au/family-law-mediator/",
    "https://mediationsaustralia.com.au/what-are-procedural-orders-in-family-court/",
    "https://mediationsaustralia.com.au/how-to-apply-file-for-get-a-divorce-in-western-australia-wa/",
    "https://mediationsaustralia.com.au/how-often-do-fathers-get-50-50-custody-in-australia/",
    "https://mediationsaustralia.com.au/postnuptial-agreement-australia-everything-you-need-to-know/",
    "https://mediationsaustralia.com.au/how-long-do-consent-orders-take/",
    "https://mediationsaustralia.com.au/property-in-divorce-settlement/",
    "https://mediationsaustralia.com.au/the-pros-and-cons-of-shuttle-mediation/",
    "https://mediationsaustralia.com.au/what-am-i-entitled-to-in-a-separation-in-australia/",
    "https://mediationsaustralia.com.au/property-settlement-after-separation-time-limit/",
    "https://mediationsaustralia.com.au/what-is-a-litigation-guardian-in-australia/",
    "https://mediationsaustralia.com.au/when-is-mediation-not-a-good-idea/",
    "https://mediationsaustralia.com.au/what-is-the-magellan-list/",
    "https://mediationsaustralia.com.au/how-to-get-a-divorce-in-australia-a-step-by-step-guide/",
    "https://mediationsaustralia.com.au/cost-of-divorce-in-australia/",
    "https://mediationsaustralia.com.au/family-loan-agreement-matters/",
    "https://mediationsaustralia.com.au/supporting-your-child-through-parents-separation-a-comprehensive-guide-for-australian-families/",
    "https://mediationsaustralia.com.au/separation-or-divorce-which-is-better/",
    "https://mediationsaustralia.com.au/12-best-strategies-for-effective-parenting-plans-in-australia/",
    "https://mediationsaustralia.com.au/same-sex-divorce-in-australia/",
    "https://mediationsaustralia.com.au/can-you-sue-a-family-trust-in-australia/",
    "https://mediationsaustralia.com.au/australia-lgbt-marriage-mediation/",
    "https://mediationsaustralia.com.au/what-is-an-avo/",
    "https://mediationsaustralia.com.au/spousal-maintenance/",
    "https://mediationsaustralia.com.au/fathers-rights-in-family-law-2022-update/",
    "https://mediationsaustralia.com.au/how-to-get-a-divorce-in-new-south-wales/",
    "https://mediationsaustralia.com.au/child-support-payments-and-taxes/",
    "https://mediationsaustralia.com.au/prenups-for-women/",
    "https://mediationsaustralia.com.au/trial-separation/",
    "https://mediationsaustralia.com.au/divorce-without-lawyers/",
    "https://mediationsaustralia.com.au/parental-alienation-australia-dont-let-your-ex-destroy-your-childs-love-for-you/",
    "https://mediationsaustralia.com.au/five-benefits-of-using-mediation-to-resolve-divorce-issues/",
    "https://mediationsaustralia.com.au/mediation-vs-collaborative-law/",
    "https://mediationsaustralia.com.au/family-law-mediation-what-happens-if-i-dont-want-to-do-it/",
    "https://mediationsaustralia.com.au/what-to-expect-at-a-family-law-mediation-for-property-division/",
    "https://mediationsaustralia.com.au/attend-mediation-in-family-law-matters/",
    "https://mediationsaustralia.com.au/is-family-law-mediation-compulsory/",
    "https://mediationsaustralia.com.au/family-law-mediation-for-property-settlements/",
    "https://mediationsaustralia.com.au/superannuation-and-family-law-important-2024-update/",
    "https://mediationsaustralia.com.au/understanding-mediation-2024/",
    "https://mediationsaustralia.com.au/what-is-the-average-split-in-a-divorce-settlement-australia/",
    "https://mediationsaustralia.com.au/getting-divorced-or-separated-the-2022-guide/",
    "https://mediationsaustralia.com.au/who-pays-bills-during-separation/",
    "https://mediationsaustralia.com.au/what-happens-to-superannuation-if-i-separate-or-divorce/",
    "https://mediationsaustralia.com.au/in-a-divorce-who-gets-what/",
    "https://mediationsaustralia.com.au/60-40-split-divorce-australia/",
    "https://mediationsaustralia.com.au/divorce-without-a-lawyer/",
    "https://mediationsaustralia.com.au/the-cost-of-divorce-in-australia/",
    "https://mediationsaustralia.com.au/high-conflict-family-law-mediation/",
    "https://mediationsaustralia.com.au/how-long-does-a-divorce-take/",
    "https://mediationsaustralia.com.au/divorce-property-settlement-your-best-options-in-2022/",
    "https://mediationsaustralia.com.au/points-to-consider-family-mediation-lawyers-in-australia/",
    "https://mediationsaustralia.com.au/family-court-mediation-process/",
    "https://mediationsaustralia.com.au/understanding-divorce-laws-in-nsw/",
    "https://mediationsaustralia.com.au/mediate-collaborate-or-litigate/",
    "https://mediationsaustralia.com.au/the-different-ways-to-resolve-family-law-disputes/",
    "https://mediationsaustralia.com.au/post-prenup-agreement/",
    "https://mediationsaustralia.com.au/joint-tenancy-and-divorce/",
    "https://mediationsaustralia.com.au/applying-for-a-divorce-in-australia/",
    "https://mediationsaustralia.com.au/property-settlement-in-family-law/",
    "https://mediationsaustralia.com.au/divorce-certificate-in-australia/",
    "https://mediationsaustralia.com.au/understanding-property-settlement-in-divorce-a-guide-to-private-agreements/",
    "https://mediationsaustralia.com.au/what-is-mediation-in-family-law/",
    "https://mediationsaustralia.com.au/stepparent-rights-and-family-law-in-australia/",
    "https://mediationsaustralia.com.au/what-are-family-reports-in-family-law-matters/",
    "https://mediationsaustralia.com.au/what-are-the-mothers-rights-in-family-law/",
    "https://mediationsaustralia.com.au/how-property-settlements-work/",
    "https://mediationsaustralia.com.au/how-to-force-a-property-settlement/",
    "https://mediationsaustralia.com.au/mediate-workplace-conflict-in-australia/",
    "https://mediationsaustralia.com.au/how-to-get-ready-for-property-settlement-mediation/",
    "https://mediationsaustralia.com.au/mediation-in-property-settlement-cases/",
    "https://mediationsaustralia.com.au/when-should-we-consider-property-settlement-mediation/",
    "https://mediationsaustralia.com.au/domestic-violence/",
    "https://mediationsaustralia.com.au/what-is-a-restraining-order/",
    "https://mediationsaustralia.com.au/arbitration-in-family-law/",
    "https://mediationsaustralia.com.au/the-marriage-separation-process-in-nsw/",
    "https://mediationsaustralia.com.au/consent-order/",
    "https://mediationsaustralia.com.au/how-do-i-change-a-consent-order/",
    "https://mediationsaustralia.com.au/breach-of-family-court-order/",
    "https://mediationsaustralia.com.au/surrogacy-laws-in-australia-2024/",
    "https://mediationsaustralia.com.au/family-law-separation-agreements-the-2024-guide/",
    "https://mediationsaustralia.com.au/application-for-divorce/",
    "https://mediationsaustralia.com.au/what-is-child-custody-mediation/",
    "https://mediationsaustralia.com.au/what-is-a-dvo-everything-you-need-to-know/",
    "https://mediationsaustralia.com.au/intervention-orders/",
    "https://mediationsaustralia.com.au/mediation-or-litigation-what-is-the-best/",
    "https://mediationsaustralia.com.au/what-happens-to-business-in-divorce/",
    "https://mediationsaustralia.com.au/family-court-process-2024-update/",
    "https://mediationsaustralia.com.au/joint-divorce-application/",
    "https://mediationsaustralia.com.au/what-you-need-to-know-about-parenting-plans/",
    "https://mediationsaustralia.com.au/role-of-a-mediator-divorce-mediation/",
    "https://mediationsaustralia.com.au/difference-mediator-and-conciliator/",
    "https://mediationsaustralia.com.au/what-is-a-dvo-how-to-apply-for-a-domestic-violence-order/",
    "https://mediationsaustralia.com.au/divorce-property-settlement-examples-in-australia/",
    "https://mediationsaustralia.com.au/family-law-regulations-explained/",
    "https://mediationsaustralia.com.au/divorce-application-process/",
    "https://mediationsaustralia.com.au/grandparents-rights-how-to-see-your-grandchildren-2022-update/",
    "https://mediationsaustralia.com.au/how-much-does-mediation-cost/",
    "https://mediationsaustralia.com.au/shuttle-mediation/",
    "https://mediationsaustralia.com.au/how-do-i-contact-centrelink/",
    "https://mediationsaustralia.com.au/parenting-plan-vs-parenting-order/",
    "https://mediationsaustralia.com.au/best-divorce-lawyers-in-sydney/",
    "https://mediationsaustralia.com.au/travel-overseas-after-a-separation/",
    "https://mediationsaustralia.com.au/how-are-assets-divided-in-a-divorce/",
    "https://mediationsaustralia.com.au/mediation-for-separation/",
    "https://mediationsaustralia.com.au/does-a-husband-have-to-support-his-wife/",
    "https://mediationsaustralia.com.au/who-gets-to-stay-in-the-house-during-separation/",
    "https://mediationsaustralia.com.au/when-child-support-stops-guide/",
    "https://mediationsaustralia.com.au/grandparents-custody-in-australia/",
    "https://mediationsaustralia.com.au/what-am-i-entitled-to-in-a-separation/",
    "https://mediationsaustralia.com.au/what-is-divorce-law-in-australia/",
    "https://mediationsaustralia.com.au/separation-lawyer-sydney/",
    "https://mediationsaustralia.com.au/im-contemplating-separation-do-i-see-a-lawyer-or-a-mediation-practice-first/",
    "https://mediationsaustralia.com.au/the-7-most-common-questions-about-mediation/",
    "https://mediationsaustralia.com.au/5-reasons-why-you-should-consider-mediation-for-child-custody-disputes/",
    # sitemap2
    "https://mediationsaustralia.com.au/the-role-of-the-lawyer-in-mediation/",
    "https://mediationsaustralia.com.au/why-you-have-to-update-your-will-after-separation/",
    "https://mediationsaustralia.com.au/what-do-i-need-to-disclose-in-my-property-settlement-dispute/",
    "https://mediationsaustralia.com.au/how-to-resolve-your-family-law-dispute-online/",
    "https://mediationsaustralia.com.au/how-to-prepare-for-a-property-settlement-mediation/",
    "https://mediationsaustralia.com.au/what-am-i-entitled-to-in-a-divorce-or-separation-in-australia/",
    "https://mediationsaustralia.com.au/how-long-does-it-take-to-get-a-divorce/",
    "https://mediationsaustralia.com.au/can-you-record-your-ex-without-permission/",
    "https://mediationsaustralia.com.au/what-is-the-role-of-an-independent-childrens-lawyer/",
    "https://mediationsaustralia.com.au/what-you-need-to-know-about-parenting-coordination-2022-update/",
    "https://mediationsaustralia.com.au/what-if-my-ex-dies-before-our-property-settlement-is-finalised/",
    "https://mediationsaustralia.com.au/pre-separation-checklist/",
    "https://mediationsaustralia.com.au/the-difference-between-a-divorce-lawyer-and-a-mediator/",
    "https://mediationsaustralia.com.au/how-to-sell-property-during-a-divorce/",
    "https://mediationsaustralia.com.au/commonly-asked-family-law-questions/",
    "https://mediationsaustralia.com.au/final-hearing-in-family-law-disputes/",
    "https://mediationsaustralia.com.au/how-to-make-changes-to-a-parenting-order/",
    "https://mediationsaustralia.com.au/how-to-protect-your-online-privacy-following-separation/",
    "https://mediationsaustralia.com.au/duty-of-disclosure-in-australian-family-law/",
    "https://mediationsaustralia.com.au/divorce-law-near-me/",
    "https://mediationsaustralia.com.au/how-long-do-consent-orders-take-in-family-law-matters/",
    "https://mediationsaustralia.com.au/parenting-payments-in-australia/",
    "https://mediationsaustralia.com.au/when-should-i-think-about-parenting-mediation-or-custody-mediation/",
    "https://mediationsaustralia.com.au/how-to-get-divorce-papers-the-2022-guide/",
    "https://mediationsaustralia.com.au/how-are-contributions-assessed-in-family-law-matters-2/",
    "https://mediationsaustralia.com.au/nothing-alternate-about-alternate-dispute-resolution-adr/",
    "https://mediationsaustralia.com.au/how-to-convince-your-ex-partner-to-do-mediation/",
    "https://mediationsaustralia.com.au/how-to-get-ready-for-mediation/",
    "https://mediationsaustralia.com.au/litigation-or-mediation-choose-very-wisely/",
    "https://mediationsaustralia.com.au/how-does-mediation-help-co-parenting/",
    "https://mediationsaustralia.com.au/is-mediation-expensive/",
    "https://mediationsaustralia.com.au/becoming-independent-sooner-how-mediation-can-help-you-agree-on-spousal-support/",
    "https://mediationsaustralia.com.au/how-mediation-can-help-in-financial-agreements/",
    "https://mediationsaustralia.com.au/how-you-can-reach-an-agreement-in-mediation/",
    "https://mediationsaustralia.com.au/costs-of-going-to-court/",
    "https://mediationsaustralia.com.au/how-are-contributions-assessed-in-family-law-matters/",
    "https://mediationsaustralia.com.au/what-is-included-in-a-matrimonial-property-pool/",
    "https://mediationsaustralia.com.au/what-is-a-section-60i-certificate-why-do-i-need-one/",
    "https://mediationsaustralia.com.au/pets-and-family-law-who-gets-the-pets-after-separation/",
]


def fetch_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SiteImporter/1.0)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", errors="replace")


def extract_meta_title(html):
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not m:
        return ""
    t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    t = re.sub(r"\s*[|–—-]\s*(Mediations Australia|Mediation Australia).*$", "", t, flags=re.I).strip()
    return t


def extract_meta_desc(html):
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
    if not m:
        m = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.I | re.S)
    return m.group(1).strip() if m else ""


def extract_h1(html):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def extract_article_body(html):
    for pat in [
        r'<div[^>]+class="[^"]*entry-content[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</article',
        r'<div[^>]+class="[^"]*post-content[^"]*"[^>]*>(.*?)(?=<(?:div|section|footer)[^>]+class="[^"]*(?:post-footer|author|related|sidebar)[^"]*")',
        r"<article[^>]*>(.*?)</article>",
    ]:
        m = re.search(pat, html, re.S | re.I)
        if m:
            body = m.group(1).strip()
            if len(body) > 200:
                return body
    return ""


def clean_body(html):
    html = re.sub(r'href="https://mediationsaustralia\.com\.au/([^"]*)"', r'href="/\1"', html)
    html = re.sub(r"\[/?[a-z_]+[^\]]*\]", "", html)
    html = re.sub(r'\s*style="[^"]*"', "", html)
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S | re.I)
    html = re.sub(r"<p>\s*</p>", "", html)
    html = re.sub(r'<figure[^>]*class="[^"]*wp-block-image[^"]*"[^>]*>', "<figure>", html)
    html = re.sub(r"<h1[^>]*>.*?</h1>", "", html, flags=re.S | re.I)
    # Strip all images and figures — WP media library images don't carry over
    html = re.sub(r"<figure[^>]*>.*?</figure>", "", html, flags=re.S | re.I)
    html = re.sub(r"<img[^>]*/?>", "", html, flags=re.I)
    html = re.sub(r"<div[^>]+class=\"[^\"]*wp-block-[^\"]*\"[^>]*>", "<div>", html, flags=re.I)
    return html.strip()


def truncate(s, limit):
    if len(s) <= limit:
        return s
    return s[: limit - 1].rsplit(" ", 1)[0] + "…"


def build_page(url, slug):
    html = fetch_html(url)
    title = extract_meta_title(html)
    desc = extract_meta_desc(html)
    h1_raw = extract_h1(html)
    body = extract_article_body(html)

    if not title:
        title = slug.replace("-", " ").title()
    if not h1_raw:
        h1_raw = title

    body = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", body, flags=re.S | re.I)
    body = clean_body(body)

    title = truncate(title, 60)
    desc = truncate(desc, 160) if desc else truncate(title + " — Mediations Australia.", 160)

    schema = [org_schema(), breadcrumb_schema([("Home", ""), ("Guides", "guides"), (h1_raw, None)])]
    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += f"""<main id="main">
<div class="wrap-narrow" style="padding:clamp(40px,6vw,72px) 0 clamp(56px,7vw,96px)">
  <nav class="crumb" aria-label="Breadcrumb">
    <a href="/">Home</a> <span aria-hidden="true">›</span>
    <a href="/guides/">Guides</a> <span aria-hidden="true">›</span>
    <span>{esc(h1_raw)}</span>
  </nav>
  <h1 style="margin-top:24px">{esc(h1_raw)}</h1>
  <div class="body-import">
{body}
  </div>
  <div class="cta-inline" style="margin-top:48px;padding:32px;background:var(--sage-light);border-radius:16px">
    <p><strong>Need help resolving your dispute?</strong> Our accredited mediators can help — book a free consultation today.</p>
    <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
  </div>
</div>
</main>"""
    doc += page_end()

    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)


# ── Main ──────────────────────────────────────────────────────────────────────

existing = {d for d in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, d))}

seen_slugs: set = set()
unique_urls = []
for url in URLS:
    slug = url.rstrip("/").split("/")[-1]
    if slug not in seen_slugs:
        seen_slugs.add(slug)
        unique_urls.append((url, slug))

built, skipped, failed = [], [], []
total = len(unique_urls)

for i, (url, slug) in enumerate(unique_urls, 1):
    if slug in existing:
        skipped.append(slug)
        continue
    try:
        build_page(url, slug)
        built.append(slug)
        print(f"  [{i}/{total}] OK  {slug}")
    except Exception as e:
        failed.append((slug, str(e)))
        print(f"  [{i}/{total}] FAIL {slug}: {e}")
    time.sleep(0.25)

print(f"\nDone. Built: {len(built)}  |  Skipped (already exist): {len(skipped)}  |  Failed: {len(failed)}")
if failed:
    print("Failed slugs:")
    for s, e in failed:
        print(f"  {s}: {e}")
