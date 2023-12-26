import pandas as pd
import numpy as np

'''
Efficient summaries
While pandas and NumPy have tons of functions, sometimes, you may need a different function to summarize your data.

The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more 
than one column of a DataFrame at once, making your aggregations super-efficient. For example,

df['column'].agg(function)

'''


# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])


def iqr(column:pd.DataFrame):
    return column.quantile(0.75) - column.quantile(0.25)

print('*' * 25 + 'Apply IQR function' + '*' * 25)
print(df[['Salary', 'exp(year)']].agg([iqr, np.median]))
print()