import time
import numpy as np
import math

inicio = time.time()

#  NumPy nos ayuda manejar mas rapido los arreglos
numeros = np.arange(2, 100001)
primos = []

for n in numeros:
    es_primo = True
    # raíz cuadrada del número
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(n)

fin = time.time()

print("Cantidad de números primos:", len(primos))
print("Tiempo de ejecución con optimización en segundos:", fin - inicio)

