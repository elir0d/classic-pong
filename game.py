import turtle
import paddles
import ball

#----------window setup----------#
window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

#----------Maingame loop----------#
while True:
    window.update()
