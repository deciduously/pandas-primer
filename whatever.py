import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('sample.xls', 'Orders')

filtered_df = df[(df.State == 'California') & (df.Quantity > 2)]
print(filtered_df)

df2 = df.groupby(["Region"])[['State']].count()
print(df2)
