import pygame

class Fundo(pygame.sprite.Sprite):
    def __init__(self,width,height,xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('img/cavernous.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos

    def update(self):
        self.rect[0] -= 1