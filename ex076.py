listagem = (str(input('Informe um produto: ')), float(input('Preço R$: ')), str(input('Informe um produto: ')), float(input('Preço R$: ')),
            str(input('Informe um produto: ')), float(input('Preço R$: ')), str(input('Informe um produto: ')), float(input('Preço R$: ')))
print(37*'=')
print(f'{"Listas de compras":^37}')
print(37*'=')
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>5.2f}')
print(37*'=')
