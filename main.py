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
all_sprites_list.add(snake1.segments, snake2.segments, food)

# Initializing clock
clock = pygame.time.Clock()
FPS = 1  # Adjust this value to control the game's frame rate

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

    # Check for collision between snakes and food
    if snake1.check_collision(food):
        snake1.grow()
        food.spawn()

    if snake2.check_collision(food):
        snake2.grow()
        food.spawn()


    # Update screen
    screen.fill(bgColor)

    # Update sprites
    print(all_sprites_list)

    # Assuming you have a subgroup named 'subgroup' within your all_sprites_list
    subgroup_sprites = all_sprites_list.snake1.sprites()

    for sprite in subgroup_sprites:
        # Access and print information about each sprite
        print(f"Sprite Position: ({sprite.rect.x}, {sprite.rect.y})")
        # You can access other attributes of the sprite as needed


    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()