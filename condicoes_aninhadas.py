nome = str(input('Qual é o seu nome: '))
if nome == 'Eduardo':
    print('Nome bacana!')
elif nome == 'João' or nome == 'Jesus' or nome == 'Pedro':
    print('Seu nome é da bíblia')
elif nome in 'José Maria':
    print('Seu nome é popular no Brasil')
else:
    print('Seu nome é normal')
print('Legal te conhecer {}!'.format(nome))