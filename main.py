"""
Turtle Crossing Game

This is a simple arcade-style game where you control a turtle character
and attempt to safely cross a busy road, avoiding oncoming cars. Your
goal is to reach the finish line at the top of the screen while
accumulating points by successfully crossing the road. Be careful, as
the game becomes more challenging with each level!

Instructions:
- Use the "Up" arrow key to move the turtle upward.
- Avoid colliding with the moving cars on the road.
- Successfully cross the road to increase your level.

Enjoy the game and have fun!
"""

# Import necessary libraries and modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates for smoother animation

# Create the player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Ask the player if they want to play the game
play_game = screen.textinput(title="Turtle Crossing Game", prompt="Welcome to Turtle Crossing!\n\nObjective: Cross the road safely and reach the finish line.\nDo you want to play the Pong game? \n Click 'OK' or enter 'y' to play the game")

# Listen for keyboard input and set the player's action
screen.listen()
screen.onkey(player.go_up, "Up")

# Initialize the game loop
if play_game == "" or "y":
  game_is_on = True
  while game_is_on:
      time.sleep(0.1)  # Control the game speed
      screen.update()  # Update the screen to show changes
  
      # Create a new car and move existing cars
      car_manager.create_car()
      car_manager.move_cars()
  
      # Detect collision with a car
      for car in car_manager.all_cars:
          if car.distance(player) < 20:
              game_is_on = False  # End the game if a collision is detected
              scoreboard.game_over()
              
  
      # Detect successful crossing of the finish line
      if player.is_at_finish_line():
          player.go_to_start()  # Reset the player's position
          car_manager.level_up()  # Increase the level by adding more cars
          scoreboard.increase_level()  # Update the level on the scoreboard

# Close the game when the player clicks anywhere on the screen
screen.exitonclick()



