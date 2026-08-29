import turtle
Geoforma=turtle.Turtle()
Geoforma.speed(3)
Geoforma.hideturtle()
lados = 3
for i in range(lados):
    Geoforma.forward(100)
    Geoforma.left(360/lados)



turtle.done()