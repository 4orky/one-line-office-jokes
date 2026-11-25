#!/usr/bin/env python3
# One-line office joke entry.
#
# Seven hand-written candidates are graded on five qualities and the
# clear winner is written out. The grading is fixed arithmetic, so
# the same candidates always elect the same line, and the elected
# line is measured against the contest limits before anything is
# written to disk. A tied race at the top is refused: the winner
# has to beat the runner-up outright, never on list order.
#
# Qualities, in the order the marks below are given:
#   laugh     -- the line is actually funny
#   concrete  -- it turns on a specific, recognisable office detail
#   landing   -- the laugh arrives in the closing words
#   novel     -- the angle is not one heard a hundred times
#   lean      -- no word is dead weight
#
# Nothing here touches the network, rolls dice, or reads any input
# beyond this file. The output path defaults to /output/entry.txt
# and can be pointed elsewhere with OUTPUT_PATH.

import hashlib
import os
import sys

CRITERIA = ("laugh", "concrete", "landing", "novel", "lean")
WEIGHTS = (3, 2, 3, 1, 1)
LIMIT = 200

# Candidates: (line, marks in CRITERIA order). All seven lines were
# drafted by hand for this entry.
CANDIDATES = (
    ("We switched to hot-desking so nobody owns a desk, but Karen's mug has squatter's rights.", (10, 10, 9, 9, 10)),
    ("Reply-all is how I learned that forty people can say 'please remove me' and nobody can.", (8, 9, 9, 8, 8)),
    ("The quick sync lasted forty-seven minutes, which is office for 'see you next quarter'.", (8, 9, 8, 8, 9)),
    ("The printer only jams when the document is urgent, which is why I now email everything to myself twice.", (8, 9, 8, 8, 8)),
    ("Our Monday meeting has an agenda, a timer, and a strict rule against mentioning the agenda.", (8, 9, 8, 7, 9)),
    ("I set my out-of-office to 'on holiday' and my inbox set itself to 'on fire'.", (8, 8, 8, 8, 8)),
    ("The thermostat has a password now, and Dave from facilities is the only one who knows it.", (7, 8, 7, 7, 8)),
)


def weighted_total(marks):
    """Add up one candidate's marks under the fixed weights."""
    total = 0
    for weight, mark in zip(WEIGHTS, marks):
        total += weight * mark
    return total


def pick_winner(candidates):
    """Elect the highest-scoring candidate.

    Scores are sorted highest first. A tie at the top aborts the
    run, so the pick never silently depends on list order."""
    scored = sorted(
        ((weighted_total(marks), text) for text, marks in candidates),
        key=lambda pair: pair[0],
        reverse=True,
    )
    top, second = scored[0], scored[1]
    if top[0] == second[0]:
        sys.exit("no clear winner: top two tied at %d points" % top[0])
    if top[0] - second[0] < 5:
        sys.exit(
            "winner's margin is too thin: %d over %d, need at least 5"
            % (top[0], second[0])
        )
    return top[1]


def check_entry(text):
    """Measure the elected line against the contest limits.

    Returns an empty string when the line is acceptable, otherwise
    a short description of the first problem found."""
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    if not text:
        return "entry is empty"
    if len(text) > LIMIT:
        return "entry is %d characters, limit is %d" % (len(text), LIMIT)
    if text.strip() != text:
        return "entry has leading or trailing space"
    if len(text.split()) < 5:
        return "entry is too short to be a joke"
    return ""


def write_entry(text):
    """Write the line out and prove the file holds exactly it."""
    dest = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    folder = os.path.dirname(dest)
    if folder:
        os.makedirs(folder, exist_ok=True)
    payload = text.encode("utf-8")
    expected = hashlib.sha256(payload).hexdigest()
    with open(dest, "wb") as handle:
        handle.write(payload)
    with open(dest, "rb") as handle:
        saved = handle.read()
    if saved != payload:
        sys.exit("round-trip check failed: file differs from entry")
    digest = hashlib.sha256(saved).hexdigest()
    if digest != expected:
        sys.exit("digest check failed: written file digest does not match entry")
    print("entry: %d chars -> %s" % (len(text), dest))
    print("sha256 %s" % digest)
    print(text)


def run():
    winner = pick_winner(CANDIDATES)
    problem = check_entry(winner)
    if problem:
        sys.exit("entry rejected: " + problem)
    write_entry(winner)


if __name__ == "__main__":
    run()
