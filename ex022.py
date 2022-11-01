nome = str(input('Escreva seu nome: ')).strip()
print('Nome com todas maiúsculas: ', nome.upper())
print('Nome com todas minúsculas: ', nome.lower())
print('Tem {} letras ao todo'.format(len(nome.strip())-nome.count(' ')))
dividido = nome.split()
print('O primeiro nome tem {} letras'.format(len(dividido[0])))


