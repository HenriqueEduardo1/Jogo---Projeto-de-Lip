class Record():
    def __init__(self):

        self.nome = 'record.txt'
        self.get_record_atual()

    def get_record_atual(self):
        with open(self.nome, 'r') as file_object:
            record = file_object.readlines()
        
        self.record_atual = int(record[0].strip())
    
    def set_record_atual(self, new_record):
        with open(self.nome, 'r+') as file_object:
            file_object.write(str(new_record)) 

