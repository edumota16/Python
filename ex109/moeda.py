def metade(n):
    resp = n/2
    return resp

def dobro(n):
    resp = 2 * n
    return resp

def aumentar(n, porc):
    resp =  n * (1 + porc / 100)
    return resp

def diminuir(n, porc):
    resp = n - (n * porc/100)
    return resp

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')