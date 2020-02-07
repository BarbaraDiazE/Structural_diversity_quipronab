"""Compute Fingerprint"""
import numpy as np
import pandas as pd
import itertools as it

import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.AtomPairs import Pairs

class FP:

    def __init__(self, csv_name, fp_name):
        self.fp_name = fp_name
        self.Data = pd.read_csv(f"databases/{csv_name}")
        _ = ["BD", "ID"]
        self.ref = self.Data[_]
        self.diccionario = {
            "MACCSKeys": self.maccskeys_fp(),
            "ECFP4": self.ecfp4_fp(),
            "ECFP6": self.ecfp6_fp(),
            "Topological": self.topological_fp(),
            "AtomPair": self.atom_pair_fp(),
        }

    def maccskeys_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [MACCSkeys.GenMACCSKeys(x) for x in ms]
        return fp

    def ecfp4_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x, 2) for x in ms]
        return fp

    def ecfp6_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [AllChem.GetMorganFingerprintAsBitVect(x, 3) for x in ms]
        return fp

    def topological_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [FingerprintMols.FingerprintMol(x) for x in ms]
        return fp

    def atom_pair_fp(self):
        ms = [Chem.MolFromSmiles(i) for i in self.Data.SMILES]
        fp = [Pairs.GetAtomPairFingerprintAsBitVect(x) for x in ms]
        return fp

    def fp_matrix(self, fp):
        matrix_fp = []
        for f in fp:
            arr = np.zeros((1,))
            DataStructs.ConvertToNumpyArray(f, arr)
            matrix_fp.append(arr)
        return matrix_fp

    def compute_asmatrix(self):
        fp = self.diccionario[self.fp_name]
        matrix_fp = self.fp_matrix(fp)
        matrix_fp = pd.DataFrame(data = matrix_fp)
        result = pd.concat([matrix_fp, self.ref], axis = 1)
        return result

    

   
