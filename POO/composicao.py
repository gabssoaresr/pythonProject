class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    def lista_enderecos(self):
        if not self.enderecos:
            print('Não tem nenhum endereço na lista')
        else:
            for endereco in self.enderecos:
                print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
