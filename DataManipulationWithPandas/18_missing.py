import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Finding missing values
Missing values are everywhere, and you don't want them interfering with your work. 
Some functions ignore missing data by default, but that's not always the behavior 
you might want. Some functions can't handle missing values at all, so these values 
need to be taken care of before you can use them. If you don't know where your missing 
values are, or if they exist, you could make mistakes in your analysis. In this exercise, 
you'll determine if there are missing values in the dataset, and if so, how many.
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, np.nan, 'Male'], [2, "Mock", np.nan, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])


print('*'*50 + ' Check empty for each fields' + '*'*50 ) 
print(df.isna())
print()

print('*'*50 + ' Check empty summary ' + '*'*50 ) 
print(df.isna().any())
print()

print('*'*50 + ' Counting missing value ' + '*'*50 ) 
print(df.isna().sum())
print()

print('*'*50 + ' Remove rows that have missing value ' + '*'*50 ) 
# print(df.dropna().head())
print()

print('*'*50 + ' Replace missing value ' + '*'*50 ) 
# print(df.fillna(0).head())
print()

print('*'*50 + ' Plot missing value ' + '*'*50 ) 
df.isna().sum().plot(kind='bar')
plt.show()