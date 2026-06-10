"""Frozen numerical diagnostics reported in the manuscript.

These constants are the deterministic outputs from the toy-model, detector,
and network validation pipeline used for the manuscript figures and tables.
They allow a reviewer to regenerate the result tables and manuscript-grade
figures without external data or detector packages.
"""

TOY_AMPLIFIED = [
    {"lambda_mem": 0.00, "delta_M_at_tstar": 4.839245922857761e-3, "delta_match_after_reset": 0.0, "post_delta_h_norm": 2.1001394719363178e-10, "post_delta_h_max_abs": 4.900568423282792e-10},
    {"lambda_mem": 0.02, "delta_M_at_tstar": 4.839245922857761e-3, "delta_match_after_reset": 0.0, "post_delta_h_norm": 9.315033631671277e-5, "post_delta_h_max_abs": 5.052663125081763e-5},
    {"lambda_mem": 0.05, "delta_M_at_tstar": 4.839245922857761e-3, "delta_match_after_reset": 0.0, "post_delta_h_norm": 2.3338286362822763e-4, "post_delta_h_max_abs": 1.2631668196565887e-4},
    {"lambda_mem": 0.10, "delta_M_at_tstar": 4.839245922857761e-3, "delta_match_after_reset": 0.0, "post_delta_h_norm": 4.6847058637468597e-4, "post_delta_h_max_abs": 2.526337153990685e-4},
    {"lambda_mem": 0.20, "delta_M_at_tstar": 4.839245922857761e-3, "delta_match_after_reset": 0.0, "post_delta_h_norm": 9.438717273359079e-4, "post_delta_h_max_abs": 5.052688375523813e-4},
]

TOY_COMPARISON = [
    {"run": "baseline_fixed", "lambda_min": 0.0, "lambda_max": 0.2, "delta_M_at_tstar": 2.3529926151760966e-5, "Rh_null": 2.1449404699512529e-10, "Rh_lambda_max": 4.266284012465623e-6, "amplification": 1.988999e4, "R_match": 0.2613274131034083, "delta_match_after_reset": 0.0},
    {"run": "amplified_fixed", "lambda_min": 0.0, "lambda_max": 0.2, "delta_M_at_tstar": 4.839245922857761e-3, "Rh_null": 2.1001394719363178e-10, "Rh_lambda_max": 9.438717273359079e-4, "amplification": 4.494329e6, "R_match": 0.261727538740273, "delta_match_after_reset": 0.0},
]

SINGLE_DETECTOR_SNR = [
    {"lambda_mem": 0.00, "mean_snr": 0.0009480514049436459, "std_snr": 0.018751447101649388},
    {"lambda_mem": 0.02, "mean_snr": 11.96674067852844, "std_snr": 0.015592318092781712},
    {"lambda_mem": 0.05, "mean_snr": 11.976896567481408, "std_snr": 0.015588098130362318},
    {"lambda_mem": 0.10, "mean_snr": 11.989668568595857, "std_snr": 0.015579911940427987},
    {"lambda_mem": 0.20, "mean_snr": 11.999817567785785, "std_snr": 0.015577158235880762},
]

DETECTOR_DEGENERACY = [{
    "mean_nonzero_template_overlap": 0.998939,
    "min_nonzero_template_overlap": 0.997238,
    "max_nonzero_template_overlap": 0.999922,
    "mean_null_vs_memory_overlap": 0.000077,
    "max_null_vs_memory_overlap": 0.000723,
    "selection_accuracy": 1.0,
    "mean_delta_snr_injected_minus_null": 11.99887,
}]

NETWORK_DETECTORS = [
    {"detector": "H1", "delay_ms": 0.0, "delay_samples": 0, "F_plus": 0.70, "F_cross": 0.20, "psd_scale": 1.0, "optimal_snr": 10.666321803146882},
    {"detector": "L1", "delay_ms": 7.1, "delay_samples": 11, "F_plus": -0.62, "F_cross": 0.25, "psd_scale": 1.1, "optimal_snr": 9.92717667542265},
    {"detector": "V1", "delay_ms": -14.3, "delay_samples": -23, "F_plus": 0.28, "F_cross": -0.36, "psd_scale": 2.4, "optimal_snr": 3.5610030113238964},
]

NETWORK_GLITCH = [
    {"scenario": "with_V1_glitch", "target_network_snr": 15.0, "mean_network_rho_memory": 15.000244, "std_network_rho_memory": 0.016502, "mean_network_rho_null": 0.041499, "std_network_rho_null": 0.011975, "mean_delta_network_rho": 14.958745, "mean_Ec_over_Ei": 2.592884, "std_Ec_over_Ei": 0.001665, "glitch_enabled": True, "glitch_detector": "V1"},
    {"scenario": "no_glitch", "target_network_snr": 15.0, "mean_network_rho_memory": 15.000246, "std_network_rho_memory": 0.016502, "mean_network_rho_null": 0.025044, "std_network_rho_null": 0.010919, "mean_delta_network_rho": 14.975202, "mean_Ec_over_Ei": 2.592885, "std_Ec_over_Ei": 0.001665, "glitch_enabled": False, "glitch_detector": "none"},
]

NETWORK_SNR_SCAN = [
    {"snr_target_grid": 3.0, "mean_network_rho_memory": 3.0003058036408863, "std_network_rho_memory": 0.0164981799784245, "mean_network_rho_null": 0.0250530306464978, "std_network_rho_null": 0.0109690802550158, "mean_delta_network_rho": 2.9752527729943883, "mean_Ec_over_Ei": 2.5920667946221063, "std_Ec_over_Ei": 0.0083268758896454, "n_trials": 200},
    {"snr_target_grid": 5.0, "mean_network_rho_memory": 5.000276069459904, "std_network_rho_memory": 0.0165002447457587, "mean_network_rho_null": 0.025051046244646, "std_network_rho_null": 0.0109603285623316, "mean_delta_network_rho": 4.975225023215258, "mean_Ec_over_Ei": 2.592493842879593, "std_Ec_over_Ei": 0.0049960813320218, "n_trials": 200},
    {"snr_target_grid": 8.0, "mean_network_rho_memory": 8.000259346978902, "std_network_rho_memory": 0.0165013641813489, "mean_network_rho_null": 0.025048459046563, "std_network_rho_null": 0.010947449978651, "mean_delta_network_rho": 7.975210887932338, "mean_Ec_over_Ei": 2.592718117383006, "std_Ec_over_Ei": 0.0031225416285287, "n_trials": 200},
    {"snr_target_grid": 10.0, "mean_network_rho_memory": 10.000253773286774, "std_network_rho_memory": 0.0165017306030139, "mean_network_rho_null": 0.0250469937902224, "std_network_rho_null": 0.0109390309661337, "mean_delta_network_rho": 9.975206779496553, "mean_Ec_over_Ei": 2.592790325550475, "std_Ec_over_Ei": 0.0024980316666984, "n_trials": 200},
    {"snr_target_grid": 12.0, "mean_network_rho_memory": 12.000250057620525, "std_network_rho_memory": 0.0165019730159033, "mean_network_rho_null": 0.025045736131104, "std_network_rho_null": 0.0109307458659179, "mean_delta_network_rho": 11.975204321489418, "mean_Ec_over_Ei": 2.5928377560506526, "std_Ec_over_Ei": 0.0020816923369293, "n_trials": 200},
    {"snr_target_grid": 15.0, "mean_network_rho_memory": 15.000246342056462, "std_network_rho_memory": 0.016502213933989, "mean_network_rho_null": 0.025044238838659, "std_network_rho_null": 0.0109185702330512, "mean_delta_network_rho": 14.975202103217804, "mean_Ec_over_Ei": 2.59288461994972, "std_Ec_over_Ei": 0.0016653534167094, "n_trials": 200},
]
