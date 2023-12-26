import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
'''


print("*"*50 + ' From a list of dicts ' + '*'*50)
# Construction row by row
list_of_dict = [
    {'id':1,'name':'pong', 'salary':1000000},
    {'id':2,'name':'mock', 'salary':200000}
]
df_list_of_dict = pd.DataFrame(list_of_dict)
print(df_list_of_dict.head())
print()


print("*"*50 + ' From a dict of lists ' + '*'*50)
# Construction column by column
dict_of_list = {
    'id':[0, 1],
    'name': ['pong', 'mock'],
    'salary': [1000000, 200000]
}
df_dict_of_list = pd.DataFrame(dict_of_list)
print(df_dict_of_list.head())

