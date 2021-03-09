# import dependencies

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# set up the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snek")
screen.tracer(0)





snake = Snake()
food = Food()
scoreboard = Scoreboard()



# listen to the screen

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


# create loop to start game; move snake initially

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect the snake's collision with the food (class) - use distance class in turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()



    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    # detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()



screen.update()



screen.exitonclick()