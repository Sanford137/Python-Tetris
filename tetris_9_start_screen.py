# Tetris Start Screen

''' This programs creates the start screen for Tetris.'''

import pygame

pygame.init()
 
def open_start_screen():
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
     
    done = False
    quit = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit = True
            elif event.type == pygame.KEYDOWN:
                done = True
     
        # --- Game logic should go here
     
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)
        
        font = pygame.font.SysFont('Calibri', 100, True, False)
        text_title = font.render("TETRIS", True, RED)
        screen.blit(text_title, [105, 180])
        
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text_instructions = font.render("press any key to start", True, WHITE)
        screen.blit(text_instructions, [94, 350])       
     
        # --- Drawing code should go here
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
        
    return quit