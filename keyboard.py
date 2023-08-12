import pygame
from pygame.locals import *


class KeyboardController:
    def __init__(self, snake1, snake2) -> None:
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

        
    def wait_for_space(self) -> bool:
        """Enters an infinite while loop until space key is pressed. Returns False if player is trying to quit."""
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            key = pygame.key.get_pressed()
            if key[K_SPACE]:
                return True