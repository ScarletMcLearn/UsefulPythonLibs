###Importing pyplot
##from matplotlib import pyplot as plt
##
###Plotting to our canvas
##plt.plot([1,2,3],[4,5,1])
##
###Showing what we plotted
##plt.show()


from matplotlib import pyplot as plt
#
# x = [5,8,10]
# y = [12,16,6]
#
# plt.plot(x,y)
#
# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
#
# plt.show()




# # Line Graphs
# plt.plot([1,2,3,4])                    #only 1 set of coordinates always y
#
#
# #plt.plot([1,5,2,0])                   #giving 2 plots at once  makes em overlap (different colors tho)
#
#
# plt.ylabel('Some Numbers')             #label of  y axis
# plt.xlabel('fuk da polis esar')        #label of  x axis
#
# plt.show()                             #show graph




# plt.plot([1,2,3,4,5],[1,4,9,16,20])      #x to y - y vs x graph    #first set x coordinates, 2nd set y coordinates
# plt.xlabel("ex balu")
# plt.ylabel("fak da poliss")
#
# plt.show()



plt.plot([1,2,3,4,5],[1,4,9,16,20], "ro")   #"ro" rED color with O symbols
plt.axis([0,6,0,20.5])  #x axis min, x axis max, y axis min, y axis max


plt.plot([1,2,3,4,5],[1,4,9,16,20], color= "d", linewidth=2.0, linestyle="--")  #increases linewidth by factor of 2
plt.show()


#interesting. making 1 plot for getting those red dots, and another for getting the line and displaying them together makes em come on top of each other



# lines = plt.plot([1,2,3,4,5],[1,4,9,16,20],)
# plt.axis([0,6,0,20.5])
# plt.setp(lines, color='r', linewidth=2.0, linestyle="--")       #plot.set property  #linestyle="--"
#
#
# plt.title(r'hey dea $\sigma_i=15$')     #set title of graph - top center - supports regex symbols
# plt.grid(True)                          #gives grid on graph
# # plt.savefig("taste.png")              #saves fig as taste.png
#
# plt.show()



# lines = plt.plot([1,2,3,4,5],[1,4,9,16,20],)
# plt.axis([0,6,0,20.5])

'''
        b: blue
        g: green
        r: red
        c: cyan
        m: magenta
        y: yellow
        k: black
        w: white
        color = '#eeefff'
'''
# calar = "m"
# plt.setp(lines, color=calar, linewidth=2.0, linestyle="--")
#
# plt.title(r'hey dea $\sigma_i=15$')
# plt.grid(True)                          #gives grid on graph


# plt.suptitle('yooooo')


# plt.show()




# def __
# def action(self):
#
#     print("I am an animal.")
#
#     print(self.movement())
#
#
#     return
#
#
# def movement(self):
#     return ("wiggle wiggle")
#
#
# a = action()


class Animal(object):
    def action(self):
        print("I am an animal.")
        print(self.movement())

    def movement(self):
        return ("wiggle wiggle")


a = Animal()
a.action()