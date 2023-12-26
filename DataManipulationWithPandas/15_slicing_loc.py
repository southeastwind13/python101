import pandas as pd

'''
This loc is slicing by index/names)


Slicing lets you select consecutive elements of an object using first:last syntax. 
DataFrames can be sliced by index values or by row/column number; we'll start with 
the first case. This involves slicing inside the .loc[] method.

Remark:
1. You can only slice an index if the index is sorted (using .sort_index()).
2. To slice at the outer level, first and last can be strings.
3. To slice at inner levels, first and last should be tuples.
4. If you pass a single slice to .loc[], it will slice the rows.
5. If you pass a double slice to .loc[], it will slice the rows and the columns.

6. loc is index slicing with inclusive.
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

df_idex = df.set_index(['id', 'Name'])
df_sort = df_idex.sort_index()

print('*' * 25 + 'Slicing first index' + '*' * 25)
print(df_sort.loc[1:2])
print()

print('*' * 25 + 'Slicing first and second index' + '*' * 25)
print(df_sort.loc[(1,'Pong'):(2, 'Mock')])
print()

print('*' * 25 + 'Slicing row and column' + '*' * 25)
print(df_sort.loc[1:2, 'Salary':'exp(year)'])
print()