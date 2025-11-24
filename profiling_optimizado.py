import cProfile
import pstats
import io
import time
import numpy as np
import math

def calcular_primos():
    numeros = np.arange(2, 100001)
    primos = []
    for n in numeros:
        es_primo = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    return primos

def main():
    inicio = time.time()
    primos = calcular_primos()
    fin = time.time()
    print("Cantidad de números primos:", len(primos))
    print("Tiempo total en segundos:", fin - inicio)

if __name__ == "__main__":
    # Creamos y uradamos en el nuevo archivo txt 
    with open("C:/Tareas_FundamentosBD/profiling_optimizado.txt", "w") as f:
        pr = cProfile.Profile()
        pr.enable()
        main()
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
        ps.print_stats()
        f.write(s.getvalue())
