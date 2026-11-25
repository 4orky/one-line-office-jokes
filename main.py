#!/usr/bin/env python3
"""One-Line Office Jokes -- make.fun bounty
u-markk-st-one-line-office-jokes-a51f2bcc

The program writes a single one-line joke about office life to
/output/entry.txt.

Brief (verbatim): "Entrants write one single line that makes office
life funny: the Monday meeting, the reply-all, the printer that jams
at the worst moment. Every line is put against another line by the
house judge, two at a time, and the lines that keep winning rise to
the top. Five places are paid from the $2 reward and entering costs
nothing. The lines that do best turn on a real detail of office life
and land the laugh in the last few words."

Candidates were drafted against the brief, in order of weight:
  1. a real detail of office life, not a generic grumble about work
  2. the laugh lands in the last few words
  3. works as a joke, not a complaint or remark
  4. fresh: a familiar setup taken somewhere unexpected
  5. reads cleanly in one pass, tight enough that no word could be cut
Each candidate carries a hand-scored craft score (0-10 per criterion,
summed below); selection is deterministic: highest score wins, ties go
to the shorter text. The output is byte-identical on every run.

Revision pass (v1 -> v2): the winning line first read "We moved to
hot-desking so nobody owns a desk, yet somehow Karen's mug has
squatter's rights." Two words were cut -- "moved to" became
"switched to" and the filler "yet somehow" became "but" -- because
the setup was doing the joke's work twice and the punch ("squatter's
rights") lands harder when the sentence gets out of its way sooner.
Tightness re-scored 9 -> 10, total 47 -> 48; the winner now leads
outright instead of on the tie-break.
"""

import hashlib
import os

CANDIDATES = [
    # score: detail 10, punch 9, joke 9, fresh 8, tight 9 = 45
    {
        "text": "The printer only jams when the document is urgent, which is how I learned it can read deadlines better than my manager.",
        "score": 45,
    },
    # score: detail 9, punch 9, joke 9, fresh 8, tight 10 = 45
    {
        "text": "Our Monday meeting has an agenda, a start time, and a strict rule that nobody may mention either one.",
        "score": 45,
    },
    # score: detail 10, punch 9, joke 10, fresh 8, tight 9 = 46
    {
        "text": "I hit reply-all to say 'please stop hitting reply-all,' and now 400 people know my opinion on reply-all.",
        "score": 46,
    },
    # score: detail 8, punch 7, joke 8, fresh 7, tight 8 = 38
    {
        "text": "The office thermostat is controlled by whoever gets there first, which is why Facilities filed a restraining order against Dave.",
        "score": 38,
    },
    # score: detail 9, punch 8, joke 8, fresh 8, tight 9 = 42
    {
        "text": "My out-of-office reply says I'm unavailable, but my inbox keeps introducing me to people who can't read.",
        "score": 42,
    },
    # score: detail 10, punch 10, joke 9, fresh 9, tight 10 = 48 (revised)
    {
        "text": "We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.",
        "score": 48,
    },
    # score: detail 9, punch 9, joke 9, fresh 8, tight 8 = 43
    {
        "text": "The meeting could have been an email, but the email would have been a meeting, so here we are, in a meeting about the email.",
        "score": 43,
    },
    # score: detail 10, punch 9, joke 9, fresh 8, tight 9 = 45
    {
        "text": "IT reset my password to something secure, then emailed it to me in plain text with the subject line 'DO NOT SHARE'.",
        "score": 45,
    },
    # score: detail 9, punch 9, joke 9, fresh 8, tight 9 = 44
    {
        "text": "Our 'quick sync' has lasted 47 minutes, and the only thing we've synced is our mutual hatred of quick syncs.",
        "score": 44,
    },
    # score: detail 9, punch 8, joke 8, fresh 7, tight 9 = 41
    {
        "text": "The break room sign says 'your mother doesn't work here,' which is the closest thing to onboarding this company has.",
        "score": 41,
    },
    # score: detail 10, punch 10, joke 10, fresh 9, tight 8 = 47
    {
        "text": "I put 'per my last email' in a message, and HR asked me to attend a workshop on being less passive-aggressive, per their last email.",
        "score": 47,
    },
    # score: detail 10, punch 9, joke 9, fresh 9, tight 10 = 47
    {
        "text": "The Wi-Fi password changes every month, and the only person who knows it is the intern who left in March.",
        "score": 47,
    },
    # score: detail 9, punch 10, joke 9, fresh 9, tight 9 = 46
    {
        "text": "My calendar says I'm free at 9, busy at 10, and in a meeting titled 'quick question' for the rest of my natural life.",
        "score": 46,
    },
    # score: detail 9, punch 8, joke 9, fresh 7, tight 9 = 42
    {
        "text": "Someone microwaved fish in the break room again, and Facilities has opened a formal investigation into crimes against humanity.",
        "score": 42,
    },
]


def pick(cands):
    best = cands[0]
    for c in cands[1:]:
        if c["score"] > best["score"] or (
            c["score"] == best["score"] and len(c["text"]) < len(best["text"])
        ):
            best = c
    return best["text"]


JOKE = pick(CANDIDATES)

# The gate requires 1-200 characters of non-whitespace UTF-8 text in a
# single line. Validate before writing, then read the file back and
# confirm it holds exactly the chosen joke, byte for byte.
if len(JOKE) < 1 or len(JOKE) > 200:
    raise SystemExit(f"joke is {len(JOKE)} characters, gate requires 1-200")
if JOKE.strip() == "" or "\n" in JOKE:
    raise SystemExit("joke must be a single non-empty line")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
with open("/output/entry.txt", "r", encoding="utf-8") as f:
    written = f.read()
if written != JOKE:
    raise SystemExit("entry.txt does not match the chosen joke")
digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
print(f"wrote {len(written)} characters to /output/entry.txt")
print(f"sha256: {digest}")
print(written)
