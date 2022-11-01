def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional.'
    else:
        return f'Com {idade} anos: Voto obrigatório.'

print(30*'-')
ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))