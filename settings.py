class Settings():
    """Uma classe para armazenar todas as configurações de El Morcegón"""
    def __init__(self):
        #Largura e altura da tela do jogo
        self.screen_w = 640
        self.screen_h = 480

        #Velocidade do morcego e do(os) inimigos
        self.speed_bat = 2
        self.speed_inimigo = 5

        #Quantidade de inimigos
        self.quant_inimigos = 5