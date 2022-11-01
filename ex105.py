def notas(*num, situacao=False):
    """
    Programa que adiciona várias notas e mostra alguns parâmetros através de um dicionário.
    :param num: notas a serem lançadas, pode ser uma ou várias.
    :param situacao: parâmetro opcional que mostra a situação do aluno baseado pela sua média.
    :return: Retorna o dicionário preenchido.
    """
    tabNotas = dict()
    tabNotas['total'] = len(num)
    tabNotas['maior'] = max(num)
    tabNotas['menor'] = min(num)
    tabNotas['média'] = sum(num) / len(num)
    if situacao:
        if tabNotas['média'] < 5:
            tabNotas['situacão'] = 'ruim'
        elif 5 <= tabNotas['média'] < 7:
            tabNotas['situacão'] = 'regular'
        else:
            tabNotas['situacão'] = 'boa'
    return tabNotas

resp = notas(5.5, 2.5, 1.5, 9.857, 9, situacao=True)
print(resp)
help(notas)