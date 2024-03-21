from turtle import Turtle

MOVE_FORWARD = 1

class Ball(Turtle):

    def __init__(self):
        """Creates a square ball for the game"""
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 1, stretch_len= 1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """makes the ball move in continuous x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """reverses the y_move to -10 and it should bounce of the top an bottom wall"""
        self.y_move *= -1

    def bounce_x(self):
        """reverses the x_move to -10 and it should bounce of the top an bottom wall"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """reset ball to home and start in the opposite direction"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()