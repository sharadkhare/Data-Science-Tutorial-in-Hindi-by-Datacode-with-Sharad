# how to extract and read the data with pandas.
import pandas as pd
health_data = pd.read_csv("dirtydata.csv", header=0, sep=",")
print(health_data)

# if you have a large csv file than you can use the head() function to show upto 5 rows.
import pandas as pd
health_data = pd.read_csv("dirtydata.csv", header=0, sep=",")
print(health_data.head())

# how to do data cleaning
# here we will remove the blank rows
import pandas as pd
health_data = pd.read_csv("dirtydata.csv", header=0, sep=",")

health_data.dropna(axis=0, inplace=True)
print(health_data)

# briefing about data category
# data can be split into three main categories: numerical: discreateand continuos.
# categorical: it contains the values that cannot be up against each other like groups.
# ordinal: like schol grades where A is better than B (related to each other)
# how to check the data type:
print(health_data.info())

# here we will convert the "average_pulse" and "max_pulse" into float64.
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data['Max_Pulse'].astype(float)
print(health_data.info())

# how to analyze the data:
# now we can use describe() function in python for summarize data:
print(health_data.describe())
