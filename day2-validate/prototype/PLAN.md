# Prototype plan: Passport Ready Check

Scenario B · ICA passport applications. Day 2, Lab 1. This is a plan only. No code yet.

All rules, documents, dates, routes and cases in the prototype are made up, and each one is labelled "(made up)". Nothing in it is real ICA guidance.

## 1. The cheapest test for each risk

A full clickable prototype is not the cheapest test of the hypothesis in `day1-discover-define/opportunity.md`. Each risk gets the cheapest test that answers it, in this order:

| Order | Risk | Cheapest test | Why this order |
|---|---|---|---|
| 1 | **Feasibility:** are most child returns caused by missing or wrong document types, not photo problems? | Return-reason data. In practice: ICA's count of child returns by reason (totals only, no personal data). In this course: a spreadsheet of 200 made-up returns, each tagged with its reason and whether the checklist would catch it. | It can stop the idea before anything is built. |
| 2 | **Usability:** will a parent act on a flag? | One fixed result screen (missing consent) shown to five people (section 9). | It needs one screen, not the whole flow. |
| 3 | **Does it all work together?** | The clickable flow, which is the real MVP. | Only worth building if tests 1 and 2 pass. |

**Limit:** the made-up spreadsheet is circular, because we wrote the return reasons ourselves. Only real return data truly tests feasibility.

Lab 1 builds the screen for test 2. Nothing here is production code or connects to any ICA system.

## 2. Format

- One HTML file: `day2-validate/prototype/index.html`. It opens by double-click and works offline. No build step and no network requests.
- Rules, made-up cases and the dry run all live in this one file, so the dry run and the parent see the **same** rules. A separate rules file could fail to load from a local file and would split the logic in two.
- System font stack. The course fonts in `assets/fonts/` are Product School branding, and a mock government service should not carry it.
- A small "Demo controls (prototype only)" panel, clearly set apart from the parent's view, holds two buttons: **Simulate stale rules** and **Run dry run**.

## 3. Situations covered

| Situation | Built? |
|---|---|
| Child renewal (Singapore citizen child) | Yes |
| Child first-time (Singapore citizen child) | Yes |
| Needs an officer (every edge case) | Yes, as a hard stop |

These are the three values of `Situation` in `day1-discover-define/skill-file.md`. Anything else is "needs an officer".

## 4. Questions and outcomes

There are up to four questions, one per screen. The progress marker reads "Question n of up to 4", because a hard stop can end the flow early. Every question screen also has a **"Something else applies to us"** link, which goes to the officer route. This covers a name that differs across documents, and any case the questions don't reach.

| Q | Question | Answer | Outcome |
|---|---|---|---|
| 1 | What are you applying for? | Renewal of my child's passport | Continue as child renewal |
| 1 | | My child's first passport | Continue as child first-time |
| 1 | | Replacing a lost, stolen or damaged passport | Hard stop: officer route (police-report route, made up) |
| 1 | | Not sure | Hard stop: officer route |
| 2 | Is your child a Singapore citizen? | Yes | Continue |
| 2 | | No, or not sure (e.g. dual nationality) | Hard stop: "This check covers Singapore citizen children only" + officer route |
| 3 | Can both parents give consent? | Yes | Continue |
| 3 | | No (e.g. a parent has died, sole custody, a custody order), or not sure | Hard stop: officer route |
| 4 | Is either parent overseas right now? | No | Continue to the checklist |
| 4 | | Yes, or not sure | Hard stop: officer route |

**Rule:** any answer not in this table goes to the officer route. The check never picks the nearest match.

## 5. The checklist (made up)

The checklist screen is titled for the exact case, for example "What you need for: child renewal, Singapore citizen, both parents consenting". The parent's answers are echoed at the top, each with a **Change** link that re-runs the flow from that question. Every item has its own "Rules as of [date] (made up)" in the rules data, shown under "What we checked" rather than on each line.

| Group | Child renewal | Child first-time |
|---|---|---|
| Identity documents | Child's current passport | Child's birth certificate |
| Supporting documents | Second parent's consent (given online) | Second parent's consent (given online); applying parent's ID document |
| Photo | Passport photo uploaded | Passport photo uploaded |
| Fees | Not shown in this prototype | Not shown in this prototype |
| What to expect | An ICA officer reviews every application | Same |

- **Photo:** the parent can tick that a photo is uploaded. A fixed reminder line reads "Photo quality is not checked here (reminder only)". The photo rules are not shown, because that would mean inventing them.
- **Fees:** no amounts are shown. `skill-file.md` forbids inventing fees, and a made-up fee could be mistaken for a real one.
- The parent ticks **document types only**. There are no text inputs anywhere: no name, NRIC, passport number or date of birth.

## 6. Consent rule

Second-parent consent is the largest made-up return reason (34%), and the check can never confirm it is valid.

- **Consent ticked:** it appears under "Confirm with an officer: second-parent consent. Only an officer can confirm the consent is valid."
- **Consent not ticked:** it appears under "Still needed: second-parent consent. Do this: ask the second parent to give consent online (made-up step)."
- The result never says "you have everything", "ready" or "approved".
- "Looks complete: Yes, for the items below" appears only when Still needed is (0). Even then, "Confirm with an officer" stays visible.

## 7. The result screen (READY CHECK)

The result follows the format in `skill-file.md` exactly:

```
READY CHECK
Situation: [child renewal | child first-time | needs an officer]
Looks complete: [Yes, for the items below | Not yet]

Still needed ([count])
1. [Item] — [what is missing] — Do this: [exact action]

Confirm with an officer ([count])
1. [Item] — [why only an officer can confirm it]

Looks present ([count] items)
[comma-separated document types ticked]

This is a guide only. It checks document types, not photo quality or
whether your documents are valid. ICA officers make the final decision.
Rules as of [date] (made up).
```

- Still needed comes before Confirm with an officer. Empty sections show "(0)".
- One line per item. The whole result is under 300 words.
- A hard stop renders `Situation: needs an officer` with the fallback text "Your situation needs a person. Here is how to reach an ICA officer." and a contact route marked "(made-up route, not a real number)".
- The result screen has a fixed link, **"Will my application be approved?"**. It shows the refusal from `skill-file.md`: only an officer decides, and the check can only show what is usually required. The other hard refusal ("fix my document") can't come up, because the prototype has no free-text input. That is a known limit.

## 8. Stale rules and the dry run

**Stale rules.** Each rule has a made-up "as of" date. The freshness window is 30 days (made up). **Simulate stale rules** pushes the date past the window. The check then hides and shows only: "This check is unavailable right now. Please use the standard guidance (made-up link)." This is the fallback in `ai-ux-flow.md`: silence is safer than a confident wrong answer.

**Dry run, built.** `dry-run.html` runs 200 made-up cases from `sample-returns.csv` through the checklist rules and shows the catch rate against the 40% and 50% lines. `make-sample-returns.py` writes both from one set of made-up numbers. The first result, 50.5%, is in `day2-validate/build-log.md`.

The feasibility test runs first as a spreadsheet (section 1), because that is cheapest. Once the full flow is built, **Run dry run** puts the same 200 made-up cases through the rule function the parent sees and prints the catch rate. This only confirms the built rules match the spreadsheet. It adds no new evidence about real returns.

- Each made-up case holds the four answers, the document types ticked (including false ticks, where consent is ticked but invalid) and its assigned return reason.
- **Catch rule:** a case counts as caught only if its return reason appears as a "Still needed" item, or as a hard stop for that reason.
- The always-on consent "Confirm with an officer" line and the photo reminder **do not count**. Otherwise every consent return would score as caught, and the rate would be inflated.
- Known limit, as in `opportunity.md`: the cases are self-authored, so this tests the checklist against our own assumed reason mix, not against real returns.

## 9. Usability check (Day 2)

This uses the Lab 1 result screen only. Five people (colleagues, each given a made-up persona). Read each one the same made-up story: "You are renewing your 8-year-old's passport online. You have uploaded everything and are about to press Submit. This screen appears." Then ask:

1. What would you do next?
2. Has your application been approved or rejected?
3. Would you press Submit anyway? Why?

Record how long each person takes to name the next action, and write down their answers word for word.

- **Pass (our own bar):** at least 4 of 5 name the next action (get the second parent's consent) within 10 seconds, and nobody thinks the check approves or rejects.
- **Fail:** 2 or more can't name the action, or anyone thinks the check decides.

This is an early signal for the fix rate (≥ 85%) and abandon rate (< 15%) targets. Five people can't prove either. A later round can show a "Looks complete: Yes" version, to check nobody reads it as approval.

## 10. Screens

| # | Screen |
|---|---|
| 1 | Review step + start of check + Question 1 |
| 2–4 | Questions 2, 3 and 4 |
| 5 | Checklist |
| 6 | Result (READY CHECK) |
| 7 | Officer route (hard stop) |
| 8 | Stale-rules notice |
| 9 | "You left the check" |

**On every screen:** the banner "Prototype, synthetic data only, not a real ICA service"; the footer "ICA officers make all final decisions · This check reads no documents · Rules as of [date] (made up)"; and a **Submit anyway** link. Submit anyway goes to screen 9, which says nothing was submitted. The check never submits for the parent.

**No ICA logo or crest**, no real form codes, phone numbers or URLs.

## 11. The screen built in Lab 1: the result screen

Lab 1 builds screen 6, the result, not screen 1. The questions carry no risk: anyone can answer "renewal or first passport?". The risk is whether a parent understands the result and acts on it, so that is the screen worth building and testing first.

It is hard-coded to one made-up case, check 2 in section 12: a renewal where the second parent has not given consent.

- Inside the made-up "Review your application (made up)" frame.
- The parent's answers echoed at the top, each with a Change link (not working yet).
- The READY CHECK result from section 7: child renewal · Not yet · Still needed (1: second-parent consent, with "Do this") · Confirm with an officer (0) · Looks present (2).
- A date on each item, and the photo reminder line.
- A main button back to the application, the Submit anyway link, and the "Will my application be approved?" link with its refusal.
- The standard banner and footer.

**In a real application,** question 1 would already be answered by the form ("Renewal, from your application. Change"), so the real flow would start at question 2. The prototype will still ask it later, because it has no real form behind it.

### Two versions for the five-person test

- **`index.html` (full):** everything in the READY CHECK format on screen.
- **`index-lean.html` (lean):** only what is load-bearing on screen: the one thing to fix, the action, the main button, one line saying an officer decides, and Submit anyway. Everything else (what is already present, the answers, the photo reminder, the rule date, "reads no documents") sits one tap away under "What we checked".

**Load-bearing test:** an element stays on screen only if removing it would stop the parent knowing what to do next, or let them misread the result in a way that hurts them.

**How to use them in the test:** show the full version to some people and the lean version to the others. Time how long each takes to name the next action, and record whether anyone reads either one as approval. If the lean version is as clear or clearer, the lean version becomes the design.

The READY CHECK text format in section 7 stays as the agent's output contract (`skill-file.md`). The screen is free to present it with progressive disclosure.

### Walkthrough for presenting

`demo.html` is a guided walkthrough for showing the idea to an instructor or stakeholders. It is not the test. On each step, a spotlight dims everything except the one thing to look at, and a guide card points at it and explains it in a sentence or two. At key moments the viewer taps the button themselves (Submit, Return, the answers, Back, Approve). Tapping a different answer explains where that answer would lead.

It follows one made-up child renewal twice, in 23 steps across six chapters:

1. **The problem.** The problem statement and three numbers, each tagged "course brief" or "made up".
2. **Today.** The parent submits, the officer finds missing consent on day 3 and returns it, and the parent resubmits on day 6.
3. **With the check.** The check opens before Submit, the viewer answers the questions, and the result shows one thing to fix.
4. **Fixed first time.** The parent submits complete, the officer confirms the consent and decides, and a timeline compares the two journeys.
5. **Needs a person.** A parent is overseas, so the check stops and hands over to an officer.
6. **What we test.** The hypothesis, the three tests in order, and the limit we accept.

It works offline. The arrow keys step through it, and the chapter buttons jump.

## 12. Done when

Each check has an expected output. `scenarios.md` repeats them as test scripts.

| # | Check | Expected |
|---|---|---|
| 1 | Clean renewal: Renewal / Yes / Yes / No; all ticked | child renewal · Looks complete: Yes, for the items below · Still needed (0) · Confirm with an officer (1: consent) |
| 2 | Missing-consent renewal: as above, consent unticked | Not yet · Still needed (1: consent, with "Do this") · Confirm with an officer (0) |
| 3 | First-time, birth certificate unticked | child first-time · Not yet · Still needed (1: birth certificate) |
| 4 | Lost passport at Q1 | Hard stop after Q1 · needs an officer |
| 5 | Citizen = No or Not sure at Q2 | Hard stop after Q2 |
| 6 | Consent = No or Not sure at Q3 | Hard stop after Q3 |
| 7 | Parent overseas = Yes or Not sure at Q4 | Hard stop after Q4 |
| 8 | "Something else applies to us" on any question | Officer route |
| 9 | Simulate stale rules | Check hidden; standard-guidance notice only |
| 10 | Change Q1 on the checklist screen | Checklist switches to the other situation |
| 11 | Submit anyway from every screen | "You left the check"; nothing submitted |
| 12 | Every screen | Banner, footer and Submit anyway present |
| 13 | Every result | Under 300 words; never claims or predicts approval: no "you are ready", "will be approved", "will pass" or "guaranteed" |
| 14 | Whole file | No text inputs; opens offline by double-click; no network requests |

## 13. Build order

1. **Lab 1 (now):** the result screen only (screen 6), in `index.html`. Preview it, fix one thing, save on main.
2. **The two cheap tests, before 1 Dec 2026:** the return-reason spreadsheet (feasibility) and the five-person test on the result screen (usability). Write both up in `day2-validate/validation-brief.md`.
3. **Only if both pass:** screens 1–5 and 7–9, `scenarios.md` and `README.md`.
4. **Then:** the in-file dry run, to confirm the built rules give the same catch rate as the spreadsheet.

If either cheap test fails, stop before step 3 and go back to the opportunity.

Every save goes on main through a pull request (CLAUDE.md rule 7).

## 14. Known limits

- The dry run tests our own assumed reason mix, not real returns.
- Inconsistent consent answers (the risk-based row in `ai-ux-flow.md`) can't be modelled with tick boxes. In the prototype, any "no" or "not sure" on consent or overseas is a hard stop instead.
- A name that differs across documents is caught only if the parent chooses "Something else applies to us".
