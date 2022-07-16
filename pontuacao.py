import pygame.font

class Pontuacao:

    def __init__(self, ai_s, screen, play_g):
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_s = ai_s
        self.play_g = play_g

        self.cor_texto = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_ponto()
    
    def prep_ponto(self):
        """Transforma a pontuação em uma imagem renderizada."""
        pontos_str = str(self.play_g.pontos)
        self.pontos_image = self.font.render(pontos_str, True, self.cor_texto)
        # Exibe a pontuação na parte superior direita da tela
        self.pontos_rect = self.pontos_image.get_rect()
        self.pontos_rect.right = self.screen_rect.right - 20
        self.pontos_rect.top = 20

    def exibe_pontos(self):
        self.screen.blit(self.pontos_image, self.pontos_rect)
