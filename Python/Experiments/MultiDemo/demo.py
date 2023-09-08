from telnetlib import theNULL
import turtle
import time

cars = {}

speed = 0.05
turn = 0.105

# Generate Window
win = turtle.Screen()
win.title("NASCAR")
win.bgcolor("light blue")
win.setup(width = 720, height = 680)
win.tracer(0)

# Generate Background
turtle.register_shape("track2.gif", shape=None)
track = turtle.Turtle()
track.penup()
track.shape("track2.gif")
track.goto(0, 0)

turtle.register_shape("line", shape=((0, 0), (30, 0), (-30, 0)))
start = turtle.Turtle()
start.penup()
start.shape("line")
start.color("black")
start.goto(0, 120)

# Generate Cars
turtle.register_shape("Nascar1.gif", shape=None)
turtle.register_shape("Nascar1Flipped.gif", shape=None)
car = turtle.Turtle()
car.penup()
car.shape("Nascar1.gif")
car.color("red")
car.left(180)
car.hideturtle()

placements = [(start.xcor()+20, start.ycor()-20), 
(start.xcor()+20, start.ycor()), 
(start.xcor()+20, start.ycor()+20)]

car1 = car.clone()
car1.showturtle()
car1.goto(placements[0])

car2 = car.clone()
car2.showturtle()
car2.goto(placements[1])

car3 = car.clone()
car3.showturtle()
car3.goto(placements[2])



def moveCar(car, speed):
    car.forward(speed)
    
def turnLeft(car, lane):
    car.left((turn-0.005)/2)
    if lane == 0:
        car.forward(turn+0.02)
    elif lane == 1:
        car.forward(turn)
    elif lane == 2:
        car.forward(turn-0.02)

def rotateCar(car):
    car.shape("Nascar1Flipped.gif")
    
def resetCar(car):
    car.shape("Nascar1.gif")


def inBounds(target, min, max):
    if target >= min and target <= max:
        return True
    else:
        return False

def driveCar(car, track, lane, speed):
    if car.xcor() >= track.xcor()-160 and car.xcor() <= track.xcor()+160:
        moveCar(car, speed)
    else:
        turnLeft(car, lane)

    if inBounds(car.ycor(), track.ycor()-0.1, track.ycor()+0.1):
        if car.xcor() < track.xcor():
            rotateCar(car)
        elif car.xcor() > track.xcor():
            resetCar(car)

while True:
    win.update()
    driveCar(car1, track, 2, speed)
    driveCar(car2, track, 1, speed+0.025)
    driveCar(car3, track, 0, speed-0.025)
    
