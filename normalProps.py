import pandas as pd 
import statistics as stats 
import plotly.figure_factory as pff 

data = pd.read_csv("HeightWeight.csv")
height = data["Height"].tolist()

mean = stats.mean(height)
mode = stats.mode(height)
standardDeviation = stats.stdev(height)

fsdstart,fsdend = mean - standardDeviation, mean + standardDeviation
region1data = [result for result in height if fsdstart<result<fsdend]

ssdstart = mean - 2*standardDeviation
ssdend = mean + 2*standardDeviation
region2data = [result2 for result2 in height if ssdstart<result2<ssdend]

tsdstart = mean - 3*standardDeviation
tsdend = mean + 3*standardDeviation
region3data = [result3 for result3 in height if tsdstart<result3<tsdend]

graph = pff.create_distplot([height],["h"], show_hist = False)

print(fsdstart,fsdend)
print(mean,mode,standardDeviation)
print(len(region1data)/len(height))
print(len(region2data)/len(height))
print(len(region3data)/len(height))
print("{} of data is in first region".format(len(region1data)/len(height)))