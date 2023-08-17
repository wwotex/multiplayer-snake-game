import pygame
from pygame.locals import *
from keyboard import KeyboardController
from snake import Snake, SnakeSegment
from food import Food
from screen import Screen
import colors
import sys

pygame.init()

# Initializing screen
screen = Screen(1280,720)

# Initializing sprites group
all_sprites_list = pygame.sprite.Group()

# Initializing starting objects
food = Food(colors.YELLOW, 20, screen.screen)
snake1 = Snake(colors.RED, 20, screen.screen, all_sprites_list)
snake2 = Snake(colors.PURPLE, 20, screen.screen, all_sprites_list)


snakes = [snake1, snake2]

# Adding them to sprites group and adding controls
all_sprites_list.add(food)
for snake in snakes:
    all_sprites_list.add(snake)

controller = KeyboardController(2, snakes)

# Initializing clock
clock = pygame.time.Clock()
FPS = 60  # Adjust this value to control the game's frame rate

# Initiate variable that keeps track of game stages. -1 corresponds to quit
game_stage = 0

# Load initial screen and wait for space
while game_stage == 0:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_stage += controller.space_key(events)
    screen.starting_screen()

# Select number of players
while game_stage == 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle input
    controller.player_number += controller.left_right_selection(events)
    game_stage += controller.space_key(events)

    # render screen
    screen.player_number_selection(controller.player_number)

# Play the game
while game_stage == 2:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # controller.snake_direction_old()
    controller.snake_direction_new(events)

    for snake in snakes:
        snake.move(food)

    # Check if snake collided into the other
    for i, snake in enumerate(snakes):
        for j, other_snake in enumerate(snakes):
            if i != j:
                snake.enemy_collision(other_snake)
    
    # Update screen
    screen.render_game_screen(controller, all_sprites_list, snakes)

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()