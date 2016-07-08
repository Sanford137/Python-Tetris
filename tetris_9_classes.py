# Tetris Classes

'''This program contains the classes for Tetris.'''

import pygame
import random

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


class Block(pygame.sprite.Sprite):
    '''This class represents the blocks that make up the shapes.'''
    
    def __init__(self, x_cordinate, y_cordinate, y_speed, color):
        ''' This is the constructor function.'''
        
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_cordinate
        self.rect.y = y_cordinate
        self.speed_x = 0
        self.speed_y = y_speed

    def move_horizontal(self):
        '''This function finds the block's new horizontal position each time through the main program loop.'''

        self.rect.x += self.speed_x
            
    def move_vertical(self):
        '''This function finds the block's new vertical position each time through the main program loop.'''
        
        self.rect.y += self.speed_y

class Box(pygame.sprite.Sprite):
    '''This class represents the (invisible) horizontal lines of boxes programmed so that, when a row of 10 of them is fully covered, the shapes that are helping to cover the row are destroyed.'''

    def __init__(self, x_cordinate, y_cordinate):
        '''This is the constructor function.'''
        
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_cordinate
        self.rect.y = y_cordinate