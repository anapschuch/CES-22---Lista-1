import turtle


def draw_square(t, sz):
    """ Turtle t draws a square of side sz """
    for i in range(4):
        t.forward(sz)
        t.left(90)


# Set up window's attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Lista 1 Python - q1")

# Draw 5 squares, the innermost of side 20 and each successive 20 units bigger.
alex = turtle.Turtle()
for i in range(5):
    draw_square(alex, 20 + 20 * i)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

wn.mainloop()
