def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro digite um número real válido.\033[m')
            continue
        else:
            return n

num = leiaInt('Digite um número natural: ')
num2 = leiaFloat('Agora digite um número real: ')
print(f'Você digitou {num} natural.')
print(f'Você digitou {num2} real.')