# Tetris Functions

'''This program contains the functions for Tetris.'''

import pygame
import random
import tetris_9_classes

current_shape = pygame.sprite.Group()
next_shape = pygame.sprite.Group()
other_shapes = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

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


def create_shape(shape, shape_list, all_sprites, input_shape, level):
    '''This function creates the shapes.'''
    
    shape.empty()
    shape_list = []
    for i in range(4):
        if input_shape == "I-1":
            block = tetris_9_classes.Block(90 + 30 * i, 0, 1 + level, LIGHT_BLUE)
        if input_shape == "I-2":
            block = tetris_9_classes.Block(120, 30 * i, 1 + level, LIGHT_BLUE)
        if input_shape == "J-1":
            if i < 3:
                block = tetris_9_classes.Block(90 + 30 * i, 0, 1 + level, BLUE)
            if i == 3:
                block = tetris_9_classes.Block(150, 30, 1 + level, BLUE)
        if input_shape == "J-2":
            if i < 3:
                block = tetris_9_classes.Block(150, 30 * i, 1 + level, BLUE)
            if i == 3:
                block = tetris_9_classes.Block(120, 60, 1 + level, BLUE)
        if input_shape == "J-3":
            if i < 3:
                block = tetris_9_classes.Block(90 + 30 * i, 30, 1 + level, BLUE)
            if i == 3:
                block = tetris_9_classes.Block(90, 0, 1 + level, BLUE)
        if input_shape == "J-4":
            if i < 3:
                block = tetris_9_classes.Block(120, 30 * i, 1 + level, BLUE)
            if i == 3:
                block = tetris_9_classes.Block(150, 0, 1 + level, BLUE)
        if input_shape == "L-1":
            if i < 3:
                block = tetris_9_classes.Block(90 + 30 * i, 0, 1 + level, ORANGE)
            if i == 3:
                block = tetris_9_classes.Block(90, 30, 1 + level, ORANGE)
        if input_shape == "L-2":
            if i < 3:
                block = tetris_9_classes.Block(150, 30 * i, 1 + level, ORANGE)
            if i == 3:
                block = tetris_9_classes.Block(120, 0, 1 + level, ORANGE)
        if input_shape == "L-3":
            if i < 3:
                block = tetris_9_classes.Block(90 + 30 * i, 30, 1 + level, ORANGE)
            if i == 3:
                block = tetris_9_classes.Block(150, 0, 1 + level, ORANGE)
        if input_shape == "L-4":
            if i < 3:
                block = tetris_9_classes.Block(120, 30 * i, 1 + level, ORANGE)
            if i == 3:
                block = tetris_9_classes.Block(150, 60, 1 + level, ORANGE)
        if input_shape == "O-1":
            if i < 2:
                block = tetris_9_classes.Block(120 + 30 * i, 0, 1 + level, YELLOW)
            if i  >= 2:
                block = tetris_9_classes.Block(60 + 30 * i, 30, 1 + level, YELLOW)
        if input_shape == "S-1":
            if i < 2:
                block = tetris_9_classes.Block(120 + 30 * i, 0, 1 + level, GREEN)
            if i  >= 2:
                block = tetris_9_classes.Block(30 + 30 * i, 30, 1 + level, GREEN)
        if input_shape == "S-2":
            if i < 2:
                block = tetris_9_classes.Block(120, 30 * i, 1 + level, GREEN)
            if i  >= 2:
                block = tetris_9_classes.Block(150, 30 * i - 30, 1 + level, GREEN)        
        if input_shape == "T-1":
            if i < 3:
                block = tetris_9_classes.Block(90 + 30 * i, 0, 1 + level, PURPLE)
            if i  == 3:
                block = tetris_9_classes.Block(120, 30, 1 + level, PURPLE)
        if input_shape == "T-2":
            if i < 3:
                block = tetris_9_classes.Block(150, 30 * i, 1 + level, PURPLE)
            if i  == 3:
                block = tetris_9_classes.Block(120, 30, 1 + level, PURPLE)
        if input_shape == "T-3":
            if i < 3:
                block = tetris_9_classes.Block(90 + 30 * i, 30, 1 + level, PURPLE)
            if i  == 3:
                block = tetris_9_classes.Block(120, 0, 1 + level, PURPLE)
        if input_shape == "T-4":
            if i < 3:
                block = tetris_9_classes.Block(120, 30 * i, 1 + level, PURPLE)
            if i  == 3:
                block = tetris_9_classes.Block(150, 30, 1 + level, PURPLE)
        if input_shape == "Z-1":
            if i < 2:
                block = tetris_9_classes.Block(90 + 30 * i, 0, 1 + level, RED)
            if i >= 2:
                block = tetris_9_classes.Block(60 + 30 * i, 30, 1 + level, RED)
        if input_shape == "Z-2":
            if i < 2:
                block = tetris_9_classes.Block(120, 30 * i + 30, 1 + level, RED)
            if i >= 2:
                block = tetris_9_classes.Block(150, 30 * i - 60, 1 + level, RED)
        all_sprites.add(block)
        shape.add(block)
        shape_list.append(block)
    return shape_list

def create_row_lists():
    '''This function creates the box sprites and returns two lists of them. Both lists are divided into rows; one consists of sub-lists of them, the other of sub-groups of them.'''
    
    list_of_rows = []
    list_of_row_groups = []
    for i in range(20):
        row_i = []
        row_i_group = pygame.sprite.Group()
        for j in range(10):
            box = tetris_9_classes.Box(10 + 30 * j, 10 + 30 * i)
            row_i.append(box)
            row_i_group.add(box)
            all_sprites_group.add(box)
        list_of_rows.append(row_i)
        list_of_row_groups.append(row_i_group)
    return list_of_rows, list_of_row_groups

def create_shape_input():
    '''This function returns random values for input_shape.'''
    
    shape_options = [["I-1", "I-2"], ["J-1", "J-2", "J-3", "J-4"], ["L-1", "L-2", "L-3", "L-4"], ["O-1"], ["S-1", "S-2"], ["T-1", "T-2", "T-3", "T-4"], ["Z-1", "Z-2"]]
    shape_type = random.randrange(7)
    if shape_type == 0 or shape_type == 4 or shape_type == 6:
        shape_rotation = random.randrange(2)
    if shape_type == 1 or shape_type == 2 or shape_type == 5:
        shape_rotation = random.randrange(4)
    if shape_type == 3:
        shape_rotation = 0
    input_shape = shape_options[shape_type][shape_rotation]
    return input_shape

def rotate(input_shape, current_shape, current_shape_list, all_sprites, level):
    '''This function rotates the falling shape.'''
    
    if input_shape == "I-1":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y + 15
        input_shape = "I-2"
    elif input_shape == "I-2":
        x = current_shape_list[1].rect.x - 105
        y = current_shape_list[1].rect.y - 45
        input_shape = "I-1"
    elif input_shape == "J-1":
        x = current_shape_list[1].rect.x - 105
        y = current_shape_list[1].rect.y - 15
        input_shape = "J-2"
    elif input_shape == "J-2":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "J-3"
    elif input_shape == "J-3":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "J-4"
    elif input_shape == "J-4":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 45
        input_shape = "J-1"
    elif input_shape == "L-1":
        x = current_shape_list[1].rect.x - 105
        y = current_shape_list[1].rect.y - 15
        input_shape = "L-2"
    elif input_shape == "L-2":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "L-3"
    elif input_shape == "L-3":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "L-4"
    elif input_shape == "L-4":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 45
        input_shape = "L-1"
    elif input_shape == "O-1":
        x = current_shape_list[0].rect.x - 120
        y = current_shape_list[0].rect.y
        input_shape = "O-1"
    elif input_shape == "S-1":
        x = current_shape_list[1].rect.x - 105
        y = current_shape_list[1].rect.y - 15
        input_shape = "S-2"
    elif input_shape == "S-2":
        x = current_shape_list[0].rect.x - 135
        y = current_shape_list[0].rect.y - 15
        input_shape = "S-1"
    elif input_shape == "T-1":
        x = current_shape_list[1].rect.x - 105
        y = current_shape_list[1].rect.y - 15
        input_shape = "T-2"
    elif input_shape == "T-2":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "T-3"
    elif input_shape == "T-3":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "T-4"
    elif input_shape == "T-4":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 45
        input_shape = "T-1"
    elif input_shape == "Z-1":
        x = current_shape_list[0].rect.x - 105
        y = current_shape_list[0].rect.y - 15
        input_shape = "Z-2"
    elif input_shape == "Z-2":
        x = current_shape_list[1].rect.x - 135
        y = current_shape_list[1].rect.y - 15
        input_shape = "Z-1"
    for sprite in current_shape:
        sprite.kill()       
    current_shape_list = create_shape(current_shape, current_shape_list, all_sprites, input_shape, level)
    for block in current_shape:
        block.rect.x += x
        block.rect.y += y
    return input_shape, current_shape_list