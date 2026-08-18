import numpy as np
import prepareData

def createStiffnesses (row_count, col_count, stiffFile):
  f = open(stiffFile, 'r')
  lines = f.readlines()
  f.close()

  stiffnesses = np.asarray(lines)
  stiffnesses = np.core.defchararray.strip(stiffnesses,"\n")
  return stiffnesses

def createDmax (dmax_file):
  f = open (dmax_file, 'r')
  lines = f.readlines ()
  f.close ()

  dmaxs = np.asarray (lines)
  dmaxs = np.core.defchararray.strip (dmaxs, "\n")
  return dmaxs

def createLegs (legs_file):
  if legs_file != None:
    f = open (legs_file, 'r')
    lines = f.readlines ()
    f.close ()

    legs = np.asarray (lines)
    legs = np.core.defchararray.strip (legs, "\n")
    return legs
  else:
    return []