import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import time
filepath = os.path.dirname(os.path.abspath(__file__))
os.chdir(filepath)

def genSummaryLists (leg, forces, startind=0):
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('TanayProject-d3e99bb3360f.json', scope)
  client = gspread.authorize(creds)
  sh = client.open("{}leg_analysis".format(leg))
  wks = sh.worksheet("OptimusInp_v4_NT2_0.01")
  exp_col = wks.find("Exp. No").col
  exp_row = wks.find("Exp. No").row
  experiments_str = wks.col_values(exp_col)
  experiments = list(map(int, experiments_str[exp_row:]))
  row_offset_start = exp_row
  row_offset_end = row_offset_start + len(experiments)

  inputs = dict()
  outputs = dict()
  inputs ["leg count"] = leg

  angle_col = wks.find("Angle").col #Find the column containing angle
  ntn_length_half_col = wks.find("NTN_Dist").col #Find the column containing ntn length half
  stiffness_col = wks.find("nStiffness").col
  max_lin_stretch_col = wks.find("Max.Stretch").col
  forces_cols = list()
  if forces:
    for i in range(1, 11):
      forces_cols.append (wks.find("Force_{}".format(i)).col)

  variableLines = list()
  inputs ["bounding angle"] = list(map(float, wks.col_values(angle_col)[row_offset_start:row_offset_end]))
  inputs ["ntn length half"] = list(map(float, wks.col_values(ntn_length_half_col)[row_offset_start:row_offset_end]))
  outputs ["stiffness"] = list(map(float, wks.col_values(stiffness_col)[row_offset_start:row_offset_end]))
  outputs ["max. lin. stretch"] = list(map(float, wks.col_values(max_lin_stretch_col)[row_offset_start:row_offset_end]))
  if forces:
    for i in range(1,11):
      outputs["force_{}".format(float(i*0.1))] = list (map (float, wks.col_values (forces_cols[i-1])[row_offset_start:row_offset_end]))

  for i in range(len(experiments)):
    variableLines.append("{} 0 0 0 - 11 {} {} {} 0 0".format(startind+i+1, inputs["leg count"], inputs ["bounding angle"][i], inputs ["ntn length half"][i]))
    variableLines.append("{} 0 0 0 - 0 {} {} {} {} {}".format(startind+i+1, inputs["leg count"], inputs ["bounding angle"][i], inputs ["ntn length half"][i], outputs["stiffness"][i], outputs["max. lin. stretch"][i]))

  return variableLines, i

def genSummary (leg, ensemble=False, forces=False):
  fixedLines = list()
  fixedLines.append("OPTIMUS Rev 10 SUMMARY FILE\n0 Nominal\n3 Inputs\n2 Outputs\nDOE\n0 Objectives")
  fixedLines.append("Exp SubExp1 SubExp2 SubExp3 Annot Failed")
  fixedLines.append("\"leg count\" 1 0 -1 1")
  fixedLines.append("\"bounding angle\" 1 0 -1 1")
  fixedLines.append("\"ntn length half\" 1 0 -1 1")
  fixedLines.append("\"stiffness\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"max. lin. stretch\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")

  if ensemble == False:
    variableLines, _ = genSummaryLists(leg, forces)
    lines = fixedLines + variableLines
    filename = "{}leg_Sum_v4_NT2_001_RF1.summary".format(leg)
  elif ensemble == True:
    longlist = list()
    ind = 0
    for legno in leg:
      variableLines, endind = genSummaryLists(legno, startind=ind)
      ind += endind+1
      longlist.extend([k for k in variableLines])
      if legno == 7: time.sleep(200)
    lines = fixedLines + longlist
    filename = "ensemble_Sum_v4_NT2_001_RF1.summary"

  with open(filename, "w") as fo:
    for line in lines:
      if isinstance(line, str) == False:
        line = str(line)
      fo.writelines(line+"\n")

def genBackdesignSummaryLists (leg, startind=0):
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('TanayProject-d3e99bb3360f.json', scope)
  client = gspread.authorize(creds)
  sh = client.open("{}leg_analysis".format(leg))
  wks = sh.worksheet("OptimusInp_v4_NT2_0.01")
  exp_col = wks.find("Exp. No").col
  exp_row = wks.find("Exp. No").row
  experiments_str = wks.col_values(exp_col)
  experiments = list(map(int, experiments_str[exp_row:]))
  row_offset_start = exp_row
  row_offset_end = row_offset_start + len(experiments)

  inputs = dict()
  outputs = dict()
  inputs ["leg count"] = leg
  angle_col = wks.find("Angle").col #Find the column containing angle
  inputs ["bounding angle"] = list(map(float, wks.col_values(angle_col)[row_offset_start:row_offset_end]))
  ntn_length_half_col = wks.find("NTN_Dist").col #Find the column containing ntn length half
  inputs ["ntn length half"] = list(map(float, wks.col_values(ntn_length_half_col)[row_offset_start:row_offset_end]))

  num_arcs_perleg = {1:1, 2:1, 3:2, 4:2, 5:4, 6:3, 7:7, 8:4, 10:5, 12:6, 14:7} #numleg:numarcs
  variableLines = list()

  if leg == 7:
    for i in (1, 2, 3, 4, 32, 34, 24):
      arci_col = wks.find("Arc{}".format(i)).col
      outputs ["Arc{}".format(i)] = list(map(float, wks.col_values(arci_col)[row_offset_start:row_offset_end]))
    for i in range(len(experiments)):
      variableLines.append("{} 0 0 0 - 1111111 {} {} {} 0 0 0 0 0 0 0".format(startind+i+1, inputs["leg count"], inputs ["bounding angle"][i], inputs ["ntn length half"][i]))
      variableLines.append("{} 0 0 0 - 0 {} {} {} {} {} {} {} {} {} {}".format(startind+i+1, inputs["leg count"], inputs ["bounding angle"][i], inputs ["ntn length half"][i], outputs["Arc1"][i], outputs["Arc2"][i], outputs["Arc3"][i], outputs["Arc4"][i], outputs["Arc32"][i], outputs["Arc34"][i], outputs["Arc24"][i]))
  else:
    for i in range(num_arcs_perleg[leg]):
      arci_col = wks.find("Arc{}".format(i+1)).col
      outputs ["Arc{}".format(i+1)] = list(map(float, wks.col_values(arci_col)[row_offset_start:row_offset_end]))
    for i in range(num_arcs_perleg[leg], max(num_arcs_perleg.values())):
      outputs ["Arc{}".format(i+1)] = [0] * (row_offset_end-row_offset_start)

    for i in range(len(experiments)):
      variableLines.append("{} 0 0 0 - 1111111 {} {} {} 0 0 0 0 0 0 0".format(startind+i+1, inputs["leg count"], inputs ["bounding angle"][i], inputs ["ntn length half"][i]))
      variableLines.append("{} 0 0 0 - 0 {} {} {} {} {} {} {} {} {} {}".format(startind+i+1, inputs["leg count"], inputs ["bounding angle"][i], inputs ["ntn length half"][i], outputs["Arc1"][i], outputs["Arc2"][i], outputs["Arc3"][i], outputs["Arc4"][i], outputs["Arc5"][i], outputs["Arc6"][i], outputs["Arc7"][i]))

  return variableLines, i

def genBackdesignSummary (leg, ensemble=False):
  fixedLines = list()
  fixedLines.append("OPTIMUS Rev 10 SUMMARY FILE\n0 Nominal\n3 Inputs\n7 Outputs\nDOE\n0 Objectives")
  fixedLines.append("Exp SubExp1 SubExp2 SubExp3 Annot Failed")
  fixedLines.append("\"leg count\" 1 0 -1 1")
  fixedLines.append("\"bounding angle\" 1 0 -1 1")
  fixedLines.append("\"ntn length half\" 1 0 -1 1")
  fixedLines.append("\"Arc1\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"Arc2\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"Arc3\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"Arc4\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"Arc5\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"Arc6\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")
  fixedLines.append("\"Arc7\" 0  0.0000000000000e+00 0  0.0000000000000e+00 0 0 0 0 0  0.0000000000000e+00  0.0000000000000e+00  1.0000000000000e+00  1.0000000000000e-03")

  if not ensemble:
    variableLines, _ = genBackdesignSummaryLists(leg)
    lines = fixedLines + variableLines
    filename = "{}leg_BackdesignSum_v4_NT2_001.summary".format(leg)
  elif ensemble:
    longlist = list()
    ind = 0
    for legno in leg:
      variableLines, endind = genBackdesignSummaryLists(legno, startind=ind)
      ind += endind+1
      longlist.extend([k for k in variableLines])
      if legno == 6: time.sleep(200)
    lines = fixedLines + longlist
    filename = "ensemble_BackdesignSum_v4_NT2_001.summary"

  with open(filename, "w") as fo:
    for line in lines:
      if isinstance(line, str) == False:
        line = str(line)
      fo.writelines(line+"\n")
