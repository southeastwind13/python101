import pandas as pd

'''
Sorting rows
Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. 
You can sort the rows by passing a column name to .sort_values().

In cases where rows have the same value (this is common if you sort on a categorical variable), 
you may wish to break the ties by sorting on another column. You can sort on multiple columns 
in this way by passing a list of column names.

Sort on …	Syntax
one column	df.sort_values("breed")
multiple columns	df.sort_values(["breed", "weight_kg"])

By combining .sort_values() with .head(), you can answer questions in the form, "What are the top cases where…?".


Remark:
1. Use single value for one column operation.
2. Use list for multiple column operation.

'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Without source' + '*' * 25)
print(df.head(5))
print()


print('*' * 25 + 'Source single' + '*' * 25)
print(df.sort_values('Salary').head(5))
print()

print('*' * 25 + 'Source single descending' + '*' * 25)
print(df.sort_values('Salary', ascending=False).head(5))
print()

print('*' * 25 + 'Source multiple' + '*' * 25)
print(df.sort_values(['Salary', 'exp(year)']).head(5))
print()

print('*' * 25 + 'Source multiple descending' + '*' * 25)
print(df.sort_values(['Salary', 'exp(year)'], ascending=[False, True]).head(5))
print()