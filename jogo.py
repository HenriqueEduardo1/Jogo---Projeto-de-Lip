import os
import pygame
from pygame.sprite import Group
from pygame.locals import *
from settings import Settings
from morcego import Morcego
import game_functions as gf
from button import Button
from playGame import PlayGame
from pontuacao import Pontuacao
from record import Record


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_w, ai_settings.screen_h))
    pygame.display.set_caption("El Morcegón")

    musica_fundo = pygame.mixer.music.load('sounds/Background Music.mp3')
    pygame.mixer.music.play(-1)

    morcego = Group()
    fundo = Group()
    inimigos = Group()
    insetos = Group()

    bat = Morcego(ai_settings)
    morcego.add(bat)

    gf.create_insetos(ai_settings, insetos)
    gf.create_inimigos(ai_settings, inimigos)
    gf.create_fundo(ai_settings, fundo)

    record = Record()
    play = Button(ai_settings, screen, "Play")
    play_game = PlayGame(ai_settings, record)
    pont = Pontuacao(ai_settings, screen, play_game)

    while True:
        gf.check_events(ai_settings, bat, inimigos, insetos, play, play_game, pont)
        
        if play_game.game_on:
            bat.update_position()

        gf.update_screen(ai_settings, screen, fundo, morcego, inimigos, insetos, bat, play, play_game, pont, record)

run_game()
