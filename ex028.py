from random import randint
from time import sleep

n_pc = randint(0, 5)
n_user = int(input('Tente advinhar o número que pensei (0 a 5): '))
print('Processando...')
sleep(2)
if n_pc == n_user:
    print('Você acertou o número! {} {}'.format(n_pc, n_user))
else:
    print('Você errou eu pensei no número {}'.format(n_pc))
