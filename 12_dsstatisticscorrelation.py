# correlation: it measures the relationship between 2 variables.
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")

# input: x = (f(x))
# correlation Coefficient: it also measures the relationship between 2 variables. the correlation coefficient can never be less than -1 or higher than 1.
# 1 = perfect linear relationship
# 0 = no relationship
# -1 = perfect negative linear relationship. 

# lets take a example of a perfect linear relationship:
import matplotlib.pyplot as plt
health_data.plot(x= 'Average_Pulse', y='Calorie_Burnage', kind= 'scatter')
plt.show()

# now example of a perfect negative linear relationship (correlation coefficient = -1)

import pandas as pd
import matplotlib.pyplot as plt
negative_corr = {'Hours_work_before_training': [10,9,8,7,6,5,4,3,2,1], 'Calorie_Burnage': [220, 240, 260, 280, 300, 320, 340, 360, 380, 400 ]}
negative_corr = pd.DataFrame(data=negative_corr)
negative_corr.plot(x = 'Hours_work_before_training', y = 'Calorie_Burnage', kind='scatter')
plt.show()

# example of no linear relationship:

import matplotlib.pyplot as plt
health_data.plot(x = 'Duration', y='Max_Pulse', kind='scatter')
plt.show()