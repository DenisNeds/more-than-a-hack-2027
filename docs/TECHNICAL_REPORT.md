# <team_name> — Technical report

More than a Hack 2027, Phase 1: frame-level ball possession.

## Approach

What we built, and why this rather than something else.

## Assets used

Which of tactical ATD, broadcast ATD, Smart Tagging, homography and video we used and how — and
which we tried and dropped.

## Training data

Every labelled dataset used, its source, who labelled it and how much. None from the provided game.

## Possession rules implemented

Where we drew the line on loose balls, challenges, deflections and restarts; how dead ball is
detected; how frames without a ball position are handled.

## Results

Public-window scores (for pipeline checking only) and anything else we measured.

## Limitations

Where it fails, and what we would fix with more time.

## Reproduction

```bash
make setup
# unpack the data bundle into data/
make submission TEAM=<team_name>
```
