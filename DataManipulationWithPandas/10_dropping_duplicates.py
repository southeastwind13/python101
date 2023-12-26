import pandas as pd

'''
Dropping duplicates
Removing duplicates is an essential skill to get accurate counts because often,
you don't want to count the same thing multiple times. In this exercise, 
you'll create some new DataFrames using unique values from sales.
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test2', 5000, 2, 'Male'] , [5, 'Test3', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Drop 1 column' + '*' * 25)
df_dropone = df.drop_duplicates('Salary')
print(df_dropone.head())
print()

print('*' * 25 + 'Drop multi columns' + '*' * 25)
df_dropmulti = df.drop_duplicates(['Salary', 'Gender'])
print(df_dropmulti.head())
print()