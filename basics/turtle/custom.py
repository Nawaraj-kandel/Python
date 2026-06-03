import random
import turtle

t = turtle.Turtle()
t.speed("fastest")
t.pensize(2)
turtle.bgcolor("black")

colors = ["red", "blue", "green", "purple", "orange", "yellow", "cyan"]
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(random.choice(colors))
    size = random.randint(20, 80)
    sides = random.randint(3, 8)
    for _ in range(sides):
        t.forward(size)
        t.right(360 / sides)

t.hideturtle()
turtle.done()
