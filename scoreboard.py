from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 265)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", font=("Arial", 24, "normal"), align="center")

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
