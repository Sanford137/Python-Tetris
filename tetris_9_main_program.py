# Tetris

'''This program runs Tetris.'''
 
# ------------Imports-----------
 
import pygame
import random
import tetris_9_classes
import tetris_9_functions
import tetris_9_start_screen
import tetris_9_game_over_screen

# --------------Initilization------------

pygame.init()

# ------------Globals------------
 
# Colors
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (0, 150, 150)
RED = (255, 0, 0)
ORANGE = (255, 100, 100)
LIGHT_BLUE = (0, 0, 150)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 200)

# Level
level = 1
lines_shattered = 0

# Rotation
rotating = False

# Score
score = 0

# Done 
done = False

# Quit
quit = False

# ----------------Data Structures--------------

current_shape = pygame.sprite.Group()
next_shape = pygame.sprite.Group()
other_shapes = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

list_of_rows, list_of_row_groups = tetris_9_functions.create_row_lists()

current_shape_list = []
input_shape = tetris_9_functions.create_shape_input()
current_shape_list = tetris_9_functions.create_shape(current_shape, current_shape_list, all_sprites_group, input_shape, level)

next_shape_list = []
next_input_shape = tetris_9_functions.create_shape_input()
next_shape_list = tetris_9_functions.create_shape(next_shape, next_shape_list, all_sprites_group, next_input_shape, level)
for block in next_shape:
    block.rect.x += 235
    block.rect.y += 175
    
# ------------Window-----------

size = (500, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() 

# ---------- Start Screen ------------

done = tetris_9_start_screen.open_start_screen()

# -------- Main Program Loop -----------

while not done:
    
    # --- Main Event Loop
    
    # Changes variables in response to keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                for block in current_shape:
                    block.speed_x = 30
            elif event.key == pygame.K_LEFT:
                for block in current_shape:
                    block.speed_x = -30
            elif event.key == pygame.K_DOWN:
                for block in current_shape:
                    block.speed_y = 15
            elif event.key == pygame.K_SPACE:
                rotating = True
     
    # --- Game Logic
    
    # Changes level
    if lines_shattered == 10:
        level += 1
        lines_shattered = 0   
    
    # Horizontal movement
    for block in current_shape:
        block.move_horizontal()
    
    collisions = pygame.sprite.groupcollide(current_shape, other_shapes, False, False)
    
    for block in current_shape:
        if block.rect.x < 0 or block.rect.x > 270:
            collisions = 1
            
    if collisions != {}:
        for block in current_shape:
            block.speed_x *= -1
            block.move_horizontal()
    
    # Vertical movement
    for block in current_shape:
        block.move_vertical()
        
    collisions = pygame.sprite.groupcollide(current_shape, other_shapes, False, False)

    for block in current_shape:
        if block.rect.y >= 570:
            collisions = 1  
        
    if collisions != {}:
        for block in current_shape:
            block.rect.y -= block.rect.y % 30
            other_shapes.add(block)
        input_shape = next_input_shape
        current_shape_list = tetris_9_functions.create_shape(current_shape, current_shape_list, all_sprites_group, input_shape, level)
        for sprite in next_shape:
            sprite.kill()
        next_input_shape = tetris_9_functions.create_shape_input()
        next_shape_list = tetris_9_functions.create_shape(next_shape, next_shape_list, all_sprites_group, next_input_shape, level)
        for block in next_shape:
            block.rect.x += 235
            block.rect.y += 175        
        
    # Rotates moving shape
    if rotating == True:
        input_shape, current_shape_list = tetris_9_functions.rotate(input_shape, current_shape, current_shape_list, all_sprites_group, level)
        
        collisions = pygame.sprite.groupcollide(current_shape, other_shapes, False, False)
        
        if collisions != {}:
            input_shape, current_shape_list = tetris_9_functions.rotate(input_shape, current_shape, current_shape_list, all_sprites_group, level)
            input_shape, current_shape_list = tetris_9_functions.rotate(input_shape, current_shape, current_shape_list, all_sprites_group, level)
            input_shape, current_shape_list = tetris_9_functions.rotate(input_shape, current_shape, current_shape_list, all_sprites_group, level)
        for block in current_shape:
            block.rect.x = block.rect.x - (block.rect.x % 30)
            block.rect.y = block.rect.y - (block.rect.y % 30)
        
        for block in current_shape:    
            if block.rect.x < 0:
                x = block.rect.x
                for item in current_shape:
                    item.rect.x -= x
            if block.rect.x > 270:
                y = block.rect.y - 270
                for item in current_shape:
                    item.rect.x -= y
        
        rotating = False
    
    # Deleting shapes that are helping cover a full row
    for i in range(20):
        row_full = True
        for sprite in list_of_rows[i]:
            if pygame.sprite.spritecollide(sprite, other_shapes, False) == []:
                row_full = False      
        if row_full == True:
            pygame.sprite.groupcollide(list_of_row_groups[i], other_shapes, False, True)
            score += 1
            for block in other_shapes:
                if block.rect.y < 30 * i + 10:
                    block.rect.y += 30
            lines_shattered += 1
    
    # Ends game when blocks go past top of screen
    for block in other_shapes:
        if block.rect.y <= 0:
            done = True
        
    # Resets speed_x
    for block in current_shape:
        block.speed_x = 0
                
    # --- Drawing Code
    
    # Fills screen with WHITE
    screen.fill(BLACK)
    
    # Draws all the sprites
    all_sprites_group.draw(screen)
    
    # Draws the lines
    for i in range(0, 11): # vertical lines
        pygame.draw.line(screen, GREY, [30 * i, 0], [30 * i, 600], 2)
    
    for i in range(0, 21): # horizontal lines
        pygame.draw.line(screen, GREY, [0, 30 * i], [300, 30 * i], 2)
        
    # Blits the score and level
    font = pygame.font.SysFont('Calibri', 35, True, False)
    
    text_score = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text_score, [315, 65])
    
    text_level = font.render("Level: " + str(level), True, WHITE)
    screen.blit(text_level, [315, 100])

    text_shape = font.render("Next Shape:", True, WHITE)
    screen.blit(text_shape, [315, 135])
    
    # --- Update Screen
    
    # Flips the display
    pygame.display.flip()
 
    # --- Loop Timing
    
    # Sets the main program loop to repeat 60 times a second
    clock.tick(60)

# ----------- Game Over Screen ------------

if quit == True:
    pygame.quit()
else:
    tetris_9_game_over_screen.open_game_over_screen(score, level)

