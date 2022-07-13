import sys
import pygame
from fundo import Fundo
from inseto import Inseto
from inimigo import Inimigo


def update_screen(ai_s, screen, fundo, morcego, inimigos, insetos, bat):
    """Atualiza as imagens na tela"""
    
    update_fundo(ai_s, fundo)
    
    draw_jogo(morcego, fundo, inimigos, insetos, screen)

    check_colisao_inimigo(bat, morcego, fundo, inimigos, insetos)
    check_colisao_inseto(ai_s, bat, insetos, inimigos)

    update_jogo(morcego, fundo, inimigos, insetos)

    pygame.display.flip()


def update_fundo(ai_s, fundo):
    if sprite_fora_da_tela(fundo.sprites()[0]):
        fundo.remove(fundo.sprites()[0])
        new_fundo = Fundo(ai_s.screen_w, ai_s.screen_h, ai_s.screen_w, ai_s)
        fundo.add(new_fundo)

def check_events(bat):
    """Responde a eventos de pressionamento de teclas"""

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


def check_colisao_inseto(ai_s, bat, insetos, inimigos):
    #Testa a colisão com os insetos
    colisao_inseto = pygame.sprite.spritecollide(bat, insetos, True, pygame.sprite.collide_mask)

    if colisao_inseto:
        ai_s.pontos += 1
        print(ai_s.pontos)
        
        if ai_s.pontos % 30 == 0:
            if ai_s.speed_inimigo < 8:
                ai_s.speed_inimigo += 1
                ai_s.speed_fundo += 1
                ai_s.speed_inseto += 1
                ai_s.speed_bat += 0.5
                
        if ai_s.pontos % 50 == 0:
            if ai_s.quant_inimigos < 4:
                ai_s.quant_inimigos += 1
                ai_s.quant_insetos += 1
                create_inimigos(ai_s, inimigos)
                

    if len(insetos) == 0:
        create_insetos(ai_s, insetos)


def check_colisao_inimigo(bat, morcego, fundo, inimigos, insetos):
    #Testa a colisão com os inimigos
    colisao_inimigo = pygame.sprite.spritecollide(bat, inimigos, False, pygame.sprite.collide_mask)

    if colisao_inimigo:
        sys.exit()


def sprite_fora_da_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


def create_insetos(ai_s, insetos):
    while len(insetos) < ai_s.quant_insetos:
        new_inseto = Inseto(ai_s)
        insetos.add(new_inseto)


def create_inimigos(ai_s, inimigos):
    while len(inimigos) < ai_s.quant_inimigos:
        new_inimigo = Inimigo(ai_s)
        inimigos.add(new_inimigo)


def create_fundo(ai_s, fundo):
    for i in range(2):
        new_fundo = Fundo(ai_s.screen_w, ai_s.screen_h, ai_s.screen_w * i, ai_s)
        fundo.add(new_fundo)


def update_jogo(morcego, fundo, inimigos, insetos):
    morcego.update()
    fundo.update()
    inimigos.update()
    insetos.update()


def draw_jogo(morcego, fundo, inimigos, insetos, screen):
    fundo.draw(screen)
    morcego.draw(screen)
    inimigos.draw(screen)
    insetos.draw(screen)