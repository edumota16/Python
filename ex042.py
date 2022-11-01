r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
if abs(r2 - r3) < r1 and r1 < r2 + r3:
    print('Pode-se formar um triângulo')
    if r1 == r2 == r3:
        print('Este triângulo é equilátero.')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1 or r2 == r1 and r2 != r3:
        print('Este triângulo é isósceles.')
    else:
        print('Este triangulo é escaleno')
else:
    print('Não se pode formar um triângulo!')