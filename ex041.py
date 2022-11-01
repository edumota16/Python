from datetime import date
nascimento = int(input('Que ano você nasceu: '))
idade = date.today().year - nascimento
print('O aluno tem {} anos.'.format(idade))
if idade < 9:
    print('Ele é da categoria: Mirim')
elif idade >= 9 and idade < 14:
    print('Ele é da categoria: Infantil')
elif 14 <= idade < 19:
    print('Ele é da categoria: Junior')
elif idade >= 19 and idade < 25:
    print('Ele é da categoria: Sênior')
else:
    print('Ele é da categoria: Master')


