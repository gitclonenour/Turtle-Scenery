import turtle as t

#Tariq
def draw_triangle(color, x, y):
    t.speed(0)
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

def draw_background_decorations(): #Drawing the background decorations for the table
    draw_triangle("red", -350, 400)
    draw_line(-350, 400, -280, 400)
    draw_triangle("blue", -280, 400)
    draw_line(-280, 400, -210, 400)
    draw_triangle("green", -210, 400)
    draw_line(-210, 400, -140, 400)
    draw_triangle("yellow", -140, 400)
    draw_line(-140, 400, -70, 400)
    draw_triangle("purple", -70, 400)
    draw_line(-70, 400, 0, 400)
    draw_triangle("orange", 0, 400)
    draw_line(0, 400, 70, 400)
    draw_triangle("cyan", 70, 400)
    draw_line(70, 400, 140, 400)
    draw_triangle("magenta", 140, 400)
    draw_line(140, 400, 210, 400)
    draw_triangle("pink", 210, 400)
    draw_line(210, 400, 280, 400)
    draw_triangle("brown", 280, 400)
    draw_line(280, 400, 350, 400)
    draw_triangle("lime", 350, 400)
    draw_line(350, 400, 420, 400)
    draw_triangle("teal", 420, 400)

t.screensize(canvwidth=400, canvheight=300, bg="LightBlue1") #Sets window size and background color
draw_background_decorations()
t.done()