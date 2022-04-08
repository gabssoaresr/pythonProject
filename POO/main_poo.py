from associacao import Escritor, Caneta, Maquina
from agregacao import CarrinhoDeCompras, Produto
from composicao import Cliente
from heranca_simples import Cliente, Aluno, ClienteVip

cliente1 = Cliente('Gabriella', 25)
cliente2 = ClienteVip('Gabriella', 25, 'Soares')
aluno1 = Aluno('Rodrigo', 19)
cliente1.falar()
cliente1.comprar()
cliente2.falar()
cliente2.comprar()













# cliente1 = Cliente('Gabriella', 25)
# cliente1.insere_endereco('Brasilia', 'DF')
# cliente1.insere_endereco('Florianopolis', 'SC')
# print(cliente1.nome)
# cliente1.lista_enderecos()
# print()
#
# cliente2 = Cliente('Chloe', 5)
# cliente2.insere_endereco('São Paulo', 'SP')
# print(cliente2.nome)
# cliente2.lista_enderecos()
# print()
#
# cliente3 = Cliente('Rubens', 33)
# cliente3.insere_endereco('Belo Horizonte', 'MG')
# print(cliente3.nome)
# cliente3.lista_enderecos()



# carrinho = CarrinhoDeCompras()
# p1 = Produto('Camiseta', 50)
# p2 = Produto('Iphone', 10000)
# p3 = Produto('Caneca', 15)
# carrinho.inserir_produto(p1)
# carrinho.inserir_produto(p2)
# carrinho.inserir_produto(p3)
# carrinho.lista_produtos()
# print(carrinho.soma_total())


# escritor = Escritor('Gabriella')
# caneta = Caneta('Bic')
# maquina = Maquina()
# escritor.ferramenta = caneta
# escritor.ferramenta.escrever()