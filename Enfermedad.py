import random

prob_enfermedad = 1 / 10000       
prob_no_enfermedad = 1 - prob_enfermedad  

prob_positivo_si_enfermo = 0.99      
prob_positivo_si_sano = 0.02         

total_simulaciones = 1000000
total_positivos = 0
total_verdaderos_positivos = 0

for _ in range(total_simulaciones):
    tiene_enfermedad = random.random() < prob_enfermedad

    if tiene_enfermedad:
        test_positivo = random.random() < prob_positivo_si_enfermo
    else:
        test_positivo = random.random() < prob_positivo_si_sano

    if test_positivo:
        total_positivos += 1
        if tiene_enfermedad:
            total_verdaderos_positivos += 1

if total_positivos > 0:
    probabilidad_estimada = total_verdaderos_positivos / total_positivos
    print(f"1. Probabilidad estimada por simulación: {probabilidad_estimada:.6f}")
else:
    print("No hubo casos positivos en la simulación.")


numerador = prob_positivo_si_enfermo * prob_enfermedad
denominador = (prob_positivo_si_enfermo * prob_enfermedad) + (prob_positivo_si_sano * prob_no_enfermedad)
probabilidad_exacta = numerador / denominador

print(f"2. Probabilidad exacta con fórmula de Bayes: {probabilidad_exacta:.6f}")
