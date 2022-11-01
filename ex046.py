from time import sleep
import emoji
print('Contagem regressiva...')
for i in range(10, 0 - 1, -1):
    sleep(1)
    print(i, end=' ')
print('\nfeliz ano novo!', emoji.emojize('Vamos beber :beer_mug:!', use_aliases=True))