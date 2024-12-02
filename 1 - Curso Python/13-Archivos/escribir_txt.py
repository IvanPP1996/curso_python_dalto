with open('1 - Curso Python\\13-Archivos\\datos_TXT.txt','w' ,encoding='UTF-8') as archivo:
    #Sobreescribiendo el archivo
    ##archivo.write('jaajjajaaj te la reteclee')
    
    #Agregando dos líneas con writelines()
    archivo.writelines([' - Hola patrón como anda, la cosa por la sabana\n',' - Misericordia'])
    #Agregando otras dos líneas con writelines()
    archivo.writelines(['\n - pero que paso con las canicas del carro\n',' - Misericordia'])