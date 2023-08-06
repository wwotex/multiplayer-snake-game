import pygame

class Snake (pygame.sprite.Sprite):
    def __init__(self, color, size):
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        pygame.draw.rect(self.image, color, [0, 0, size, size])

        self.rect = self.image.get_rect()