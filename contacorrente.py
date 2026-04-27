import conta

class ContaCorrente(conta.Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def __str__(self):
        return f"ContaCorrente(titular={self.titular}, saldo={self.saldo}, limite={self.limite})"
