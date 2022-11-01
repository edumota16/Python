dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos quilômetros rodados: '))
valor = float(dias * 60 + km * 0.15)
print('Então o toptal a pagar é R$ {:.2f}'.format(valor))