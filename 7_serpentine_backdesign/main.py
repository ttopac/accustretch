import os
import pickle
import utils

import keras
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def extract_serpentine_model_OBSOLETE(wd): # Extract serpentine model (Run this function after designing new serpentines and fitting models to them
	all_stiff_coeffs_quad = dict()
	all_max_str_coeffs_quad = dict()
	for leg in (2,4,6,8,10):
		stiff_coeffs_quad, max_str_coeffs_quad = utils.extractQuadCoeffs(wd+"/rsm_files/{}leg_quad_NT2_v3_001_RF1.rsm".format(leg))
		all_stiff_coeffs_quad [leg] = tuple(stiff_coeffs_quad)
		all_max_str_coeffs_quad [leg] = tuple(max_str_coeffs_quad)
	pickle.dump(all_stiff_coeffs_quad, open("all_stiff_coeffs_quad_NT2_001_RF1_246810.p", "wb"))
	pickle.dump(all_max_str_coeffs_quad, open("all_max_str_coeffs_quad_NT2_001_RF1_246810.p", "wb"))

def extract_serpentine_model_wints(wd): # Extract serpentine model (Run this function after designing new serpentines and fitting models to them
	leg = 246
	all_stiff_coeffs_quad = dict()
	all_max_str_coeffs_quad = dict()
	stiff_coeffs_quad, max_str_coeffs_quad = utils.extractQuadCoeffs(wd+"/rsm_files/{}leg_designVSk0dMax_wleg_v4.rsm".format(leg))
	all_stiff_coeffs_quad [leg] = tuple(stiff_coeffs_quad)
	all_max_str_coeffs_quad [leg] = tuple(max_str_coeffs_quad)
	pickle.dump(all_stiff_coeffs_quad, open("integral_stiff_coeffs_quad_NT2_001_RF1_246v4.p", "wb"))
	pickle.dump(all_max_str_coeffs_quad, open("integral_max_str_coeffs_quad_NT2_001_RF1_246v4.p", "wb"))

def extract_objectives(wd, summaryFilename, first_useful_stiff_char, last_useful_stiff_char, first_useful_str_char, last_useful_str_char, first_useful_maxstr_char, last_useful_maxstr_char):
	# Extract objective stiffnesses (run this function after improving objective in Optimus surrogate analysis)
	# Params:
	# first_useful_stiff_char: Where stiffness values start in the second last line minus one (Python convention) (For nominal220: 168)
	# last_useful_stiff_char: Where stiffness values end in the second last line. (For nominal220: 2477)
	# first_useful_maxlin_char: Where maxlin values start in the last line minus one (Python convention) (For nominal220: 4738)
	# last_useful_maxlin_char: Where maxlin values start in the last line one. (For nominal220: -1)

	obj_stiffnesses = utils.extractObjStiffness(wd+"/summary_files/"+summaryFilename, first_useful_stiff_char, last_useful_stiff_char)
	pickle.dump(obj_stiffnesses, open("obj_stiffnesses_FinalNom_2D_feasReg_246_v5.p", "wb"))
	print ("First and last 2 objective stiffness values for verification. First 2 values: "+str(obj_stiffnesses[0:2]) + ", Last 2 values: "+str(obj_stiffnesses[-2:]))

	# Extract objective stretching requirement (run this function after improving objective in Optimus surrogate analysis)
	req_lin_str = utils.extractReqLinStr(wd+"/summary_files/"+summaryFilename, first_useful_str_char, last_useful_str_char)
	pickle.dump(req_lin_str, open("obj_req_str_FinalNom_2D_feasReg_246_v5.p", "wb"))
	print ("First and last 2 required stretch values for verification. First 2 values: "+str(req_lin_str[0:2]) + ", Last 2 values: "+str(req_lin_str[-2:]))

	obj_dmax = utils.extractObjDmax (wd + "/summary_files/" + summaryFilename, first_useful_maxstr_char, last_useful_maxstr_char)
	pickle.dump (obj_dmax, open ("obj_dmax_FinalNom_2D_feasReg_246_v5.p", "wb"))
	print ("First and last 2 objective dmax values for verification. First 2 values: " + str (obj_dmax[0:2]) + ", Last 2 values: " + str (obj_dmax[-2:]))

def getDmaxVsForceFromSurrogate (legs, useNNtoGetNonlinForce, fitPoly):
	num_springs = len(surr_stiffness)
	poly_order = 6
	surr_polycoeffs = np.zeros((num_springs, poly_order+1))

	for i in range(num_springs):
		dmax_disps = np.linspace(0,surr_dmax[i],11)
		dp_disps = np.linspace(0,surr_req_str[i],11)
		if useNNtoGetNonlinForce:
			estimator = keras.models.load_model (NN_model_path)
			test_sample = np.asarray ([surr_stiffness[i], surr_dmax[i]]).reshape (1, 2)
			test_sample_scaled = inp_scaler.transform (test_sample)
			scaled_nonlin_force = estimator.predict (test_sample_scaled)
			nonlin_force = out_scaler.inverse_transform (scaled_nonlin_force)
			nonlin_force = np.insert(nonlin_force, 0, 0)
		else: #Use quadratic model from Optimus to get nonlin_force DPs.
			nonlin_force = np.zeros(11)
			for j in range(10):
				nonlin_force[j+1] = FvsDmax_params[legs][j][0] + FvsDmax_params[legs][j][1]*surr_stiffness[i] + \
                     FvsDmax_params[legs][j][2] * surr_dmax[i] + FvsDmax_params[legs][j][3]*(surr_stiffness[i])**2 + \
                     FvsDmax_params[legs][j][4] * surr_dmax[i] * surr_stiffness[i] + FvsDmax_params[legs][j][5]*surr_dmax[i]*surr_dmax[i]
		if fitPoly:
			#Fit poly function for predicted surr_dmax, nonlin_force:
			model = make_pipeline(PolynomialFeatures(poly_order), LinearRegression())
			model.fit (dmax_disps.reshape(-1,1), nonlin_force.reshape(-1,1))
			LRparams = model.get_params()["linearregression"]
			surr_polycoeffs[i] = getattr(LRparams, "coef_")[0]
			dp_forces = model.predict(dp_disps.reshape(-1,1))

			# #Plots for testing
			# plt.figure (figsize=(5, 4))
			# plt.plot (dmax_disps, nonlin_force, 'b+')
			# plt.plot (dp_disps, dp_forces, 'r-')
			# plt.show ()

	return surr_polycoeffs

def OBSOLETEgetInitAndTerminalForceFromSurrogate(): #THIS FUNCTION IS OBSOLETE NOW!!! DONT USE
	num_springs = len(surr_stiffness)
	surr_DPs = np.zeros((2,num_springs))

	for i in range(num_springs):
		# dmax_space = np.linspace (0, surr_dmax[i], 11)
		# F_query = utils.find_nearest_left_idx (dmax_space, surr_req_str[i])
		F_term_ix = 2
		surr_DPs[0][i] = FvsDmax_params[68][0][0] + FvsDmax_params[68][0][1] * surr_stiffness[i] + \
		                 FvsDmax_params[68][0][2] * surr_dmax[i] + FvsDmax_params[68][0][3] * (surr_stiffness[i]) ** 2 + \
		                 FvsDmax_params[68][0][4] * surr_dmax[i] * surr_stiffness[i] + FvsDmax_params[68][0][5] * surr_dmax[i] * surr_dmax[i]

		surr_DPs[1][i] = FvsDmax_params[68][F_term_ix][0] + FvsDmax_params[68][F_term_ix][1] * surr_stiffness[i] + \
		                 FvsDmax_params[68][F_term_ix][2] * surr_dmax[i] + FvsDmax_params[68][F_term_ix][3] * (surr_stiffness[i]) ** 2 + \
		                 FvsDmax_params[68][F_term_ix][4] * surr_dmax[i] * surr_stiffness[i] + FvsDmax_params[68][F_term_ix][5] * surr_dmax[i] * surr_dmax[i]

	return surr_DPs

if __name__ == "__main__":
	# summaryFilename = "FinalNom_2D_feasReg_246_v5.summary"
	curpath = os.getcwd()
	# extract_serpentine_model(curpath) #(Run this function after designing new serpentines and fitting models to them
	# extract_serpentine_model_wints(curpath) #(Run this function after designing new serpentines and fitting models to them. Integers are integrated into the model.
	# extract_objectives(curpath,summaryFilename, first_useful_stiff_char=4696, last_useful_stiff_char=7004, first_useful_str_char=7300, last_useful_str_char=9608, first_useful_maxstr_char=2386, last_useful_maxstr_char=4694) #(run this function after improving objective in Optimus surrogate analysis)

	legs = 246
	surr_stiffness = pickle.load(open(os.path.join(curpath,"obj_stiffnesses_FinalNom_2D_feasReg_246_v5.p"), "rb"))
	surr_dmax = pickle.load(open(os.path.join(curpath,"obj_dmax_FinalNom_2D_feasReg_246_v5.p"), "rb"))
	surr_req_str = pickle.load(open(os.path.join(curpath,"obj_req_str_FinalNom_2D_feasReg_246_v5.p"), "rb"))
	inp_scaler = pickle.load (open (os.path.join (Path (__file__).parents[1], "nonlinearStiffness", "inp_scaler246_v4_wolegs.pkl"), 'rb'))
	out_scaler = pickle.load (open (os.path.join (Path (__file__).parents[1], "nonlinearStiffness", "out_scaler246_v4_wolegs.pkl"), 'rb'))
	FvsDmax_params = pickle.load (open (os.path.join (Path (__file__).parents[1], "nonlinearStiffness", "summary&model_files", 	"246leg_v4", "LH_quadmodel_RF1_v4.p"), 'rb'))
	NN_model_path = os.path.join(Path(__file__).parents[1], "nonlinearStiffness", "246leg_v4_NN_model_NT2_random_RF1_scaled_wolegs.h5")
	surr_polycoeffs = getDmaxVsForceFromSurrogate(legs, useNNtoGetNonlinForce=False, fitPoly=True) #We don't use NN here because our LH model is quite good.
	pickle.dump (surr_polycoeffs, open ("surr_polycoeffs_FinalNom_2D_feasReg_246_v5.p", "wb"))

