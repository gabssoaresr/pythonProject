from cnpj import cnpj
cnpj_original = '12.544.992/0001-05'
cnpj_formatado = cnpj.remover_caracteres(cnpj_original)
novo_cnpj = cnpj_formatado[:-2]
cnpj_validado = cnpj.calcula_digito(novo_cnpj)
e_valido = cnpj.valida(cnpj_validado, cnpj_formatado)
print(e_valido)