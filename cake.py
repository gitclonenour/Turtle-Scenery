import turtle as t 
import random

def tweak():
     t.pencolor("black")
     t.pensize(3)

def cake(radius):

    # if radius < table 
        layer = random.randint(3,3)
        print("your got", layer, "layers")
        if layer == 1:
            cl_1 = input("what color do you want it to be: ")

            t.fillcolor(cl_1)
            t.begin_fill()
            
            t.forward(radius*3)
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.end_fill()
        elif layer == 2:
            cl_1 = input("what color do you want the first layer to be: ")
            cl_2 = input("what color do you want the second layer to be: ")
            #layer 1
            t.fillcolor(cl_1)
            t.pencolor(cl_1)
            t.begin_fill()
            t.forward(radius*3)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius)
            t.end_fill()
           
           #l1 positioning
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward(radius*3/2 )
            

            
        #layer 2

            t.fillcolor(cl_2)
            t.pencolor(cl_2)
            t.begin_fill()
            t.left(180)
            t.forward((radius*1/3)*3)
            t.left(90)            
            t.forward(radius)
            t.left(90)
            t.forward((radius*1/3)*6)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward((radius*1/3)*3)
            t.end_fill()

            #l2 postioning

            t.left(90)
            t.forward(radius)
            t.right(90)

        else:
            cl_1 = input("what color do you want the first layer to be: ")
            cl_2 = input("what color do you want the second layer to be: ")
            cl_3 = input("what color do you want the third layer to be: ")
            
            #layer 1
            
            
            t.fillcolor(cl_1)
            t.pencolor(cl_1)
            t.begin_fill()
            t.forward(radius*3)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius)
            t.end_fill()
           
           #l1 positioning
            t.left(90)
            t.forward(radius*3)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward(radius*3/2 )
            

            
        #layer 2

            t.fillcolor(cl_2)
            t.pencolor(cl_2)
            t.begin_fill()
            t.left(180)
            t.forward((radius*1/3)*3)
            t.left(90)            
            t.forward(radius)
            t.left(90)
            t.forward((radius*1/3)*6)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward((radius*1/3)*3)
            t.end_fill()

            #l2 postioning

            t.left(90)
            t.forward(radius)
            t.right(90)

            #layer 3

            t.fillcolor(cl_3)
            t.pencolor(cl_3)
            t.begin_fill()
            t.forward((radius*1/3)*2)
            t.left(90)            
            t.forward(radius)
            t.left(90)
            t.forward((radius*1/3)*4)
            t.left(90)
            t.forward(radius)
            t.left(90)
            t.forward((radius*1/3)*2)
            t.end_fill()


        
    # else
        # cake(radius= int(input("please enter the size you want for the cake: ")))



def test_main():
    length = int(input("please enter the size you want for the cake: "))
    
    tweak()
    cake(radius= length)
    input("please press enter to leave: ")

if __name__ == "__main__":
    test_main()