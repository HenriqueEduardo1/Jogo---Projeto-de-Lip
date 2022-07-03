import pygame
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_img = os.path.join(diretorio_principal, 'img')

sprite_inimigo = pygame.image.load(os.path.join(diretorio_img, 'vulture.png'))

class inimigo():