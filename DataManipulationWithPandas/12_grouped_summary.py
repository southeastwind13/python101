import pandas as pd

'''
What percent of sales occurred at each store type?
While .groupby() is useful, you can calculate grouped summary statistics without it.

Walmart distinguishes three types of stores: "supercenters," "discount stores,"
 and "neighborhood markets," encoded in this dataset as type "A," "B," and "C." 
 In this exercise, you'll calculate the total sales made at each store type, without using 
 .groupby(). You can then use these numbers to see what proportion of Walmart's total sales were made at each type.

 Calculations with .groupby()
The .groupby() method makes life much easier. In this exercise, 
you'll perform the same calculations as last time, except you'll use the 
.groupby() method. You'll also perform calculations on data grouped by two variables to see 
if sales differ by store type depending on if it's a holiday week or not.

 Remark:
 df.groupby([col1, col2, ... * Columns that would like to group])[[col1, col2, ...* Columns that would like to get statistics]].other_function()
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

print('*' * 25 + 'Groupby' + '*' * 25)
print(df.groupby(['Gender', 'exp(year)'])['Salary'].mean())
print()