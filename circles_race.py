import turtle
import random
import time



delay = 0.1

wn = turtle.Screen()
wn.title("Race")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 365)
pen.write("Circles Race", align="center", font=("Courier", 24, "normal"))

line = turtle.Turtle()
line.color("white")
line.penup()
line.backward(400)
line.left(90)
line.forward(350)
line.right(90)
line.pendown()
line.forward(1000)

turtle_white = turtle.Turtle()
turtle_white.speed()
turtle_white.shape("circle")
turtle_white.color("white")
turtle_white.penup()
turtle_white.goto(-350, -350)
turtle_white.direction = "up"
turtle_white.setheading(90)

turtle_grey = turtle.Turtle()
turtle_grey.speed()
turtle_grey.shape("circle")
turtle_grey.color("grey")
turtle_grey.penup()
turtle_grey.goto(-280, -350)
turtle_grey.direction = "stop"
turtle_grey.setheading(90)

turtle_maroon = turtle.Turtle()
turtle_maroon.speed()
turtle_maroon.shape("circle")
turtle_maroon.color("brown")
turtle_maroon.penup()
turtle_maroon.goto(-210, -350)
turtle_maroon.direction = "stop"
turtle_maroon.setheading(90)

turtle_red = turtle.Turtle()
turtle_red.speed()
turtle_red.shape("circle")
turtle_red.color("red")
turtle_red.penup()
turtle_red.goto(-140, -350)
turtle_red.direction = "stop"
turtle_red.setheading(90)

turtle_pink = turtle.Turtle()
turtle_pink.speed()
turtle_pink.shape("circle")
turtle_pink.color("pink")
turtle_pink.penup()
turtle_pink.goto(-70, -350)
turtle_pink.direction = "stop"
turtle_pink.setheading(90)

turtle_purple = turtle.Turtle()
turtle_purple.speed()
turtle_purple.shape("circle")
turtle_purple.color("purple")
turtle_purple.penup()
turtle_purple.goto(0, -350)
turtle_purple.direction = "stop"
turtle_purple.setheading(90)

turtle_blue = turtle.Turtle()
turtle_blue.speed()
turtle_blue.shape("circle")
turtle_blue.color("blue")
turtle_blue.penup()
turtle_blue.goto(70, -350)
turtle_blue.direction = "stop"
turtle_blue.setheading(90)

turtle_turquoise = turtle.Turtle()
turtle_turquoise.speed()
turtle_turquoise.shape("circle")
turtle_turquoise.color("turquoise")
turtle_turquoise.penup()
turtle_turquoise.goto(140, -350)
turtle_turquoise.direction = "stop"
turtle_turquoise.setheading(90)

turtle_green = turtle.Turtle()
turtle_green.speed()
turtle_green.shape("circle")
turtle_green.color("green")
turtle_green.penup()
turtle_green.goto(210, -350)
turtle_green.direction = "stop"
turtle_green.setheading(90)

turtle_yellow = turtle.Turtle()
turtle_yellow.speed()
turtle_yellow.shape("circle")
turtle_yellow.color("yellow")
turtle_yellow.penup()
turtle_yellow.goto(280, -350)
turtle_yellow.direction = "stop"
turtle_yellow.setheading(90)

turtle_orange = turtle.Turtle()
turtle_orange.speed()
turtle_orange.shape("circle")
turtle_orange.color("orange")
turtle_orange.penup()
turtle_orange.goto(350, -350)
turtle_orange.direction = "stop"
turtle_orange.setheading(90)



points_white = 0
points_grey = 0
points_maroon = 0
points_red = 0
points_pink = 0
points_purple = 0
points_turquoise = 0
points_blue = 0
points_green = 0
points_yellow = 0
points_orange = 0

timer = 0




while timer < 3:
   while True:

       wn.update()
       time.sleep(delay)

       white_y = turtle_white.ycor()
       grey_y = turtle_grey.ycor()
       maroon_y = turtle_maroon.ycor()
       red_y = turtle_red.ycor()
       pink_y = turtle_pink.ycor()
       purple_y = turtle_purple.ycor()
       blue_y = turtle_blue.ycor()
       turquoise_y = turtle_turquoise.ycor()
       green_y = turtle_green.ycor()
       yellow_y = turtle_yellow.ycor()
       orange_y = turtle_orange.ycor()

       white_speed = random.randint(5, 15)
       grey_speed = random.randint(5, 15)
       maroon_speed = random.randint(5, 15)
       red_speed = random.randint(5, 15)
       pink_speed = random.randint(5, 15)
       purple_speed = random.randint(5, 15)
       blue_speed = random.randint(5, 15)
       turquoise_speed = random.randint(5, 15)
       green_speed = random.randint(5, 15)
       yellow_speed = random.randint(5, 15)
       orange_speed = random.randint(5, 15)

       turtle_white.sety(white_y + white_speed)
       turtle_grey.sety(grey_y + grey_speed)
       turtle_maroon.sety(maroon_y + maroon_speed)
       turtle_red.sety(red_y + red_speed)
       turtle_pink.sety(pink_y + pink_speed)
       turtle_purple.sety(purple_y + purple_speed)
       turtle_turquoise.sety(turquoise_y + turquoise_speed)
       turtle_blue.sety(blue_y + blue_speed)
       turtle_green.sety(green_y + green_speed)
       turtle_yellow.sety(yellow_y + yellow_speed)
       turtle_orange.sety(orange_y + orange_speed)

       location = [white_y, grey_y, maroon_y, red_y, pink_y, purple_y, blue_y, turquoise_y, green_y, yellow_y,
                   orange_y]

       for i in location:
           if i > 340:
               if white_y > 340:
                   winner = "White won a race!!!"
                   print("White won a race!!!")
                   points_white += 1
               if grey_y > 340:
                   winner = "Grey won a race!!!"
                   print("Grey won a race!!!")
                   points_grey += 1
               if maroon_y > 340:
                   winner = "Maroon won a race!!!"
                   print("Maroon won a race!!!")
                   points_maroon += 1
               if red_y > 340:
                   winner = "Red won a race!!!"
                   print("Red won a race!!!")
                   points_red += 1
               if pink_y > 340:
                   winner = "pink won a race!!!"
                   print("Pink won a race!!!")
                   points_pink += 1
               if purple_y > 340:
                   winner = "Purple won a race!!!"
                   print("Purple won a race!!!")
                   points_purple += 1
               if blue_y > 340:
                   winner = "Blue won a race!!!"
                   print("Blue won a race!!!")
                   points_blue += 1
               if turquoise_y > 340:
                   winner = "Turquoise won a race!!!"
                   print("Turquoise won a race!!!")
                   points_turquoise += 1
               if green_y > 340:
                   winner = "Green won a race!!!"
                   print("Green won a race!!!")
                   points_green += 1
               if yellow_y > 340:
                   winner = "Yellow won a race!!!"
                   print("Yellow won a race!!!")
                   points_yellow += 1
               if orange_y > 340:
                   winner = "Orange won a race!!!"
                   print("Orange won a race!!!")
                   points_orange += 1
               turtle_white.goto(-350, -350)
               turtle_grey.goto(-280, -350)
               turtle_maroon.goto(-210, -350)
               turtle_red.goto(-140, -350)
               turtle_pink.goto(-70, -350)
               turtle_purple.goto(0, -350)
               turtle_blue.goto(70, -350)
               turtle_turquoise.goto(140, -350)
               turtle_green.goto(210, -350)
               turtle_yellow.goto(280, -350)
               turtle_orange.goto(350, -350)
               pen.clear()
               pen.write("Winner: {}".format(winner), align="center", font=("Courier", 24, "normal"))


   timer += 1

wn.mainloop()

