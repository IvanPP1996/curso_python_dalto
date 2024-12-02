#Importando un modulo
##import modulo_saludar

#Importando un modulo pero reduciendo el nombre de la funcion a llamar
##import modulo_saludar as m_saludar

#Importamos todas las funciones sin necesida de escribir sus nombres pero es una mala practica
##from modulo_saludar import *
#Importando un modulo y solo la funcion, este se puede usar para llamar varias funciones
from modulo_saludar import saludar, saludar_raro

#print(modulo_saludar.saludar('Lucas'))
#print(m_saludar.saludar('Lucas'))
print(saludar('Lucas'))
print(saludar_raro('Donald'))