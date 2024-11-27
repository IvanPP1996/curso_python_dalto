frutas = ['banana', 'manzana', 'ciruela', 'pera', 'naranja', 'granadilla', 'durazno']

for fruta in frutas:
    if fruta == 'granadilla':
        #Continue hace un salto y no muestra esa condición en este caso granadilla no la muestra
        continue
    ##print(f'Me voy a comer una {fruta}')
for fruta in frutas:
    if fruta == 'pera':
        #Break termina la condición en este caso pera es decir termina todo el código
        break
    ##print(f'Me voy a comer una {fruta}')

#Recorriendo una cadena de texto
cadena = 'Hola Dalto'

for letra in cadena:
    print(letra)

#Recorriendo lista de números
numeros = [2,5,8,10]
#for en una sola lista de código (duplicados los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
