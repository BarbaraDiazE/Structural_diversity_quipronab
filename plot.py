from bokeh.io import show, output_file
from bokeh.models import (
    ColumnDataSource,
    LassoSelectTool,
    ZoomInTool,
    ZoomOutTool,
    SaveTool,
    HoverTool,
    PanTool,
    Legend,
)
from bokeh.plotting import figure
from bokeh.core.enums import LegendLocation
import os
import pandas as pd
from column_source import column_source

"""
Plot chemical space
"""


class Plot:
    def __init__(self, result):
        self.result = pd.read_csv(f"tSNE_results/{result}", index_col = "Unnamed: 0")
        print(self.result.BD.unique())

    def plot_tsne(self, parameter):
        result = self.result
        source1 = column_source(result, 'INACTIVO' )
        source2 = column_source(result, 'PQSR-AGONISTA')
        source3 = column_source(result, 'RHLR-ANTAGONISTA')
        source4 = column_source(result, 'LASR-AGONISTA')
        source5 = column_source(result,'PQSR-ANTAGONISTA')
        source6 = column_source(result, 'BIOFACQUIM_V2')
        source7 = column_source(result, 'LASR-ANTAGONISTA')
        source8 = column_source(result, 'QUIPRONAB')
        source9 = column_source(result, 'NuBBE')
        source10 = column_source(result, 'RHLR-AGONISTA')
        hover = HoverTool(tooltips=[("PCA 1", "$x"), ("PCA 2", "$y"), ("NAME", "@N"),])
        p = figure(
            title="tSNE based on " + parameter,
            x_axis_label="PC 1",
            y_axis_label="PC 2",
            x_range=(-7, 7),
            y_range=(-7, 7),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        
        INACTIVO_plot = p.circle(x="x", y="y", source=source1, color="indigo", size=5)
        PQSR_AGONISTA_plot = p.circle(x="x", y="y", source=source2, color="hotpink", size=5)
        RHLR_ANTAGONISTA_plot = p.circle(x="x", y="y", source=source3, color="navy", size=5)
        LASR_AGONISTA_plot = p.circle(x="x", y="y", source=source4, color="dodgerblue", size=5)
        PQSR_ANTAGONISTA_plot = p.circle(
            x="x", y="y", source=source5, color="lightcoral", size=5)
        BIOFACQUIM_V2_plot = p.circle(x="x", y="y", source=source6, color="gold", size=5)
        LASR_ANTAGONISTA_plot = p.circle(
            x="x", y="y", source=source7, color="yellowgreen", size=5)
        QUIPRONAB_plot = p.circle(
            x="x", y="y", source=source8, color="green", size=5)
        NuBBE_plot = p.circle(
            x="x", y="y", source=source9, color="orangered", size=5)
        RHLR_AGONISTA_plot = p.circle(
            x="x", y="y", source=source10, color="mediumvioletred", size=5)
        legend = Legend(
            items=[
                ('INACTIVO'          ,[INACTIVO_plot]),
                ('PQSR-AGONISTA'     ,[PQSR_AGONISTA_plot]),
                ('RHLR-ANTAGONISTA'  ,[RHLR_ANTAGONISTA_plot]),
                ('LASR-AGONISTA'     ,[LASR_AGONISTA_plot]),
                ('PQSR-ANTAGONISTA'  ,[PQSR_ANTAGONISTA_plot]),
                ('BIOFACQUIM_V2'     ,[BIOFACQUIM_V2_plot]),
                ('LASR-ANTAGONISTA'  ,[LASR_ANTAGONISTA_plot]),
                ('QUIPRONAB'         ,[QUIPRONAB_plot]),
                ('NuBBE'             ,[NuBBE_plot]),
                ('RHLR-AGONISTA'     ,[RHLR_AGONISTA_plot]),
            ],
            location="center",
            orientation="vertical",
            click_policy="hide",
        )
        p.add_layout(legend, place="right")
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"

        show(p)

