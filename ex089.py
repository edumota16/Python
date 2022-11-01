lista = []
provisorio = []
nota = []
soma = n = 0
while True:
    provisorio.append(str(input('Nome: ')))
    provisorio.append(float(input('Nota 1: ')))
    provisorio.append(float(input('Nota 2: ')))
    lista.append(provisorio[:])
    for c in range(1, 3):
        soma += provisorio[c]
        media = soma / 2
    nota.append(media)
    provisorio.clear()
    soma = 0
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(30*'=-')
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print(20*'-')
for i in range(0, len(lista)):
    print(f'{i}')
for i, j in enumerate(lista):
    print(f'{j[0]}')
for i in nota:
    print(f'{i}')

while n != 999:
    n = str(input('Mostrar notas de qual aluno? (999 para interromper): '))
    for notas in enumerate(lista):
        print(f'As notas de {lista[n][0]} foram {lista[n][1], lista[n][2]}')
print('FINALIZANDO...')
print('<<<  Volte Sempre  >>>')