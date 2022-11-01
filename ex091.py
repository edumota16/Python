from random import randint
from time import sleep
from operator import itemgetter
apostadores = {
    'jogador1':randint(1, 6),
    'jogador2':randint(1, 6),
    'jogador3':randint(1, 6),
    'jogador4':randint(1, 6)}
ranking = {}
print('---------- Valores sorteados ----------')
for k, v in apostadores.items():
    sleep(1)
    print(f'{k} tirou {v} no lançamento do dado.')
print(30*'=-')
print('-------- Ranking de Vencedores --------')
ranking = sorted(apostadores.items(), key=itemgetter(1), reverse=True) #método para ordenar dicionários por valores
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')