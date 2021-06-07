import turtle

#----------balls----------#

# Ball One
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("blue")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 2
ball1.dy = 2

# Ball Two
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("red")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -2
ball2.dy = -2

# deifne a list that can be responsible for trackin each ball.
balls = [ball1, ball2] 

#----------balls----------#