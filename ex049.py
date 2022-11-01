n1 = int(input('Digite um número para saber a sua tabuada: '))
for i in range(1, 11):
    resultado = n1 * i
    print('{} x {:2} = {:2}'.format(n1, i, resultado))
