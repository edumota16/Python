print('Progressão Aritmérica\n', 10*'=-')
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
fim = razao * 10 + inicio
while fim > inicio:
    print('{} -> '.format(inicio), end='')
    inicio += razao
print('Fim')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')