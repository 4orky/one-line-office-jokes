#!/usr/bin/env python3
"""One-line office joke entry.

The program holds a small shortlist of office jokes, scores each one
on five qualities, and writes the best-scoring line to the output
file. The scoring is deliberately simple and fully deterministic:
the same shortlist always produces the same winner, and the winner
is checked against the competition's own limits before anything is
written. A tie at the top is treated as a fault, not settled by
luck: the shortlist must have one clear winner.

Qualities, most important first:
  * funny      -- does the line actually make someone laugh
  * punch      -- does the laugh land in the last few words
  * detail     -- does it turn on a real, specific office detail
  * fresh      -- is it an angle nobody has heard a hundred times
  * tight      -- is every word earning its place

The output path defaults to /output/entry.txt and can be moved
with the OUTPUT_PATH environment variable. No network, no random
choices, no input besides this file.
"""

from hashlib import sha256
from os import environ
from pathlib import Path

# Weights for the five qualities, in priority order.
WEIGHTS = {"funny": 3, "punch": 3, "detail": 2, "fresh": 1, "tight": 1}

# Shortlist. Each entry carries the line plus one mark (0-10) per
# quality. All lines were written for this entry.
ENTRIES = [
    {
        "line": "We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.",
        "marks": {"funny": 10, "punch": 9, "detail": 10, "fresh": 9, "tight": 10},
    },
    {
        "line": "Reply-all is how I learned that forty people can say 'please remove me' and nobody can.",
        "marks": {"funny": 8, "punch": 9, "detail": 9, "fresh": 8, "tight": 8},
    },
    {
        "line": "The quick sync lasted forty-seven minutes, which is office for 'see you next quarter'.",
        "marks": {"funny": 8, "punch": 8, "detail": 9, "fresh": 8, "tight": 9},
    },
    {
        "line": "The printer only jams when the document is urgent, which is why I now email everything to myself twice.",
        "marks": {"funny": 8, "punch": 8, "detail": 9, "fresh": 8, "tight": 8},
    },
    {
        "line": "Our Monday meeting has an agenda, a timer, and a strict rule against mentioning the agenda.",
        "marks": {"funny": 8, "punch": 8, "detail": 9, "fresh": 7, "tight": 9},
    },
    {
        "line": "I set my out-of-office to 'on holiday' and my inbox set itself to 'on fire'.",
        "marks": {"funny": 8, "punch": 8, "detail": 8, "fresh": 8, "tight": 8},
    },
    {
        "line": "The thermostat has a password now, and Dave from facilities is the only one who knows it.",
        "marks": {"funny": 7, "punch": 7, "detail": 8, "fresh": 7, "tight": 8},
    },
]


def tally(entry):
    """Weighted total for one entry's five marks."""
    return sum(WEIGHTS[name] * value for name, value in entry["marks"].items())


def choose_best(entries):
    """Return the highest-scoring entry.

    The ranking is stable, but a tie at the top is refused outright:
    the winner must beat the runner-up by at least one point, so the
    pick never depends on list order or on luck.
    """
    ranked = sorted(entries, key=tally, reverse=True)
    if len(ranked) > 1 and tally(ranked[0]) == tally(ranked[1]):
        raise SystemExit("self-check failed: tie at the top, no clear winner")
    return ranked[0]


def verify_line(line):
    """Check the chosen line against the competition's limits.

    Returns a list of problems; an empty list means the line is fine.
    """
    problems = []
    if "\n" in line or "\r" in line:
        problems.append("entry is not a single line")
    if not 1 <= len(line) <= 200:
        problems.append("length %d is outside 1..200 characters" % len(line))
    if line != line.strip():
        problems.append("entry has surrounding whitespace")
    return problems


def main():
    best = choose_best(ENTRIES)
    line = best["line"]
    problems = verify_line(line)
    if problems:
        raise SystemExit("self-check failed: " + "; ".join(problems))

    out = Path(environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    digest = sha256(out.read_bytes()).hexdigest()
    print("wrote %d characters to %s" % (len(line), out))
    print("sha256: %s" % digest)
    print(line)


if __name__ == "__main__":
    main()
