import cnpj
cnpj_original = '00.453.469/0001-86'
cnpj_formatado = cnpj.remover_caracteres(cnpj_original)
novo_cnpj = cnpj_formatado[:-2]
cnpj_validado = cnpj.calcula_digito(novo_cnpj)
e_valido = cnpj.valida(cnpj_validado, cnpj_formatado)
print(e_valido)