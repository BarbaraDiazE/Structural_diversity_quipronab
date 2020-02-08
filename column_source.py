"""
column source, to allow bokeh plot
"""
import numpy as np
import bokeh
from bokeh.models import ColumnDataSource


def column_source(result, BD):
    """
    input:
        result (DataFrame)
        BD (str)
    Output:
        ColumnDataSource (bokeh object)
    """
    DF = result[result["BD"] == BD]
    X = np.array(DF["PC 1"])
    Y = np.array(DF["PC 2"])
    N = np.array(DF["ID"])
    return ColumnDataSource(dict(x=X, y=Y, N = N))
