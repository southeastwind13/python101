import pandas as pd

'''
Cumulative statistics

Cumulative statistics can also be helpful in tracking summary statistics over time. 
In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, 
which will allow you to identify what the total sales were so far as well as what the highest weekly sales were so far.

Remark:
Normally we do
1. Select column
2. Calculate cumulative 
3. Assign to the new column
'''


# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Apply IQR function' + '*' * 25)
df['cum_sum_salary'] = df['Salary'].cumsum()
df['cum_max_salary'] = df['Salary'].cummax()
df['cum_min_salary'] = df['Salary'].cummin()
print(df.head())
print()