#Utilizando parametro args (*)
def suma (nombre, *numeros):
    return f'{nombre}, la suma de tus números es {sum(numeros)}'
resultado = suma("Lucas",5,10,3,9,20,3)
print(resultado)

#Con lista []
def suma_total (numeros):
    return sum([*numeros])
resultado = suma_total([5,10,3,9,20,3])
print(resultado)