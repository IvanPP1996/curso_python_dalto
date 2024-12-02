#Abriendo archivo con with open
with open('1 - Curso Python\\13-Archivos\\datos_TXT.txt') as archivo:
    #Leemos y mostramos el archivo
    print(archivo.read())
#No es necesario cerrarlo al usar with open