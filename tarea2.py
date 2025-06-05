palabraSecreta = "newton"
letra_acertada = ""
intento = 5

while True:
    letra = input("Escribe una letra: ")
    letra = letra.upper()
    palabraSecreta = palabraSecreta.upper()

    if letra not in palabraSecreta:
        intento -= 1
        print("La letra", letra, "no se encuentra en la palabra, te quedan", intento, "intentos")

        if intento == 0:
            print("Has perdido maloooo, la palabra era", palabraSecreta)
            break
        continue

    if not letra.isalpha():
        intento -= 1
        print("Te equivocasteee, te quedan", intento, "intentos")

        if intento == 0:
            print("Has perdido maloooo, la palabra era", palabraSecreta)
            break
        continue

    letra_acertada += letra

    resultado = [
        l if l in letra_acertada else "_" for l in palabraSecreta
    ]

    print("Resultado:", ' '.join(resultado))

    if ''.join(resultado) == palabraSecreta:
        print("Felicidades! Adivinaste la palabra", palabraSecreta)
        break