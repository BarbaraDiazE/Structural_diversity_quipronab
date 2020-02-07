import pandas as pd
import numpy as np

import rdkit
from rdkit import Chem, DataStructs

#csv_name = input("write database name: ")

def validate_smiles(csv_name):
    Data = pd.read_csv(f'databases/{csv_name}')
    SMILES = Data.SMILES.tolist()
    ms = list()
    for i in range(Data.shape[0]):
        _ = Chem.MolFromSmiles(SMILES[i])
        if _:
            ms.append(_)
        else:
            print(i, SMILES[i])
            continue
    print("database smiles: ", Data.shape[0])
    print("identified smiles:", len(ms))
    return ms
    
validate_smiles("BD_RHLR_Antagonistas.csv")