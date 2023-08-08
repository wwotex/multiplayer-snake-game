import pygame
import time


class Snake(pygame.sprite.Sprite):
    def __init__(self, color, size, x, y, SCREEN):
        super().__init__()
        self.size = size
        self.color = color
        self.screen_width = SCREEN.get_width()
        self.screen_height = SCREEN.get_height()
        self.screen = SCREEN

        # Define initial position and direction
        self.x = x
        self.y = y
        self.direction = (1, 0)
        
        # Body of the snake (3 body segments originally)
        self.body = []
        self.body.append((x - 2*self.direction[0], y - 2*self.direction[1])) 
        self.body.append((x - self.direction[0], y - self.direction[1]))
        self.body.append((x, y)) # head

        self.time = time.time()
        # snakes speed determined by the delay (and so its not dependent on FPS but is strictly attached to the grid)
        self.movement_delay = 0.06

    def move(self):
        """Move the snake by 1 unit in the current direction."""
        if time.time() <= self.time + self.movement_delay:
            return
        
        self.x = (self.x + self.direction[0] * self.size) % self.screen_width
        self.y = (self.y + self.direction[1] * self.size) % self.screen_height
        
        self.body.append((self.x, self.y))
        del self.body[0]

        self.time = time.time()

    def change_direction(self, dx, dy):
        """Update direction of the snake"""
        # only change if it is not a 180 degree turn
        if dx != -self.direction[0] or dy != -self.direction[1]:
            self.direction = (dx, dy)

    # def update(self):
    #     """Update position of the snake"""
    #     self.rect.topleft = (self.x, self.y)

    def check_collision(self, other_sprite):
        """Check if the snake collides with another sprite (e.g., food)."""
        return self.rect.colliderect(other_sprite.rect)
    
    def draw(self):
        for snake_segment in self.body:
            pygame.draw.rect(self.screen, self.color, [snake_segment[0], snake_segment[1], self.size, self.size])
