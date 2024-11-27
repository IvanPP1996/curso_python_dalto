##Todo lo aplicado aqui tambien funciona con tuplas

animales = ["Gato", "Perro", "Loro", "Cocodrilo"]

#Recorriendo lista animales
##for animal in animales:
    ##print(f'Ahora la variable animal es: {animal}')

#Recorriendo lista números
numeros = [52, 16, 14, 72]
##for numero in numeros:
    ##print(numero * 10)

#Recorriendo dos listas con for NOTA se puede iterar con mas de dos listas ys e iterar intercalados
##for numero, animal in zip(numeros, animales):
    ##print(f'Recorriendo lista 1: {animal}')
    ##print(f'Recorriendo lista 2: {numero}')

#Iterando de manera simple y basica desede el 5 al 10 Nota: Este método se basa mas por los indices
#for (nombre de la condicion) in range (parametro donde inicia, parametro donde termina, aumentador)
##for num in range (5, 11, 1):
    ##print(num)
    
#otra forma de escribir este parametro: Se omite el tercer parametro
##for num in range (5,11):
    ##print(num)
    
#otra forma de escribir este parametro: Se omite el primer y tercer parametro
##for num in range (21):
    ##print(num)

#Forma de recorrer una lista o tupla con sus indices si se requiere
for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    ##print(f'El inidce es {indice} y el número de la lista es {valor}')

#Usando el else en un for
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('El bucle termino')
