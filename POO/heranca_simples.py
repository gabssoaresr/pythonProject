class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')
    def falar(self):
        super().falar()
        print('Cliente')

class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super(ClienteVip, self).__init__(nome, idade)
        self.sobrenome = sobrenome
    def falar(self):
        print(f'{self.nome} {self.sobrenome} está falando')