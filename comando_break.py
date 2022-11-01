n = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
print('A soma vale {}'.format(soma))

soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')

nome = 'José'
idade = 33
salario = 1100.59
print(f'O {nome:^20} tem {idade} anos e recebe R$ {salario:.2f}')