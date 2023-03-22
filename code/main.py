import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
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

<<<<<<< HEAD
			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
=======
        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.direction.y = -1
                    elif event.key == pygame.K_DOWN:
                        self.player.direction.y = 1
                    elif event.key == pygame.K_LEFT:
                        self.player.direction.x = -1
                    elif event.key == pygame.K_RIGHT:
                        self.player.direction.x = 1



            self.screen.fill('black')
            # self.level.update()
            self.level.draw(self.screen)
            # self.screen.run()
            pygame.display.update()
            self.clock.tick(FPS)
>>>>>>> 17d68fefbb9b04de95fb9be7e93aa2f7cefe289c




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
    #         self.clock.tick(FPS)a

if __name__ == '__main__':
	game = Game()
	game.run()