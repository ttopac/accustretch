# Assembly macro

assemblyMacro.py builds the Abaqus model Onerow_Stretch of the paper
device.

## Provenance

The file is a recorded Abaqus/CAE Python journal. It imports the
serpentine STEP designs (0.stp through 109.stp, download link in
S_logo_results/3_serpentineDesigns) as parts P0 through P109 with
PartFromGeometryFile, assigns their sections, and creates the instances
of the full assembly.

## Notes for rerunning

The script contains hard-coded absolute paths from the original machine,
which must be adapted to your local layout. Its final block chains the
old per-part seeding scripts through execfile calls. Those scripts are
consolidated in this repository, so remove that trailing block and run
S_logo_results/5_abaqusMeshingScripts/mesh_parts.py instead.
