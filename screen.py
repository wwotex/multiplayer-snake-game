import pygame
import colors
import time

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

    def render_game_screen(self, controller, all_sprites_list: pygame.sprite.Group, snake1, snake2):
        """Renders the screen during game."""
        if not (snake1.Q and snake2.Q): # Check for winner
            self.winner_message(controller, snake1, snake2)
        else: # No winner. Game continues. Update Sprites
            self.screen.fill(colors.DARK)
            all_sprites_list.update()
            all_sprites_list.draw(self.screen)

        pygame.display.flip()

    def winner_message(self, controller, snake1, snake2) -> None:
        """Displays the round winner message on top of the current screen"""
        # Both snakes died at the same time
        if not snake1.Q and not snake2.Q:
            self.centered_message("Draw! Press space to restart.", colors.MINT_CREAM)
            pygame.display.flip()
            controller.wait_for_space()
            self.display_scores(controller, snake1.score,snake2.score)
            snake1.reset(100, 100)
            snake2.reset(self.width - 100, self.height - 100)
        # Player 1 died
        elif not snake1.Q and snake2.Q:
            snake2.score += 1       
            self.centered_message("Player 2 wins! Press space to restart.", colors.MINT_CREAM)
            pygame.display.flip()
            controller.wait_for_space()
            self.display_scores(controller, snake1.score,snake2.score)
            snake1.reset(100, 100)
            snake2.reset(self.width - 100, self.height - 100)
        #Player 2 died
        elif snake1.Q and not snake2.Q:
            snake1.score += 1
            self.centered_message("Player 1 wins! Press space to restart.", colors.MINT_CREAM)
            pygame.display.flip()
            controller.wait_for_space()
            self.display_scores(controller, snake1.score,snake2.score)
            snake1.reset(100, 100)
            snake2.reset(self.width - 100, self.height - 100)

    def display_scores(self, controller, score1: int, score2: int) -> None:
        """Displays scores on the screen"""
        print("Im displaying scores")
        self.screen.fill(colors.DARK)
        self.centered_message("The current score is: " + str(score1) + " : " + str(score2) + "! Press space to continue.", colors.MINT_CREAM)
        pygame.display.flip()
        time.sleep(1)
        controller.wait_for_space()
        

    