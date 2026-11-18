# Living PRD: Passport Ready Check

Scenario B · ICA passport applications. All data is made up unless marked "course".

This PRD describes what the code in `prototype/` actually does today, not what the plan hoped for. Where the two differ, it says so. Update it whenever the prototype changes.

## Notes from the engineering walkthrough of `prototype/`

- **Solid:** the spec and the rule logic. `prototype/PLAN.md` gives every answer an outcome and lists 14 checks with expected results. The `check()` function in `prototype/dry-run.html` is about 10 readable lines that do what the spec says. The five test questions in `context-skill.md` have exact expected answers to build against.
- **Fragile:** the rules live in four places, and none of them is in charge: `dry-run.html`, `make-sample-returns.py`, `context-skill.md` and the text of the three screens. Change one and the others silently disagree. The dry-run result (101 of 200, 50.5%) is also pasted into three documents, so it goes stale the moment the dry run changes. Fix: one rules file that everything reads, and one place for the result.
- **Surprise:** the parent ticks "consent given", but online consent is given inside ICA's own system. A real build could look it up instead of asking. That would remove the biggest group of misses, where consent is ticked but never given, and would change the catch rate. Ask the instructor or an ICA contact whether that lookup is possible.

## 1. Product overview

The Passport Ready Check runs just before a parent submits an online passport application for a child under 16. The parent answers up to four questions about their situation. The check then shows only what that situation needs, what is still missing and the exact next step. It never reads documents, never says an application will be approved, and sends edge cases to an ICA officer.

**What exists today:** a set of static web pages and one small rules engine. There is no backend, no login, no real form and no connection to any ICA system.

## 2. Problem and riskiest assumption

**Problem:** parents only find out their child's application is incomplete when an officer returns it, about 6 days later (course). In the made-up numbers, 26% of child applications come back, and missing second-parent consent is the most common reason.

**Riskiest assumption:** most child returns are caused by a missing or wrong document type, which a checklist can catch, not by photo or form problems it can't see. The kill switch is a catch rate under 40%. The success signal is 50% or more by 1 Dec 2026. Details are in `build-log.md`.

**What the code shows:** `dry-run.html` catches 101 of 200 made-up returns, 50.5%. That result is decided by the inputs, not discovered. The cases assume 56% document problems and about 10% false ticks, and 56% × 90% ≈ 50%. The code proves the rules work as written. It can't test the assumption, because the real return mix isn't in the repo.

## 3. User flow and screen map

| # | Screen | Planned in `PLAN.md` | What the code has |
|---|---|---|---|
| 1 | Review step and question 1 | Yes | Only inside `demo.html`, as a scripted step |
| 2–4 | Questions 2 to 4 | Yes | Only inside `demo.html`, scripted to one path |
| 5 | Checklist with tick boxes | Yes | **Not built anywhere** |
| 6 | Result | Yes | `index.html` (full) and `index-lean.html` (lean), each hard-coded to one case: a renewal missing consent |
| 7 | Officer hand-off | Yes | Only inside `demo.html` (overseas parent) |
| 8 | Stale-rules notice | Yes | **Not built anywhere** |
| 9 | "You left the check" | Yes | **Not built.** "Submit anyway" only shows a note |

**What this means:** no screen is driven by the rules. The result screens are typed by hand and don't call `check()`. The only flow a person can click through is the scripted walkthrough in `demo.html`, which has its own copies of every screen. A real parent journey doesn't exist yet in code.

## 4. Success metrics

| Metric | Target (made up) | Measured by the code today? |
|---|---|---|
| Catch rate | 50% or more; stop below 40% | **Yes**, in `dry-run.html`, on made-up cases only |
| Fix rate (parents who fix a flag before submitting) | 85% or more | No. Needs the five-person test, then the pilot |
| Abandon rate ("Submit anyway") | Under 15% | No. Nothing is logged |
| False all-clear rate | Near 0% | No. Needs real returns to compare against |
| Edge-case routing accuracy | High | No. None of the 200 cases triggers a hard stop (see section 5) |
| Pilot gain over control, whole treatment group | 8 points or more on first-time acceptance | No. Needs a live pilot |

Only one of the six metrics has any code behind it, and that one runs on our own data.

## 5. Technical reality

**Stack:** plain HTML, CSS and JavaScript, plus one Python script. No build step, no dependencies, no network requests. The pages work offline. They load the course fonts from `../../assets/fonts/`, and fall back to system fonts if a page is copied out on its own.

**The rules engine:** `check()` in `dry-run.html` takes one case and returns:

- a hard stop, if the child isn't a citizen, a parent can't consent, a parent is overseas, or the situation is unknown;
- otherwise, the documents still needed (unticked items for that situation) and whether consent goes to an officer.

`caught()` counts a case as caught only if its real return reason appears in "still needed".

**The data:** `make-sample-returns.py` builds 200 made-up cases from fixed counts, shuffles them with a fixed seed (417), writes `sample-returns.csv`, and pastes the same cases into `dry-run.html` between `/*DATA*/` and `/*END*/` markers. That puts all 200 cases on one 68,000-character line.

**Gaps an engineer would find:**

- **Rules are copied in four places**: `NEEDS` in `dry-run.html`, `DOCS` in the script, the rules table in `context-skill.md`, and the screen text. Only the context skill has rule IDs and dates.
- **The hard-stop path is never exercised.** All 200 cases answer "citizen yes, both can consent, no one overseas", so the dry run never tests the edge-case routing in `check()`.
- **The stale-rules switch-off isn't implemented.** No code reads a rule date. Every rule is dated 1 Nov 2026 with a 30-day window, so the check would have to hide itself on 1 Dec, the dry-run deadline.
- **No tests.** The five test questions in `context-skill.md` are written down, not automated.
- **No instrumentation**, so nothing could measure fix rate or abandon rate even in a pilot.
- **The result screens don't use the engine**, so they can drift from the rules without anyone noticing.
- **The script edits `dry-run.html` with a text match.** Hand edits near the markers can be overwritten.
- **`demo.html` is the most polished file but is presentation code.** It duplicates the screens and shouldn't be built on.

## 6. Assumptions and risks

| Assumption or risk | Where it sits in the code | How to check it |
|---|---|---|
| 56% of child returns are document problems | The fixed counts in `make-sample-returns.py` | ICA's real return totals by reason |
| About 10% of parents tick documents they don't have | 11 false-tick cases in the script | Real returns, or an ICA consent lookup |
| Parents answer the four questions truthfully | `check()` trusts every answer | The five-person test; later, compare answers with officer findings |
| Ticking is the only way to know consent was given | The `ticked_consent` field | Ask ICA whether consent can be looked up (the surprise above) |
| The rules are right and current | Hand-typed lists, dated 1 Nov 2026 | A named rules owner and a rules review |
| Parents act on a flag instead of skipping it | Nothing in code yet | The five-person test, then the pilot's abandon rate |

The market, technical and team risks in `one-pager.md` still apply.

## 7. In and out of scope

**In scope for the prototype:**

- child renewals and first passports for Singapore citizen children;
- up to four questions;
- document types only, ticked by the parent;
- hard stops to an officer for edge cases;
- the catch-rate dry run on made-up data.

**Out of scope:**

- reading or checking any document, including photo quality;
- adult applications;
- any real ICA data, rules, system or login;
- approving, rejecting or submitting anything;
- storing anything about the parent;
- fees and processing times.

**Planned but not yet built:** the questions and checklist screens, the stale-rules switch-off, the officer hand-off as a real screen, "You left the check", and any logging.

## 8. Engineering recommendation

**Don't build on this code. Keep three things from it and rebuild the rest.**

**Keep:**

- the `check()` logic and the "what counts as caught" rule;
- the case data shape in `sample-returns.csv`;
- `PLAN.md` and `context-skill.md` as the spec and acceptance tests.

**Do next, in this order:**

1. **One rules file** (for example `rules.json`, using the rule IDs and dates in `context-skill.md`) that the engine, the script and the screens all read. This fixes the biggest fragility.
2. **Automated tests for `check()`**: the five test questions, plus at least one case for each hard stop, since the dry run currently never tests them.
3. **Make the result screen render from `check()`**, so the screen and the dry run can't disagree.
4. **A short spike with ICA on a consent lookup.** If consent can be read from ICA's system, drop the tick box for it and re-run the dry run. This may change the catch rate more than any other fix.
5. **Implement the stale-rules check**, and agree a realistic review window with the rules owner.
6. **Get ICA's real return totals by reason.** Until then, the 50.5% result is a statement about our assumptions, not about the idea.

Steps 1 to 3 are small, a day or two of work. Steps 4 and 6 need people at ICA, not code, and they're the ones that decide whether the idea survives.
