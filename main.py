from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(-380, 0)
r_paddle = Paddle(380, 0)

ball = Ball()

game_is_on = True

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.distance(r_paddle) < 50 and ball.xcor() == 360 or ball.distance(l_paddle) < 50 and ball.xcor() == -360:
        ball.x_bounce()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_pos()
