#Falto el profesor y los alumnos van a aramar la clase

#Pedir el nombre y la edad de los compañeros que vinieron hoy a clase
def obtener_alumnos (cantidad):
    compañeros = []
    #Ejecutando for para pedir información de cada compañero
    for i in range(1,cantidad,1):
        nombre = input('Ingrese el nombre del alumno. ')
        edad = int(input('Ingrese la edad de la persona: '))
        alumno = (nombre, edad)
        #Agregando información a la lista
        compañeros.append(alumno)
        #Ordenar de menor a mayor según su edad
    compañeros.sort(key=lambda x: x[1])
    #Definimos asistente y profesor el asistente es el mas joven y el profesor es el mas viejo es decir el ultimo dato
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #Retornamos una tupla
    return asistente, profesor
#Desempaquetamos lo que nos retorna la función
asistente, profesor = obtener_alumnos(5)
#mostrando el resultado
print(f'El profesor es {profesor} y su asistenete es {asistente}')