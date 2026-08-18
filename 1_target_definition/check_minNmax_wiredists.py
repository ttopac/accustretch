import sys, os
import math
import numpy as np
scriptpath = os.path.realpath(os.path.dirname(sys.argv[0]))
parentpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
os.chdir(scriptpath)
sys.path.append("../generateSerpentines")
import prepareData

def get_stretched_wire_lengths(island):
    hor_wire_dist = list()
    ver_wire_dist = list()
    
    count = 0
    for i in range(row_count): #Get horizontal wire distances. First right then down.
        for j in range(col_count):
            if (count+1) % col_count != 0:
                hor_island_dist_x = island[count+1]['str_mm'][0] - island[count]['str_mm'][0]
                hor_island_dist_y = island[count+1]['str_mm'][1] - island[count]['str_mm'][1]
                hor_wire_dist.append (math.sqrt(hor_island_dist_x**2 + hor_island_dist_y**2))
            else:
                pass
            count += 1
    
    for i in range(col_count): #Get vertical wire distances. First down then right.
        for j in range(row_count-1):
            ver_island_dist_x = island[col_count*(j+1)+i]['str_mm'][0] - island[col_count*j+i]['str_mm'][0]
            ver_island_dist_y = island[col_count*(j+1)+i]['str_mm'][1] - island[col_count*j+i]['str_mm'][1]
            ver_wire_dist.append (math.sqrt(ver_island_dist_x**2 + ver_island_dist_y**2))
    
    return (hor_wire_dist, ver_wire_dist)



if __name__ == '__main__':
    roundbase = 1.0
    node_edge_size = 2.512 #(mm)
    nom_dist_btw_nodes = 2.4 #(mm) Change based on average size of allowed legs.
    col_count = 7 #7
    row_count = 9 #9
    twoD = False if row_count == 1 else True
    maxsize = 83.3 if twoD else 60.2 #Note that this is the distance from center to center. Total size will be 2.512mm larger than this.
    use_dists_from_photoshop = False
    nodeLoc_photoshop = parentpath+"/1_PhotoshopFiles/Stanford5.psd.txt"
    nodeLocX_abaqus = parentpath+"/99_ResultsFiles/12.2_2D_feasReg_246/v5/1_AbaqusFiles/x_coords_end.txt"
    nodeLocY_abaqus = parentpath+"/99_ResultsFiles/12.2_2D_feasReg_246/v5/1_AbaqusFiles/y_coords_end.txt"


    if use_dists_from_photoshop:
        (island, islandID, long_stretch, short_stretch) = prepareData.prepare_stretched_locs_fromphotoshop(maxsize, roundbase, col_count, row_count, nom_dist_btw_nodes, node_edge_size, nodeLoc_photoshop, twoD)
    else:
        island = prepareData.prepare_stretched_locs_fromabaqsurr(nodeLocX_abaqus, nodeLocY_abaqus)
    (hor_wires, ver_wires) = get_stretched_wire_lengths(island)


    hor_maxs = np.zeros(col_count-1) #This will contain col_count-1 elements, indicating max distances at each column-wise horizontal wire.
    ver_maxs = np.zeros(row_count-1) #This will contain row_count-1 elements, indicating max distances at each row-wise vertical wire.
    
    for i, hor_wire in enumerate(hor_wires):
        col = i%(col_count-1)
        if hor_wire > hor_maxs[col]:
            hor_maxs[col] = hor_wire
    for i, ver_wire in enumerate(ver_wires):
        row = i%(row_count-1)
        if ver_wire > ver_maxs[row]:
            ver_maxs[row] = ver_wire

    for i in range(col_count-1):
        print ("Maximum length horizontal wire in column {} is {}mm.".format(i, hor_maxs[i]-node_edge_size))
    for i in range(row_count-1):
        print ("Maximum length vertical wire in row {} is {}mm.".format(i, ver_maxs[i]-node_edge_size))