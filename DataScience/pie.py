import matplotlib.pyplot as plt

import pandas as pd
file = 'DataScience/sample2.xlsx'
df = pd.read_excel(file)
df = df[4:7]
print(df)
sales = df['Sales']
customers = df['Customer Name']

cols = ['blue', 'green', 'yellow']

plt.pie(sales, labels=customers, colors=cols, startangle=90, shadow=True, autopct='%.1f%%')

plt.title('Sales Data')
plt.legend()
plt.show()