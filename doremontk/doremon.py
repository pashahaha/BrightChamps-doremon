from turtle import *

setup(500,500)
speed(5)
bgcolor('black')
shape('turtle')

def drawRound(size, filled):
    pendown()
    if filled == True:
        begin_fill()
    setheading(180)
    circle(size, 360)
    if filled == True:
        end_fill()

def drawRect(length, width, filled):
    pendown()
    if filled == True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled == True:
        end_fill()

def head():
    color('blue', 'blue')
    penup()
    goto(0, 100)
    drawRound(25, True)
    color('white', 'white')
    penup()
    goto(0, 72)
    drawRound(60, True)

def eyes():
    color("black", "white")
    penup()
    goto(-15, 80)
    drawRound(17, True)
    color("black", "white")
    penup()
    goto(19,80)
    drawRound(17, True)
    color("black", "black")
    penup() 
    goto(-8, 70)
    drawRound(6, True)
    color("white", "white")
    penup()
    goto(-8,66)
    drawRound(2, True)
    color("black", "black")
    penup()
    goto(12, 70)
    drawRound(6, True)
    color("white", "white")
    penup()
    goto(12, 66)
    drawRound(2, True)

def nose():
    color('red', 'red')
    penup()
    goto(0, 40)
    drawRound(7, True)

def mouth():
    color('black', 'black')
    penup()
    goto(-30, -20)
    pendown()
    setheading(-27)
    circle(30, 60)
    penup()
    goto(0, 26)
    pendown()
    goto(0, -25)

def body():
    color('blue', 'blue')
    penup()
    goto(0, -35)
    drawRound(50, True)
    color('white', 'white')
    penup()
    goto(0, -35)
    drawRound(40, True)
    color('red', 'red')
    penup()
    goto(35, -30)
    drawRect(80, 10, True)
    color('white', 'white')
    penup()
    goto(15, -27)
    pendown()
    setheading(0)
    begin_fill()
    circle(14, 180)
    end_fill()

def feet():
    color('black', 'white')
    penup()
    goto(-30, -110)
    drawRound(20, True)
    color('black', 'white')
    penup()
    goto(30, -110)
    drawRound(20, True)

def arms():
    color('blue', 'blue')
    penup()
    begin_fill()
    goto(45, -50)
    pendown()
    drawRound(15, True)
    color('red', 'red')
    penup()
    goto(-45, -50)
    drawRound(15, True)
    color('blue', 'blue')
    pendown()


if __name__ == '__main__':
    head()
    eyes()
    nose()
    mouth()
    body()
    feet()
    arms()