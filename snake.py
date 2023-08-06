import pygame

class Snake (pygame.sprite.Sprite):
    def __init__(self, color, size, x, y, screen_width, screen_height):
        """
        Initialize a new Snake instance.

        Parameters:
            color (tuple): RGB color value (e.g., (255, 0, 0) for red) representing the snake's appearance.
            size (int): The size (width and height) of the snake's body segments in pixels.
            x (int): The initial x-coordinate of the snake's position on the screen.
            y (int): The initial y-coordinate of the snake's position on the screen.

        Attributes:
            image (pygame.Surface): The surface representing the appearance of the snake's body segments.
            rect (pygame.Rect): The rectangular bounding box for the snake's current position on the screen.
            size (int): The size (width and height) of the snake's body segments in pixels.
            speed (int): The number of pixels the snake moves in each update, controlling its movement speed.
            x (int): The current x-coordinate of the snake's position on the screen.
            y (int): The current y-coordinate of the snake's position on the screen.
        """
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Adjust for snake movement speed
        self.speed = 20

        # Define initial position and direction
        self.x = x
        self.y = y
        self.direction = (1, 0)

    def move(self):
        """Move the snake by 1 unit in the current direction."""
        self.x = (self.x + self.direction[0] * self.speed) % self.screen_width
        self.y = (self.y + self.direction[1] * self.speed) % self.screen_height

    def change_direction(self, dx, dy):
        """Update direction of the snake"""
        # only change if it is not a 180 degree turn
        if dx != -self.direction[0] or dy != -self.direction[1]:
            self.direction = (dx, dy)

    def update(self):
        """Update position of the snake"""
        self.rect.topleft = (self.x, self.y)

    def check_collision(self, other_sprite):
        """Check if the snake collides with another sprite (e.g., food)."""
        return self.rect.colliderect(other_sprite.rect)