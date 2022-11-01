matrizA = [[], [], []]
matrizB = [[], [], []]
matrizC = [[], [], []]
for i in range(0,9):
    n = int(input(f'Digite o {i} valor: '))
    if i <= 2:
        matrizA[i].append(n)
    elif 2 < i <= 5:
        matrizB[i-3].append(n)
    elif 5 < i <= 8:
        matrizC[i-6].append(n)
print(matrizA)
print(matrizB)
print(matrizC)

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print(30*'=-')
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()