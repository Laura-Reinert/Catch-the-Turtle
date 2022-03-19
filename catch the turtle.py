#Catch the Turtle
#=======================================================================
#"Catch the Turtle" is the first project I have made
#in Python(level: novice). This was adapted
#from a Youtube tutorial by Christian Thompson
# teaching how to make Pong using turtle
# module in Python. I found the tutorial
#through "Learn Python by Building
# Five Games - Full Course by freeCodeCamp.org.
    #Youtube tutorial: https://www.youtube.com/watch?v=XGf2GcyHPhc
        #Pong: 0:01:18 - 0:45:36

#I also heavily relied on docs.python.org,
#geeksforgeeks.org, & stackoverflow.com.

#Retrieved March, 2022
#=======================================================================


#make the landscape
import turtle
import winsound
import random

wn = turtle.Screen()
wn.title("Catch the Turtle")
wn.bgcolor("beige")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#instructions - beginning
ins = turtle.Turtle()
ins.penup()
ins.setpos(0,250)
ins.write("Use arrow keys to catch turtle", align = "center", font = "Courier")

#objects - bed
bed = turtle.Turtle()
bed.shape("square")
bed.color("blue")
bed.shapesize(stretch_wid = 30, stretch_len = 10)
bed.penup()
bed.goto(-350, 350)

pillow = turtle.Turtle()
pillow.shape("square")
pillow.color("white")
pillow.shapesize(stretch_wid = 10, stretch_len = 10)
pillow.penup()
pillow.goto(-350, 350)

#objects - dresser
dresser = turtle.Turtle()
dresser.shape("square")
dresser.color("brown")
dresser.shapesize(stretch_wid = 10, stretch_len = 10)
dresser.penup()
dresser.goto(350,350)

#objects - door
door = turtle.Turtle()
door.shape("square")
door.color("black")
door.shapesize(stretch_wid = 10, stretch_len = 10)
door.penup()
door.goto(-350,-350)

#objects - shelf
shelf = turtle.Turtle()
shelf.shape("square")
shelf.color("green")
shelf.shapesize(stretch_wid = 30, stretch_len = 5)
shelf.penup()
shelf.goto(350,-350)

#objects - rug
rug = turtle.Turtle()
rug.shape("triangle")
rug.color("orange")
rug.shapesize(stretch_wid = 10, stretch_len = 10)
rug.penup()
rug.goto(0,0)

#objects - decor
decor = turtle.Turtle()
decor.shape("circle")
decor.color("green")
decor.shapesize(stretch_wid = 12, stretch_len = 12)
decor.penup()
decor.goto(-250,-100)

#objects - decor
decor = turtle.Turtle()
decor.shape("circle")
decor.color("violet")
decor.shapesize(stretch_wid = 12, stretch_len = 12)
decor.penup()
decor.goto(250,125)

#turtle start position
tur = turtle.Turtle()
tur.penup()
tur.shape("turtle")

colorsettur = ["blue", "red", "pink", "orange", "violet"]
thecolortur = random.choice(colorsettur)
tur.color(thecolortur)

randomx = random.randrange(-250,250)
randomy = random.randrange(-350,350)
tur.setpos(randomx, randomy)

speedometer = (0, 2, 3, 4, 5, 6, 7, 8, 9, 10)
turspeed = random.choice(speedometer)
tur.speed(turspeed)

flipperx = (0.5, 0.75, 1, 1.25, 1.5)
flippery = (-0.5, -0.75, -1, -1.25, -1.5)
tur.dx = random.choice(flipperx)
tur.dy = random.choice(flippery)

#self
self = turtle.Turtle()
self.speed(0)
self.shape("circle")
self.color("black")
self.penup()
self.setpos(0,0)
self.dx = 0.5
self.dy = -0.5

#self function
def self_up():
    y1 = self.ycor()
    y1 += 20
    self.sety(y1)

def self_down():
    y1 = self.ycor()
    y1 += -20
    self.sety(y1)

def self_left():
    x1 = self.xcor()
    x1 += -20
    self.setx(x1)

def self_right():
    x1 = self.xcor()
    x1 += 20
    self.setx(x1)

#keyboard binding
wn.listen()
wn.onkeypress(self_up,"Up")
wn.onkeypress(self_down, "Down")
wn.onkeypress(self_left,"Left")
wn.onkeypress(self_right,"Right")


#main game loop
while True:
    wn.update()

    #move the turtle
    tur.setx(tur.xcor() + tur.dx)
    tur.sety(tur.ycor() + tur.dy)
    tur.setheading(turtle.towards(tur.dx,tur.dy))


    #border checking for self
    if self.ycor() > 285:
        self.sety(285)
        self.dy *= -1

    if self.ycor() < -280:
        self.sety(-280)
        self.dy *= -1

    if self.xcor() > 390:
        self.setx(390)
        self.dx *= -1

    if self.xcor() < -390:
        self.setx(-390)
        self.dx *= -1

    #border checking for turtle
    if tur.ycor() > 285:
        tur.sety(285)
        tur.dy *= -1

    if tur.ycor() < -280:
        tur.sety(-280)
        tur.dy *= -1

    if tur.xcor() > 390:
        tur.setx(390)
        tur.dx *= -1

    if tur.xcor() < -390:
        tur.setx(-390)
        tur.dx *= -1

    #turtle and self collisions
    if self.xcor() and self.ycor() == tur.xcor() and self.ycor():
        #instructions - end
        end = turtle.Turtle()
        end.penup()
        end.setpos(0,-250)
        end.write("You caught the turtle!", align = "center", font = "Courier")
        #turtle stop
        tur.goto(-50,-200)
        self.goto(50,-200)
        tur.dx = 0
        tur.dy = 0
        #turtle party
        for i in range(100):
            # instructions - end
            end2 = turtle.Turtle()
            end2.penup()
            end2.setpos(-50, -275)
            end2.write("Turtle Party!", align="center", font="Courier")

            idx = int(i/10)
            turpar = turtle.Turtle()
            turpar.penup()
            turpar.shape("turtle")
            colorset = ["blue", "red", "pink", "orange", "violet"]
            thecolor = random.choice(colorset)
            turpar.color(thecolor)
            randomx_turpar = random.randrange(-250,250)
            randomy_turpar = random.randrange(-350,350)
            turpar.setpos(randomx_turpar, randomy_turpar)
            turpar.setheading(turtle.towards(tur.dx, tur.dy))



