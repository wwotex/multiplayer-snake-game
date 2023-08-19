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

player_number = active_snakes = 2 # initial player number

while True:
    # Load initial screen and wait for space
    if game_stage == 0:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game_stage += controller.space_key(events)
        screen.starting_screen()

    # Select number of players
    elif game_stage == 1:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # handle input
        player_number += controller.left_right_selection(events)

        if controller.space_key(events) == 1:
            # Playernumber is confirmed. Initialize snakes.
            for _ in range(player_number):
                new_snake = Snake(colors.RED, 20, screen.screen, all_sprites_list)  # Adjust parameters as needed
                snakes.append(new_snake)
                all_sprites_list.add(new_snake)

            # initilize active snake number for game tracking and score calculation
            active_snakes = player_number
            # progress to next stage of the game
            game_stage = 2
        else:
            # render screen
            screen.player_number_selection(player_number)

    # Play the game
    elif game_stage == 2:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if active_snakes < 2:
            for snake in snakes:
                if snake.Q:
                    snake.round_score = player_number - active_snakes
            game_stage = 3
        else:
            # Adjust snake directions according to input
            # controller.snake_direction_old()
            controller.snake_direction_new(snakes, events)

            print(active_snakes)

            # All snakes take a move
            for snake in snakes:
                snake.move(food)

            # Check collisions
            for i, snake in enumerate(snakes):
                # Check self collision
                if snake.self_collision() == 1: # if snake deleted 
                    snake.round_score = player_number - active_snakes # assign score
                    active_snakes -= 1 # decrease number of acitve snakes
                # Check enemy collisions
                for j, other_snake in enumerate(snakes):
                    if i != j:
                        deleted_snakes = snake.enemy_collision(other_snake)
                        if deleted_snakes == 2: # if both snakes deleted 
                            snake.round_score = player_number - active_snakes # assign score
                            other_snake.round_score = player_number - active_snakes # assign score
                            active_snakes -= 2 # decrease number of acitve snakes
                        elif deleted_snakes == 1: # if snake deleted 
                            snake.round_score = player_number - active_snakes # assign score
                            other_snake.round_score = player_number - active_snakes # assign score
                            active_snakes -= 1 # decrease number of acitve snakes

            
            # Update screen
            screen.render_game_screen(all_sprites_list)

            # Control the frame rate
            clock.tick(FPS)

    # Display scores
    elif game_stage == 3:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Transfer round scores to overall scores:
        for snake in snakes:
            if snake.round_score != 0:
                snake.score += snake.round_score
                snake.round_score = 0

        screen.display_scores(snakes)

        # Go back to previous game stage
        if controller.space_key(events) == 1:
            print("lets go back to game stage")
            active_snakes = player_number
            for snake in snakes:
                snake.reset()
            game_stage = 2
    else:    
        pygame.quit()
        sys.exit()