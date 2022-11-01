salario = float(input('Qual é o salário do funcionário: '))
if salario <= 1250.00:
    salario = salario * 1.15
    print('Seu novo salário é R$ {:.2f} com 15% de aumento'.format(salario))
else:
    salario = salario * 1.10
    print('Seu novo salário é R$ {:.2f} com 10% de aumento'.format(salario))