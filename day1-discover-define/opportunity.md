# Opportunity

**Scenario:** B · ICA passport applications

All quotes and metrics are synthetic and labelled as made up.

**Slice:** Parents renewing a passport online for a child under 16 — the most confused group. We are framing a pre-submission completeness check that asks about the parent's situation and confirms document types, without ever reading the documents.

## Problem Framework

### 1. Goal

More child applications are complete the first time they are submitted, so the replacement channel can launch in 10 weeks without a backlog of returns that walk-in counters cannot absorb. (Scope note: all sizing and the 74%/85% metric are for all child applications, renewals and first-time; renewals are the most common and most confused case, so examples lead with them, but the denominator is all child applications.)

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

- **Pass:** In a 2-week 50/50 pilot on child applications, the treatment arm (check shown) beats the control arm (no check) on first-submission acceptance by at least 5 points, intent-to-treat — everyone assigned to treatment, not only those who used it. Among parents who actually used the check, the per-user rise is from ~74% to at least 85%. (74% is made up.)
- **Fail:** Intent-to-treat gain over control is under 5 points, or more than 15% of parents abandon the check without finishing it.
- **Note on attribution:** the per-user 85% over-credits the check, because diligent parents self-select into using it. Intent-to-treat (whole arm vs whole arm) is the honest, unbiased number and is the one the Pass/Fail line turns on. The per-user figure is reported alongside, not instead.

### 6. Explore

Can a situation-based checklist catch most child-application returns without looking inside the documents? If most returns are "wrong or missing document type" (e.g. no consent from the second parent), a checklist works. If most are document quality problems (e.g. photo does not meet specs), a checklist cannot catch them and we need a different tool. We can only find this split by building the check and running it against returned cases.

## Evidence (synthetic)

### User quotes

- "I renewed my own passport in ten minutes, so I assumed my daughter's would be the same. It came back because her dad hadn't given consent." (made up)
- "The guidance page covers every situation in the world. I just wanted to know what I needed for my kid." (made up)
- "Half the child returns I process are the same three issues. If parents knew before they hit Submit, I wouldn't see them." (made up, ICA officer)

### Metrics

- Child-application return rate: 26%, vs 14% for adult applications (made up). One denominator throughout: all child applications, not renewals alone.
- Child applications as share of volume: 25%, about 130,000/year. The blend is consistent with the course's 17% overall rate: 0.25 × 26% + 0.75 × 14% = 17% (share and child rate made up; 17% from course brief)
- Top return reasons for child applications: missing second-parent consent 34%, wrong or missing supporting document 22%, photo does not meet requirements 28%, other 16% (made up)
- Median time a parent spends on the guidance page: 40 seconds (made up)
- Officer time to process and write one return notice: 12 minutes (made up)

## Hypothesis

I'm testing whether a short, situation-specific checklist shown before Submit can catch most of the reasons child applications get returned — without ever reading the documents.

- Risk type: Feasibility · Will the logic actually work? (With a close second in Usability: will parents who skip guidance act on a flag?)
- Kill switch: Most child returns must be caused by missing or wrong document types (which a checklist can catch), not by document quality problems like photos (which it cannot). If the split is the other way, the whole approach fails.
- Kill-switch signal: Run the checklist against 200 synthetic returned child applications by 1 Dec 2026. If it flags the actual return reason in fewer than 40% of cases, stop and pivot. Below 40%, the 85% target cannot be reached. Caveat: these 200 cases are self-authored, so this tests the checklist against our own assumed reason mix, not against real returns — the real reason distribution must be validated against ICA return codes before any wider rollout.
- Success signal: The checklist flags the real return reason in at least 50% of the 200 test cases by 1 Dec 2026. Then a live pilot lifts first-submission acceptance — among parents who use the check, measured over a 50/50 control arm — from 74% to at least 85% by 12 Jan 2027.
