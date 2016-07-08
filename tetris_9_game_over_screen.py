# Tetris Game Over Screen

''' This programs creates the game over screen for Tetris.'''

import pygame

pygame.init()
 
def open_game_over_screen(score, level):
    '''This function opens the start screen for Tetris.'''

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
      
    # Set the width and height of the screen [width, height]
    size = (500, 600)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Tetris")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
        # --- Game logic should go here
     
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)
        
        font = pygame.font.SysFont('Calibri', 100, True, False)
        text_title = font.render("Game Over", True, RED)
        screen.blit(text_title, [40, 150])
        
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text_instructions = font.render("Final score: " + str(score), True, WHITE)
        screen.blit(text_instructions, [70, 260])
        
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text_instructions = font.render("Highest level achieved: " + str(level), True, WHITE)
        screen.blit(text_instructions, [70, 330])        
     
        # --- Drawing code should go here
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
        
    # Closes the window and quits
    pygame.quit()