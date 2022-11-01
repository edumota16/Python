brasileirao = ('Corinthians', 'Varmengo', 'AtléticoMG', 'Palbeiras', 'Santos', 'SPFW', 'AtléticoPR', 'AtléticoGO',
               'Cuiabá', 'Juventude', 'Grêmio', 'Inter', 'Fluminense', 'RedBull', 'Ceará', 'Fortaleza',
               'Bahia', 'AméricaMG', 'Sport', 'Chapecoense', 'AtléticoGO')
print(f'Os cinco primeiros colocados são: {brasileirao[0:5]}')
print(f'Os quatro últimos são: {brasileirao[-4:]}')
print(f'Em ordem alfabética {sorted(brasileirao)}')
print(f'A Chapecoense está no {brasileirao.index("Chapecoense")}º lugar')