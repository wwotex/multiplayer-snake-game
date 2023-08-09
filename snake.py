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

class Snake(pygame.sprite.AbstractGroup, ):
    def __init__(self, color, size, x, y, screen, all_sprites_list) -> None:
        super().__init__()
        self.Q = []
        self.color = color
        self.size = size
        self.x = x # keeps track of the head x coordinate
        self.y = y # keeps track of the head y coordinate
        self.direction = (1,0)
        self.screen = screen # width and height can be accessed using .get_width() and .get_height() functions
        self.all_sprites_list = all_sprites_list
        self.alive = True

        # snakes speed determined by the delay (and so its not dependent on FPS but is strictly attached to the grid)
        self.movement_delay = 0.06
        self.time = time.time()

        # Initial body of the snake
        self.add(SnakeSegment(color, 20, x, y, screen))

    def add(self, *sprites):
        super().add(*sprites)
        self.Q.append(*sprites)

    def move(self, food):
        """Move the snake by 1 unit in the current direction."""
        if time.time() <= self.time + self.movement_delay:
            return
        
        if not self.alive:
            return
        
        self.x = (self.x + self.direction[0] * self.size) % self.screen.get_width()
        self.y = (self.y + self.direction[1] * self.size) % self.screen.get_height()
        segment = SnakeSegment(self.color, self.size, self.x, self.y, self.screen)
        self.Q.append(segment)
        self.all_sprites_list.add(segment)

        # Check for food collision. If not true: delete last segment to maintain length. Otherwise keep it to increase length
        if not self.check_collision(food):
            segment = self.Q.pop(0)
            self.all_sprites_list.remove(segment)
        else:
            food.spawn()

        # check if snake collides with itself. If yes it died
        self.self_collision()
      
        self.time = time.time()

    def change_direction(self, dx, dy):
        """Update direction of the snake"""
        # only change if it is not a 180 degree turn
        if dx != -self.direction[0] or dy != -self.direction[1]:
            self.direction = (dx, dy)

    def check_collision(self, other_sprite):
        #head is self.Q[-1].rect
        return pygame.Rect.colliderect(self.Q[-1].rect,other_sprite.rect)
        
    def self_collision(self):
        for segment in self.Q[:-1]:
            if self.check_collision(segment):
                print("You bit yourself. You died from poisoning")
                # Delete the entire snake
                self.alive = False
                for _ in range(len(self.Q)):
                    segment = self.Q.pop(0)
                    self.all_sprites_list.remove(segment)
                break


