""" Write fp explicict matrix for a single library """
import os
import pandas as pd
import numpy as np

from fp import FP

#csv_name = input("write database name: ")
#fp_name = input("write desired Fingerprint: ")
#output_name = input("write output name: ")

def write(csv_name, fp_name, output_name):
    fp_name = fp_name.replace(' ', '')
    result = FP(csv_name, fp_name).compute_asmatrix()
    result.to_csv(f"fp_matrix/{fp_name}/{output_name}")
    print("file ready")
    return result

write("BD_RHLR_Antagonistas.csv", "MACCS Keys", "BD_RHLR_Antagonistas_MACCS Keys.csv")    
write("BD_RHLR_Antagonistas.csv", "ECFP4", "BD_RHLR_Antagonistas_ECFP4.csv")
write("BD_RHLR_Antagonistas.csv", "ECFP6", "BD_RHLR_Antagonistas_ECFP6.csv")