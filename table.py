import turtle as t

t.speed(5)

def draw_table(length, height, color):
    #table top
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(0,0)  
    t.pendown()
    t.forward(length/2)    
    t.right(90)
    t.forward(height)    
    t.right(90)
    t.forward(length)   
    t.right(90)
    t.forward(height)     
    t.right(90)
    t.forward(length/2)
    t.end_fill()
    t.penup()
    
    #legs
    t.goto(0,-height)
    t.setheading(180)
    t.forward((length/2)*0.9)

    t.pendown()
    t.setheading(270)
    t.forward(100)
    t.penup()

    t.goto(0,-height)
    t.setheading(180)
    t.forward((length/2)*0.6)

    t.pendown()
    t.setheading(270)
    t.forward(80)
    t.penup()

    t.goto(0,-height)
    t.setheading(0)
    t.forward((length/2)*0.9)

    t.pendown()
    t.setheading(270)
    t.forward(100)
    t.penup()

    t.goto(0,-height)
    t.setheading(0)
    t.forward((length/2)*0.6)

    t.pendown()
    t.setheading(270)
    t.forward(80)
    t.penup()

draw_table(200, 20, "blue")
t.exitonclick()