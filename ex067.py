while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(35*'-')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print(35 * '-')
print(35 * '-')
print('Programa tabuada finalizado!')