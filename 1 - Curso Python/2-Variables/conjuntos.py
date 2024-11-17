#Creando un cojunto con set NOTA: con set solo se pueden pasar valores que no se pueden cambiar despues
conjunto = set(["Dato 1","Dato 2", ("Dato 3.1", "Dato 3.2", "Dato 3.3")])

##print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto_meter = frozenset(["dato 1", "dato 2"])
conjunto_general = {conjunto_meter, "dato 3"}

##print(conjunto_general)

#Teoría de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
conjunto3 = {2,4,10}

#Verificanco si es un sub-conjunto
##print(conjunto2.issubset(conjunto1))
##print(conjunto1.issubset(conjunto2))
##print(conjunto2 <= conjunto1)
##print(conjunto1 <= conjunto2)

#Verificanco si es un super-conjunto
##print(conjunto2.issuperset(conjunto1))
##print(conjunto1.issuperset(conjunto2))
##print(conjunto2 < conjunto1)
##print(conjunto1 < conjunto2)

#Verificar si hay un número en común (OJo esto es (True) si los datos son diferentes pero si hay un solo dato igual es (False))
print(conjunto2.isdisjoint(conjunto1))
print(conjunto3.isdisjoint(conjunto1))