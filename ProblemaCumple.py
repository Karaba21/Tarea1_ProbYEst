import random

def simulacion_cumpleanos(m):
    cumpleanos = set()
    for i in range(m):
        dia = random.randint(1, 365)  # Ignoramos años bisiestos para simplificar
        if dia in cumpleanos:
            return True  # Hay coincidencia
        cumpleanos.add(dia)
    return False  # No hay coincidencia


def ejecutar_simulaciones(m, n_simulaciones):
    victorias = 0
    for _ in range(n_simulaciones):
        if simulacion_cumpleanos(m):
            victorias += 1
    derrotas = n_simulaciones - victorias
    probabilidad_empirica = victorias / n_simulaciones
    return victorias, derrotas, probabilidad_empirica


def probabilidad_teorica(m):
    if m > 365:
        return 1.0
    prob_no_coincidencia = 1.0
    for i in range(m):
        prob_no_coincidencia *= (365 - i) / 365
    return 1 - prob_no_coincidencia


def main():
    valores_m = [10, 20, 30, 40, 50]
    n_simulaciones_lista = [1000, 10000, 100000]

    print("--------- Resultados ---------")
    print("m  | Simulaciones | Victorias | Derrotas | Prob. Empírica | Prob. Teórica | Diferencia")
    print("-" * 90)

    for m in valores_m:
        prob_teo = probabilidad_teorica(m)
        for n_sim in n_simulaciones_lista:
            victorias, derrotas, prob_emp = ejecutar_simulaciones(m, n_sim)
            diferencia = abs(prob_emp - prob_teo)

            print(
                f"{m:2} | {n_sim:12,} | {victorias:9,} | {derrotas:8,} | "
                f"{prob_emp:14.4f} | {prob_teo:13.4f} | {diferencia:9.4f}")
        print("-" * 90)


if __name__ == "__main__":
    main()