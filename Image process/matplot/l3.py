# to make sidde by side bar graphs

import matplotlib.pyplot as plt
import numpy as np
x=["gkaple","gdhale","abhonde","kkasambe","dugale"]
y=[9.9,8.8,8.5,9,9.6]
z=[1.2,4.5,6.5,2.6,0.9]
width = 0.2
plt.xlabel("great elements",fontsize=15)  #label for x-axis and y-axis elements
plt.ylabel("c.g.p.a", fontsize=15)
plt.title("toppers")  #title of our graph
p = np.arange(len(x))
p1 = [i+width for i in p]

#by default the graph is vertical allign to make it align horizontal

# plt.bar(p,y, width, color="brown",edgecolor = "red",label="GREAT")
# plt.bar(p1,z, width, color="gray",edgecolor = "red",label="Elements")   #vertical

plt.barh(p,y, width, color="brown",edgecolor = "red",label="GREAT")
plt.barh(p1,z, width, color="gray",edgecolor = "red",label="Elements")   #horizontal

#if you want name as a valuee on the x-axis

plt.xticks(p+width/2,x, rotation=10)  #u can also rotate values of x-axis
plt.legend() #legend parameter is use to add label
plt.show()