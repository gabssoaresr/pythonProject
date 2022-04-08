import re

def remover_caracteres(cnpj):
    return  re.sub(r'[^0-9]', '', cnpj)

def calcula_digito(cnpj_formatado):
    total = 0
    reverso = 5
    for index in range(24):
        total += int(cnpj_formatado[index]) * reverso
        #print("cnpj :",  cnpj_formatado[index])
        #print("reverso :", reverso)
        reverso -= 1
        if reverso < 2:
            reverso = 9

        if index > 10:
            reverso = 6
            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0
            total = 0
            cnpj_formatado += str(digito)

            total += int(cnpj_formatado[index]) * reverso
            #print("cnpj :", cnpj_formatado[index])
            #print("reverso :", reverso)
            reverso -= 1
            if reverso < 2:
                reverso = 9

            if index > 11:
                break
    return cnpj_formatado
def valida(cnpj_validado, cnpj_formatado):
    if cnpj_validado == cnpj_formatado:
        print("CNPJ Válido")
    else:
        print("CNPJ Inválido")
    return cnpj_validado





