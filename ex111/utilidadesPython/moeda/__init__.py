def metade(n=0, format=False):
    resp = n/2
    if format:
        return moeda(resp)
    else:
        return resp

def dobro(n=0, format=False):
    resp = 2 * n
    if format:
        return moeda(resp)
    else:
        return resp

def aumentar(n, porc, format=False):
    resp =  n * (1 + porc / 100)
    if format:
        return moeda(resp)
    else:
        return resp

def diminuir(n, porc, format=False):
    resp = n - (n * porc/100)
    if format:
        return moeda(resp)
    else:
        return resp

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(n=0, aumento=0, diminuicao=0):
    print(30*'-')
    print('RESUMO DO VALOR'.center(30))
    print(30*'-')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}')
    print(f'{diminuicao}% de redução: \t{diminuir(n, diminuicao, True)}')
    print(30*'-')