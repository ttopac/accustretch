#%%
import sys
import numpy as np
import prepareData
import utils
import os
from pathlib import Path
import pickle
import sklearn
print (os.path.dirname(sys.executable))

#%% Define parameters (all in mm)
roundbase = 1.0
node_edge_size = 2.512 #(mm)

### maxsize specifies the max(horizontal, vertical) distance between top left points of the island nodes.
### maxsize is determined manually based on the stretchability constraints of serpentines.
### maxsize specifies the max(horizontal, vertical) distance between top left points of the island nodes.

nom_dist_btw_nodes = 1.95 #(mm) Change based on average size of allowed legs.
col_count = 7 #7
row_count = 9 #9
twoD = False if row_count == 1 else True
maxsize = 83.3 if twoD else 60.2 #Note that this is the distance from center to center. Total size will be 2.512mm larger than this.
linear = False
nonlin_coeff_surrogate = 0.1540433 #0.08 ###Change this based on best fit!! !!!NEGLECT IF USING NN MODEL!!!
FvsDmax_params = pickle.load (open (os.path.join (Path (__file__).parents[1], "nonlinearStiffness", "summary&model_files", "8leg", "LH_quad_Model_RF1.p"), 'rb')) #!!!NEGLECT IF USING NN MODEL!!!
NN_model_path = os.path.join(Path(__file__).parents[1], "nonlinearStiffness", "246leg_v4_NN_model_NT2_random_RF1_scaled_wolegs.h5")
inp_scaler = pickle.load(open(os.path.join(Path(__file__).parents[1], "nonlinearStiffness", "inp_scaler246_v4_wolegs.pkl"), 'rb'))
out_scaler = pickle.load(open(os.path.join(Path(__file__).parents[1], "nonlinearStiffness", "out_scaler246_v4_wolegs.pkl"), 'rb'))
dmax_model_params = dict() # !!!NEGLECT IN 2021 TESTS!!! This associates k0 stiffness with dmax: dmax = 1, k0, k0^2 (Obtained from Optimus 8leg_v3 8leg_dmax_NT2_RF1)
use_simple_nonlin = False
use_NN = True
useConnectors = True

spring_count = (row_count-1)*col_count + row_count*(col_count-1)

def getParams():
  return (maxsize, roundbase, col_count, row_count, twoD, nom_dist_btw_nodes, node_edge_size)

if __name__ == "__main__":
  print (sys.version)
  multileg = False
  stiffFile = sys.argv[1]
  itercount = sys.argv[2] #This number specifies iteration number to change distances between islands.
  distFile = sys.argv[3]
  nodeLoc = sys.argv[4]
  dmax_file = sys.argv[5]
  if multileg: legs_file = sys.argv[6]

  # scriptpath = os.path.realpath(os.path.dirname(sys.argv[0]))
  # os.chdir(scriptpath)
  # cwd = os.getcwd()
  # multileg = False
  # stiffFile = cwd+"/parameterFiles/stiffness_file.txt"
  # itercount = 1
  # nodeLoc = cwd+"/parameterFiles/Stanford5.psd.txt"
  # dmax_file = cwd+"/parameterFiles/dmax_file.txt"
  # distFile = cwd+"/parameterFiles/dist_file.txt"


  #%% Prepare data for .inp file
  (island, islandID, movelong, moveshort) = prepareData.prepare_stretched_locs_fromphotoshop(maxsize, roundbase, col_count, row_count, distFile, node_edge_size, nodeLoc, twoD)
  (hor_island_dist, ver_island_dist) = prepareData.output_dist_btw_nodes(col_count, row_count, itercount, distFile)
  (nodePos, centerNodes, nodeCon, BCsets, springCon) = prepareData.prepare_for_inp_file(hor_island_dist, ver_island_dist, island, islandID, col_count, row_count, node_edge_size, twoD)
  #%%
  import createinp
  if multileg:
    createinp.createFile(nodePos, centerNodes, nodeCon, BCsets, movelong, moveshort, row_count, col_count, springCon, stiffFile, twoD, linear,
                       nonlin_coeff_surrogate, useConnectors, use_simple_nonlin, FvsDmax_params, dmax_model_params, use_NN, NN_model_path, inp_scaler, out_scaler, dmax_file, legs_file)
  else:
    createinp.createFile(nodePos, centerNodes, nodeCon, BCsets, movelong, moveshort, row_count, col_count, springCon, stiffFile, twoD, linear,
                       nonlin_coeff_surrogate, useConnectors, use_simple_nonlin, FvsDmax_params, dmax_model_params, use_NN, NN_model_path, inp_scaler, out_scaler, dmax_file)
  #%%
  # utils.writeks (spring_count)
  # utils.writeds (spring_count)
  # utils.write_stretch_pos (islandID, row_count, col_count)
  # utils.write_interconnectStretchs_lines(row_count, col_count, node_edge_size, hor_island_dist, ver_island_dist)
  # utils.write_unique_deviations(row_count, col_count)
