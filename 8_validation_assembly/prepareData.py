import numpy as np
import os
import csv

rundir = os.getcwd()

def prepare_stretched_locs_fromabaqsurr(nodeLocX, nodeLocY):
  island = dict()
  xlocs = list()
  ylocs = list()
  
  with open(nodeLocX, "r") as f:
    lines = f.readlines()
    for line in lines:
      xlocs.append(float(line))
  with open(nodeLocY, "r") as f:
    lines = f.readlines()
    for line in lines:
      ylocs.append(float(line))

  for i in range(len(xlocs)):
    island[i] = dict()
    island[i]["str_mm"] = np.zeros(2)
    island[i]["str_mm"][0] = xlocs.pop()
    island[i]["str_mm"][1] = ylocs.pop()
  
  return island


def prepare_stretched_locs_fromphotoshop(maxsize, roundbase, col_count, row_count, distFile, node_edge_size, nodeLoc, twoD):
  island = list()
  with open(nodeLoc, "r") as f:
    fieldnames = ("nodetype","str_xpixel","str_ypixel")
    csv_read = csv.DictReader(f, fieldnames=fieldnames)

    #Convert keys of xpixel and ypixel to integers
    #Also change the coordinates to centroids  
    for row in csv_read:
      for key, value in row.items():
        if key == "str_xpixel" or key == "str_ypixel":
          row[key] = int (value) + 10
        else:
          row[key] = value
      island.append(row)

    #Sort dictionary based on ypixel and xpixel increasing
    # island = sorted (island, key=lambda i:(i["str_ypixel"], i["str_xpixel"])) #This listing creates unintentional results. Doesn't preserve the grid
    sorted_ix = list()
    islands = np.zeros((len(island), 2))
    for count,isl in enumerate(island):
      islands[count] = (isl["str_xpixel"], isl["str_ypixel"])
    for i in range(row_count):
      ysort = np.argsort(islands[:,1])[0:col_count]
      xsort = np.argsort(islands[ysort,0])
      for k in xsort:
        sorted_ix.append(ysort[k])
      islands [ysort] = 99999
    island = [island[i] for i in sorted_ix]

    #Create dict to map island ID to island object
    hor_nodes = 5
    ver_nodes = 5

    count = 0
    islandID = dict()
    for i in range(row_count):
      for j in range(col_count):
        islandID[(i,j)] = island[count]
        islandID[i,j]["unstr_mm"] = np.zeros(2)
        islandID[i,j]["node_pos"] = list()
        islandID[i,j]["node_ID"] = np.zeros((hor_nodes,ver_nodes))
        count += 1

    #Store island locations as numpy array
    for i in range(len(island)):
      island[i]["str_pixel"] = np.asarray((float(island[i]["str_xpixel"]), float(island[i]["str_ypixel"])))

    #Get topleft pixel. Normalize others so that topleft is (0,0)
    xmin, ymin = islandID[(0,0)]["str_pixel"][0], islandID[(0,0)]["str_pixel"][1]
    for i in island:
      i["str_pixel"][0] -= float(xmin)
      i["str_pixel"][1] -= float(ymin)
        
    #Rescale based on the size we want
    maxpix = np.amax(island[-1]["str_pixel"])
    counter = 0
    for i in island:
      i["str_mm"] = (i["str_pixel"] / maxpix * maxsize)  # 03/05/20 Prev. version

    #Determine stretch amount
    with open(distFile, "r") as f:
      dists = f.readlines()
      dists = [float(i) for i in dists]
      
    hor_wires = dists[0:(col_count-1)*row_count]
    ver_wires = dists[(col_count-1)*row_count:]
    init_hor_edge = sum(hor_wires[0:(col_count-1)]) + node_edge_size*col_count
    init_ver_edge = sum(ver_wires[0:(row_count-1)]) + node_edge_size*row_count
    initShortEdge = min (init_hor_edge, init_ver_edge)
    initLongEdge = max (init_hor_edge, init_ver_edge)
    
    id1, id2 = 0,0
    for i in range(len(island)):
      if island[i]["str_mm"][0] > id1:
        id1 = island[i]["str_mm"][0]
      if island[i]["str_mm"][1] > id2:
        id2 = island[i]["str_mm"][1]
    long_pos = max(id1,id2)
    short_pos = min(id1,id2) 

    long_stretch = long_pos-initLongEdge+node_edge_size
    short_stretch = short_pos-initShortEdge+node_edge_size
    if not twoD:
      short_stretch = 0 #THIS IS FOR ONEROW ONLY.
  return (island, islandID, long_stretch, short_stretch)

def output_dist_btw_nodes(col_count, row_count, itercount=1, distFile=None):
  #Calculate number of springs
  # corner_islands = 4
  # edge_islands = col_count*2 + (row_count-2)*2 - 4
  # inner_islands = (col_count-2) * (row_count-2)
  f = open(distFile, 'r')
  lines = f.readlines()
  f.close()
  count = 0
  hor_island_dist = np.zeros((row_count, col_count-1)) #Create an array to later modify island_distances(left_island_ID(0,0),right_island_ID(0,1),dist)
  ver_island_dist = np.zeros((row_count-1, col_count))
  if int(itercount) == 1:
    for i in range(row_count):
      for j in range(col_count-1):
        hor_island_dist[i,j] = lines[count] #hor_island_dist[i,j] refers to the distance between islandID[i,j] and islandID[i,j+1]
        count += 1
    for i in range(col_count):
      for j in range(row_count-1):
        ver_island_dist[j,i] = lines[count] #ver_island_dist[i,j] refers to the distance between islandID[i,j] and islandID[i+1,j]
        count += 1
  else:
    raise NotImplementedError
  return (hor_island_dist, ver_island_dist)

def prepare_for_inp_file(hor_island_dist, ver_island_dist, island, islandID, col_count, row_count, node_edge_size, twoD):
  # ------------- #
  # Prepare island node coords
  # ------------- #
  nodePos = list()
  centerNodes = list()
  nodeID = 1

  for i in range(row_count):
    for j in range(col_count):
      islandID[i,j]["unstr_mm"][0] = j*node_edge_size + np.sum(hor_island_dist[i,0:j]) - node_edge_size/2 #Gives x coord of topleft corner of the Island
      islandID[i,j]["unstr_mm"][1] = -1 * (i*node_edge_size + np.sum(ver_island_dist[0:i,j])) + node_edge_size/2 #Gives y coord of topleft corner of the Island
  
  for i in range(row_count):
    for j in range(col_count):
      for k in range(5): #Going down
        for l in range(5): #Going right
          islandID[i,j]["node_pos"] += (islandID[i,j]["unstr_mm"][0] +l/4*node_edge_size, islandID[i,j]["unstr_mm"][1] -k/4*node_edge_size, 0)
          islandID[i,j]["node_ID"][k,l] = nodeID
          line = str (str(nodeID) + "," + str(islandID[i,j]["unstr_mm"][0]+l/4*node_edge_size) + "," + str(islandID[i,j]["unstr_mm"][1] -k/4*node_edge_size) + ", 0.")
          nodePos.append(line)
          if k == 2 and l == 2:
            centerNodes.append(nodeID)
          nodeID += 1
  
  # ------------- #
  #Prepare node connectivity for island elements
  # ------------- #
  nodeCon = list()
  count = 1
  for i in range(row_count):
    for j in range(col_count):
      for k in range(4): #Going down
        for l in range(4): #Going right
          topLeft = islandID[i,j]["node_ID"][k,l]
          topRight = islandID[i,j]["node_ID"][k,l+1]
          bottomRight = islandID[i,j]["node_ID"][k+1,l+1]
          bottomLeft = islandID[i,j]["node_ID"][k+1,l]
          line = str(str(count) + "," + str(int(topRight)) + "," + str(int(topLeft)) + "," + str(int(bottomLeft)) + "," + str(int(bottomRight)))
          nodeCon.append(line)
          count += 1

  # ------------- #
  #Define sets for BCs
  # ------------- #
  BCsets = dict()

  #BC1: Fixed left
  nodes = list()
  for i in range(row_count):
    for k in range(5):
      nodes.append(islandID[i,0]["node_ID"][k,0])
  BCsets["fixed_left"] = nodes

  #BC2: Move right
  nodes = list()
  for i in range(row_count):
    for k in range(5):
      nodes.append(islandID[i,col_count-1]["node_ID"][k,4])
  BCsets["move_right"] = nodes

  if twoD:
    #BC3: Fixed top
    nodes = list()
    for j in range(col_count):
      for l in range(5):
        nodes.append(islandID[0,j]["node_ID"][0,l])
    BCsets["fixed_top"] = nodes

    #BC4: Fixed sides
    nodes = list()
    for i in range(row_count):
      for k in range(5):
        nodes.append(islandID[i,0]["node_ID"][k,0])
    for i in range(row_count):
      for k in range(5):
        nodes.append(islandID[i,col_count-1]["node_ID"][k,4])
    BCsets["fixed_sides"] = nodes

    #BC5: Move bottom
    nodes = list()
    for j in range(col_count):
      for l in range(5):
        nodes.append(islandID[row_count-1,j]["node_ID"][4,l])
    BCsets["move_bot"] = nodes

  # ------------- #
  #Define spring elements
  # ------------- #
  springCon = list()

  #Define horizontal springs 
  for i in range(row_count):
    for j in range(col_count-1):
      leftElm = islandID[i,j]["node_ID"][2,4]
      rightElm = islandID[i,j+1]["node_ID"][2,0]
      springCon.append((leftElm, rightElm))

  if twoD:
    # Define vertical springs
    for j in range(col_count):
      for i in range(row_count-1):
        upElm = islandID[i,j]["node_ID"][4,2]
        downElm = islandID[i+1,j]["node_ID"][0,2]
        springCon.append((upElm, downElm))

  return (nodePos, centerNodes, nodeCon, BCsets, springCon)
  
# if __name__ == '__main__':

  # ###Parameters### (all in mm)
  # #Stretched loc parameters
  # maxsize = 250.0 #Specify the longer edge length of the device when stretched (in mm)
  # roundbase = 3.0 #Base to round node locations (mm)

  # #Abaqus inp file parameters
  # col_count = 7
  # row_count = 9
  # nom_dist_btw_nodes = 2.4 #(mm)
  # node_edge_size = 2.512 #(mm)
  # ###Parameters End###

  # (island, islandID, long_stretch, short_stretch) = prepare_stretched_locs(maxsize, roundbase, col_count, row_count, nom_dist_btw_nodes, node_edge_size)
  # hor_island_dist, ver_island_dist = output_dist_btw_nodes(col_count, row_count, nom_dist_btw_nodes)
  # (nodePos, centerNodes, nodeCon, BCsets, springCon) = prepare_for_inp_file(hor_island_dist, ver_island_dist, island, islandID, col_count, row_count, node_edge_size)
  # pickle.dump(island, open("stretched_island_locs.p", "wb"))
