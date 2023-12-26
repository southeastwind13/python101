import pandas as pd

'''
Counting categorical variables

Counting is a great way to get an overview of your data and to spot curiosities 
that you might not notice otherwise. In this exercise, you'll count the number of 
each type of store and the number of each department number using the DataFrames 
you created in the previous exercise:

Remark:
1. df[group of data that want to count].value_counts(sort=..., normalize=...)
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test2', 5000, 2, 'Male'] , [5, 'Test3', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Counting ' + '*' * 25)
print(df['Salary'].value_counts())
print()

print('*' * 25 + 'Counting with proportion ' + '*' * 25)
print(df['Salary'].value_counts(normalize=True))
print()

print('*' * 25 + 'Counting with sort ' + '*' * 25)
print(df['Salary'].value_counts(sort=True))
print()