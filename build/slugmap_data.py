# Old site URL inventory captured from sitemaps (page-sitemap + post-sitemap1).
# post-sitemap2 still to be fetched in a later phase.
# Maps each old slug -> action: ("redirect","new-slug") or ("rebuild","new-slug") or ("keep","same")

# PAGES already rebuilt or with a clear target:
PAGE_MAP = {
 "": ("keep",""),
 "about-mediations-australia": ("keep","about-mediations-australia"),
 "contact-us": ("keep","contact-us"),
 "book-a-consultation": ("keep","book-a-consultation"),
 "family-law-mediation": ("keep","family-law-mediation"),
 "property-settlement-mediation": ("keep","property-settlement-mediation"),
 "parenting-plan-mediation": ("keep","parenting-plan-mediation"),
 "financial-agreements-mediation": ("keep","financial-agreements-mediation"),
 "workplace-mediation": ("keep","workplace-mediation"),
 "estate-dispute-mediation": ("keep","estate-dispute-mediation"),
 "online-divorce": ("keep","online-divorce"),
 "consent-orders": ("keep","consent-orders"),
 "divorce-counselling": ("keep","divorce-counselling"),
 "collaborative-family-lawyers": ("keep","collaborative-family-lawyers"),
 "getting-ready-for-separation": ("keep","getting-ready-for-separation"),
 "parenting-plan-template": ("keep","parenting-plan-template"),
 "separation-under-one-roof-assessment": ("redirect","separation-under-one-roof"),
 "family-law-cost-calculator": ("redirect","family-law-cost-estimator"),
 # old service slugs -> new canonical service slugs
 "section-601-certificate-mediation": ("redirect","section-60i-certificates"),
 "spousal-support-dispute-mediation": ("redirect","spousal-support-mediation"),
 "spousal-maintenance-australia": ("redirect","spousal-support-mediation"),
 "child-support-dispute-mediation": ("redirect","child-support-mediation"),
 "de-facto-relationship-dispute-mediation": ("redirect","de-facto-mediation"),
 "grandparent-mediation": ("redirect","grandparents-mediation"),
 "family-law-dispute-mediation": ("redirect","family-law-mediation"),
 "family-law-arbitrators": ("rebuild","family-law-arbitration"),
 "accredited-family-law-mediators": ("rebuild","our-mediators"),
 "family-law-practitioners": ("rebuild","our-mediators"),
 "our-mediators": ("rebuild","our-mediators"),
 # location: mediation
 "family-law-melbourne-mediation": ("redirect","melbourne-mediation"),
 # tools / misc pages to rebuild later
 "guides": ("rebuild","guides"),
 "mediation-information": ("rebuild","mediation-information"),
 "domestic-violence-support-services-australia": ("rebuild","domestic-violence-support-services-australia"),
 "memberships": ("rebuild","memberships"),
 "our-fee-structure": ("keep","our-fee-structure"),
 "preparing-for-mediation": ("keep","preparing-for-mediation"),
 "how-mediation-works": ("keep","how-mediation-works"),
 # state parenting templates
 "parenting-plan-template-nsw": ("rebuild","parenting-plan-template-nsw"),
 "parenting-plan-template-vic": ("rebuild","parenting-plan-template-vic"),
 "parenting-plan-template-qld": ("rebuild","parenting-plan-template-qld"),
 "parenting-plan-template-wa": ("rebuild","parenting-plan-template-wa"),
 # forms / low-value WP pages -> redirect to booking or contact
 "make-an-appointment": ("redirect","book-a-consultation"),
 "lawyer-booking": ("redirect","book-a-consultation"),
 "online-mediation-enquiry": ("redirect","book-a-consultation"),
 "mediation-podcast": ("rebuild","mediation-podcast"),
 "law-firms": ("rebuild","for-lawyers"),
 "team-single": ("redirect","our-mediators"),
 "legal-info": ("rebuild","legal-info"),
 "qld": ("redirect","brisbane-mediation"),
 "mediation": ("redirect","how-mediation-works"),
 "resolve-your-property-settlement-with-mediation-in-australia": ("redirect","property-settlement-mediation"),
}
