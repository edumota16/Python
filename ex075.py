tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nehuma posição')
print(f'Os valores pares digitados foram ', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')