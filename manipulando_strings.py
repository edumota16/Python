frase = '  Curso em Video Python  '
print(len(frase))
print(len(frase.strip()))
print(frase)
print(frase[3])
print(frase[:15])
print(frase[1:15])
print(frase[:21:3])
print("""Este curso é para aprender os conceitos básicos de python, como neste caso em imprimir um texto grande, usando três aspas""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print('José' in frase)
frase = frase.replace('Curso', 'Aula')
print(frase)
print(frase.find('Aula'))
print(frase.find('Video'))
print(frase.split())
dividido = frase.split()
print(dividido[1])
print(dividido[2][2])