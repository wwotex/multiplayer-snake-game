import pygame

class Snake (pygame.sprite.Sprite):
    def __init__(self, color, size, x, y):
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

        # Adjust for snake movement speed
        self.speed = 1

        # Initialize position
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """Move the snake by dx and dy units in the current direction."""
        self.x += dx * self.speed
        self.y += dy * self.speed

    def update(self):
        """Update position of the snake"""
        self.rect.topleft = (self.x, self.y)

    def check_collision(self, other_sprite):
        """Check if the snake collides with another sprite (e.g., food)."""
        return self.rect.colliderect(other_sprite.rect)