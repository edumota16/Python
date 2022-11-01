pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))
if pessoa['media'] >= 7:
    pessoa['situacao'] = 'Aprovado'
else:
    pessoa['situacao'] = 'Reprovado'
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')