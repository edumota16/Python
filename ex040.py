n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
if n1 <= 10 and n2 <=10 and n1 >=0 and n2 >=0:
    media = (n1 + n2)/2
    if media < 5:
        print('Sua média foi {:.2f}, você está reprovado!'.format(media))
    elif media >= 5 and media < 7:
        print('Sua média foi {:.2f}, você está de recuperação.'.format(media))
    else:
        print('Sua média foi {:.2f}, você foi aprovado com bom conceito!'.format(media))
else:
    print('Uma das notas é inválida, tente novamente.')