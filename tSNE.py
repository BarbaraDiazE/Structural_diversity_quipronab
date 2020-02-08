"""
perform tSNE analysis
"""

import pandas as pd
import numpy as np

import sklearn
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE


class performTSNE:
    def __init__(self):
        pass

    def tsne_fingerprint(self, database, output):
        """
        Input:
            database: explicit fingerprint of numerated libraries
            output: file csv with tSNE results
        Output:
            result: DataFrame whit tSNE result
        """
        Data = pd.read_csv(f"final_databases/{database}", index_col="Unnamed: 0")
        fp_matrix = Data.select_dtypes(exclude=["object"]).as_matrix()
        model = TSNE(n_components=2, init="pca", random_state=1992, angle=0.3, perplexity=50
            ).fit_transform(fp_matrix)
        tsne_result = np.array(model)
        ref_id = Data.select_dtypes(include=["object"]).as_matrix()
        result = np.concatenate((tsne_result, ref_id), axis=1)
        result = pd.DataFrame(
            data=result, columns=["PC 1", "PC 2", "BD","ID"]
        )
        print(result.head())
        result.to_csv(f"tSNE_results/{output}")
        return result

performTSNE().tsne_fingerprint("Final_ECFP6_DB.csv", "result_TSNE_ECFP6.csv")