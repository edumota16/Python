def escreva(msg):
    tamtio = len(msg) + 4
    print(tamtio * '~')
    print(f'  {msg}')
    print(tamtio * '~')

escreva('Olá Mundo!')
escreva('Curso de Python no YouTube')
escreva('CeV')