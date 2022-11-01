escolha = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while escolha == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    escolha = str(input('Quer continuar [S/N]: ').strip().upper())[0]
media = soma/cont
print('Você digitou {} números e a média entre eles é {:.2f}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))