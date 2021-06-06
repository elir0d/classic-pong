import turtle
import modules.ball as b
import modules.paddles as p
import modules.paddles_control as pc

# AI control for Player B
def ai_control():
    if p.rp.ycor() < b.e.ycor() and abs(p.rp.ycor() - b.e.ycor()) > 10: 
        pc.paddle_right_up()

    elif p.rp.ycor() > b.e.ycor() and abs(p.rp.ycor() - b.e.ycor()) > 10:
        pc.paddle_right_down()
