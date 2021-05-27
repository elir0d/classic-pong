import turtle
import ball_trajectory as ball_t

#----------score-variables---------#

score_a = 0
score_b = 0

#-----------scoreboard-------------#

players_score = turtle.Turtle()
players_score.speed(0)
players_score.color("White")
players_score.penup()
players_score.hideturtle()
players_score.goto(0, 260)

#----------Printing-score----------#

def initial_score():
    players_score.write(f"Player A: {score_a}   "   f"Player B: {score_b} ",\
    align="center", font=("Courier", 24, "normal"))

def update_score():
    global score_a, score_b
    players_score.write(f"Player A: {score_a}   "   f"Player B: {score_b} ",\
    align="center", font=("Courier", 24, "normal"))

def reset_score():
    global score_a, score_b
    players_score.clear()

def score_tracking():
    global score_a, score_b
    if ball_t.A == True:
        score_a += 1
        reset_score()
        update_score()
        ball_t.A = False

    elif ball_t.B == True:
        score_b += 1
        reset_score()
        update_score()
        ball_t.B = False

#--------functions-call-----------#
initial_score()
score_tracking()
#---------------------------------#