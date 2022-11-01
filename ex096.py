def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area:.2f}m².')

print('Controle de terrenos')
print(15*'-')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)