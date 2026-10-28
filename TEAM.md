# Team workflow

Our fork of the challenge repo. `origin` = github.com/DenisNeds/more-than-a-hack-2027 (the
public repo we submit), `upstream` = metrica-sports (organiser fixes). **Deadline: 17 Nov 2026.**

## One-time setup (each of us)

```bash
brew install uv                      # or: curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/DenisNeds/more-than-a-hack-2027.git
cd more-than-a-hack-2027
make setup                           # Python 3.11 venv, pinned deps, git guards, Jupyter kernel
make eval                            # should print the 4-baseline scoreboard
```

Then unpack the data bundle (download link from enrolment email) into `data/` — see
[data/README.md](data/README.md). Each of us needs our own copy; **never commit or share it via
the repo**. In VS Code pick the `.venv` interpreter / "MTAH 2027 (.venv)" kernel.

## Daily loop

```bash
git checkout main && git pull
git checkout -b <name>/<idea>        # e.g. miha/dead-ball-from-tagging
# ... work ...
make submission TEAM=<name>_<idea>   # writes + validates evaluation/results/<name>_<idea>.csv
make eval                            # compare against baselines on the public 5 min
git push -u origin HEAD              # open a PR into main, one teammate reviews
```

- Small PRs, merged often. `main` must always run `make submission` cleanly.
- Exploration goes in notebooks under `notebooks/<name>/`; anything we keep moves into
  `solution/` as a function. Notebook outputs are stripped on commit automatically.
- Added a package? `uv pip install --python .venv/bin/python <pkg>` then `make lock` and commit
  `requirements-lock.txt` in the same PR.
- Organiser updates: `git fetch upstream && git merge upstream/main`.

## Guard rails (these can disqualify us)

| | |
|---|---|
| **No data in git** | `data/` is gitignored and a pre-commit hook blocks data files, submissions and anything > 5 MB. Don't paste data rows into issues/PRs either — the repo is public. |
| **No data to hosted LLMs** | Terms forbid uploading videos/data/extracts to ChatGPT, Claude, Gemini etc. Fine to ask them about code and the documented format; not fine to paste rows, plots or frames. `.claude/settings.json` blocks Claude Code from reading `data/`. |
| **No hand labels** | Watching the video to understand it is fine; turning what we saw into labels, corrections or frame-specific constants is not. |
| **Don't tune on the public 5 min** | 17 possessions — it picks the wrong window even for the baseline. Use it to check correctness; use `make bootstrap` before trusting a gap. |
| **Reproducible** | `python solution/run.py` must regenerate the exact submitted file. Seed everything. |

## Who does what

| | owner | notes |
|---|---|---|
| Possession / team-in-control model | | |
| Dead-ball detection (Smart Tagging set pieces, ball out of bounds) | | |
| Ball-gap handling & smoothing / state model | | |
| Technical report ([docs/TECHNICAL_REPORT.md](docs/TECHNICAL_REPORT.md)) | | |
| Final submission: CSV + repo URL + report via Google Form | | one response per team |

## Submission checklist

- [ ] `make submission TEAM=<team_name>` on a clean clone of `main` reproduces the file
- [ ] `make validate FILE=evaluation/results/<team_name>.csv` passes
- [ ] report exported as `<team_name>.pdf` (or `.md`)
- [ ] repo is public and contains no data (`git ls-files data/` shows only the README)
- [ ] uploaded through the form before 17 Nov 2026
