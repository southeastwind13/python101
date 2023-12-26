import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Quantiles also call percentiles, split up the data into some number of qual parts

'''

file_path = 'StatisticsInPython/Iris.csv'
df = pd.read_csv(file_path)

'''
quantiles 0.5 = median
'''
print(df['SepalLengthCm'].median())
print(df['SepalLengthCm'].quantile(0.5))
print()

'''
Get multiple quantiles at once
'''
print(df['SepalLengthCm'].quantile([0.1, 0.3, 0.5, 0.7, 1.0]))
print(df['SepalLengthCm'].quantile(np.linspace(0,1,6)))
print()

'''
Box plot use quantiles
Top: Q3
Middle line: Q2
Bottom: Q1
'''

'''
Interquartile range (IQR)

It is distance between 25th and 75th percentile, which is also he height of the box in the boxplot.
'''
iqr = df['SepalLengthCm'].quantile(0.75) - df['SepalLengthCm'].quantile(0.25)
print(iqr)
print()

'''
Outlier
1. data < Q1-1.5iqr 
2. data > Q3+1.5iqr
'''

from scipy.stats import iqr
iqr = iqr( df['SepalWidthCm'])
lower_treshold = df['SepalWidthCm'].quantile(0.25) - (1.5*iqr)
upper_treshold = df['SepalWidthCm'].quantile(0.75) + (1.5*iqr)

print(df[(df['SepalWidthCm']<lower_treshold) | (df['SepalWidthCm']>upper_treshold)])