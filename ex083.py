lista = []
expressao = str(input('Digite sua expressão: '))
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
for caractere in expressao:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')