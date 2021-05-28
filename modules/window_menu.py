import turtle
import time

window = turtle.Screen()
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)
window.goto(0, 0)
window.listen()



def exit_pong():
    window.bye()