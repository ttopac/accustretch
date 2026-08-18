import pickle
import numpy as np
import os
import utils

if __name__ == "__main__":
	summary_filename = "LH_quadmodel_RF1_v4.rsm"
	summary_for_leg = 246810
	num_outputs = 10
	num_coeffs_peroutput = 6

	curpath = os.getcwd()
	summary_filepath = os.path.join(curpath,"summary&model_files","246810leg_v4",summary_filename)

	quad_model_params = utils.getQuadModelParamsfromOptSummary (summary_for_leg, summary_filepath, num_outputs, num_coeffs_peroutput)
	pickle.dump (quad_model_params, open (summary_filepath[:-4]+'.p', "wb"))
