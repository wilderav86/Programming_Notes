import turtle

def draw_square(some_turtle):
    for side in range(80):
        
        some_turtle.forward(10)
        some_turtle.right(5)
colors = ["red", "yellow", "orange", "green", "blue"]
romeo = turtle.Turtle()
romeo.width(5)
romeo.speed(0)
for petal in range(80):
    draw_square(romeo)
    romeo.right(45)
    if petal % 5 == 0:
        romeo.color("red")
    if petal % 5 == 1: 
        romeo.color("yellow")   
    if petal % 5 == 2: 
        romeo.color("orange")
    if petal % 5 == 3: 
        romeo.color("green")
    if petal % 5 == 4: 
        romeo.color("blue")