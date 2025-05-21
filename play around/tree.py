import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Set up turtle
tree = turtle.Turtle()
tree.speed(0)
tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()

# Recursive function to draw a realistic tree


def draw_branch(t, length, thickness):
    if length < 10:
        # Leaves or flowers at the ends
        t.color(random.choice(["green", "lightgreen", "pink", "red"]))
        t.begin_fill()
        t.circle(4)
        t.end_fill()
        t.color("brown")
        return

    t.pensize(thickness)
    t.forward(length)

    # Random angle and size for more natural look
    angle = random.randint(15, 30)
    shrink = random.uniform(0.6, 0.8)

    # Right branch
    t.right(angle)
    draw_branch(t, length * shrink, thickness * 0.7)

    # Left branch
    t.left(angle * 2)
    draw_branch(t, length * shrink, thickness * 0.7)

    # Restore position
    t.right(angle)
    t.backward(length)


# Start drawing
tree.color("brown")
draw_branch(tree, 100, 10)

# Finish
tree.hideturtle()
screen.exitonclick()
