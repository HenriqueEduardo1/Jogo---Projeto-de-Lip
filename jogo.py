import sys
import os
import pygame
from pygame.locals import *
from settings import Settings
from morcego import Morcego
from fundo import Fundo

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("El Morcegón")

    bat = Morcego()
    todas_as_sprites = pygame.sprite.Group()
    sprite_fundo = pygame.sprite.Group()
    todas_as_sprites.add(bat)

    for i in range(2):
        fundo = Fundo(640,480,640 * i)
        sprite_fundo.add(fundo)


    while True:
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
        if sprite_fora_da_tela(sprite_fundo.sprites()[0]):
            sprite_fundo.remove(sprite_fundo.sprites()[0])
            novo_fundo = Fundo(640,480,640 * i-1)
            sprite_fundo.add(novo_fundo)

        sprite_fundo.draw(screen)
        todas_as_sprites.draw(screen)
        todas_as_sprites.update()
        sprite_fundo.update()
        pygame.display.flip()

def sprite_fora_da_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


run_game()
