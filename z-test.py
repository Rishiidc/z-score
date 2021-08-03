import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import statistics as stats
import random 
import pandas as pd
import csv

data = pd.read_csv("Mathscores.csv")
data1 = data["mathscores"].tolist()

mean = stats.mean(data1)
standardDeviation = stats.stdev(data1)

def randommean():
    meanset = []
    for i in range(0,100):
        randomindex = random.randint(0,len(data)-1)
        value = data1[randomindex]
        meanset.append(value)
    mean_sample = stats.mean(meanset)
    return mean_sample
    
meanlist = []
for i in range(0,1000):
    mean_sample = randommean()
    meanlist.append(mean_sample)

samplingmean = stats.mean(meanlist)
samplingsd = stats.stdev(meanlist)
sdstart,sdend = samplingmean - samplingsd, samplingmean + samplingsd
ssdstart,ssdend = samplingmean - 2*samplingsd, samplingmean + 2*samplingsd
tsdstart,tsdend = samplingmean - 3*samplingsd, samplingmean + 3*samplingsd
graph = pff.create_distplot([meanlist],["Scores"], show_hist = False)

intervention1 = pd.read_csv("Studentinterventions1.csv")
i1 = intervention1["math_score"].tolist()

i1mean = stats.mean(i1)

zscore = (i1mean - samplingmean)/samplingsd

intervention2 = pd.read_csv("Studentinterventions2.csv")
i2 = intervention1["math_score"].tolist()

i2mean = stats.mean(i2)

zscore1 = (i2mean - samplingmean)/samplingsd

#graph.show()
print(mean,standardDeviation)
print(samplingmean,samplingsd)
print(zscore,zscore1)