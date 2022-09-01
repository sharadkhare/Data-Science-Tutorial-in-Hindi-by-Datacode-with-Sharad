# introduction to statistics.: it means a science of analyzing data.
# descriptive statistics: 
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
print(health_data.describe())

# breifing of percentiles.
# here we will find the 10% percentile for max_pulse.
import numpy as np
Max_Pulse = health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
print(percentile10)