print(30*'=')
print('{:^30}'.format('LOJÃO BARATÃO'))
print(30*'=')
fatura = 0
acima1000 = 0
cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    fatura += preco
    cont += 1
    if preco > 1000:
        acima1000 += 1
    if cont == 1:
        maisbarato = produto
        menor = preco
    else:
        if preco < menor:
            maisbarato = produto
            menor = preco
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {fatura:.2f}')
print(f'Temos {acima1000} produtos acima de R$ 1000.00')
print(f'O produto mais barato foi {maisbarato} que custou R$ {menor:.2f}')