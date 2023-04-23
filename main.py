import pygame
import random, math
from entities import Player
from settings import *
from debug import debug
from level import get_background, draw

class Game:
    #standard pygame setup
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Innerfarer")
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.background, self.bg_image = get_background("orange.png")

        self.player = Player(100,100,32,32)

    def run(self):
        #event loop
        isRunning = True
        while isRunning:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    isRunning = False
                    break
            self.player.player_loop(FPS)
            draw(self.window, self.background, self.bg_image, self.player)
        pygame.quit()
        quit()

#check if this is the main file to instantiate the game class
if(__name__ == "__main__"):
    game = Game()
    game.run()