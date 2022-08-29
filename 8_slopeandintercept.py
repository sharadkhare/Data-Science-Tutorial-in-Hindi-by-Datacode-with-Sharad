
import matplotlib.pyplot as plt
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x = 'Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()


# f(x) = 2x + 80
# as we see the average_pulse increases with 10, calorie_burnage increases by 20.
# slope = 20/10=2, the slope is 2.
# slope = f(x2) - f(x1) / x2-x1
# f(x2)= second observaton of calorie_burnage like 260
# f(x1) = first observation of calorie_burnage like 240
# x2 = second observaton of average_pulse = 90
# x1 = first observaton of average_pulse = 80
# slope = (260-240) / (90-80) = 2, the slope is 2

# how to use python to find the slope
def slope(x1, y1, x2, y2):
    s = (y2-y1) / (x2-x1)
    return s
print(slope(80, 240, 90, 260))

# how to find the intercept:
# here now after proper understanding we will now find the slope and the intercept using python:
# the np.polyfit() function returns the slope and the intercept.
import pandas as pd
import numpy as np
health_data = pd.read_csv("data.csv", header=0, sep=",")
x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)

#  now we can write the mathematical function
# f(x) = 2x + 80
# if we want to predict calorie burnage if the average pulse is 135
 # f(135) = 2 * 135 + 80 = 350
 # if the average pulse is 135 than the calorie burnage is 350
# now we will define it with mathematical function
def sharad_function(x):
    return 2*x + 80
print(sharad_function(135))


# now we will plot a new graph in python
import matplotlib.pyplot as plt
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x = 'Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0, ymax=400)
plt.xlim(xmin=0, xmax=150)
plt.show()

