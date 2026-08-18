import sys, os
import gspread
import numpy as np
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
scriptpath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptpath)

def createK0LowHighCSVfromGsheets(filename):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('TanayProject-d3e99bb3360f.json', scope)
    client = gspread.authorize(creds)
    
    sh = client.open("combined_leg_analysis")
    wks = sh.worksheet("combined_k0_lowhigh")
    col_ct = 4

    exp_row = wks.find("Experiment #").row
    exp_col = wks.find("Experiment #").col
    experiments_str = wks.col_values(exp_col)
    experiments = list(map(int, experiments_str[exp_row:]))
    num_exps = len(experiments)

    leg_col = wks.find("leg_count").col
    displ_col = wks.find("displacement").col
    k0low_col = wks.find("nStiffness").col
    k0high_col = wks.find("nStiffnessMax").col

    header_names = [wks.col_values(leg_col)[0], wks.col_values(displ_col)[0], wks.col_values(k0low_col)[0], wks.col_values(k0high_col)[0]]
    
    leg_data = np.zeros((num_exps, col_ct))
    leg_data[:,0] = np.asarray(wks.col_values(leg_col)[1:]).astype(np.int32)
    leg_data[:,1] = np.asarray(wks.col_values(displ_col)[1:]).astype(np.float)
    leg_data[:,2] = np.asarray(wks.col_values(k0low_col)[1:]).astype(np.float)
    leg_data[:,3] = np.asarray(wks.col_values(k0high_col)[1:]).astype(np.float)
	
    df = pd.DataFrame(leg_data, columns=header_names)
    df.to_csv(filename)

if __name__ == "__main__":
    createK0LowHighCSVfromGsheets('try.csv')