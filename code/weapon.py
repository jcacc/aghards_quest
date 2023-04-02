import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split('_')[0]

        # graphic
        full_path = f'graphics\weapons\{player.weapon}\{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        self.rect = self.image.get_rect(center=player.rect.center)

        # placement
        if direction == 'right':
            self.rect.midleft = player.rect.midright + pygame.math.Vector2(0, 16)
        elif direction == 'left':
            self.rect.midright = player.rect.midleft + pygame.math.Vector2(0, 16)
        elif direction == 'down':
            self.rect.midtop = player.rect.midbottom + pygame.math.Vector2(-10, 0)
        else:
            self.rect.midbottom = player.rect.midtop + pygame.math.Vector2(-10, 0)

        self.player = player
        self.groups = groups

    def update(self):
        # move the weapon with the player
        self.rect.center = self.player.rect.center

        # display the weapon image
        self.groups[0].screen.blit(self.image, self.rect)














#before
# class Weapon(pygame.sprite.Sprite):
#     def __init__(self,player,groups):
#         super().__init__(groups)
#         direction = player.status.split('_')[0]

#         # graphic
#         full_path = f'graphics\weapons\{player.weapon}\{direction}.png'
#         self.image = pygame.image.load (full_path).convert_alpha()
#         self.rect = self.image.get_rect(center = player.rect.center)

#         # placement
#         if direction == 'right':
#             self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
#         elif direction == 'left':
#             self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
#         elif direction == 'down':
#             self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
        
            
            
#         else:
#             self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))