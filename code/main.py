# note to future joe, if something isn't working, check python interpreter
import pygame, sys
from settings import *
from debug import debug
from level import Level


class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Aghard's Quest")
        self.clock = pygame.time.Clock()

        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.screen.fill('black')
            # self.level.update()
            self.level.draw(self.screen)
            self.screen.run()
            pygame.display.update()
            self.clock.tick(FPS)




    # def run(self):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
            
    #         self.screen.fill('black')
    #         self.level.run()
    #         # debug('Hello :)')
    #         pygame.display.update()
    #         self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


