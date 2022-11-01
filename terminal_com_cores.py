print('Olá mundo!')
print('\033[36mOlá mundo!\033[m')
print('\033[31;43mOlá mundo!\033[m')
print('\033[4mOlá mundo!\033[m')
print('\033[7mOlá mundo!\033[m')
print('\033[1;37;46mOlá mundo!\033[m')

a = 5
b = 3
print('Os valores são \033[32m{}\033[m e \033[36m{}\033[m!'.format(a, b))
nome = 'Eduardo'
print('Legal te conhecer {}{}{}!'.format('\033[33m', nome, '\033[m'))

cores = {'vermelho':'\033[31m',
         'azul':'\033[34m',
         'cinza':'\033[37m',
         'limpa':'\033[m',
         'pretoebranco':'\033[7;30m'}
print('Prazer em te conhecer {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
print('Prazer em te conhecer {}{}{}!!!'.format(cores['cinza'], nome, cores['limpa']))
print('Prazer em te conhecer {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))
print('Prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))



