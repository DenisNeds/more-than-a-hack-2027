"""Our submission: data in, possession file out. The one command the deliverables ask for.

    python solution/run.py --team <team_name>        # or: make submission TEAM=<team_name>

Writes evaluation/results/<team_name>.csv and validates it. Right now it reproduces
baseline_smooth50 (the published floor) so the pipeline is wired end to end; replace predict()
with the real method.

Rules worth keeping in view while editing this file (RULES.md):
  - no hand labels or frame-specific constants for this game -- everything comes out of code
  - the public 5 minutes are for checking the pipeline, never for tuning
  - the output must be byte-identical on every run: seed anything random
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "starter"))
import baseline  # noqa: E402

RESULTS_DIR = os.path.join(ROOT, "evaluation", "results")


def predict():
    """One label per tactical video frame: an array of 'H' / 'A' / 'D' / 'X', length 199319."""
    codes = baseline.build()
    return baseline.smooth(codes, 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--team", default=os.environ.get("TEAM", "our_team"),
                        help="file name for the submission; the board names the row after it")
    parser.add_argument("--out", default=RESULTS_DIR, help="where to write")
    args = parser.parse_args()

    path = baseline.write_submission(os.path.join(args.out, args.team + ".csv"), predict())
    print("wrote", os.path.relpath(path, ROOT))
    sys.exit(subprocess.call([sys.executable,
                              os.path.join(ROOT, "evaluation", "validate_submission.py"), path]))
