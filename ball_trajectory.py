import ball
import turtle
#----------Speed and Directions------#

ball_dx = ball.element.dx = 0.1
ball_dy = ball.element.dy = 0.1

ball_speed = 0.1
#------------------------------------#
# This two variables are responsible to send
# the results of each# border collision# to 
# help "score" module to tracking de current score

A = False # set as global
B = False # set as global

#----------X and Y functions---------#

def ball_x():
    ball_x = ball.element.xcor()
    ball_x = ball.element.setx(ball_x + ball_dx)

def ball_y():
    ball_y = ball.element.ycor()
    ball_y = ball.element.sety(ball_y + ball_dy)

#----------Border Collision check-----#

def border_checker_y():
    global ball_dy, ball_dx
    if ball.element.ycor() > 290:
        ball.element.sety(290)
        ball_dy *= -1
    
    if ball.element.ycor() < -290:
        ball.element.sety(-290)
        ball_dy *= -1

def border_checker_x():
    global ball_dy, ball_dx, A, B
    if ball.element.xcor() > 390:
        ball.element.goto(0, 0)
        ball_dx *= -1
        A = True

    if ball.element.xcor() < -390:
        ball.element.goto(0, 0)
        ball_dx *= -1
        B = True



#prototype for increase speed after certain score
# ball_dx += ball_speed
# ball_dx += -ball_speed
    

