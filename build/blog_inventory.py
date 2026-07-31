#!/usr/bin/env python3
"""Complete blog inventory from post-sitemap1 + post-sitemap2, with consolidation plan."""

# All ~201 post slugs from the two sitemaps
SITEMAP1 = [
"family-mediation","understanding-family-conflict-and-why-mediation-is-your-best-path-forward",
"why-going-to-court-for-your-family-law-dispute-is-a-mistake","are-mediation-agreements-legally-binding",
"binding-financial-agreement","avoid-these-mistakes-with-a-binding-financial-agreement",
"binding-financial-agreement-v-consent-orders","why-mediation-works-the-science-behind-it",
"how-long-does-mediation-take","abc-expose-the-hidden-cost-of-family-court-battles","mediation-who-pays",
"estate-dispute-mediation","preparing-for-mediation","binding-financial-agreement-what-you-need-to-know",
"how-to-lodge-a-caveat-over-property-in-family-law-matters","preparing-for-property-settlement-when-youre-financially-vulnerable",
"ex-delaying-property-settlement","my-partner-wants-me-out-understanding-your-rights-when-youre-not-on-the-title",
"the-role-of-fair-work-australia-and-workplace-mediation","what-is-workplace-mediation-2023-important-update",
"consent-orders-2025-update","what-is-section-79a-of-family-law-act","divorce-fees-in-australia",
"fathers-rights-after-separation","what-is-the-difference-between-mediation-and-family-dispute-resolution",
"conciliation-in-family-law","difference-between-mediation-conciliation","create-parenting-plan-that-works",
"what-factors-do-property-settlement-lawyers-consider-when-dividing-assets",
"property-settlement-mediation-most-effective-strategies-for-resolving-property-settlement-disputes",
"12-essential-things-to-know-about-binding-financial-agreements-in-australia","parenting-plans-example",
"family-mediation-process-guide","mediation-in-family-law-a-comprehensive-guide","what-is-a-prenup-agreement-in-2024",
"how-to-resolve-your-property-settlement-with-mediation-in-australia","separated-under-one-roof","what-hannahs-law-means",
"court-ordered-drug-and-alcohol-testing","can-my-ex-wife-claim-money-after-divorce-in-australia",
"what-do-i-do-if-my-former-partner-will-not-do-mediation","best-apps-for-separated-parents","my-ex-wont-sign-divorce-papers",
"are-gifts-included-in-property-settlements-in-australia","de-facto-relationships","how-do-de-facto-couples-split-assets",
"cryptocurrency-and-digital-assets-in-property-settlements","whats-the-difference-between-a-de-facto-relationship-and-marriage",
"de-facto-relationships-and-prenups-what-you-have-to-know","changes-to-the-family-law-act-2025-you-must-know",
"investment-property-division-in-family-law-disputes","family-law-mediator","what-are-procedural-orders-in-family-court",
"how-to-apply-file-for-get-a-divorce-in-western-australia-wa","how-often-do-fathers-get-50-50-custody-in-australia",
"postnuptial-agreement-australia-everything-you-need-to-know","consent-orders-example","how-long-do-consent-orders-take",
"property-in-divorce-settlement","the-pros-and-cons-of-shuttle-mediation","what-am-i-entitled-to-in-a-separation-in-australia",
"property-settlement-after-separation-time-limit","what-is-a-litigation-guardian-in-australia","when-is-mediation-not-a-good-idea",
"how-much-does-a-family-lawyer-cost-in-australia","what-is-the-magellan-list","how-to-get-a-divorce-in-australia-a-step-by-step-guide",
"cost-of-divorce-in-australia","property-settlement-after-separation","family-loan-agreement-matters",
"supporting-your-child-through-parents-separation-a-comprehensive-guide-for-australian-families",
"separation-or-divorce-which-is-better","12-best-strategies-for-effective-parenting-plans-in-australia",
"same-sex-divorce-in-australia","can-you-sue-a-family-trust-in-australia","australia-lgbt-marriage-mediation","what-is-an-avo",
"spousal-maintenance","mediation-with-a-narcissist","fathers-rights-in-family-law-2022-update","how-to-get-a-divorce-in-new-south-wales",
"child-support-payments-and-taxes","prenups-for-women","trial-separation","divorce-without-lawyers",
"parental-alienation-australia-dont-let-your-ex-destroy-your-childs-love-for-you","five-benefits-of-using-mediation-to-resolve-divorce-issues",
"mediation-vs-collaborative-law","family-law-mediation-what-happens-if-i-dont-want-to-do-it",
"what-to-expect-at-a-family-law-mediation-for-property-division","attend-mediation-in-family-law-matters",
"is-family-law-mediation-compulsory","family-law-mediation-for-property-settlements","superannuation-and-family-law-important-2024-update",
"understanding-mediation-2024","what-is-the-average-split-in-a-divorce-settlement-australia","getting-divorced-or-separated-the-2022-guide",
"who-pays-bills-during-separation","what-happens-to-superannuation-if-i-separate-or-divorce","in-a-divorce-who-gets-what",
"60-40-split-divorce-australia","divorce-without-a-lawyer","the-cost-of-divorce-in-australia","high-conflict-family-law-mediation",
"how-long-does-a-divorce-take","divorce-property-settlement-your-best-options-in-2022","points-to-consider-family-mediation-lawyers-in-australia",
"section-79-of-the-family-law-act-1975","family-court-mediation-process","understanding-divorce-laws-in-nsw","mediate-collaborate-or-litigate",
"the-different-ways-to-resolve-family-law-disputes","post-prenup-agreement","joint-tenancy-and-divorce","applying-for-a-divorce-in-australia",
"property-settlement-in-family-law","divorce-certificate-in-australia","understanding-property-settlement-in-divorce-a-guide-to-private-agreements",
"what-is-mediation-in-family-law","stepparent-rights-and-family-law-in-australia","what-are-family-reports-in-family-law-matters",
"what-are-the-mothers-rights-in-family-law","how-property-settlements-work","how-to-force-a-property-settlement","mediate-workplace-conflict-in-australia",
"how-to-get-ready-for-property-settlement-mediation","mediation-in-property-settlement-cases","when-should-we-consider-property-settlement-mediation",
"domestic-violence","what-is-a-restraining-order","arbitration-in-family-law","the-marriage-separation-process-in-nsw","consent-order",
"how-do-i-change-a-consent-order","breach-of-family-court-order","surrogacy-laws-in-australia-2024","family-law-separation-agreements-the-2024-guide",
"application-for-divorce","what-is-child-custody-mediation","what-is-a-dvo-everything-you-need-to-know","intervention-orders",
"mediation-or-litigation-what-is-the-best","what-happens-to-business-in-divorce","family-court-process-2024-update","joint-divorce-application",
"what-you-need-to-know-about-parenting-plans","role-of-a-mediator-divorce-mediation","difference-mediator-and-conciliator",
"what-is-a-dvo-how-to-apply-for-a-domestic-violence-order","divorce-property-settlement-examples-in-australia","family-law-regulations-explained",
"divorce-application-process","grandparents-rights-how-to-see-your-grandchildren-2022-update","what-is-alimony-in-australia","how-much-does-mediation-cost",
"shuttle-mediation","how-do-i-contact-centrelink","parenting-plan-vs-parenting-order","best-divorce-lawyers-in-sydney","travel-overseas-after-a-separation",
"how-are-assets-divided-in-a-divorce","mediation-for-separation","does-a-husband-have-to-support-his-wife","who-gets-to-stay-in-the-house-during-separation",
"when-child-support-stops-guide","grandparents-custody-in-australia","what-am-i-entitled-to-in-a-separation","what-is-divorce-law-in-australia",
"separation-lawyer-sydney","im-contemplating-separation-do-i-see-a-lawyer-or-a-mediation-practice-first","the-7-most-common-questions-about-mediation",
"5-reasons-why-you-should-consider-mediation-for-child-custody-disputes","the-role-of-the-lawyer-in-mediation","why-you-have-to-update-your-will-after-separation",
"what-do-i-need-to-disclose-in-my-property-settlement-dispute","how-to-resolve-your-family-law-dispute-online","how-to-prepare-for-a-property-settlement-mediation",
"what-am-i-entitled-to-in-a-divorce-or-separation-in-australia","how-long-does-it-take-to-get-a-divorce","can-you-record-your-ex-without-permission",
"what-is-the-role-of-an-independent-childrens-lawyer","what-you-need-to-know-about-parenting-coordination-2022-update","what-if-my-ex-dies-before-our-property-settlement-is-finalised",
"pre-separation-checklist","the-difference-between-a-divorce-lawyer-and-a-mediator","how-to-sell-property-during-a-divorce","commonly-asked-family-law-questions",
"final-hearing-in-family-law-disputes","how-to-make-changes-to-a-parenting-order","how-to-protect-your-online-privacy-following-separation",
"duty-of-disclosure-in-australian-family-law","divorce-law-near-me","how-long-do-consent-orders-take-in-family-law-matters","parenting-payments-in-australia",
"when-should-i-think-about-parenting-mediation-or-custody-mediation","how-to-get-divorce-papers-the-2022-guide","how-are-contributions-assessed-in-family-law-matters-2",
"nothing-alternate-about-alternate-dispute-resolution-adr","how-to-convince-your-ex-partner-to-do-mediation","how-to-get-ready-for-mediation",
]
SITEMAP2 = [
"litigation-or-mediation-choose-very-wisely","how-does-mediation-help-co-parenting","is-mediation-expensive",
"becoming-independent-sooner-how-mediation-can-help-you-agree-on-spousal-support","how-mediation-can-help-in-financial-agreements",
"how-you-can-reach-an-agreement-in-mediation","costs-of-going-to-court","how-are-contributions-assessed-in-family-law-matters",
"what-is-included-in-a-matrimonial-property-pool","what-is-a-section-60i-certificate-why-do-i-need-one","pets-and-family-law-who-gets-the-pets-after-separation",
]
ALL = SITEMAP1 + SITEMAP2
print(f"Total posts in sitemaps: {len(ALL)}")

# ============================================================
# CONSOLIDATION PLAN
# Each CLUSTER = one canonical cornerstone post that absorbs several old posts.
# Old posts in the cluster -> 301 redirect to the canonical.
# ============================================================
CLUSTERS = {
 # CANONICAL SLUG : (Title, [old slugs to consolidate/redirect into it])
 "cost-of-divorce-in-australia": ("How Much Does Divorce Cost in Australia?",
   ["the-cost-of-divorce-in-australia","divorce-fees-in-australia","costs-of-going-to-court","how-much-does-a-family-lawyer-cost-in-australia"]),
 "how-much-does-mediation-cost": ("How Much Does Mediation Cost?",
   ["mediation-who-pays","is-mediation-expensive","how-much-does-mediation-cost"]),
 "what-am-i-entitled-to-in-a-separation-in-australia": ("What Am I Entitled To in a Separation?",
   ["what-am-i-entitled-to-in-a-separation","what-am-i-entitled-to-in-a-divorce-or-separation-in-australia",
    "in-a-divorce-who-gets-what","what-is-the-average-split-in-a-divorce-settlement-australia",
    "60-40-split-divorce-australia","how-are-assets-divided-in-a-divorce","can-my-ex-wife-claim-money-after-divorce-in-australia",
    "does-a-husband-have-to-support-his-wife"]),
 "property-settlement-after-separation": ("Property Settlement After Separation",
   ["property-in-divorce-settlement","property-settlement-in-family-law","how-property-settlements-work",
    "understanding-property-settlement-in-divorce-a-guide-to-private-agreements","divorce-property-settlement-your-best-options-in-2022",
    "divorce-property-settlement-examples-in-australia","property-settlement-after-separation-time-limit",
    "what-factors-do-property-settlement-lawyers-consider-when-dividing-assets","how-to-force-a-property-settlement",
    "what-do-i-need-to-disclose-in-my-property-settlement-dispute","duty-of-disclosure-in-australian-family-law",
    "what-is-included-in-a-matrimonial-property-pool","how-are-contributions-assessed-in-family-law-matters",
    "how-are-contributions-assessed-in-family-law-matters-2","are-gifts-included-in-property-settlements-in-australia",
    "investment-property-division-in-family-law-disputes","cryptocurrency-and-digital-assets-in-property-settlements",
    "how-to-sell-property-during-a-divorce","joint-tenancy-and-divorce","how-to-lodge-a-caveat-over-property-in-family-law-matters",
    "what-if-my-ex-dies-before-our-property-settlement-is-finalised","ex-delaying-property-settlement",
    "preparing-for-property-settlement-when-youre-financially-vulnerable","my-partner-wants-me-out-understanding-your-rights-when-youre-not-on-the-title",
    "section-79-of-the-family-law-act-1975","what-is-section-79a-of-family-law-act"]),
 "property-settlement-mediation-guide": ("Property Settlement Mediation: Full Guide",
   ["mediation-in-property-settlement-cases","when-should-we-consider-property-settlement-mediation",
    "how-to-get-ready-for-property-settlement-mediation","how-to-prepare-for-a-property-settlement-mediation",
    "what-to-expect-at-a-family-law-mediation-for-property-division","family-law-mediation-for-property-settlements",
    "property-settlement-mediation-most-effective-strategies-for-resolving-property-settlement-disputes",
    "how-to-resolve-your-property-settlement-with-mediation-in-australia"]),
 "how-to-get-a-divorce-in-australia-a-step-by-step-guide": ("How to Get a Divorce in Australia",
   ["applying-for-a-divorce-in-australia","application-for-divorce","divorce-application-process","how-to-get-divorce-papers-the-2022-guide",
    "joint-divorce-application","getting-divorced-or-separated-the-2022-guide","what-is-divorce-law-in-australia",
    "how-to-get-a-divorce-in-new-south-wales","how-to-apply-file-for-get-a-divorce-in-western-australia-wa",
    "understanding-divorce-laws-in-nsw","the-marriage-separation-process-in-nsw","divorce-certificate-in-australia",
    "my-ex-wont-sign-divorce-papers","divorce-law-near-me"]),
 "how-long-does-a-divorce-take": ("How Long Does a Divorce Take?",
   ["how-long-does-it-take-to-get-a-divorce"]),
 "consent-orders-explained": ("Consent Orders Explained",
   ["consent-order","consent-orders-example","consent-orders-2025-update","how-do-i-change-a-consent-order",
    "how-long-do-consent-orders-take","how-long-do-consent-orders-take-in-family-law-matters","breach-of-family-court-order"]),
 "binding-financial-agreements-guide": ("Binding Financial Agreements: Complete Guide",
   ["binding-financial-agreement","binding-financial-agreement-what-you-need-to-know","avoid-these-mistakes-with-a-binding-financial-agreement",
    "binding-financial-agreement-v-consent-orders","12-essential-things-to-know-about-binding-financial-agreements-in-australia",
    "what-is-a-prenup-agreement-in-2024","prenups-for-women","post-prenup-agreement","postnuptial-agreement-australia-everything-you-need-to-know",
    "de-facto-relationships-and-prenups-what-you-have-to-know","how-mediation-can-help-in-financial-agreements"]),
 "parenting-plans-guide": ("Parenting Plans in Australia: Complete Guide",
   ["what-you-need-to-know-about-parenting-plans","create-parenting-plan-that-works","parenting-plans-example",
    "12-best-strategies-for-effective-parenting-plans-in-australia","parenting-plan-vs-parenting-order",
    "how-to-make-changes-to-a-parenting-order","what-you-need-to-know-about-parenting-coordination-2022-update",
    "best-apps-for-separated-parents"]),
 "child-custody-mediation": ("Child Custody Mediation",
   ["what-is-child-custody-mediation","5-reasons-why-you-should-consider-mediation-for-child-custody-disputes",
    "when-should-i-think-about-parenting-mediation-or-custody-mediation","how-often-do-fathers-get-50-50-custody-in-australia",
    "what-is-the-role-of-an-independent-childrens-lawyer","what-are-family-reports-in-family-law-matters",
    "supporting-your-child-through-parents-separation-a-comprehensive-guide-for-australian-families",
    "how-does-mediation-help-co-parenting"]),
 "fathers-rights": ("Fathers' Rights After Separation",
   ["fathers-rights-after-separation","fathers-rights-in-family-law-2022-update"]),
 "mothers-rights": ("Mothers' Rights in Family Law", ["what-are-the-mothers-rights-in-family-law"]),
 "grandparents-rights": ("Grandparents' Rights",
   ["grandparents-rights-how-to-see-your-grandchildren-2022-update","grandparents-custody-in-australia"]),
 "spousal-maintenance-guide": ("Spousal Maintenance in Australia",
   ["spousal-maintenance","what-is-alimony-in-australia","becoming-independent-sooner-how-mediation-can-help-you-agree-on-spousal-support"]),
 "child-support-guide": ("Child Support in Australia",
   ["child-support-payments-and-taxes","when-child-support-stops-guide","parenting-payments-in-australia","how-do-i-contact-centrelink"]),
 "de-facto-relationships-guide": ("De Facto Relationships & Separation",
   ["de-facto-relationships","how-do-de-facto-couples-split-assets","whats-the-difference-between-a-de-facto-relationship-and-marriage"]),
 "superannuation-and-divorce": ("Superannuation & Divorce",
   ["superannuation-and-family-law-important-2024-update","what-happens-to-superannuation-if-i-separate-or-divorce"]),
 "separation-guide": ("Separation in Australia: What to Know",
   ["trial-separation","separation-or-divorce-which-is-better","who-pays-bills-during-separation","who-gets-to-stay-in-the-house-during-separation",
    "pre-separation-checklist","travel-overseas-after-a-separation","why-you-have-to-update-your-will-after-separation",
    "how-to-protect-your-online-privacy-following-separation","family-law-separation-agreements-the-2024-guide"]),
 "what-is-mediation-in-family-law": ("What Is Mediation in Family Law?",
   ["mediation-in-family-law-a-comprehensive-guide","understanding-mediation-2024","family-mediation",
    "family-mediation-process-guide","mediation-for-separation","the-7-most-common-questions-about-mediation",
    "why-mediation-works-the-science-behind-it","understanding-family-conflict-and-why-mediation-is-your-best-path-forward",
    "how-you-can-reach-an-agreement-in-mediation","role-of-a-mediator-divorce-mediation","family-law-mediator","family-court-mediation-process"]),
 "is-family-law-mediation-compulsory": ("Is Family Law Mediation Compulsory?",
   ["is-family-law-mediation-compulsory","attend-mediation-in-family-law-matters","family-law-mediation-what-happens-if-i-dont-want-to-do-it",
    "what-do-i-do-if-my-former-partner-will-not-do-mediation","how-to-convince-your-ex-partner-to-do-mediation",
    "what-is-the-difference-between-mediation-and-family-dispute-resolution","what-is-a-section-60i-certificate-why-do-i-need-one"]),
 "mediate-or-litigate": ("Mediate or Litigate? How to Choose",
   ["mediation-or-litigation-what-is-the-best","mediate-collaborate-or-litigate","litigation-or-mediation-choose-very-wisely",
    "the-different-ways-to-resolve-family-law-disputes","why-going-to-court-for-your-family-law-dispute-is-a-mistake",
    "abc-expose-the-hidden-cost-of-family-court-battles","five-benefits-of-using-mediation-to-resolve-divorce-issues",
    "nothing-alternate-about-alternate-dispute-resolution-adr","mediation-vs-collaborative-law",
    "im-contemplating-separation-do-i-see-a-lawyer-or-a-mediation-practice-first","the-role-of-the-lawyer-in-mediation",
    "the-difference-between-a-divorce-lawyer-and-a-mediator","points-to-consider-family-mediation-lawyers-in-australia",
    "how-to-resolve-your-family-law-dispute-online"]),
 "shuttle-mediation-guide": ("Shuttle Mediation Explained",
   ["shuttle-mediation","the-pros-and-cons-of-shuttle-mediation"]),
 "conciliation-vs-mediation": ("Conciliation vs Mediation",
   ["conciliation-in-family-law","difference-between-mediation-conciliation","difference-mediator-and-conciliator"]),
 "high-conflict-mediation": ("High-Conflict Family Law Mediation",
   ["high-conflict-family-law-mediation","when-is-mediation-not-a-good-idea"]),
 "domestic-violence-and-family-law": ("Domestic Violence & Family Law",
   ["domestic-violence","what-is-an-avo","what-is-a-restraining-order","what-is-a-dvo-everything-you-need-to-know",
    "what-is-a-dvo-how-to-apply-for-a-domestic-violence-order","intervention-orders","court-ordered-drug-and-alcohol-testing",
    "what-hannahs-law-means","parental-alienation-australia-dont-let-your-ex-destroy-your-childs-love-for-you"]),
 "arbitration-in-family-law": ("Arbitration in Family Law",
   ["arbitration-in-family-law"]),
 "workplace-mediation-guide": ("Workplace Mediation in Australia",
   ["what-is-workplace-mediation-2023-important-update","the-role-of-fair-work-australia-and-workplace-mediation","mediate-workplace-conflict-in-australia"]),
 "pets-and-family-law": ("Pets & Family Law: Who Gets the Pet?",
   ["pets-and-family-law-who-gets-the-pets-after-separation"]),
 "business-in-divorce": ("What Happens to a Business in Divorce?",
   ["what-happens-to-business-in-divorce","can-you-sue-a-family-trust-in-australia","family-loan-agreement-matters"]),
 "same-sex-family-law": ("Same-Sex Separation & Divorce",
   ["same-sex-divorce-in-australia","australia-lgbt-marriage-mediation"]),
 "family-court-process": ("The Family Court Process",
   ["family-court-process-2024-update","what-are-procedural-orders-in-family-court","final-hearing-in-family-law-disputes",
    "what-is-a-litigation-guardian-in-australia","what-is-the-magellan-list","family-law-regulations-explained",
    "commonly-asked-family-law-questions","are-mediation-agreements-legally-binding"]),
 "divorce-without-a-lawyer": ("Divorce Without a Lawyer",
   ["divorce-without-lawyers","divorce-without-a-lawyer"]),
 "stepparent-rights": ("Step-Parent Rights", ["stepparent-rights-and-family-law-in-australia"]),
 "surrogacy-laws": ("Surrogacy Laws in Australia", ["surrogacy-laws-in-australia-2024"]),
 "can-you-record-your-ex": ("Can You Record Your Ex?", ["can-you-record-your-ex-without-permission"]),
 "best-divorce-lawyers-sydney": ("Best Divorce Lawyers in Sydney", ["best-divorce-lawyers-in-sydney","separation-lawyer-sydney"]),
 "changes-to-family-law-act-2025": ("Changes to the Family Law Act 2025", ["changes-to-the-family-law-act-2025-you-must-know"]),
 # already-built cornerstones (keep)
 "mediation-with-a-narcissist": ("Mediation With a Narcissist", []),
 "how-long-does-mediation-take": ("How Long Does Mediation Take?", []),
 "preparing-for-mediation": ("Preparing for Mediation", ["how-to-get-ready-for-mediation"]),
 "estate-dispute-mediation": ("Estate Dispute Mediation", []),
}

# Tally
canonical = list(CLUSTERS.keys())
absorbed = [s for _,(_,lst) in CLUSTERS.items() for s in lst]
print(f"\\nCONSOLIDATION PLAN:")
print(f"  {len(ALL)} original posts")
print(f"  -> {len(canonical)} canonical cornerstone posts")
print(f"  -> {len(absorbed)} old posts redirect (301) into a canonical")
covered = set(canonical) | set(absorbed)
uncovered = [s for s in ALL if s not in covered]
print(f"  Uncovered (need a decision): {len(uncovered)}")
for u in uncovered: print("     -",u)

# Straggler -> existing resource page
CLUSTERS["__redirect_to_resource__"] = ("(redirects to resource pages)", ["separated-under-one-roof"])
EXTRA_REDIRECTS = {"separated-under-one-roof":"separation-under-one-roof"}

# Already built (cornerstones done this far)
DONE = ["cost-of-divorce-in-australia","mediation-with-a-narcissist",
        "what-am-i-entitled-to-in-a-separation-in-australia","how-long-does-mediation-take"]

def export_manifest():
    import csv, os
    rows=[]
    for canon,(title,absorbed) in CLUSTERS.items():
        if canon.startswith("__"): 
            for old in absorbed:
                rows.append((old, "redirect-301", EXTRA_REDIRECTS.get(old,""), "resource page"))
            continue
        status = "DONE" if canon in DONE else "TO BUILD"
        rows.append((canon, "CANONICAL ("+status+")", canon, title))
        for old in absorbed:
            rows.append((old, "redirect-301", canon, "-> "+title))
    out="/mnt/user-data/outputs/blog-content-manifest.csv"
    with open(out,"w",newline="") as f:
        w=csv.writer(f); w.writerow(["old_slug","action","target_slug","note"])
        for r in rows: w.writerow(r)
    print(f"Manifest exported: {len(rows)} rows -> blog-content-manifest.csv")
    tobuild=[c for c,(t,a) in CLUSTERS.items() if not c.startswith('__') and c not in DONE]
    print(f"Cornerstones still TO BUILD: {len(tobuild)}")

export_manifest()
