#!/usr/bin/env python3
"""Curated library of authoritative external sources for blog citations.
STANDARD: every blog post must include at least 2-3 links to authoritative
(.gov.au / .edu / peak-body) sources. Pull from this library by topic."""

AUTHORITY = {
 # Legislation & courts
 "family_law_act": ("Family Law Act 1975", "https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/"),
 "fcfcoa": ("Federal Circuit and Family Court of Australia", "https://www.fcfcoa.gov.au/"),
 "fcfcoa_fees": ("FCFCOA fee schedule", "https://www.fcfcoa.gov.au/fl/fees/fl-fees"),
 "fcfcoa_fdr": ("FCFCOA family dispute resolution", "https://www.fcfcoa.gov.au/fl/fdr"),
 "fcfcoa_disclosure": ("FCFCOA duty of disclosure", "https://www.fcfcoa.gov.au/fl/duty-disclosure"),
 "fcfcoa_consent_orders": ("FCFCOA consent orders", "https://www.fcfcoa.gov.au/fl/consent-orders"),
 "fcfcoa_apply_consent": ("FCFCOA: Apply for consent orders", "https://www.fcfcoa.gov.au/hdi/apply-consent-orders"),
 "fcfcoa_safety_risk": ("FCFCOA: Safety and risk in children's matters", "https://www.fcfcoa.gov.au/fl/children/safety-risk"),
 "fcfcoa_serve_divorce": ("FCFCOA: Serving divorce documents", "https://www.fcfcoa.gov.au/fl/divorce/serve-divorce"),
 "fcfcoa_served": ("FCFCOA: I have been served with a divorce application", "https://www.fcfcoa.gov.au/fl/divorce/served"),
 "fcfcoa_trouble_serving": ("FCFCOA: Trouble serving divorce documents", "https://www.fcfcoa.gov.au/fl/pubs/trouble-serving-divorce"),
 "fcfcoa_proof_sig": ("FCFCOA: Affidavit proving signature (divorce)", "https://www.fcfcoa.gov.au/fl/forms/affidavit-proof-sig-divorce"),
 "fcfcoa_one_roof": ("FCFCOA: Separated under one roof", "https://www.fcfcoa.gov.au/fl/pubs/separated-under-one-roof"),
 "fcwa_parenting_examples": ("Family Court of WA: Examples of parenting orders", "https://www.familycourt.wa.gov.au/E/examples_of_parenting_orders.aspx"),
 "cdt_review": ("Bortolotti et al., CDT as a marker of alcohol abuse (J Chromatogr B, 2006)", "https://pubmed.ncbi.nlm.nih.gov/16725384/"),
 "frol_fdr": ("Family Relationships Online: Family mediation and FDR", "https://www.familyrelationships.gov.au/separation/family-mediation-dispute-res"),
 "comcourts_portal": ("Commonwealth Courts Portal", "https://www.comcourts.gov.au/"),
 "family_court_wa": ("Family Court of Western Australia", "https://www.familycourt.wa.gov.au/"),
 # Government services
 "services_australia_cs": ("Services Australia \u2014 Child Support", "https://www.servicesaustralia.gov.au/child-support"),
 "ag_fdr": ("Attorney-General's Dept \u2014 Family Dispute Resolution", "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
 "frc": ("Family Relationships Online", "https://www.familyrelationships.gov.au/"),
 "amdras": ("Mediator Standards Board (AMDRAS)", "https://msb.org.au/"),
 "legal_aid": ("National Legal Aid", "https://www.legalaid.gov.au/"),
 "ag_frc": ("Attorney-General's Dept — Family Relationship Centres", "https://www.ag.gov.au/families-and-marriage/families/family-relationship-centres"),
 "fair_work": ("Fair Work Commission", "https://www.fwc.gov.au/"),
 "fwo_unfair_dismissal": ("Fair Work Ombudsman: Unfair dismissal", "https://www.fairwork.gov.au/ending-employment/unfair-dismissal"),
 "veohrc": ("Victorian Equal Opportunity &amp; Human Rights Commission", "https://www.humanrights.vic.gov.au/"),
 "vcat": ("Victorian Civil and Administrative Tribunal", "https://www.vcat.vic.gov.au/"),
 "vic_equal_opp_act": ("Equal Opportunity Act 2010 (Vic)", "https://www.legislation.vic.gov.au/in-force/acts/equal-opportunity-act-2010"),
 "safework_mental": ("Safe Work Australia — mental health", "https://www.safeworkaustralia.gov.au/safety-topic/hazards/mental-health"),
 # Statistics & research
 "abs_divorce": ("ABS Marriages and Divorces, Australia", "https://www.abs.gov.au/statistics/people/people-and-communities/marriages-and-divorces-australia/latest-release"),
 "aifs": ("Australian Institute of Family Studies", "https://aifs.gov.au/"),
 "ato": ("Australian Taxation Office", "https://www.ato.gov.au/"),
 "moneysmart": ("MoneySmart (ASIC)", "https://moneysmart.gov.au/"),
 # Support / safety
 # International travel / abduction
 "afp_watchlist": ("AFP: Family Law Watchlist", "https://www.afp.gov.au/our-services/national-policing-services/family-law-watchlist"),
 "passports_consent": ("Australian Passport Office: Child passports and consent", "https://www.passports.gov.au/consent"),
 "ag_child_abduction": ("Attorney-General's Dept: International parental child abduction", "https://www.ag.gov.au/families-and-marriage/international-family-law-and-children/international-parental-child-abduction"),
 # Child support — school costs
 "sa_change_assessment": ("Services Australia: Changing your assessment in special circumstances", "https://www.servicesaustralia.gov.au/changing-your-child-support-assessment-special-circumstances"),
 "sa_non_agency": ("Services Australia: Non-agency payments", "https://www.servicesaustralia.gov.au/individuals/services/child-support/binding-child-support-agreement/how-pay-and-collect-child-support/choose-how-pay-child-support/non-agency-payments"),
 "respect_1800": ("1800RESPECT", "https://www.1800respect.org.au/"),
 "dsm_pd": ("APA \u2014 personality disorders (DSM-5)", "https://www.psychiatry.org/patients-families/personality-disorders/what-are-personality-disorders"),
}

def cite(key):
    """Return an <a> tag for an authority source."""
    label, url = AUTHORITY[key]
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'

# Recommended sources by post topic (for writers building the backlog)
TOPIC_SOURCES = {
 "costs":        ["fcfcoa_fees","abs_divorce","family_law_act"],
 "property":     ["family_law_act","fcfcoa_disclosure","fcfcoa_consent_orders"],
 "parenting":    ["family_law_act","fcfcoa_fdr","frc"],
 "child_support":["services_australia_cs","family_law_act"],
 "divorce":      ["fcfcoa_fees","family_law_act","abs_divorce"],
 "consent_orders":["fcfcoa_consent_orders","family_law_act"],
 "workplace":    ["fair_work"],
 "workplace_vic":["veohrc","vcat","vic_equal_opp_act","safework_mental","fair_work"],
 "de_facto":     ["family_law_act","aifs"],
 "high_conflict":["dsm_pd","respect_1800","fcfcoa_fdr"],
 "process":      ["fcfcoa","ag_fdr","amdras"],
 "affordability": ["ag_fdr","frc","legal_aid","ag_frc"],
 "wa":           ["family_court_wa","family_law_act"],
}

if __name__ == "__main__":
    print(f"Authority library: {len(AUTHORITY)} curated sources across {len(TOPIC_SOURCES)} topics")
    print("STANDARD: >=2 authority links per post.")
