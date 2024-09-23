"""
This file draws a table with a cake on top of it. The user can input the color of the table, the length of the table, the height of the table, and the radius of the cake. The cake will be drawn on top of the table with the given radius. 
The cake will have four layers with different colors. 
The cake will also have decorations on top. 
The table will have four legs and a top with the given color, length, and height.
Project by: Noureldin, Saloni, and Mehdi
"""
import turtle as t

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

#Noureldin
def plate(radius): #Drawing the plate for the cake
    t.goto(0,0)
    t.setheading(east)
    t.pendown()
    t.fillcolor("gray60")
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

def prepare_next_layer(distance): #Moving the turtle to the next layer of the cake
    t.setheading(north) #Setting the turtle to face up
    t.forward(distance) 

def cake_layer(color, width, height): #Drawing the cake layers with the given color, width, and height
    t.setheading(east)
    t.pendown()
    t.fillcolor(color)
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
    star_location = layer1_height + layer2_height
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
    t.pendown()
    t.forward(length)    
    t.right(90)
    t.forward(height)    
    t.right(90)
    t.forward(length*2)   
    t.right(90)
    t.forward(height)     
    t.right(90)
    t.forward(length)
    t.end_fill()
    t.penup()
    
    #Drawing legs from left to right
    reset_turtle(180, 0.9)
    #First leg
    t.pendown()
    t.setheading(south)
    t.forward(100)
    t.penup()

    reset_turtle(180, 0.6)
    #Second leg
    t.pendown()
    t.setheading(south)
    t.forward(80)
    t.penup()

    reset_turtle(0, 0.9)
    #Third leg
    t.pendown()
    t.setheading(south)
    t.forward(100)
    t.penup()

    reset_turtle(0, 0.6)
    #Fourth leg
    t.pendown()
    t.setheading(south)
    t.forward(80)
    t.penup()

#Mehdi

def decorations(second_layer_height, radius):
    candle_question = input("Do you want a candle [y/n]?: ")

    x_place = t.xcor()  
    y_place = t.ycor()  

    if candle_question == "y" or candle_question== "yes":
        color = input("What color do you want the candle?: ")
        candle(color)
    else:
        print("No candle.")

    frosting_question = input("Do you want frosting [y/n]?: ")
    if frosting_question == "y" or frosting_question == "yes":
        color = input("What color do you want the frosting?: ")
        frosting(color, x_place, y_place, radius)  
    else:
        print("No frosting.")

    star_question = input("Do you want a star [y/n]?: ")
    if star_question == "y" or star_question== "yes":
        color = input("What color do you want the star?: ")
        star(second_layer_height + 30, color)  
    else:
        print("No star.")

def candle(color):
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

    t.pencolor("orange")
    t.fillcolor("orange")
    t.begin_fill()
    t.pendown()
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.end_fill()

def frosting(color, x_place, y_place, radius):
    t.penup()
    t.goto(x_place - radius, y_place)
    t.pendown()

    t.pencolor(color)
    t.fillcolor(color)

    t.begin_fill()
    t.setheading(0)
    t.forward(radius * 2)
    t.right(90)
    t.forward(10)
    t.right(95)
    t.forward(radius)
    t.circle(5,30)
    t.right(10)
    t.forward(radius)
    t.setheading(90)
    t.forward(10)
    t.end_fill()

    t.penup()

def star(starlocation,color):    
    t.penup()
    t.goto(0, starlocation)  
    t.setheading(0)  
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)  
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

def main():

    t.screensize(canvwidth=window_width, canvheight=window_height, bg="LightBlue1")  #Setting up the screen

    """
    table_color = input("Enter the color of the table: ") #Asking the user for the color of the table
    print("\nWe recommend a table length of at least 200.")
    table_length = int(input("Enter the length of the table: ")) #Asking the user for the length of the table
    print("\nWe recommend a table height of 40.")
    table_height = int(input("Enter the height of the table: ")) #Asking the user for the height of the table
    cake_radius = int(input("Enter the radius of the cake: ")) #Asking the user for the radius of the cake
    """
    #Debugging
    
    table_color = "brown"
    table_length = 401
    table_height = 40
    cake_radius = 75
    
    #Validity checks by Noureldin.
    #Limitation: The program only does this validity check once. If the user enters an invalid value again, the program will proceed.
    if table_length > window_width:
        print("The table is too big for the screen!")
        table_length = int(input(f"Enter a value smaller than {window_width} for the table: ")) 
    elif table_height > window_height:
        print("The table is too tall for the screen!")
        table_height = int(input(f"Enter a value smaller than {window_height} for the table: "))
    elif cake_radius > window_width:
        print("The cake is too big for the screen!")
        cake_radius = int(input(f"Enter a value smaller than {table_length/2} for your cake: "))
    elif cake_radius > table_length/2:
        print("The cake is too big for the table!")
        cake_radius = int(input(f"Enter a value smaller than {table_length/2} for your cake: "))
    else:
        print("The cake fits on the table! Enjoy your cake!")

    tweak() #Setting up the turtle for drawing
    draw_table(table_length, table_height, table_color) #Drawing the table
    plate(cake_radius) #Drawing the plate for the cake
    t.goto(0,0) #Moving the turtle to the center of the plate
    prepare_next_layer(cake_radius*0.2) #Moving the turtle to the first layer of the cake
    cake(cake_radius) #Drawing the cake
    t.exitonclick()

if __name__ == "__main__":
    main()