class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super(Cliente, self).__init__(nome, idade)
        self.conta = None
    def inserir_conta(self, conta):
        self.conta = conta




