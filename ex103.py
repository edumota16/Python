def ficha(nome='<desconhecido>', gols=0):
    print(30*'-')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome do jogador: ')).strip()
if len(nome) == 0:
    nome = '<desconhecido>'
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)