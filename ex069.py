maiores = tothomens = ninfetas = 0
while True:
    print(30*'-','\nCADASTRE UMA PESSOA\n',30*'-')
    idade = int(input('Idade: '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Gênero: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if genero == 'M':
        tothomens += 1
    if genero == 'F' and idade < 20:
        ninfetas += 1
    escolha = ' '
    print(30*'-')
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(30*'-','\nPrograma finalizado!\n',30*'-')
print(f'No total tivemos {maiores} pessoas maiores de idade.')
print(f'No total foram cadastrados {tothomens} homens.')
print(f'E no total tivemos {ninfetas} mulheres menores que 20 anos.')