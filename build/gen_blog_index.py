#!/usr/bin/env python3
"""Blog/guides index page — topic-based UX redesign."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, cta_band,
                       org_schema, breadcrumb_schema, BOOK_URL, PHONE_HREF, PHONE, DOMAIN)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── CORNERSTONE GUIDES ────────────────────────────────────────────────────────
# Organised by topic section for the redesigned page.
# Each entry: (slug, title, blurb)

SEPARATION = [
    ("separation-guide",               "Separation in Australia: Complete Guide",            "First steps, the date of separation, who stays in the house, and protecting yourself."),
    ("de-facto-relationships-guide",   "De Facto Relationships & Separation",                "What counts as de facto, how assets are split, the two-year limit."),
    ("how-to-get-a-divorce-in-australia-a-step-by-step-guide", "How to Get a Divorce in Australia", "Eligibility, the 12-month rule, applying online, cost, and serving papers."),
    ("how-long-does-a-divorce-take",   "How Long Does a Divorce Take?",                      "The 12-month rule, processing times, and avoiding delays."),
    ("divorce-without-a-lawyer",       "Divorce Without a Lawyer",                           "How to DIY the application and the cost-effective middle path."),
    ("mediation-before-divorce",       "Mediation Before Divorce",                           "Why resolving parenting and property before filing saves time and money."),
    ("my-ex-wont-sign-divorce-papers", "My Ex Won't Sign the Divorce Papers",                "Your ex cannot block a divorce. The sole-applicant process explained."),
    ("same-sex-family-law",            "Same-Sex Separation & Divorce",                      "Equal rights for LGBTQ+ couples in divorce, property, parenting and de facto matters."),
    ("application-for-divorce", "Application for Divorce Australia: 15 Minute Success Guide…", "What are the complexities of divorce? With our comprehensive guide on completing your application for divorce in Australia, you can feel confident..."),
    ("applying-for-a-divorce-in-australia", "Applying for a Divorce in Australia: What You Need to Know", "Divorce in Australia involves various key considerations, including cost, duration and process. We will delve deeper into these aspects"),
    ("best-divorce-lawyers-in-sydney", "The Best Divorce Lawyers in Sydney", "Find the best divorce lawyers in Sydney. Expert guidance on Family Law Act. Choose wisely for a fair outcome."),
    ("can-my-ex-wife-claim-money-after-divorce-in-australia", "Can My Ex Wife Claim Money after Divorce in Australia", "Can My Ex Wife Claim Money after Divorce in Australia is a commonly asked question. The answer is relatively simple, in this article and podcast, w..."),
    ("can-you-record-your-ex-without-permission", "Can You Record Your Ex Without Permission", "Unless you're protecting yourself or your property, it's illegal to record someone without their agreement under state law."),
    ("de-facto-relationships", "De Facto Relationships", "De facto relationships can be complex. In this article, podcast and assessment, we discuss everything you need to know about de facto relationships"),
    ("de-facto-relationships-and-prenups-what-you-have-to-know", "De Facto Relationships and Prenups: What You Have to Know", "Are you in a De Facto relationship? It might be wise to consider a prenup. A prenup is like an insurance policy. In this article we tell you"),
    ("divorce-application-process", "Divorce Application Process: A Step-by-step Guide To Help", "Divorce application process: Discover the essential steps and tips for successfully completing the divorce application process in Australia."),
    ("divorce-certificate-in-australia", "Divorce Certificate in Australia: What You Need", "Divorce certificate: Learn its significance, how to obtain one, and streamline your post-divorce processes in Australia with confidence."),
    ("divorce-law-near-me", "Divorce Law Near Me", "Divorce Law Near me, iIf you're considering divorce or separation in Australia, it's important to understand the relevant laws and processes."),
    ("divorce-without-lawyers", "How to Divorce Without Lawyers in Australia", "Divorce without lawyers in Australia is possible, and mediation and arbitration can be effective ways to resolve family law disputes"),
    ("does-a-husband-have-to-support-his-wife", "Does a Husband Have to Support His Wife during Separation?", "Does a husband have to support his wife during separation in Australia? Explore legal obligations and financial considerations here."),
    ("five-benefits-of-using-mediation-to-resolve-divorce-issues", "Five Huge Benefits of Using Mediation to Resolve Divorce…", "Here are five benefits of using mediation to resolve issues around divorce, which our mediation office can help you with."),
    ("five-things-to-do-before-uttering-i-want-a-divorce", "Five Things to Do Before Uttering, &#x27;I Want a Divorce&#x27;", "Five Things to Do Before Uttering, &#x27;I Want a Divorce&#x27;"),
    ("how-long-does-it-take-to-get-a-divorce", "How Long Do Take Get a Divorce?", "In Australia, how long does it take to get a divorce granted? At Mediations Australia, we can assist you with your divorce concerns, including Onli..."),
    ("how-to-apply-file-for-get-a-divorce-in-western-australia-wa", "How to Apply, File for & Get a Divorce in Western…", "How to Apply, File for & Get a Divorce in Western…"),
    ("how-to-convince-your-ex-partner-to-do-mediation", "How to Convince Your Ex-Partner to Do Mediation", "The best way to have your former partner agree to mediation is through the provision of information. A great way to have them informed is"),
    ("how-to-get-a-divorce-in-new-south-wales", "How to Get a Divorce in New South Wales", "In this article, we'll take you through the process of how to get a divorce in New South Wales, step-by-step."),
    ("how-to-get-divorce-papers-the-2022-guide", "How to Get Divorce Papers - Guide 2022", "Are you considering separation or divorce and want to know how to get divorce papers? In this 2022 Guide, we advise you of everything."),
    ("how-to-protect-your-online-privacy-following-separation", "How to Protect Your Online Privacy Following Separation?", "There are several steps that you can take to protect your online privacy following a separation in Australia: Call us today!"),
    ("how-to-separate-from-your-spouse-or-partner-in-australia", "How to Separate from Your Spouse or Partner in Australia", "How to Separate from Your Spouse or Partner in Australia"),
    ("im-contemplating-separation-do-i-see-a-lawyer-or-a-mediation-practice-first", "I’m Contemplating Separation, Do I See Lawyer or Mediation…", "I’m Contemplating Separation, Do I See a Lawyer or a Mediation Practice First? Call Mediations Australia today."),
    ("in-a-divorce-who-gets-what", "In a Divorce Who Gets What?", "Who gets what following divorce can be a complex question. In this article, we discuss all the things you need to know."),
    ("joint-divorce-application", "Joint Divorce Application: A Guide for Couples", "Joint Divorce Application: Simplify the process by collaborating with your spouse. Explore benefits, eligibility, and step-by-step guidance."),
    ("joint-tenancy-and-divorce", "Impact of Joint Tenancy and Divorce in Australia", "Explore the legal intricacies of joint tenancy and divorce. Learn the definition, benefits, risks, and post-divorce scenarios to protect your inter..."),
    ("mediation-for-separation", "Mediation for Separation", "Mediation for separation has become a popular option for couples seeking a cost-effective approach to resolving disputes."),
    ("pre-separation-checklist", "Pre-Separation Checklist", "Separation, in the worst-case scenario, involves a person leaving the marital or de facto home in haste and not returning. In this article"),
    ("same-sex-divorce-in-australia", "Same Sex Divorce Australia: Your Legal Guide for LGBTQ+…", "Your love story deserves a dignified ending. Same sex divorce in Australia shouldn't cost you your sanity or your savings. Join couples saving $150..."),
    ("separation-lawyer-sydney", "Separation Lawyer Sydney", "Separation lawyer in Sydney: Expert legal guidance for navigating separation, property division, and custody matters."),
    ("separation-or-divorce-which-is-better", "Separation or Divorce? Which is Better?", "Separation or Divorce? Which is Better?"),
    ("the-marriage-separation-process-in-nsw", "The Marriage Separation Process in NSW", "Navigate marriage separation in NSW with legal insights. Understand separation, legal requirements, child custody, and the role of mediation"),
    ("trial-separation", "Trial Separation: Everything You Need to Know", "Don't give up just yet if saving your marriage seems impossible. Instead, try out a trial separation. You might learn something"),
    ("understanding-divorce-laws-in-nsw", "Understanding Divorce Laws in NSW", "One of the most important things about divorce laws in NSW is that there is no need to prove fault or wrongdoing. Read our blog.."),
    ("what-am-i-entitled-to-in-a-divorce-or-separation-in-australia", "What am I Entitled to in a Divorce or Separation in…", "What am I entitled to in a divorce or separation is the most commonly asked question by separating couples. In this article we cover in all topic...."),
    ("what-am-i-entitled-to-in-a-separation", "What am I entitled to in a Separation?", "One of the most common questions asked by separating couples, what am I entitled to in a separation. In this article we answer the all queries rega..."),
    ("what-is-divorce-law-in-australia", "What is Divorce Law in Australia?", "Divorce can be a challenging and emotional process, and it's essential to understand the legal framework that governs"),
    ("what-is-the-average-split-in-a-divorce-settlement-australia", "What is The Average Split in a Divorce Settlement…", "Worried about what is the average split in a divorce settlement in Australia? We are telling you everything on how assets are really divided, from…"),
    ("whats-the-difference-between-a-de-facto-relationship-and-marriage", "What’s the Difference Between a De Facto Relationship and…", "A de facto relationship is defined under section 44A of the Family Law Act 1975 as a relationship between two people, including same sex"),
    ("who-gets-to-stay-in-the-house-during-separation", "Who gets to stay in the house during separation in…", "Who gets to stay in the house during separation in Australia? Navigate legal complexities and find fair housing solutions here."),
]

PARENTING = [
    ("child-custody-mediation",        "Child Custody Mediation",                            "What the law says about custody, 50/50 care, and how parents agree without court."),
    ("parenting-plans-guide",          "Parenting Plans in Australia",                       "What to include, whether it's binding, and how to agree one through mediation."),
    ("fathers-rights",                 "Fathers' Rights After Separation",                   "The truth about 50/50 care, parental responsibility, and securing meaningful time."),
    ("mothers-rights",                 "Mothers' Rights in Family Law",                      "Parental responsibility, the best-interests test, and the myth of automatic preference."),
    ("co-parenting-mediation",         "Co-Parenting Mediation",                             "Resolving ongoing disputes over schedules, decisions and communication."),
    ("child-support-guide",            "Child Support in Australia",                         "The formula, how care affects payments, when it stops, and resolving disputes."),
    ("parental-alienation-australia",  "Parental Alienation in Australia",                   "What it is, how the law treats it, and rebuilding the relationship without court."),
    ("grandparents-rights",            "Grandparents' Rights in Australia",                  "How grandparents seek time with grandchildren — and why mediation comes first."),
    ("best-apps-for-separated-parents","Best Apps for Separated Parents",                    "Co-parenting apps that reduce conflict and create a court-admissible record."),
    ("stepparent-rights",              "Step-Parent Rights in Australia",                    "Parental responsibility, contact after separation, and staying in a child's life."),
    ("12-best-strategies-for-effective-parenting-plans-in-australia", "12 Best Strategies for Effective Parenting Plans in…", "Creating a solid parenting plans is important for families going through separation or divorce. At Mediations Australia,"),
    ("5-reasons-why-you-should-consider-mediation-for-child-custody-disputes", "Five Reasons to Consider Mediation for Child Custody…", "Mediation for child custody offers a less adversarial, cost-effective, and child-centric approach compared to lengthy court battles."),
    ("binding-child-support-agreements-in-australia-important-2026-update", "Binding Child Support Agreements Australia", "Learn how binding child support agreements work in Australia. Understand legal requirements, payment options, and how mediation helps create fair a..."),
    ("child-support-payments-and-taxes", "Child Support Payments and Taxes in Australia: What…", "Child Support Payments and Taxes: Understand the tax implications of child support payments in Australia and avoid common pitfalls."),
    ("create-parenting-plan-that-works", "Create a Parenting Plan That Actually Works", "Find out how to create a parenting plan that works. In this comprehensive article, we discuss everything you need to know"),
    ("grandparents-custody-in-australia", "Grandparents Custody and Parenting Orders in Australia", "Grandparents Custody: Explore legal rights under Australia's Family Law Act 1975, empowering grandparents to seek custody or visitation."),
    ("grandparents-rights-how-to-see-your-grandchildren-2022-update", "What Are Grandparents rights & Grandchildren&#x27;s Rights?", "Grandparents Rights: Discover the crucial role they play and understand their legal rights in this comprehensive guide."),
    ("how-does-mediation-help-co-parenting", "How Does Mediation Help Co-Parenting", "To know more about how you can better the prospects of co-parenting effectively post-separation via mediation, contact us today."),
    ("how-often-do-fathers-get-50-50-custody-in-australia", "How Often do Fathers get 50/50 Custody in Australia", "The question of How Often do Fathers get 50/50 Custody in Australia hasn't got a clear answer. However, in this comprehensive article..."),
    ("parental-alienation-australia-dont-let-your-ex-destroy-your-childs-love-for-you", "Parental Alienation Australia: Don&#x27;t Let Your Ex Destroy…", "Parental alienation Australia is rising. Don't let your ex destroy your relationship with your child. Our mediators help rebuild parent-child bonds..."),
    ("parenting-plan-vs-parenting-order", "What is the difference between a Parenting Plan and…", "A Parenting Plan offers flexibility, while a Parenting Order provides a legally binding framework when navigating child custody."),
    ("parenting-plans-example", "Parenting Plans Example", "Looking for Parenting Plans Example. In this article we give you a full parenting plan example including useful information to guide you..."),
    ("pets-and-family-law-who-gets-the-pets-after-separation", "Pet Custody After a Divorce or Separation", "Who gets the pets after separation is a very common question. In this article, we discuss everything you need to know about."),
    ("stepparent-rights-and-family-law-in-australia", "Stepparent Rights and Family Law in Australia", "Stepparent Rights: Consult our family lawyers and mediators to understand potential challenges regarding legal rights and obligations."),
    ("supporting-your-child-through-parents-separation-a-comprehensive-guide-for-australian-families", "Supporting Your Child Through Parents&#x27; Separation: A…", "Supporting Your Child Through Parents&#x27; Separation: A…"),
    ("surrogacy-laws-in-australia-2024", "Understanding Surrogacy Laws in Australia: What You Need…", "Surrogacy laws in Australia are extremely complex and not consistent from state to state. In this definitive Surrogacy Laws guide you will learn ho..."),
    ("travel-overseas-after-a-separation", "Child travel overseas after a separation: is it allowed?", "Planning to travel overseas after a separation? Navigate complexities with legal insights and practical tips for post-separation child travel."),
    ("what-are-the-mothers-rights-in-family-law", "What Are The Mother&#x27;s Rights in Child Custody", "Historically, when considering a mother's or father's rights when it comes to custody of the children, mothers were granted custody."),
    ("what-is-child-custody-mediation", "What is Child Custody Mediation", "What is Child Custody Mediation. In this 2022 update, w give you all the information you need to find out what is..."),
    ("what-is-the-role-of-an-independent-childrens-lawyer", "What is the Role of an Independent Children&#x27;s Lawyer?", "In complex parenting cases, a judge may order the appointment of an independent children's lawyer (ICL). In this article"),
    ("what-you-need-to-know-about-parenting-plans", "What You Need to Know About Parenting Plans", "Mediations Australia can assist in all parenting dispute matters."),
    ("when-child-support-stops-guide", "When Child Support Stops: A Guide for Australian Parents", "When Child Support Stops: Empower Sydney parents with options and resources to recover unpaid child support payments effectively."),
    ("when-should-i-think-about-parenting-mediation-or-custody-mediation", "When should I think about Parenting Mediation or Custody…", "When parents cannot agree on issues that affect a child's near and long term future, parental mediation is advised. Read more here."),
]

PROPERTY = [
    ("property-settlement-after-separation", "Property Settlement After Separation",          "The four-step process, asset pool, time limits and how to settle without court."),
    ("what-am-i-entitled-to-in-a-separation-in-australia", "What Am I Entitled To?",         "How property, super and support are divided — and how to reach a fair split."),
    ("binding-financial-agreements-guide", "Binding Financial Agreements",                   "Prenups and postnups explained — what makes them valid and BFA vs consent orders."),
    ("consent-orders-explained",       "Consent Orders Explained",                           "How to make your agreement legally binding without going to court."),
    ("consent-orders-2026-update",     "Consent Orders 2026: What Changed",                  "The 2025 reforms, updated process, and what you need to know this year."),
    ("superannuation-and-divorce",     "Superannuation and Divorce",                         "How super splitting works, valuation, and why it matters — especially for carers."),
    ("property-settlement-mediation-guide", "Property Settlement Mediation Guide",           "How to prepare, what to bring, what to expect on the day."),
    ("what-is-in-the-property-pool",   "What's in the Property Pool?",                      "Assets, super, businesses, debts and inheritances — what counts."),
    ("spousal-maintenance-guide",      "Spousal Maintenance in Australia",                   "Who pays, how much, how long it lasts, and how it differs from child support."),
    ("business-in-divorce",            "Business in Divorce",                                "How businesses and trusts are valued and divided — and how to protect yours."),
    ("who-pays-bills-during-separation","Who Pays Bills During Separation?",                 "Mortgage, utilities, joint cards — and how to set up an interim arrangement."),
    ("pets-and-family-law",            "Pets and Family Law",                                "Who gets the pet after separation and the 2025 law changes."),
    ("delaying-property-settlement",   "Can My Ex Delay Settlement?",                        "Stalling tactics, time limits, and how mediation forces progress."),
    ("12-essential-things-to-know-about-binding-financial-agreements-in-australia", "12 Essential Things to Know About Binding Financial…", "12 Essential Things to Know About Binding Financial…"),
    ("60-40-split-divorce-australia", "What is a 60/40 Split Divorce Australia", "Discover how Mediations Australia can guide you through a 60/40 split divorce Australia. Get expert help in navigating asset division, protecting y..."),
    ("are-gifts-included-in-property-settlements-in-australia", "Are Gifts Included in Property Settlements in Australia?", "Are Gifts Included in Property Settlements in Australia? This is a commonly asked question. In this article, we provide all you need to know about..."),
    ("becoming-independent-sooner-how-mediation-can-help-you-agree-on-spousal-support", "How Mediation Can Help You Agree on Spousal Support", "If you want to know more about how mediation can help you agree on spousal support, simply ask one of our Mediations Australia team members."),
    ("binding-financial-agreement", "Binding Financial Agreement: 7 Things Lawyers Don&#x27;t Tell You", "Understand the ins and outs of a binding financial agreement in Australia. Learn how to protect your assets, understand the legal requirements, and..."),
    ("binding-financial-agreement-v-consent-orders", "Binding Financial Agreement v Consent Orders", "Binding Financial Agreement v Consent Orders which is best for you? In this article, we explain all you need to know."),
    ("binding-financial-agreement-what-you-need-to-know", "Binding Financial Agreement: What You Need to Know", "A Binding Financial Agreement is a contract between two people who are in a relationship. It's like a prenuptial agreement. Learn what you need to..."),
    ("can-you-sue-a-family-trust-in-australia", "Can You Sue a Family Trust in Australia? Exploring…", "Can you sue a family trust in Australia? While you can't sue a trust directly, we help resolve trustee disputes through mediation - saving tens of…"),
    ("consent-orders-2025-update", "Consent Orders: Important 2025 Update", "Important updates on Consent orders. They are a legally binding agreement that is made between parties involved in a legal dispute and is approved..."),
    ("consent-orders-example", "Consent Orders Example", "Are you looking for Consent Orders Example, in this article we provide a full example of consent orders, including everything you need..."),
    ("cryptocurrency-and-digital-assets-in-property-settlements", "Cryptocurrency and Digital Assets in Property Settlements", "Cryptocurrency and Digital Assets in Property Settlements is becoming a huge issue. In this article, we thoroughly discuss all the ramifications"),
    ("difference-mediator-and-conciliator", "Difference Between Mediator and Conciliator", "Alternative dispute resolution, \"mediator\" and \"conciliator\" are used interchangeably, but there are differences between these two roles."),
    ("divorce-property-settlement-examples-in-australia", "Divorce Property Settlement Examples in Australia", "Our skilled Family law team works arduously to make sure you get the best result possible in the event of a divorce or separation. comes to divorce..."),
    ("divorce-property-settlement-your-best-options-in-2022", "Divorce Property Settlement: Your Best Options in 2022", "Are you considering divorce and property settlement? In this article, we discuss the best options to consider in 2022."),
    ("ex-delaying-property-settlement", "Ex Delaying Property Settlement. What to Do Next", "Expert guidance on handling property settlement delays in Australia. Learn your legal rights, practical solutions, and protective measures with you..."),
    ("family-law-mediation-for-property-settlements", "Family Law Mediation for Property Settlements", "In this guide, we explore benefits of family law mediation in property settlements, the definition of property in family law, and the importance of..."),
    ("family-law-mediator", "How a Family Law Mediator Can Ease Your Parenting Disputes", "Ease your parenting disputes with a family law mediator. Find peace and solutions for your family. #familylawmediator"),
    ("how-are-assets-divided-in-a-divorce", "How Are Assets Divided In A Divorce", "Find out how assets are divided in a divorce. Navigate Australian divorce with expert guidance, legal principles, superannuation, and post-divorce..."),
    ("how-do-de-facto-couples-split-assets", "How Do De Facto Couples Split Assets?", "One commonly asked question is, \"How Do De Facto Couples Split Assets?\" In this article, we explain fully how if you are in a De Facto..."),
    ("how-do-i-change-a-consent-order", "How Do I Change a Consent Order?", "Discover the ins and outs of modifying a consent order in family law. Learn when changes are possible, the legal thresholds involved, and how to na..."),
    ("how-do-i-contact-centrelink", "How Do I Contact Centrelink in Australia?", "Learn how to contact Centrelink efficiently, tips for effective communication, and safeguarding your personal information."),
    ("how-long-do-consent-orders-take", "How Long Do Consent Orders Take?", "How Long Do Consent Orders Take is a question asked by many people looking to finally resolve a famukly law matter. In this article, we answer..."),
    ("how-long-do-consent-orders-take-in-family-law-matters", "How Long Consent Orders Take in Family Law Matters in…", "Consent orders in family law matters are a common way to ratify an agreement made in a family law dispute. Read our blog to know more!"),
    ("how-mediation-can-help-in-financial-agreements", "How Mediation Can Help in Financial Agreements", "Contact Mediations Australia for help and guidance on making a financial agreement through family law mediation today."),
    ("how-property-settlements-work", "How Property Settlements Work", "How does a property settlement work. It's a common question asked by most people who have separated or are contemplating separation."),
    ("how-to-force-a-property-settlement", "How to Force a Property Settlement", "Forcing a property settlement in Australia can be a complex and challenging process, particularly when one party is reluctant or"),
    ("how-to-get-ready-for-property-settlement-mediation", "How to Get Preparing for Property Settlement Mediation", "Property settlement mediation offers an alternative to court battles, collaboration and efficiency in resolving asset division disputes."),
    ("how-to-lodge-a-caveat-over-property-in-family-law-matters", "How to Lodge a Caveat Over Property in Family Law", "Comprehensive guide to lodging property caveats in Australian family law matters. Learn requirements, risks, alternatives, and why mediation may be..."),
    ("how-to-prepare-for-a-property-settlement-mediation", "How to Prepare for a Property Settlement Mediation", "Property settlement mediation can help you go through your separation. In this article, we’ll share some tips to help you get ready."),
    ("how-to-resolve-your-property-settlement-with-mediation-in-australia", "Resolve Your Property Settlement with Mediation in Australia", "In this article, we will explore the ins and outs of property settlement in Australia and how mediation can play a significant role in its resolution."),
    ("how-to-sell-property-during-a-divorce", "How to Sell Property During a Divorce", "Sell Property During a Divorce: Explore your options with Mediation Australia. Contact us today for guidance and support."),
    ("investment-property-division-in-family-law-disputes", "Investment Property Division in Family Law Disputes", "Investment Property Division in Family Law Disputes"),
    ("kennon-v-spry", "Kennon v Spry: The Latest on Family Trusts & Family Law", "Kennon v Spry (2008) fundamentally changed this understanding, establishing that trust assets can, in certain circumstances, be treated as property"),
    ("preparing-for-property-settlement-when-youre-financially-vulnerable", "Preparing for Property Settlement When You&#x27;re Financially…", "Preparing for Property Settlement When You&#x27;re Financially…"),
    ("property-in-divorce-settlement", "Property in Divorce Settlement", "What is Property in Divorce Settlement? In this comprehensive article, we discuss all you need to know about property settlements."),
    ("property-settlement-after-separation-time-limit", "Property Settlement After Separation Time Limit", "Property Settlement After Separation Time Limit is a commonly asked question. In this article we explain fully all you need to know..."),
    ("property-settlement-in-family-law", "Understanding Property Settlement in Family Law", "Property settlement in family law is a crucial process that occurs after a marriage or relationship breakdown. It involves the division of assets and…"),
    ("property-settlement-mediation-most-effective-strategies-for-resolving-property-settlement-disputes", "Property Settlement Mediation: Most Effective Strategies…", "Property Settlement Mediation: Most Effective Strategies…"),
    ("role-of-a-mediator-divorce-mediation", "Divorce Mediation in Australia: Understanding the Role of…", "Divorce can be a challenging and emotionally taxing process. In Australia, couples have the option to go through divorce mediation as an alternativ..."),
    ("section-79-of-the-family-law-act-1975", "Section 79 Family Law Act 1975: Property Settlement…", "Section 79 of the Family Law Act 1975 governs property division in Australian divorce. What it covers, the 4-step process, and how courts apply it."),
    ("spousal-maintenance", "Spousal Maintenance Rights: Don&#x27;t Settle for Less Than You…", "Understand your spousal maintenance rights in Australia. Learn how mediation can save you tens of thousands while securing a fair financial agreeme..."),
    ("superannuation-and-family-law-important-2024-update", "Superannuation and Family Law. Important 2024 Update", "New superannuation and family law changes announced in 2024 will have a significant impact. In this 2022 update find out what"),
    ("the-difference-between-a-divorce-lawyer-and-a-mediator", "The Difference Between a Divorce Lawyer and a Mediator", "Family law matters can be complex, but that doesn't mean that you need to run off and soldier up with a family lawyer. In this article"),
    ("understanding-property-settlement-in-divorce-a-guide-to-private-agreements", "Private Agreements-Understanding Property Settlement in…", "Private agreements in divorce necessitate consideration of property division, assets, debts, and obligations acquired during the marriage."),
    ("what-do-i-need-to-disclose-in-my-property-settlement-dispute", "What Document Do I Need to Disclose in My Property…", "What do I need to disclose in my property settlement dispute? Please read this article to know about this."),
    ("what-factors-do-property-settlement-lawyers-consider-when-dividing-assets", "What Factors Do Property Settlement Lawyers Consider When…", "Need this question answered? What Factors Do Property Settlement Lawyers Consider When Dividing Assets? In this comprehensive article.."),
    ("what-happens-to-business-in-divorce", "What Happens to Business in Divorce: Strategic Protection…", "Worried about what happens to business in divorce? Learn how to protect your company assets, understand valuation processes, and explore mediation…"),
    ("what-happens-to-superannuation-if-i-separate-or-divorce", "What Happens to Superannuation During a Divorce?", "Mediation Australia is familiar with a wide variety of family matters, including splitting superannuation when separating or divorcing. Get advice..."),
    ("what-happens-when-property-values-change-before-your-divorce-settlement-in-australia", "Property Value Changes Before Divorce Settlement Australia", "Learn how property value changes between separation and settlement affect your divorce outcome in Australia. Discover why mediation resolves proper..."),
    ("what-if-my-ex-dies-before-our-property-settlement-is-finalised", "What If Ex Die Before Finalising My Property Settlement?", "If your ex dies before your property settlement is complete, there can be major ramifications. In this article, we cover all scenarios."),
    ("what-is-alimony-in-australia", "What is Alimony in Australia? Spousal Maintenance Explained", "Alimony isn't an Australian legal term"),
    ("what-is-included-in-a-matrimonial-property-pool", "What Is Included in a Matrimonial Property Pool?", "Coming to a property settlement that meets the satisfaction of both parties is often the hardest part of a divorce. Learn more."),
    ("what-to-expect-at-a-family-law-mediation-for-property-division", "What to Expect At a Family Law Mediation for Property…", "Dealing with property assets when a couple decides to separate can be a difficult, stressful process. Mediation can be an alternative."),
    ("when-should-we-consider-property-settlement-mediation", "When Should We Consider Property Settlement Mediation?", "We Consider Property Settlement? One myth that can trip up separating couples is the belief they need to wait for a divorce to finalize a property..."),
]

PROCESS = [
    ("what-is-mediation-in-family-law","What Is Mediation in Family Law?",                  "How the process works, the mediator's role, why it succeeds, cost and time."),
    ("how-long-does-mediation-take",   "How Long Does Mediation Take?",                     "Most disputes resolve in one or two sessions — compared with years in court."),
    ("is-family-law-mediation-compulsory","Is Mediation Compulsory?",                       "When a Section 60I certificate is required, the exemptions, and if your ex refuses."),
    ("shuttle-mediation-guide",        "Shuttle Mediation Explained",                       "How keeping parties apart resolves high-conflict disputes safely."),
    ("online-mediation-australia",     "Online Mediation in Australia",                     "How it works, when to use it, and how to choose an accredited mediator."),
    ("mediate-or-litigate",            "Mediate or Litigate? How to Choose",                "An honest comparison of cost, time, control and outcomes."),
    ("what-happens-if-mediation-fails","What If Mediation Fails?",                          "Section 60I certificates, going to court, and why failure usually still helps."),
    ("arbitration-in-family-law",      "Arbitration in Family Law",                         "How a binding private decision is reached, faster than court."),
    ("are-mediation-agreements-legally-binding","Are Mediation Agreements Binding?",        "Heads of agreement, consent orders, BFAs — what each means for enforceability."),
    ("family-court-process-2026",      "The Family Court Process (2026)",                   "From filing to trial — how long it takes, what it costs, and how to avoid it."),
    ("conciliation-vs-mediation",      "Conciliation vs Mediation",                         "What each is, how the third party's role differs, and which suits your dispute."),
    ("50-years-of-the-family-law-act-how-mediation-has-changed-the-landscape", "50 Years of the Family Law Act: How Mediation Has Changed…", "50 Years of the Family Law Act: How Mediation Has Changed…"),
    ("attend-mediation-in-family-law-matters", "Do I need to attend Mediation in family law matters?", "Mediation in Family Law. Choose mediation for voluntary, cost-effective resolutions. Get legal advice for informed decisions."),
    ("commonly-asked-family-law-questions", "Commonly Asked Family Law Questions", "Here are the most commonly asked family law questions answered by Mediations Australia. If you need family law help, contact Mediations"),
    ("conciliation-in-family-law", "What is Conciliation in Family Law Matters in Australia", "Conciliation in Family Law in Australia: Resolve disputes cooperatively. Benefits include emotional support, cost savings, and efficient resolutions."),
    ("court-ordered-drug-and-alcohol-testing", "Court-Ordered Drug and Alcohol Testing in Australian…", "Court-Ordered Drug and Alcohol Testing in Australian…"),
    ("difference-between-mediation-conciliation", "What is the Difference Between Mediation and Conciliation", "What is the difference between Mediation and conciliation? What is best for your particular family law dispute is best achieved by consulting one o..."),
    ("duty-of-disclosure-in-australian-family-law", "Duty of Disclosure in Australian Family Law", "In Australian family law, parties involved in legal proceedings have a duty of disclosure, which requires them to provide all relevant information..."),
    ("family-court-mediation-process", "Confronting Family Court Mediation: Your Clear Roadmap to…", "Discover the power of family court mediation with a clear roadmap to long-lasting resolution. Learn how to greatly reduce the cost and stress without…"),
    ("family-law-mediation-what-happens-if-i-dont-want-to-do-it", "Family Law Mediation. What happens if I say No?", "At Mediations Australia, we can answer your questions regarding mediation, FDR and other types of alternate dispute resolution."),
    ("family-loan-agreement-matters", "Lending to Loved Ones? Why a Family Loan Agreement Matters", "Protect family finances with a legally binding family loan agreement. Avoid disputes, clarify terms, and safeguard relationships. Learn more today!"),
    ("family-mediation", "Family Law Dispute Mediation", "Family Law Dispute Mediation is the most effective way to resolve family law disputes. At Mediations Australia, we help you resolve family law issu..."),
    ("final-hearing-in-family-law-disputes", "Final Hearing in Family Law Disputes", "A final hearing in family law in Australia is a court proceeding in which a judge makes a final decision on the issues in a family law case."),
    ("franchise-disputes-in-australia-mediation-under-the-franchising-code-of-conduct", "Franchise Disputes in Australia: Mediation Under the Code", "Learn how the Franchising Code of Conduct requires mediation for franchise disputes in Australia, how the process works, and how to prepare for the..."),
    ("how-are-contributions-assessed-in-family-law-matters", "How Are Contributions Assessed in Family Law Matters?", "Contributions can consist of both financial and non-financial inputs into the former union. Find out more in this blog."),
    ("how-are-contributions-assessed-in-family-law-matters-2", "How Are Contributions Assessed in Family Law Matters?", "Contributions can consist of both financial and non-financial inputs into the former union. Find out more in this blog."),
    ("how-to-get-ready-for-mediation", "Tips for Preparing for Mediation", "If you have any questions on becoming better prepared for your mediation. Please read this article to get more tips for Preparing for mediation."),
    ("how-to-resolve-your-family-law-dispute-online", "How to Resolve Your Family Law Dispute Online?", "Family law disputes can now be resolved via a dispute resolution platform. Let’s take a look at how to resolve your legal disputes online."),
    ("how-you-can-reach-an-agreement-in-mediation", "How You Can Reach an Agreement in Mediation", "How you can reach an agreement in mediation. Please read this article for more information."),
    ("is-mediation-expensive", "Is Mediation Expensive?", "In the scheme of things, mediation is inexpensive when compared with the alternatives. Please read this article to get all the information."),
    ("litigation-or-mediation-choose-very-wisely", "Litigation or Mediation? Choose Very Wisely!", "You don't know how to choose between litigation or mediation. Please read this article for more information."),
    ("mediate-collaborate-or-litigate", "Mediate, Collaborate or Litigate", "Mediate, collaborate, or litigate"),
    ("mediation-in-family-law-a-comprehensive-guide", "Mediation in Family Law: A Comprehensive Guide", "Mediation in Family Law Matters is a compulsory step. When approach with a genuine commitment to negotiation, 90% of all disputes can be successfully"),
    ("mediation-or-litigation-what-is-the-best", "Mediation or Litigation. What is the Best?", "In family law cases in Australia, parties have the option of resolving their disputes through either mediation or litigation."),
    ("my-partner-wants-me-out-understanding-your-rights-when-youre-not-on-the-title", "My Partner Wants Me Out: Understanding Your Rights When…", "My Partner Wants Me Out: Understanding Your Rights When…"),
    ("nothing-alternate-about-alternate-dispute-resolution-adr", "Nothing Alternate About Alternate Dispute Resolution", "In the context of family law, there are essentially 3 types of Alternate Dispute Resolution. Please read this article for more information."),
    ("online-mediation-how-virtual-sessions-work-and-why-theyre-effective", "Online Mediation in Australia: How Virtual Sessions Work", "How online mediation works in Australia, why courts now default to virtual sessions, and how to prepare for effective dispute resolution from home."),
    ("parenting-payments-in-australia", "Parenting Payments in Australia", "Parenting payments in Australia are designed to help families with the costs of raising children. Read to learn more"),
    ("points-to-consider-family-mediation-lawyers-in-australia", "5 Points to consider family mediation lawyer in Australia", "Family mediation lawyer: Discover the significance of family mediation in Australia and the advantages it brings."),
    ("post-prenup-agreement", "Post Prenup Agreement - Everything You Need to Know", "A Post prenup agreement, also known as a binding financial agreement or a post-marriage agreement, is a legally binding contract"),
    ("postnuptial-agreement-australia-everything-you-need-to-know", "Postnuptial Agreement Australia. Everything You Need to Know", "Postnuptial Agreement Australia are what is commonly called a Binding Financial Agreement. In this article, we provide a comprehensive..."),
    ("prenups-for-women", "Prenups for Women. Everything You Need to Know", "Prenups for Women are very common. At Mediations Australia, we can help you craft the perfect, biding prenup."),
    ("privacy-policy", "Privacy Policy", "How Mediations Australia collects, uses, and protects your personal information in accordance with the Privacy Act 1988."),
    ("separated-under-one-roof", "Separated Under One Roof in Australia: Proof, Rights &…", "Separated but living in the same house? How to prove separation under one roof for divorce, Centrelink, and property settlement in Australia."),
    ("shuttle-mediation", "Shuttle Mediation. What You Need to Know", "Shuttle mediation offers an alternative to court proceedings in Australian family law disputes, providing a less adversarial approach."),
    ("strata-neighbour-dispute-mediation", "Strata & Neighbour Disputes: Resolve Without Going to a…", "Strata & Neighbour Disputes: Resolve Without Going to a…"),
    ("the-7-most-common-questions-about-mediation", "Seven Most Common Questions About Mediation", "Common questions about mediation: Seven most frequently asked questions. Contact Mediations Australia today for further information."),
    ("the-different-ways-to-resolve-family-law-disputes", "The Different Ways to Resolve Family Law Disputes", "There are now numerous ways to resolve family law disputes without having to go to court. Please get all the information here."),
    ("the-pros-and-cons-of-shuttle-mediation", "The Pros and Cons of Shuttle Mediation", "The Pros and Cons of Shuttle Mediation is a very commonly asked question. In thios comprehensive article, we cover all you need to know about shutt..."),
    ("the-role-of-the-lawyer-in-mediation", "The Role of the Lawyer in Mediation", "The role of the lawyer in mediation differs from courtroom advocacy, focusing on empowering parties to resolve disputes collaboratively."),
    ("understanding-family-conflict-and-why-mediation-is-your-best-path-forward", "Don&#x27;t Be Too Hard on Yourself", "Don&#x27;t Be Too Hard on Yourself"),
    ("what-are-family-reports-in-family-law-matters", "What are Family Reports in Family Law Matters?", "Family Reports help parents and the Court determine what is in the child's best interests in family law matters."),
    ("what-are-procedural-orders-in-family-court", "What Are Procedural Orders in Family Court?", "What are Procedural Orders in Family Court? This question is asked often by people seeking information on what best way..."),
    ("what-hannahs-law-means", "What Hannah&#x27;s Law Means for You", "What Hannah&#x27;s Law Means for You"),
    ("what-is-a-litigation-guardian-in-australia", "What is a Litigation Guardian in Australia?", "What is a Litigation Guardian is a very commonly asked question. In Australia, there are circumstances where individuals may be unable to make deci..."),
    ("what-is-a-section-60i-certificate-why-do-i-need-one", "What is a Section 60I Certificate & Why Do I Need One?", "For a couple to progress their family law matter to court, they need to obtain a Section 60I Certificate from Mediations Australia or"),
    ("what-is-the-difference-between-mediation-and-family-dispute-resolution", "What is the Difference Between Mediation and Family…", "One of the most commonly asked questions, is What is the Difference Between Mediation and Family Dispute Resolution? In this article we answer the..."),
    ("what-is-the-magellan-list", "What is the Magellan List?", "What is the Magellan List? It's a very commonly asked question. In this article, we give you all the information you need to know about the Magella..."),
    ("when-is-mediation-not-a-good-idea", "When is Mediation Not a Good Idea?", "When is Mediation Not a Good Idea. In this article we explain all the circumstances when mediation might not be best for you."),
    ("who-gets-the-dog-how-mediation-resolves-pet-disputes-after-separation", "Who Gets the Dog? How Mediation Resolves Pet Disputes…", "Discover how mediation"),
    ("why-arbitration-might-be-the-best-way-to-resolve-your-complex-family-law-dispute", "Why Arbitration Might Be the Best Way to Resolve Your…", "Why Arbitration Might Be the Best Way to Resolve Your…"),
    ("why-going-to-court-for-your-family-law-dispute-is-a-mistake", "Why Going to Court for Your Family Law Dispute is a Mistake", "Why Going to Court for Your Family Law Dispute is a Mistake"),
    ("why-mediation-works-the-science-behind-it", "Why Mediation Works: The Science Behind It", "Why mediation works is a commonly asked question. In tyhis article we give you the empirical evidence behind why mediation..."),
]

COSTS = [
    ("how-much-does-mediation-cost",   "How Much Does Mediation Cost?",                     "Family mediation fees, who pays, free options, and why it's far cheaper than court."),
    ("cost-of-divorce-in-australia",   "How Much Does Divorce Cost?",                       "Court fees, lawyer costs, and how mediation saves tens of thousands."),
    ("who-pays-for-mediation",         "Who Pays for Mediation?",                           "How the fee is usually split, when one party pays, and free options."),
    ("private-vs-free-mediation",      "Private vs Free Mediation",                         "Wait times, cost, complexity and outcomes — how to choose."),
    ("cant-afford-mediation",          "Can't Afford Mediation?",                           "Free, subsidised, Legal Aid, and reduced-fee — every realistic pathway."),
    ("is-family-mediation-free-australia","Is Family Mediation Free?",                      "When mediation can be free, when it's subsidised, and what to do if not."),
    ("family-relationship-centre-vs-private-mediation","FRC vs Private Mediation",          "An honest 10-factor comparison — when an FRC is the right call."),
    ("legal-aid-vs-private-mediation", "Legal Aid vs Private Mediation",                    "What Legal Aid covers and what to do if you don't qualify."),
    ("divorce-mediator-vs-divorce-lawyer","Mediator vs Lawyer: Which Do You Need?",         "What each does, what they cost, and why most people benefit from both."),
    ("abc-expose-the-hidden-cost-of-family-court-battles", "ABC Expose the Hidden Cost of Family Court Battles", "ABC Expose the Hidden Cost of Family Court Battles"),
    ("divorce-fees-in-australia", "Divorce Fees in Australia", "What are the Divorce Fees in Australia. In this article, we will provide a comprehensive overview of divorce fees..."),
    ("how-much-does-a-family-lawyer-cost-in-australia", "How Much Does a Family Lawyer Cost in Australia? [2026]", "What does a family lawyer cost in Australia? Typical fees, hidden costs, fixed-price options, and how mediation can save you thousands."),
    ("mediation-who-pays", "Who Pays for Mediation in Australia? Cost Splitting…", "Who covers the cost of family mediation in Australia"),
    ("the-cost-of-divorce-in-australia", "The Cost of Divorce in Australia", "The Cost of Divorce in Australia doesn't have to be as high as you may think. It's likely that you have heard of the horror stories of lawyers"),
]

HIGH_CONFLICT = [
    ("mediation-with-a-narcissist",    "Mediation With a Narcissist",                       "Yes — often better than court. Proven strategies for high-conflict exes."),
    ("high-conflict-mediation",        "High-Conflict Family Law Mediation",                "How shuttle mediation resolves even the most bitter disputes."),
    ("high-conflict-family-law-mediation","When High-Conflict Mediation Works",             "When it works, when it doesn't, and what to do instead."),
    ("domestic-violence-and-family-law","Domestic Violence & Family Law",                   "Protection orders, safety during separation, mediation exemptions, and help."),
    ("avoid-these-mistakes-with-a-binding-financial-agreement", "Avoid These Mistakes with a Binding Financial Agreement", "Considering a Binding Financial Agreement? Avoid these massive mistakes. Read this article letting you know how to avoid them."),
    ("domestic-violence", "Domestic Violence: Recognizing the Signs and Finding…", "Domestic Violence: One in Six. One in Sixteen. Understanding the impact, signs, and support options available in Australia."),
    ("intervention-orders", "Intervention Orders", "Applying for intervention orders can be an intimidating idea for those seeking protection from threats or violence. We also understand seeking an i..."),
    ("what-is-a-dvo-how-to-apply-for-a-domestic-violence-order", "What is a DVO? How to Apply for a Domestic Violence Order", "Domestic abuse has long-term consequences for the victim, their children, and their families. Learn everything you need to know about obtaining a d..."),
    ("what-is-a-restraining-order", "What is a Restraining Order? Everything You Need to Know", "One way for attempting to control the actions of a person who you fear will commit violence against you or your family is a restraining order."),
    ("what-is-an-avo", "What is an AVO?", "What is an AVO? Learn about Apprehended Violence Orders and how they can protect you from domestic and personal violence. Discover the types of AVO..."),
]

WORKPLACE = [
    ("workplace-mediation-guide",      "Workplace Mediation in Australia",                  "How it resolves workplace conflict, the Fair Work process, and the benefits."),
    ("victorian-right-to-work-from-home","Victoria's Right to Work From Home",              "What the law means for employers and employees — and resolving disputes fast."),
    ("commercial-lease-dispute-mediation-australia", "Commercial Lease Disputes: How Mediation Resolves Them", "Commercial Lease Disputes: How Mediation Resolves Them"),
    ("conflict-resolution-in-the-workplace", "Conflict Resolution in the Workplace", "Workplace conflict is costing Australian businesses between $6 and $12 billion every year. Learn step-by-step methods and your legal obligations un..."),
    ("how-employers-can-use-mediation-to-reduce-workplace-conflict-costs", "How Employers Can Use Mediation to Reduce Workplace…", "Workplace conflict costs Australia billions yearly. Learn how employers can use workplace mediation to cut costs, retain staff, and meet WHS obliga..."),
    ("how-mediation-exposes-workplace-issues-and-how-belbin-team-roles-can-help", "How Mediation Exposes Workplace Issues", "How workplace mediation reveals organisational dysfunction and how Belbin Team Roles can prevent recurring conflict. Expert insights from accredited…"),
    ("mediate-workplace-conflict-in-australia", "How to Mediate Workplace Conflict in Australia", "Workplace conflict is an inevitable reality in any organization, regardless of its size or industry. Read our blog to know more information!"),
    ("redundancy-and-restructuring-disputes-how-mediation-can-help", "Redundancy and Restructuring Disputes: How Mediation Helps", "Facing a redundancy or restructuring dispute? Learn how workplace mediation resolves genuine redundancy conflicts faster and cheaper than Fair Work..."),
    ("right-to-disconnect-workplace-mediation", "The Right to Disconnect: Resolving Disputes Under…", "The Right to Disconnect: Resolving Disputes Under…"),
    ("shareholder-partnership-dispute-mediation", "Shareholder & Partnership Disputes: Resolving Them with…", "Shareholder & Partnership Disputes: Resolving Them with…"),
    ("the-role-of-fair-work-australia-and-workplace-mediation", "The Role of Fair Work Australia and Workplace Mediation", "Workplace Mediation anf the Fair Work system offers multiple pathways for resolving workplace disputes, starting with workplace-level discussions a..."),
    ("what-is-workplace-mediation-2023-important-update", "Workplace-Mediation", "Workplace mediation: Considering it? In this article, discover all you need to know about workplace mediation."),
    ("why-workplace-conflicts-really-happen-how-mediation-resolves-them", "Why Workplace Conflicts Really Happen & How Mediation…", "The endemic causes behind Australian workplace disputes"),
    ("why-your-employee-mediation-fails-how-to-make-it-work", "Why Your Employee Mediation Fails & How to Make it Work", "Why workplace mediations fail and 4 proven strategies to fix them. Learn how employers can resolve employee disputes faster, reduce costs and meet…"),
    ("workplace-bullying-complaints-how-mediation-can-help", "Workplace Bullying Complaints: How Mediation Can Help", "Facing a workplace bullying complaint? Learn how mediation resolves bullying disputes faster and more effectively than formal tribunal proceedings..."),
    ("workplace-discrimination-mediation-your-options-in-australia", "Workplace Discrimination Mediation Your Options in Australia", "Explore your options for resolving workplace discrimination in Australia through mediation, including AHRC, Fair Work Commission, and private media..."),
    ("workplace-disputes-are-surging-why-early-mediation-is-the-smarter-path-forward", "Workplace Disputes Are Surging: Why Mediation is Best", "Australian workplaces are experiencing an unprecedented wave of formal disputes, with the Fair Work Commission facing record-breaking caseloads"),
]

ESTATE = [
    ("estate-inheritance-dispute-mediation","Estate & Inheritance Dispute Mediation",       "Contested wills, family provision claims, executor disputes — resolved faster than court."),
    ("consent-order", "Consent Order: Will They Keep Their Promise?", "Don't risk your children's future on handshake deals. Learn how to make your agreements legally binding through mediation and consent orders, saving…"),
    ("contesting-a-will-in-australia-can-mediation-avoid-a-court-battle", "Contesting a Will in Australia: Can Mediation Avoid Court?", "Over 80% of contested will claims settle at mediation. Learn how family provision claims work in Australia and how mediation can save your family t..."),
    ("contesting-a-will-with-mediation", "Contesting a Will with Mediation: A Comprehensive Guide…", "Contesting a will with mediation saves 80% on legal costs. Resolve inheritance disputes faster without court. Expert Australian mediators. Confiden..."),
    ("why-you-have-to-update-your-will-after-separation", "Updating Your Will After Separation?", "Separation and Estate Planning: Get expert legal assistance from Mediation Australia to navigate this critical juncture effectively."),
]

LEGAL_UPDATES = [
    ("changes-to-family-law-act-2025", "Changes to the Family Law Act 2025",                "The new property framework, family violence, pets — what the reforms mean for you."),
    ("surrogacy-laws",                 "Surrogacy Laws in Australia",                       "Altruistic vs commercial, legal parentage, and the state-by-state rules."),
    ("can-you-record-your-ex",         "Can You Record Your Ex?",                           "Surveillance laws, whether recordings can be used in court, and what to do instead."),
    ("breach-of-family-court-order", "Breach of Family Court Order: Immediate Legal Help (2024…", "Worried about a family court order breach? Expert guide reveals what counts as a breach, your rights, and immediate steps to protect yourself. Free…"),
    ("changes-to-the-family-law-act-2025-you-must-know", "Changes to the Family Law Act (2025) You Must Know", "Changes to the Family Law Act (2025) You Must Know"),
    ("family-court-process-2024-update", "Family Court Process: The Latest 2024 Update", "The Family Court process can be very complex. In this article, we discuss everything you need to know about the process"),
    ("family-law-regulations-explained", "Australia&#x27;s 2025 Family Law Landscape: Key Reforms and…", "Understand how Australia's 2024 family law regulations reshape the legal landscape for all families, including LGBTQ+. Explore key reforms, simplif..."),
    ("family-law-separation-agreements-the-2024-guide", "Separation Agreements in 2024: Hidden Traps & Expert…", "Mediations Australia: Your essential guidance for a separation agreement in 2024. Explore legal options, protect your assets, and secure your futur..."),
    ("fathers-rights-in-family-law-2022-update", "Fathers&#x27; Rights in Family Law Cases", "Fathers Rights: Ensure your rights are protected by consulting with a family lawyer. Contact us for assistance today."),
    ("getting-divorced-or-separated-the-2022-guide", "Getting Divorced or Separated. The 2024 Guide", "Getting divorced or separated marks a challenging period for everyone involved in a marriage or de facto relationship."),
    ("how-to-make-changes-to-a-parenting-order", "How to Make Changes to a Parenting Order", "In Australia, parenting orders are made by a court to determine the arrangements for the care, welfare, and development of a child...."),
    ("mediation-vs-collaborative-law", "Mediation vs Collaborative Law in 2024: Exploring…", "Discover the power of collaborative law in divorce resolution. Learn how this innovative approach compares to mediation, offering a path to amicable…"),
    ("shinohara-how-the-2025-family-law-changes-abolished-add-backs", "Shinohara & Shinohara: How the 2025 Family Law Changes…", "Shinohara & Shinohara: How the 2025 Family Law Changes…"),
    ("understanding-mediation-2024", "Understanding Mediation: 5 Things You May Not Know", "Understanding mediation in family law disputes 2024. Learn how this collaborative approach can save time, money, and relationships. Expert insights..."),
    ("what-is-a-prenup-agreement-in-2024", "What is a Prenup Agreement in 2025: Your Comprehensive…", "Discover what is a prenup agreement and what it really means in 2025. Mediations Australia, your trusted family law experts, offer comprehensive in..."),
    ("what-is-section-79a-of-family-law-act", "What Is Section 79A of Family Law Act", "What Is Section 79A of Family Law Act is a commonly asked question. Property settlement is a major part of family law ....."),
    ("what-you-need-to-know-about-parenting-coordination-2022-update", "What You Need to Know About Parenting Coordination: 2022…", "Parenting coordination, unlike parenting planning, is not a step in the process of creating a parenting plan. This definitive guide"),
]

# ── TOPIC SECTIONS ────────────────────────────────────────────────────────────
TOPICS = [
    ("separation",    "separation-icon",   "Separation & Divorce",        SEPARATION),
    ("parenting",     "parenting-icon",    "Parenting & Children",        PARENTING),
    ("property",      "property-icon",     "Property & Finances",         PROPERTY),
    ("process",       "process-icon",      "The Mediation Process",       PROCESS),
    ("costs",         "costs-icon",        "Costs & Affordability",       COSTS),
    ("highconflict",  "conflict-icon",     "High Conflict & Safety",      HIGH_CONFLICT),
    ("workplace",     "workplace-icon",    "Workplace Disputes",          WORKPLACE),
    ("estate",        "estate-icon",       "Estate & Inheritance",        ESTATE),
    ("updates",       "updates-icon",      "Legal Updates",               LEGAL_UPDATES),
]

# Build flat slug set for imported detection
cornerstone_slugs = set()
for _,_,_,posts in TOPICS:
    for slug,_,_ in posts:
        cornerstone_slugs.add(slug)

# ── SCHEMA ────────────────────────────────────────────────────────────────────
schema=[org_schema(),breadcrumb_schema([("Home",""),("Guides","guides")]),
        {"@type":"CollectionPage","name":"Mediation & Dispute Resolution Guides",
         "url":f"{DOMAIN}/guides/","isPartOf":{"@id":f"{DOMAIN}/#website"}}]

d = head("Mediation &amp; Dispute Resolution Guides | Mediations Australia",
    "Practical, expert guides on mediation, separation, workplace disputes, estate matters and more — written by accredited mediators to help you resolve disputes without court.",
    "guides", extra_schema=schema) + nav()

# ── TOPIC NAV ICONS (inline SVGs) ─────────────────────────────────────────────
TOPIC_ICONS = {
    "separation-icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "parenting-icon":  '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "property-icon":   '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>',
    "process-icon":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>',
    "costs-icon":      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "conflict-icon":   '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    "workplace-icon":  '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "estate-icon":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14,2 14,8 20,8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10,9 9,9 8,9"/></svg>',
    "updates-icon":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><polyline points="23,4 23,10 17,10"/><polyline points="1,20 1,14 7,14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',
}

# ── TOPIC NAV ─────────────────────────────────────────────────────────────────
def topic_nav():
    items = ""
    for tid, icon_key, label, posts in TOPICS:
        count = len(posts)
        icon = TOPIC_ICONS.get(icon_key, "")
        items += f'<a href="#{tid}" class="tnav-item"><span class="tnav-icon">{icon}</span><span class="tnav-label">{esc(label)}</span><span class="tnav-count">{count}</span></a>'
    return f'<nav class="topic-nav" aria-label="Guide topics"><div class="wrap tnav-inner">{items}</div></nav>'

# ── GUIDE CARD (compact, list-style within a topic) ───────────────────────────
def guide_card(slug, title, blurb):
    return (f'<a href="/{slug}/" class="gcard">'
            f'<span class="gcard-title">{esc(title)}</span>'
            f'<span class="gcard-blurb">{esc(blurb)}</span>'
            f'<span class="gcard-arr">→</span>'
            f'</a>')

# ── TOPIC SECTION ─────────────────────────────────────────────────────────────
def topic_section(tid, icon_key, label, posts):
    icon = TOPIC_ICONS.get(icon_key, "")
    cards = "".join(guide_card(s, t, b) for s, t, b in posts)
    return (f'<section class="tsec" id="{tid}">'
            f'<div class="wrap">'
            f'<div class="tsec-hd"><span class="tsec-icon">{icon}</span>'
            f'<h2>{esc(label)}</h2>'
            f'<span class="tsec-count">{len(posts)} guide{"s" if len(posts)!=1 else ""}</span>'
            f'</div>'
            f'<div class="gcards">{cards}</div>'
            f'</div></section>')

# ── AUTO-DISCOVER IMPORTED FOR SEARCH ─────────────────────────────────────────
SKIP_SLUGS = {
    "guides","about-mediations-australia","contact-us","book-a-consultation",
    "how-mediation-works","preparing-for-mediation","our-fee-structure",
    "family-law-mediation","divorce-mediation","property-settlement-mediation",
    "parenting-plan-mediation","section-60i-certificates","financial-agreements-mediation",
    "spousal-support-mediation","child-support-mediation","de-facto-mediation",
    "grandparents-mediation","consent-orders","online-divorce","workplace-mediation",
    "estate-dispute-mediation","collaborative-family-lawyers","family-law-arbitration",
    "divorce-counselling","memberships","our-mediators","our-team",
    "sydney-mediation","melbourne-mediation","brisbane-mediation","perth-mediation",
    "adelaide-mediation","canberra-mediation","gold-coast-mediation","newcastle-mediation",
    "wollongong-mediation","geelong-mediation","hobart-mediation","townsville-mediation",
    "cairns-mediation","toowoomba-mediation","ballarat-mediation","bendigo-mediation",
    "launceston-mediation","mackay-mediation","rockhampton-mediation","sunshine-coast-mediation",
    "bundaberg-mediation","darwin-mediation","coffs-harbour-mediation",
    "parenting-plan-template","bfa-or-consent-orders","getting-ready-for-separation",
    "family-law-cost-estimator","separation-under-one-roof-assessment",
    "questions","assets","sitemap",
}

import re as _re



# All searchable guides: cornerstones + imported
all_search = []
for _, _, _, posts in TOPICS:
    for slug, title, blurb in posts:
        all_search.append((slug, title))

imported_items = []  # now empty - all articles are in topic sections

# Combined search data (JSON for JS)
import json as _json
search_data = _json.dumps(
    [{"s": s, "t": t} for s, t in all_search],
    ensure_ascii=False
)

n_total = len(all_search)

# ── BUILD PAGE ────────────────────────────────────────────────────────────────
d += f"""<main id="main">
{crumb_html([("Home",""),("Guides",None)])}

<section class="guides-hero"><div class="wrap">
  <span class="eyebrow"><span class="pulse"></span>Expert guides — free</span>
  <h1>Find the guide <em>you need</em>.</h1>
  <p class="lede">Practical answers on separation, property, parenting, workplace and estate disputes — written by accredited mediators.</p>
  <div class="ghero-search">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="search" id="gsearch" placeholder="Search {n_total} guides &amp; articles…" aria-label="Search guides" autocomplete="off">
  </div>
  <div id="search-results" class="search-results" hidden></div>
</div></section>

{topic_nav()}

{"".join(topic_section(tid, ik, label, posts) for tid, ik, label, posts in TOPICS)}
"""

d += cta_band("Can't find what you're <em>looking for</em>?",
    "Book a free consultation and get a direct answer from an accredited mediator — tailored to your situation.")
d += "</main>" + page_end()

# ── STYLES ────────────────────────────────────────────────────────────────────
d = d.replace("</head>", """<style>
/* Hero */
.guides-hero{padding:56px 0 48px;background:var(--sand)}
.guides-hero h1{font-size:clamp(2rem,4vw,3rem);margin-bottom:16px}
.ghero-search{position:relative;display:flex;align-items:center;max-width:560px;margin-top:28px}
.ghero-search svg{position:absolute;left:18px;color:var(--ink-soft);pointer-events:none;flex-shrink:0}
#gsearch{width:100%;padding:16px 20px 16px 52px;border:1.5px solid var(--line);border-radius:14px;font-size:1rem;font-family:inherit;color:var(--ink);background:#fff;outline:none;transition:border-color .15s;box-shadow:0 2px 8px rgba(0,0,0,.06)}
#gsearch:focus{border-color:var(--sage)}

/* Search results dropdown */
.search-results{position:absolute;top:calc(100% + 6px);left:0;right:0;background:#fff;border:1.5px solid var(--line);border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,.12);max-height:420px;overflow-y:auto;z-index:200}
.sr-item{display:flex;align-items:center;padding:13px 18px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink);transition:background .12s;gap:12px;font-size:.95rem}
.sr-item:last-child{border-bottom:none}
.sr-item:hover{background:var(--sand)}
.sr-item em{color:var(--sage-deep);font-style:normal;font-weight:600}
.sr-none{padding:18px;color:var(--ink-soft);font-size:.92rem;text-align:center}

/* Topic nav */
.topic-nav{background:var(--cream);border-bottom:1px solid var(--line);padding:20px 0}
.tnav-inner{display:flex;flex-wrap:wrap;gap:10px}
.tnav-item{display:flex;align-items:center;gap:9px;padding:12px 20px;border-radius:100px;border:1.5px solid var(--line);background:#fff;color:var(--ink);text-decoration:none;font-size:.92rem;font-weight:500;transition:all .15s;white-space:nowrap}
.tnav-item:hover{border-color:var(--sage);color:var(--sage-deep);background:var(--sand)}
.tnav-icon{color:var(--sage-deep);display:flex;align-items:center;flex-shrink:0}
.tnav-count{background:var(--sage-light);color:var(--sage-deep);border-radius:100px;padding:2px 10px;font-size:.78rem;font-weight:600}

/* Topic sections */
.tsec{padding:60px 0;border-bottom:1px solid var(--line)}
.tsec:nth-child(even){background:var(--cream)}
.tsec-hd{display:flex;align-items:center;gap:16px;margin-bottom:32px}
.tsec-icon{width:48px;height:48px;border-radius:14px;background:var(--sage-light);color:var(--sage-deep);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.tsec-hd h2{margin:0;font-size:1.6rem}
.tsec-count{margin-left:auto;font-size:.88rem;color:var(--ink-soft);white-space:nowrap;flex-shrink:0}

/* Guide cards */
.gcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.gcard{display:grid;grid-template-columns:1fr auto;grid-template-rows:auto auto;gap:4px 14px;align-items:start;padding:22px 24px;background:#fff;border:1.5px solid var(--line);border-radius:14px;text-decoration:none;color:var(--ink);transition:all .15s}
.gcard:hover{border-color:var(--sage);box-shadow:0 4px 18px rgba(0,0,0,.09);transform:translateY(-1px)}
.gcard-title{font-weight:600;font-size:1.02rem;color:var(--ink);grid-column:1;line-height:1.4}
.gcard-blurb{font-size:.87rem;color:var(--ink-soft);line-height:1.55;grid-column:1;margin-top:6px}
.gcard-arr{grid-column:2;grid-row:1/3;color:var(--sage-deep);font-size:1.2rem;align-self:center;opacity:.4;transition:opacity .15s,transform .15s}
.gcard:hover .gcard-arr{opacity:1;transform:translateX(4px)}


@media(max-width:768px){
  .gcards{grid-template-columns:1fr}
  .tnav-inner{gap:8px}
  .tnav-item{padding:10px 16px;font-size:.86rem}
}
</style></head>""")

# ── SEARCH SCRIPT ─────────────────────────────────────────────────────────────
d = d.replace("</body>", f"""<script>
(function(){{
  var DATA={search_data};
  var inp=document.getElementById('gsearch');
  var box=document.getElementById('search-results');
  if(!inp)return;
  function hl(text,q){{
    if(!q)return text;
    var re=new RegExp('('+q.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&')+')','gi');
    return text.replace(re,'<em>$1</em>');
  }}
  inp.addEventListener('input',function(){{
    var q=this.value.trim();
    if(q.length<2){{box.hidden=true;return;}}
    var ql=q.toLowerCase();
    var hits=DATA.filter(function(d){{return d.t.toLowerCase().indexOf(ql)!==-1;}}).slice(0,12);
    if(!hits.length){{
      box.innerHTML='<p class="sr-none">No guides found — try different keywords.</p>';
    }}else{{
      box.innerHTML=hits.map(function(d){{
        return '<a class="sr-item" href="/'+d.s+'/">'+hl(d.t,q)+'</a>';
      }}).join('');
    }}
    box.hidden=false;
  }});
  document.addEventListener('click',function(e){{
    if(!inp.contains(e.target)&&!box.contains(e.target))box.hidden=true;
  }});
}})();
</script>
</body>""")

os.makedirs(os.path.join(OUT, "guides"), exist_ok=True)
open(os.path.join(OUT, "guides", "index.html"), "w").write(d)
n_guides = sum(len(p) for _,_,_,p in TOPICS)
print(f"Guides index built — {n_guides} cornerstones + {len(imported_items)} imported | {len(TOPICS)} topic sections")
