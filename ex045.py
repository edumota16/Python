from random import choice
from time import sleep
print(15*'=', 'JOKENPÔ', 15*'=')
lista = ['pedra','papel','tesoura']
pc = choice(lista)
print('''[ 1 ] para pedra
[ 2 ] para papel
[ 3 ] para tesoura''')
escolha = int(input('Escolha: '))
print('Jokenpô....')
sleep(2)
if escolha == 1:
    jogador = 'pedra'
    if pc == 'pedra':
        print('{} x {} - Empate!'.format(jogador, pc))
    elif pc == 'papel':
        print('{} x {} - PC venceu!'.format(jogador, pc))
    else:
        print('{} x {} - Você venceu!'.format(jogador, pc))
elif escolha == 2:
    jogador = 'papel'
    if pc == 'pedra':
        print('{} x {} - Você venceu!'.format(jogador, pc))
    elif pc == 'papel':
        print('{} x {} - Empate!'.format(jogador, pc))
    else:
        print('{} x {} - PC venceu!'.format(jogador, pc))
elif escolha == 3:
    jogador = 'tesoura'
    if pc == 'pedra':
        print('{} x {} - PC venceu!'.format(jogador, pc))
    elif pc == 'papel':
        print('{} x {} - Você venceu!'.format(jogador, pc))
    else:
        print('{} x {} - Empate!'.format(jogador, pc))
else:
    print('Escolha inválida, tente novamente.')

