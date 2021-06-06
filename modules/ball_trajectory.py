import turtle
import modules.ball_element as be
import sound.sound_effects as sounds

#----------Speed and Directions------#

ball_dx = be.ball.dx = 0.1
ball_dy = be.ball.dy = 0.1

ball_speed = 0.1

"""----------------------------------------------------------
| This two variables are responsible to send the results    |
| of each border collision to "scoreboard" module this      |
| help "scoreboard" module to tracking de current score and |
| update in the scoreboard.                                 |
---------------------------------------------------------"""

A = False # set as global #
B = False # set as global #

#----------X and Y functions---------#

def ball_x():
    ball_x = be.ball.xcor()
    ball_x = be.ball.setx(ball_x + ball_dx)

def ball_y():
    ball_y = be.ball.ycor()
    ball_y = be.ball.sety(ball_y + ball_dy)

#----------Border Collision check-----#

def border_checker_y():
    global ball_dy, ball_dx
    if be.ball.ycor() > 290:
        be.ball.sety(290)
        ball_dy *= -1

    if be.ball.ycor() < -290:
        be.ball.sety(-290)
        ball_dy *= -1

def border_checker_x():
    global ball_dy, ball_dx, A, B
    if be.ball.xcor() > 390:
        be.ball.goto(0, 0)
        ball_dx *= -1
        A = True

    if be.ball.xcor() < -390:
        be.ball.goto(0, 0)
        ball_dx *= -1
        B = True



#prototype for increase speed after certain score#
# ball_dx += ball_speed
# ball_dx += -ball_speed
    

