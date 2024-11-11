#Variables definidas
a = 5
b = 8
c = a + b
print(c)

#Variables definidas modificadas
nombre = "Lucas Dalto"
nombre = "javier Costa"
nombre = "Pedrito"
print(nombre)

numero = 10
numero += 5
numero -= 5
print(numero)

#Cocatenación
nombre = "Luccas"
bienvenido = "Hola " + nombre + " ¿como estas?"
print(bienvenido);

#concatenación f strings se usa para converitr cualquier dato a texto
nombre = 5
bienvenido = f"Contando {nombre} números de la regla metrica"
#del se usa para borrar datos
    #del bienvenido
print(bienvenido);

#(Operador de pertencias in / not in)
nombre1 = "cinco"
bienvenido2 = f"Analizando {nombre1} números de la regla de todas las partes de la matematica"
print("artes" in bienvenido2) #True
print("ortanlencias" in bienvenido2) #True
print("analizando" in bienvenido2) #True
print("cinco" in bienvenido2) #True
print("artes" not in bienvenido2) #False
print("ortanlencias" not in bienvenido2) #False
print("analizando" not in bienvenido2) #False
