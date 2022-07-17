class PlayGame:
    def __init__(self, ai_s, record):
        
        self.ai_s = ai_s
        self.record = record
        self.reset_pontos()

        #estado do jogo
        self.game_on = False

        #pontuação máxima
        self.max_pontuacao = self.record.record_atual
    
    def reset_pontos(self):
        #Pontuação do jogador
        self.pontos = 0