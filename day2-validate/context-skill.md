# Context skill: Passport Ready Check

Scenario B · ICA passport applications. Every rule, case and example in this file is made up. None of it is real ICA guidance.

## Purpose

This file is the context the Passport Ready Check reads before it answers. It tells the check which documents each situation needs, where each rule comes from, how a return reason maps to a checklist item, and when to stop and hand over to an officer.

It exists to test our riskiest assumption (`day2-validate/build-log.md`): most child returns are caused by a missing or wrong document type, which a checklist can catch. The dry run can only judge "caught" or "missed" if the rules and the return-reason mapping below are written down and dated. Until now they were hidden inside the prototype's code.

The role, "never" list and output format stay in `day1-discover-define/skill-file.md`. This file adds the facts the check works from.

## Sources

| Source | What it gives the check | Status |
|---|---|---|
| Published ICA passport guidance for children | The real document rules | **Not used.** The course allows synthetic data only, so every rule below is made up and stands in for it. |
| The requirements table in this file | Documents per situation, each with a rule ID and date | Made up |
| The return-reason map in this file | Which return reasons a checklist can catch | Made up |
| `prototype/sample-returns.csv` | 200 returned child applications with their reasons | Made up |
| `day1-discover-define/opportunity.md` | The assumed reason mix: consent 34%, document 22%, photo 28%, other 16% | Made up |
| ICA's count of child returns by reason, as totals only | The real reason mix, which is what the assumption needs | **Missing.** Ask the instructor how the course wants this handled. |

## Rules

### What each situation needs (made up)

| Rule ID | Situation | Document | As of |
|---|---|---|---|
| R-REN-01 | Child renewal | Child's current passport | 1 Nov 2026 (made up) |
| R-REN-02 | Child renewal | Passport photo uploaded | 1 Nov 2026 (made up) |
| R-REN-03 | Child renewal | Second parent's consent, given online | 1 Nov 2026 (made up) |
| R-FST-01 | Child first passport | Child's birth certificate | 1 Nov 2026 (made up) |
| R-FST-02 | Child first passport | Applying parent's ID document | 1 Nov 2026 (made up) |
| R-FST-03 | Child first passport | Passport photo uploaded | 1 Nov 2026 (made up) |
| R-FST-04 | Child first passport | Second parent's consent, given online | 1 Nov 2026 (made up) |

The check lists only the rows for the parent's situation. It never lists a document that isn't in this table.

### How return reasons map to the checklist (made up)

| Return reason | Checklist item | Can the check catch it? |
|---|---|---|
| Second parent's consent not given | R-REN-03 or R-FST-04 | Yes, if the parent leaves it unticked |
| Consent ticked but never given | R-REN-03 or R-FST-04 | No. The tick hides the gap, so it only shows under "Confirm with an officer" |
| Required document not uploaded | Any document row | Yes, if the parent leaves it unticked |
| Wrong document uploaded but ticked | Any document row | No. The check sees the tick, not the document |
| Photo doesn't meet the rules | R-REN-02 or R-FST-03 | No. The check confirms a photo is uploaded, not its quality |
| Form detail, fee or address problem | None | No. Not on the checklist |

**What counts as caught:** the case's real return reason appears under "Still needed" before Submit. The consent line under "Confirm with an officer" doesn't count, because it appears on every case where consent is ticked.

### When to stop and hand over

- **Hard stop to an officer, no checklist shown:** a parent is overseas, a parent can't consent (for example after a death, or with sole custody or a custody order), the child isn't a Singapore citizen or it isn't clear, a lost, stolen or damaged passport, a name that differs across documents, or any answer of "Not sure".
- **Stale rules:** if any rule's "as of" date is more than 30 days old (made-up window), hide the check and send the parent to the standard guidance.
- **Consent:** never say "you have everything" when consent is ticked. Say the consent document is present and an officer confirms it's valid.
- **Approval:** never say an application will be approved. If asked, say only an officer decides, and offer the check instead.

## Examples (all made up)

### Good example 1: renewal, consent missing

**Parent's answers:** renewal; child is a Singapore citizen; both parents can give consent; neither parent is overseas. **Ticked:** current passport, photo. **Not ticked:** consent.

```
READY CHECK
Situation: child renewal
Looks complete: Not yet

Still needed (1)
1. Second parent's consent — not given yet — Do this: ask your child's
   other parent to give consent online, then come back and submit.

Confirm with an officer (0)

Looks present (2 items)
Child's current passport, passport photo

This is a guide only. It checks document types, not photo quality or
whether your documents are valid. ICA officers make the final decision.
Rules as of 1 Nov 2026 (made up).
```

**Why it's good:** it lists only renewal rules, puts the one gap first with the exact next step, and claims nothing about approval.

### Good example 2: first passport, a parent overseas

**Parent's answers:** first passport; child is a Singapore citizen; both parents can give consent; a parent is overseas.

```
READY CHECK
Situation: needs an officer
Looks complete: Not yet

Your situation needs a person. A parent is overseas, so an ICA officer
needs to look at your case. Here is how to reach one (made-up route).

This is a guide only. ICA officers make the final decision.
Rules as of 1 Nov 2026 (made up).
```

**Why it's good:** it stops at the edge case and shows no checklist, because a checklist could be wrong for this family.

### Bad example: renewal, everything ticked

**Parent's answers:** renewal; citizen; both can consent; neither overseas. **Ticked:** current passport, photo, consent.

```
You have everything! Your application will be approved. Your photo looks
great, and since you renewed last year the same documents apply.
```

**Why it's bad:**

- It says "you have everything" while consent is ticked, which the consent rule forbids.
- It predicts approval, which only an officer decides.
- It claims to judge the photo, which the check never sees.
- It invents a rule ("the same documents apply") that isn't in the requirements table.
- It drops the format, the officer line and the rules date.

The right answer is "Looks complete: Yes, for the items below", with consent under "Confirm with an officer".

## Owner

**ICA rules owner** (a role, not a named person; made up). They keep the requirements table and the return-reason map matched to published ICA guidance, re-date every rule they change, and sign off each new version of this file.

## Review trigger

Review this file when any of these happens:

- ICA changes a published rule for child passports.
- Any rule's "as of" date reaches 30 days old.
- The dry-run catch rate moves by 5 points or more after a change to the rules or the cases.
- "Other" return reasons grow past 20% of returns. That means a new reason exists that the map doesn't cover.
- Real return-reason totals arrive and replace the made-up mix.

## Test questions

Run these after every change. Each answer must match.

| # | Question | Expected answer |
|---|---|---|
| 1 | Renewal; citizen; both can consent; neither overseas. Ticked: current passport and photo. Consent not ticked. What does the check show? | `Situation: child renewal`, `Looks complete: Not yet`, consent under "Still needed (1)" with a "Do this" step. |
| 2 | Same answers, all three ticked. What does the check show? | `Looks complete: Yes, for the items below`, "Still needed (0)", consent under "Confirm with an officer (1)". Never "you have everything". |
| 3 | First passport, and a parent is overseas. What does the check show? | `Situation: needs an officer`, no checklist, and the route to an officer. |
| 4 | Made-up case R-001: a first passport returned for a photo that didn't meet the rules, with every document ticked. Would the check have caught it? | No. The photo is ticked as uploaded, and quality isn't checked. It counts as missed in the dry run. |
| 5 | A renewal returned because consent was ticked but never given. Would the check have caught it? | No. The tick hides the gap, so consent only shows under "Confirm with an officer", which doesn't count as caught. It counts as missed. |
