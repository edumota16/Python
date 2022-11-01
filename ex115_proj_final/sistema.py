from ex115_proj_final.biblioteca.interface import *
from ex115_proj_final.biblioteca.arquivo import *

nome_arquivo = 'arquivo.txt'
if arq_existe(nome_arquivo):
    print(f'{nome_arquivo} encontrado com sucesso!')
else:
    criar_arquivo(nome_arquivo)

cabecalho('\033[35mSISTEMA DE CADASTRO v1.0\033[m')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Mostrando lista de pessoas')
        ler_arquivo(nome_arquivo)
    elif resposta == 2:
        cabecalho('Cadastrando nova pessoa')
        nome = str(input('Nome: '))
        idade = leia_num.leiaInt('Idade: ')
        adicionar_pessoa(nome_arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[031mErro, digite uma opção válida.\033[m')
    sleep(2)