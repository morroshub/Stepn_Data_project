import json
import statistics

# Cargar resultados desde el archivo JSON
with open("/Users/lucasmorrone/Documents/Projectos_data/Stepn_Data_project/Codigo_Probabilidad/resultados.json", "r") as archivo:
    resultados = json.load(archivo)

# Obtener los conteos de intentos fallidos, intentos exitosos y intentos exitosos con gran premio
conteos_intentos_fallidos = [resultado[1] for resultado in resultados]
conteos_intentos_exitosos = [resultado[2] for resultado in resultados]
conteos_intentos_exitosos_gran_premio = [resultado[3] for resultado in resultados]

# Calcular la moda y la media de los conteos de intentos fallidos
moda_intentos_fallidos = statistics.mode(conteos_intentos_fallidos)
media_intentos_fallidos = statistics.mean(conteos_intentos_fallidos)

# Calcular la moda y la media de los conteos de intentos exitosos
moda_intentos_exitosos = statistics.mode(conteos_intentos_exitosos)
media_intentos_exitosos = statistics.mean(conteos_intentos_exitosos)

# Calcular la moda y la media de los conteos de intentos exitosos con gran premio
moda_intentos_exitosos_gran_premio = statistics.mode(conteos_intentos_exitosos_gran_premio)
media_intentos_exitosos_gran_premio = statistics.mean(conteos_intentos_exitosos_gran_premio)

print("Moda de los intentos fallidos:", moda_intentos_fallidos)
print("Media de los intentos fallidos:", media_intentos_fallidos)

print("Moda de los intentos exitosos:", moda_intentos_exitosos)
print("Media de los intentos exitosos:", media_intentos_exitosos)

print("Moda de los intentos exitosos con gran premio:", moda_intentos_exitosos_gran_premio)
print("Media de los intentos exitosos con gran premio:", media_intentos_exitosos_gran_premio)
