import turtle
CoderMohit = turtle.Screen()
CoderMohit.bgcolor('black')
Mohit=turtle.Turtle()
Mohit.shape("turtle")
Mohit.color("red")
Mohit.penup()
Coder=20
for i in range(50):
    Mohit.stamp()
    Coder=Coder+3
    Mohit.forward(Coder)
    Mohit.right(30)
CoderMohit.mainloop()