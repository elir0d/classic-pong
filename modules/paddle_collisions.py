import turtle
import modules.ball as b
import modules.paddles as p
import modules.ball_trajectory as bd

"""-------Caption------------
|   rp == right_paddle      |
|   lp == left_paddle       |
|   e  == element           |
--------------------------"""

#----------Paddle Collision checker----------------#
def collisions():
    if (b.e.xcor() > 340 and  b.e.xcor() < 350) and\
       (b.e.ycor() < p.rp.ycor() + 40 and b.e.ycor() > p.rp.ycor() -40):
            
            b.e.setx(340)
            bd.ball_dx *= -1

    if (b.e.xcor() < -340 and  b.e.xcor() > -350) and\
       (b.e.ycor() < p.lp.ycor() + 40 and b.e.ycor() > p.lp.ycor() -40):
            
            b.e.setx(-340)
            bd.ball_dx *= -1