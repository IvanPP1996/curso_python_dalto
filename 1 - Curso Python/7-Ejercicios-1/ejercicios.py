#a)Promedio duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencias de duración
print("--------------------")
diferencia_curso_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_curso_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_curso_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
print(f"El curso de Dalto dura {diferencia_curso_min}% menos que el más rapido")
print(f"El curso de Dalto dura {diferencia_curso_max}% menos que el más rapido")
print(f"El curso de Dalto dura {diferencia_curso_promedio}% menos que el más rapido")
print("--------------------")


#b)Duración crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Calculando el porcentaje de tiempo vacío
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print(f"Un curso de promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío")
print(f"El curso de Dalto de elimina un {tiempo_vacio_dalto}% de tiempo vacío")
print("--------------------")


#c)Mostrando diferencias si los cursos durán 10 horas
print(f"Ver 10 horas de este curso equivalen a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivalen a ver {dalto_curso *100 // otros_cursos_promedio / 10} horas de otros cursos")
print("--------------------")