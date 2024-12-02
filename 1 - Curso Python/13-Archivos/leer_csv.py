import csv

with open('1 - Curso Python\\13-Archivos\\datos.csv') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)