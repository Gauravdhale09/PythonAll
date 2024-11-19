import matplotlib.pyplot as plt

import pandas as pd
file = 'DataScience/sample2.xlsx'
df = pd.read_excel(file)
df = df[0:5]

print(df)

x = df['Customer Name']
y = df['Order Quantity']

y1 = df['Sales']
plt.bar(x, y, label='Order Quantity Data', color='red')
plt.bar(x, y1, label='Order Sales Data', color='green')

plt.xlabel('Customer Name')
plt.ylabel('Order Quantity')


plt.title('Order Quantity Data Analysis') # title


plt.legend() 
plt.show() # display the graph