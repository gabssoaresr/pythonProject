from banco import Banco
from conta import ContaCorrente, ContaPoupanca
from cliente import Cliente
banco = Banco()
cliente1 = Cliente('Gabriella', 25)
cliente2 = Cliente('Luiz', 33)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(254165, 1111, 0)
conta2 = ContaCorrente(254165, 1111, 0)
conta3 = ContaCorrente(254165, 5000, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_cliente(cliente2)
banco.inserir_cliente(cliente3)
if banco.autenticar(cliente1):
    cliente1.conta.depositar(1000)
    print()
    cliente1.conta.sacar(50)
else:
    print('Cliente não autenticado')
if banco.autenticar(cliente2):
    cliente2.conta.depositar(1000)
    print()
    cliente2.conta.sacar(50)
else:
    print('Cliente não autenticado')
if banco.autenticar(cliente3):
    cliente3.conta.depositar(1000)
    cliente3.conta.sacar(50)
else:
    print('Cliente não autenticado')
