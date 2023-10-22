import turtle

screen = turtle.Screen()
screen.title("Flag of Palestine")
screen.bgcolor("white")
screen.setup(width=600, height=400)
flag_turtle = turtle.Turtle()
flag_turtle.speed(0)


def draw_rectangle(color, width, height):
    flag_turtle.begin_fill()
    flag_turtle.fillcolor(color)
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(height)
        flag_turtle.right(90)
    flag_turtle.end_fill()


flag_turtle.penup()
flag_turtle.goto(-300, 150)
flag_turtle.pendown()
draw_rectangle("black", 600, 40)


flag_turtle.penup()
flag_turtle.goto(-300, 60)
draw_rectangle("white", 600, 40)


flag_turtle.penup()
flag_turtle.goto(-300, 40)
flag_turtle.pendown()
draw_rectangle("green", 600, 40)


flag_turtle.penup()
flag_turtle.goto(-300, 20)
flag_turtle.pendown()
flag_turtle.begin_fill()
flag_turtle.fillcolor("red")
flag_turtle.goto(-300, 140)
flag_turtle.goto(-180, 80)
flag_turtle.goto(-300, 20)
flag_turtle.end_fill()


screen.exitonclick()
