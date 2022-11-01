from time import sleep
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
operacao = ''
while operacao != '5':
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    operacao = str(input('Qual a sua opção? '))
    if operacao == '1':
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif operacao == '2':
        multiplicacao = n1 * n2
        print('O produto de {} x {} é {}'.format(n1, n2, multiplicacao))
    elif operacao == '3':
        if n1 > n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('Os números {} e {} são iguais'.format(n1, n2))
        else:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n2))
    elif operacao == '4':
        print('Novos números:')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif operacao != '1' and operacao != '2' and operacao != '3' and operacao != '4' and operacao != '5':
        print('Opção inválida, digite novamente!')
print('Fechando o programa...')
sleep(2)
print(23*'=')
print('Programa finalizado!')