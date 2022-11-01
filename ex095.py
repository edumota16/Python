jogador = {}
time = list()
gols = list()
n = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for i in range(1, partidas + 1):
        n = int(input(f'Quantos gols na partida {i}? '))
        gols.append(n)
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    time.append(jogador.copy())
    if resposta == 'N':
        break
print(30*'=-')
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":<15}')
print(50*'-')
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print(50*'-')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!, o índice de jogador {busca} não existe.')
    else:
        print(f'--  Levantamento do jogador: {time[busca]["nome"]}')
        for k, v in enumerate(time[busca]['gols']):
            print(f'    => Na partida {k+1}, fez {v} gols.')
    print(40*'-')
print('<<< Volte Sempre >>>')