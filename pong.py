import turtle
import os


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("lime")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("lime")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lime")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = -2.5

pen = turtle.Turtle()
pen.speed(0)
pen.color("lime")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
   y = paddle_a.ycor()
   y += 20
   paddle_a.sety(y)

def paddle_a_down():
   y = paddle_a.ycor()
   y -= 20
   paddle_a.sety(y)

def paddle_b_up():
   y = paddle_b.ycor()
   y += 20
   paddle_b.sety(y)

def paddle_b_down():
   y = paddle_b.ycor()
   y -= 20
   paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
   wn.update()

   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)

   if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1
       os.system("afplay bounce.wav&")

   if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1
       os.system("afplay bounce.wav&")

   if ball.xcor() > 390:
       ball.goto(0, 0)
       ball.dx *= -1
       score_a += 1
       os.system("afplay whoo.wav&")
       pen.clear()
       pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

   if ball.xcor() < -390:
       ball.goto(0, 0)
       ball.dx *= -1
       score_b += 1
       os.system("afplay whoo.wav&")
       pen.clear()
       pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

   if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
       ball.setx(340)
       ball.dx *= -1
       os.system("afplay bounce.wav&")

   if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
       ball.setx(-340)
       ball.dx *= -1
       os.system("afplay bounce.wav&")