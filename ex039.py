from datetime import date
genero = str(input('Gênero (M / F): ')).upper()
if genero == 'M':
    nascimento = int(input('Ano de nascimento: '))
    idade = date.today().year - nascimento
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, date.today().year))
    if idade < 18:
        print('Ainda faltam {} anos para o seu alistamento'.format(18-idade))
        print('Seu alistamento será em {}'.format(date.today().year + 18-idade))
    elif idade == 18:
        print('Seu alistamento é esse ano!')
    else:
        print('Seu alistamento está atrasado {} anos'.format(idade - 18))
        print('Seu alistamento era em {}'.format(date.today().year - (idade - 18)))
elif genero == "F":
    print('Você é mulher, não precisa se alistar')
else:
    print('Opção inválida, tente novamente.')



