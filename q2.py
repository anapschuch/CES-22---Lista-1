import turtle


def draw_poly(t, n, sz):
    """ Makes a turtle t draws a regular polygon of n sides with length sz """
    angle = 180 - (n - 2) * 180 / n
    for i in range(n):
        t.forward(sz)
        t.left(angle)


# Set window's attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Lista 1 Python - q2")

# Draw a regular polygon of 8 sides with length 50
tess = turtle.Turtle()
draw_poly(tess, 8, 50)
wn.mainloop()
