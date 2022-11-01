n1 = int(input('Digite um número de 0 a 9999: '))
'''print('unidade: {}'.format(n1[3]))
print('dezena: {}'.format(n1[2]))
print('centena: {}'.format(n1[1]))
print('milhar: {}'.format(n1[0]))'''

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))