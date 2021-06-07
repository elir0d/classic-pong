import modules.ball_element as be
import sound.sound_effects as sounds

#----------Speed and Directions------#

"""----------------------------------------------------------
| This two variables are responsible to send the results    |
| of each border collision to "scoreboard" module this      |
| help "scoreboard" module to tracking de current score and |
| update in the scoreboard.                                 |
---------------------------------------------------------"""

A = False # set as global #
B = False # set as global #

#----------X and Y functions---------#

def ball_x(ball):
    ball.setx(ball.xcor() + ball.dx)

def ball_y(ball):
    ball.sety(ball.ycor() + ball.dy)

#----------Border Collision check-----#

def border_checker_y(ball):
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

def border_checker_x(ball):
    global A, B
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        A = True

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        B = True

#prototype for increase speed after certain score#
# ball.dx += ball_speed
# ball.dx += -ball_speed