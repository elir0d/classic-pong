import turtle
import modules.paddles as p
import modules.ball_element as be
import modules.ball_trajectory as bd
import sound.sound_effects as sound_effects


"""-------Caption------------
|   rp == right_paddle      |
|   lp == left_paddle       |
|   e  == element           |
--------------------------"""

#----------Paddle Collision checker----------------#
def collisions():
    if (be.ball.xcor() < -340 and  be.ball.xcor() > -350) and\
       (be.ball.ycor() < p.lp.ycor() + 40 and be.ball.ycor() > p.lp.ycor() -40):
            
            be.ball.setx(-340)
            bd.ball_dx *= -1
            sound_effects.play(0)

    if (be.ball.xcor() > 340 and  be.ball.xcor() < 350) and\
       (be.ball.ycor() < p.rp.ycor() + 40 and be.ball.ycor() > p.rp.ycor() -40):
            
            be.ball.setx(340)
            bd.ball_dx *= -1
            sound_effects.play(1)
