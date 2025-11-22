import time #descargamos la libreria para poder calcular el tiemo

inicio = time.time()

primos = [] #Para crear la lista de num prims y hacemos un ciclo for para revisar del 1 al 100000
for num in range(1, 100001):
    if num > 1:  
        for i in range(2, num):
            if (num % i) == 0:  # Si el número se puede dividir entonces no es numero primo
                break
        else:
            primos.append(num)  #  lo guardamos como primo


fin = time.time()

print("Cantidad de números primos:", len(primos))
print("Tiempo de ejecución del codigo en segundos:", fin - inicio, )
