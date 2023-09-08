import turtle

rightBool = [False]
leftBool = [False]
upBool = [False]
downBool = [False]

win = turtle.Screen()
win.setup(width=720, height=720)
win.bgcolor("black")
win.tracer(0)

block = turtle.Turtle()
block.shape("square")
block.color("white")
block.penup()
blockdx = 0.05
blockdy = 0.05

trail = turtle.Turtle()
trail.hideturtle()
ext = turtle.Turtle()
ext.hideturtle()

def setRight():
    rightBool[0] = True
def setLeft():
    leftBool[0] = True
def setUp():
    upBool[0] = True
def setDown():
    downBool[0] = True

def unRight():
    rightBool[0] = False
def unLeft():
    leftBool[0] = False
def unUp():
    upBool[0] = False
def unDown():
    downBool[0] = False

def right():
    x = block.xcor()
    x += blockdx
    block.setx(x)
def left():
    x = block.xcor()
    x -= blockdx
    block.setx(x)
def up():
    y = block.ycor()
    y += blockdy
    block.sety(y)
def down():
    y = block.ycor()
    y -= blockdy
    block.sety(y)
win.listen()
win.onkeypress(setRight, "d")
win.onkeyrelease(unRight, "d")
win.onkeypress(setLeft, "a")
win.onkeyrelease(unLeft, "a")
win.onkeypress(setUp, "w")
win.onkeyrelease(unUp, "w")
win.onkeypress(setDown, "s")
win.onkeyrelease(unDown, "s")



while True:
    win.update()
    if rightBool[0] == True:
        distS = block.xcor()
        right()
        distE = block.xcor()
        dist = (distE - distS)+10
        xOffset = block.xcor()-dist-10
        yOffset = block.ycor()+10
        turtle.addshape("trail", ((0, 0), (0, dist), (20, dist), (20, 0)))
        trail.showturtle()
        trail.shape("trail")
        trail.color("orange")
        trail.penup()
        trail.goto(xOffset, yOffset)
        ext.showturtle()
        ext.shape("trail")
        ext.color("orange")
        ext.penup()
        ext.goto(xOffset-dist, yOffset)
        mult = 0
        for i in range(1):
            ext.shape("trail")
            ext.color("orange")
            ext.penup()
            mult += 10
            ext.goto(xOffset-dist, yOffset)
        ext.clear()
        trail.clear()
    if leftBool[0] == True:
        distS = block.xcor()
        left()
        distE = block.xcor()
        dist = (distE - distS)+10
        turtle.addshape("trail", ((0, 0), (0, dist), (20, dist), (20, 0)))
        trail.showturtle()
        trail.shape("trail")
        trail.color("orange")
        trail.penup()
        trail.goto(block.xcor()+dist, block.ycor()+10)
        trail.clear()
    if upBool[0] == True:
        distS = block.xcor()
        up()
        distE = block.xcor()
        dist = (distE - distS)+10
        turtle.addshape("trail", ((0, 0), (dist, 0), (dist, 20), (0, 20)))
        trail.showturtle()
        trail.shape("trail")
        trail.color("orange")
        trail.penup()
        trail.goto(block.xcor()-10, block.ycor()-dist)
        trail.clear()
    if downBool[0] == True:
        distS = block.xcor()
        down()
        distE = block.xcor()
        dist = (distE - distS)+10
        turtle.addshape("trail", ((0, 0), (dist, 0), (dist, 20), (0, 20)))
        trail.showturtle()
        trail.shape("trail")
        trail.color("orange")
        trail.penup()
        trail.goto(block.xcor()-10, block.ycor()+dist+10)
        trail.clear()
