from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_SCREEN_POS = (-230, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_level_board()

    def create_level_board(self):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(LEVEL_SCREEN_POS)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT)


