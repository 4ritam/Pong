from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move_ball(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def reset_pos(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.05

    def x_bounce(self):
        self.x_move *= -1
        self.speed_up()

    def y_bounce(self):
        self.y_move *= -1
        self.speed_up()

    def speed_up(self):
        self.move_speed *= 0.95
