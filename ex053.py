frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
juntas = ''.join(palavras)
inverso2 = juntas[::-1] #Letras inversas de outra forma
inverso = ''
for i in range(len(juntas)-1, -1, -1):
    inverso = inverso + juntas[i]
print('O inverso de {} é {}'.format(juntas, inverso))
if juntas == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
print('O inverso de outra forma {}'.format(inverso2))