# Linear Regression.: the term regression is used when you try to find the relationship between variables.
# least Square Method: here the concept is to draw a line through all the plotted data points.here you will find the word "distance" which means residuals or errors.

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
health_data = pd.read_csv("data.csv", header=0, sep=",")
x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def sharadfunc(x):
    return slope * x + intercept

sharadmodel = list(map(sharadfunc, x))
plt.scatter(x,y)
plt.plot(x, slope * x + intercept)
plt.ylim(ymin= 0, ymax= 2000)
plt.xlim(xmin=0,xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show()
