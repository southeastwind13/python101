import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

'''
One of the importance characteristics of data is central.

We have many method to find the central of data
- Mean: Good with data that have symmetrical data but weak for the outlier.
- Median: Good with data that have skew or outlier.
'''

file_path = 'StatisticsInPython/Iris.csv'
df = pd.read_csv(file_path)

print(df[['SepalWidthCm', 'SepalWidthCm']].mean())
print(df[['SepalWidthCm', 'SepalWidthCm']].median())