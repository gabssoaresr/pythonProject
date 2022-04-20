class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

b1 = BaseDeDados()
b1.inserir_cliente(1, 'Gabriella')
b1.inserir_cliente(2, 'vini')
b1.inserir_cliente(3, 'rodrigo')
b1.inserir_cliente(4, 'jojo')
b1.apaga_cliente(2)
b1.lista_clientes()
print(b1.__dados)
