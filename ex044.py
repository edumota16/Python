print(11*'=', 'LOJAS DO VAREJO', 11*'=')
compras = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual é a opção? '))
if forma == 1:
    print('Sua compra de R$ {:.2f}, custará R${:.2f}'.format(compras, compras - (compras*0.10)))
elif forma == 2:
    print('Sua compra de R$ {:.2f}, custará R${:.2f}'.format(compras, compras - (compras*0.05)))
elif forma == 3:
    print('Sua compra ficará com o valor normal em 2 parcelas de R$ {:.2f}'.format(compras/2))
elif forma == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra de R$ {:.2f}, custará R${:.2f} em {} parcelas de {:.2f}'.format(compras, compras + (compras*0.20), parcelas, (compras + (compras*0.20))/parcelas))
else:
    print('Opção inválida, tente novamente.')