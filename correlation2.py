import pandas as pd
import plotly.express as pex
import numpy as np

data = pd.read_csv("correlationData2.csv")
#graph = pex.scatter( data, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")
correlation = np.corrcoef(data["Size of TV"],data["Average time spent watching TV in a week (hours)"])

print(correlation)
#graph.show()