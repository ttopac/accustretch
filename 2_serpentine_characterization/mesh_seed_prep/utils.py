def createExcel (numleg, leg_to_arc, symmetry_dict, numpointsperarc=12, numpointsperarc_curveedge=16):
	numarcs = leg_to_arc[numleg]
	symmetry = symmetry_dict[numleg]
	excel_list = list ()
	for arc in range (numarcs):
		for point in range (1, numpointsperarc + 1):
			for coord in range (2):
				if coord == 0:
					excel_list.append ("PNT_{}_{}_XCOORD".format (arc, point))
				else:
					excel_list.append ("PNT_{}_{}_YCOORD".format (arc, point))
					excel_list.append ("PNT_{}_{}_ZCOORD".format (arc, point))
	if symmetry == True:
		excel_list.append ("PNT_MID_1_XCOORD")
		excel_list.append ("PNT_MID_1_YCOORD")
		excel_list.append ("PNT_MID_1_ZCOORD")
	#Added on Jun 2020 to include 1 node seed at curves for v4.
	for arc in range (numarcs):
		for point in range (1, numpointsperarc_curveedge + 1):
			for coord in range (2):
				if coord == 0:
					excel_list.append ("PNT_{}_{}_XCOORD_edge".format (arc, point))
				else:
					excel_list.append ("PNT_{}_{}_YCOORD_edge".format (arc, point))
					excel_list.append ("PNT_{}_{}_ZCOORD_edge".format (arc, point))
	return excel_list


def createPyScript (numleg, leg_to_arc, symmetry_dict, numpointsperarc=12, numpointsperarc_curveedge=16):
	numarcs = leg_to_arc[numleg]
	symmetry = symmetry_dict[numleg]
	pyscript_list = list ()
	pyscript_list.append ("    p = mdb.models['6leg_4split_triangle_MERGE_trim'].parts['P6_leg_4split_triangle_exp2']")
	pyscript_list.append ("    e = p.edges")
	for arc in range (numarcs):
		points_list = []
		for point in range (1, numpointsperarc + 1):
			points_list.append ("($PNT_{}_{}_XCOORD$, 0, $PNT_{}_{}_ZCOORD$), ".format (arc, point, arc, point))
		s = ""
		flatlist = s.join(points_list)
		pyscript_list.append ("    pickedEdges = e.getClosest (coordinates=({}))".format (flatlist))
		pyscript_list.append ("    edges_list = []")
		pyscript_list.append ("    for item in pickedEdges.values():")
		pyscript_list.append ("        edges_list.append(item[0])")
		pyscript_list.append ("    mytuple = tuple (edges_list)")
		if arc == 0 or arc == 1:
			pyscript_list.append ("    p.seedEdgeByNumber(edges=mytuple, number=16, constraint=FINER)")
		else:
			pyscript_list.append ("    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)")
		points_list = []
		for point in range (1, numpointsperarc_curveedge + 1):
			points_list.append ("($PNT_{}_{}_XCOORD_edge$, 0, $PNT_{}_{}_ZCOORD_edge$), ".format (arc, point, arc, point))
		s = ""
		flatlist = s.join (points_list)
		pyscript_list.append ("    pickedEdges = e.getClosest (coordinates=({}))".format (flatlist))
		pyscript_list.append ("    edges_list = []")
		pyscript_list.append ("    for item in pickedEdges.values():")
		pyscript_list.append ("        edges_list.append(item[0])")
		pyscript_list.append ("    mytuple = tuple (edges_list)")
		pyscript_list.append ("    p.seedEdgeByNumber(edges=mytuple, number=1, constraint=FINER)")

	if symmetry == True:
		# Process the symmetry now
		for arc in range (numarcs):
			points_list = []
			for point in range (1, numpointsperarc + 1):
				pyscript_list.append ("    distToSym_{} = $PNT_MID_1_XCOORD$ - $PNT_{}_{}_XCOORD$".format (point, arc, point))
				points_list.append ("($PNT_{}_{}_XCOORD$ + 2*distToSym_{}, 0, $PNT_{}_{}_ZCOORD$), ".format (arc, point, point, arc, point))
			s = ""
			flatlist = s.join(points_list)
			pyscript_list.append ("    pickedEdges = e.getClosest (coordinates=({}))".format (flatlist))
			pyscript_list.append ("    edges_list = []")
			pyscript_list.append ("    for item in pickedEdges.values():")
			pyscript_list.append ("        edges_list.append(item[0])")
			pyscript_list.append ("    mytuple = tuple (edges_list)")
			if arc == 0 or arc == 1:
				pyscript_list.append ("    p.seedEdgeByNumber(edges=mytuple, number=16, constraint=FINER)")
			else:
				pyscript_list.append ("    p.seedEdgeByNumber(edges=mytuple, number=32, constraint=FINER)")
			points_list = []
			for point in range (1, numpointsperarc_curveedge + 1):
				pyscript_list.append ("    distToSym_{} = $PNT_MID_1_XCOORD$ - $PNT_{}_{}_XCOORD_edge$".format (point, arc, point))
				points_list.append ("($PNT_{}_{}_XCOORD_edge$ + 2*distToSym_{}, 0, $PNT_{}_{}_ZCOORD_edge$), ".format (arc, point, point, arc, point))
			s = ""
			flatlist = s.join (points_list)
			pyscript_list.append ("    pickedEdges = e.getClosest (coordinates=({}))".format (flatlist))
			pyscript_list.append ("    edges_list = []")
			pyscript_list.append ("    for item in pickedEdges.values():")
			pyscript_list.append ("        edges_list.append(item[0])")
			pyscript_list.append ("    mytuple = tuple (edges_list)")
			pyscript_list.append ("    p.seedEdgeByNumber(edges=mytuple, number=1, constraint=FINER)")
	return pyscript_list


def write_file (list, filename):
	with open (filename, "w") as fo:
		for line in list:
			if not isinstance (line, str):
				line = str (line)
			fo.writelines (line + "\n")
