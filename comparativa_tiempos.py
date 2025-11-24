import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Tiempos en segundos
tiempo_original = 79.08926916122437
tiempo_optimizado = 0.56

versiones = ['Original', 'Optimizado']
tiempos = [tiempo_original, tiempo_optimizado]

plt.bar(versiones, tiempos, color=['pink', 'green'])
plt.title('Comparativa de tiempos de ejecución')
plt.ylabel('Segundos')
plt.xlabel('Versión del código')

# Agregar los valores encima de las barras
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo + 1, f'{tiempo:.2f}s', ha='center')

plt.show()
