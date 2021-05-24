import turtle
import ball_direction
import ball
import paddles

#----------Paddle Collision checker----------------#
def collisions():
    if (ball.element.xcor() > 340 and  ball.element.xcor() < 350) and (ball.element.ycor() < paddles.right_paddle.ycor() + 40 and ball.element.ycor() > paddles.right_paddle.ycor() -40):
        ball.element.setx(340)
        ball_direction.speed_dx *= -1

    if (ball.element.xcor() < -340 and  ball.element.xcor() > -350) and (ball.element.ycor() < paddles.left_paddle.ycor() + 40 and ball.element.ycor() > paddles.left_paddle.ycor() -40):
        ball.element.setx(-340)
        ball_direction.speed_dx *= -1