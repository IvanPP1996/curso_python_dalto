lista = list(["hola", "dalto", 34, 56, 23, True])
lista_sin_cadenas = list([34, 56, 23, True, False, 2030, 4560, -456])

#Funcion len en listas devuelve el número de datos que hay
##print(len(lista))

#Método Agregando elementos con append() pero hasta el final de la lista
lista.append("JAJAJAJAJAJ")
##print(lista)

#Método Agregando elementos con append() pero indicando un indice especifico y los otros datos se corren al siguiete indice
lista.insert(2, "Hola mama")
##print(lista)

#Método para agregar varios elementos a una lista al final de esta
lista.extend([False,2030])
##print(lista)

#Método eleiminar un elemento de la lista por su indice
lista.pop(0)
#Forma de elminar el ultimo dato del elemento (-1) para eliminar el anteultimo (-2)
lista.pop(-1)
##print(lista)

#Método para remover un elemento por su valor
lista.remove("Hola mama")
##print(lista)

#Método para ordenar todos los elementos de una lista pero la lista no puede tener cadenas de caracteres
lista_sin_cadenas.sort()
##print(lista_sin_cadenas)

#Método para ordenar la lista en reversa es decir ascendente a descendente
lista_sin_cadenas.reverse()
##print(lista_sin_cadenas)

#Método para eliminar todos los elementos de la lista
##lista.clear()
##print(lista)