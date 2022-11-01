print(30*'=')
print('{:^30}'.format('BANCO DO POVO'))
print(30*'=')
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 100
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula:.2f}')
        if cedula == 100:
            cedula = 50
            totcedula = 0
        elif cedula == 50:
            cedula = 20
            totcedula = 0
        elif cedula == 20:
            cedula = 10
            totcedula = 0
        elif cedula == 10:
            cedula = 5
            totcedula = 0
        elif cedula == 5:
            cedula = 1
            totcedula = 0
        elif total == 0:
            break
print(30*'=')
print('Obrigado por utilizar o BANCO DO POVO')
