#Listas (Se pueden modificar)-----------------------------------------------
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]
##print(lista)
##print(lista[1])
#Cambiar datos
lista[3] = "Maquinola"
##print(lista)
##print(lista[3])

#Tuplas (No se pueden modificar)-------------------------------------------
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)
##print(tupla)
##print(lista[1])

#Conjuntos (Los datos se muestran en desorden, no se puede acceder por el indice y no permite almacenar valores repetidos)-----------------------------------------------------------------
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85, "Lucas Dalto", "Soy Dalto"}
##print(conjunto)

#Dicionario (la estructura es key:value)
diccionario = {
    #(key)   : (value)
    "nombre" : "Lucas dalto",
    "canal" : "Soy Dalto",
    "estas_emocionado" : True,
    "altura" : 1.85,
    "dato_duplicado" : "Soy Dalto"
}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["altura"])
print(diccionario["altura"] + 2)