import pygame
from pygame.locals import *


class KeyboardController:

    def snake_direction_old(self, snakes) -> None:
        """Handles keys for snakes"""
        key = pygame.key.get_pressed()
        # handle "wsad" keys for snake1
        if key[K_w]:
            snakes[0].change_direction(0, -1)
        if key[K_s]:
            snakes[0].change_direction(0, 1)
        if key[K_a]:
            snakes[0].change_direction(-1, 0)
        if key[K_d]:
            snakes[0].change_direction(1, 0)

        # handle arrows for snake2
        if key[K_UP]:
            snakes[1].change_direction(0, -1)
        if key[K_DOWN]:
            snakes[1].change_direction(0, 1)
        if key[K_LEFT]:
            snakes[1].change_direction(-1, 0)
        if key[K_RIGHT]:
            snakes[1].change_direction(1, 0)

    def snake_direction_new(self, snakes, events) -> None:
        """Changes snake directions using 2 keys only. Better for multiplayer support"""
        for event in events:         
            # Snake 1 direction   
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                snakes[0].turn_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                snakes[0].turn_right()
            #Snake 2 direction
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                snakes[1].turn_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                snakes[1].turn_right()
        
    def space_key(self, events) -> int:
        """Returns 1 if space key is released, 0 otherwise"""        
        for event in events:            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return 1
        return 0
            
    def left_right_selection(self, events) -> int:
        """Handles left right keys for selections. Returns default (0) / left (-1) / right (1)"""
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                return -1
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                return 1
        return 0
        
    def wait_for_space(self) -> bool:
        """Stops the game until the space key is pressed. Returns False if player is trying to quit."""
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            key = pygame.key.get_pressed()
            if key[K_SPACE]:
                return True
