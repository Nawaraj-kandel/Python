import turtle
t = turtle.Turtle()

sides = 5
length = 100
angle = 360 / sides
for _ in range(sides):
    t.forward(length)
    t.right(angle)
turtle.done()
