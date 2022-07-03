import sys
import pygame
from fundo import Fundo

def check_events(bat):
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bat.moving_up = True
            elif event.key == pygame.K_DOWN:
                bat.moving_down = True
            elif event.key == pygame.K_LEFT:
                bat.moving_left = True
            elif event.key == pygame.K_RIGHT:
                bat.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                bat.moving_up = False
            elif event.key == pygame.K_DOWN:
                bat.moving_down = False
            elif event.key == pygame.K_LEFT:
                bat.moving_left = False
            elif event.key == pygame.K_RIGHT:
                bat.moving_right = False 

def update_screen(ai_s, screen, fundo, sprites, inimigo):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    if sprite_fora_da_tela(fundo.sprites()[0]):
        fundo.remove(fundo.sprites()[0])
        novo_fundo = Fundo(ai_s.screen_w, ai_s.screen_h, ai_s.screen_w)
        fundo.add(novo_fundo)

    fundo.draw(screen)
    sprites.draw(screen)
    inimigo.draw(screen)

    sprites.update()
    fundo.update()
    inimigo.update()

    pygame.display.flip()

def sprite_fora_da_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])