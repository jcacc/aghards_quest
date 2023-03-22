import pygame 
from settings import *
from tile import Tile
from player import Player



class Level:
<<<<<<< HEAD
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
=======
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
>>>>>>> 17d68fefbb9b04de95fb9be7e93aa2f7cefe289c

		# sprite group setup
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

<<<<<<< HEAD
	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
				if col == 'p':
					Player((x,y),[self.visible_sprites])

	def run(self):
		# update and draw the game
		self.visible_sprites.draw(self.display_surface)
=======
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites])

    def run(self):
        # handle input for the player
        self.player.input()

        # update the player's position
        self.player.rect.move_ip(self.player.direction * self.player.speed)

        # draw the game world
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        print("Player update called:", self.player)

        # debug the player's direction
        debug(self.player.direction)
    
    def draw(self, surface):
        self.visible_sprites.draw(surface)




# class Level:
#     def __init__(self):

#         # get the display surface
#         self.display_surface = pygame.display.get_surface()

#         # sprite group setup
#         self.visible_sprites = pygame.sprite.Group()
#         self.obstacle_sprites = pygame.sprite.Group()

#         # sprite setup
#         self.create_map()

#     def create_map(self):
#         for row_index,row in enumerate(WORLD_MAP):
#             for col_index, col in enumerate(row):
#                 x = col_index * TILESIZE
#                 y = row_index * TILESIZE
#                 if col == 'x':
#                     Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
#                 if col == 'p':
#                     self.player = Player((x,y),[self.visible_sprites])                    
#     def run(self):
#         # update and draw the game
#         self.visible_sprites.draw(self.display_surface)
#         self.visible_sprites.update()
#         debug(self.player.direction)
        
>>>>>>> 17d68fefbb9b04de95fb9be7e93aa2f7cefe289c
