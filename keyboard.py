import pygame
from pygame.locals import *


class KeyboardController:
    def __init__(self, player_number, snake1, snake2) -> None:
        self.player_number = player_number
        self.snake1 = snake1
        self.snake2 = snake2

    def handleKeyPress(self) -> None:
        """Handles keys for snakes"""
        key = pygame.key.get_pressed()
        # handle "wsad" keys for snake1
        if key[K_w]:
            self.snake1.change_direction(0, -1)
        if key[K_s]:
            self.snake1.change_direction(0, 1)
        if key[K_a]:
            self.snake1.change_direction(-1, 0)
        if key[K_d]:
            self.snake1.change_direction(1, 0)

        # handle arrows for snake2
        if key[K_UP]:
            self.snake2.change_direction(0, -1)
        if key[K_DOWN]:
            self.snake2.change_direction(0, 1)
        if key[K_LEFT]:
            self.snake2.change_direction(-1, 0)
        if key[K_RIGHT]:
            self.snake2.change_direction(1, 0)

    def space_key(self) -> int:
        """Returns 1 if space key is pressed, 0 otherwise"""        
        key = pygame.key.get_pressed()
        if key[K_SPACE]:
            return 1
        else:
            return 0
            
    def left_right_selection(self) -> int:
        """Handles left right keys for selections. Returns default (0) / left (-1) / right (1)"""
        key = pygame.key.get_pressed()
        if key[K_a] or key[K_LEFT]:
            return -1
        elif key[K_w] or key[K_RIGHT]:
            return 1
        else:
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
