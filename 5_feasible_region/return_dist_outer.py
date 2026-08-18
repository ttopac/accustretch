from calc_distanceFromEllipse import calcdist
import sys
import json
import numpy as np
import os
from pathlib import Path
import math

if __name__ == "__main__":
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  dists_list = list()
  stiff_file = sys.argv[1]
  dmax_file = sys.argv[2]
  # stiff_file = os.path.join(cur_dir, 'stiffness_file.txt')
  # dmax_file = os.path.join(cur_dir, 'dmax_file.txt')
  
  with open(os.path.join(cur_dir,'246_ellipse_def_ver.json'), 'r', encoding='utf-8') as f:
    ellipse1 = json.load(f)
  with open(os.path.join(cur_dir,'246_ellipse_def_hor.json'), 'r', encoding='utf-8') as f:
    ellipse2 = json.load(f)
  with open(stiff_file, "r") as fo:
    lines = fo.readlines()
    stiffnesses = np.asarray(lines)
    stiffnesses = np.core.defchararray.strip(stiffnesses,"\n").astype('float32') * 1e5 #Because we do this multiplacion in fitting the ellipse too
  with open(dmax_file, "r") as fo:
    lines = fo.readlines()
    dmaxs = np.asarray(lines)
    dmaxs = np.core.defchararray.strip(dmaxs,"\n").astype('float32')
  points = np.vstack((stiffnesses, dmaxs))

  a1 = ellipse1["a"]
  b1 = ellipse1["b"]
  x01 = ellipse1["x0"]
  y01 = ellipse1["y0"]
  theta1 = ellipse1["theta"]
  a2 = ellipse2["a"]
  b2 = ellipse2["b"]
  x02 = ellipse2["x0"]
  y02 = ellipse2["y0"]
  theta2 = ellipse2["theta"]

  for i in range(points.shape[1]):
    pointdist1, _ = calcdist(x01, y01, a1, b1, theta1, points[:,i])
    pointdist2, _ = calcdist(x02, y02, a2, b2, theta2, points[:,i])
    pointdist = min(pointdist1, pointdist2)
    pointdist = math.exp(pointdist)-1 #Return exponential of the distance. Penalty exponentially increases as we get further away from ellipse bound
    dists_list.append(pointdist)

  with open("outer_ellipse_dist.txt", "w") as fo:
    for line in dists_list:
      if isinstance(line, str) == False:
        line = str(line)
      fo.writelines(line+"\n")
