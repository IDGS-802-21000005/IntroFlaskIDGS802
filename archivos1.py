from io import open

archivo_texto = open("archivo.txt", "r")
# archivo_texto.write('\n datos en el archivo')
print(archivo_texto.read())

# el archivo se lee con un cursor por lo que ya no vuelve a mostrar el texto
# utilizamos el seek para reposicionar el cursor al inicio del archivo
archivo_texto.seek(0)
print(archivo_texto.read())

archivo_texto.seek(0)
print(archivo_texto.readlines())

archivo_texto.seek(0)
for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

archivo_texto.close()