num = [2, 5, 9, 1]
print(num)
num[1] = 80
print(num)
num.append(50)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2, 77)
print(num)
num.pop()
print(num)
num.pop(1)
print(num)
num.insert(1, 2)
print(num)
num.remove(2)
print(num)
num.insert(3, 87)
print(num)
if 87 in num:
    num.remove(87)
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for i in valores:
    print(f'{i}...')
for i, j in enumerate(valores):
    print(f'na posição {i}, encontrei o valor {j}')

valores = list()
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for i, j in enumerate(valores):
    print(f'Na posição {i+1}, foi digitado o valor {j}')

a = [2, 7, 9, 7]
b = a[:] #Cria uma cópia de a, e não uma ligação entre as listas
b[2] = 55
print(a)
print(b)