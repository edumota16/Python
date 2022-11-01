r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
if abs(r2 - r3) < r1 and r1 < r2 + r3:
    print('Pode-se formar um triângulo')
else:
    print('Não se pode formar um triângulo!')

