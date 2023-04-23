import pygame
from settings import *
from tiles import Tile
from entities import Player
from os.path import join

class Level:
    def __init__(self, level_data, surface):
        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                cellX = column_index * TILE_SIZE
                cellY = row_index * TILE_SIZE
                if(cell == "x"):
                    tile = Tile((cellX,cellY),TILE_SIZE)
                    self.tiles.add(tile)
                if(cell == "p"):
                    player_sprite = Player((cellX,cellY))
                    self.player.add(player_sprite)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)

# def get_bg(theme):
#     image = pygame.image.load(join("assets", "tiles", "background", theme)).convert_alpha()
#     _, _, width, height = image.get_rect()
#     tiles = []

#     for i in range(WIDTH // width + 1):
#         for j in range(HEIGHT // height + 1):
#             #denote the position of the top-left corner of the current tile being added
#             pos = (i*width, j*height)
#             tiles.append(pos)
#     return tiles, image

# def draw_bg(window, background, bg_image):
#     #looping by every single tile, and drawing the bg_image at the tile pos
#     for tile in background:
#         window.blit(bg_image, tile)
    
#     pygame.display.update()