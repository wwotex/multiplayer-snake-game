import pygame
import random
from pygame.locals import *
from snake import Snake

def spawn_food():
    """
    Spawns food at a random location on the screen. 
    Returns Food rect.\n
    Example:\n
    food = spawn_food()
    """
    x = random.randint(0, SCREEN_WIDTH - 20)
    y = random.randint(0, SCREEN_HEIGHT - 20)
    return pygame.Rect(x, y, 20, 20)

pygame.init()

# Initializing screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Initializing colours
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
bgColor = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Initializing starting objects
snake1 = Snake(RED, 20, 100, 100)
snake2 = Snake(RED, 20, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(snake1, snake2)

food = spawn_food()

run = True
while run:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[K_w]:
        snake1.move(0, -1)
    if key[K_s]:
        snake1.move(0, 1)
    if key[K_a]:
        snake1.move(-1, 0)
    if key[K_d]:
        snake1.move(1, 0)

    if key[K_UP]:
        snake2.move(0, -1)
    if key[K_DOWN]:
        snake2.move(0, 1)
    if key[K_LEFT]:
        snake2.move(-1, 0)
    if key[K_RIGHT]:
        snake2.move(1, 0)

    screen.fill(bgColor)  

    all_sprites_list.update()

    all_sprites_list.draw(screen)
    pygame.draw.rect(screen, YELLOW, food)
    pygame.display.flip()

pygame.quit()