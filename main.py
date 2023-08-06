import pygame

from snake import Snake

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

color1 = (255, 0, 0)
bgColor = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snake1 = pygame.Rect((10, 10, 20, 20))
snake2 = Snake(color1, 20)
snake2.rect.x = 100
snake2.rect.y = 100

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(snake2)

run = True
while run:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        snake1.move_ip(0, -1)
    if key[pygame.K_DOWN] == True:
        snake1.move_ip(0, 1)
    if key[pygame.K_LEFT] == True:
        snake1.move_ip(-1, 0)
    if key[pygame.K_RIGHT] == True:
        snake1.move_ip(1, 0)

    screen.fill(bgColor)  

    all_sprites_list.update()

    all_sprites_list.draw(screen)
    pygame.draw.rect(screen, color1, snake1)
    pygame.display.flip()





    pygame.display.update()

pygame.quit()