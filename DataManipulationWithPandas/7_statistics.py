import pandas as pd

'''
Mean and median
Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. 
For example, mean, median, minimum, maximum, and standard deviation are summary statistics. 
Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.

'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Mean' + '*' * 25)
print(df['Salary'].mean())
print()

print('*' * 25 + 'Median' + '*' * 25)
print(df['Salary'].median())
print()

print('*' * 25 + 'Mode' + '*' * 25)
print(df['Salary'].mode())
print()

print('*' * 25 + 'Min' + '*' * 25)
print(df['Salary'].min())
print()

print('*' * 25 + 'Max' + '*' * 25)
print(df['Salary'].max())
print()