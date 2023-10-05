import random
import json
import matplotlib.pyplot as plt

def simular_intentos():
    intentos = 0
    exito = False

    while not exito:
        intentos += 1
        if random.random() >= 0.75:
            if random.random() <= 0.005:
                exito = True

    return intentos

resultados = []
num_simulaciones = 1000  # Número de simulaciones a realizar

for _ in range(num_simulaciones):
    intentos = simular_intentos()
    resultados.append(intentos)

# Guardar resultados en archivo JSON
with open("resultados.json", "w") as archivo:
    json.dump(resultados, archivo)

