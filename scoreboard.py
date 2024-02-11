from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = None
        self.color("black")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_score()

        self.high_score_display = Turtle()  # Create a separate Turtle for high score
        self.high_score_display.color("black")
        self.high_score_display.penup()
        self.high_score_display.goto(0, 270)
        self.high_score_display.hideturtle()
        self.update_high_score()

    def update_score(self):
        self.clear_score()
        self.write(arg=f"Score = {self.score}", align="center", font=("Courier", 20, "normal"))

    def update_high_score(self):
        with open("HighScore.txt") as file:
            self.high_score = int(file.read())
        self.clear_high_score()
        self.high_score_display.write(arg=f"High Score = {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def clear_score(self):
        self.clear()

    def clear_high_score(self):
        self.high_score_display.clear()

    def change_high_score(self):
        with open("HighScore.txt") as file:
            current_high_score = int(file.read())
        if self.score > current_high_score:
            with open("HighScore.txt", 'w') as file:
                file.write(f"{self.score}")

    def game_over(self):
        self.change_high_score()
        self.goto(0, 0)
        self.write(arg=f"Game Over!!", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

        # Check if the score is higher than the current high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()

