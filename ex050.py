soma = 0
for i in range(1, 7):
    num = int(input('Digite o {}º número: '.format(i)))
    if num % 2 == 0:
        soma += num
print('A soma desses valores pares é: {}'.format(soma))