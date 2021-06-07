import modules.paddles as paddles

# increment #
i = 20

#----------paddle up----------#
def paddle_left_up():
    left_Y = paddles.left_paddle.ycor()
    left_Y += i
    paddles.left_paddle.sety(left_Y)

def paddle_right_up():
    right_Y = paddles.right_paddle.ycor()
    right_Y += i
    paddles.right_paddle.sety(right_Y)

#----------paddle Down----------#
def paddle_left_down():
    left_Y = paddles.left_paddle.ycor()
    left_Y -= i
    paddles.left_paddle.sety(left_Y)

def paddle_right_down():
    right_Y = paddles.right_paddle.ycor()
    right_Y -= i
    paddles.right_paddle.sety(right_Y)
    