from math import factorial
n1 = int(input('Digite um número para saber o seu fatorial: '))
print('O fatorial desse número é: {}'.format(factorial(n1)))

i = n1
fatorial = 1
print('{}!='.format(n1), end='')
while i > 0:
    print('{}'.format(i), end='')
    if i != 1:
        print('x', end='')
    else:
        print('=', end='')
    fatorial = fatorial * i
    i -= 1
print(fatorial)
print('O fatorial de {} é {}'.format(n1, fatorial))

fatorial = 1
for j in range(n1, 0, -1):
    fatorial *= j
print('O fatorial, com o FOR, de {} é {}'.format(n1, fatorial))