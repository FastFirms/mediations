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
 "comcourts_portal": ("Commonwealth Courts Portal", "https://www.comcourts.gov.au/"),
 "family_court_wa": ("Family Court of Western Australia", "https://www.familycourt.wa.gov.au/"),
 # Government services
 "services_australia_cs": ("Services Australia \u2014 Child Support", "https://www.servicesaustralia.gov.au/child-support"),
 "ag_fdr": ("Attorney-General's Dept \u2014 Family Dispute Resolution", "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
 "frc": ("Family Relationships Online", "https://www.familyrelationships.gov.au/"),
 "amdras": ("Mediator Standards Board (AMDRAS)", "https://msb.org.au/"),
 "fair_work": ("Fair Work Commission", "https://www.fwc.gov.au/"),
 # Statistics & research
 "abs_divorce": ("ABS Marriages and Divorces, Australia", "https://www.abs.gov.au/statistics/people/people-and-communities/marriages-and-divorces-australia/latest-release"),
 "aifs": ("Australian Institute of Family Studies", "https://aifs.gov.au/"),
 # Support / safety
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
 "de_facto":     ["family_law_act","aifs"],
 "high_conflict":["dsm_pd","respect_1800","fcfcoa_fdr"],
 "process":      ["fcfcoa","ag_fdr","amdras"],
 "wa":           ["family_court_wa","family_law_act"],
}

if __name__ == "__main__":
    print(f"Authority library: {len(AUTHORITY)} curated sources across {len(TOPIC_SOURCES)} topics")
    print("STANDARD: >=2 authority links per post.")
