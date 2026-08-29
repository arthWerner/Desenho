import turtle
turtle.Screen()
Geoforma=turtle.Turtle()
Geoforma.speed(3)
Geoforma.hideturtle()
lados = 4
for i in range(lados):
    Geoforma.forward(100)
    Geoforma.left(360/lados)

for i in range(lados):
    Geoforma.penup()
    Geoforma.forward(10)

for i in range(lados):
    Geoforma.pendown()
    Geoforma.forward(100)
    Geoforma.left(360 / lados)
    Geoforma.pendown()
turtle.exitonclick()