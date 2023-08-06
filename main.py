import pygame
from pygame.locals import *
from snake import Snake
from food import Food

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
snake1 = Snake(RED, 20, 100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
snake2 = Snake(RED, 20, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, SCREEN_WIDTH, SCREEN_HEIGHT)
food = Food(YELLOW, 20, SCREEN_WIDTH, SCREEN_HEIGHT)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(snake1, snake2, food)

run = True
while run:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[K_w]:
        snake1.change_direction(0, -1)
    if key[K_s]:
        snake1.change_direction(0, 1)
    if key[K_a]:
        snake1.change_direction(-1, 0)
    if key[K_d]:
        snake1.change_direction(1, 0)

    if key[K_UP]:
        snake2.change_direction(0, -1)
    if key[K_DOWN]:
        snake2.change_direction(0, 1)
    if key[K_LEFT]:
        snake2.change_direction(-1, 0)
    if key[K_RIGHT]:
        snake2.change_direction(1, 0)

    snake1.move()
    snake2.move()

    # Add a 0.1-second delay
    pygame.time.delay(100)

    screen.fill(bgColor)

    # Check for collision between snakes and food
    if snake1.check_collision(food):
        food.spawn()

    if snake2.check_collision(food):
        food.spawn()  

    # Update sprites
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()

pygame.quit()