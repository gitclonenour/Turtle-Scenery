import turtle as t

# Function to draw a flipped triangle (180 degrees)
def draw_triangle(color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(180)  # Set the t facing downwards
    #Drawing the triangle sides
    t.forward(50)  # Triangle side length
    t.left(120)    # Turn the t 120 degrees
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.end_fill()

# Function to draw a connecting line between triangles
def draw_line(x_start, y_start, x_end, y_end):
    t.penup()
    t.goto(x_start, y_start)
    t.pendown()
    t.goto(x_end, y_end)

# Set up the t
t.speed(0)  # Slower drawing speed
t.bgcolor("white")

draw_triangle("red", -350, 200)
draw_line(-350, 200, -280, 200)
draw_triangle("blue", -280, 200)
draw_line(-280, 200, -210, 200)
draw_triangle("green", -210, 200)
draw_line(-210, 200, -140, 200)
draw_triangle("yellow", -140, 200)
draw_line(-140, 200, -70, 200)
draw_triangle("purple", -70, 200)
draw_line(-70, 200, 0, 200)
draw_triangle("orange", 0, 200)
draw_line(0, 200, 70, 200)
draw_triangle("cyan", 70, 200)
draw_line(70, 200, 140, 200)
draw_triangle("magenta", 140, 200)
draw_line(140, 200, 210, 200)
draw_triangle("pink", 210, 200)
draw_line(210, 200, 280, 200)
draw_triangle("brown", 280, 200)
draw_line(280, 200, 350, 200)
draw_triangle("lime", 350, 200)
draw_line(350, 200, 420, 200)
draw_triangle("teal", 420, 200)

# Finish drawing
t.hideturtle()
t.done()
