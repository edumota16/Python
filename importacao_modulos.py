import math
from math import sqrt, floor
import random
import emoji

n1 = int(input('Digite um número: '))
raiz = sqrt(n1)
print('Sua raiz é {:.2f}'.format(math.sqrt(n1)))
print('A raiz arredondada para baixo é {}'.format(floor(raiz)))

n2 = random.random()
print(n2)

n3 = random.randint(1, 10)
print(n3)

print(emoji.emojize(':alien:', use_aliases=True))
print(emoji.emojize('Vamos beber :beer_mug:', use_aliases=True))
