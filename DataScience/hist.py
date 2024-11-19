import matplotlib.pyplot as plt

import pandas as pd
file = 'DataScience/sample2.xlsx'
df = pd.read_excel(file)
df = df[0:10]
df = df.fillna({'Sales': 0})

df = df.sort_values('Sales')
print(list(df.Sales))
print(df)
plt.hist(df['Order ID'], df['Sales'], histtype='bar', rwidth=0.8, color='cyan')


plt.xlabel('Order ID')
plt.ylabel('Sales')
plt.title('Histogram of Sales')
# plt.xticks(rotation=90)

plt.legend()
plt.show()