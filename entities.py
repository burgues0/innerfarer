import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        #how fast we are moving the player each frame
        self.x_velocity = 0
        self.y_velocity = 0
        self.gravity = 1
        self.fall_count = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    
    def movement(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def movement_left(self, velocity):
        self.x_velocity = -velocity
        if(self.direction != "left"):
            self.direction = "left"
            self.animation_count = 0

    def movement_right(self, velocity):
        self.x_velocity = velocity
        if(self.direction != "right"):
            self.direction = "right"
            self.animation_count = 0
    
    def key_input(self):
        self.x_velocity = 0
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_a]):
            self.movement_left(PLAYER_VELOCITY)
        if(keys[pygame.K_d]):
            self.movement_right(PLAYER_VELOCITY)

    def player_loop(self, fps):
        self.y_velocity += min(1, (self.fall_count / fps) * self.gravity)
        self.movement(self.x_velocity, self.y_velocity)
        self.key_input()

        self.fall_count += 1

    def draw_player(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)