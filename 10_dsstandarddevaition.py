# standard deviation: it is a number that describes how spread out the obeservations are : 
# a low SD means that most od the numbers are close to the mean or average value.
# a high SD means that the values are spread out over a wider range.
import numpy as np
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
sharadstd = np.std(health_data)
print(sharadstd)

# what does these output numbers means?
# coefficient of variation : it is used to just get an idea of how large the standard deviation is.
# mathematically you can say that. "coefficient of variation = standard deviation/mean"

import numpy as np
cov = np.std(health_data) / np.mean(health_data)
print(cov)

