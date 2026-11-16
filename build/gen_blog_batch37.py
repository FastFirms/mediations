"""gen_blog_batch37.py: flexible-work-request-refused (workplace).
Facts checked against Fair Work Act 2009 (Cth) ss 65, 65A, 65B, 65C (Nov 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite

body = (
  key_takeaway("If an eligible employee's flexible work request is refused, or ignored for 21 days, the "
               "Fair Work Act requires both sides to first try to resolve it by discussion at work. If that "
               "fails, either party can take it to the Fair Work Commission, which must try mediation or "
               "conciliation before it can arbitrate. Mediating early usually settles it faster.")
  + f"""
<h2 id="why-now">Why flexible work disputes are rising</h2>
<p>Return-to-office mandates, longer commutes and a workforce juggling school pick-ups and ageing parents have turned flexible work into one of the most common sources of friction between employees and employers. Since June 2023, the rules have also had real teeth. Changes to the {cite('fwa_flexible')} made by the Secure Jobs, Better Pay reforms introduced a strict process for responding to requests and gave the {cite('fair_work')} power to resolve disputes, including by making binding orders.</p>
<p>That shift matters for both sides. An employer who once could say "no" in a short email now has to follow defined steps, and an employee who is refused now has a clear pathway. Most of these disputes, though, are not really about the law. They are about trust, workload, fairness between team members and a manager's worry about precedent. That is exactly the territory where a neutral conversation does better than a formal fight.</p>
<p>This guide covers the national rules. Victoria is also moving toward a separate right to work from home; see our guide to <a href="/victorian-right-to-work-from-home/">Victoria's right to work from home</a>.</p>
"""
  + inline_cta("Has a flexible work request turned into a standoff? Talk to us about resolving it early.")
  + """
<h2 id="who-can-ask">Who has a legal right to request flexible work</h2>
<p>Any employee can ask for flexibility, but the formal right in section 65 of the Fair Work Act applies to employees in particular circumstances. An employee can make a request if they:</p>
<ul>
  <li>are pregnant;</li>
  <li>are the parent, or have responsibility for the care, of a child who is school age or younger;</li>
  <li>are a carer within the meaning of the <em>Carer Recognition Act 2010</em>;</li>
  <li>have a disability;</li>
  <li>are 55 or older;</li>
  <li>are experiencing family and domestic violence; or</li>
  <li>provide care or support to a member of their immediate family or household who is experiencing family and domestic violence.</li>
</ul>
<p>Employees returning from parental leave can also ask to return part time to help care for the child.</p>
<p>There is a service requirement. A permanent employee needs at least 12 months of continuous service with the employer. A casual employee qualifies if they have worked on a regular and systematic basis for at least 12 months and reasonably expect that work to continue. The request must be in writing and set out the change sought and the reasons for it.</p>
"""
  + inline_cta("Not sure whether a request is covered? We can help both sides understand where they stand.")
  + """
<h2 id="employer-duties">What an employer must do before saying no</h2>
<p>Under section 65A, the employer must give a written response within <strong>21 days</strong>. It must either grant the request, record an agreed alternative, or refuse it. A refusal is only allowed if the employer has:</p>
<ol>
  <li>discussed the request with the employee;</li>
  <li>genuinely tried to reach agreement on a change that accommodates the employee's circumstances;</li>
  <li>had regard to the consequences of refusal for the employee; and</li>
  <li>a refusal based on <strong>reasonable business grounds</strong>.</li>
</ol>
<p>A written refusal must explain the reasons, the specific business grounds and how they apply to this request, and any other changes the employer would be willing to make (or state that there are none). It must also tell the employee about their right to take the dispute further under sections 65B and 65C.</p>
<figure class="tbl"><table><caption>Reasonable business grounds listed in the Act (examples, not an exhaustive list)</caption>
<thead><tr><th>Ground</th><th>What it looks like in practice</th></tr></thead>
<tbody>
<tr><td>The new arrangement would be too costly</td><td>Extra equipment, duplicated roles or overtime to cover the gap</td></tr>
<tr><td>Other employees' arrangements can't be changed to accommodate it</td><td>A roster that only works if everyone covers set shifts</td></tr>
<tr><td>It would be impractical to change others' arrangements or recruit</td><td>A small team with no realistic backfill</td></tr>
<tr><td>A significant loss in efficiency or productivity</td><td>Work that genuinely depends on being on site together</td></tr>
<tr><td>A significant negative impact on customer service</td><td>Counter, clinical or client-facing hours that can't be met remotely</td></tr>
</tbody></table></figure>
<p class="source-note">Summary of s 65A of the Fair Work Act 2009 (Cth). General information only, not legal advice.</p>
<p>The step most often skipped is the genuine discussion. A refusal sent without a real conversation is the easiest kind for the Commission to find wanting, and it is also the one most likely to damage the working relationship.</p>
"""
  + inline_cta("Employers: a facilitated conversation can show you genuinely tried to reach agreement, and often finds one.")
  + f"""
<h2 id="dispute-path">What happens if the request is refused or ignored</h2>
<p>Section 65B applies when the employer refuses, or when 21 days pass without a written response. The process is staged:</p>
<ol>
  <li><strong>Workplace discussion first.</strong> The parties must first try to resolve the dispute by discussion at the workplace level.</li>
  <li><strong>Referral to the Fair Work Commission.</strong> If that fails, either party can refer the dispute to the Commission.</li>
  <li><strong>Mediation or conciliation.</strong> The Commission must first deal with it by means other than arbitration, such as mediation, conciliation, making a recommendation or expressing an opinion, unless there are exceptional circumstances.</li>
  <li><strong>Arbitration as a last resort.</strong> Under section 65C the Commission can arbitrate and make orders, including that the employer is taken to have refused, that its grounds were or were not reasonable, that it take further steps, or, if there is no reasonable prospect of resolving it otherwise, that the request or an alternative be granted.</li>
</ol>
<p>Breaching a Commission order is a civil remedy provision, so these orders are enforceable. The {cite('fwo_flexible')} has practical guidance for both sides. If your workplace is covered by an enterprise agreement or award, check its dispute resolution clause too, as it may set out additional steps.</p>
"""
  + inline_cta("Prefer to settle it before it reaches the Commission? Independent mediation can happen within days.")
  + """
<h2 id="why-mediate">Why mediation works well for these disputes</h2>
<p>A flexible work dispute is rarely a single yes-or-no question. Underneath it there is usually a mix of practical needs (school hours, medical appointments, a carer's roster) and organisational worries (fairness to the rest of the team, coverage, whether one exception will open the floodgates). A formal process forces both sides to argue positions. Mediation lets them work on the actual problem.</p>
<ul>
  <li><strong>It satisfies the spirit of the law.</strong> The Act asks both sides to genuinely try to reach agreement. An independent mediator makes that effort real and visible.</li>
  <li><strong>It finds middle options.</strong> Trial periods, compressed hours, a hybrid split, adjusted start times or a review date are often more workable than the original request or a flat refusal.</li>
  <li><strong>It protects the relationship.</strong> The employee keeps working for the same manager tomorrow. An outcome both helped design is far easier to live with than one imposed by a third party.</li>
  <li><strong>It is confidential and fast.</strong> A session can usually be arranged within days, rather than waiting on a Commission listing.</li>
</ul>
<p>Mediation is not right in every case. Where the request is linked to family and domestic violence, safety and privacy come first; separate sessions or a support person may be needed, and confidential support is available through 1800RESPECT (1800 737 732). If you are in immediate danger, call 000.</p>
"""
  + callout("A worked example (illustrative only)",
            "Mia, a team leader with three years' service, asks to work from home two days a week so she can do school pick-up. "
            "Her manager refuses by email, citing team cohesion, without meeting her. In mediation the manager explains the real "
            "concern: two other team members have asked for the same days. The agreed outcome is a three-month trial of one fixed "
            "home day plus a 2:30pm early finish on Wednesdays, with a rostered team day on Tuesdays and a review meeting at the end "
            "of the trial. This is a composite scenario, not a real client.")
  + inline_cta("Want a practical outcome both sides can live with? Book a free, confidential consultation.")
  + """
<h2 id="prepare">How to prepare, whichever side you are on</h2>
<p><strong>Employees:</strong> put your request in writing, say which eligibility circumstance applies, and be specific about the change and why you need it. Think about how the work will still get done, and what you could offer in return, such as core in-office days, a trial period or flexibility around busy periods. Keep a copy of every message and note the date you sent the request.</p>
<p><strong>Employers:</strong> meet the employee before deciding, ask what is driving the request, and consider alternatives seriously. If you refuse, tie your reasons to the specific job and team, not a general policy, and set out any alternative you would accept. Remember the 21-day clock starts when the request is received.</p>
<p><strong>Both:</strong> if the conversation stalls, bring in an independent mediator before positions harden. Our <a href="/workplace-mediation/">workplace mediation</a> service is built for exactly this, and you can check <a href="/workplace-mediation-cost/">what workplace mediation costs</a> before you commit.</p>
"""
  + inline_cta("Talk to an accredited workplace mediator about your situation, confidentially.")
)

qa = [
 ("How long does an employer have to respond to a flexible work request?",
  "The employer must give a written response within 21 days of receiving the request. If it doesn't respond in that time, the employee can treat that as a dispute and, after trying to resolve it at the workplace, refer it to the Fair Work Commission."),
 ("Can my employer refuse a flexible work request?",
  "Yes, but only on reasonable business grounds, and only after discussing the request with you, genuinely trying to reach agreement and considering the consequences of refusal for you. The refusal must be in writing and explain the reasons and any alternative the employer would accept."),
 ("Who is eligible to request flexible working arrangements?",
  "Employees with at least 12 months' continuous service (or long-term regular casuals) who are pregnant, are parents or carers of a school-age or younger child, are carers, have a disability, are 55 or older, are experiencing family and domestic violence, or are supporting a family or household member experiencing it."),
 ("Can the Fair Work Commission force my employer to agree?",
  "It can, but only as a last resort. The Commission must first try mediation, conciliation or a recommendation. If there is no reasonable prospect of resolving the dispute otherwise, it can arbitrate and order that the request, or an alternative change, be granted."),
 ("Do we have to try to resolve it at work first?",
  "Yes. The Act requires the employer and employee to first attempt to resolve the dispute by discussion at the workplace level before either refers it to the Fair Work Commission."),
 ("Is mediation confidential?",
  "Yes. Workplace mediation is confidential, and what is said is generally treated as without prejudice. That makes it easier to explore options such as trial periods or hybrid arrangements without either side feeling locked in."),
 ("Does Victoria have different rules?",
  "Victoria has announced its own right to work from home for some employees. The national Fair Work Act rules in this guide still apply. See our guide to Victoria's right to work from home for the state-specific position."),
]

post(
  "flexible-work-request-refused",
  "Flexible Work Request Refused? Your Options in Australia",
  "Flexible work request refused or ignored? What the Fair Work Act requires, how disputes reach the Fair Work Commission, and how mediation resolves them faster.",
  "Workplace",
  "Flexible work request <em>refused</em>",
  "Since 2023, refusing a flexible work request has come with strict rules and a path to the Fair Work Commission. Here is what employers must do, what employees can do, and how to resolve the dispute before it escalates.",
  [("why-now", "Why flexible work disputes are rising"),
   ("who-can-ask", "Who has a legal right to request"),
   ("employer-duties", "What an employer must do before saying no"),
   ("dispute-path", "If the request is refused or ignored"),
   ("why-mediate", "Why mediation works well"),
   ("prepare", "How to prepare")],
  body, qa,
  [("workplace-mediation", "Workplace Mediation"),
   ("victorian-right-to-work-from-home", "Victoria's Right to Work From Home"),
   ("right-to-disconnect-workplace-mediation", "Right to Disconnect"),
   ("workplace-mediation-cost", "Workplace Mediation Cost"),
   ("is-mediation-right-for-workplace-dispute", "Is Mediation Right for You?"),
   ("workplace-mediation-guide", "Workplace Mediation Guide")],
  read_min=9,
)
print("flexible-work-request-refused built")
