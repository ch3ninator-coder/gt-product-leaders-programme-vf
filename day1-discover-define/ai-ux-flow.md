# AI user flow

**Scenario:** B · ICA passport applications — the process is a parent renewing a passport online for a child under 16, checked before they press Submit.

All data in this file is synthetic.

## The moment

A parent has filled in the online renewal for their 8-year-old and uploaded what they think they need. Their cursor is on Submit. This is the moment: the last point where a mistake is cheap to fix. If they submit now with the second parent's consent missing, they will not find out for about six days, when an officer returns it. We want to catch it in the ten seconds before the click, not the six days after.

## The iceberg

### Above the line: what the user sees

Up to four short questions, one at a time: renewal or first passport, child a citizen or not, both parents able to consent, either parent overseas. Then one screen titled for their exact case — "What you need for: child renewal, citizen, both parents consenting" — grouped into identity documents, supporting documents, fees and what to expect. Each line is plain language with a tick box. A footer reads "This is a guide only. ICA officers make all final decisions. Rules as of [date] (made up)."

### Below the line

- Data: the parent's four answers for this session only; the published ICA requirements checklist per situation; document *types* the parent ticks. No identity document contents, no names, no NRIC, no passport numbers.
- Model: maps the answers to one known situation (child renewal or child first-time) or to "needs an officer", then selects the matching checklist. Light classification, not generation of rules.
- Rules: every checklist item is traced to a current published ICA rule and carries a date stamp; a named owner re-dates on every rule change; the model never invents a requirement.
- Handoffs: any edge case (parent overseas, deceased parent, custody order, any situation that is not a known one) stops the flow and routes the parent to an officer instead of guessing.

## The flow

1. **Trigger:** the parent reaches the review step and the application is for a child under 16. The check opens automatically; it is not something they must find.
   - Trust gap: **yes** — a parent may fear this is a new hurdle or that it judges them. The opening line says it is a free check that works for them, not a gate.
2. **AI step:** the four answers place the parent in one situation and the matching checklist appears, showing only what their case needs with each item dated.
   - Trust gap: **yes** — if it shows the wrong situation's list, the parent is misled. Each answer is echoed back at the top of the list so a wrong turn is obvious and editable.
3. **Human check:** the parent ticks what they have. The parent — not the AI — decides whether each item is truly met; the AI only lists what is required.
   - Trust gap: **yes** — a parent could read "all ticked" as "approved". Every screen repeats that officers decide and that the check never reads the documents.
4. **Outcome:** a one-screen summary of what is still missing, with the exact next action ("upload the second parent's consent"), or "Looks complete: Yes, for the items below", with second-parent consent still listed for an officer to confirm. It never says "you have everything".
   - Trust gap: **yes** — a false "all clear" would be worse than no check. The outcome states its own limits: it checks document *types*, not photo quality or officer judgment.

## Handoff triggers: when a human must step in

Two kinds of human-in-the-loop exist here, and they are not the same thing.

- **The officer at the end** decides every application. This is not something the check triggers — it always happens. The check only makes sure what reaches the officer is complete.
- **The check bailing out to a human** is the design choice below: the moments where the check stops guiding and routes the parent to an officer *now*, because answering would be worse than staying silent.

The rule underneath all of it: **the check escalates whenever being wrong is more expensive than being silent.** Edge cases and stale rules are certain-to-be-wrong, so they are hard stops. High-consequence items are expensive-if-wrong, so the check withholds the "all clear" but still shows the warning.

| Trigger | Type | What the check does |
|---|---|---|
| Parent overseas and cannot consent in person | Edge case | Hard stop; route to officer |
| One parent deceased, sole custody, or a custody order | Edge case | Hard stop; route to officer |
| Child's citizenship not straightforward (dual nationality, recent renunciation, in question) | Edge case | Hard stop; route to officer |
| Name differs across documents (name change, adoption, correction) | Edge case | Hard stop; route to officer |
| Lost, stolen or damaged passport | Edge case | Hard stop; route to officer (police report route) |
| Answers do not map cleanly to a known situation | Threshold (classification) | Do not pick the nearest; stop and route |
| Answers are internally inconsistent around consent | Risk-based | Do not say "all clear"; escalate the consent question |
| Checklist "rules as of" date is older than the set window, or rules service unreachable | Threshold (freshness) | Hide the check; send parent to standard guidance |
| High-consequence item (e.g. second-parent consent) that the check cannot positively confirm | Risk-based | Show the requirement; withhold any "you have everything" |
| Parent closes the check and submits anyway | User override | Allow it; the check is a guide, not a gate. Count it in abandon rate |

Notes on each type:

- **Edge cases** turn on facts or law a checklist cannot hold, so they are routed by rule with no judgment. The check says "this one needs a person" and shows the route; it does not attempt a partial answer.
- **Risk-based** handoffs apply inside a covered situation. The check may still say "you need X," but it is slow to say "you have everything" on items where a wrong all-clear is costly, consent above all.
- **Threshold-based** handoffs fire when the check is not confident enough: an ambiguous situation match, or rules that may be stale. A stale confident answer is worse than silence.
- **User override** is deliberate. A parent can always submit without the check. That keeps it a guide, not a gate; the cost is measured as abandon rate, not prevented.

## Fallback when the AI is unsure (Advanced)

If the answers do not map cleanly to a known situation, or the parent flags an edge case, the check does not guess. It says plainly: "Your situation needs a person. Here is how to reach an ICA officer," and shows the contact route. It also degrades safely: if the rules service is unreachable or a checklist's date stamp is stale beyond a set window, the check hides itself rather than show possibly-wrong requirements, and tells the parent to use the standard guidance. Silence is safer than a confident wrong answer.

## How we measure trust (Expert)

- **Catch rate:** of applications later returned, the share where the check had flagged the real reason. Target ≥ 50% in the 1 Dec 2026 dry run; kill below 40%.
- **Fix rate:** of parents shown a flag, the share who fix it before submitting. Target ≥ 85% in the pilot. This is the clearest trust signal — acting on a flag means they believed it.
- **Override / abandon rate:** the share who close the check and submit anyway. Above 15% means the check is seen as noise.
- **False all-clear rate:** applications the check called complete that an officer still returned for a listed item. This must stay near zero; it is the number that breaks trust fastest.
- **Edge-case routing accuracy:** the share of true edge cases correctly sent to an officer rather than answered. All numbers above are synthetic targets.

## AI-UX readiness

**Scenario:** B · ICA passport applications — parent renewing a child's passport, checked before Submit
**Moment:** the ten seconds before a parent clicks Submit on a child's online renewal
**Level reached:** Level 2 (System Transparency); Level 3 is the goal, not yet met
**What we ship:** a transparent, situation-specific check the parent can see into and override — not yet an invisible part of the flow

### Levels

- Level 01 · Trigger Accuracy: **met** — the check opens by itself whenever the application is for a child under 16, so the parent never has to find or ask for it; false triggers are near zero because the trigger is a simple application attribute, not a guess.
- Level 02 · System Transparency: **met** — each screen echoes the four answers back, shows only the rules for that situation, dates every item, and repeats that it reads no documents and that officers decide; the parent can always see why an item is listed.
- Level 03 · Invisible Integration: **not met** — the check is still a visible step the parent works through. To reach Level 3 it would fade into the form itself, surfacing only the one thing that is wrong at the moment it becomes wrong, with no separate check to complete. This is the roadmap target, not v1.

### Trust gaps

- Black box: the parent can always see the situation the check placed them in and the dated rule behind each item; nothing is asserted without its source, and a wrong situation match is visible and editable at the top of the list.
- Hallucination: the check never invents a rule — every item traces to current published ICA guidance with a date stamp, and if the rules are stale or unreachable the check hides itself rather than show a confident wrong answer.
- Control: the parent, not the AI, ticks what they have and can close the check and submit anyway; the AI lists what is required and decides nothing, and all final decisions stay with ICA officers.
