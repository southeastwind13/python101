import pandas as pd
import matplotlib.pyplot as plt

'''
'''

# Generate mock DataFrame for learning
data = [[1, 'Pong', 10000, 5, 'Male'], [2, "Mock", 5000, 3, 'Female'], [3, 'Test', 3000, 2, 'Female'], [4, 'Test', 5000, 2, 'Male']]
df = pd.DataFrame(data, columns=['id', 'Name', 'Salary', 'exp(year)', 'Gender'])

df_gender_salary = df.groupby('Gender')['Salary'].mean()

# -- Normal bar plot
# df_gender_salary.plot(kind='bar', rot=45)
# plt.show()

# -- Normal scatter plot
# df.plot(kind='scatter', x='Gender', y='Salary', title='test-title')


#-------- example histrogram ----
'''
# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
'''

plt.show()