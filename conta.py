from historico import Historico  # Add this import if Historico is defined in historico.py

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nSaldo insuficiente para saque.")
        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("\nValor inválido para saque.")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("\nValor inválido para depósito.")
        return False