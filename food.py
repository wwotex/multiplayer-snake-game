import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, color, block_size, SCREEN):
        super().__init__()
        self.block_size = block_size
        self.screen_width = SCREEN.get_width()
        self.screen_height = SCREEN.get_height()

        # Spawn the food at a random position
        self.spawn()

    def spawn(self):
        """
        Spawns the food at a random position on the screen.
        """
        self.x = random.randint(0, (self.screen_width - self.block_size) / self.block_size) * self.block_size
        self.y = random.randint(0, (self.screen_height - self.block_size) / self.block_size) * self.block_size

    def draw(self):
        pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))