# #  1. Gráfico de línea simple
# #    Escribe un programa que grafique la siguiente lista de valores:
# #    valores = \[3, 7, 1, 5, 12]
# #    Agrega título, etiquetas de ejes y una cuadrícula.

# import matplotlib.pyplot as plt

# # Lista de valores a graficar
# valores = [3, 7, 1, 5, 12]

# # Crear una lista para el eje X (por ejemplo: índices)
# x = list(range(len(valores)))

# # Crear el gráfico de línea
# plt.plot(x, valores, marker='o', linestyle='-', color='b', label='Valores')
# plt.legend()

# # Título y etiquetas
# plt.title('Gráfico de Línea Simple')
# plt.xlabel('Índice')
# plt.ylabel('Valor')

# # Mostrar la cuadrícula
# plt.grid(True)

# # Mostrar el gráfico
# plt.show()
# plt.savefig('uno.png')

# # ---------------------------------------------------------------------------------------------------
# 2. Gráfico de barras
# Grafica la cantidad de estudiantes en 5 cursos:
# cursos = ['A', 'B', 'C', 'D', 'E']
# cantidad = [30, 25, 40, 20, 35]
# import matplotlib.pyplot as plt
# cursos = ['A', 'B', 'C', 'D', 'E']
# cantidad = [30, 25, 40, 20, 35]
# plt.bar(cursos, cantidad, color = 'orange')
# plt.title('Grafica de estudiantes')
# plt.xlabel('curso')
# plt.ylabel('cantidad')
# plt.savefig('dos.png')
# plt.show()
# nota: se pone primero eje x y luego eje y, ademas se pone un color que quieras 
# ---------------------------------------------------------------------------------------------------
# 3. Gráfico de dispersión (scatter plot)
# Genera dos listas de números aleatorios de 50 elementos y haz un gráfico de dispersión.
# import matplotlib.pyplot as plt
# import random
# x= [random.randint(0,100) for _ in range(50)]
# y= [random.randint(0,100) for _ in range(50)]
# plt.scatter(x,y, color = 'orange')
# plt.title('Grafica de dispercion')
# plt.xlabel('numero ramdon')
# plt.ylabel('numero ramdon')
# plt.savefig('tres.png')
# plt.show()
# ---------------------------------------------------------------------------------------------------
# 4. Subplots
# Crea un figure con 2 subgráficos:
# Uno con una línea senoidal.
# Otro con una función cuadrática.
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-10, 10, 100)
# y1 = np.sin(x)
# y2 = x ** 2

# plt.subplot(1, 2, 1)         # 1 fila, 2 columnas, primer gráfico
# plt.plot(x, y1)
# plt.title("Seno")

# plt.subplot(1, 2, 2)         # 1 fila, 2 columnas, segundo gráfico
# plt.plot(x, y2)
# plt.title("Cuadrática")

# plt.tight_layout()           # Ajusta los espacios
# plt.show()
# plt.savefig('cuatro.png')
# ---------------------------------------------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-10, 10, 100)   # Genera los valores de x
# y = x**2 - 3*x + 2              # Aplica la fórmula y = x² - 3x + 2

# plt.plot(x, y)                  # Dibuja la función
# plt.title("Gráfica de y = x² - 3x + 2")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(True)
# plt.show()
# plt.savefig('cinco.png')
# ---------------------------------------------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2*np.pi, 100)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# plt.plot(x, y_sin, label='sin(x)', color='blue')
# plt.plot(x, y_cos, label='cos(x)', color='red')

# plt.title("Funciones sin(x) y cos(x)")
# plt.xlabel("x (radianes)")
# plt.ylabel("y")
# plt.grid(True)
# plt.legend()

# plt.show()
# plt.savefig('seis.png')
# ---------------------------------------------------------------------------------------------------
# import numpy as np

# # Generar los dos vectores
# v1 = np.random.randint(0, 101, 100)
# v2 = np.random.randint(0, 101, 100)

# # Cálculos para el primer vector
# print("Vector 1:")
# print("Suma total:", v1.sum())
# print("Valor máximo:", v1.max())
# print("Desviación estándar:", v1.std())

# # Cálculos para el segundo vector
# print("\nVector 2:")
# print("Suma total:", v2.sum())
# print("Valor máximo:", v2.max())
# print("Desviación estándar:", v2.std())
# ---------------------------------------------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt

# # Generar 1000 números con distribución normal (media 0, desviación 1)
# datos = np.random.normal(0, 1, 1000)

# # Mostrar histograma
# plt.hist(datos, bins=30, color='skyblue', edgecolor='black')
# plt.title("Histograma de distribución normal")
# plt.xlabel("Valor")
# plt.ylabel("Frecuencia")
# plt.grid(True)
# plt.show()
# plt.savefig('histograma.png')
# ---------------------------------------------------------------------------------------------------
# import pandas as pd

# # Cargar el archivo CSV
# df = pd.read_csv("ventas.csv")

# # Mostrar las primeras 5 filas
# print(df.head())
# ---------------------------------------------------------------------------------------------------
# import pandas as pd

# # Cargar el archivo CSV
# df = pd.read_csv("ventas.csv")

# # Verificar los nombres de las columnas
# print(df.columns)

# # Limpiar posibles espacios en los nombres de las columnas
# df.columns = df.columns.str.strip()

# # Total de ventas: sumamos todas las columnas de productos
# total_ventas = df["producto_a"].sum() + df["producto_b"].sum() + df["producto_c"].sum()
# print(f"Total de ventas: {total_ventas}")

# # Promedio de precio: calculamos el promedio de ventas por producto
# promedio_precio_a = df["producto_a"].mean()
# promedio_precio_b = df["producto_b"].mean()
# promedio_precio_c = df["producto_c"].mean()

# print(f"Promedio de ventas Producto A: {promedio_precio_a:.2f}")
# print(f"Promedio de ventas Producto B: {promedio_precio_b:.2f}")
# print(f"Promedio de ventas Producto C: {promedio_precio_c:.2f}")

# # Producto más vendido: buscar cuál de los productos tiene la mayor venta total
# ventas_totales = {
#     "producto_a": df["producto_a"].sum(),
#     "producto_b": df["producto_b"].sum(),
#     "producto_c": df["producto_c"].sum()
# }

# producto_mas_vendido = max(ventas_totales, key=ventas_totales.get)
# print(f"Producto más vendido: {producto_mas_vendido}")
# ---------------------------------------------------------------------------------------------------
# import pandas as pd

# # Cargar el archivo CSV
# df = pd.read_csv("ventas.csv")

# # Mostrar las primeras filas para verificar la estructura del archivo
# print(df.head())

# # Filtrar las ventas de enero
# enero_ventas = df[df["mes"] == "Enero"]

# # Mostrar las ventas de enero
# print("Ventas en el mes de Enero:")
# print(enero_ventas)
# ---------------------------------------------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar el archivo CSV
# df = pd.read_csv("ventas.csv")

# # Limpiar posibles espacios en los nombres de las columnas
# df.columns = df.columns.str.strip()

# # Sumar las ventas por producto
# total_ventas_producto = df[["producto_a", "producto_b", "producto_c"]].sum()

# # Graficar la cantidad total vendida por producto
# total_ventas_producto.plot(kind='bar', color=['blue', 'green', 'orange'])

# # Configurar el título y etiquetas
# plt.title("Cantidad total vendida por producto")
# plt.xlabel("Producto")
# plt.ylabel("Ventas")
# plt.xticks(rotation=0)  # Asegura que las etiquetas de los productos sean horizontales

# # Mostrar el gráfico
# plt.show()
# plt.savefig('ultima.png')

# ---------------------------------------------------------------------------------------------------
