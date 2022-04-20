from abc import ABC, abstractmethod
class Conta(ABC):
    def __init__(self, conta, agencia, saldo):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo


    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo  precisa ser numérico")
        self._saldo = valor
        self.detalhes()

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f"Conta: {self.conta}")
        print(f"Agência: {self.agencia}")
        print(f"Saldo: {self.saldo}")
    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo, limite=500):
        super(ContaCorrente, self).__init__(conta, agencia, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo = self.saldo - valor

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo = self.saldo - valor

