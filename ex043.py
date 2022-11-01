peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (cm) '))/100
imc = peso / pow(altura, 2) # ou altura ** 2
print('Seu IMC é {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida!')