from turtle import Turtle
import car_manager

SCORE_FONT = ("Courier", 24, "normal")
GO_FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-220, 265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Level: {self.score}", align="center", font=SCORE_FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GO_FONT)
