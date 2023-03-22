import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\\python_projects\\aghards_quest\\graphics\\test\\player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        print("Player created!")

        
    def input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction.y = -1
                print("Up arrow key pressed!")
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                print("Down arrow key pressed!")
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                print("Left arrow key pressed!")
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                print("Right arrow key pressed!")
            else:
                self.direction.x = 0

    def move(self, speed):
        self.rect.center += self.direction * speed
        print("Player position:", self.rect.center)

    def update(self):
        self.input()
        self.move(self.speed)

