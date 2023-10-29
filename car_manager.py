from turtle import Turtle
import random

# Constants for car management
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# CarManager class responsible for creating and managing cars
class CarManager:
    def __init__(self):
        self.all_cars = []  # List to store all car instances
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial car speed

    def create_car(self):
        """Create a new car with a random color and position."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars backward by the current car speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increase the car speed to make the game more challenging."""
        self.car_speed += MOVE_INCREMENT
