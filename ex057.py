genero = ''
while genero != 'M' and genero != 'F':
    genero = str(input('Digite o seu gênero [M/F]: ')).strip().upper()[0]
    if genero == 'M' or genero == 'F':
        print('Ok! Você é do gênero: {}'.format(genero))
    else:
        print('Digite novamente! Campo inválido!')

genero = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados errados, digite novamente: ')).strip().upper()[0]
print('Gênero {} registrado com sucesso!'.format(genero))