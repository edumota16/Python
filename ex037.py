numero = int(input('Digite um número inteiro: '))
print('[1] converter para Binário')
print('[2] converter para Octal')
print('[3] converter para Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida')