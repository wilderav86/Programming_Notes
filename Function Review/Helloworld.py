

import turtle
t = turtle.Turtle()



for length in range(100):
    t.width(20)
    t.forward(length * 2)
    t.right(30)
    if length % 3 == 0:
        t.color("red")
    if length % 3 == 1:
        t.color("yellow")
    if length % 3 == 2:
        t.color("blue")

    