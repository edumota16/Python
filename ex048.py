print('Soma dos ímpares múltiplos de 3, entre 1 e 500: ')
soma = 0
contador = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma = soma + i
        contador += 1
print('A soma dos {} valores do intervalo é {}'.format(contador, soma))