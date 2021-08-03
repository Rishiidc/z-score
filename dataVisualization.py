import pandas
import plotly.express as px

data = pandas.read_csv("data.csv")
graph = px.line(data,x="Country",y="InternetUsers",title = "InternetUsers")
graph.show()

graph2 = px.bar(data,x = "Country", y = "InternetUsers", title = "Bar Graph")
graph2.show() 

graph3 = px.scatter(data, x = "Country", y = "InternetUsers", title = "Scatter plot", size = "InternetUsers", color = "Country", size_max = 20 )
graph3.show()