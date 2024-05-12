from turtle import Turtle,Screen
import time
from player import Player
from car_manager import CarManger
from score import Score
screen=Screen()
screen.setup(600,600)
screen.tracer(0)
player=Player()
car_manager=CarManger()
score=Score()

screen.listen()
screen.onkey(player.go_up,"Up")

game=True


while game:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()
    
    
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game=False
            score.game_over()
    if player.is_finished():
        player.start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()


