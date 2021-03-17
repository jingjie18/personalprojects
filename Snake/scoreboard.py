from turtle import Turtle
with open("data.txt") as file:
    HIGH_SCORE = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(x=0, y=280)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=("Arial", 12, "normal"), align="center")


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=("Arial", 12, "normal"), align="center")

