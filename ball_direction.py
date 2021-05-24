import time
import turtle
import ball
#----------Speed and Directions------#

speed_dx = ball.element.dx = 0.1
speed_dy = ball.element.dy = 0.1

#----------X and Y functions---------#

def ball_x():
    ball_x = ball.element.xcor()
    ball_x = ball.element.setx(ball_x + speed_dx)

def ball_y():
    ball_y = ball.element.ycor()
    ball_y = ball.element.sety(ball_y + speed_dy)

#----------Border Collision check-----#
def border_checker_y():
    global speed_dy, speed_dx
    if ball.element.ycor() > 290:
        ball.element.sety(290)
        speed_dy *= -1
    if ball.element.ycor() < -290:
        ball.element.sety(-290)
        speed_dy *= -1

def border_checker_x():
    global speed_dy, speed_dx
    if ball.element.xcor() > 390:
        ball.element.goto(0, 0)
        speed_dx *= -1
    if ball.element.xcor() < -390:
        ball.element.goto(0, 0)
        speed_dx *= -1


    

