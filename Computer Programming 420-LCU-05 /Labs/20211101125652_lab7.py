from turtle import *
def basics():
    forward(100)    #Got an error before importing, draws a line after
    circle(100)
#1b) I get a tracebak
#1c) It draws a line

def draw_polygon(n_sides, x, y, length, color, angle):
    speed(0)
    penup()
    goto(x, y)
    pendown()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for i in range(n_sides):
        forward(length)
        left(angle)
    end_fill()


def testPolygons():
    draw_polygon(5,0,0,20,"blue",90)        #Square
    draw_polygon(8,100,100,40,"blue",45)    #Octagon
    draw_polygon(3,-100,-100,40,"blue",120) #Triangle

def iterative_spiral(n):
    x = n
    speed(0)
    pendown()
    while x > 0:
        circle(x,30)
        x -= 2

def recursive_spiral(n):
    x = n
    speed(0)
    pendown()
    if x > 0:
        circle(x, 30)
        return recursive_spiral(x - 2)

def drawSpirals():
    iterative_spiral(120)
    penup()
    goto(200,200)
    recursive_spiral(120)

def tree(trunkLength, levels):
    pendown()
    x = trunkLength
    y = levels
    if y > 0:
        forward(trunkLength)
        y -= 1
        left(15)
        tree(x, y)
        right(30)
        tree(x, y)
        left(15)
        backward(x)

def drawTree():
    left(90)
    tree(50,10)
    done()

def tree1(trunkLength, levels):
    pendown()
    x = trunkLength
    y = levels
    if y > 0:
        width(levels)
        forward(trunkLength)
        y -= 1
        left(15)
        tree(x, y)
        right(30)
        tree(x, y)
        left(15)
        backward(x)

def drawTree1():
    left(90)
    tree1(50,5)
    done()
drawTree1()