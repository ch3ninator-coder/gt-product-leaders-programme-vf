# One Pager

Use case: **Scenario B · ICA passport applications and renewals** (synthetic data only; all quotes and metrics are made up)

## Problem and user

**User:** Parents or guardians renewing a passport online for a Singapore citizen child under 16. The brief names them as the most confused group.

**Problem:** Parents only find out their application is incomplete after an officer has reviewed it, days later. The guidance is long and generic, and only 38% read it. None of it tells a parent what "complete" means for their own case. 17% of ~520,000 applications a year are returned, about 88,000 returns, and each adds ~6 days.

**Status quo:** The vendor-run online channel withdraws in 10 weeks, on a date that will not move. Walk-in counters can cover only ~35% of online demand.

## Opportunity and evidence

**Opportunity:** A pre-submission check. The parent answers 3–4 questions about their situation and confirms the document types they have against a checklist for that situation. The check never reads the documents. Full framing: `day1-discover-define/opportunity.md`.

**Evidence (made up):**
- Child-renewal return rate is 26%, against 14% for adults.
- Missing consent from the second parent causes 34% of child returns.
- Parents spend a median of 40 seconds on the guidance page.

**Success metric:** Among parents who use the check, first-submission acceptance for child applications rises from ~74% to at least 85% in the pilot — measured as the gain over a 50/50 control arm, not an absolute number, so seasonal drift does not read as success. Population-wide, at an assumed 70% uptake, that is about an 8-point lift, not 11.

## Experience and trust

The flow and its trust design are in `day1-discover-define/ai-ux-flow.md`. In short: the check opens by itself for child-under-16 applications, echoes the parent's answers back so a wrong turn is visible, dates every rule, and reads no documents. The parent ticks what they have and can always submit without the check — it is a guide, not a gate. The rule for when a human steps in: the check escalates to an officer whenever being wrong costs more than staying silent (edge cases, stale rules, and any "all clear" on consent it cannot confirm).

## Risks (market, technical, team)

*To be completed in Day 2*

## Build plan and handoff

*To be completed in Day 2*

## Agent role and guardrails

*To be completed in Day 3*

## Roles and operating model

*To be completed in Day 3*

## Strategy and roadmap

### Strategy kernel

Full working-backwards version: `day3-build/prfaq.md`.

**Diagnosis:** Errors are found too late. Child applications are 25% of volume but 38% of returns, about 650 a week (made up). Parents only learn what "complete" means from a return notice, six days later. About 56% of those returns are rule-based (missing consent, wrong document), so they are preventable before Submit. The vendor leaves in 10 weeks and counters cover only 35% of demand, so the new channel cannot afford a backlog of avoidable returns on day one.

**Guiding policy:** Move the completeness check to before Submit, starting with child applications. Use only document types and dated ICA rules. Never read document contents and never make decisions; officers decide. Photo quality is out of scope for v1.

**Three coherent actions:**
1. **Build** a 4-question screener and situation checklist. Every item traces to a dated ICA rule, and one named owner re-dates it on every rule change.
2. **Test** the checklist against 200 made-up returned applications by 1 Dec 2026. Kill if the catch rate is under 40%. Continue if it is 50% or more.
3. **Pilot** it as a 50/50 live split from 29 Dec 2026 to 12 Jan 2027, with edge cases sent to officers. Target: among users, a lift from 74% to 85% or higher over the control arm, which needs catch rate × fix rate ≥ 42%.

**Known limit of the cheap test:** the 1 Dec dry run uses 200 applications we authored, so it checks that the checklist matches our own assumed return reasons — not that real returns are 56% rule-based. The live pilot is the first real test of that assumption, and of the behavioural risk (will parents who skip guidance act on a flag?). Validate the reason mix against real ICA return codes before any wider rollout.

**What this does not solve:** about 190 avoided returns a week is a small share of counter capacity, and not every return becomes a counter visit. The new channel itself must still launch on time; this check depends on that channel shipping.

*Roadmap to be completed in Day 3, Module 9*

## Metrics plan and stop line

*To be completed in Day 4*

## Evals and gates

*To be completed in Day 4*

## Decision: continue, pivot or stop

*To be completed in Day 4*

## Open issues

*To be completed in Day 4*
