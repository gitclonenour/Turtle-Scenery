import turtle as t 

def tweak(): #Setting up turtle for the drawing
    t.pencolor("black")
    t.pensize(3)
    t.speed(10)

def plate(radius): #Drawing the plate for the cake
    t.pendown()
    t.fillcolor("gray90")
    t.pencolor("gray90")
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
    t.setheading(90) #Setting the turtle to face up
    t.forward(distance) 

def cake_layer(color, width, height): #Drawing the cake layers with the given color, width, and height
    t.setheading(0)
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
    #Drawing the layers
    cake_layer("DeepPink2", radius, layer1_height) #Bottom layer
    prepare_next_layer(layer1_height)
    cake_layer("gray20", radius, layer2_height) #Middle layer 1
    prepare_next_layer(layer2_height)
    cake_layer("chocolate", radius, layer3_height) #Middle layer 2
    prepare_next_layer(layer3_height)
    cake_layer("bisque", radius, layer1_height) #Top of the cake

def main():
    length = int(input("Enter the radius of the cake: ")) #Asking the user for the radius of the cake
    tweak()
    plate(length)
    prepare_next_layer(length*0.2) #Moving the turtle to the first layer of the cake
    cake(length)
    t.exitonclick()

if __name__ == "__main__":
    main()