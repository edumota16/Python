maior = menor = 0
lista = list()
for i in range(0, 5):
    lista.append(int(input(f'Digite um número na posição {i}: ')))
for i, j in enumerate(lista):
    if i == 0:
        maior = menor = j
    else:
        if j > maior:
            maior = j
        elif j < menor:
            menor = j
print(30*'=-')
print(f'O maior valor foi {maior}, digitado na posição... ', end=' ')
for i, j in enumerate(lista): #Este FOR serve para percorrer cada valor/elemento do vetor
    if j == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor foi {menor}, digitado na posição... ', end=' ')
for i, j in enumerate(lista):
    if j == menor:
        print(f'{i}...', end=' ')
print('\n',30*'-=')
print(f'Por este meio, o maior valor foi {max(lista)}, digitado na posição...', end=' ')
for i, j in enumerate(lista):
    if j == max(lista):
        print(f'{i}...', end=' ')
print(f'\nPor este meio, o maior valor foi {min(lista)}, digitado na posição...', end=' ')
for i, j in enumerate(lista):
    if j == min(lista):
        print(f'{i}...', end=' ')
