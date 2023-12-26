import pandas as pd

'''
When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. 
There are several useful methods and attributes for this.

.head() returns the first few rows (the “head” of the DataFrame).
.info() shows information on each of the columns, such as the data type and number of missing values.
.shape returns the number of rows and columns of the DataFrame.
.describe() calculates a few summary statistics for each column.
'''


# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Head' + '*' * 25)
print(df.head(5))
print()

print('*' * 25 + 'Info' + '*' * 25)
print(df.info())
print()

print('*' * 25 + 'Shape' + '*' * 25)
print(df.shape)
print()

print('*' * 25 + 'Describe()' + '*' * 25)
print(df.describe())
print()
