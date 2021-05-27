import turtle
import modules.ball_trajectory as ball_t

#----------score-variables---------#

score_a = 0
score_b = 0

#-----------scoreboard-------------#

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("White")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)

#----------Printing-score----------#

def score_board():
    global score_a, score_b
    scoreboard.write(f"Player A: {score_a}   "   f"Player B: {score_b} ",\
    align="center", font=("Courier", 24, "normal"))

def score_board_refresh():
    global score_a, score_b
    scoreboard.clear()

def score_tracking():
    global score_a, score_b
    if ball_t.A == True:
        score_a += 1
        score_board_refresh()
        score_board()
        ball_t.A = False

    elif ball_t.B == True:
        score_b += 1
        score_board_refresh()
        score_board()
        ball_t.B = False

#--------functions-call-----------#
score_board()
score_tracking()
#---------------------------------#