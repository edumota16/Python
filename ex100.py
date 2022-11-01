from random import randint
from time import sleep
numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        sleep(0.3)
        n = randint(0, 10)
        print(n, end=' ')
        numeros.append(n)
    print('PRONTO!')

def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros} temos {soma}.')

sorteia()
somaPar(numeros)