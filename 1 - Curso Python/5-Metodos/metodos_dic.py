diccionario = {
    "nombre" : "Lucas",
    "apellido" : "Dalto",
    "subs" : 1000000
}

#Método que permite ver las llaves del diccionario y las devuleve en una lista
##print(diccionario.keys())

#Método para ver el valor del key con el nombre que le pongamos
##print(diccionario.get("nombre"))


#Método para eliminar la llave y el valor de esta de un diccionario
diccionario.pop("subs")
##print(diccionario)

#Método para iterar un diccionario es decir separar cada item con su llave y valor ("nombre", "Lucas"), ("apellido", "Dalto")
##print(diccionario.items())

#Método para eliminar todo el dccionario
diccionario.clear()
print(diccionario)