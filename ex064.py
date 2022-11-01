n = 0
soma = 0
total = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        total += 1
print('Você digitou {} números e a soma entre eles é {}'.format(total, soma))

soma = total = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    total += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(total, soma))
