class Settings():
    """Uma classe para armazenar todas as configurações de El Morcegón"""
    def __init__(self):
        #Largura e altura da tela do jogo
        self.screen_w = 640
        self.screen_h = 480

        #incremendo da velocidade
        self.incre_speed = 1

        #incremendo do inseto e do inimigo
        self.incre_ini_ins = 1

        self.inicializar_config()

    def inicializar_config(self):
        #Velocidade do morcego, do inseto e do inimigo
        self.speed_bat = 3
        self.speed_inimigo = 4
        self.speed_inseto = 2
        self.speed_fundo = 1

        #Quantidade de inimigos e de insetos
        self.quant_inimigos = 2
        self.quant_insetos = 3

    def incremento_velociade(self):
        self.speed_bat += self.incre_speed
        self.speed_inimigo += self.incre_speed
        self.speed_inseto += self.incre_speed
        self.speed_fundo += self.incre_speed
    
    def incremento_ini_ins(self):
        self.quant_inimigos += self.incre_ini_ins
        self.quant_insetos += self.incre_ini_ins