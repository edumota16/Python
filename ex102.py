def fatorial(n=1, show=False):
    """
    Programa que caucula o fatorial de um número lido pelo teclado.
    :param n: número para calcular o fatorial.
    :param show: parâmetro que mostra o processo (as multiplicações) do fatorial.
    :return: retorna o valor e/ou as multiplicações do fatorial dado.
    """
    f = 1
    for i in range(n, 0, -1):
        if show == True:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5))
print(fatorial(5, True))
print(fatorial(5, False))
help(fatorial)