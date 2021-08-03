import pandas as pd
import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import statistics as stats
import random as r
import csv

data = pd.read_csv("average.csv")
data = data["average"].tolist()

populationMean = stats.mean(data)
populationsd = stats.stdev(data)

def takesample():
    samples = []
    for i in range(0,100):
        randomindex = r.randint(0,len(data)-1) 
        value = data[randomindex]
        samples.append(value)
    mean = stats.mean(samples)
    standardDeviation = stats.stdev(samples)
    return(mean)

def setup():
    meanlist = []
    for i in range(0,1000):
        value = takesample()
        meanlist.append(value)
    print("samplingmean")
    print(stats.mean(meanlist))
    print(stats.stdev(meanlist))
    graph_show(meanlist)

def graph_show(meanlist):
    data1 = meanlist
    graph2 = pff.create_distplot([data1],["b"],show_hist = False)
    graph2.show()

graph = pff.create_distplot([data],["h"],show_hist = False)
graph.add_trace(pgo.Scatter(x = [populationMean,populationMean],y = [0,2], mode = "lines", name = "populationMean"))

graph.show()
setup()
print(populationMean,populationsd)