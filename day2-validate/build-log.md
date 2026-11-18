# Build log

Scenario B · ICA passport applications. All data is made up unless marked "course".

## Riskiest assumption

**Most child passport returns are caused by a missing or wrong document type, which a checklist can catch before Submit, and not by photo, form or other problems it can't see.**

If this is wrong, the check is the wrong product however well it's designed. That's why it's tested first. Source: the kill switch in `day1-discover-define/opportunity.md`.

- **Risk type:** Feasibility. Will the logic actually work?
- **Kill switch:** In the dry run, the checklist catches the real return reason in **under 40%** of 200 made-up returned child applications. Below 40%, even a perfect fix rate can't reach the target, so we stop and pivot, for example to a photo check or an officer-side tool.
- **Success signal:** The checklist catches the real return reason in **50% or more** of the 200 cases by **1 Dec 2026**. Between 40% and 50% is a watch band: decide on the five-person test's fix rate.
- **What counts as caught:** the case's real return reason appears under "Still needed" before Submit. The "confirm with an officer" consent line doesn't count, because it appears on every case.

## How the prototype tests it

- **`prototype/dry-run.html`** runs all 200 made-up cases through the same checklist rules as the result screen. It shows the catch rate against the stop and continue lines, why each reason was caught or missed, a filterable list of every case, and two sliders to see how wrong our made-up numbers can be before the idea fails.
- **`prototype/sample-returns.csv`** holds the same 200 made-up cases for checking in a spreadsheet. Every row is marked "made up".
- **`prototype/make-sample-returns.py`** writes both files from one set of made-up numbers, so they always match.

The made-up case mix follows `opportunity.md`: consent 34%, wrong or missing document 22%, photo 28%, other 16%, split 140 renewals and 60 first passports. About 10% of consent and document cases are false ticks, where the parent ticks a document they don't really have.

## Log

### 18 Nov 2026: first dry run

- **Result:** 101 of 200 made-up cases caught, **50.5%**. Just over the continue line.
- **Caught:** 61 of 68 consent cases and 40 of 44 document cases. The misses are false ticks: the parent ticked consent that was never given, or the wrong document was uploaded.
- **Missed:** all 56 photo cases and all 32 other cases, as expected. The check doesn't look at photos and has no form-detail rules.
- **Decision:** continue to the five-person test, but with almost no margin. The sliders show a document share of about 45% already drops the estimate into the watch band.
- **What this does not prove:** we wrote the cases with the reason mix we assumed, so 50.5% mostly confirms our own numbers and that the rules work. The real test is ICA's count of child returns by reason, as totals only.
- **Next:**
  - Ask the instructor how the course wants real return-reason data handled.
  - Run the five-person test on `index-lean.html`.
  - Find out how common false ticks really are, because each one is a return the check misses.
