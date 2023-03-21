import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\\python_projects\\aghards_quest\\graphics\\test\\player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction = pygame.math.Vector2(0,0)
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction = 0

    
def update(self):
    self.input()
    self.rect.move_ip(self.direction.x * PLAYER_SPEED, self.direction.y * PLAYER_SPEED)