nome = str(input('Qual o seu nome: '))
if nome == 'Eduardo':
    print('Bonito nome!')
else:
    print('Seu nome é normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média é {:.2f}'.format(m))
if m >= 6:
    print('Média boa!')
else:
    print('Média ruim!')
print('Parabéns' if m >= 6 else 'Estude mais!') #if simplificado
