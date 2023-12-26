import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'StatisticsInPython/Iris.csv'
df = pd.read_csv(file_path)

np.random.seed(13)

# sampling without replacement
print(df.sample(5))

# sampling with replacement
print(df.sample(5, replace=True))