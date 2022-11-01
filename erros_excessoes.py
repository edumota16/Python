try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos um problema com o tipo de dados de entrada.')
except ZeroDivisionError:
    print('Não se pode dividir por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
#except Exception as erro:
#    print(f'Tivemos um problema chamado {erro}.')
else:
    print(f'O resultado deu {r:.2f}.')
finally:
    print('Volte sempre muito obrigado.')