from time import sleep
def maior(* numeros):
    print(30*'-=')
    print('Analisando os valores passados...')
    if len(numeros) == 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        for n in numeros:
            sleep(0.3)
            print(n, end=' ')
        print(f'Foram informados {len(numeros)} valores ao todo.')
        print(f'O maior valor informado foi {max(numeros)}.')

maior(2, 9, 4, 5, 7, 1)
maior(2, 7, 0)
maior(1, 2)
maior(6)
maior()