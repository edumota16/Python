import urllib
import urllib.request

site = str(input('Digite um site para ver se ele está acessível: '))

try:
    urllib.request.urlopen('https://' + site)
except:
    print('\033[31mO site não está acessivel.\033[m')
else:
    print('O site está acessível')
