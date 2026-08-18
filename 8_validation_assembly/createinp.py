import numpy as np
import prepareData
import createSpringStiffness
from tensorflow import keras
import os


## Variable Text ##

def createNodePos (nodePos):
  nodePosText = list()
  nodePosText.append("*Part, name=MP")
  nodePosText.append("*Node")
  for node in nodePos:
    nodePosText.append(node)
  return nodePosText

def createElmConn (nodeCon):
  elmConnText = list()
  elmConnText.append("*Element, type=S4")
  for node in nodeCon:
    elmConnText.append(node)
  return elmConnText

def createBCSets (BCsets, nodePos, twoRow):
  BCSetsText = list()
  setID = 1
  setnames = list(BCsets.keys())
  for i in range(len(BCsets)):
    BCSetsText.append("*Nset, nset=SET-{}, instance=MP-1".format(setID))
    for j in range(len(BCsets[setnames[i]])):
      BCSetsText.append(int(BCsets[setnames[i]][j]))
    setID += 1

  if twoRow:
    BCSetsText.append("*Nset, nset=SET-{}, instance=MP-1, generate".format(setID))
    BCSetsText.append("1, {}, 1".format(len(nodePos)))
  else:
    BCSetsText.append ("*Nset, nset=SET-6, instance=MP-1, generate")
    BCSetsText.append ("1, {}, 1".format (len (nodePos)))

  return BCSetsText

def createCenterNodeSet (centerNodes):
  centerNodeSetText = list()
  centerNodeSetText.append("*Nset, nset=SET-CENTERNODES, instance=MP-1")
  for node in centerNodes:
    centerNodeSetText.append(node)
  return centerNodeSetText

def createSprings (springCon, stiffnesses, row_count, col_count, linear, nonlin_coeff_surrogate):
  #SpringCon has horizontal and then vertical springs
  springsText = list()
  for i in range(len(springCon)):
    if linear == True:
      springsText.append("*Spring, elset=SPRINGS/DASHPOTS-{}-SPRING-spring\n".format(i+1))
      springsText.append(stiffnesses[i])
    else:
      springsText.append ("*Spring, nonlinear, elset=SPRINGS/DASHPOTS-{}-SPRING-spring".format (i + 1))
      for displ in np.arange(0.0,25.0,0.025): #Here we discretize the nonlinear F-D plot from 0mm to 25mm with 0.25mm increments
        nonlin_force = displ * (float(stiffnesses[i]) + float(stiffnesses[i])*nonlin_coeff_surrogate*displ)
        if displ == 0.0:
          springsText.append ("0,0")
        else:
          springsText.append ("{},{}".format(displ, nonlin_force))
    springsText.append("*Element, type=SpringA, elset=SPRINGS/DASHPOTS-{}-SPRING-spring".format(i+1))
    springsText.append("{}, MP-1.{}, MP-1.{}".format(i+1,int(springCon[i][0]),int(springCon[i][1])))
  springsText.append("*End Assembly")
  return springsText

def createConnectorsAssembly (springCon):
  #SpringCon has horizontal and then vertical springs
  connectorsAssemblyText = list()
  for i in range(len(springCon)):
    connectorsAssemblyText.append ("*Element, type=CONN3D2")
    connectorsAssemblyText.append ("{}, MP-1.{}, MP-1.{}".format(i+1,int(springCon[i][0]),int(springCon[i][1])))
    connectorsAssemblyText.append ("*Connector Section, elset=Conns-{}, behavior=ConnSect-{}".format(i+1,i+1))
    connectorsAssemblyText.append ("Axial,")

  for i in range(len(springCon)):
    connectorsAssemblyText.append ("*Elset, elset=Conns-{}".format(i+1))
    connectorsAssemblyText.append ("{},".format(i+1))

  for i in range (len (springCon)):
    connectorsAssemblyText.append ("*Nset, nset=Wire-{}-Set-1, instance=MP-1".format(i+1))
    connectorsAssemblyText.append ("{} {}".format(int(springCon[i][0]),int(springCon[i][1])))
    connectorsAssemblyText.append ("*Elset, elset=Wire-{}-Set-1".format (i + 1))
    connectorsAssemblyText.append ("{}".format(i+1))
  connectorsAssemblyText.append("*End Assembly")
  return connectorsAssemblyText

def createConnectorsSections (springCon, stiffnesses, linear, nonlin_coeff_surrogate, use_simple_nonlin, FvsDmax_params, dmax_model_params,
                              use_NN, NN_model_path, inp_scaler, out_scaler, dmaxs, legs):
  multiLeg=True if len(legs) > 0 else False
  connectorsSectionsText = list()
  stiffnesses = stiffnesses.astype(float)
  dmaxs = dmaxs.astype(float)
  if multiLeg: legs=legs.astype(float).astype(int)

  nor_stiffnesses = stiffnesses

  #Calculate connector stiffnesses
  estimator = keras.models.load_model (NN_model_path) if use_NN else None
  for i in range(len(springCon)):
    connectorsSectionsText.append ("*Connector Behavior, name=ConnSect-{}".format(i+1))

    if linear == True:
      connectorsSectionsText.append ("*Connector Elasticity, component=1")
      connectorsSectionsText.append ("{},".format(stiffnesses[i]))
    else:
      connectorsSectionsText.append ("*Connector Elasticity, nonlinear, component=1")
      if use_simple_nonlin:
        for displ in np.arange (0.0, 25.0,0.25):  # Here we discretize the nonlinear F-D plot from 0mm to 25mm with 0.25mm increments
          nonlin_force = displ * (stiffnesses[i] + stiffnesses[i] * nonlin_coeff_surrogate * displ)
          connectorsSectionsText.append ("{}, {}".format (nonlin_force, displ))
      else: #Not using simple nonlin
        # dmax = dmax_model_params[8][0] + dmax_model_params[8][1]*nor_stiffnesses[i] + dmax_model_params[8][2]*nor_stiffnesses[i]**2
        if use_NN:
          if multiLeg:
            test_sample = np.asarray([nor_stiffnesses[i], dmaxs[i], legs[i]]).reshape(1, 3)
            connectorsSectionsText.append ("0.0, 0.0, 0.0")
          else:
            test_sample = np.asarray([nor_stiffnesses[i], dmaxs[i]]).reshape(1, 2)
            connectorsSectionsText.append ("0.0, 0.0")
          test_sample_scaled = inp_scaler.transform (test_sample)
          scaled_nonlin_force = estimator.predict (test_sample_scaled)
          nonlin_force = out_scaler.inverse_transform (scaled_nonlin_force)
          for j in range(1,11):
            connectorsSectionsText.append ("{}, {}".format (nonlin_force[0][j-1]*5000, dmaxs[i]*j/10))
          connectorsSectionsText.append ("{}, {}".format (nonlin_force[0][9]*15*5000, dmaxs[i]*2)) #Make it very stiff after its dmax region to avoid going beyond dmax.

        else: #Not using NN
          for count,displ in enumerate(np.linspace(0.0, dmaxs[i], 10)):
            nonlin_force = FvsDmax_params[8][count][0] + FvsDmax_params[8][count][1] * nor_stiffnesses[i] + \
                           FvsDmax_params[8][count][2] * dmaxs[i] + FvsDmax_params[8][count][3] * nor_stiffnesses[i]**2 + \
                           FvsDmax_params[8][count][4] * nor_stiffnesses[i] * dmaxs[i] + FvsDmax_params[8][count][5] * dmaxs[i]**2
            connectorsSectionsText.append ("{}, {}".format (nonlin_force, displ))

  return connectorsSectionsText

def createBCsStep1 (moveamt=7):
  BCsStep1Text = list()
  BCsStep1Text.append("*Boundary")
  BCsStep1Text.append("SET-2, 1, 1, {}".format(moveamt))
  BCsStep1Text.append("SET-2, 2, 2")
  BCsStep1Text.append("*Restart, write, frequency=0")
  BCsStep1Text.append("*Output, field, variable=PRESELECT")
  BCsStep1Text.append("*Output, field, number interval=1")
  BCsStep1Text.append("*Node Output, nset=SET-CENTERNODES")
  BCsStep1Text.append("COORD,")
  BCsStep1Text.append("*Output, history, variable=PRESELECT, frequency=1")
  BCsStep1Text.append("*End Step")
  return BCsStep1Text

def createBCsStep2 (moveamt=7):
  BCsStep2Text = list()
  BCsStep2Text.append("*Step, name=Step-2, nlgeom=YES, inc=800")
  BCsStep2Text.append("*Dynamic, application=QUASI-STATIC, initial=NO")
  BCsStep2Text.append("0.001,1.,1e-7")
  BCsStep2Text.append("*Boundary, op=NEW")
  BCsStep2Text.append("*Boundary, op=NEW")
  BCsStep2Text.append("*Boundary, op=NEW")
  BCsStep2Text.append("SET-3, 2, 2")
  BCsStep2Text.append("*Boundary, op=NEW, fixed")
  BCsStep2Text.append("SET-4, 1, 1")
  BCsStep2Text.append("*Boundary, op=NEW")
  BCsStep2Text.append("SET-5, 2, 2, -{}".format(moveamt))
  BCsStep2Text.append("*Restart, write, frequency=0")
  BCsStep2Text.append("*Output, field, variable=PRESELECT")
  BCsStep2Text.append("*Output, history, variable=PRESELECT, frequency=1")
  BCsStep2Text.append("*Output, field, frequency=99999")
  BCsStep2Text.append("*Node Output, nset=SET-CENTERNODES")
  BCsStep2Text.append("COORD,")
  BCsStep2Text.append("*End Step")
  return BCsStep2Text



### Fixed Text ###
def createHeader ():
  headerText = list()
  headerText.append("*Heading")
  headerText.append("** Job name: v1_auto_614 Model name: v1")
  headerText.append("** Generated by: Abaqus/CAE 6.14-1")
  headerText.append("*Preprint, echo=NO, model=NO, history=NO, contact=NO")
  return headerText

def createSections (nodePos, nodeCon):
  sectionsText = list()
  sectionsText.append("*Nset, nset=SET-1, generate")
  sectionsText.append("1, "+str(len(nodePos))+", 1")
  sectionsText.append("*Elset, elset=SET-1, generate")
  sectionsText.append("1, "+str(len(nodeCon))+", 1")
  sectionsText.append("** Section: Section-1-SET-1")
  sectionsText.append("*Shell Section, elset=SET-1, composite")
  sectionsText.append ("0.014, 3, PI-2611, 0., TOP-2611")
  sectionsText.append ("0.001, 3, PI-2545, 0., TOP-2545")
  sectionsText.append ("0.0002, 3, GOLD, 0., GOLD")
  sectionsText.append ("0.001, 3, PI-2545, 0., BOT-2545")
  sectionsText.append ("0.014, 3, PI-2611, 0., BOT-2611")
  sectionsText.append("*End Part")
  return sectionsText

def createAssembly ():
  assemblyText = list()
  assemblyText.append("*Assembly, name=Assembly")
  assemblyText.append("*Instance, name=MP-1, part=MP")
  assemblyText.append("*End Instance")
  return assemblyText

def createMat ():
  materialText = list()
  materialText.append ("*Material, name=GOLD")
  materialText.append ("*Density")
  materialText.append ("1.42e-09,")
  materialText.append ("*Elastic")
  materialText.append ("54000., 0.4")
  materialText.append("*Material, name=MATERIAL-1")
  materialText.append("*Density")
  materialText.append("0.0001,")
  materialText.append("*Elastic")
  materialText.append("1e+06, 0.3")
  materialText.append ("*Material, name=PI-2545")
  materialText.append ("*Density")
  materialText.append ("1.42e-09,")
  materialText.append ("*Elastic")
  materialText.append ("2300., 0.34")
  materialText.append ("*Material, name=PI-2611")
  materialText.append ("*Density")
  materialText.append ("1.4e-09,")
  materialText.append ("*Elastic")
  materialText.append ("8000., 0.34")
  return materialText

def createBCsFixed ():
  BCsFixedText = list()
  BCsFixedText.append("*Boundary")
  BCsFixedText.append("SET-6, 3, 3")
  BCsFixedText.append("*Boundary")
  BCsFixedText.append("SET-1, 1, 1")
  BCsFixedText.append("*Boundary")
  BCsFixedText.append("SET-1, 2, 2")
  return BCsFixedText

def createStep1 ():
  step1Text = list()
  step1Text.append("*Step, name=Step-1, nlgeom=YES, inc=800")
  step1Text.append("*Dynamic, application=QUASI-STATIC, initial=NO")
  step1Text.append("0.001,1.,1e-7")
  return step1Text


def createFile(nodePos, centerNodes, nodeCon, BCsets, movelong, moveshort, row_count, col_count, springCon, stiffFile, twoRow, linear,
               nonlin_coeff_surrogate, useConnectors, use_simple_nonlin, FvsDmax_params, dmax_model_params, use_NN, NN_model_path, inp_scaler, out_scaler, dmax_file, legs_file=None):
  flatten = lambda l: [item for sublist in l for item in sublist]
  inplist = list()

  header = createHeader()
  nodepos = createNodePos(nodePos)
  elmconn = createElmConn(nodeCon)
  sections = createSections(nodePos, nodeCon)
  assembly = createAssembly()
  bcsets = createBCSets(BCsets, nodePos, twoRow)
  centernodeset = createCenterNodeSet (centerNodes)

  stiffnesses = createSpringStiffness.createStiffnesses(row_count, col_count, stiffFile)
  dmaxs = createSpringStiffness.createDmax(dmax_file)
  legs = createSpringStiffness.createLegs(legs_file)
  springs = createSprings(springCon, stiffnesses, row_count, col_count, linear, nonlin_coeff_surrogate)
  connectorAssm = createConnectorsAssembly(springCon)
  connectorSect = createConnectorsSections(springCon,stiffnesses,linear,nonlin_coeff_surrogate, use_simple_nonlin, FvsDmax_params,
                                           dmax_model_params, use_NN, NN_model_path, inp_scaler, out_scaler, dmaxs, legs)

  materials = createMat()
  bcsfixed = createBCsFixed()
  step1 = createStep1()

  if twoRow:
    bcsstep1 = createBCsStep1(moveshort)
    bcsstep2 = createBCsStep2(movelong)
  else:
    bcsstep1 = createBCsStep1 (movelong)

  if not useConnectors:
    if twoRow:
      inplist.append((header, nodepos, elmconn, sections, assembly, bcsets, centernodeset, springs,
                       materials, bcsfixed, step1, bcsstep1, bcsstep2))
    else:
      inplist.append ((header, nodepos, elmconn, sections, assembly, bcsets, centernodeset, springs,
                       materials, bcsfixed, step1, bcsstep1))
  else:
    if twoRow:
      inplist.append ((header, nodepos, elmconn, sections, assembly, bcsets, centernodeset, connectorAssm, connectorSect,
                       materials, bcsfixed, step1, bcsstep1, bcsstep2))
    else:
      inplist.append ((header, nodepos, elmconn, sections, assembly, bcsets, centernodeset, connectorAssm, connectorSect,
                       materials, bcsfixed, step1, bcsstep1))

  inplist = flatten(inplist)
  inplist = flatten(inplist)

  with open("autoinp.inp", "w") as fo:
    for line in inplist:
      if isinstance(line, str) == False:
        line = str(line)
      fo.writelines(line+"\n")
