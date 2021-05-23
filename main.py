#----------Library-----------------#

import sys
import turtle

#----------Modules-----------------#

import ball
import paddles
import paddles_control
import ball_direction

#----------window setup------------#

window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

#----------window changes----------#

window.listen()
window.onkeypress(paddles_control.paddle_left_up, "w")
window.onkeypress(paddles_control.paddle_right_up, "Up")
window.onkeypress(paddles_control.paddle_left_down, "s")
window.onkeypress(paddles_control.paddle_right_down, "Down")

#----------Maingame loop-----------#
while True:
    # window FPS
    window.update()

    # Ball Movement
    ball_direction.ball_x()
    ball_direction.ball_y()
    ball_direction.border_checker_y()
    ball_direction.border_checker_x()