import turtle
import modules.paddles as p
import modules.ball_element as be
import modules.paddles_control as pc

# AI control for Player B
def ai_control():
    if p.rp.ycor() < be.ball.ycor() and abs(p.rp.ycor() - be.ball.ycor()) > 10: 
        pc.paddle_right_up()

    elif p.rp.ycor() > be.ball.ycor() and abs(p.rp.ycor() - be.ball.ycor()) > 10:
        pc.paddle_right_down()
