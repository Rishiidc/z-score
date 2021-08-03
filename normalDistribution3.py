import random as r
import plotly.figure_factory as pff

dice = []
for i in range(0,100):
    d1 = r.randint(1,6)
    d2 = r.randint(1,6)
    dice.append(d1+d2)

graph = pff.create_distplot([dice],["d"], show_hist = False)

graph.show()