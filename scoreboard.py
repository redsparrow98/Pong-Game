from turtle import Turtle

class Scoreboard(Turtle):
    """creates a scoreboard on top of the screen for right and left paddle"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_Scoreboard()   

    def update_Scoreboard(self):
        """updates scoreboards with the l and r score"""
        self.clear()
        self.goto(-80, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        """increases l score when right paddle misses and calls the updat score to update it on the screan"""
        self.l_score +=1
        self.update_Scoreboard()

    def r_point(self):
        """increases r score when left paddle misses and calls the updat score to update it on the screan"""
        self.r_score +=1
        self.update_Scoreboard()