#Creando una función simple
def saludar ():
    print('Hola Lucas mi maestro como andas')

#Ejecutando la función simple
##saludar()

#Creando funcion con parametro
def saludar (nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'reina'
    elif sexo == 'hombre':
        adjetivo = 'titan'
    else:
        adjetivo = 'crack'
    print(f'Hola {nombre} mi {adjetivo} como andas')

##saludar('Camila', 'MUJER')
##saludar('Dalto', 'Hombre')
##saludar('Frank', 'no identifica')

#Crear una función que nos retorne valores