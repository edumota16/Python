print(5*'=', 'Verificador de números primos', 5*'=')
num = int(input('Digite um número: '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[31m{}\033[m '.format(i), end='')
        cont +=1
    else:
        print('{} '.format(i), end='')
if cont <= 2:
    print('\nO número digitado é primo!')
else:
    print('\nO número digitado \033[31m NÃO \033[m é primo!, porque ele foi dividido {} vezes.'.format(cont))