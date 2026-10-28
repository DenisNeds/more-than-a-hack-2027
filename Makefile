# Team shortcuts. Every target is a thin wrapper over a command documented in TEAM.md.
PY   := .venv/bin/python
TEAM ?= our_team

.PHONY: setup lock eval bootstrap baseline submission validate notebook

setup:              ## venv + pinned deps + git guards + Jupyter kernel (run once per clone)
	uv venv --allow-existing --python 3.11 .venv
	uv pip install --python $(PY) -r requirements-lock.txt
	git config core.hooksPath .githooks
	$(PY) -m nbstripout --install --attributes .gitattributes
	$(PY) -m ipykernel install --user --name mtah2027 --display-name "MTAH 2027 (.venv)"

lock:               ## re-pin after adding a dependency: uv pip install --python .venv/bin/python <pkg>
	{ echo "# Pinned environment for reproducing the submission (Python 3.11). Regenerate with: make lock"; \
	  uv pip freeze --python $(PY); } > requirements-lock.txt

eval:               ## score everything in evaluation/results/ against the public 5 minutes
	$(PY) evaluation/run_evaluation.py

bootstrap:          ## same, with confidence intervals -- use before believing any gap
	$(PY) evaluation/run_evaluation.py --bootstrap 1000

baseline:           ## regenerate the four reference baselines (needs data/)
	$(PY) starter/baseline.py

submission:         ## build + validate evaluation/results/$(TEAM).csv (needs data/)
	$(PY) solution/run.py --team $(TEAM)

validate:           ## make validate FILE=path/to.csv
	$(PY) evaluation/validate_submission.py $(FILE)

notebook:
	$(PY) -m notebook starter/
