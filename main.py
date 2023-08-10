import pygame
from pygame.locals import *
from keyboard import KeyboardController
from snake import Snake, SnakeSegment
from food import Food
import colors

pygame.init()

# Initializing screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font_style = pygame.font.SysFont(None, 30)

# Function for displaying messages on the screen
# Initializing screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


def message(screen, message, color):
    """Function for displaying messages on the screen"""
    font = pygame.font.SysFont(None, 30) # Initialize font
    text_surface = font.render(message, True, color) # Render the message
    # Get the dimensions of the text surface
    text_width, text_height = text_surface.get_size()
    # Calculate the coordinates to center the text
    x = (screen.get_width() - text_width) // 2
    y = (screen.get_height() - text_height) // 2
    
    # Blit the text surface onto the screen
    screen.blit(text_surface, (x, y))


# Initializing sprites group
all_sprites_list = pygame.sprite.Group()

# Initializing starting objects
snake1 = Snake(colors.RED, 20, 100, 100, screen, all_sprites_list)
snake2 = Snake(
    colors.PURPLE,
    20,
    SCREEN_WIDTH - 100,
    SCREEN_HEIGHT - 100,
    screen,
    all_sprites_list
)
food = Food(colors.YELLOW, 20, screen)

# Adding them to sprites group and adding controls
all_sprites_list.add(snake1, snake2, food)
controller = KeyboardController(snake1, snake2)

# Initializing clock
clock = pygame.time.Clock()
FPS = 60  # Adjust this value to control the game's frame rate

# Load initial screen
screen.fill(colors.DARK)
message(screen, "Welcome to the ultimate snake game. Press space to play.", colors.MINT_CREAM)
pygame.display.flip()
controller.wait_for_space()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controller.handleKeyPress()

    snake1.move(food)
    snake2.move(food)

    # Check if snake collided into the other
    snake1.enemy_collision(snake2)
    snake2.enemy_collision(snake1)
    
    # Update screen
    screen.fill(colors.DARK)
    # Both snakes died at the same time
    if not snake1.Q and not snake2.Q:
        message(screen, "Draw: You died at the same time.", colors.MINT_CREAM)
    # Player 1 died
    elif not snake1.Q and snake2.Q:       
        message(screen, "Player 2 wins!", colors.MINT_CREAM)
    #Player 2 died
    elif snake1.Q and not snake2.Q:
        message(screen, "Player 1 wins!", colors.MINT_CREAM)
    # No winner. Game continues. Update Sprites
    else:
        all_sprites_list.update()
        all_sprites_list.draw(screen)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
