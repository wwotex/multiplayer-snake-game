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
snakes = [] # Snake list to keep track of existing snakes
food = Food(colors.YELLOW, 20, screen.screen)
all_sprites_list.add(food)

controller = KeyboardController()

# Initializing clock
clock = pygame.time.Clock()
FPS = 60  # Adjust this value to control the game's frame rate

# Initiate variable that keeps track of game stages. -1 corresponds to quit
game_stage = 0

player_number = 2 # initial player number


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
    player_number += controller.left_right_selection(events)
    game_stage += controller.space_key(events)

    if game_stage == 2:
        # Playernumber is confirmed. Initialize snakes.
        for _ in range(player_number):
            new_snake = Snake(colors.RED, 20, screen.screen, all_sprites_list)  # Adjust parameters as needed
            snakes.append(new_snake)
            all_sprites_list.add(new_snake)

    # render screen
    screen.player_number_selection(player_number)

# Play the game
while game_stage == 2:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Adjust snake directions according to input
    # controller.snake_direction_old()
    controller.snake_direction_new(snakes, events)

    # All snakes take a move
    for snake in snakes:
        snake.move(food)

    # Check collisions
    for i, snake in enumerate(snakes):
        # Check self collision
        snake.self_collision()
        # Check enemy collisions
        for j, other_snake in enumerate(snakes):
            if i != j:
                snake.enemy_collision(other_snake)
    
    # Update screen
    screen.render_game_screen(controller, all_sprites_list, snakes)

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()