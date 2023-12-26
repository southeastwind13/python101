import pandas as pd

'''
Subsetting rows
A large part of data science is about finding which bits of your dataset are interesting.
One of the simplest techniques for this is to find a subset of rows that match some criteria.
This is sometimes known as filtering rows or selecting rows.

There are many ways to subset a DataFrame, perhaps the most common is to use relational operators 
to return True or False for each row, then pass that inside square brackets.

dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
You can filter for multiple conditions at once by using the "bitwise and" operator, &.

dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]

Remark:
1. Use single value for one column operation.
2. Use list for multiple column operation.
3. Row filter form df[condition] -> Condition example df['col'] > 5
4. In case of multiple conditions df[(condition1) operator (condition2)] -> operator &, |
5. In case of subsetting rows by categorical variables use .isin()
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Filter with 1 condition' + '*' * 25)
print(df[df['Salary'] > 3000])
print()

print('*' * 25 + 'Filter with multiple condition' + '*' * 25)
print(df[(df['Salary'] == 3000) | (df['Salary'] == 10000)])
print()

print('*' * 25 + 'Filter by categories' + '*' * 25)
print(df[df['Gender'].isin(['Male'])])
print()
