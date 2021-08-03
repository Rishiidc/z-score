import pandas as pd
import plotly.express as pex
import numpy as np

data = pd.read_csv("correlationData3.csv")
correlation = np.corrcoef(data["Roll No"], data["Marks In Percentage"])

print(correlation)