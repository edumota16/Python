i = 1
while i < 10:
    print(i, end=' ')
    i += 1
print('Fim')

num = 1
while num != 0:
    num = int(input('Digite um valor: '))
print('Fim')

resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar [S/N]: ')).upper()
print('Fim')

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} ímpares.'.format(par, impar))
