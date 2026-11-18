"""Make 200 made-up returned child passport applications for the dry run.

Every row is synthetic. Nothing here is real ICA data.

Writes sample-returns.csv and puts the same rows into dry-run.html, so the
spreadsheet and the page always match. Run it again after changing a number
below:

    python3 make-sample-returns.py
"""
import csv
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Made-up numbers. Each matches day1-discover-define/opportunity.md.
TOTAL = 200
SITUATION_SPLIT = {"renewal": 140, "first": 60}  # made up
# Return reasons per situation: consent 34%, wrong or missing document 22%,
# photo 28%, other 16% (made up). Counts add up to the split above.
REASONS = {
    "renewal": {"consent": 48, "document": 31, "photo": 39, "other": 22},
    "first": {"consent": 20, "document": 13, "photo": 17, "other": 10},
}
# Parents who tick a document they don't really have, for example consent the
# other parent never completed. Made up, with no evidence: about 10%.
FALSE_TICKS = {
    "renewal": {"consent": 5, "document": 3},
    "first": {"consent": 2, "document": 1},
}

DOCS = {
    "renewal": ["current_passport", "photo", "consent"],
    "first": ["birth_certificate", "parent_id", "photo", "consent"],
}
ALL_DOCS = ["current_passport", "birth_certificate", "parent_id", "photo", "consent"]
OTHER_NOTES = ["a form detail was wrong", "the fee was not paid", "an address did not match"]


def build():
    rows = []
    for sit, reasons in REASONS.items():
        doc_flip = 0
        other_flip = 0
        for reason, count in reasons.items():
            false_ticks = FALSE_TICKS[sit].get(reason, 0)
            for i in range(count):
                ticked = {d: ("yes" if d in DOCS[sit] else "n/a") for d in ALL_DOCS}
                false_tick = i < false_ticks
                if reason == "consent":
                    item = "consent"
                    note = "consent ticked but never given" if false_tick else "consent not given"
                elif reason == "document":
                    if sit == "renewal":
                        item = "current_passport"
                    else:
                        item = ["birth_certificate", "parent_id"][doc_flip % 2]
                        doc_flip += 1
                    note = "document ticked but the wrong one uploaded" if false_tick else "document missing"
                elif reason == "photo":
                    item = "photo"
                    note = "photo uploaded but did not meet the rules"
                else:
                    item = "other"
                    note = OTHER_NOTES[other_flip % len(OTHER_NOTES)]
                    other_flip += 1
                if reason in ("consent", "document") and not false_tick:
                    ticked[item] = "no"
                rows.append({
                    "situation": sit,
                    "citizen": "yes",
                    "both_can_consent": "yes",
                    "parent_overseas": "no",
                    **{f"ticked_{d}": ticked[d] for d in ALL_DOCS},
                    "return_reason": reason,
                    "return_item": item,
                    "note": note,
                })
    assert len(rows) == TOTAL, len(rows)
    random.Random(417).shuffle(rows)
    for n, r in enumerate(rows, 1):
        r["case_id"] = f"R-{n:03d}"
        r["data"] = "made up"
    return rows


def main():
    rows = build()
    cols = ["case_id", "situation", "citizen", "both_can_consent", "parent_overseas",
            *[f"ticked_{d}" for d in ALL_DOCS], "return_reason", "return_item", "note", "data"]
    with open(HERE / "sample-returns.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    page = HERE / "dry-run.html"
    html = page.read_text()
    blob = json.dumps([{k: r[k] for k in cols} for r in rows], separators=(",", ":"))
    html, n = re.subn(r"/\*DATA\*/.*?/\*END\*/", lambda m: "/*DATA*/" + blob + "/*END*/", html, flags=re.S)
    assert n == 1, "dry-run.html is missing its /*DATA*/ ... /*END*/ markers"
    page.write_text(html)
    print(f"wrote {len(rows)} made-up cases to sample-returns.csv and dry-run.html")


if __name__ == "__main__":
    main()
