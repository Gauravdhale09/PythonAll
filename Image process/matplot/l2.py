# create a bar graph of cgpa in sem3 of 6 great elements

import matplotlib.pyplot as plt

x = ["gkaple","gdhale","abhonde","kkasambe","dugale"]
plt.xlabel("great elements",fontsize=15)  #label for x-axis and y-axis elements
plt.ylabel("c.g.p.a", fontsize=15)
plt.title("toppers")  #title of our graph
y=[9.9,8.8,8.5,9,9.6]
z=[1.2, 4.5, 6.5, 2.6, 0.9]

#plt.bar(x,y, width=0.3, color="black")  #you can also set width of bars and also colour
#plt.bar(x,y, width=0.3, color="yellow",edgecolor = "red", linewidth=5)  #you can also change edge colour of edges of bars and its width
#plt.bar(x,y, width=0.3, color="yellow",edgecolor = "red", linewidth=5, alpha=0.1)  #to make bar light color use alpha

#to make double we will need two values for each x-axis elements
plt.bar(x,y, width=0.3, color="brown",edgecolor = "red",label="GREAT")
plt.bar(x,z, width=0.3, color="gray",edgecolor = "red",label="Elements")

plt.legend() #legend parameter is use to add label
plt.show()