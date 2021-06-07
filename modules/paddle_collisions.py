import modules.paddles as p
import modules.ball_element as be
import modules.ball_trajectory as bt
import sound.sound_effects as sound_effects


"""-------Caption------------
|   rp == right_paddle      |
|   lp == left_paddle       |
--------------------------"""

#----------Paddle Collision checker----------------#
def collisions(ball):
    if (ball.xcor() < -340 and  ball.xcor() > -350) and\
       (ball.ycor() < p.lp.ycor() + 40 and ball.ycor() > p.lp.ycor() -40):
            
            ball.setx(-340)
            ball.dx *= -1
            sound_effects.play(0)

    if (ball.xcor() > 340 and  ball.xcor() < 350) and\
       (ball.ycor() < p.rp.ycor() + 40 and ball.ycor() > p.rp.ycor() -40):
            
            ball.setx(340)
            ball.dx *= -1
            sound_effects.play(1)
