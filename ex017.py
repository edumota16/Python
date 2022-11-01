import math

n1 = float(input('Digite o 1 cateto: '))
n2 = float(input('Digite o 2 cateto: '))
hip = math.sqrt(pow(n1, 2) + pow(n2, 2))
hip2 = math.hypot(n1, n2)
print('A hipotenusa deste triângulo é {:.3f}'.format(hip))
print('A hipotenusa por hypot mede {:.3f}'.format(hip2))