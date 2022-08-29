# data science linear function: linear function has one independent variable (x) and one dependent vaiable (y) and has the below form:
# y = f(x) = ax + b..... this function used to calculate the dependent variable:
# y = the output
# x = input, independent varaible
# a = slope = is the coefficient of the independent variable, it gives the rate of the change of the dependent variable.
# b = intercept = is the value of the dependent variable.

# linear function with one explantory variable:we can use one variable for prediction.
# f(x) = ax + b
# f(x) = 2x + 80 
# f(x) = the output
# x = input which is average_pulse
# 2 = slope = specifies how much calorie_burnage increases if the average_pulse increase by 1
# 80 = intercept = a fixed value.

# data science - Plotting
# we can fisrt plot the values of average_pulse against calorie_burnage by using the matplotlib.

import matplotlib.pyplot as plt
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x = 'Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()