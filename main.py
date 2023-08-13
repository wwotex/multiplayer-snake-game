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
snake1 = Snake(colors.RED, 20, 100, 100, screen.screen, all_sprites_list)
snake2 = Snake(
    colors.PURPLE,
    20,
    screen.width - 100,
    screen.height - 100,
    screen.screen,
    all_sprites_list
)
food = Food(colors.YELLOW, 20, screen.screen)

# Adding them to sprites group and adding controls
all_sprites_list.add(snake1, snake2, food)
controller = KeyboardController(2, snake1, snake2)

# Initializing clock
clock = pygame.time.Clock()
FPS = 60  # Adjust this value to control the game's frame rate

# Initiate variable that keeps track of game stages. -1 corresponds to quit
game_stage = 0

# Load initial screen and wait for space
while game_stage == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stage = -1

    game_stage += controller.space_key()
    screen.starting_screen()

# butchered solution. To be solved later
pygame.time.delay(500)

# Select number of players
while game_stage == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stage = -1

    # handle input
    controller.player_number += controller.left_right_selection()
    pygame.time.delay(500) # bad solution. Fix later
    game_stage += controller.space_key()

    # render screen
    screen.player_number_selection(controller.player_number)

# Play the game
while game_stage == 2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stage = -1

    controller.handleKeyPress()

    snake1.move(food)
    snake2.move(food)

    # Check if snake collided into the other
    snake1.enemy_collision(snake2)
    snake2.enemy_collision(snake1)
    
    # Update screen
    screen.render_game_screen(controller, all_sprites_list, snake1, snake2)

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()