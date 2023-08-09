from typing import Any, Iterable, Union
import pygame
import time

from pygame.sprite import AbstractGroup


class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, color, size, x, y, screen):
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.size = size
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Define initial position
        self.rect.x = x
        self.rect.y = y
        
    # def move(self):
    #     """Move the snake by 1 unit in the current direction."""
    #     if time.time() <= self.time + self.movement_delay:
    #         return
        
    #     self.x = (self.x + self.direction[0] * self.size) % self.screen_width
    #     self.y = (self.y + self.direction[1] * self.size) % self.screen_height
        
    #     self.time = time.time()

    # def update(self):
    #     """Update position of the snake"""
    #     self.rect.topleft = (self.x, self.y)

    # def check_collision(self, other_sprite):
    #     """Check if the snake collides with another sprite (e.g., food)."""
    #     return self.rect.colliderect(other_sprite.rect)


class Snake(pygame.sprite.AbstractGroup, ):
    def __init__(self, color, size, x, y, screen, all_sprites_list) -> None:
        super().__init__()
        self.Q = []
        self.color = color
        self.size = size
        self.x = x # keeps track of the head x coordinate
        self.y = y # keeps track of the head y coordinate
        self.direction = (1,0)
        self.screen = screen
        self.all_sprites_list = all_sprites_list
        # self.screen_width = screen.get_width()
        # self.screen_height = screen.get_height()

        # snakes speed determined by the delay (and so its not dependent on FPS but is strictly attached to the grid)
        self.movement_delay = 0.06
        self.time = time.time()

        # Initial body of the snake
        self.add(SnakeSegment(color, 20, x, y, screen))

    def add(self, *sprites):
        super().add(*sprites)
        self.Q.append(*sprites)

    # def move(self):
    #     segment = self.Q.pop(0)
    #     segment.x = (self.Q[-1].x + segment.size) % segment.screen_width
    #     self.Q.append(segment)

    def move(self, food):
        """Move the snake by 1 unit in the current direction."""
        if time.time() <= self.time + self.movement_delay:
            return
        
        self.x = (self.x + self.direction[0] * self.size) % self.screen.get_width()
        self.y = (self.y + self.direction[1] * self.size) % self.screen.get_height()
        segment = SnakeSegment(self.color, self.size, self.x, self.y, self.screen)
        self.Q.append(segment)
        self.all_sprites_list.add(segment)

        if self.check_collision(food):
            segment = self.Q.pop(0)
            self.all_sprites_list.remove(segment)
        else:
            food.spawn()

        # segment.x = (self.x + self.direction[0] * self.size) % self.screen_width
        # segment.y = (self.y + self.direction[1] * self.size) % self.screen_height
        
        self.time = time.time()

    def change_direction(self, dx, dy):
        """Update direction of the snake"""
        # only change if it is not a 180 degree turn
        if dx != -self.direction[0] or dy != -self.direction[1]:
            self.direction = (dx, dy)

    def check_collision(self, other_sprite):
        #head is self.Q[-1].rect
        return not pygame.Rect.colliderect(self.Q[-1].rect,other_sprite.rect)
        # idk why I had to negate it. I would expect the collide function to return true if they collide and false otherwise. And its code is doing union so this is how it should be. But somehow it is not.