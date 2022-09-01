# Correlation matrix: it is simply a table showing the correlation coefficients between the variables.
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
corr_matrix = round(health_data.corr(), 2)
print(corr_matrix)

# here we can use the seaborn library to create a correlation heatmap:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
health_data = pd.read_csv("data.csv", header=0, sep=",")
sharadhealthdata = health_data.corr()
axis_corr = sns.heatmap(sharadhealthdata, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(50, 500, n=500), square=True)
plt.show()