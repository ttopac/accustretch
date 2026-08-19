# AccuStretch

Design and optimization code for the article "Stretchable Electronics Design
for Non-uniform Deployment on Prescribed Positions" (submitted to npj
Flexible Electronics). AccuStretch places the functional islands of an
island-bridge stretchable device at prescribed target positions by tailoring
the serpentine bridge between every pair of islands, so a wafer-scale device
can expand non-uniformly onto a much larger target layout.

## Pipeline

The numbered folders follow the order of the design pipeline.

    0_characterization             material stress-strain curves for the FE models
    1_target_definition            target layout export and design checks
    2_serpentine_characterization  mesoscale serpentine FE runs and summaries
    3_stretch_limits               serpentine stretch range notebooks
    4_surrogate_model              Keras NN surrogate with scalers and training data
    5_feasible_region              feasibility ellipses of the (k0, dmax) space
    6_network_optimization         Optimus macroscale network expansion
    7_serpentine_backdesign        FICO Xpress serpentine back-design
    8_validation_assembly          Abaqus assembly generation for validation
    S_logo_results                 the run reported in the paper (see VersionLog.rtf)

## Requirements

Python 3 with numpy, scikit-learn, and TensorFlow/Keras. Abaqus 6.14 or
newer for the finite element runs. PTC Creo 5.0 for parametric serpentine
geometry. Noesis Optimus 2020.x for the macroscale optimization. FICO
Xpress 8.10 for the serpentine back-design step.

## Geometry files

STEP serpentine geometries are intentionally not tracked here. They are
regenerated in Creo from the optimized serpentine parameters (bounding
angle, wire width, node-to-node length, required stretch) produced by the
back-design step, then imported and assembled into the Abaqus validation
model by 8_validation_assembly/genAbaqAssm.py, the macro in
S_logo_results/4_abaqusAssemblyMacro, and the consolidated mesh seeding
script in S_logo_results/5_abaqusMeshingScripts. The meshed forward
simulation input deck fwd_122_v4.inp (27 MB) and heavy solver outputs
(odb, cae, sat, dxf) are likewise excluded because they are regenerable
from these inputs. Google Drive download links for the untracked
artifacts (the STEP designs, the assembled 246assm_v4.cae model, and the
meshed input deck) sit as README files in the matching S_logo_results
subfolders.

## Notes

The scripts were written for the original research folder layout, so some
hard-coded paths inside them (for example references to sibling folders
of the original machine) may need one-line adjustments when run from this
repository structure.

## Citation

Please cite the npj Flexible Electronics article above. Earlier stages of
this work were presented at IWSHM 2019 (doi 10.12783/shm2019/32426) and
as a conference abstract at innoLAE 2021.

## Acknowledgement

This work was supported by the U.S. Air Force Office of Scientific
Research (AFOSR) under grant no. FA9550-16-1-0087.

## License

MIT. See LICENSE.
