import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle object
flower = turtle.Turtle()
flower.speed(0)
flower.pensize(2)

# Draw a single petal


def draw_petal(radius, angle, color):
    flower.color(color)
    flower.begin_fill()
    for _ in range(2):
        flower.circle(radius, angle)
        flower.left(180 - angle)
    flower.end_fill()

# Draw multiple petals around the center


def draw_flower_layer(petals, radius, angle, color):
    for _ in range(petals):
        draw_petal(radius, angle, color)
        flower.right(360 / petals)

# Draw the flower


def draw_flower():
    flower.penup()
    flower.goto(0, -100)
    flower.pendown()

    # Outer petal layer
    draw_flower_layer(12, 100, 60, "red")

    # Middle petal layer
    flower.right(15)
    draw_flower_layer(12, 60, 60, "orange")

    # Inner petal layer
    flower.right(15)
    draw_flower_layer(6, 40, 60, "yellow")

    # Flower center
    flower.penup()
    flower.goto(0, -20)
    flower.setheading(0)
    flower.pendown()
    flower.color("brown")
    flower.begin_fill()
    flower.circle(20)
    flower.end_fill()

# Draw stem


def draw_stem():
    flower.penup()
    flower.goto(0, -100)
    flower.setheading(-90)
    flower.pendown()
    flower.color("green")
    flower.pensize(10)
    flower.forward(200)

# Draw leaves


def draw_leaf(x, y, angle):
    flower.penup()
    flower.goto(x, y)
    flower.setheading(angle)
    flower.pendown()
    flower.color("forest green")
    flower.begin_fill()
    flower.circle(50, 60)
    flower.left(120)
    flower.circle(50, 60)
    flower.end_fill()


# Compose everything
draw_flower()
draw_stem()
draw_leaf(-30, -180, -45)
draw_leaf(30, -220, 45)

# Hide turtle
flower.hideturtle()

# Exit on click
screen.exitonclick()
