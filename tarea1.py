cantidadPalabras = int(input("Cuantas palabras tiene la frase?>>"))

palabrasEncriptadas = []
for i in range(cantidadPalabras):
    palabra = input(f"Escribe la palabra encriptada {i+1}: ")
    palabrasEncriptadas.append(palabra)


def desencriptacion(listaPalabras):
    palabrasDesencriptadas = []
    for palabra in listaPalabras:
        letrasMayusculas = [c for c in palabra if c.isupper()]
        palabraDesencriptada = ''.join(letrasMayusculas).lower()
        palabrasDesencriptadas.append(palabraDesencriptada)
    resultado = ' '.join(palabrasDesencriptadas)
    return resultado

fraseDesencriptada = desencriptacion(palabrasEncriptadas).lower()

print(fraseDesencriptada)
