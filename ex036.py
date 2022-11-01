casa = float(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos você vai pagar? '))
salario = float(input('Qual é o seu salário? '))
prestacao = casa / (anos * 12)
if prestacao > salario * 0.3:
    print('Você não possui renda, NEGADO!')
else:
    print('A casa custa R${:.2f}, com R${:.2f} de salário, a parcela fica em R${:.2f}'.format(casa, salario, prestacao))