import pygame
from entities import Player
from settings import *
from os import listdir
from os.path import isfile, join

def get_background(theme):
    image = pygame.image.load(join("assets", "sprites", "tiles", "background", theme)).convert_alpha()
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            #denote the position of the top-left corner of the current tile being added
            pos = (i*width, j*height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image, player):
    #looping by every single tile, and drawing the bg_image at the tile pos
    for tile in background:
        window.blit(bg_image, tile)
    
    player.draw_player(window)
    pygame.display.update()