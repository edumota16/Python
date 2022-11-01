def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um valor inválido.\033[m')
        else:
            valido = True
            return float(entrada)

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