from random import randint
vitorias = 0
print(25*'-=', '\nJogo do Par ou Ímpar\n', 25*'-=')
while True:
    n_user = int(input('Qual número de dedos vai colocar: '))
    n_pc = randint(0, 10)
    soma = n_pc + n_user
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    if soma % 2 == 0 and escolha == 'P':
        print(f'O computador escolheu {n_pc} a soma deu {soma} é par e você ganhou!')
        vitorias += 1
    elif soma % 2 == 1 and escolha == 'I':
        print(f'O computador escolheu {n_pc} a soma deu {soma} é ímpar e você ganhou!')
        vitorias += 1
    else:
        break
print(f'O computador escolheu {n_pc} a soma deu {soma}.')
print(f'Você perdeu essa! mas conquistou {vitorias} vitórias seguidas.')