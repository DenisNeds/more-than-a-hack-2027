# Project notes for Claude Code

Hackathon repo (More than a Hack 2027, Phase 1): label every tactical-video frame of one match
`H`/`A`/`D`/`X`. Ranked on `spellF1`, tie-break `macroF1`. Docs: README → CHALLENGE → DATA →
EVALUATION → SUBMISSION → RULES. `evaluation/possession_metrics.py` is the metric spec.

## Hard rule: never read the match data

The terms forbid sending the videos, datasets or any extract of them to a hosted LLM — that
includes you. Do not open, print, sample, `head`, plot-and-view or summarise anything under
`data/` (or `$MTAH_DATA_DIR`), and do not read notebook outputs or logs that echo data rows.
Work from the documented formats in DATA.md and the loader code instead. When code needs
running against the data, ask the human to run it and report only aggregate numbers they choose
to share. `.claude/settings.json` denies the obvious reads; respect the intent beyond them.

The public ground truth `evaluation/gt/BAR-ATH_possession_gt_public.csv` and the committed
`baseline_*.csv` files are in the public repo and are fine to read.

## Other rules that shape code

- Labels must come from an algorithm. No hand labels, no frame-specific constants for this game.
- Do not tune on the public 5 minutes; it has 17 possessions and picks the wrong answer.
- The submission must be reproducible byte-for-byte from `solution/run.py`: seed randomness,
  pin deps (`make lock` after adding any).

## Layout

- `solution/run.py` — our entry point; `predict()` is where the method goes.
- `starter/` — organiser loaders (`load_atd.py`, `load_smart_tagging.py`, `load_homography.py`)
  and `baseline.py`. Prefer importing from these over re-parsing files.
- `games.py` — frame alignment. ATD `frame_id` = video frame + 1; Smart Tagging seconds × 25.
- Run things with `.venv/bin/python`; shortcuts in the `Makefile`.
