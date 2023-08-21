import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_WIDTH = 200
CELL_HEIGHT = 50
CELL_SPACING = 10
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CELL_FONT = pygame.font.Font(None, 36)

# Colors
DARK = (70, 63, 58)
GRAY = (229, 236, 233)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clickable Cells")

# Cell values and states
cell_values = ["1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4"]
cell_states = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]  # True means cell has value, False means it's waiting for input

player_number = 8

# Create cells
x_displacement = (SCREEN_WIDTH - 3*CELL_WIDTH - 2*CELL_SPACING) // 2
y_displacement = (SCREEN_HEIGHT - (player_number+1)*CELL_HEIGHT - player_number * CELL_SPACING) // 2

cells = []

for i in range(player_number):
    cells.append(pygame.Rect(x_displacement + CELL_SPACING, y_displacement + (i+1) * CELL_SPACING + i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
    cells.append(pygame.Rect(x_displacement + CELL_WIDTH + 2*CELL_SPACING, y_displacement + (i+1) * CELL_SPACING + i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            for i, cell in enumerate(cells):
                if cell.collidepoint(event.pos) and cell_states[i]:
                    cell_states[i] = False

    screen.fill(DARK)
    
    for i, cell in enumerate(cells):
        pygame.draw.rect(screen, GRAY, cell, 2)  # Draw cell border

        if cell_states[i]:
            cell_text = CELL_FONT.render(cell_values[i], True, GRAY)
        else:
            cell_text = CELL_FONT.render("Click to input", True, GRAY)

        cell_text_rect = cell_text.get_rect(center=cell.center)
        screen.blit(cell_text, cell_text_rect)

    pygame.display.flip()

    while any(not state for state in cell_states):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                index = cell_states.index(False)
                cell_values[index] = pygame.key.name(event.key).upper()
                cell_states[index] = True

pygame.quit()
sys.exit()