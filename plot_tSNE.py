from plot import Plot

Plot("result_TSNE_MACCSKeys.csv").plot_tsne("MACCS Keys")

#plot ECFP4 results
Plot("result_TSNE_ECFP4.csv").plot_tsne("ECFP4")

#plot ECFP6 results
Plot("result_TSNE_ECFP6.csv").plot_tsne("ECFP6")