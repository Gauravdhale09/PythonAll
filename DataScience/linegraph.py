import matplotlib.pyplot as plt

import pandas as pd
file = 'DataScience/sample2.xlsx'
df = pd.read_excel(file)
df = df[0:5]
df = df.sort_values('Order Quantity')
print(list(df['Order Quantity']))
print(list(df['Sales']))
plt.plot(df['Order Quantity'], df['Sales'], 'green')

plt.title('Customer Sales Line Graph')
plt.xlabel('Order Quantity')
plt.ylabel('Sales')

plt.show()