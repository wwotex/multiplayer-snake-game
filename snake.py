from typing import Any, Iterable, Union
import pygame
import time
import random
from pygame.sprite import AbstractGroup

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, color, size, x, y):
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.size = size

        # Define initial position
        self.rect.x = x
        self.rect.y = y

class Snake(pygame.sprite.AbstractGroup):
    def __init__(self, color, block_size, screen, all_sprites_list) -> None:
        super().__init__()
        self.Q = []
        self.color = color
        self.block_size = block_size
        self.screen = screen # width and height can be accessed using .get_width() and .get_height() functions
        self.all_sprites_list = all_sprites_list
        self.movement_delay = 0.06 # snakes speed determined by the delay (and so its not dependent on FPS but is strictly attached to the grid)
        self.time = time.time()
        self.score = 0
        self.x = random.randint(0, (self.screen.get_width() - self.block_size) / self.block_size) * self.block_size
        self.y = random.randint(0, (self.screen.get_height() - self.block_size) / self.block_size) * self.block_size
        self.direction = (1,0)

        # Initial body of the snake
        self.add(SnakeSegment(color, 20, self.x, self.y))

    def add(self, *sprites) -> None:
        """Adds sprites to the AbstractSpriteGroup and to the Q snake body segment list"""
        super().add(*sprites)
        self.Q.append(*sprites)

    def move(self, food: pygame.sprite.Sprite) -> None:
        """Move the snake by 1 unit in the current direction."""
        if time.time() <= self.time + self.movement_delay:
            return
        
        if not self.Q:
            return
        
        self.x = (self.x + self.direction[0] * self.block_size) % self.screen.get_width()
        self.y = (self.y + self.direction[1] * self.block_size) % self.screen.get_height()
        segment = SnakeSegment(self.color, self.block_size, self.x, self.y)
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

    def change_direction(self, dx: int, dy: int) -> None:
        """Update direction of the snake"""
        # only change if it is not a 180 degree turn
        if dx != -self.direction[0] or dy != -self.direction[1]:
            self.direction = (dx, dy)

    def turn_left(self) -> None:
        """Update direction of the snake by making a 90 degree LEFT turn"""
        dx = self.direction[1]
        dy = -self.direction[0]
        self.direction = (dx, dy)

    def turn_right(self) -> None:
        """Update direction of the snake by making a 90 degree RIGHT turn."""
        dx = -self.direction[1]
        dy = self.direction[0]
        self.direction = (dx, dy)

    def check_collision(self, other_sprite: pygame.sprite.Sprite)  -> None:
        """Checks collision between snake head and passed sprite"""
        # Check whether list is empty
        if not self.Q:
            return False
        
        #head is self.Q[-1].rect
        return pygame.Rect.colliderect(self.Q[-1].rect,other_sprite.rect)
        
    def self_collision(self) -> None:
        """Handles collision with own body segments"""
        if not self.Q:
            return
        
        for segment in self.Q[:-1]:
            if self.check_collision(segment):
                print("You bit yourself. You died from poisoning")
                # Delete the entire snake
                for _ in range(len(self.Q)):
                    delete = self.Q.pop(0)
                    self.all_sprites_list.remove(delete)
                return

    def enemy_collision(self, snake: 'Snake')  -> None:
        """Handles collision with enemy snake"""
        if not (self.Q and snake.Q):
            return
        
        # if the snakes collide head by head
        if self.check_collision(snake.Q[-1]):
            print("Yall made out. Cute but you poisoned each other and you're both dead #Romeo&Juliet")
            self.delete_snake()
            snake.delete_snake()

        # Snake collided with a bodypart of the other snake
        for segment in snake.Q:
            if self.check_collision(segment):
                print("You bumped into your mate. You died from embarassment.")
                # Delete the entire snake
                self.delete_snake()
                return
            
    def delete_snake(self) -> None:
        """Deletes all body segments of the snake"""
        for _ in range(len(self.Q)):
            delete = self.Q.pop(0)
            self.all_sprites_list.remove(delete)

    def reset(self) -> None:
        """Resets Snake at specified coordinates"""
        # make sure snake is deleted
        self.delete_snake()
        self.x = random.randint(0, (self.screen.get_width() - self.block_size) / self.block_size) * self.block_size
        self.y = random.randint(0, (self.screen.get_height() - self.block_size) / self.block_size) * self.block_size
        self.direction = (1,0) # reset direction
        self.time = time.time()

        # reset body of the snake
        # self.Q = [] # delete body
        new_head = SnakeSegment(self.color, 20, self.x, self.y)
        self.add(new_head)
        self.all_sprites_list.add(new_head)