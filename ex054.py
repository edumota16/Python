from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Digite o ano de nasc da {}ª pessoa: '.format(i)))
    if atual - nasc >= 18:
        maior += 1
    else:
        menor += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))