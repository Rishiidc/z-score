import pandas as pd
import plotly.express as pex
import numpy as np

data = pd.read_csv("correlationData4.csv")
correlation = np.corrcoef(data["week"], data["Coffee in ml"])

print(correlation)