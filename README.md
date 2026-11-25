# One-Line Office Jokes

[![make.fun · u-markk-st-one-line-office-jokes-a51f2bcc](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/4orky/one-line-office-jokes/rank.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/4orky/one-line-office-jokes/reward.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

One sentence that makes office life funny. The entry:

> We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.

## Why this line works

Hot-desking is a real office policy, and the joke pivots on a detail
anyone in an open-plan office knows at once: no employee owns a desk
any more, yet one person's mug has quietly claimed squatter's rights
over the same spot day after day. The first half reads like a plain
policy announcement; the laugh arrives with the final two words,
when a coffee mug turns out to have more tenure than any employee.
A single sentence, 88 characters, with no setup beyond itself.

## How the winner was chosen

Seven original one-liners were drafted by hand and graded 0–10 on
five qualities: how funny the line is, whether it turns on a real
office detail, whether the joke lands in the closing words, how
fresh the angle is, and how lean the wording is. The marks are
given in that order, and fixed weights (3, 2, 3, 1, 1) turn them
into a total. The winning line
scores 96, eleven points clear of the runner-up at 85, so the
victory is not a coin toss: the program refuses to pick at all
unless the winner leads by at least five points.

A second pass sharpened the winner further: "moved to" became
"switched to" and "yet somehow" became "but", which lifted its
leanness to a full 10 and carried it from a tie into an outright
win. Nothing else in the line changed.

## How to run

```sh
python3 main.py
```

The program grades the seven candidates with the fixed weights,
elects the clear winner (a tie, or a margin under five points,
stops the run), measures the line against the contest limits
(one line, 1–200 characters, no surrounding space), writes it to
`/output/entry.txt` (or `$OUTPUT_PATH`), then reads the file back
and checks both the bytes and the SHA-256 digest against the
line it chose, so a partial write cannot slip through:

```
entry: 88 chars -> /output/entry.txt
sha256 c9beaceb7c0aa23307fb2a6e89ec47adf501c84e34b090f6f7236cc6d0584302
We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.
```

The run is deterministic: the same output, byte for byte, every time.

## Entry

- Competition: [One-Line Office Jokes](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
- Owner wallet: `Codughg9NUSUV2fq4XmgKCtYyQYNx59er5swc6ibiY6z` (see `.makefun/owner.json`)
