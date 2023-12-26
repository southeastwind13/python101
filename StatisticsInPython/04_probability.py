import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'StatisticsInPython/Iris.csv'
df = pd.read_csv(file_path)

'''
Calculate probability
'''
counts = df['Species'].value_counts()
prob = counts/counts.sum()
print(prob)

np.random.seed(4)
print(np.random.sample(5))