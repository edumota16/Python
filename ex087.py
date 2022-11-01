matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = coluna3 = coluna3b = maior =  0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
linha2 = max(matriz[1][0], matriz[1][1], matriz[1][2])
print(30*'=-')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(30*'=-')
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {linha2}')
print(30*'=-')
for l in range(0, 3):
    coluna3b += matriz[l][2]
print(f'Por outro método, a soma da terceira coluna é {coluna3b}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'Por outro método, o maior valor da segunda linha é {maior}')