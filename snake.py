import pygame

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, color, size, x, y):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        print("new segment created at" + str(self.rect.topleft))

class Snake (pygame.sprite.Sprite):
    def __init__(self, color, size, x, y, screen_width, screen_height):
        super().__init__()
        self.color = color
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Adjust for snake movement speed
        self.speed = 20
        self.direction = (1, 0)

        # Store the snake's body segments
        self.head = SnakeSegment(color, size, x, y)
        self.segments = pygame.sprite.Group(self.head)

        # Set the image and rect attributes for the snake
        self.image = self.head.image
        self.rect = self.head.rect

    def move(self):
        """Move the snake by 1 unit in the current direction."""
        # Remove the last segment and insert at front as new head
        print("Im moving in direction"+str(self.direction))
        print(self.segments)
        dx, dy = self.direction
        new_head_x = (self.head.rect.x + dx * self.speed) % self.screen_width
        new_head_y = (self.head.rect.y + dy * self.speed) % self.screen_height

        # Insert new segment at head
        new_segment = SnakeSegment(self.color, self.size, new_head_x, new_head_y)
        self.segments.add(new_segment)
        self.head = new_segment

        

    def grow(self):
        """Snake grows 1 body segment"""
        # Same as move() but without removing the last element
        dx, dy = self.direction
        new_head_x = (self.head.rect.x + dx * self.speed) % self.screen_width
        new_head_y = (self.head.rect.y + dy * self.speed) % self.screen_height
        new_segment = SnakeSegment(self.color, self.size, new_head_x, new_head_y)
        self.segments.add(new_segment)
        self.head = new_segment

    def update(self, all_sprites_list):
        """Update the snake sprite list"""
        all_sprites_list
        self.move()

    def change_direction(self, dx, dy):
        """Update direction of the snake"""
        # only change if it is not a 180 degree turn
        if dx != -self.direction[0] or dy != -self.direction[1]:
            self.direction = (dx, dy)

    def check_collision(self, other_sprite):
        """Check if the snake collides with another sprite (e.g., food)."""
        return self.head.rect.colliderect(other_sprite.rect)