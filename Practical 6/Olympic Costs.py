# import matplotlib to draw figures
import matplotlib.pyplot as plt
# list the costs and cities
Costs=[1,8,15,7,5,14,43,40]
Costs.sort()
print(Costs)

Games=['Los Angeles 1984','Sydney 2000','Atlanta 1996' , 'Seoul 1988','Athens 2003','Barcelona 1992', 'London 2012','Beijing 2008' ]
# output value
print(Costs)

# draw figure
# Set the data of x-axis and y-axis
y=Costs
x=Games
plt.plot(x, y,label='costs')
# Set the title and font size for the x-axis and y-axis
plt.xlabel('cost(in $ billions)',fontsize=12)
plt.ylabel("cities",fontsize=12)
# adjust the size of x ticks
plt.xticks(range(len(Costs)), Games, fontsize=6)
# show legend and adjust the size of it
plt.legend(fontsize='small')
# show the figure
plt.show()