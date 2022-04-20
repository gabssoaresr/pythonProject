class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333, 4444]
        self.clientes = []
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            print('cliente')
            return False
        elif cliente.conta not in self.contas:
            print('contas')
            return False
        elif cliente.conta.agencia not in self.agencias:
            print('agencias ')
            return False
        print()
        return True


