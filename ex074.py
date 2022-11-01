maior = menor = 0
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {tupla}')
tupla = sorted(tupla)
print(f'O maior número foi {tupla[4]}')
print(f'O menor número foi {tupla[0]}')
print(f'O maior valor sorteado por função MAX foi: {max(tupla)}')
print(f'O maior valor sorteado por função MIN foi: {min(tupla)}')


