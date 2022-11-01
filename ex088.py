from random import randint
from time import sleep
print(30*'-')
print('       JOGA NA MEGASENA       ')
print(30*'-')
jogo = [[0], [0], [0], [0], [0], [0]]
n = int(input('Quantos jogos você quer que eu sorteie: '))
print(3*'-=', f'SORTEANDO {n} JOGOS', 3*'-=')
for i in range(1, n+1):
    print(f'Jogo {i}: ', end='')
    for p in range(0, 6):
        jogo[p] = randint(1, 60)
    jogo.sort()
    print(jogo)
    sleep(1)
print(3*'-=', ' < BOA SORTE! > ', 3*'-=')