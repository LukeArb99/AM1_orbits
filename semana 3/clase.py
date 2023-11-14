

def leer_archivo_como_string(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"El archivo '{nombre_archivo}' no se encontró."
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {str(e)}"
 
# Reemplaza 'nombre_del_archivo.txt' con la ruta de tu archivo de texto
nombre_archivo = 'semana 3\musica.txt'
contenido_del_archivo = leer_archivo_como_string(nombre_archivo)
 

lista = contenido_del_archivo.split('\n')
# print(lista)
p = len(lista)
# print(p)
# p = 5
lista = list(lista)
lista_final=['***letra cancion****']
for i in range(p):
    if i%2==0:
        lista_final.append(lista[i])


p =lista_final.index('[Verse 1]')

for i in range(p-1):
    lista_final.remove(lista_final[1])
    


h=len(lista_final)
for i in range(h):
    print(lista_final[i])

