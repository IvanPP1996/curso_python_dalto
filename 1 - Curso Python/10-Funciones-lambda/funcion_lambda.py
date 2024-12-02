#Lambda se usa cuando solo se quiere mostrar una instrucción
multiplicar = lambda x: x*2
##print(multiplicar(5))

#Creando una funcion que devuelva si es par o no y los agregue a una nueva lista
numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))