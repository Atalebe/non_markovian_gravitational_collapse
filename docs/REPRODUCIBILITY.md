# Reproducibility Notes

This repository is a frozen validation snapshot for the manuscript. It is not a full numerical relativity code.

The reproducibility target is narrower and explicit:

- regenerate manuscript result tables,
- regenerate manuscript figures,
- verify that reported scalar toy, detector, and network diagnostics are traceable to CSV outputs.

The most important executable command is:

```bash
make reproduce
```

The key output files are:

```text
results/toy_model_amplified_fixed_scan.csv
results/toy_model_comparison.csv
results/synthetic_detector/synthetic_detector_snr_by_template.csv
results/synthetic_detector/synthetic_detector_degeneracy_summary.csv
results/network_glitch_comparison.csv
results/network_snr_threshold_scan.csv
```

The calculations are dimensionless and synthetic. They do not report astrophysical detection rates, distances, or calibrated detector sensitivities.

## Archived reproducibility snapshot

The initial reproducibility snapshot is archived on Zenodo:

- DOI: https://doi.org/10.5281/zenodo.20622873
- Version: v1.0.0

This DOI should be used when citing the exact code, configuration files, frozen tables, and manuscript figures associated with the initial release.
