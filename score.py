from turtle import Turtle


class Score(Turtle):
    def __init__(self, screen, screen_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, screen_height // 2 - 50)
        self.__score = 0
        self.update_score()
        self.screen = screen

    def update_score(self):
        self.write(f"Score: {self.__score}", font=(
            "courier", 24, "normal"), align="center")

    def increase_score(self):
        self.__score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.screen.bgcolor("dark red")
        self.goto(0, 0)
        self.write(f"Game Over!\nYour score is {self.__score}", align="center", font=(
            "arial", 28, "bold"))
