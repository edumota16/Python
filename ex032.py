from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano  % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('Este ano {} não é bissexto!'.format(ano))