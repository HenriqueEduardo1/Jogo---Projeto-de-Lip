from random import randrange
import pygame
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_img = os.path.join(diretorio_principal, 'img')

sprite_inseto = pygame.image.load(os.path.join(diretorio_img, 'inseto.png'))

class Inseto(pygame.sprite.Sprite):
    '''Classe para representar o inseto e seu movimento na tela'''

    def __init__(self, ai_s):
        pygame.sprite.Sprite.__init__(self)

        self.imgs_inseto = []
        self.ai_s = ai_s
    
        for i in range(0,3):
            img = sprite_inseto.subsurface((i * 29, 0),(29, 25))
            img = pygame.transform.scale(img, (29 * 1.5, 25 * 1.5))
            self.imgs_inseto.append(img)
        
        self.id_list = 0
        self.image = self.imgs_inseto[self.id_list]
        self.rect = self.image.get_rect()

        self.rect.x = randrange(self.ai_s.screen_w, self.ai_s.screen_w * 2, 45)
        self.rect.y = randrange(5, self.ai_s.screen_h - 40, 40)

    def update(self):
        if self.id_list > 2:
            self.id_list = 0

        self.id_list += 0.15
        self.image = self.imgs_inseto[int(self.id_list)]
        self.mask = pygame.mask.from_surface(self.image)

        if self.rect.topright[0] < 0:
            self.rect.x = randrange(self.ai_s.screen_w, self.ai_s.screen_w * 2, 45)
            self.rect.y = randrange(5, self.ai_s.screen_h - 40, 40) 
        
        self.rect.x -= self.ai_s.speed_inseto