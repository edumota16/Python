preco = float(input('Preço do produto: '))
salario = float(input('Salário do funcionário: '))
desconto = preco * 0.95
aumento = salario * 1.15
print('O preço com 5% de desconto é {} e o salário com 15% de aumento é {:.2f}'.format(desconto, aumento))