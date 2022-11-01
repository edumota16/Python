import leia_num
from time import sleep

def linha(tam = 42):
    return tam * '-'

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leia_num.leiaInt('\033[33mSua opção: \033[m')
    return opc