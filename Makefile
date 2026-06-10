.PHONY: install reproduce tables figures paper clean test

install:
	python -m pip install -U pip
	python -m pip install -e .
	python -m pip install -r requirements.txt

reproduce:
	python scripts/reproduce_results.py --all

tables:
	python scripts/reproduce_results.py --tables

figures:
	python scripts/reproduce_results.py --figures

paper:
	cd paper && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex

test:
	python scripts/reproduce_results.py --tables
	python -c "import pandas as pd; from pathlib import Path; p=Path('results/toy_model_amplified_fixed_scan.csv'); assert p.exists(); df=pd.read_csv(p); assert abs(df.loc[df.lambda_mem.eq(0.2), 'post_delta_h_norm'].iloc[0] - 9.438717273359079e-4) < 1e-12; print('[ok] reproducibility smoke test passed')"

clean:
	rm -rf results/*.csv results/synthetic_detector results/multidetector paper/*.aux paper/*.log paper/*.out
