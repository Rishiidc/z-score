import pandas as pd
import plotly.express as pex
import numpy as np 

data = pd.read_csv("correlationData1.csv")
#graph = pex.scatter(data, x = "Temperature", y = "Ice-cream Sales( ₹ )")
correlation = np.corrcoef(data["Temperature"],data["Ice-cream Sales( ₹ )"])

print(correlation[0][1])
#graph.show()