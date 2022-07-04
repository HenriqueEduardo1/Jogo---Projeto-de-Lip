from random import randrange
import pygame
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_img = os.path.join(diretorio_principal, 'img')

sprite_inimigo = pygame.image.load(os.path.join(diretorio_img, 'inimigo.png'))

class Inimigo(pygame.sprite.Sprite):
    '''classe para representar os inimigos e seus movimentos na tela'''

    def __init__(self, ai_s):
        pygame.sprite.Sprite.__init__(self)

        self.imgs_inimigo = []
        self.ai_s = ai_s

        for i in range(0,4):
            img = sprite_inimigo.subsurface((i * 64, 0),(64, 44))
            img = pygame.transform.scale(img, (64 * 1.5, 44 * 1.5))
            self.imgs_inimigo.append(img)
        
        self.id_list = 0
        self.image = self.imgs_inimigo[self.id_list]
        self.rect = self.image.get_rect()

        self.rect.x = randrange(self.ai_s.screen_w, self.ai_s.screen_w * 2, 95)
        self.rect.y = randrange(5, self.ai_s.screen_h - 70, 70)
    
    def update(self):
        if self.id_list > 3:
            self.id_list = 0

        self.id_list += 0.15
        self.image = self.imgs_inimigo[int(self.id_list)]
        self.mask = pygame.mask.from_surface(self.image)

        if self.rect.topright[0] < 0:
            self.rect.x = randrange(self.ai_s.screen_w, self.ai_s.screen_w * 2, 95)
            self.rect.y = randrange(5, self.ai_s.screen_h - 70, 70) 
        
        self.rect.x -= self.ai_s.speed_inimigo