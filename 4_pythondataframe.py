# python Dataframe.: 
# how to create a Data frame with pandas: 3 col and 5 rows
import pandas as pd
sharad = {'col1': [1,2,3,4,7], 'col2': [4,5,6,9,5], 'col3':[7,8,12,1,11]}
sharaddf = pd.DataFrame(data=sharad)
print(sharaddf)

# here we can use python to count the col and rows, for this we can use sharaddf[1] to find the numbers of columns
newsharad = sharaddf.shape[1]
print("the number of columns is : ", newsharad)

# for this we can use sharaddf[0] to find the numbers of rows
sharadrows = sharaddf.shape[0]
print("the number of rows is : ", sharadrows)