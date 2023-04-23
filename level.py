import pygame
from settings import *
from os.path import join

def get_bg(theme):
    image = pygame.image.load(join("assets", "tiles", "background", theme)).convert_alpha()
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            #denote the position of the top-left corner of the current tile being added
            pos = (i*width, j*height)
            tiles.append(pos)
    return tiles, image

def draw_bg(window, background, bg_image):
    #looping by every single tile, and drawing the bg_image at the tile pos
    for tile in background:
        window.blit(bg_image, tile)
    
    pygame.display.update()