import utils

#v4: include 1 node seed at curves

if __name__ == "__main__":
	numleg = 10
	leg_to_arc = {8:6, 6:5, 4:4, 2:3, 10:7, 12:8, 1:4, 3:6, 5:8, 7:10, 14:9} #numleg:arc
	symmetry_dict = {1:False, 2:True, 3:False, 4:True, 5:False, 6:True, 7:False, 8:True, 10:True, 12:True, 14:True} #numleg:symmetry
	excel_list = utils.createExcel(numleg, leg_to_arc, symmetry_dict, numpointsperarc=3, numpointsperarc_curveedge=4)
	pyscript_list = utils.createPyScript(numleg, leg_to_arc, symmetry_dict, numpointsperarc=3, numpointsperarc_curveedge=4)

	utils.write_file(excel_list, "{}_leg_v4_CreoOutputs.csv".format(numleg))
	utils.write_file(pyscript_list, "{}_leg_v4_pyscript.py".format(numleg))
