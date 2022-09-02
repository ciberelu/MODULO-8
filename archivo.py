f = open ("archivo_de_texto.txt", "w")
f.write("hola\n")
f.write("hola de nuevo\n")
f.close()

f = open("archivo_de_texto.txt", "a")
f.write("es algo nuevo")
f.close()