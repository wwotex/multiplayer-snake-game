import pygame
import colors

class Screen:
    def __init__(self,width,height):
        # Initializing screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.font_style = pygame.font.SysFont(None, 30)

    def get_width(self):
        """Returns width of the screen"""
        return self.width
    
    def get_height(self):
        """Returns height of the screen"""
        return self.height

    def centered_message(self, message, color):
        """Function for displaying messages on the screen"""
        font = pygame.font.SysFont(None, 30) # Initialize font
        text_surface = font.render(message, True, color) # Render the message

        # Get the dimensions of the text surface
        text_width, text_height = text_surface.get_size()

        # Calculate the coordinates to center the text
        x = (self.width - text_width) // 2
        y = (self.height - text_height) // 2

        # Blit the text surface onto the screen
        self.screen.blit(text_surface, (x, y))

    def starting_screen(self):
        """Displays the starting screen"""
        self.screen.fill(colors.DARK)
        self.centered_message("Welcome to the ultimate snake game. Press space to play.", colors.MINT_CREAM)
        pygame.display.flip()

    def render_game_screen(self, all_sprites_list, snake1, snake2):
        """Renders the screen during game."""
        self.screen.fill(colors.DARK)
        # Both snakes died at the same time
        if not snake1.Q and not snake2.Q:
            self.centered_message("Draw: You died at the same time.", colors.MINT_CREAM)
        # Player 1 died
        elif not snake1.Q and snake2.Q:       
            self.centered_message("Player 2 wins!", colors.MINT_CREAM)
        #Player 2 died
        elif snake1.Q and not snake2.Q:
            self.centered_message("Player 1 wins!", colors.MINT_CREAM)
        # No winner. Game continues. Update Sprites
        else:
            all_sprites_list.update()
            all_sprites_list.draw(self.screen)

        pygame.display.flip()
    