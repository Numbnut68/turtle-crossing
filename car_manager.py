from turtle import Turtle
from scoreboard import Scoreboard
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FASTER = 1.1
NUM_OF_CARS = 3


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.level = 0

    def create_car(self):
        level = 6
        if self.level >= 5:
            level -= 1
        elif self.level >= 10:
            level -= 1
        elif self.level >= 15:
            level -= 1
        elif self.level >= 20:
            level -= 1
        ran_chance = random.randint(1, level)
        if ran_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-10, 10)
            new_car.goto(300, y_pos * 25)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            if self.level > 0:
                car.backward(STARTING_MOVE_DISTANCE * (FASTER * self.level))
            else:
                car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.level += 1

