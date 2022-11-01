contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número (0 a 20): '))
    if n < 0 or n > 20:
        print('Número errado, tente novamente!')
    else:
        break
print(f'Você digitou o número {contagem[n]}')
