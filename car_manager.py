from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
LEVEL_UP_MOVE_INCREMENT = 3

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        ycor = random.randint(-250, 250)
        self.goto(x=300, y=ycor)

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        # this method is going to execute based on a 1/6 chance
        if random.randint(1, 6) == 1:
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.bk(self.car_speed)

    def collided(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def level_up(self):
        self.car_speed += LEVEL_UP_MOVE_INCREMENT