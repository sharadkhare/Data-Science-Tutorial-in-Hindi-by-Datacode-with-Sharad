# what is variance: variance is just an another number that indicates how spread out the values are.:
# steps involved for calculating the variance.
# here we will find the variance of Average_pulse
# 1. we will find the mean:
# 80+85+90+95+100+105+110+115+120+125/ 10 = 105.5

# 2. we will find the difference from the mean for each value:
# 80-102.50 = -22.5
# 85-102.50 =-17.5 
# 90-102.50 =-12.5
# 95-102.50 =-7.5
# 100-102.50 =-2.5
# 105-102.50=2.5
# 110-102.50=7.5
# 115-102.50=12.5
# 120-102.50=17.5
# 125-102.50=22.5

# 3. now we will find the square value for each difference.
# -22.5^2 =-506.25
# -17.5^2 =-306.25
# -12.5^2 =-156.25
# -7.5^2 =-56.25
# -2.5^2 =-6.25
# 2.5^2 =6.25
# 7.5^2 =56.25
# 12.5^2 =156.25
# 17.5^2 =306.25
# 22.5^2 = 506.25

# 4. the variance is the average number of these squared values.
# for this we will sum the squared values and find the average.
# (506.25 + 306.25 + 156.25 + 56.25 + 6.25 + 6.25 + 56.25 + 156.25 + 306.25 + 506.25) / 10 = 206.25

# the variance is 206.25

import numpy as np
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")

sharadvar = np.var(health_data)
print(sharadvar)