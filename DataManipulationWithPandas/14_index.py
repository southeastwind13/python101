import pandas as pd

'''
* Not importance and should skip it. We shouldn't follow more than one methodology for working
- Normal subsetting         -> pd[col1].isin([col2, col3])
- Subsetting with new index -> pd.loc[[col2, col3]]

pandas allows you to designate columns as an index. 
This enables cleaner code when taking subsets (as well as providing more efficient lookup under some circumstances).

Remark
'''


# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Normal' + '*' * 25)
print(df.head())
print()

print('*' * 25 + 'Set single index' + '*' * 25)
df_index = df.set_index('id')
print(df_index.head())
print()

print('*' * 25 + 'Reset single index' + '*' * 25)
df_index_reset = df_index.reset_index()
print(df_index_reset.head())
print()

print('*' * 25 + 'Reset single index with drop' + '*' * 25)
df_index_reset_drop = df_index.reset_index(drop=True)
print(df_index_reset_drop.head())
print()

print('*' * 25 + 'Reset with modify the DataFrame rather than creating a new one.' + '*' * 25)
df_index.reset_index(inplace=True)
print(df_index.head())
print()

print('*' * 25 + 'Sub set with iloc' + '*' * 25)
'''
Filet by iloc -> focus on index
'''
df_index2 = df.set_index('id')
print(df_index2.loc[[1, 2]])
print()


print('*' * 25 + 'Multiple index' + '*' * 25)
df_index3 = df.set_index(['id', 'Name'])
print(df_index3.loc[[(1, 'Pong')]])
print()


