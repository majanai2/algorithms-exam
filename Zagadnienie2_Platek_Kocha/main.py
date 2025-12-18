import turtle

def koch_curve(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch_curve(length, depth - 1)
        turtle.left(60)
        koch_curve(length, depth - 1)
        turtle.right(120)
        koch_curve(length, depth - 1)
        turtle.left(60)
        koch_curve(length, depth - 1)

def koch_snowflake(length, depth):
    for _ in range(3):
        koch_curve(length, depth)
        turtle.right(120)

# KONFIGURACJA
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

depth = int(input("Podaj głębokość rekurencji (0–6): "))
koch_snowflake(300, depth)

turtle.done()
