import turtle
import random
import time
from PIL import Image

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
    else:
        if inBounds(player.towards(object), 270, 360) or inBounds(player.towards(object), 90, 180):
            sidels = []
            for x, y in object.get_shapepoly():
                sidels.append(y)
            sidels.sort()
            ylow = sidels[0]
            yhigh = sidels[len(sidels)-1]
            ylen = yhigh - ylow
            bound = (ylen/2)+1
        if inBounds(player.towards(object), 180, 270) or inBounds(player.towards(object), 0, 90):
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