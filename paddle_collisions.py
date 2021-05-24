import turtle
import ball_direction
import ball
import paddles

'''--------------------------------------------
| Defining variables for better understanding |
|                                             |
| Paddles right and left with method ycor()   |
| ball element with method xcor() and xcor()  |
| ball direction and speed variable imported  |
--------------------------------------------'''

rpy = paddles.right_paddle.ycor()
lpy = paddles.left_paddle.ycor()

bex = ball.element.xcor()
bey = ball.element.ycor()

speed_dx = ball_direction.speed_dx
speed_dy = ball_direction.speed_dy

#----------Paddle Collision checker----------------#
def collisions():
    if (bex > 340 and  bex < 350) and (bey < rpy + 40 and bey > rpy -40):
        ball.element.setx(340)
        speed_dx *= -1

    if (bex < -340 and  bex > -350) and (bey < lpy + 40 and bey > lpy -40):
        ball.element.setx(-340)
        speed_dx *= -1