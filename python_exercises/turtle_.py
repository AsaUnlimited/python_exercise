import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("gray")
turtle.circle(40, steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color("brown")
turtle.circle(40, steps=5)
turtle.end_fill()




turtle.done()