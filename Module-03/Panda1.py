# pip install openpyxl

import pandas as pd
# import os
# print(os.path.exists('C:\\Users\\Admin\\Desktop\\example.xlsx'))

print(pd.read_excel('example.xlsx', index_col = 0))