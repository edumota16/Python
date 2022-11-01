def leiaInt(frase):
   ok = False
   valor = 0
   while True:
       n = str(input(frase))
       if n.isnumeric():
           valor = int(n)
           ok = True
       else:
           print('\033[31mErro digite um número válido.\033[m')
       if ok:
           break
   return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
