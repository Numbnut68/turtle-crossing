import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


turtle = Player()
score = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars = CarManager()

    # Reset player after scoring
    if turtle.ycor() > 280:
        turtle.next_level()
        score.inc_score()
        car_manager.level_up()

    # create new car
    car_manager.create_car()

    # move cars
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()