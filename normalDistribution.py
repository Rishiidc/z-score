import pandas as pd
import plotly.figure_factory as pff

data = pd.read_csv("HeightWeight.csv")
height = data["Height"].tolist()
graph = pff.create_distplot([height],["h"],show_hist = False)

graph.show()