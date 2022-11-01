def fatorial(n=1):
    """
    Este programa retorna o fatorial de um número lido pelo teclado.
    :param n: Número solicitado pelo teclado.
    :return: Valor do fatorial retornado.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número para o seu fatorial: '))
print(fatorial(n))

r1 = fatorial(4)
r2 = fatorial(10)
r3 = fatorial(0)
r4 = fatorial()
print(f'Os resultados foram {r1}, {r2}, {r3}, e {r4}.')

num = int(input('Digite um número para saber se é par: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
