"""
This file draws a table with a cake on top of it. The user can input the color of the table, the length of the table, the height of the table, and the radius of the cake. The cake will be drawn on top of the table with the given radius. 
The cake will have four layers with different colors. 
The cake will also have decorations on top. 
The table will have four legs and a top with the given color, length, and height.
Project by: Noureldin, Saloni, Tariq, and Mehdi
"""
import turtle as t

#Noureldin

#Setting up the directions for the setheading() function
east = 0
north = 90
west = 180
south = 270
window_width = 400
window_height = 300

def tweak(): #Setting up turtle for the drawing
    t.pencolor("black")
    t.pensize(2)
    t.speed(7)

def plate(radius): #Drawing the plate for the cake
    t.goto(0,0)
    t.setheading(east)
    t.pendown()
    t.fillcolor("gray60")
    t.pencolor("black")
    t.begin_fill()
    t.forward(radius*1.5) #Bottom side first half
    t.left(90)
    t.forward(radius*0.2) #Right side
    t.left(90)
    t.forward(radius*3) #Top side
    t.left(90)
    t.forward(radius*0.2) #Left side
    t.left(90)
    t.forward(radius*1.5) #Bottom side second half
    t.end_fill()
    t.penup()
    t.goto(0,0) #Moving the turtle to the center of the plate

def prepare_next_layer(distance): #Moving the turtle to the next layer of the cake
    t.setheading(north) #Setting the turtle to face up
    t.forward(distance) 

def cake_layer(color, width, height): #Drawing the cake layers with the given color, width, and height
    t.setheading(east)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.forward(width) #Bottom side first half
    t.left(90)
    t.forward(height) #Right side
    t.left(90)
    t.forward(width*2) #Top side
    t.left(90)
    t.forward(height) #Left side
    t.left(90)
    t.forward(width) #Bottom side second half
    t.end_fill()
    t.penup()

def cake(radius): #Drawing the cake with the given radius
    #Setting up the height of the layers using the radius
    layer1_height = radius*0.6 
    layer2_height = radius*0.3
    layer3_height = radius*0.15
    star_location = radius*1.15
    #Drawing the layers
    cake_layer("DeepPink2", radius, layer1_height) #Bottom layer
    prepare_next_layer(layer1_height)
    cake_layer("gray20", radius, layer2_height) #Middle layer 1
    prepare_next_layer(layer2_height)
    cake_layer("chocolate", radius, layer3_height) #Middle layer 2
    prepare_next_layer(layer3_height)
    cake_layer("bisque", radius, layer1_height) #Top of the cake
    prepare_next_layer(layer1_height)

    decorations(star_location, radius)  # Pass radius to the decorations function

#*********************************************************************************************************************
#Saloni
def draw_table(length, height, color): #Drawing the table with the given length, height, and color
    def reset_turtle(heading, distance): #Resetting the turtle to the starting position for drawing the next leg
        t.goto(0,-height) #Moving the turtle to the bottom of the table
        t.setheading(heading)
        t.forward(length*distance) #Moving the turtle to the starting position for drawing the next leg
    
    #table top
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(0,0)
    t.setheading(east)  
    t.pendown()
    t.forward(length)   #Top half 1 
    t.right(90)
    t.forward(height)    
    t.right(90)
    t.forward(length*2)   #Bottom of the table
    t.right(90)
    t.forward(height)     
    t.right(90)
    t.forward(length)   #Top half 2
    t.end_fill()
    t.penup()
    
    #Drawing legs from left to right
    reset_turtle(west, 0.9)  #Moving the turtle 90% of the table's length in the west direction.
    #First leg
    t.pendown()
    t.setheading(south)
    t.forward(100)
    t.penup()

    reset_turtle(west, 0.6)
    #Second leg
    t.pendown()
    t.setheading(south)
    t.forward(80)
    t.penup()

    reset_turtle(east, 0.9)
    #Third leg
    t.pendown()
    t.setheading(south)
    t.forward(100)
    t.penup()

    reset_turtle(east, 0.6)
    #Fourth leg
    t.pendown()
    t.setheading(south)
    t.forward(80)
    t.penup()

#*********************************************************************************************************************
#Mehdi
def decorations(second_layer_height, radius): #Drawing decorations on the cake
    print("\nTime to decorate your cake!\n")

    frosting_question = input("Do you want frosting [y/n]?: ")
    if frosting_question == "y" or frosting_question == "yes":
        color = input("What color do you want the frosting?: ")
        frosting(color, radius)  
    else:
        print("No frosting.")
    
    candle_question = input("\nDo you want a candle [y/n]?: ")
    if candle_question == "y" or candle_question== "yes":
        candle("red")
    else:
        print("No candle.")

    star_question = input("\nDo you want a star [y/n]?: ")
    if star_question == "y" or star_question== "yes":
        star(second_layer_height + 30, "yellow")  
    else:
        print("No star.")

def candle(color): #Candle drawing function
    prepare_next_layer(20)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(30)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(30)
    
    t.end_fill()
    t.penup()
    t.left(180)
    t.forward(30)

    t.fillcolor("orange")
    t.begin_fill()
    t.pendown()
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.end_fill()

def frosting(color, width):
    cake_layer(color, width*1.15, 20) #Drawing a frosting on top of the cake

def star(starlocation,color): #Star drawing function
    t.penup()
    t.goto(0, starlocation)  
    t.setheading(east)  
    t.pendown()
    t.fillcolor(color)
    t.pencolor("black")
    t.pensize(1)
    t.begin_fill()
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.forward(20)
    t.right(144)
    t.end_fill()

#*********************************************************************************************************************
#Tariq
# Function to draw a triangle
def draw_triangle(color, x, y):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(180)  # Set the turtle facing downwards
    # Drawing the triangle sides
    t.forward(50)  # Triangle side length
    t.left(120)    # Turn the turtle 120 degrees
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

def draw_background_decorations():  # Drawing the background decorations for the table
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

def draw_birthday_message():
    t.penup()
    t.goto(0, 260)  # Position the message below the triangles
    t.pendown()
    t.color("black")
    t.write("Happy Birthday!", align="center", font=("Arial", 24, "bold"))


#Noureldin.
def main(): #Main function to draw the table and the cake

    print("\n\nWelcome to the cake drawing program!")
    table_color = input("Enter the color of the table: ") #Asking the user for the color of the table
    print("\nWe recommend a table length between 200 and 400.\nMinimum value is 100.")
    table_length = int(input("Enter the length of the table: ")) #Asking the user for the length of the table
    print("\nWe recommend a table height of 40.\nMinimum value is 20.")
    table_thickness = int(input("Enter the thickness of the table: ")) #Asking the user for the height of the table
    print("\nWe recommend a cake radius of at least 50.")
    cake_radius = int(input("Enter the radius of the cake: ")) #Asking the user for the radius of the cake
    
    #Limitation: The program only does this validity check once. If the user enters an invalid value again, the program will proceed.
    if table_length > window_width: #Checking if the table is too big for the screen
        print("\nThe table is too big for the screen!")
        table_length = int(input(f"Enter a value smaller than {window_width} for the table: ")) 
    elif table_thickness > window_height:
        print("\nThe table is too thick for the screen!")
        table_thickness = int(input(f"Enter a value smaller than {window_height} for the table: "))
    elif cake_radius > window_width: #Checking if the cake is too big for the screen
        print("\nThe cake is too big for the screen!")
        cake_radius = int(input(f"Enter a value smaller than {table_length/2} for your cake: "))
    elif cake_radius > table_length/2: #Checking if the cake is too big for the table. Cannot exceed half the table's length.
        print("\nThe cake is too big for the table!")
        cake_radius = int(input(f"Enter a value smaller than {table_length/2} for your cake: "))
    elif table_length < 100: #Checking if the table is too small
        print("\nThe table is too small!")
        table_length = int(input("Enter a value larger than 100 for the table: "))
    elif table_thickness < 20: #Checking if the table is too thin
        print("\nThe table height is too thin!")
        table_thickness = int(input("Enter a value larger than 20 for the table thickness: "))
    elif cake_radius < 25: #Checking if the cake is too small
        print("\nThe cake is too small!")
        cake_radius = int(input("Enter a value larger than 25 for your cake: "))
    else:
        print("\nThe cake fits on the table! Drawing your cake...")

    t.screensize(canvwidth=window_width, canvheight=window_height, bg="LightBlue1")  #Setting up the screen
    tweak() #Setting up the turtle for drawing

    #Drawing functions
    draw_background_decorations()
    draw_birthday_message()
    draw_table(table_length, table_thickness, table_color) #Drawing the table
    plate(cake_radius) #Drawing the plate for the cake
    prepare_next_layer(cake_radius*0.2) #Moving the turtle to the first layer of the cake, above the plate
    cake(cake_radius) #Drawing the cake

    t.hideturtle() #Hiding the turtle
    print("\n\nEnjoy your cake!")
    t.exitonclick()

if __name__ == "__main__":
    main()