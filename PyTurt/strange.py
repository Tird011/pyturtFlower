import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
t.color("gold")

def polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)

def glow_circle(radius, layers=6, color="orange"):
    for i in range(layers):
        t.pencolor(color)
        t.circle(radius + i*2)

for i in range(3):
    t.penup()
    t.goto(0, -150 - i*10)
    t.pendown()
    glow_circle(150 + i*10, color="gold")

t.penup()
t.goto(0, -140)
t.setheading(90)
t.pendown()
t.pencolor("#ffb300")

t.penup()
t.goto(0, 0)
t.pendown()

t.setheading(90)
t.circle(120, steps=5)  


t.penup()
points = []
for i in range(5):
    angle = 90 + i * 72
    x = 120 * math.cos(math.radians(angle))
    y = 120 * math.sin(math.radians(angle))
    points.append((x, y))

t.pencolor("#ff8800")
t.pendown()
for i in range(5):
    t.goto(points[i])
    t.goto(points[(i + 2) % 5])
t.goto(points[0])

t.pencolor("#ff6600")
for r in [100, 70, 40]:
    t.penup()
    t.goto(0, -r)
    t.setheading(0)
    t.pendown()
    t.circle(r)

t.pencolor("#ffaa00")
for i in range(12):
    angle = i * 30
    x = 130 * math.cos(math.radians(angle))
    y = 130 * math.sin(math.radians(angle))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(5)


t.penup()
t.goto(-60, -200)
t.pencolor("white")
turtle.done()
