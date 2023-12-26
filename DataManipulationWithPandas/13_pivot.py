import pandas as pd
import numpy as np
'''

Pivoting on one variable
Pivot tables are the standard way of aggregating data in spreadsheets.

In pandas, pivot tables are essentially another way of performing grouped calculations. 
That is, the .pivot_table() method is an alternative to .groupby().

In this exercise, you'll perform calculations using .pivot_table() to replicate the calculations 
you performed in the last lesson using .groupby().


Remark:
1. Pivot is equal groupby with statistics mean
- df.groupby(col1)[col2].mean() is the same with df.pivot_table(values=col2, index=col1)

2. If we would like to group more that 1 columns we need to use parameter 'columns'
- df.pivot_table(values=col1, index=col2, columns=col3)

3. We can replace NaN data with specific value by use parameter 'fill_value'
- df.pivot_table(values=col1, index=col2, columns=col3, fill_value=0)

4. If we would like to have a summary. We can use option 'margins'
- df.pivot_table(values=col1, index=col2, columns=col3, fill_value=0, margins=True)
- This case will calculate statistics (Mean) in the last row by exclude NaN or data that replace by option 'fill_value' 

5. If we would like to get other statistics (Not only mean) we can use option 'aggfunc'
- df.pivot_table(values=col1, index=col2, columns=col3, fill_value=0, margins=True, aggfunc=np.mean)


values = col that you want to summarize
index = col that you want to groupby
fill_value = Value that request to replace NaN
margins= Is last row will contain mean of all values in the column or row (Not including the missing values that we fill it by option fill_values)
columns = If group by more than 1 col have to use this fields 


default of pivot statistics is mean but we can change it by
df.pivot_table(values=col2, index=col1, aggfunc=np.median)

'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Pivot' + '*' * 25)
print(df.pivot_table(values='Salary', index='Gender'))
print()

print('*' * 25 + 'Pivot with group more than 1 columns' + '*' * 25)
print(df.pivot_table(values='Salary', index='Gender', columns='exp(year)'))
print()

print('*' * 25 + 'Pivot with replace NaN' + '*' * 25)
print(df.pivot_table(values='Salary', index='Gender', columns='exp(year)', fill_value=191))
print()

print('*' * 25 + 'Summary statistics' + '*' * 25)
print(df.pivot_table(values='Salary', index='Gender', columns='exp(year)', fill_value=191, margins=True))
print()

print('*' * 25 + 'Get other statistics' + '*' * 25)
print(df.pivot_table(values='Salary', index='Gender', columns='exp(year)', fill_value=191, margins=True, aggfunc=np.median))
print()