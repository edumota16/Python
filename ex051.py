print('Progressão Aritmética')
inicio = int(input('Digite o início da PA: '))
razao = int(input('Digite a razão: '))
fim = inicio + 10 * razao
for i in range(0, 10):
    for j in range(inicio, fim, razao):
        print(j, end=' -> ')
        inicio += razao
print('Fim')