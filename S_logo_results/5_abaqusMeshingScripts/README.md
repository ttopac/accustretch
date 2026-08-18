# Mesh seeding

mesh_parts.py and meshing_seeds.json seed and mesh every serpentine part
of the paper-run assembly.

## How meshing_seeds.json was created

The mesh seeding originally lived in 110 per-part Abaqus scripts (P0.py
through P109.py), one for every serpentine part. Each script was
executed against a recording stub of the Abaqus Python API, which
captured the part name, the global seedPart parameters (size 0.028,
deviation factor 0.013, minimum size factor 0.3, identical for all
parts), and every seedEdgeByNumber call with its exact getClosest pick
coordinates and edge seed count. The extraction recovered 2084 seeding
operations across the 110 parts, all with the FINER constraint, and was
verified file by file against the call counts of the sources.

## Schema

The JSON stores the model name and, per part, the seedPart parameters
plus an ordered operations list with method, pick coordinates, seed
number, and constraint.

## Usage

Run mesh_parts.py inside Abaqus CAE after the macro in
S_logo_results/4_abaqusAssemblyMacro has created the parts, with
meshing_seeds.json next to it. For example

    abaqus cae noGUI=mesh_parts.py

The script replays the recorded picks and finishes every part with
generateMesh.
