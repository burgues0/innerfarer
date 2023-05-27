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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if(player_x < (WIDTH / 4) and direction_x < 0):
            self.world_shift = 8
            player.speed = 0
        elif (player_x > (WIDTH - (WIDTH / 4)) and direction_x > 0):
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def x_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if(sprite.rect.colliderect(player.rect)):
                if(player.direction.x < 0):
                    player.rect.left = sprite.rect.right
                elif(player.direction.x > 0):
                    player.rect.right = sprite.rect.left

    def y_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if(sprite.rect.colliderect(player.rect)):
                if(player.direction.y > 0):
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif(player.direction.y < 0):
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self): 
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.x_movement_collision()
        self.y_movement_collision()
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