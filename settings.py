class Settings():
    """Uma classe para armazenar todas as configurações de El Morcegón"""
    def __init__(self):
        #Largura e altura da tela do jogo
        self.screen_w = 640
        self.screen_h = 480

        #Velocidade do morcego, do inseto e do inimigo
        self.speed_bat = 2
        self.speed_inimigo = 5
        self.speed_inseto = 3

        #Quantidade de inimigos e de insetos
        self.quant_inimigos = 3
        self.quant_insetos = 4