class Settings():
    """Uma classe para armazenar todas as configurações de El Morcegón"""
    def __init__(self):
        #Largura e altura da tela do jogo
        self.screen_w = 640
        self.screen_h = 480

        #Velocidade do morcego, do inseto e do inimigo
        self.speed_bat = 2
        self.speed_inimigo = 4
        self.speed_inseto = 2
        self.speed_fundo = 1

        #Quantidade de inimigos e de insetos
        self.quant_inimigos = 2
        self.quant_insetos = 3

        #Pontuação do jogador
        self.pontos = 0

        self.game_on = False