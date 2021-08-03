import math 
import csv 
import pandas

data = pandas.read_csv("C:/Users/Rishi/Downloads/Python Intro/archive/indexHeightWeight.csv")

height = data["Height(Inches)"].tolist()
n = len(height)
sum = 0
for i in height:
    sum = sum + i
    
mean = sum/n
squarelist = []
for i in height:
    temp = i - mean
    temp = temp**2
    squarelist.append(temp)

sumsquare = 0
for i in squarelist:
    sumsquare = sumsquare + i 

result = sumsquare/n
standarddeviation = math.sqrt(result)

print(standarddeviation)
