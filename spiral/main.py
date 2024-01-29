import turtle
animation =turtle.Turtle()
animation.speed(50)
animation.hideturtle()
animation.getscreen().bgcolor("black")
animation.color("green")

for i in range(170):
    animation.circle(i)
    animation._rotate(6)