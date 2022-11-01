lista = []
for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[len(lista)-1]: #este comando serve para pegar sempre o último elemento da lista
        lista.append(n)
        print('Adicionado ao final da fila...')
    else:
        posicao = 0
        while posicao <= len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Valor inserido na posição {posicao} da fila')
                break
            posicao += 1
print(30*'=-')
print(f'Os valores digitados em ordem foi: {lista}')