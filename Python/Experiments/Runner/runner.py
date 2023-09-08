import turtle
import random
import time
from PIL import Image
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
level = 1
highScore = 1

counter = []
# Generate Window
win = turtle.Screen()
win.title("Runner")
win.bgcolor("light blue")
win.setup(width = 720, height = 360)
win.tracer(0)


# Generate Score
score = turtle.Turtle()
score.color("black")
score.hideturtle()
score.penup()
score.goto(0, 150)
score.write("Level {}".format(level), align = "center", font = ("Courier", 14, "normal"))

# Generate Background
grass = turtle.Turtle()
grass.penup()
grass.shape("square")
grass.color("dark green")
grass.shapesize(stretch_wid=4, stretch_len=40)
grass.goto(0, -135)

turtle.register_shape("clouds2.gif", shape=None)
cloud = turtle.Turtle()
cloud.penup()
cloud.shape("clouds2.gif")
cloud.goto(0, 0)

# Generate Movable Scenary
platform = turtle.Turtle()
platform.penup()
platform.shape("square")
platform.color("brown")
platform.shapesize(stretch_len=4, stretch_wid=1)
a1 = platform.clone()
a2 = platform.clone()
a3 = platform.clone()
a1.goto(-180, 0)
a2.goto(0, 0)
a3.goto(180, 0)
platform.hideturtle()

turtle.addshape("door.gif", shape=None)
door = turtle.Turtle()
door.shape("door.gif")
door.penup()
door.goto(340, 80)
print(door.shape())
file = Image.open(door.shape())
print(file.size)
# Create Player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.shapesize(stretch_len=1, outline=1)
player.color("black", "white")
player.goto(-340, -75)
playerdx = 0.5
playerdy = 0.1
maxSpeed = 25
turtle.addshape("eye", ((0, 0), (-5, 0)))
eye = turtle.Turtle()
eye.penup()
eye.shape("eye")
eye.color("black")
eyeLeft = eye.clone()
eyeRight = eye.clone()
eye.hideturtle()

# Create Trail
trail = turtle.Turtle()
trail.speed(0)
trail.shape("square")
trail.shapesize(stretch_len=1, stretch_wid=1)
trail.color("black")
trail.penup()
trail.hideturtle()

# Create Enemies
enemy = turtle.Turtle()
enemy.speed(0)
enemy.penup()
enemy.shape("square")
enemy.shapesize(stretch_len=1, outline=1)
enemy.color("black", "red")
enemy.goto(0, -60)
enemy.hideturtle()
enemydx = 0.1
enemydy = 0.1
enemyEyeLeft = eye.clone()
enemyEyeRight = eye.clone()

enemy1 = enemy.clone()
enemy1EyeLeft = eye.clone()
enemy1EyeRight = eye.clone()
enemy1dy = 0.1

enemy2 = enemy.clone()
enemy2EyeLeft = eye.clone()
enemy2EyeRight = eye.clone()
enemy2dy = 0.1
reverse = [False]
enemyPlace = []

# Create death objects
turtle.addshape("spikes", ((0, 0), (-5, 5), (0, 10), (-5, 15), (0, 20), (-5, 25), (0, 30), (-5, 35), (0, 40), (-5, 45), (0, 50)))
turtle.addshape("spikes1", ((0, 0), (-5, 5), (0, 10), (-5, 15), (0, 20), (-5, 25), (0, 30), (-5, 35), (0, 40), (-5, 45), (0, 50)))
turtle.addshape("spikes2", ((0, 0), (-5, 5), (0, 10), (-5, 15), (0, 20), (-5, 25), (0, 30), (-5, 35), (0, 40), (-5, 45), (0, 50)))
turtle.addshape("spikes3", ((0, 0), (-5, 5), (0, 10), (-5, 15), (0, 20), (-5, 25), (0, 30), (-5, 35), (0, 40), (-5, 45), (0, 50)))
deathPlate = turtle.Turtle()
deathPlate.shape("spikes")
deathPlate.penup()
deathPlate.color("red")
deathPlate.goto(door.xcor()-40, grass.ycor()+40)
dPCenter = turtle.Turtle()
dPCenter.penup()
dPCenter.goto(deathPlate.xcor()+25, deathPlate.ycor()+2.5)
dPCenter.hideturtle()

d1 = turtle.Turtle()
d1.shape("spikes1")
d1.penup()
d1.color("red")
d1.goto(a1.xcor()-25, grass.ycor()+40)
d1.hideturtle()
d1PCenter = turtle.Turtle()
d1PCenter.penup()
d1PCenter.goto(d1.xcor()+25, d1.ycor()+2.5)
d1PCenter.hideturtle()

d2 = turtle.Turtle()
d2.shape("spikes2")
d2.penup()
d2.color("red")
d2.goto(a2.xcor()-25, grass.ycor()+40)
d2.hideturtle()
d2PCenter = turtle.Turtle()
d2PCenter.penup()
d2PCenter.goto(d2.xcor()+25, d2.ycor()+2.5)
d2PCenter.hideturtle()

d3 = turtle.Turtle()
d3.shape("spikes3")
d3.penup()
d3.color("red")
d3.goto(a3.xcor()-25, grass.ycor()+40)
d3.hideturtle()
d3PCenter = turtle.Turtle()
d3PCenter.penup()
d3PCenter.goto(d3.xcor()+25, d3.ycor()+2.5)
d3PCenter.hideturtle()

#Staircase
step = turtle.Turtle()
step.color("maroon")
step.shape("square")
step.penup()
print(step.get_shapepoly())
firstStep = step.clone()
firstStep.shapesize(0.5, 3)
firstStep.goto(330, grass.ycor()+45)
firstStep.hideturtle()
secStep = step.clone()
secStep.shapesize(0.5, 2)
secStep.goto(340, firstStep.ycor()+10)
secStep.hideturtle()
thirdStep = step.clone()
thirdStep.shapesize(0.5, 1)
thirdStep.goto(350, secStep.ycor()+10)
thirdStep.hideturtle()
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
boss.hideturtle()
bossdy = 0
bosseyeLeft = eyeLeft.clone()
bosseyeLeft.shapesize(5, 1)
bosseyeRight = eyeRight.clone()
bosseyeRight.shapesize(5, 1)
bosseyeLeft.hideturtle()
bosseyeRight.hideturtle()

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
def checkHigh(level, high):
    if level > high:
        return level
    else:
        return high
def inBounds(target, lower, upper):
    if lower <= target <= upper:
        return True
    else:
        return False
def checkCollide(player, object):
    bound = 0
    found = str(object.shape()).find("gif")
    if (str(object.shape()).find("gif") > -1):
        file = Image.open(object.shape())
        width, height = file.size
        bound = width/2
    elif object.shape() == "spikes":
        if inBounds(player.towards(dPCenter), 180, 250) or inBounds(player.towards(dPCenter), 290, 360): # Check if player is to the right or left of spikes
            sidels = []
            for x, y in object.get_shapepoly():
                sidels.append(y)
            sidels.sort()
            ylow = sidels[0]
            yhigh = sidels[len(sidels)-1]
            ylen = yhigh - ylow
            bound = (ylen/2)+1
        if inBounds(player.towards(dPCenter), 250, 290): # Check if player is above spikes
            upls = []
            for x, y in object.get_shapepoly():
                upls.append(x)
            upls.sort()
            xlow = upls[0]
            xhigh = upls[len(upls)-1]
            xlen = xhigh - xlow
            bound = (xlen/2)+1
        if player.distance(dPCenter) < bound+5:
            return True
        else:
            return False
    elif object.shape() == "spikes1":
        if inBounds(player.towards(d1PCenter), 180, 250) or inBounds(player.towards(d1PCenter), 290, 360): # Check if player is to the right or left of spikes
            sidels = []
            for x, y in object.get_shapepoly():
                sidels.append(y)
            sidels.sort()
            ylow = sidels[0]
            yhigh = sidels[len(sidels)-1]
            ylen = yhigh - ylow
            bound = (ylen/2)+1
        if inBounds(player.towards(d1PCenter), 250, 290): # Check if player is above spikes
            upls = []
            for x, y in object.get_shapepoly():
                upls.append(x)
            upls.sort()
            xlow = upls[0]
            xhigh = upls[len(upls)-1]
            xlen = xhigh - xlow
            bound = (xlen/2)+1
        if player.distance(d1PCenter) < bound+5:
            return True
        else:
            return False
    elif object.shape() == "spikes2":
        if inBounds(player.towards(d2PCenter), 180, 250) or inBounds(player.towards(d2PCenter), 290, 360): # Check if player is to the right or left of spikes
            sidels = []
            for x, y in object.get_shapepoly():
                sidels.append(y)
            sidels.sort()
            ylow = sidels[0]
            yhigh = sidels[len(sidels)-1]
            ylen = yhigh - ylow
            bound = (ylen/2)+1
        if inBounds(player.towards(d2PCenter), 250, 290): # Check if player is above spikes
            upls = []
            for x, y in object.get_shapepoly():
                upls.append(x)
            upls.sort()
            xlow = upls[0]
            xhigh = upls[len(upls)-1]
            xlen = xhigh - xlow
            bound = (xlen/2)+1
        if player.distance(d2PCenter) < bound+5:
            return True
        else:
            return False
    elif object.shape() == "spikes3":
        if inBounds(player.towards(d3PCenter), 180, 250) or inBounds(player.towards(d3PCenter), 290, 360): # Check if player is to the right or left of spikes
            sidels = []
            for x, y in object.get_shapepoly():
                sidels.append(y)
            sidels.sort()
            ylow = sidels[0]
            yhigh = sidels[len(sidels)-1]
            ylen = yhigh - ylow
            bound = (ylen/2)+1
        if inBounds(player.towards(d3PCenter), 250, 290): # Check if player is above spikes
            upls = []
            for x, y in object.get_shapepoly():
                upls.append(x)
            upls.sort()
            xlow = upls[0]
            xhigh = upls[len(upls)-1]
            xlen = xhigh - xlow
            bound = (xlen/2)+1
        if player.distance(d3PCenter) < bound+5:
            return True
        else:
            return False
    else:
        if inBounds(player.towards(object), 270, 360) or inBounds(player.towards(object), 90, 180): # Left
            sidels = []
            for x, y in object.get_shapepoly():
                sidels.append(y)
            sidels.sort()
            ylow = sidels[0]
            yhigh = sidels[len(sidels)-1]
            ylen = yhigh - ylow
            bound = (ylen/2)+1
        if inBounds(player.towards(object), 180, 270) or inBounds(player.towards(object), 0, 90): # Right
            upls = []
            for x, y in object.get_shapepoly():
                upls.append(x)
            upls.sort()
            xlow = upls[0]
            xhigh = upls[len(upls)-1]
            xlen = xhigh - xlow
            bound = (xlen/2)+1
    if player.distance(object) < bound+5:
        return True
    else:
        return False

def checkPlatform(player, playerdy, platform, grass, inAir, onGround):
    xls = []
    yls = []
    ls = platform.get_shapepoly()
    for y, x in ls:
        xls.append(x)
        yls.append(y)
    xls.sort()
    yls.sort()
    greatY = yls[len(yls)-1] - yls[0]
    dist = xls[len(xls)-1]+10

    gls = []
    ls = grass.get_shapepoly()
    for y, x in ls:
        gls.append(y)
    gls.sort()
    grassY = gls[len(gls)-1]+10

    if player.xcor() > platform.xcor()-dist and player.xcor() < platform.xcor()+dist: # Check plr inBounds x-axis
        if player.ycor() > platform.ycor()+(greatY-0.2):
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
        elif inBounds(player.ycor(), platform.ycor(), platform.ycor()+greatY):
            player.goto(player.xcor(), platform.ycor()+greatY)
            inAir[0] = False
            onGround[0] = True
        elif player.ycor() > grass.ycor()+(grassY-0.2):
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
        else:
            player.goto(player.xcor(), grass.ycor()+grassY)
            inAir[0] = False
            onGround[0] = True
        return True
    else:
        return False


def onPlatform(enemy, a1, a2, a3, reverse):
    if inBounds(enemy.xcor(), a1.xcor()-50, a1.xcor()+50):
        if enemy.xcor() > a1.xcor()+25:
            reverse[0] = True
        if enemy.xcor() <= a1.xcor()-25:
            reverse[0] = False
        if reverse[0] == False:
            enemy.forward(enemydx)
        elif reverse[0] == True:
            enemy.backward(enemydx)
    elif inBounds(enemy.xcor(), a2.xcor()-50, a2.xcor()+50):
        if enemy.xcor() > a2.xcor()+25:
            reverse[0] = True
        
        if enemy.xcor() <= a2.xcor()-25:
            reverse[0] = False
        if reverse[0] == False:
            enemy.forward(enemydx)
        elif reverse[0] == True:
            enemy.backward(enemydx)
    elif inBounds(enemy.xcor(), a3.xcor()-50, a3.xcor()+50):
        if enemy.xcor() > a3.xcor()+25:
            reverse[0] = True
        
        if enemy.xcor() <= a3.xcor()-25:
            reverse[0] = False
        if reverse[0] == False:
            enemy.forward(enemydx)
        elif reverse[0] == True:
            enemy.backward(enemydx)

def levelDesign(level):
    if level == 1:
        win.bgcolor("light blue")
        player.goto(-340, -75)
        a1.goto(-180, 0)
        a2.goto(0, 0)
        a3.goto(180, 0)
        door.goto(340, 80)
        enemy.hideturtle()
        enemyEyeLeft.hideturtle()
        enemyEyeRight.hideturtle()
        enemy1.hideturtle()
        enemy1EyeLeft.hideturtle()
        enemy1EyeRight.hideturtle()
        enemy2.hideturtle()
        enemy2EyeLeft.hideturtle()
        enemy2EyeRight.hideturtle()
        deathPlate.showturtle()
        d1.hideturtle()
        d2.hideturtle()
        d3.hideturtle()
    elif level == 2:
        player.goto(-340, -75)
        a1y = -30
        a2y = 65
        a3y = 80
        a1.goto(-180, a1y)
        a2.goto(0, a2y)
        a3.goto(180, a3y)
        cloud.speed(6)
        doory = random.randint(60, 120)
        door.goto(340, doory)
        platRand = random.randint(1, 3)
        if platRand == 1:
            enemy.goto(a1.xcor(), a1.ycor()+25)
        elif platRand == 2:
            enemy.goto(a2.xcor(), a2.ycor()+25)
        elif platRand == 3:
            enemy.goto(a3.xcor(), a3.ycor()+25)
        enemy.showturtle()
        enemyEyeLeft.showturtle()
        enemyEyeRight.showturtle()
    elif level == 3:
        player.goto(-340, -75)
        a1y = -30
        a2y = 65
        a3y = 80
        a1.goto(-180, a1y)
        a2.goto(0, a2y)
        a3.goto(180, a3y)
        cloud.speed(6)
        doory = random.randint(60, 120)
        door.goto(340, doory)
        platRand = random.randint(1, 3)
        if platRand == 1:
            enemy.goto(a1.xcor(), a1.ycor()+25)
            platRand = random.randint(1, 2)
            if platRand == 1:
                enemy1.goto(a2.xcor(), a2.ycor()+25)
            else:
                enemy1.goto(a3.xcor(), a3.ycor()+25)
        elif platRand == 2:
            platRand = random.randint(1, 2)
            enemy.goto(a2.xcor(), a2.ycor()+25)
            if platRand == 1:
                enemy1.goto(a1.xcor(), a1.ycor()+25)
            else:
                enemy1.goto(a3.xcor(), a3.ycor()+25)
        elif platRand == 3:
            platRand = random.randint(1, 2)
            enemy.goto(a3.xcor(), a3.ycor()+25)
            if platRand == 1:
                enemy1.goto(a1.xcor(), a1.ycor()+25)
            else:
                enemy1.goto(a2.xcor(), a2.ycor()+25)
        enemy1.showturtle()
        enemy1EyeLeft.showturtle()
        enemy1EyeRight.showturtle()
    elif level == 4:
        player.goto(-340, -75)
        a1y = -30
        a2y = 65
        a3y = 80
        a1.goto(-180, a1y)
        a2.goto(0, a2y)
        a3.goto(180, a3y)
        cloud.speed(6)
        doory = random.randint(60, 120)
        door.goto(340, doory)
        platRand = random.randint(1, 3)
        if platRand == 1:
            enemy.goto(a1.xcor(), a1.ycor()+25)
            platRand = random.randint(1, 2)
            if platRand == 1:
                enemy1.goto(a2.xcor(), a2.ycor()+25)
                enemy2.goto(a3.xcor(), a3.ycor()+25)
            else:
                enemy1.goto(a3.xcor(), a3.ycor()+25)
                enemy2.goto(a2.xcor(), a2.ycor()+25)
        elif platRand == 2:
            platRand = random.randint(1, 2)
            enemy.goto(a2.xcor(), a2.ycor()+25)
            if platRand == 1:
                enemy1.goto(a1.xcor(), a1.ycor()+25)
                enemy2.goto(a3.xcor(), a3.ycor()+25)
            else:
                enemy1.goto(a3.xcor(), a3.ycor()+25)
                enemy2.goto(a1.xcor(), a1.ycor()+25)
        elif platRand == 3:
            platRand = random.randint(1, 2)
            enemy.goto(a3.xcor(), a3.ycor()+25)
            if platRand == 1:
                enemy1.goto(a1.xcor(), a1.ycor()+25)
                enemy2.goto(a2.xcor(), a2.ycor()+25)
            else:
                enemy1.goto(a2.xcor(), a2.ycor()+25)
                enemy2.goto(a1.xcor(), a1.ycor()+25)
        enemy2.showturtle()
        enemy2EyeLeft.showturtle()
        enemy2EyeRight.showturtle()
    elif level == 5:
        player.goto(-340, -75)
        a1y = random.randint(-80, 80)
        a2y = random.randint(-80, 80)
        a3y = random.randint(-30, 80)
        a1.goto(-180, a1y)
        a2.goto(0, a2y)
        a3.goto(180, a3y)
        cloud.speed(6)
        doory = random.randint(60, 120)
        door.goto(340, doory)
        deathPlate.goto(door.xcor()-40, grass.ycor()+40)
        platRand = random.randint(1, 3)
        if platRand == 1:
            enemy.goto(a1.xcor(), a1.ycor()+25)
            platRand = random.randint(1, 2)
            if platRand == 1:
                enemy1.goto(a2.xcor(), a2.ycor()+25)
                enemy2.goto(a3.xcor(), a3.ycor()+25)
            else:
                enemy1.goto(a3.xcor(), a3.ycor()+25)
                enemy2.goto(a2.xcor(), a2.ycor()+25)
        elif platRand == 2:
            platRand = random.randint(1, 2)
            enemy.goto(a2.xcor(), a2.ycor()+25)
            if platRand == 1:
                enemy1.goto(a1.xcor(), a1.ycor()+25)
                enemy2.goto(a3.xcor(), a3.ycor()+25)
            else:
                enemy1.goto(a3.xcor(), a3.ycor()+25)
                enemy2.goto(a1.xcor(), a1.ycor()+25)
        elif platRand == 3:
            platRand = random.randint(1, 2)
            enemy.goto(a3.xcor(), a3.ycor()+25)
            if platRand == 1:
                enemy1.goto(a1.xcor(), a1.ycor()+25)
                enemy2.goto(a2.xcor(), a2.ycor()+25)
            else:
                enemy1.goto(a2.xcor(), a2.ycor()+25)
                enemy2.goto(a1.xcor(), a1.ycor()+25)
        enemy2.showturtle()
        enemy2EyeLeft.showturtle()
        enemy2EyeRight.showturtle()
        deathPlate.showturtle()
    elif level == 6:
        levelDesign(5)
        d1.showturtle()
    elif level == 7:
        levelDesign(6)
        d2.showturtle()
    elif level == 8:
        levelDesign(7)
        d3.showturtle()
    elif level == 9:
        levelDesign(1)
        a1.hideturtle()
        a2.hideturtle()
        a3.hideturtle()
        deathPlate.hideturtle()
        door.hideturtle()
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
    elif level == 10:
        win.bgcolor("brown")
        cloud.hideturtle()
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
        
    

# Keyboard Functions
win.listen()
win.onkeypress(setUp, "w")
win.onkeypress(setRight, "d")
win.onkeypress(setLeft, "a")
win.onkeypress(setDown, "s")
win.onkeyrelease(unUp, "w")
win.onkeyrelease(unRight, "d")
win.onkeyrelease(unLeft, "a")
win.onkeyrelease(unDown, "s")

"""def inBounds(target, lower, upper):
    target = round(target, 1)
    ls = []
    for x in range((upper-lower)*10):
        ls.append(x/10+lower)
    for i in ls:
        if target == i:
            return True
    return False"""

levelDesign(level)

def mainLoop(level, highScore):
    while True:
        win.update()
        eyeLeft.goto(player.xcor()-5, player.ycor())
        eyeRight.goto(player.xcor()+5, player.ycor())
        enemyEyeLeft.goto(enemy.xcor()-5, enemy.ycor())
        enemyEyeRight.goto(enemy.xcor()+5, enemy.ycor())
        enemy1EyeLeft.goto(enemy1.xcor()-5, enemy1.ycor())
        enemy1EyeRight.goto(enemy1.xcor()+5, enemy1.ycor())
        enemy2EyeLeft.goto(enemy2.xcor()-5, enemy2.ycor())
        enemy2EyeRight.goto(enemy2.xcor()+5, enemy2.ycor())

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
        
        # Handle movement of enemy on each platform
        if level == 2:
            onPlatform(enemy, a1, a2, a3, reverse)
        elif level == 3:
            onPlatform(enemy, a1, a2, a3, reverse)
            onPlatform(enemy1, a1, a2, a3, reverse)
        elif level >= 4:
            onPlatform(enemy, a1, a2, a3, reverse)
            onPlatform(enemy1, a1, a2, a3, reverse)
            onPlatform(enemy2, a1, a2, a3, reverse)
        
        
        # Handle enemy clipping through ground
        if enemy.ycor() > grass.ycor()+50:
            enemy.sety(enemy.ycor()-enemydx)
        else:
            enemy.goto(enemy.xcor(), grass.ycor()+50)
        """
        # Handle player clipping through platform and ground
        if player.xcor() > a1.xcor()-50 and player.xcor() < a1.xcor()+50: # Platform a1
            if player.ycor() > a1.ycor()+19.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
            elif inBounds(player.ycor(), a1.ycor(), a1.ycor()+20):
                player.goto(player.xcor(), a1.ycor()+20)
                inAir[0] = False
                onGround[0] = True
            elif player.ycor() > grass.ycor()+49.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
            else:
                player.goto(player.xcor(), grass.ycor()+50)
                inAir[0] = False
                onGround[0] = True"""
        """    if player.xcor() > a2.xcor()-50 and player.xcor() < a2.xcor()+50: # Platform a2
            if player.ycor() > a2.ycor()+19.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
            elif inBounds(player.ycor(), a2.ycor(), a2.ycor()+20):
                player.goto(player.xcor(), a2.ycor()+20)
                inAir[0] = False
                onGround[0] = True
            elif player.ycor() > grass.ycor()+49.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
            else:
                player.goto(player.xcor(), grass.ycor()+50)
                inAir[0] = False
                onGround[0] = True
        elif player.xcor() > a3.xcor()-50 and player.xcor() < a3.xcor()+50: # Platform a3
            if player.ycor() > a3.ycor()+19.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
            elif inBounds(player.ycor(), a3.ycor(), a3.ycor()+20):
                player.goto(player.xcor(), a3.ycor()+20)
                inAir[0] = False
                onGround[0] = True
            elif player.ycor() > grass.ycor()+49.8:
                player.sety(player.ycor()-playerdy)
                inAir[0] = True
                onGround[0] = False
            else:
                player.goto(player.xcor(), grass.ycor()+50)
                inAir[0] = False
                onGround[0] = True"""
        plat = False
        if checkPlatform(player, playerdy, a1, grass, inAir, onGround):
            plat = True
        elif checkPlatform(player, playerdy, a2, grass, inAir, onGround):
            plat = True
        elif checkPlatform(player, playerdy, a3, grass, inAir, onGround):
            plat = True
        elif player.ycor() > grass.ycor()+49.8:
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
        else:
            player.goto(player.xcor(), grass.ycor()+50)
            inAir[0] = False
            onGround[0] = True

        # Handle enemy clipping through platform
        if enemy.xcor() > a1.xcor()-50 and enemy.xcor() < a1.xcor()+50: # Platform a1
            if enemy.ycor() > a1.ycor()+19.8:
                enemy.sety(enemy.ycor()-enemydy)
            elif inBounds(enemy.ycor(), a1.ycor(), a1.ycor()+20):
                enemy.goto(enemy.xcor(), a1.ycor()+20)

        elif enemy.xcor() > a2.xcor()-50 and enemy.xcor() < a2.xcor()+50: # Platform a2
            if enemy.ycor() > a2.ycor()+19.8:
                enemy.sety(enemy.ycor()-enemydy)
            elif inBounds(enemy.ycor(), a2.ycor(), a2.ycor()+20):
                enemy.goto(enemy.xcor(), a2.ycor()+20)

        elif enemy.xcor() > a3.xcor()-50 and enemy.xcor() < a3.xcor()+50: # Platform a3
            if enemy.ycor() > a3.ycor()+19.8:
                enemy.sety(enemy.ycor()-enemydy)
            elif inBounds(enemy.ycor(), a3.ycor(), a3.ycor()+20):
                enemy.goto(enemy.xcor(), a3.ycor()+20)
        
        # Enemy 1
        if enemy1.xcor() > a1.xcor()-50 and enemy1.xcor() < a1.xcor()+50: # Platform a1
            if enemy1.ycor() > a1.ycor()+19.8:
                enemy1.sety(enemy1.ycor()-enemy1dy)
            elif inBounds(enemy1.ycor(), a1.ycor(), a1.ycor()+20):
                enemy1.goto(enemy1.xcor(), a1.ycor()+20)

        elif enemy1.xcor() > a2.xcor()-50 and enemy1.xcor() < a2.xcor()+50: # Platform a2
            if enemy1.ycor() > a2.ycor()+19.8:
                enemy1.sety(enemy1.ycor()-enemy1dy)
            elif inBounds(enemy1.ycor(), a2.ycor(), a2.ycor()+20):
                enemy1.goto(enemy1.xcor(), a2.ycor()+20)

        elif enemy1.xcor() > a3.xcor()-50 and enemy1.xcor() < a3.xcor()+50: # Platform a3
            if enemy1.ycor() > a3.ycor()+19.8:
                enemy1.sety(enemy1.ycor()-enemy1dy)
            elif inBounds(enemy1.ycor(), a3.ycor(), a3.ycor()+20):
                enemy1.goto(enemy1.xcor(), a3.ycor()+20)

        # Enemy 2
        if enemy2.xcor() > a1.xcor()-50 and enemy2.xcor() < a1.xcor()+50: # Platform a1
            if enemy2.ycor() > a1.ycor()+19.8:
                enemy2.sety(enemy2.ycor()-enemy2dy)
            elif inBounds(enemy2.ycor(), a1.ycor(), a1.ycor()+20):
                enemy2.goto(enemy2.xcor(), a1.ycor()+20)

        elif enemy2.xcor() > a2.xcor()-50 and enemy2.xcor() < a2.xcor()+50: # Platform a2
            if enemy2.ycor() > a2.ycor()+19.8:
                enemy2.sety(enemy2.ycor()-enemy2dy)
            elif inBounds(enemy2.ycor(), a2.ycor(), a2.ycor()+20):
                enemy2.goto(enemy2.xcor(), a2.ycor()+20)

        elif enemy2.xcor() > a3.xcor()-50 and enemy2.xcor() < a3.xcor()+50: # Platform a3
            if enemy2.ycor() > a3.ycor()+19.8:
                enemy2.sety(enemy2.ycor()-enemy2dy)
            elif inBounds(enemy2.ycor(), a3.ycor(), a3.ycor()+20):
                enemy2.goto(enemy2.xcor(), a3.ycor()+20)


        # Handle player going off screen
        if player.xcor() >= 350:
            if level < 9:
                level = 1
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
                levelDesign(level)
        elif player.xcor() <= -350: 
            player.goto(-348, player.ycor())
        
        # Handle win
        if checkCollide(player, door):
            if level < 9:
                level += 1
                score.clear()
                highScore = checkHigh(level, highScore)
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
                levelDesign(level)
        
        # Handle death by enemy
        if checkCollide(player, enemy):
            if level > 1 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        elif checkCollide(player, enemy1):
            if level > 2 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        elif checkCollide(player, enemy2):
            if level > 3 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        
        # Handle death by deathPlate
        if checkCollide(player, deathPlate):
            if level > 1 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        if checkCollide(player, d1) and level >= 6:
            if level > 1 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        if checkCollide(player, d2) and level >= 7:
            if level > 1 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        if checkCollide(player, d3) and level >= 8:
            if level > 1 and level < 9:
                level = 1
                levelDesign(level)
                score.clear()
                score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
        


while True:
    win.update()

    # Handle character eyes
    eyeLeft.goto(player.xcor()-5, player.ycor())
    eyeRight.goto(player.xcor()+5, player.ycor())
    enemyEyeLeft.goto(enemy.xcor()-5, enemy.ycor())
    enemyEyeRight.goto(enemy.xcor()+5, enemy.ycor())
    enemy1EyeLeft.goto(enemy1.xcor()-5, enemy1.ycor())
    enemy1EyeRight.goto(enemy1.xcor()+5, enemy1.ycor())
    enemy2EyeLeft.goto(enemy2.xcor()-5, enemy2.ycor())
    enemy2EyeRight.goto(enemy2.xcor()+5, enemy2.ycor())
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
    
    # Handle movement of enemy on each platform
    if level == 2:
        onPlatform(enemy, a1, a2, a3, reverse)
    elif level == 3:
        onPlatform(enemy, a1, a2, a3, reverse)
        onPlatform(enemy1, a1, a2, a3, reverse)
    elif level >= 4:
        onPlatform(enemy, a1, a2, a3, reverse)
        onPlatform(enemy1, a1, a2, a3, reverse)
        onPlatform(enemy2, a1, a2, a3, reverse)
    
    
    # Handle enemy clipping through ground
    if enemy.ycor() > grass.ycor()+50:
        enemy.sety(enemy.ycor()-enemydx)
    else:
        enemy.goto(enemy.xcor(), grass.ycor()+50)
    plat = False
    if checkPlatform(player, playerdy, a1, grass, inAir, onGround):
        plat = True
    elif checkPlatform(player, playerdy, a2, grass, inAir, onGround):
        plat = True
    elif checkPlatform(player, playerdy, a3, grass, inAir, onGround):
        plat = True
    elif player.ycor() > grass.ycor()+49.8:
        if level < 10:
            player.sety(player.ycor()-playerdy)
            inAir[0] = True
            onGround[0] = False
    else:
        player.goto(player.xcor(), grass.ycor()+50)
        inAir[0] = False
        onGround[0] = True

    # Handle enemy clipping through platform
    if enemy.xcor() > a1.xcor()-50 and enemy.xcor() < a1.xcor()+50: # Platform a1
        if enemy.ycor() > a1.ycor()+19.8:
            enemy.sety(enemy.ycor()-enemydy)
        elif inBounds(enemy.ycor(), a1.ycor(), a1.ycor()+20):
            enemy.goto(enemy.xcor(), a1.ycor()+20)

    elif enemy.xcor() > a2.xcor()-50 and enemy.xcor() < a2.xcor()+50: # Platform a2
        if enemy.ycor() > a2.ycor()+19.8:
            enemy.sety(enemy.ycor()-enemydy)
        elif inBounds(enemy.ycor(), a2.ycor(), a2.ycor()+20):
            enemy.goto(enemy.xcor(), a2.ycor()+20)

    elif enemy.xcor() > a3.xcor()-50 and enemy.xcor() < a3.xcor()+50: # Platform a3
        if enemy.ycor() > a3.ycor()+19.8:
            enemy.sety(enemy.ycor()-enemydy)
        elif inBounds(enemy.ycor(), a3.ycor(), a3.ycor()+20):
            enemy.goto(enemy.xcor(), a3.ycor()+20)
    
    # Enemy 1
    if enemy1.xcor() > a1.xcor()-50 and enemy1.xcor() < a1.xcor()+50: # Platform a1
        if enemy1.ycor() > a1.ycor()+19.8:
            enemy1.sety(enemy1.ycor()-enemy1dy)
        elif inBounds(enemy1.ycor(), a1.ycor(), a1.ycor()+20):
            enemy1.goto(enemy1.xcor(), a1.ycor()+20)

    elif enemy1.xcor() > a2.xcor()-50 and enemy1.xcor() < a2.xcor()+50: # Platform a2
        if enemy1.ycor() > a2.ycor()+19.8:
            enemy1.sety(enemy1.ycor()-enemy1dy)
        elif inBounds(enemy1.ycor(), a2.ycor(), a2.ycor()+20):
            enemy1.goto(enemy1.xcor(), a2.ycor()+20)

    elif enemy1.xcor() > a3.xcor()-50 and enemy1.xcor() < a3.xcor()+50: # Platform a3
        if enemy1.ycor() > a3.ycor()+19.8:
            enemy1.sety(enemy1.ycor()-enemy1dy)
        elif inBounds(enemy1.ycor(), a3.ycor(), a3.ycor()+20):
            enemy1.goto(enemy1.xcor(), a3.ycor()+20)

    # Enemy 2
    if enemy2.xcor() > a1.xcor()-50 and enemy2.xcor() < a1.xcor()+50: # Platform a1
        if enemy2.ycor() > a1.ycor()+19.8:
            enemy2.sety(enemy2.ycor()-enemy2dy)
        elif inBounds(enemy2.ycor(), a1.ycor(), a1.ycor()+20):
            enemy2.goto(enemy2.xcor(), a1.ycor()+20)

    elif enemy2.xcor() > a2.xcor()-50 and enemy2.xcor() < a2.xcor()+50: # Platform a2
        if enemy2.ycor() > a2.ycor()+19.8:
            enemy2.sety(enemy2.ycor()-enemy2dy)
        elif inBounds(enemy2.ycor(), a2.ycor(), a2.ycor()+20):
            enemy2.goto(enemy2.xcor(), a2.ycor()+20)

    elif enemy2.xcor() > a3.xcor()-50 and enemy2.xcor() < a3.xcor()+50: # Platform a3
        if enemy2.ycor() > a3.ycor()+19.8:
            enemy2.sety(enemy2.ycor()-enemy2dy)
        elif inBounds(enemy2.ycor(), a3.ycor(), a3.ycor()+20):
            enemy2.goto(enemy2.xcor(), a3.ycor()+20)


    # Handle player going off screen
    if player.xcor() >= 350:
        if level < 9:
            level = 1
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
            levelDesign(level)
    elif player.xcor() <= -350: 
        player.goto(-348, player.ycor())
    
    # Handle win
    if checkCollide(player, door):
        if level >= 1:
            level += 1
            score.clear()
            highScore = checkHigh(level, highScore)
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
            levelDesign(level)
    
    # Handle death by enemy
    if checkCollide(player, enemy):
        if level > 1:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    elif checkCollide(player, enemy1):
        if level > 2:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    elif checkCollide(player, enemy2):
        if level > 3:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    
    # Handle death by deathPlate
    if checkCollide(player, deathPlate):
        if level >= 1 and level < 9:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    if checkCollide(player, d1) and level >= 6:
        if level >= 1 and level < 9:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    if checkCollide(player, d2) and level >= 7:
        if level >= 1 and level < 9:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    if checkCollide(player, d3) and level >= 8:
        if level >= 1 and level < 9:
            level = 1
            levelDesign(level)
            score.clear()
            score.write("Level {} High Score {}".format(level, highScore), align = "center", font = ("Courier", 14, "normal"))
    if level == 10: # BOSS LEVEL
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