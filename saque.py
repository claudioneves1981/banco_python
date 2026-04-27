from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()
    
    def registrar(self, historico):
        historico.adicionar_transacao(self)