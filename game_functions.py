import sys
import pygame
from fundo import Fundo
from inseto import Inseto
from inimigo import Inimigo


def update_screen(ai_s, screen, fundo, morcego, inimigos, insetos, bat, play, play_g):
    """Atualiza as imagens na tela"""
    
    update_fundo(ai_s, fundo)
    
    draw_jogo(ai_s, morcego, fundo, inimigos, insetos, screen, play, play_g)

    check_colisao_inimigo(ai_s, bat, morcego, fundo, inimigos, insetos, play_g)
    #check_colisao_inseto(ai_s, bat, insetos, inimigos, play_g)

    update_jogo(ai_s, morcego, fundo, inimigos, insetos, play_g)

    pygame.display.flip()


def update_fundo(ai_s, fundo):
    if sprite_fora_da_tela(fundo.sprites()[0]):
        fundo.remove(fundo.sprites()[0])
        new_fundo = Fundo(ai_s.screen_w, ai_s.screen_h, ai_s.screen_w, ai_s)
        fundo.add(new_fundo)

def check_events(ai_s, bat, inimigos, insetos, play, play_g):
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_s, inimigos, insetos, play, mouse_x, mouse_y, play_g, bat)


def check_play_button(ai_s, inimigos, insetos, play, mouse_x, mouse_y, play_g, bat):
    """Inicia o jogo quando o jogador clicar em Play."""
    button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not play_g.game_on:
        ai_s.inicializar_config()
        #pygame.mouse.set_visible(False)

        play_g.reset_pontos()
        play_g.game_on = True

        inimigos.empty()
        insetos.empty()

        create_inimigos(ai_s, inimigos)
        create_insetos(ai_s, insetos)
        bat.alinha_bat(ai_s)





def check_colisao_inseto(ai_s, bat, insetos, inimigos, play_g):
    #Testa a colisão com os insetos
    colisao_inseto = pygame.sprite.spritecollide(bat, insetos, True, pygame.sprite.collide_mask)

    if colisao_inseto:
        ai_s.pontos += 1
        print(ai_s.pontos)
        
        if ai_s.pontos % 30 == 0:
            if ai_s.speed_inimigo < 8:
                ai_s.incremento_velociade()
                
        if ai_s.pontos % 50 == 0:
            if ai_s.quant_inimigos < 4:
                ai_s.incremento_ini_ins()
                create_inimigos(ai_s, inimigos)
                

    if len(insetos) == 0:
        create_insetos(ai_s, insetos)


def check_colisao_inimigo(ai_s, bat, morcego, fundo, inimigos, insetos, play_g):
    #Testa a colisão com os inimigos
    colisao_inimigo = pygame.sprite.spritecollide(bat, inimigos, False, pygame.sprite.collide_mask)

    if colisao_inimigo:
        play_g.game_on = False
        


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


def update_jogo(ai_s, morcego, fundo, inimigos, insetos, play_g):
    if play_g.game_on:
        morcego.update()
        fundo.update()
        inimigos.update()
        insetos.update()


def draw_jogo(ai_s, morcego, fundo, inimigos, insetos, screen, play, play_g):
    fundo.draw(screen)
    morcego.draw(screen)
    inimigos.draw(screen)
    insetos.draw(screen)

    if not play_g.game_on:
        play.draw_button()