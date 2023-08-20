import pygame
from pygame.locals import *


class KeyboardController:
    def __init__(self):
        self.player_controls = [
    [1073741904, 1073741903], # left arrow, right arrow
    [97, 115], # a, s
    [110, 109], # n, m
    [1073741918, 1073741921], # num pad 6, 9
    [99, 9], # ` key, tab key
    [53, 54], # 5 key, 6 key
    [57, 48], # 9 key, 0 key
    [1073741922, 1073741923] # num pad 0, num pad . key
]

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

    def snake_direction_new(self, snakes, events, player_number) -> None:
        """Changes snake directions using 2 keys only. Better for multiplayer support"""
        for i in range(player_number):         
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == self.player_controls[i][0]:
                    snakes[i].turn_left()
                if event.type == pygame.KEYDOWN and event.key == self.player_controls[i][1]:
                    snakes[i].turn_right()
            
            # # Snake 1 direction   
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            #     snakes[0].turn_left()
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            #     snakes[0].turn_right()
            # #Snake 2 direction
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     snakes[1].turn_left()
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     snakes[1].turn_right()
        
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
