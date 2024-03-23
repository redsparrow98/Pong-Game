from turtle import Turtle

class Paddle(Turtle):
    """This class inherits from the Turtle class, and it creates the
    paddles and how they behave in the game,
    it has two functions
    
    > Go_up
    > go_down
    
    """

    def __init__(self, starting_pos):
        """creates a paddle on the screen white color.
        it takes a tuple for (x, y) position for starter position."""
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(starting_pos)
        self.shapesize(stretch_wid= 5, stretch_len= 1)

    def go_up(self):
        """moves the paddle up by 20 pixel spaces on the y-axis"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """moves the paddle down by 20 pixel spaces on the y-axis"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
