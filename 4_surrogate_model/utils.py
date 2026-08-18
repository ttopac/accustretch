import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

def createSamplesCSVfromGsheets(leg, filename, k0type, multiLeg=False): #k0type = modeled or simulated
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('TanayProject-d3e99bb3360f.json', scope)
	client = gspread.authorize(creds)
	if multiLeg:
		sh = client.open("combined_leg_analysis")
		col_ct = 13
		wks = sh.worksheet("{}leg_random_results_v4".format(leg))
		leg_col = wks.find("leg_count").col
	else:
		sh = client.open("v3_NT2_randomTests")
		col_ct = 12
		wks = sh.worksheet("{}leg_new300LH_RF1_results".format(leg))

	stiffness_data = np.empty((1, col_ct))		
	exp_col = wks.find("Experiment #").col
	exp_row = wks.find("Experiment #").row
	experiments_str = wks.col_values(exp_col)
	experiments = list(map(int, experiments_str[exp_row:]))

	num_exps = len(experiments)
	k0_col = wks.find("k0_{}".format(k0type)).col
	displ_col = wks.find("displacement").col
	force_01_col = wks.find("Force_0.1").col

	leg_data = np.zeros((num_exps, col_ct))
	leg_data[:,0] = np.asarray(wks.col_values(k0_col)[1:]).astype(np.float)
	leg_data[:,1] = np.asarray(wks.col_values(displ_col)[1:]).astype(np.float)
	if multiLeg: leg_data[:,2] = np.asarray(wks.col_values(leg_col)[1:]).astype(np.float)
	for force in range(10):
		leg_data[:,col_ct-10+force] = np.asarray(wks.col_values(force_01_col+force)[1:]).astype(np.float)
	
	
	stiffness_data = np.append(stiffness_data, leg_data, axis=0)
	stiffness_data = np.delete(stiffness_data,0,0)
	np.savetxt(filename, stiffness_data, delimiter=',')

def getQuadModelParamsfromOptSummary(leg, summary_filepath, num_outputs, num_coeffs_peroutput):
	quad_model_params = dict()
	params_for_leg = np.zeros ((num_outputs, num_coeffs_peroutput))
	capture = False
	out_count = 0
	coeff_count = 0

	with open(summary_filepath, 'r') as f:
		line = f.readline()
		while line:
			if capture == True:
				data = float(line.split()[-1])
				params_for_leg[out_count][coeff_count] = data
				coeff_count += 1
			if coeff_count == num_coeffs_peroutput:
				coeff_count = 0
				capture = False
				out_count += 1
			if line == "  Model terms:\n":
				capture = True
			line = f.readline ()

	quad_model_params[leg] = params_for_leg
	return quad_model_params
