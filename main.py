from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
COLLISION_TOLERANCE = 15

screen = Screen()
screen.title("Snake Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score(screen, SCREEN_HEIGHT)

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()

    # If snake collision with food
    if snake.head.distance(food) < COLLISION_TOLERANCE:
        print("Yummy_Food ^_^")
        food.appear_food()
        snake.grow_snake()
        score.increase_score()

    # If snake collision with walls
    if snake.head.xcor() > (SCREEN_WIDTH // 2 - 20) or snake.head.xcor() < -(SCREEN_WIDTH // 2 - 20) or snake.head.ycor() > (SCREEN_HEIGHT // 2 - 20) or snake.head.ycor() < -(SCREEN_HEIGHT // 2 - 20):
        game_on = False
        score.game_over()

    # If snake collision with itself
    for segment in snake.turtles:
        if segment.distance(snake.head) < 5:
            game_on = False
            score.game_over()


screen.exitonclick()
