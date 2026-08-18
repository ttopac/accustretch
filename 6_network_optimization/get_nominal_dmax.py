import main
import prepareData
import os
from pathlib import Path
import math

def get_obj_stretches ():
	node_loc = os.path.join (Path (__file__).parents[1], "PhotoshopFiles", "Stanford5.psd.txt")
	(maxsize, roundbase, col_count, row_count, twoRow, nom_dist_btw_nodes, node_edge_size) = main.getParams ()
	(island, islandID, long_stretch, short_stretch) = prepareData.prepare_stretched_locs (maxsize, roundbase, col_count, row_count, nom_dist_btw_nodes, node_edge_size, node_loc, twoRow)
	obj_stretches = list()

	#First traverse across horizontal serpentines
	for row in range(row_count): #9
		for col in range(col_count-1): #7
			left_island = row * col_count + col
			right_island = left_island + 1
			xdist_stretched = island[right_island]["str_mm"][0] - island[left_island]["str_mm"][0] - node_edge_size
			ydist_stretched = island[right_island]["str_mm"][1] - island[left_island]["str_mm"][1]
			dist_stretched = math.sqrt(xdist_stretched**2 + ydist_stretched**2)
			dist_expanded = dist_stretched - nom_dist_btw_nodes
			obj_stretches.append(dist_expanded)

	#Then traverse across vertical serpentines. Down and then right.
	for col in range(col_count): #7
		for row in range(row_count-1): #9
			top_island = row * col_count + col
			bottom_island = top_island + col_count
			xdist_stretched = island[bottom_island]["str_mm"][0] - island[top_island]["str_mm"][0]
			ydist_stretched = island[bottom_island]["str_mm"][1] - island[top_island]["str_mm"][1] - node_edge_size
			dist_stretched = math.sqrt (xdist_stretched ** 2 + ydist_stretched ** 2)
			dist_expanded = dist_stretched - nom_dist_btw_nodes
			obj_stretches.append (dist_expanded)

	return obj_stretches


def get_nominal_dmax_list (min_dmax, max_dmax):
	#We essentially normalize obj_stretches to min_dmax, max_dmax range
	nominal_dmax_list = list()
	for obj_stretch in obj_stretches:
		nom_dmax = (max_dmax - min_dmax) * (obj_stretch - min(obj_stretches)) / (max(obj_stretches) - min(obj_stretches)) + min_dmax
		nominal_dmax_list.append(nom_dmax)
	return nominal_dmax_list

if __name__ == '__main__':
	obj_stretches = get_obj_stretches()
	nominal_dmax_list = get_nominal_dmax_list(min_dmax=20, max_dmax=26)

	with open("nominal_dmax_list.csv","w") as f:
		for i in range(len(nominal_dmax_list)):
			f.write(str(nominal_dmax_list[i])+"\n")
