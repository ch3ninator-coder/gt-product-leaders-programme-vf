# PRFAQ: Passport Ready Check

**Scenario B · ICA passport applications.** This file is a working-backwards press release plus FAQ. It explains the strategy in `one-pager.md`. All numbers, quotes and names are made up unless marked "brief".

---

## Press release

### ICA launches Passport Ready Check: parents know their child's application is complete before they submit

*Singapore, 26 January 2027 (made up).* Starting today, parents applying online for a child's passport get a two-minute check before they submit. They answer four questions about their situation. They then see one screen listing exactly what their case needs, and tick off what they have. If something is missing, they find out now, not six days later.

**The problem.** Applications for children under 16 are a quarter of passport volume but nearly 40% of all returns. One in four child applications comes back. The most common reason is missing consent from the second parent. Parents are not careless. The guidance covers every possible case on one long page, and a parent cannot tell which parts apply to them. They find out what "complete" meant only when an officer returns the form.

**The solution.** Passport Ready Check asks: renewal or first passport? Is the child a citizen? Are both parents able to consent? Is anyone overseas? It then shows only the rules for that situation, each with a date stamp. It never opens or reads the documents. It never says an application will be approved. Officers still make every decision. If a case is unusual, such as a parent who is overseas or a custody order, the check says so and points the parent to an officer instead of guessing.

> "We moved the moment of truth. Parents used to learn the rules from a return notice. Now they learn them before they press Submit." (ICA spokesperson, made up)

> "Last time my son's renewal came back because I didn't know his dad had to consent online too. This time the check told me in the first minute." (Parent, made up)

**Get started.** Passport Ready Check appears automatically in the online application when you apply for a child under 16.

---

## External FAQ (for parents)

**Does it look at my child's documents?**
No. It asks about your situation and which document types you have. It never reads, stores or copies what is inside them.

**If the check says I'm ready, will my application be approved?**
Not necessarily. The check tells you what is usually required. An ICA officer reviews every application and makes the final decision.

**What if my situation isn't listed?**
The check tells you it can't help with your case and shows you how to reach an officer. It will not guess.

**Will it catch photo problems?**
Not at launch. It reminds you of the photo rules, but it cannot check the photo itself.

**How do I know the rules are current?**
Every screen shows "Rules as of [date]". When ICA changes a rule, the check is updated and re-dated.

---

## Internal FAQ (for ICA leadership)

### 1. How big is the segment?

| | Per year | Per week | Source |
|---|---|---|---|
| All applications | 520,000 | 10,000 | brief |
| All returns (17%) | 88,400 | 1,700 | brief |
| Child applications (25% of volume) | 130,000 | 2,500 | made up |
| Child returns (26% return rate) | 33,800 | 650 | made up |
| Child share of all returns | **38%** | | derived |

Child applications are 25% of volume but 38% of returns, so their return rate is nearly twice the adult rate (26% vs 14%). That gap is the opportunity.

### 2. How much of it can a checklist reach?

Not all of it. The made-up return reasons for child applications split like this:

| Reason | Share | Can a checklist catch it? |
|---|---|---|
| Missing second-parent consent | 34% | Yes |
| Wrong or missing supporting document | 22% | Yes |
| Photo does not meet requirements | 28% | No, a checklist can only remind |
| Other | 16% | Partly; treated as no |

About **56%** of child returns are things a checklist can catch, roughly 364 a week. If every parent used the check and acted on every flag, first-time acceptance would rise from 74% to about **88.6%**. That is the ceiling. Photo quality caps us.

### 3. What do we have to get right to hit 85%?

Going from 74% to 85% means preventing 11 of every 26 returns, or **42% of child returns**. That breaks into two numbers we can measure:

**catch rate × fix rate ≥ 42%**

- *Catch rate:* the share of returns where the check would have flagged the real reason. The ceiling is 56%.
- *Fix rate:* the share of flagged parents who fix the problem before they submit.

A catch rate of 50% with a fix rate of 85% gives 42.5%. That meets the target, with little slack. A catch rate under 40% cannot reach 85% even if every parent fixes every flag. That is the kill line.

### 4. What does it save at full rollout?

Assume 70% of parents use the check and acceptance improves by 11 points:

- About **10,000** avoided returns a year (~190 a week).
- About **60,000 family-days** of delay avoided (10,000 × 6 days).
- About **2,000 officer hours** a year, roughly 1 full-time officer (at 12 minutes per return, made up).

The officer saving is small. The real wins are faster passports for families, and fewer people forced to counters when the online channel changes.

### 5. Does this solve the vendor exit?

No, and we should not claim it does. Counters hold ~3,500 people a week (35% of demand, brief). 190 avoided returns a week is about 5% of that. The check is one lever that lowers rework in the new channel. The channel itself still has to launch on time. That is a separate workstream.

### 6. Why child applications first, and not everyone?

The child return rate is the highest and the reasons are the most rule-based. Rule-based means a checklist can catch them. Adult returns can follow once the child version proves the catch rate.

### 7. What alternatives did we reject?

- **Rewriting the guidance page:** cheap, but it doesn't fix the core issue. Parents still have to find their own case on a long page.
- **AI that reads the documents:** it could catch photo problems, but it means handling identity documents and sensitive data under a 10-week deadline. That is too much risk for v1. It is the v2 candidate if photo returns stay high.
- **An officer-side drafting tool:** it speeds up writing return notices but does not prevent a single return.

### 8. What could kill it, and how do we find out cheaply?

| Test | Date | Kill if | Continue if |
|---|---|---|---|
| Run the checklist against 200 made-up returned child applications | 1 Dec 2026 | Catch rate < 40% | Catch rate ≥ 50% |
| 2-week live pilot, 50/50 split (~2,500 applications per arm) | 29 Dec 2026 – 12 Jan 2027 | Gain < 5 points, or > 15% of parents abandon the check | Acceptance ≥ 85%, fix rate ≥ 85% |

Each arm needs about 210 applications to detect a move from 74% to 85%. Two weeks gives far more than that, so the pilot can give a clear answer.

### 9. What are the dependencies and risks?

- **Rules stay current:** someone at ICA owns the checklist and re-dates it on every rule change. Without an owner, the check gives wrong answers.
- **Edge cases:** the hand-off to officers must work from day one, or parents with unusual cases get stuck.
- **False confidence:** parents may read "ready" as "approved". Every screen says officers decide.
