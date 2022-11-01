lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[0:5])
print(lanche[2:])
print(lanche[-3:])
#Tuplas são imutáveis
for i in lanche:
    print(f'Eu vou comer {i}')
print('Estou satisfeito!')

print(len(lanche))
for i in range(0, len(lanche)):
    print(lanche[i])

for pos, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posição {pos}')

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]} na posição {i}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(c.count(5))
print(c.index(8))
print(c.index(5, 2))

#Tuplas podem receber tipos primitivos diferentes
pessoa = ('Eduardo', 33, 'M', 73.5)
print(pessoa)