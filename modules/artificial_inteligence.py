import modules.paddles as p
import modules.ball_element as be
import modules.paddles_control as pc
from modules.ball_element import balls

# This verible define the closest ball. That way AI module can track all the balls
c_ball = balls[0]

# AI control for Player B
def ai_control(ball):
    global c_ball

    # This loop is responsible to compare which ball is closer than other
    for ball in balls:
        if ball.xcor() > c_ball.xcor():
            c_ball = ball

    # this statements are responsible to move AI paddle
    if p.rp.ycor() < c_ball.ycor() and abs(p.rp.ycor() - c_ball.ycor()) > 10:
        pc.paddle_right_up()
    if p.rp.ycor() > c_ball.ycor() and abs(p.rp.ycor() - c_ball.ycor()) > 10:
        pc.paddle_right_down()