def linha():
    print(30*'-')

def soma(a, b):
    print(f'A soma é: {a + b}')

def contador(* numeros):
    print(f'Recebi os valores {numeros} e são {len(numeros)} números no total.')

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

def soma2(* numeros):
    soma = 0
    for num in numeros:
        soma += num
    print(f'Somando os valores {numeros} temos {soma}.')

linha()
print('Olá world')
linha()

soma(4, 5)
soma(2, 1)
soma(b=8, a=9)

contador(5, 7)
contador(0, 1, 0)
contador(4, 4, 7, 9, 5)

valores = [2, 7, 5, 1, 0, 9]
dobra(valores)
print(valores)

soma2(2, 3, 5)
soma2(1, 0)