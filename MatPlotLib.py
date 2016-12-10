###Importing pyplot
##from matplotlib import pyplot as plt
##
###Plotting to our canvas
##plt.plot([1,2,3],[4,5,1])
##
###Showing what we plotted
##plt.show()


from matplotlib import pyplot as plt

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
