# Serpentine STEP designs

The STEP geometries of the serpentine bridges used in the paper device
are not tracked in this repository because of file size. Download them
from Google Drive.

https://drive.google.com/drive/folders/1yRcebtFO8xOrDBfPEnk-elYopCvKk08H?usp=sharing

## How the designs are generated

Every bridge geometry comes from a parametric serpentine part in PTC
Creo. The driving dimensions of each bridge (leg count, bounding angle,
node-to-node length, wire width, curve length, and stretched length) are
taken from the size tables in S_logo_results/2_serpentineSizes. The Creo
part is regenerated once per bridge with that row of parameters and
exported as a STEP file numbered by bridge location, 0.stp through
109.stp, which is the order the assembly macro in
S_logo_results/4_abaqusAssemblyMacro expects when importing parts P0
through P109. In the original pipeline this regenerate-and-export loop
ran automatically through the Optimus and Creo coupling described in
8_validation_assembly/readme!!.txt. The same parametric serpentine
family underlies the mesoscale characterization models in
2_serpentine_characterization, whose CreoOutputs tables record the
key-point coordinates per leg count.
