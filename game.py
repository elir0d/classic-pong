import sys
import turtle
import ball
import paddles
import paddlesControl

#----------window setup----------#
window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

#----------window changes----------#
window.listen()
window.onkeypress(paddlesControl.paddle_left_up, "w")
window.onkeypress(paddlesControl.paddle_right_up, "Up")
window.onkeypress(paddlesControl.paddle_left_down, "s")
window.onkeypress(paddlesControl.paddle_right_down, "Down")


#----------Maingame loop----------#
while True:
    window.update()
