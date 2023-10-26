

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
 
# if contenido_del_archivo:
#     print(contenido_del_archivo)

lista = contenido_del_archivo.split('\n')
print(lista)
p = len(lista)

for n in range(p):


