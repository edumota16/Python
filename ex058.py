from random import randint
print('--------- JOGO DA ADVINHAÇÃO ---------')
n_pc = randint(0, 10)
n_user = int(input('Tente advinhar o número que pensei: '))
tentativas = 1
while n_user != n_pc:
    if n_user < n_pc:
        n_user = int(input('Errou! é um pouco mais, tente novamente: '))
    else:
        n_user = int(input('Errou! é um pouco menos, tente novamente: '))
    tentativas += 1
print('Parabéns! Eu pensei no {}. Você conseguiu em {} tentativas.'.format(n_pc, tentativas))
