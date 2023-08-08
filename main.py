import pygame
from pygame.locals import *
from keyboard import KeyboardController
from snake import Snake, SnakeSegment
from food import Food
import colors

pygame.init()

# Initializing screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initializing starting objects
snake1 = SnakeSegment(colors.RED, 20, 100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
snake2 = SnakeSegment(
    colors.PURPLE,
    20,
    SCREEN_WIDTH - 100,
    SCREEN_HEIGHT - 100,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
food = Food(colors.OLIVE, 20, SCREEN_WIDTH, SCREEN_HEIGHT)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(snake1, snake2, food)
controller = KeyboardController(snake1, snake2, food)

snake = Snake()
for i in range(5):
    temp = SnakeSegment(colors.RED, 20, 10+20*i, 10, SCREEN_WIDTH, SCREEN_HEIGHT)
    snake.add(temp)

# Initializing clock
clock = pygame.time.Clock()
FPS = 60  # Adjust this value to control the game's frame rate

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controller.handleKeyPress()

    snake1.move()
    snake2.move()
    snake.move()

    # Check for collision between snakes and food
    if snake1.check_collision(food):
        food.spawn()

    if snake2.check_collision(food):
        food.spawn()

    # Update screen
    screen.fill(colors.DARK)

    # Update sprites
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    snake.update()
    snake.draw(screen)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
