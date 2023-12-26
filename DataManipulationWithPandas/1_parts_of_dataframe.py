import pandas as pd

'''
Parts of a DataFrame
To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

.values: A two-dimensional NumPy array of values.
.columns: An index of columns: the column names.
.index: An index for the rows: either row numbers or row names.
You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. (These will be covered later in the course.)

homelessness is available.
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Values' + '*' * 25)
print(df.values)
print()

print('*' * 25 + 'Columns' + '*' * 25)
print(df.columns)
print()

print('*' * 25 + 'Index' + '*' * 25)
print(df.index)
print()