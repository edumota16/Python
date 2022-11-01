from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    print(30*'-=')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if passo == 0:
        passo = 1
    if inicio < fim:
        fim = fim + 1
    if inicio > fim:
        passo *= -1
        fim = fim - 1
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(f'{i}', end=' ')
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print(30*'-=')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)