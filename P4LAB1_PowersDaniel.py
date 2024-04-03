#Daniel Powers
#3/25/24
#P4LAB1
#Use a for loop


import turtle          
win = turtle.Screen()  
thomas = turtle.Turtle()

# add some display options
thomas.pensize(4)            # increase pensize (takes integer)
thomas.pencolor("blue")     # set pencolor (takes string)
thomas.shape("turtle")

#commands from here to the last line can be replaced
# square, sides are 360 / 4 = 90 degrees
 
thomas.left(180)             # this time we'll draw it in a different direction

# draw square
thomas.forward(100)
thomas.left(90)

for var in range(4):
    print (thomas.forward(100))
    print (thomas.left(90))


#triangle, sides are 360 / 3 = 120 degrees

# draw triangle
thomas.forward(100)
thomas.right(120)

for var in range(3):
    print (thomas.forward(100))
    print (thomas.right(120))

#end
win.mainloop() 


