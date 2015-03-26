import turtle
from turtle import *
turtle.pd()
turtle.speed(1000)
finish=False
shape=True
Color=0
size=30

def circle(x,y,size):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.begin_fill()
	turtle.circle(size)
	turtle.end_fill()


def square(x,y,size):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.begin_fill()
	for x in range(0,4):
		turtle.lt(90)
		turtle.forward(size*1.5)
	turtle.end_fill()
	
#def meetsign(arg,move,align,font):
        #turtle.write("MEET", move=False, align="center", font=("Arial", 20, "normal"))


def finish():
        clear()   


def switch():
	global shape
	shape = not shape


def draw(x,y):              
	global shape
	global size
	if shape:
		circle(x,y,size)
	else:
		square(x,y,size)
	#else:
                #meetsign(arg,move,align,font)


def color():
	global Color
	if Color==3:
		Color=0
	Color=Color+1
	if Color==1:
		turtle.color("Blue")
	elif Color==2:
		turtle.color("Green")
	elif Color==3:
		turtle.color("Red")
	#elif Color==4:
                #turtle.color("navy")
		

#Sadek, may you please check why the "navy" function doesn't work?

def Bigger():
	global size
	size=size+10


def Smaller():
	global size
	size=size-10


turtle.getscreen().onkeypress(finish,"e")

turtle.getscreen().onkeypress(switch,"s"or"S")

turtle.getscreen().onkeypress(color,"c"or"C")

turtle.getscreen().onkeypress(Bigger,"8")

turtle.getscreen().onkeypress(Smaller,"9")

turtle.ondrag(draw,1,add=True)

turtle.onscreenclick(draw)

turtle.pu()

turtle.getscreen().listen()

turtle.mainloop()

