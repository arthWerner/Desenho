import random
import turtle
turtle.Screen().setup(width=1600, height=600)
ana =turtle.Turtle()
ana.hideturtle()
ana.speed(0)
ana.pencolor("#00ff00")
l= 10
for i in range(100):
    ana.forward(l)
    ana.left(90)
    l= l+10



turtle.exitonclick()