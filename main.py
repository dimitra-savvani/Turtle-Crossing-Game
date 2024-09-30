import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = CarManager()
player = Player()
score = Scoreboard()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move_cars()

    # Detect collision with cars
    if cars.collided(player):
        game_is_on = False
        score.game_over()

    # Detect finish line crossing
    if player.is_at_finish_line():
        player.level_up()
        cars.level_up()
        score.level_up()

screen.exitonclick()
