1.-Compute fo explicit matrix for a single library
    a)Validate smiles (validate_smiles.py)
    b)run write_matrix.py (this file return  a database with explicit fp, and storage data in "fp_matrix" folder)

2.- Merge desired libraries
        a) run write_final_databases_MACCSKeys.py
        b) run write_final_databases_ECFP4.py
        c) run write_final_databases_ECFP6.py
        Final libraries are storaged at final_databases folder. 

3.- Perform tSNE:
        a) run TSNE.py for each Fingerprint. Results are storage at tSNE_results

4.- Plot
        a) set colors and libraries at plot.py
        b) call Plot class and visualize interactive plot at Plot_tSNE.ipynb