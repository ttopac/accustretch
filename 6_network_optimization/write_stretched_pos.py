import numpy as np
import utils
import prepareData
import sys
import main
import os
from pathlib import Path

nodeLoc = sys.argv[1]
axis = sys.argv[2]

# nodeLoc = os.path.join(Path(__file__).parents[1], "PhotoshopFiles", "Stanford5.psd.txt")
# axis = "x"

if __name__ == "__main__":
	(maxsize, roundbase, col_count, row_count, twoRow, nom_dist_btw_nodes, node_edge_size) = main.getParams()
	(island, islandID, long_stretch, short_stretch) = prepareData.prepare_stretched_locs(maxsize, roundbase, col_count, row_count, nom_dist_btw_nodes, node_edge_size, nodeLoc, twoRow)
	utils.write_stretch_pos_optimus (axis, islandID, row_count, col_count)
