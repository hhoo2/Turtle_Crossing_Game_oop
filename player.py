from turtle import Turtle

# Constants for player movement and the finish line position
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Player class that inherits from the Turtle class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        # Configure the player turtle
        self.shape("turtle")
        self.penup()
        self.go_to_start()  # Initialize the player's position
        self.setheading(90)  # Set the player's initial direction to face upward

    def go_up(self):
        """Move the player turtle upward."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Reset the player's position to the starting point."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the player has reached the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
