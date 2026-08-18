import os
import pandas as pd
import glob

def importSerpentines(serpcount):
	importSerpentinesList = list()
	importSerpentinesList.append("from abaqusConstants import *")
	importSerpentinesList.append("")
	for i in range(serpcount):
		importSerpentinesList.append("session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)")
		importSerpentinesList.append("step = mdb.openStep(\'C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/{}.stp\', scaleFromFile=OFF)".format(i))
		importSerpentinesList.append("mdb.models[\'Onerow_Stretch\'].PartFromGeometryFile(name=\'P{}\', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)".format(i))
		importSerpentinesList.append("mdb.models[\'Onerow_Stretch\'].parts[\'P{}\'].Set(faces=mdb.models[\'Onerow_Stretch\'].parts[\'P{}\'].faces.getSequenceFromMask((\'[#ffffffff:5 ]\', ), ), name=\'Set-20\')".format(i,i))
		importSerpentinesList.append("mdb.models[\'Onerow_Stretch\'].parts[\'P{}\'].SectionAssignment(offset=0.0, offsetField=\'\', offsetType=MIDDLE_SURFACE, region=mdb.models[\'Onerow_Stretch\'].parts[\'P{}\'].sets[\'Set-20\'], sectionName=\'Sand_Sec\', thicknessAssignment=FROM_SECTION)".format(i,i))
	return importSerpentinesList

def getNtnDistances():
	fileLoc = os.path.dirname(os.path.abspath(__file__))+"/designFiles"
	os.chdir(fileLoc)
	filename = glob.glob("*.csv")[0]
	df = pd.read_csv (os.path.join(fileLoc,filename))
	ntnDistances = df.iloc[:, -3]*2
	return ntnDistances.tolist()

def getWireWidths():
	fileLoc = os.path.dirname (os.path.abspath (__file__)) + "/designFiles"
	os.chdir (fileLoc)
	filename = glob.glob ("*.csv")[0]
	df = pd.read_csv (os.path.join(fileLoc,filename))
	wireWidths = df.iloc[:, -2]
	return wireWidths.tolist ()

def assembleObjects(col_count, row_count, serpcount):
	ntnDistances = getNtnDistances()
	assembleSerpentinesList = list()
	offsetXnode, offsetYnode, offsetZnode = 1.2, 28.E-3, 1.2
	offsetXserp, offsetYserp, offsetZserp = 2.456, 0, -186.7E-3
	offsetXserp_vert, offsetYserp_vert, offsetZserp_vert = 1.248, 0, 1.1173
	verticalDistances = list()
	first_vert_spring = row_count*(col_count-1)
	for i in range(row_count-1):
		verticalDistances.append(ntnDistances[first_vert_spring+i])

	#Initially assemble nodes
	row = 0
	assembleSerpentinesList.append ("a = mdb.models[\'Onerow_Stretch\'].rootAssembly")
	for i in range(col_count*row_count):
		if i % col_count == 0 and i != 0:
			row += 1 #We moved one row down
		assembleSerpentinesList.append ("p = mdb.models[\'Onerow_Stretch\'].parts['NodeOnly']")
		assembleSerpentinesList.append ("a.Instance(name=\'NodeOnly-{}\', part=p, dependent=ON)".format(i))
		assembleSerpentinesList.append ("a = mdb.models[\'Onerow_Stretch\'].rootAssembly")
		assembleSerpentinesList.append ("a.rotate(instanceList=(\'NodeOnly-{}\', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)".format(i))
		moveamtXnode = offsetXnode + i % col_count * 2.512 + sum(ntnDistances[0:i % col_count])
		moveamtYnode = offsetYnode
		moveamtZnode = offsetZnode + i//col_count * 2.512 + sum(verticalDistances[:row])
		assembleSerpentinesList.append ("a.translate(instanceList=(\'NodeOnly-{}\', ), vector=({}, {}, {}))".format(i, moveamtXnode, moveamtYnode, moveamtZnode))
		assembleSerpentinesList.append ("a = mdb.models[\'Onerow_Stretch\'].rootAssembly")

	#Then assemble horizontal serpentines
	row = 0
	for i in range(row_count*(col_count-1)):
		if i % (col_count-1) == 0 and i != 0:
			row += 1 #We moved one row down
		assembleSerpentinesList.append ("p = mdb.models[\'Onerow_Stretch\'].parts[\'P{}\']".format(i))
		assembleSerpentinesList.append ("a.Instance(name=\'P{}-0\', part=p, dependent=ON)".format(i))
		moveamtXserp = offsetXserp + i % (col_count-1) * 2.512 + sum(ntnDistances[((i//(col_count-1))*(col_count-1)):i])
		moveamtYserp = offsetYserp
		moveamtZserp = offsetZserp + i // (col_count-1) * 2.512 + sum(verticalDistances[:row])
		assembleSerpentinesList.append ("a.translate(instanceList=(\'P{}-0\', ), vector=({}, {}, {}))".format(i, moveamtXserp, moveamtYserp, moveamtZserp))
		assembleSerpentinesList.append ("a = mdb.models[\'Onerow_Stretch\'].rootAssembly")

	#Then assemble vertical serpentines
	row = 0
	for count,j in enumerate(range(first_vert_spring, serpcount)):
		if count % (row_count-1) == 0:
			row = 0
		assembleSerpentinesList.append ("p = mdb.models[\'Onerow_Stretch\'].parts[\'P{}\']".format(j))
		assembleSerpentinesList.append ("a.Instance(name=\'P{}-0\', part=p, dependent=ON)".format(j))
		moveamtXserp_vert = offsetXserp_vert + count // (row_count-1) * 2.512 + sum(ntnDistances[:count//(row_count-1)])
		moveamtYserp_vert = offsetYserp_vert
		moveamtZserp_vert = offsetZserp_vert + count % (row_count-1) * 2.512 + sum(verticalDistances[:row])
		curXloc, curYloc, curZloc = moveamtXserp_vert, moveamtYserp_vert, moveamtZserp_vert + 1.3387
		assembleSerpentinesList.append ("a.translate(instanceList=(\'P{}-0\', ), vector=({}, {}, {}))".format(j, moveamtXserp_vert, moveamtYserp_vert, moveamtZserp_vert))
		assembleSerpentinesList.append ("a = mdb.models[\'Onerow_Stretch\'].rootAssembly")
		assembleSerpentinesList.append ("a.rotate(instanceList=(\'P{}-0\', ), axisPoint=({}, {}, {}), axisDirection=(0.0, -1.0, 0.0), angle=90.0)".format(j, curXloc, curYloc, curZloc))
		assembleSerpentinesList.append ("a = mdb.models[\'Onerow_Stretch\'].rootAssembly")
		row += 1

	return assembleSerpentinesList

def tieSerpentines(col_count, row_count, serpcount): #Currently only works for single row
	ntnDistances = getNtnDistances ()
	wireWidths = getWireWidths()
	tieSerpentinesList = list ()
	offsetXserp, offsetYserp, offsetZserp = 2.456, 0, 1.152
	offsetXserp_vert, offsetYserp_vert, offsetZserp_vert = 1.248, 0, 2.456
	verticalDistances = list()
	first_vert_spring = row_count*(col_count-1)
	for i in range(row_count-1):
		verticalDistances.append(ntnDistances[first_vert_spring+i])

	#First tie horizontal serpentines
	row = 0
	nodeid = 0
	for i in range(row_count*(col_count-1)):
		if i % (col_count-1) == 0 and i != 0:
			row += 1 #We moved one row down
			nodeid += 1
		#First left side of the serpentines
		serppos_x_left = offsetXserp + i % (col_count - 1) * 2.512 + sum (ntnDistances[((i // (col_count - 1)) * (col_count - 1)):i])
		serppos_y_left = offsetYserp
		serppos_z_left1 = offsetZserp + i // (col_count - 1) * 2.512 + sum(verticalDistances[:row]) + wireWidths[i]/2 - 0.0001
		serppos_z_left2 = offsetZserp + i // (col_count - 1) * 2.512 + sum(verticalDistances[:row]) + wireWidths[i]/2 + 0.0001
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_left_M\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'NodeOnly-{}\'].edges.findAt (coordinates = (({},{},{}),)))".format (i,nodeid,serppos_x_left,serppos_y_left,serppos_z_left1))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_left_S\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'P{}-0\'].edges.findAt (coordinates = (({},{},{}), ({},{},{}),)))".format (i, i, serppos_x_left, serppos_y_left, serppos_z_left1, serppos_x_left, serppos_y_left, serppos_z_left2))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].Tie(adjust=ON, master=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_left_M\'], name=\'Constraint-{}_left\', positionToleranceMethod=COMPUTED, slave=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_left_S\'],thickness=ON, tieRotations=ON)".format(i,i,i))
		
		#Then right side of the serpentines
		serppos_x_right = offsetXserp + i % (col_count - 1) * 2.512 + sum (ntnDistances[((i // (col_count - 1)) * (col_count - 1)):i]) + ntnDistances[i]
		serppos_y_right = offsetYserp
		serppos_z_right1 = offsetZserp + i // (col_count - 1) * 2.512 + sum(verticalDistances[:row]) + wireWidths[i]/2 - 0.0001
		serppos_z_right2 = offsetZserp + i // (col_count - 1) * 2.512 + sum(verticalDistances[:row]) + wireWidths[i]/2 + 0.0001
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_right_M\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'NodeOnly-{}\'].edges.findAt (coordinates = (({},{},{}),)))".format (i, nodeid+1, serppos_x_right, serppos_y_right, serppos_z_right1))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_right_S\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'P{}-0\'].edges.findAt (coordinates = (({},{},{}), ({},{},{},))))".format (i, i, serppos_x_right, serppos_y_right, serppos_z_right1, serppos_x_right, serppos_y_right, serppos_z_right2))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].Tie(adjust=ON, master=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_right_M\'], name=\'Constraint-{}_right\', positionToleranceMethod=COMPUTED, slave=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_right_S\'],thickness=ON, tieRotations=ON)".format(i,i,i))
		nodeid += 1
	#Then tie vertical serpentines
	row = 0
	nodeid = 0
	for count,i in enumerate(range(first_vert_spring, serpcount)):
		if count % (row_count-1) == 0:
			row = 0
			nodeid = count // (row_count-1)
		#First upper side of the serpentines
		serppos_x_up1 = offsetXserp_vert + count // (row_count-1) * 2.512 + sum(ntnDistances[:count//(row_count-1)]) - wireWidths[i]/2 - 0.0001
		serppos_x_up2 = offsetXserp_vert + count // (row_count-1) * 2.512 + sum(ntnDistances[:count//(row_count-1)]) - wireWidths[i]/2 + 0.0001
		serppos_y_up = offsetYserp_vert
		serppos_z_up = offsetZserp_vert + count % (row_count-1) * 2.512 + sum(verticalDistances[:row])
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_up_M\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'NodeOnly-{}\'].edges.findAt (coordinates = (({},{},{}),)))".format (i,nodeid,serppos_x_up1,serppos_y_up,serppos_z_up))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_up_S\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'P{}-0\'].edges.findAt (coordinates = (({},{},{}), ({},{},{}),)))".format (i, i, serppos_x_up1, serppos_y_up, serppos_z_up, serppos_x_up2, serppos_y_up, serppos_z_up))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].Tie(adjust=ON, master=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_up_M\'], name=\'Constraint-{}_up\', positionToleranceMethod=COMPUTED, slave=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_up_S\'],thickness=ON, tieRotations=ON)".format(i,i,i))

		#Then lower side of the serpentines
		serppos_x_low1 = offsetXserp_vert + count // (row_count-1) * 2.512 + sum(ntnDistances[:count//(row_count-1)]) - wireWidths[i]/2 - 0.0001
		serppos_x_low2 = offsetXserp_vert + count // (row_count-1) * 2.512 + sum(ntnDistances[:count//(row_count-1)]) - wireWidths[i]/2 + 0.0001
		serppos_y_low = offsetYserp_vert
		serppos_z_low = offsetZserp_vert + count % (row_count-1) * 2.512 + sum(verticalDistances[:row]) + ntnDistances[i]
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_low_M\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'NodeOnly-{}\'].edges.findAt (coordinates = (({},{},{}),)))".format (i,nodeid+col_count,serppos_x_low1,serppos_y_low,serppos_z_low))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].rootAssembly.Surface(name=\'serp_{}_low_S\',side1Edges=mdb.models[\'Onerow_Stretch\'].rootAssembly.instances[\'P{}-0\'].edges.findAt (coordinates = (({},{},{}), ({},{},{}),)))".format (i, i, serppos_x_low1, serppos_y_low, serppos_z_low, serppos_x_low2, serppos_y_low, serppos_z_low))
		tieSerpentinesList.append ("mdb.models[\'Onerow_Stretch\'].Tie(adjust=ON, master=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_low_M\'], name=\'Constraint-{}_low\', positionToleranceMethod=COMPUTED, slave=mdb.models[\'Onerow_Stretch\'].rootAssembly.surfaces[\'serp_{}_low_S\'],thickness=ON, tieRotations=ON)".format(i,i,i))
		row += 1
		nodeid += col_count
	return tieSerpentinesList

def meshSerpentines(): #Currently only works for single row
	meshFilesLoc = os.path.join(os.path.dirname(os.path.abspath (__file__)),"meshingScripts")
	meshSerpentinesList = list()
	for file in os.listdir (meshFilesLoc):
		filename = os.fsdecode (file)
		if filename[-3:] == ".py":
			line = "execfile('{}',__main__.__dict__)".format(os.path.join(meshFilesLoc,filename))
			line = line.replace ("7.2", "\\7.2")
			line = line.replace ("6_g", "\\6_g")
			meshSerpentinesList.append (line)
	return meshSerpentinesList


if __name__ == "__main__":
	col_count = 7 #Number of nodes, column-wise (default=7)
	row_count = 9 #Number of nodes, row-wise (default=9)
	serpcount = 110 #This is usually equal to: (col_count-1)*row_count + (row_count-1)*col_count. (default=110)
	# assemblyList = importSerpentines(serpcount) + assembleObjects(col_count, row_count, serpcount)
	assemblyList = importSerpentines (serpcount) + assembleObjects (col_count, row_count, serpcount) + tieSerpentines(col_count, row_count, serpcount) + meshSerpentines()

	with open("assemblyMacro.py", "w") as fo:
		for line in assemblyList:
			fo.writelines(line+"\n")
