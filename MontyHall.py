import random

def generar_puertas() -> list[int]:
    puertas = [0, 0, 0]
    puertas[random.randint(0, 2)] = 1  # Coloca el auto en una puerta
    return puertas

def obtener_puerta_auto(puertas: list[int]) -> int:
    return puertas.index(1)

def abre_puerta(puertas: list[int], puerta_elegida: int) -> int:
    opciones = [i for i in range(3) if i != puerta_elegida and puertas[i] != 1]
    return random.choice(opciones)

def cambiar_puerta(puerta_elegida: int, puerta_abierta: int) -> int:
    return [i for i in range(3) if i != puerta_elegida and i != puerta_abierta][0]

def verificar_ganador(puertas: list[int], puerta_elegida: int) -> bool:
    return puertas[puerta_elegida] == 1

# Configuración
juegos_totales = 10000 #Cantidad de juegos totales
mostrar_logs = False  # ¡¡¡Cambiar a True o False para ver o no cada juego en especifico!!!

# Contadores
cambios = 0
no_cambios = 0
victorias_cambiando = 0
victorias_sin_cambiar = 0

for i in range(juegos_totales):
    puertas = generar_puertas()
    puerta_con_auto = obtener_puerta_auto(puertas)
    puerta_elegida_original = random.randint(0, 2)
    puerta_abierta = abre_puerta(puertas, puerta_elegida_original)

    cambiar = random.choice([True, False])
    puerta_final = puerta_elegida_original

    if cambiar:
        puerta_final = cambiar_puerta(puerta_elegida_original, puerta_abierta)

    gano = verificar_ganador(puertas, puerta_final)

    if mostrar_logs:
        print(f"\nJuego {i + 1}:")
        print(f"Puerta elegida por el participante: {puerta_elegida_original}")
        print(f"Puerta donde está el auto: {puerta_con_auto}")
        print(f"Puerta abierta por el presentador: {puerta_abierta}")
        if cambiar:
            print(f"Cambiaste a la puerta: {puerta_final}")
        else:
            print("No cambiaste de puerta")
        print(f"Resultado del concurso: {'Ganaste el auto' if gano else 'Perdiste'}")

    # Contadores
    if cambiar:
        cambios += 1
        if gano:
            victorias_cambiando += 1
    else:
        no_cambios += 1
        if gano:
            victorias_sin_cambiar += 1

# Resultados finales
print(f"\n Simulaciones: {juegos_totales}")
print(f" Cambió de puerta: {cambios} veces")
print(f" Victorias cambiando: {victorias_cambiando}"
      f" ({(victorias_cambiando / cambios) * 100:.2f}%)\n"
      if cambios > 0 else "")

print(f" No cambió de puerta: {no_cambios} veces")
print(f" Victorias sin cambiar: {victorias_sin_cambiar}"
      f" ({(victorias_sin_cambiar / no_cambios) * 100:.2f}%)\n"
      if no_cambios > 0 else "")

victorias_totales = victorias_cambiando + victorias_sin_cambiar
print(f" Total de victorias: {victorias_totales} de {juegos_totales} juegos")
print(f" Probabilidad total de ganar: {(victorias_totales / juegos_totales) * 100:.2f}%")
