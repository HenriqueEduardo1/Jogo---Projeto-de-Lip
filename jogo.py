import os
import pygame
from pygame.sprite import Group
from pygame.locals import *
from settings import Settings
from morcego import Morcego
import game_functions as gf
from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_w, ai_settings.screen_h))
    pygame.display.set_caption("El Morcegón")

    morcego = Group()
    fundo = Group()
    inimigos = Group()
    insetos = Group()

    bat = Morcego(ai_settings)
    morcego.add(bat)

    gf.create_insetos(ai_settings, insetos)
    gf.create_inimigos(ai_settings, inimigos)
    gf.create_fundo(ai_settings, fundo)

    play = Button(ai_settings, screen, "Play")

    while True:
        gf.check_events(bat)
        
        if ai_settings.game_on:
            bat.update_position()

        gf.update_screen(ai_settings, screen, fundo, morcego, inimigos, insetos, bat, play)

run_game()
