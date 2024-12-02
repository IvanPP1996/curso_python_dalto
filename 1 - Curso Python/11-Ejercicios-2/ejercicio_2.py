#retornando una función que nos devuelva los números primos entre el 0 y el argumento que pasemos

def numeros_primos (numero):
    
    for i in range(2,numero-1):
        if numero % i == 0:
            return False
    return True

def primos_hasta (numero):
    primos = []
    for i in range (2,numero+1):
        resultado = numeros_primos(i)
        if resultado == True:
            primos.append(i)
    return primos

#print(numeros_primos(13))
#print(numeros_primos(9))

print(primos_hasta(98))