# pip install openpyxl
# print(pd.__version__)

import pandas as pd
# import os
# print(os.path.exists('C:\\Users\\Admin\\Desktop\\example.xlsx'))

# print(pd.read_excel('salary.xlsx', index_col = 0))

data = pd.read_excel('salary.xlsx')

# data_1 =  data.groupby('Occupation')['Occupation'].count()

data_1 = data.groupby(['Occupation'],as_index=False).Salary.mean()
# data_1 = data.groupby(['Occupation']).Salary.mean()

print(data_1)