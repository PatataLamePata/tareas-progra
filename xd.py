import random

palabrasSecretasLV1 = ["astro", "dirac", "celular", "casa", "fisica"]
palabrasSecretasLV2 = ["programacion", "dinosaurio", "guitarra", "pokemon", "badminton"]
palabrasSecretasLV3 = ["hipotenusa", "einstein", "hiperbolico", "arcotangente", "ciclico"]

nivel = 0
niveles = [palabrasSecretasLV1, palabrasSecretasLV2, palabrasSecretasLV3]

while nivel < len(niveles):
    palabraSecreta = random.choice(niveles[nivel]).upper()
    letra_acertada = ""
    intento = 5

    while True:

        letra = input("Escribe una letra: ").upper()

        if letra not in palabraSecreta:
            intento -= 1
            print("La letra", letra, "no se encuentra en la palabra, te quedan", intento, "intentos")

            if intento == 0:
                print("Has perdido maloooo, la palabra era", palabraSecreta)
                continuar = input("Desea continuar? (Si/No)>").strip().lower()
                if continuar == "si":
                    break
                else:
                    print("Juego terminado.")
                    exit()
                break
            continue  

        if not letra.isalpha():
            intento -= 1
            print("Te equivocasteee, te quedan", intento, "intentos")

            if intento == 0:
                print("Has perdido maloooo, la palabra era", palabraSecreta)
                continuar = input("Desea continuar? (Si/No)>").strip().lower()
                if continuar == "si":
                    break
                else:
                    print("Juego terminado.")
                    exit()
                break
            continue

        letra_acertada += letra

        resultado = [
            l if l in letra_acertada else "_" for l in palabraSecreta
        ]

        print("Resultado:", ' '.join(resultado))

        if ''.join(resultado) == palabraSecreta:
            nivel += 1
            print("Felicidades! Adivinaste la palabra", palabraSecreta)
            if nivel < 3:
                continuar = input("Desea continuar? (Si/No):").strip().lower()
                if continuar == "no":
                    print("Juego terminado.")
                    exit()
                    break
                elif continuar == "si":
                    break
            else:
                print("¡Has completado todos los niveles! 🏆")
                break
