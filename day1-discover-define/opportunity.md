# Opportunity

**Scenario:** B · ICA passport applications

All quotes and metrics are synthetic and labelled as made up.

**Slice:** Parents renewing a passport online for a child under 16 — the most confused group. We are framing a pre-submission completeness check that asks about the parent's situation and confirms document types, without ever reading the documents.

## Problem Framework

### 1. Goal

More child-renewal applications are complete the first time they are submitted, so the replacement channel can launch in 10 weeks without a backlog of returns that walk-in counters cannot absorb.

### 2. Problem

Parents only discover their application is incomplete after an officer reviews it days later. The guidance page is generic and long (only 38% read it), so most parents skip it. None of it tells a parent what "complete" means for their specific situation. The feedback arrives too late and is too vague to act on quickly. 17% of ~520,000 applications a year means roughly 88,000 returns; each adds about 6 days.

### 3. Context

- **Who:** Parents or guardians renewing a passport for a Singapore citizen child under 16 — named in the brief as the most confused group.
- **Where:** The online passport application, after documents are uploaded and before Submit. This is the last moment where fixing an error is cheap.
- **When:** Within 10 weeks, before the vendor withdraws. Counters handle only ~35% of current online demand, so a slow or error-prone replacement pushes people to counters that cannot take them.
- **Also affected:** ICA officers who spend time processing and writing return notices for every avoidable error.

### 4. Constraints

- Vendor exit date is fixed at ~10 weeks (around late January 2027). The check must be buildable within that window.
- Applications hold identity documents and sensitive personal data. The check asks about the applicant's situation and document types only — it never reads, stores or repeats document contents.
- Officers make every final decision. The check says what is usually required; it never says "your application will be accepted."
- Every requirement must trace to current published ICA guidance with a "rules as of [date]" stamp. When rules change, the checklist must be updated.
- Edge cases (parent overseas, deceased parent, custody order) go straight to an officer. The check does not guess.

### 5. Success

- **Pass:** In a 2-week pilot, first-submission acceptance rate for child renewals rises from ~74% to at least 85% among parents who used the check. (74% is made up.)
- **Fail:** Improvement is less than 5 percentage points, or more than 15% of parents abandon the check without finishing it.

### 6. Explore

Can a situation-based checklist catch most child-renewal returns without looking inside the documents? If most returns are "wrong or missing document type" (e.g. no consent from the second parent), a checklist works. If most are document quality problems (e.g. photo does not meet specs), a checklist cannot catch them and we need a different tool. We can only find this split by building the check and running it against returned cases.

## Evidence (synthetic)

### User quotes

- "I renewed my own passport in ten minutes, so I assumed my daughter's would be the same. It came back because her dad hadn't given consent." (made up)
- "The guidance page covers every situation in the world. I just wanted to know what I needed for my kid." (made up)
- "Half the child returns I process are the same three issues. If parents knew before they hit Submit, I wouldn't see them." (made up, ICA officer)

### Metrics

- Child-renewal return rate: 26%, vs 14% for adult renewals (made up)
- Child applications as share of volume: ~30%, about 156,000/year (made up)
- Top return reasons for child applications: missing second-parent consent 34%, wrong or missing supporting document 22%, photo does not meet requirements 28%, other 16% (made up)
- Median time a parent spends on the guidance page: 40 seconds (made up)
- Officer time to process and write one return notice: 12 minutes (made up)

## Hypothesis

I'm testing whether a short, situation-specific checklist shown before Submit can catch most of the reasons child-renewal applications get returned — without ever reading the documents.

- Risk type: Feasibility · Will the logic actually work?
- Kill switch: Most child-renewal returns must be caused by missing or wrong document types (which a checklist can catch), not by document quality problems (which it cannot). If the split is the other way, the whole approach fails.
- Kill-switch signal: Run the checklist against 200 synthetic returned child applications by 1 Dec 2026. If it flags the actual return reason in fewer than 50% of cases, stop and pivot.
- Success signal: The checklist flags the real return reason in at least 70% of the 200 test cases by 1 Dec 2026, and a live pilot lifts first-submission acceptance for child renewals by at least 10 percentage points by 12 Jan 2027.
