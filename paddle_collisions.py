import turtle
import ball_trajectory as bd
import ball as b
import paddles as p

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