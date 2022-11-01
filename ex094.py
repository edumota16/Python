pessoas = dict()
cadastro = list()
somaidade = media = 0
mulheres = list()
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['genero'] = str(input('Gênero (M/F): ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    somaidade += pessoas['idade']
    if pessoas['genero'] == 'F':
        mulheres.append(pessoas['nome'])
    resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Erro! Digite S ou N!')
        resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if resposta == 'N':
        break
media = somaidade / len(cadastro)
print(30*'=-')
print(f'- O grupo tem {len(cadastro)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print('- Lista das pessoas que estão acima da média: ')
for p in cadastro:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<<< ENCERRADO >>>')

