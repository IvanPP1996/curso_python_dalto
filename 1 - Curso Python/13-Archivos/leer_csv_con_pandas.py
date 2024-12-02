import pandas as pd

df = pd.read_csv('1 - Curso Python\\13-Archivos\\datos.csv')
df2 = pd.read_csv('1 - Curso Python\\13-Archivos\\datos.csv')
##df = pd.read_csv('1 - Curso Python\\13-Archivos\\datos.csv' ,names=['name','lastname','age'])
##print(df)

#Obteniendo datos de la columna nombre
##nombres = df["name"]
nombres = df["nombre"]
##print(nombres)

#Metodo para recorrer cadena y obtener caracteres especificos
cadena = "0123456789"
##print(cadena[:3])
##print(cadena[:7])
##print(cadena[2:7])

#Ordenanado el df por edad de forma ascendente
df_ordenado = df.sort_values('edad')
##print(df_ordenado)
#Ordenanado el df por edad de forma descendente
df_ordenadoAscend = df.sort_values('edad',ascending=False)
##print(df_ordenadoAscend)

#Concatenando los dos df (dataframes)
df_concatenado = pd.concat([df, df2])
##print(df_concatenado)

#Accediendo a la primer fila con head()
primer_fila = df.head(1)
primer_fila = df.head(0)
primer_fila = df.head(3)

##print(primer_fila)

#Accediendo a las ultimas filas con tail()
ultimas_filas = df.tail(2)

##print(ultimas_filas)

#Accediendo a la cantidad de filas y columnas shape Nota: primer valor es filas y segundo valor columnas
filas_totales, columnas_totales = df.shape

print(filas_totales)
print(columnas_totales)
