import pygame
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_img = os.path.join(diretorio_principal, 'img')

sprite_bat = pygame.image.load(os.path.join(diretorio_img, 'morcego.png'))

class Morcego(pygame.sprite.Sprite):

    def __init__(self, ai_s):
        pygame.sprite.Sprite.__init__(self)

        self.imgs_bat = []
        self.ai_s = ai_s

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        for i in range(0,5):
            img = sprite_bat.subsurface((i * 32, 0),(32, 32))
            img = pygame.transform.scale(img, (32 * 2.5, 32 * 2.5))
            self.imgs_bat.append(img)

        self.id_list = 0
        self.image = self.imgs_bat[self.id_list]
        self.rect = self.image.get_rect()
        self.rect.center = (200,150)
    
    def update(self):
        if self.id_list > 4:
            self.id_list = 0

        self.id_list += 0.15
        self.image = self.imgs_bat[int(self.id_list)]
    
    def update_position(self):
        if self.moving_right:
            self.rect.centerx += self.ai_s.speed_bat
        if self.moving_left:
            self.rect.centerx -= self.ai_s.speed_bat
        if self.moving_up:
            self.rect.centery -= self.ai_s.speed_bat
        if self.moving_down:
            self.rect.centery += self.ai_s.speed_bat