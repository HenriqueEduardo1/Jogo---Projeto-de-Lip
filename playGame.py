class PlayGame:
    def __init__(self, ai_s):
        
        self.ai_s = ai_s
        self.reset_pontos()

        #estado do jogo
        self.game_on = False
    
    def reset_pontos(self):
        #Pontuação do jogador
        self.pontos = 0