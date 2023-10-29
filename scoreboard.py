from turtle import Turtle

# Font style for the scoreboard
FONT = ("Courier", 24, "normal")

# Scoreboard class to display the player's level and game over messages
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the scoreboard and display the current level."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level and update the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display a 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
