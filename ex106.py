from time import sleep
cores = ('\033[m',          # 0 - sem cor
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[7;30m'       # 6 - branco
         )

def ajuda(comando):
    print(cores[5])
    help(comando)
    print(cores[0])
    sleep(2)

def titulo(msg, cor = 0):
    tamtio = len(msg) + 4
    print(cores[cor], end='')
    print(tamtio * '~')
    print(f'  {msg}')
    print(tamtio * '~')
    print(cores[0])

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou comando: '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO', 1)
        break
    else:
        titulo(f'Acessando o manual do comando {comando}', 4)
        sleep(2)
        ajuda(comando)