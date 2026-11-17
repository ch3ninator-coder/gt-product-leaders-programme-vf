# Opportunity

**Scenario:** B · ICA passport applications

All quotes and metrics are synthetic and labelled as made up.

**Slice:** Parents applying online to renew a passport for a child under 16. We are framing a pre-submission check. The parent answers 3 to 4 questions about their situation, then confirms what they have against a checklist made for that situation. The check never reads the documents.

## Problem Framework

### 1. Goal

More child applications are complete the first time they are submitted. That way the replacement channel launches in 10 weeks without a backlog of returns that walk-in counters cannot absorb.

The outcome is the first-submission acceptance rate. A chatbot shipped on time is only an output.

### 2. Problem

Parents only find out their application is incomplete after an officer reviews it, days later. The guidance is generic and long, so most people skip it (only 38% read it). None of it tells a parent what "complete" means for their own case. The feedback comes too late and is too vague.

From the brief: 17% of ~520,000 applications a year comes to about 88,000 returns, or about 1,700 a week. Each one adds about 6 days.

### 3. Context

- **Who:** Parents or guardians renewing a passport for a Singapore citizen child under 16. The brief names them as the most confused group.
- **Where:** In the online application, after the documents are uploaded and before Submit. This is the last point where an error is cheap to fix.
- **When:** Now, during the 10 weeks before the vendor withdraws. Counters can cover only ~35% of online demand, so a slow or error-prone replacement channel pushes people to counters that cannot take them.
- **Also affected:** ICA officers, who do the rework on every avoidable return.

### 4. Constraints

- The vendor exit date is fixed: about 10 weeks, around 26 Jan 2027. Whatever we test has to be buildable in that window.
- Applications hold identity documents and sensitive personal data. The check asks about the applicant's situation and document *types*. It never reads, stores or repeats document contents.
- Officers make every decision. The check only says what is usually required. It never says "your application will be accepted".
- Every requirement must trace to current published ICA guidance, with a "rules as of [date]" stamp. When rules change, the checklist must be updated and re-dated.
- Edge cases the check cannot handle (a parent overseas, a parent who is deceased, a custody order) go straight to an officer. The check does not guess.

### 5. Success

- **Pass:** In a 2-week pilot, the first-submission acceptance rate for child renewals rises from 74% to at least 85% for parents who used the check. (74% is made up.)
- **Fail:** It rises by less than 5 percentage points, or more than 15% of parents leave the check without finishing it.

### 6. Explore

How many child-renewal returns can a situation-based checklist catch without looking inside the documents?

If most returns are "wrong or missing document" (for example, no consent from the second parent), a checklist works. If most are document quality problems (for example, a photo that does not meet the rules), a checklist cannot catch them and we need a different tool. We can only find this split by building the check and running it against returned cases.

## Evidence (synthetic)

### User quotes

- "I renewed my own passport online in ten minutes, so I assumed my daughter's would be the same. It came back because her dad hadn't given consent." (made up)
- "The guidance page covers every situation in the world. I just wanted to know what *I* needed for *my* kid." (made up)
- "Half the returns I process for children are the same three issues. If parents knew before they hit Submit, I wouldn't see them." (made up, ICA officer)

### Metrics

- Return rate for child renewals: 26%, against 14% for adult renewals (made up)
- Child applications as a share of all volume: 30%, about 156,000 a year (made up)
- Return reasons for child applications: missing second-parent consent 34%, missing or wrong supporting document 22%, photo does not meet requirements 28%, other 16% (made up)
- Median time parents spend on the guidance page: 40 seconds (made up)
- Officer time to process and write one return: 12 minutes (made up)

## Hypothesis

I'm testing whether a short, situation-specific checklist shown before Submit can catch most of the reasons child-renewal applications get returned, without ever reading the documents.

- Risk type: Feasibility · Will the logic actually work?
- Kill switch: Most child-renewal returns are caused by missing or wrong document *types*, which a checklist can catch, not by document *quality*, which it cannot.
- Kill-switch signal: Run the checklist against 200 made-up returned child applications by 1 Dec 2026. If it would have flagged the actual return reason in fewer than 50% of them, stop. Then pivot to a photo and document quality check, or to an officer-side tool.
- Success signal: The checklist flags the real return reason in at least 70% of the 200 test cases by 1 Dec 2026. Then a live pilot lifts first-submission acceptance for child renewals from 74% to at least 85% by 12 Jan 2027, two weeks before the vendor exits.
