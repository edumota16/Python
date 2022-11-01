soma = 0
media = 0
tot20 = 0
maior = 0
velho = ''
for i in range(1, 5):
    print(5*'-', '{}ª PESSOA'.format(i), 5*'-')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero [M/F]: ')).strip()
    soma = soma + idade
    if genero in 'Mm':
        if i == 1:
            maior = idade
            velho = nome
        else:
            if idade > maior:
                maior = idade
                velho = nome
    if genero in 'Ff':
        if idade <= 20:
            tot20 += 1
media = float(soma/4)
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot20))