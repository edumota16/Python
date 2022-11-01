pessoas = {'nome': 'Eduardo','idade':33, 'genero': 'M'} #dicionário se declara por chaves
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
del pessoas['genero']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 73.7
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

brasil = []
estado1 = {'uf':'São Paulo', 'sigla':'SP'}
estado2 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['sigla'])
print()

brasil = list()
estado = {}
for i in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil: #FOR para percorrer primeiro as listas e depois os valores no dicionário
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()