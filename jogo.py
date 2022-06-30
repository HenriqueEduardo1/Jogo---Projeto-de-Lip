import os
import pygame
from pygame.locals import *
from settings import Settings
from morcego import Morcego
from fundo import Fundo
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_w, ai_settings.screen_h))
    pygame.display.set_caption("El Morcegón")

    todas_as_sprites = pygame.sprite.Group()
    sprite_fundo = pygame.sprite.Group()

    bat = Morcego(ai_settings, screen)
    todas_as_sprites.add(bat)

    for i in range(2):
        fundo = Fundo(ai_settings.screen_w, ai_settings.screen_h, ai_settings.screen_w * i)
        sprite_fundo.add(fundo)

    while True:
        gf.check_events(bat)
        bat.update_position()
        gf.update_screen(ai_settings, screen, sprite_fundo, todas_as_sprites)

run_game()
