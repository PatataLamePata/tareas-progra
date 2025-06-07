cantidadJugadores = int(input("Cuantos jugadores habrán?>>"))
jugadores = []

def obtener_puntaje(texto):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    numeros = "0123456789"
    puntaje = 0

    for c in texto:
        if c in vocales: 
            puntaje += 3
        elif c in consonantes:
            puntaje += 1
        elif c in numeros:
            puntaje += int(c)
        else:
            puntaje += 0
    return puntaje
    

def puntajesYTop(jugadores):
    listaPuntajes = []

    for jugador in jugadores:
        nombre = jugador[0]
        palabras = jugador[1:]
        puntajeTotal = 0

        for palabra in palabras:
            puntajeTotal += obtener_puntaje(palabra)
        
        listaPuntajes.append((nombre, puntajeTotal))
    
    listaPuntajes.sort(key=lambda x: x[1], reverse=True)

    print(f"El ganador es {listaPuntajes[0][0]} con {listaPuntajes[0][1]} puntos!!!")

    print("\n Los demás jugadores obtuvieron:")
    for i, (nombre, puntaje) in enumerate(listaPuntajes[1:], start=2):
        print(f"{i}. {nombre} : {puntaje} puntos")

for i in range(cantidadJugadores):
    jugadores.append([])

for i in range(cantidadJugadores):
    nombre = input(f"Cuál es el nombre del jugador {i+1}?>> ")
    jugadores[i].append(nombre)
    cantidadPalabras = int(input(f"Cuántas palabras jugará el jugador {nombre}?>> "))
    for j in range(cantidadPalabras):
        palabra = input(f"Ingrese la palabra {j + 1} de {nombre} >> ")
        jugadores[i].append(palabra)
        
puntajesYTop(jugadores)



