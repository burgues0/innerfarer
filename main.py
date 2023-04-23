import pygame, sys
from settings import *
from debug import debug
from level import get_bg, draw_bg

class Game:
    def __init__(self):
        #general setup | initiating pygame
        pygame.init()
        pygame.display.set_caption("Innerfarer")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.background, self.bg_image = get_bg("orange.png")

    def run(self):
        #event loop
        while True:
            for event in pygame.event.get():
                #checking if the game is being closed
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
            #filling the screen with color black
            #updating the screen
            #controlling the FPS
            draw_bg(self.screen, self.background, self.bg_image)
            pygame.display.update()
            self.clock.tick(FPS)

#check if this is the main file to instantiate the game class
if(__name__ == "__main__"):
    game = Game()
    game.run()