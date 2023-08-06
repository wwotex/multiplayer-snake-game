import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snake1 = pygame.Rect((10, 10, 20, 20))
color1 = (255, 0, 0)
bgColor = (0, 0, 0)

run = True
while run:
    screen.fill(bgColor)  

    pygame.draw.rect(screen, color1, snake1)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        snake1.move_ip(0, -1)
    if key[pygame.K_DOWN] == True:
        snake1.move_ip(0, 1)
    if key[pygame.K_LEFT] == True:
        snake1.move_ip(-1, 0)
    if key[pygame.K_RIGHT] == True:
        snake1.move_ip(1, 0)
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()