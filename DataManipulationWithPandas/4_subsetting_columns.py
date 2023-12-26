import pandas as pd

'''
Subsetting columns
When working with data, you may not need all of the variables in your dataset. 
Square brackets ([]) can be used to select only the columns that matter to you 
in an order that makes sense to you. To select only "col_a" of the DataFrame df, use

df["col_a"]
To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]

Remark:
1. Use single value for one column operation.
2. Use list for multiple column operation.
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Without subsetting' + '*' * 25)
print(df.head(5))
print()

print('*' * 25 + 'Subsetting 1 column' + '*' * 25)
print(df['Name'].head(5))
print()

print('*' * 25 + 'Subsetting multiple columns' + '*' * 25)
print(df[['Name', 'Salary']].head(5))
print()
