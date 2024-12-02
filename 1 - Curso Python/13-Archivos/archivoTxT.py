archivo = open('1 - Curso Python\\13-Archivos\\datos_TXT.txt', encoding="UTF-8")
#mostrar todo el archivo
##print(archivo.read())

#Leer línea por línea
##linea_1 = archivo.readlines()
##print(linea_1)
#Leer solo una línea
linea_1 = archivo.readline()
##print(linea_1)
#Mostrar la cantidad de caracteres
linea_1 = archivo.readline(13)
##print(linea_1)
#Cerrar el archivo
archivo.close()
print(archivo.read())