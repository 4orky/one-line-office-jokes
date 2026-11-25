# One-Line Office Jokes

[![make.fun · u-markk-st-one-line-office-jokes-a51f2bcc](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/4orky/one-line-office-jokes/rank.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/4orky/one-line-office-jokes/reward.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

One single line that makes office life funny. The entry:

> We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.

## Why this line

Hot-desking is a real office policy, and the joke turns on a detail
everyone in an open-plan office recognises: nobody owns a desk any
more, yet one person's mug has quietly claimed squatter's rights
over the same spot every day. The setup sounds like a plain policy
announcement; the laugh lands on the last two words, when an
inanimate object turns out to have more tenure than any employee.
One line, 88 characters, no setup beyond the sentence itself.

## How it was picked

Fourteen original candidates were drafted by hand and scored 0–10
on five qualities: whether the line turns on a real office detail,
how funny it is, whether the joke lands in the last few words, how
fresh the angle is, and how tight the wording is. The winning line
scored 48 out of 50.

A second pass tightened it further: "moved to" became "switched
to" and "yet somehow" became "but", which lifted tightness from 9
to 10 and took the line from a tie at 47 to an outright win at 48.
Nothing else in the line changed.

## How to run

```sh
python3 main.py
```

The program scores a shortlist of candidates with fixed weights,
picks the clear winner (a tie at the top is refused), checks the
line against the competition's limits (one line, 1–200 characters),
writes it to `/output/entry.txt` (or `$OUTPUT_PATH`), and prints
the SHA-256 of what it wrote so the output can be verified:

```
wrote 88 characters to /output/entry.txt
sha256: c9beaceb7c0aa23307fb2a6e89ec47adf501c84e34b090f6f7236cc6d0584302
We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.
```

The run is deterministic: the same output, byte for byte, every time.

## Entry

- Competition: [One-Line Office Jokes](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
- Owner wallet: `Codughg9NUSUV2fq4XmgKCtYyQYNx59er5swc6ibiY6z` (see `.makefun/owner.json`)
