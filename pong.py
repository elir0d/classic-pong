#----------Library-----------------#

import os
import sys
import time
import turtle

#----------Modules-----------------#

import modules.paddles                as paddles
import modules.scoreboard             as scoreboard
import modules.window_menu            as window_menu
import modules.ball_element           as ball_element
import modules.paddles_control        as paddles_control
import modules.ball_trajectory        as ball_trajectory
import modules.paddle_collisions      as paddle_collisions
import modules.artificial_inteligence as artifial_inteligence

#----------window setup------------#

window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0, 0)

#----------window changes----------#

window.listen()
window.onkeypress(paddles_control.paddle_left_up, "w")
window.onkeypress(paddles_control.paddle_left_down, "s")
window.onkeypress(paddles_control.paddle_right_up, "Up")
window.onkeypress(paddles_control.paddle_right_down, "Down")

window.onkeypress(window_menu.exit_pong, "Escape")

#----------Maingame loop-----------#
def main():
    while True:
        # window FTP
        time.sleep(1 / 60)
        window.update()

        for ball in ball_element.balls:

            # Ball Movement
            ball_trajectory.ball_x(ball)
            ball_trajectory.ball_y(ball)
            window.update()

            # Tracking score after check each collisions
            scoreboard.score_tracking()

            # colissions checker
            ball_trajectory.border_checker_y(ball)
            ball_trajectory.border_checker_x(ball)
            paddle_collisions.collisions(ball)
            window.update()

            # AI control - Player B only
            artifial_inteligence.ai_control(ball)

if __name__ == "__main__":
    main()