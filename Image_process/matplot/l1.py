import matplotlib.pyplot as plt

#simple graph
x = [1,2,3,4]  # X-axis values
y = [1,10,45,12]  # Y-axis values
c= ["r", "g", "y", "black"] #to colourize the graph
#plt.plot(x,y)  #plot values of x and y
plt.bar(x, y, color=c)  #bar graph values of x and y
plt.show()
