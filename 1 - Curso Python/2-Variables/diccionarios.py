#Creando diccionarios con dict
diccionario = dict(nombre="Lucas", apellido="Dalto")

#Creando diccionarios con fromkeys()
diccionario1 = dict.fromkeys("nombre","apellido")
diccionario1 = dict.fromkeys(["nombre","apellido","suscriptores"])
diccionario1 = dict.fromkeys(["nombre","apellido","suscriptores"], "No se")

##print(diccionario)
print(diccionario1)