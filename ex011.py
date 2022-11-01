altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))
area = altura * largura
tinta = area / 2
print('Esta parede tem {} metros de área e vai precisar de {:.2f} litros de tinta'.format(area, tinta))