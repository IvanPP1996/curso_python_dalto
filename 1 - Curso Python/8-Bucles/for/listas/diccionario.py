diccionario = {
    'nombre' : 'Lucas',
    'apellido' : 'Dalto',
    'suscriptores' : 1000000,
}

##print(diccionario)

#Recorriendo diccionario pero solo sus claves (Key)
for valor in diccionario:
    print(valor)

#Recorriendo diccionario pero ahora con su clave y valor (key: value) nos devuleve una tupla por cada clave y valor
for valor in diccionario.items():
    ##print(valor)
    #Otra forma de recorrer un diccionario
    key = valor[0]
    value = valor[1]
    print(f'la clave es: "{key}" y el valor es: "{value}"')