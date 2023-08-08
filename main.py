import pygame
from pygame.locals import *
from keyboard import KeyboardController
from snake import Snake
from food import Food
import colors

pygame.init()

# Initializing screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initializing starting objects
snake1 = Snake(colors.RED, 20, 100, 100, screen)
snake2 = Snake(
    colors.PURPLE,
    20,
    SCREEN_WIDTH - 100,
    SCREEN_HEIGHT - 100,
    screen
)
food = Food(colors.OLIVE, 20, screen)
controller = KeyboardController(snake1, snake2)

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

    # # Check for collision between snakes and food
    # if snake1.check_collision(food):
    #     food.spawn()

    # if snake2.check_collision(food):
    #     food.spawn()

    # Update screen
    screen.fill(colors.DARK)

    # Update sprites
    snake1.draw()
    snake2.draw()

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
