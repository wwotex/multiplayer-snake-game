import pygame
from pygame.locals import *
from keyboard import KeyboardController
from snake import Snake, SnakeSegment
from food import Food
from screen import Screen
import colors

pygame.init()

# Initializing screen
screen = Screen(1280,720)

# Initializing sprites group
all_sprites_list = pygame.sprite.Group()

# Initializing starting objects
snake1 = Snake(colors.RED, 20, 100, 100, screen, all_sprites_list)
snake2 = Snake(
    colors.PURPLE,
    20,
    screen.width - 100,
    screen.height - 100,
    screen,
    all_sprites_list
)
food = Food(colors.YELLOW, 20, screen)

# Adding them to sprites group and adding controls
all_sprites_list.add(snake1, snake2, food)
controller = KeyboardController(snake1, snake2)

# Initializing clock
clock = pygame.time.Clock()
FPS = 60  # Adjust this value to control the game's frame rate

# Load initial screen and wait for space
screen.starting_screen()
controller.wait_for_space()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controller.handleKeyPress()

    snake1.move(food)
    snake2.move(food)

    # Check if snake collided into the other
    snake1.enemy_collision(snake2)
    snake2.enemy_collision(snake1)
    
    # Update screen
    screen.render_game_screen(all_sprites_list, snake1, snake2)

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
