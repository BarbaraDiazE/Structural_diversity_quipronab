import pandas as pd 

a = pd.read_csv('fp_matrix/ECFP6/BD_Inactivos_QS_ECFP6.csv', index_col = "Unnamed: 0")     
b = pd.read_csv('fp_matrix/ECFP6/BD_PQSR_Agonistas_ECFP6.csv', index_col = "Unnamed: 0")     
c = pd.read_csv('fp_matrix/ECFP6/BD_RHLR_Antagonistas_ECFP6.csv', index_col = "Unnamed: 0")
d = pd.read_csv('fp_matrix/ECFP6/BD_LASR_Agonistas_ECFP6.csv', index_col = "Unnamed: 0")     
e = pd.read_csv('fp_matrix/ECFP6/BD_PQSR_Antagonistas_ECFP6.csv', index_col = "Unnamed: 0")    
f = pd.read_csv('fp_matrix/ECFP6/BIOFACQUIM_ECFP6.csv', index_col = "Unnamed: 0")
g = pd.read_csv('fp_matrix/ECFP6/BD_LASR_Antagonistas_ECFP6.csv', index_col = "Unnamed: 0") 
h = pd.read_csv('fp_matrix/ECFP6/BD_QUIPRONAB_2020_ECFP6.csv', index_col = "Unnamed: 0")
i = pd.read_csv('fp_matrix/ECFP6/BD_NuBBE_ECFP6.csv', index_col = "Unnamed: 0")              
j = pd.read_csv('fp_matrix/ECFP6/BD_RHLR_Agonistas_ECFP6.csv', index_col = "Unnamed: 0")

frames = [a, b, c, d, e, f, g, h, i, j]
DF = pd.concat(frames, axis = 0).reset_index()
DF = DF.drop(["index"], axis = 1)
DF.to_csv("final_databases/Final_ECFP6_DB.csv")
print(DF.head())