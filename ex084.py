galera = list()
nomepeso = list()
totpessoas = maior = menor = 0
while True:
   nomepeso.append(str(input('Nome: ')))
   nomepeso.append(float(input('Peso: ')))
   if len(galera) == 0:
      maior = menor = nomepeso[1]
   else:
      if nomepeso[1] > maior:
         maior = nomepeso[1]
      if nomepeso[1] < menor:
         menor = nomepeso[1]
   galera.append(nomepeso[:])
   totpessoas += 1
   nomepeso.clear()
   resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
   if resposta == 'N':
       break
print(30*'=-')
print(f'Ao todo, você cadastrou {totpessoas} pessoas.')
print(f'O maior peso foi de {maior} kg, de ', end='')
for p in galera:
   if p[1] == maior:
      print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor} kg, de ', end='')
for p in galera:
   if p[1] == menor:
      print(f'[{p[0]}] ', end='')