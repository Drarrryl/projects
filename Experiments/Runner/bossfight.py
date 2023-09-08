import turtle
import time
from gameFunc import inBounds, checkCollide, checkPlatform
from threading import *
class Jump():
    def __init__(self, jumps) -> None:
        self.jumps = jumps

    
    def setJumps(self, num):
        self.jumps = num
    def checkJumps(self, num):
        if self.jumps == num:
            return True
        else:
            return False
    def decreaseJumps(self, num):
        self.jumps -= num
        if self.jumps < 0:
            self.jumps = 0

rightBool = [False]
leftBool = [False]
downBool = [False]
upBool = [False]
jumpedBool = [False]
onGround = [False]
inAir = [False]
jumpCount = Jump(2)
jumping = [False]
level = 9
highScore = 1
bossDir = 1

win = turtle.Screen()
win.title("Runner")
win.bgcolor("light blue")
win.setup(width = 720, height = 360)
win.tracer(0)
grass = turtle.Turtle()
grass.penup()
grass.shape("square")
grass.color("dark green")
grass.shapesize(stretch_wid=4, stretch_len=40)
grass.goto(0, -135)
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.shapesize(outline=1)
player.color("black", "white")
player.goto(-340, -75)
playerdx = 0.2
playerdy = 0.075
maxSpeed = 25
turtle.addshape("eye", ((0, 0), (-5, 0)))
eye = turtle.Turtle()
eye.penup()
eye.shape("eye")
eye.color("black")
eyeLeft = eye.clone()
eyeRight = eye.clone()
eye.hideturtle()

#Staircase
step = turtle.Turtle()
step.color("maroon")
step.shape("square")
step.penup()
print(step.get_shapepoly())
firstStep = step.clone()
firstStep.shapesize(0.5, 3)
firstStep.goto(330, grass.ycor()+45)
secStep = step.clone()
secStep.shapesize(0.5, 2)
secStep.goto(340, firstStep.ycor()+10)
thirdStep = step.clone()
thirdStep.shapesize(0.5, 1)
thirdStep.goto(350, secStep.ycor()+10)
step.hideturtle()

# Generate Labrynth
labFloor = turtle.Turtle()
labFloor.shape("square")
labFloor.shapesize(1.5, 36)
labFloor.color("maroon")
labFloor.penup()
labFloor.goto(0, -165)
labFloor.hideturtle()

labWall = turtle.Turtle()
labWall.shape("square")
labWall.shapesize(18, 1.5)
labWall.color("maroon")
labWall.penup()
labWall.goto(345, 0)
labWall.hideturtle()

labPlat = turtle.Turtle()
labPlat.shape("square")
labPlat.shapesize(1, 4)
labPlat.color("maroon")
labPlat.penup()
labPlat1 = labPlat.clone()
labPlat2 = labPlat.clone()
labPlat3 = labPlat.clone()
labPlat.hideturtle()
labPlat1.hideturtle()
labPlat2.hideturtle()
labPlat3.hideturtle()

boss = turtle.Turtle()
boss.shape("square")
boss.shapesize(5, 5, outline=1)
boss.color("black", "red")
boss.penup()
boss.goto(120, 800)
bossdy = 0
bosseyeLeft = eyeLeft.clone()
bosseyeLeft.shapesize(5, 1)
bosseyeRight = eyeRight.clone()
bosseyeRight.shapesize(5, 1)

win.register_shape("key.gif", shape=None)
key = turtle.Turtle()
key.shape("key.gif")
key.penup()
key.goto(0, 0)
key.hideturtle()

def right():
    x = player.xcor()
    x += playerdx
    player.setx(x)
def left():
    x = player.xcor()
    x -= playerdx
    player.setx(x)

def setUp():
    upBool[0] = True
def setRight():
    rightBool[0] = True
def setLeft():
    leftBool[0] = True
def setDown():
    downBool[0] = True
def unRight():
    rightBool[0] = False
def unLeft():
    leftBool[0] = False
def unDown():
    downBool[0] = False
def unUp():
    upBool[0] = False
    jumpedBool[0] = False

def down():
    if inAir[0] == True:
        y = player.ycor()
        y -= 1
        player.sety(y)

def playerJump(jumpCount):
    if jumpCount.jumps > 0:
        jumping[0] = True
        vel = 0
        for x in range(40):
            y = player.ycor()
            vel += 0.1
            y += vel
            player.sety(y)
            eyeLeft.goto(player.xcor()-5, player.ycor())
            eyeRight.goto(player.xcor()+5, player.ycor())
            win.update()
            #mainloop(level, highScore)
    jumpCount.decreaseJumps(1)
    upBool[0] = False
    jumpedBool[0] = True

def enemyJump(enemy, direction):
    print("Enemy Jumps!")
    if direction == -1:
        vel = 0
        for x in range(80):
            y = enemy.ycor()
            vel += 0.1
            y += vel
            enemy.sety(y)
            bosseyeLeft.goto(boss.xcor()-25, boss.ycor())
            bosseyeRight.goto(boss.xcor()+25, boss.ycor())
            time.sleep(0.01)
    elif direction == 1:
        vel = 0
        for x in range(75):
            y = enemy.ycor()
            vel += 0.1
            y += vel
            enemy.sety(y)
            bosseyeLeft.goto(boss.xcor()-25, boss.ycor())
            bosseyeRight.goto(boss.xcor()+25, boss.ycor())
            win.update()

def levelDesign(level):
    if level == 9:
        win.bgcolor("light blue")
        player.goto(-340, -75)
        firstStep.goto(330, grass.ycor()+45)
        firstStep.showturtle()
        secStep.goto(340, firstStep.ycor()+10)
        secStep.showturtle()
        thirdStep.goto(350, secStep.ycor()+10)
        thirdStep.showturtle()
        grass.showturtle()
        labFloor.hideturtle()
        labWall.hideturtle()
        labWall.goto(345, 0)
        labPlat1.hideturtle()
        labPlat2.hideturtle()
        labPlat3.hideturtle()
        boss.hideturtle()
        bosseyeLeft.hideturtle()
        bosseyeRight.hideturtle()
        bossdy = 0
    elif level >= 9:
        win.bgcolor("brown")
        player.goto(-340, -75)
        firstStep.hideturtle()
        secStep.hideturtle()
        thirdStep.hideturtle()
        grass.hideturtle()
        labFloor.showturtle()
        labWall.showturtle()
        labPlat1.goto(-180, -45)
        labPlat1.showturtle()
        labPlat2.goto(180, -45)
        labPlat2.showturtle()
        labPlat3.goto(0, 90)
        labPlat3.showturtle()
        boss.goto(120, 600)
        boss.showturtle()
        bosseyeLeft.showturtle()
        bosseyeRight.showturtle()
        key.goto(0, 0)
        key.showturtle()
        

win.listen()
win.onkeypress(setUp, "w")
win.onkeypress(setRight, "d")
win.onkeypress(setLeft, "a")
win.onkeypress(setDown, "s")
win.onkeyrelease(unUp, "w")
win.onkeyrelease(unRight, "d")
win.onkeyrelease(unLeft, "a")
win.onkeyrelease(unDown, "s")

while True:
    win.update()
    eyeLeft.goto(player.xcor()-5, player.ycor())
    eyeRight.goto(player.xcor()+5, player.ycor())
    bosseyeLeft.goto(boss.xcor()-25, boss.ycor())
    bosseyeRight.goto(boss.xcor()+25, boss.ycor())

    if onGround[0] == True:
        jumpCount.setJumps(2)
    if upBool[0] == True:
        if jumpedBool[0] == False:
            playerJump(jumpCount)
    if rightBool[0] == True:
        right()
    if leftBool[0] == True:
        left()
    if downBool[0] == True:
        down()

    if level == 9: # Staircase into labrynth level
        if player.ycor() > grass.ycor()+49.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
        else:
            player.goto(player.xcor(), grass.ycor()+50)
            inAir[0] = False
            onGround[0] = True
    elif level == 10: # BOSS LEVEL
        plat = False
        if checkPlatform(player, playerdy, labPlat1, labFloor, inAir, onGround): # Handle player-platform collision for labrynth level
            plat = True
        elif checkPlatform(player, playerdy, labPlat2, labFloor, inAir, onGround):
            plat = True
        elif checkPlatform(player, playerdy, labPlat3, labFloor, inAir, onGround):
            plat = True
        elif player.ycor() > labFloor.ycor()+25:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
        else:
            player.goto(player.xcor(), labFloor.ycor()+25)
            inAir[0] = False
            onGround[0] = True
        
        if boss.ycor() > labFloor.ycor()+65:
            boss.sety(boss.ycor()-bossdy)
        else:
            boss.goto(boss.xcor(), labFloor.ycor()+65)
            bossdy = 0.25
            bossDir*=-1
            boss.sety(boss.ycor()+10)
            child = Thread(target= lambda: enemyJump(boss, bossDir))
            child.run()
        if checkCollide(player, key):
            key.goto(boss.xcor(), boss.ycor())
            bossdy = 1
        if checkCollide(player, boss):
            level = 9
            bossdy = 0
            levelDesign(level)

    if level == 9:
        if player.xcor() > firstStep.xcor()-30 and player.xcor() < firstStep.xcor()+30: # First Step
            if player.ycor() > firstStep.ycor()+15:
                player.sety(player.ycor()-playerdy)
            elif inBounds(player.ycor(), firstStep.ycor(), firstStep.ycor()+20):
                player.goto(player.xcor(), firstStep.ycor()+15)
        if player.xcor() > secStep.xcor()-20 and player.xcor() < secStep.xcor()+20: # Second Step
            if player.ycor() > secStep.ycor()+15:
                player.sety(player.ycor()-playerdy)
            elif inBounds(player.ycor(), secStep.ycor(), secStep.ycor()+20):
                player.goto(player.xcor(), secStep.ycor()+15)
        if player.xcor() > thirdStep.xcor()-10 and player.xcor() < thirdStep.xcor()+10: # Third Step
            if player.ycor() > thirdStep.ycor()+15:
                player.sety(player.ycor()-playerdy)
            elif inBounds(player.ycor(), thirdStep.ycor(), thirdStep.ycor()+20):
                player.goto(player.xcor(), thirdStep.ycor()+15)

    # Handle player-wall collision for labrynth level
    if level == 10:
        if player.xcor() >= labWall.xcor()-25 and player.ycor() >= labWall.ycor()-180:
            player.setx(labWall.xcor()-25)

    # Handle player going off screen
    if player.xcor() >= 350:
        if level == 9:
            level = 10
            levelDesign(level)
        elif level == 10:
            level = 9
            levelDesign(level)
    elif player.xcor() <= -350: 
        player.goto(-350, player.ycor())