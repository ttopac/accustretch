"""Consolidated mesh seeding for the paper-run assembly.

This single script replaces the 110 per-part seeding scripts (P0.py to
P109.py) that originally performed the mesh seeding. All part names,
global seed parameters, edge pick coordinates, and per-edge seed counts
were extracted verbatim into meshing_seeds.json, which must sit next to
this file.

Run it inside Abaqus CAE after the assembly macro in
S_logo_results/4_abaqusAssemblyMacro has created the parts of the
Onerow_Stretch model, for example with

    abaqus cae noGUI=mesh_parts.py

The script seeds every part globally, applies the recorded edge seeds
through the same getClosest picks the original scripts used, and calls
generateMesh on each part. Compatible with the Python 2.7 interpreter of
Abaqus 6.14 and later.
"""
import json
import os

from abaqus import *
from abaqusConstants import *

CONSTRAINTS = {"FINER": FINER, "FIXED": FIXED, "FREE": FREE}

try:
    _here = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _here = os.getcwd()

with open(os.path.join(_here, "meshing_seeds.json")) as f:
    data = json.load(f)

model = mdb.models[data["model"]]


def part_number(name):
    try:
        return int(name[1:])
    except ValueError:
        return 10 ** 9


for pname in sorted(data["parts"], key=part_number):
    spec = data["parts"][pname]
    p = model.parts[pname]
    sp = spec["seedPart"]
    p.seedPart(size=sp["size"], deviationFactor=sp["deviationFactor"],
               minSizeFactor=sp["minSizeFactor"])
    e = p.edges
    for op in spec["operations"]:
        picked = e.getClosest(
            coordinates=tuple(tuple(c) for c in op["coordinates"]))
        edges = tuple(v[0] for v in picked.values())
        constraint = CONSTRAINTS[op.get("constraint", "FINER")]
        if op["method"] == "seedEdgeByNumber":
            p.seedEdgeByNumber(edges=edges, number=op["number"],
                               constraint=constraint)
        elif op["method"] == "seedEdgeBySize":
            p.seedEdgeBySize(edges=edges, size=op["size"],
                             constraint=constraint)
        else:
            raise ValueError("unknown seed method %s" % op["method"])
    p.generateMesh()
    print("meshed %s" % pname)
