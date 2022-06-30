import sys
import pygame
from fundo import Fundo

def check_events():
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_s, screen, fundo, sprites):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    if sprite_fora_da_tela(fundo.sprites()[0]):
        fundo.remove(fundo.sprites()[0])
        novo_fundo = Fundo(ai_s.screen_w, ai_s.screen_h, ai_s.screen_w)
        fundo.add(novo_fundo)

    fundo.draw(screen)
    sprites.draw(screen)

    sprites.update()
    fundo.update()

    pygame.display.flip()

def sprite_fora_da_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])