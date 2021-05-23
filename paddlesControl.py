import turtle
import paddles
import sys

y = 20
x = 20

#----------paddle up----------#
def paddle_left_up():
    left_Y = paddles.left_paddle.ycor()
    left_Y += y
    paddles.left_paddle.sety(left_Y)

def paddle_right_up():
    right_Y = paddles.right_paddle.ycor()
    right_Y += y
    paddles.right_paddle.sety(right_Y)

#----------paddle Down----------#
def paddle_left_down():
    left_Y = paddles.left_paddle.ycor()
    left_Y -= y
    paddles.left_paddle.sety(left_Y)

def paddle_right_down():
    right_Y = paddles.right_paddle.ycor()
    right_Y -= y
    paddles.right_paddle.sety(right_Y)





