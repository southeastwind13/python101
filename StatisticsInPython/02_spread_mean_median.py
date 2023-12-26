import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

'''
One of the importance characteristics of data is spread.

We have many ways to measure the spreads.

1. Variance (VAR)
- sum(df-df.mean())**2 / (n-1).
- unit of variance are squared so it hard to interpret.
- using numpy -> np.var(df['col1'], ddof=1)
- ddof = 1 => calculate variance of sample
- doof != 1 => calculate variance of population

2. Standard deviation (SD)
- Square root of Variance
- using numpy -> np.std(df['col1', ddof=1])
- unit is the same with the data so it easy to understand.

3. Mean absolute deviation
- abs(df-df.mean()) / (n-1) 

Standard deviation vs Mean absolute deviation
- Standard deviation square distances, penalize longer distance more than shorter ones.
- Mean absolute deviation penalize each distance equally.
- One ins't better than other, but the SD is common than MAD.

'''

file_path = 'StatisticsInPython/Iris.csv'
df = pd.read_csv(file_path)

print(np.var(df['SepalLengthCm'], ddof=1)) # Variance of sample
print(np.var(df['SepalLengthCm'])) # Variance of population
print(df['SepalLengthCm'].var()) # Variance of sample
print(df['SepalLengthCm'].var(ddof=0)) # Variance of population
print()
print(np.std(df['SepalLengthCm'], ddof=1)) # Standard deviation of sample
print(np.std(df['SepalLengthCm'])) # Standard deviation of population
print(df['SepalLengthCm'].std()) # Standard deviation of sample
print(df['SepalLengthCm'].std(ddof=0)) # Standard deviation of sample
print()
print(np.mea)