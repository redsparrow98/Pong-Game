# set up the screen with the middle separation (from turtle screen class)
# create the boards class for users inputs (from turtle class inheritance)
# create the boards class 2 users
# create the pong (ball) class and make it move (from turtle inheritance)
# figure out collision with the wall and bounce
# detect collision with board and bounce back
# detect missed ball
# create the score class (also turtle inheritance)

###########################################################################
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Nat's Pong Game")
screen.tracer(0)


screen.listen()
screen.onkey(fun= r_paddle.go_up, key="Up")
screen.onkey(fun= r_paddle.go_down, key="Down")

screen.onkey(fun= l_paddle.go_up, key="w")
screen.onkey(fun= l_paddle.go_down, key="s")

# creats a main while loop for the game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  
    ball.move()

    # detect collision with top and bottom wall to bounce
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350 or
        ball.distance(l_paddle) < 50 and ball.xcor() < - 350):
        ball.bounce_x()

    # detect the ball going out of bounds and missing the r_paddle
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect the ball going out of bounds and missing the l_paddle
    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
