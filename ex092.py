from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de Nascimento: '))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
cadastro['idade'] = date.today().year - cadastro['idade']
if cadastro['CTPS'] == 0:
    print(cadastro)
else:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário R$: '))
    cadastro['aposentadoria'] = 35 - (date.today().year - cadastro['contratacao']) + cadastro['idade']
    print(cadastro)
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')