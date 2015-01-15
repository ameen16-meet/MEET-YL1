import turtle
from turtle import *

turtle.speed(1000)
ht()
size = 10




def blanksquare(x,y):
    global size,color
    pu()
    goto(x,y) 
    pd(x,y)
    forward(50)
    lt(90)  
    forward(50)
    lt(90)
    forward(50)
    lt(90)
    forward(50)
    pu()

def fillsquare(x,y):
    global size
    pu()
    goto(x,y)
    pd()
    begin_fill()
    fillcolor(color)
    forward(50)
    lt(90)  
    forward(50)
    lt(90)
    forward(50)
    lt(90)
    forward(50)
    pu()
    end_fill()

def circle(x,y):
    global size
    begin_fill()
    fillcolor(color)
    pu()
    goto(x,y)
    pd()
    turtle.circle(50)
    #myfun1()
    #myfun2()
    end_fill
    
    

def togreen():
    turtle.fillcolor("green")

def tored():
    turtle.fillcolor("red")

def myfun2():
    turtle.fillcolor("green")
    turtle.getscreen().onkeypress(myfun2,"2")
    turtle.getscreen().listen()    

def draw_square2():
    turtle.onscreenclick(fillsquare, btn = 1, add = False)
    turtle.pu()

def draw_circle2():
    turtle.onscreenclick(circle, btn = 1, add = False)
    turtle.pu()




turtle.getscreen().onkeypress(draw_square2 , "s")
turtle.getscreen().onkeypress(draw_circle2 , "c")


turtle.listen()
turtle.mainloop
