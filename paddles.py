import turtle

#----------Left Paddle----------#
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.penup()
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.goto(-350, 0)

lp = left_paddle
#----------Right Paddle----------#
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.penup()
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.goto(350, 0)

rp = right_paddle