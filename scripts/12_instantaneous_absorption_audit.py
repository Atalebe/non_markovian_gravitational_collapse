#!/usr/bin/env python3
"""
Instantaneous-state absorption audit.

Purpose:
    Probe the falsifiability boundary stated in the manuscript.

The matched-state toy model forces R, dR/dt, and A to agree at t_star.
Therefore a Markovian source model built only from those matched instantaneous
variables predicts no post-match divergence.

However, if an enlarged instantaneous model is allowed to include the
post-coupling acceleration difference at t_star, then it can absorb the memory
effect, because that acceleration contains lambda_mem * Delta M_coll.

This audit quantifies that boundary. It does not prove the astrophysical
memory hypothesis. It clarifies what kind of enlarged state would be needed
to remove the residual.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SRC = Path("results/toy_model_amplified_fixed_scan.csv")
OUT = Path("results/instantaneous_absorption_audit.csv")
SUMMARY = Path("results/instantaneous_absorption_audit_summary.csv")

if not SRC.exists():
    raise FileNotFoundError(
        f"Missing {SRC}. Run `make reproduce` first."
    )

df = pd.read_csv(SRC).copy()

required = [
    "lambda_mem",
    "delta_match_after_reset",
    "delta_M_at_tstar",
    "post_delta_h_norm",
]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns in {SRC}: {missing}")

# Because R, v=dR/dt, and A are reset to match, ordinary matched-state
# Markovian variables have zero separation by construction.
df["delta_x_matched_state"] = df["delta_match_after_reset"]

# The memory-coupled acceleration difference at t_star is proportional to
# lambda_mem * Delta M_coll because all other post-match terms are identical.
df["delta_acc_memory_term"] = df["lambda_mem"] * df["delta_M_at_tstar"]

# A Markovian model using only matched variables predicts zero acceleration
# difference from the matched state itself.
df["delta_acc_markovian_matched_state"] = 0.0

# Fit Rh ~ slope * (lambda * Delta M) through the origin.
x = df["delta_acc_memory_term"].to_numpy(dtype=float)
y = df["post_delta_h_norm"].to_numpy(dtype=float)

mask = x > 0
if mask.sum() >= 2:
    slope = float(np.sum(x[mask] * y[mask]) / np.sum(x[mask] ** 2))
    yhat = slope * x[mask]
    ss_res = float(np.sum((y[mask] - yhat) ** 2))
    ss_tot = float(np.sum((y[mask] - np.mean(y[mask])) ** 2))
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 0 else np.nan
else:
    slope = np.nan
    r2 = np.nan

df.to_csv(OUT, index=False)

summary = pd.DataFrame([{
    "n_rows": len(df),
    "max_delta_match_after_reset": df["delta_match_after_reset"].abs().max(),
    "delta_M_at_tstar": df["delta_M_at_tstar"].iloc[-1],
    "max_delta_acc_memory_term": df["delta_acc_memory_term"].max(),
    "max_post_delta_h_norm": df["post_delta_h_norm"].max(),
    "slope_Rh_vs_lambda_deltaM": slope,
    "r2_Rh_vs_lambda_deltaM": r2,
    "interpretation": (
        "Matched instantaneous variables alone cannot explain the residual; "
        "a post-coupling acceleration variable can absorb it because it is "
        "equivalent to including lambda_mem times the retained memory contrast."
    ),
}])

summary.to_csv(SUMMARY, index=False)

print("[ok] wrote", OUT)
print("[ok] wrote", SUMMARY)
print(summary.to_string(index=False))
