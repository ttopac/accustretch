# Serpentine size tables

Per-bridge serpentine dimensions of the paper device, solved by the FICO
Xpress back-design step.

## Provenance

The tables are produced by the notebook
FICO_2D_latest_246leg_INTSinModel_v4_PaperRepeatOct2023.ipynb in
7_serpentine_backdesign. For every bridge of the optimized network, the
solver combines the bridge stiffness and required stretch targets of the
macroscale optimization (S_logo_results/1_AbaqusFiles, produced by
6_network_optimization) with the surrogate polynomial and integral
coefficient pickles in 7_serpentine_backdesign, and solves for the
serpentine parameters of that bridge.

## Files

FICO_small_feasReg_2D_246_v4_all.csv lists all 110 bridges with columns
BridgeLoc, leg count, bounding angle, node-to-node length, wire width,
and nominal stiffness. The serpentine_4_NTN and serpentine_6_NTN tables
split the same solution by leg count and append the curve length and
stretched length columns used for the Creo geometry regeneration (see
S_logo_results/3_serpentineDesigns). The optimized network needed no
2-leg serpentines, so there is no 2_NTN table.
