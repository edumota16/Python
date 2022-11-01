for c in range(0, 10):
    print('Olá, mundo')
print('Fim')
for c in range(5, 10):
    print(c)
for c in range(10, 1, -1):
    print(c)
for c in range(0, 7, 2):
    print(c)

n1 = int(input('Digite um número para contar: '))
for c in range(0, n1+1):
    print(c)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim + 1, passo):
    print(c)

soma = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    soma = soma + n
print('A soma desses valores é {}'.format(soma))