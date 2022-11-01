jogador = {}
gols = list()
somagols = partidas = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(1, partidas + 1):
    n = int(input(f'Quantos gols na partida {i}? '))
    gols.append(n)
    somagols += n
jogador['gols'] = gols.copy()
jogador['total'] = somagols #Pode-se usar também o soma = sum(gols)
print(30*'=-')
print(jogador)
print(30*'=-')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(30*'=-')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(1, partidas + 1):
    print(f'    => Na partida {i}, fez {gols[i-1]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
