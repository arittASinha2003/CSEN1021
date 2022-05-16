import pandas as pd

# data = pd.read_excel('example.xlsx')
# df = pd.DataFrame(data, columns = ['Students'])
# print(df)

std_dict = {'Branch' : ['ECE', 'CSE', 'MECH', 'CIVIL'], 'Strength' : [120, 1000, 12, 14], 'Year' : [2020, 2021, 2019, 2022]}

s = pd.DataFrame(std_dict)
print(s)