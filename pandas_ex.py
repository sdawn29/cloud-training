import pandas as pd

df = pd.read_csv('dbdump.csv')
print(df['IP'])
df2 = df['ID'].describe()
print(df2)
line = '-' * 40
print(line)
df3 = df['IP'].describe()
print(df3)
print(line)

df4 = df.describe()
print(df4)
print(line)

df5 = df['ID'].mean()
print('df5=', df5)
print(line)

df6 = df.head(2)
df7 = df.tail(2)
print('df6=', df6)
print(line)
print('df7=', df7)
print(line)

df8 = df['PICS'].value_counts()
print(df8)
print(line)

import matplotlib.pyplot as plt

# df8.plot()
# plt.show()

df8.plot.bar()
# plt.tight_layout()
plt.savefig('mygraph.png', bbox_inches='tight')

writer = pd.ExcelWriter('Report.xlsx', engine='xlsxwriter')
df8.to_excel(writer, sheet_name='DATA')
wb = writer.book
ws = wb.add_worksheet('Graph')
ws.insert_image('B2', 'mygraph.png')
writer.close()

df9 = df[df['ID'] > 2]
print(df9)
print(line)

df10 = df[df['PICS'].str.endswith('jpg')]
print(df10)
print(line)

df11 = df.groupby(['PICS']).count()
print(df11)
print(line)

# slicing
df12 = df.iloc[1, 1]  # one cell
df13 = df.iloc[1]  # row 1
df14 = df.iloc[:, 1]  # column 1
df15 = df.iloc[1:10:2]  # 1 to 9 step by 2
df16 = df.iloc[:, 0:5:2]  # 0 to 5 step by 2
df17 = df.iloc[5:10, 1:4]
df18 = df.iloc[[1, 4, 3]]
df19 = df.iloc[[1, 3, 5], [1, 3]]
