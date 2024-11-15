cadena1 = "hola a, todos"
cadena2 = "Bienvenido al mundo de la programación"
cadena3 = "58685965869"
cadena4 = "fghrrr"

#Funcion para saber lo que se puede hacer con la cadena de texto seleccionada
##print(dir(cadena1))
##print(dir(4))

#Método para convertir todo a mayuscula
##print(cadena1.upper())

#Método para convertir todo a minuscula
##print(cadena1.lower())

#Método para convertir solamente la primera letra en mayuscula
##print(cadena1.capitalize())

#Método para buscar una cadena en una frase y lo devuelve en la posición que este y si no esta devuelve (-1)
##print(cadena1.find("hola"))
##print(cadena1.find("a"))
##print(cadena1.find("f"))

#Método index() cumple las mismas condiciones que find con expcción que devuleve un error si no lo encunetra
##print(cadena1.index("a"))
##print(cadena1.index("f"))

#Método para saber si es númerico devuleve un boolean
##print(cadena1.isnumeric())
##print(cadena3.isnumeric())

#Método para devolver alfa-númerico es decir valores de la (a-z) sin espacios ni nada
##print(cadena4.isalpha())

#método para buscar y contar las coincidencias que existan en la cadena
##print(cadena1.count("a"))
##print(cadena1.count("A"))
##print(cadena1.count("o"))
##print(cadena1.count("todo"))

#Funcion para contar cantidad de caracteres que tiene una cadena
##print(len(cadena1))

#Método para verificar si una cadena empieza con una cadena dada si ess verdad devuelve True
##print(cadena1.startswith("ho"))
##print(cadena1.startswith("la"))

#Método para verificar si una cadena termina con una cadena dada si ess verdad devuelve True
##print(cadena1.endswith("dos"))
##print(cadena1.endswith("g"))

#Método remplaza un valor por otro
##print(cadena1.replace("hola", "vamos"))

#Método para separa las palabras por , de acuerdo a una conidicion devuelve una lista
print(cadena2.split(" "))
print(cadena2.split(" ")[2])
