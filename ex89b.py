ficha = list()
n = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(30*'=-')
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print(25*'-')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    n = int(input('Quer mostrar as notas de qual aluno? (999 para sair): '))
    if n == 999:
        print('FINALIZANDO...')
        break
    if n <= len(ficha)-1:
        print(f'As notas de {ficha[n][0]} foram {ficha[n][1]}')
print('<<< VOLTE SEMPRE >>>')
