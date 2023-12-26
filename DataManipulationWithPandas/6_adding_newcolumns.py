import pandas as pd

'''
Adding new columns can go with many names mutating, transforming, feature engineering. 

df[new_column_name] = df[column] with some operation.

'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Add columns' + '*' * 25)
df['SalaryNew'] = df['Salary'] * 1.2
print(df.head())
print()