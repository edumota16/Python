distancia = int(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O valor da sua passagem é R$ {:.2f}'.format(passagem))