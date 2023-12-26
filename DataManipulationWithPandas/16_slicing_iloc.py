import pandas as pd

'''
Subsetting by row/column number
The most common ways to subset rows are the ways we've previously discussed: 
using a Boolean condition or by index labels. However, it is also occasionally useful to pass row numbers.

This is done using .iloc[], and like .loc[], it can take two arguments to let you subset by rows and columns.

Remark:
1. iloc is exclusive slicing -> .iloc[0:2] will return row 0, 1 and exclude row 2
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Slicing rows' + '*' * 25)
print(df.iloc[0:2])
print()

print('*' * 25 + 'Slicing columns' + '*' * 25)
print(df.iloc[:, 0:2 ])
print()

print('*' * 25 + 'Slicing both' + '*' * 25)
print(df.iloc[0:2, 0:2 ])
print()