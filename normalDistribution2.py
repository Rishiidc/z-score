import pandas as pd
import plotly.figure_factory as pff

data = pd.read_csv("HeightWeight.csv")
weight = data["Weight(Pounds)"].tolist()
graph = pff.create_distplot([weight],["w"],show_hist = False)

graph.show()