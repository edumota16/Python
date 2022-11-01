velocidade = float(input('Qual a velocidade do carro: '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Tudo bem, velocidade normal')
else:
    print('Você foi multado por excesso de velocidade! O valor da multa é de R$ {:.2f}'.format(multa))