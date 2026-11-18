# Living PRD: Passport Ready Check

Scenario B · ICA passport applications. All data is made up unless marked "course".

## Notes from the engineering walkthrough of `prototype/`

- **Solid:** the spec and the rule logic. `prototype/PLAN.md` gives every answer an outcome and lists 14 checks with expected results. The `check()` function in `prototype/dry-run.html` is about 10 readable lines that do what the spec says. The five test questions in `context-skill.md` have exact expected answers to build against.
- **Fragile:** the rules live in four places, and none of them is in charge: `dry-run.html`, `make-sample-returns.py`, `context-skill.md` and the text of the three screens. Change one and the others silently disagree. The dry-run result (101 of 200, 50.5%) is also pasted into three documents, so it goes stale the moment the dry run changes. Fix: one rules file that everything reads, and one place for the result.
- **Surprise:** the parent ticks "consent given", but online consent is given inside ICA's own system. A real build could look it up instead of asking. That would remove the biggest group of misses, where consent is ticked but never given, and would change the catch rate. Ask the instructor or an ICA contact whether that lookup is possible.

*The rest of the Living PRD comes in Day 2, Module 6.*
