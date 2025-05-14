# # Objetivo: Animar una onda seno que cambia de fase a lo largo del tiempo.
# # • Animar una función sin(x + t).
# # • Usar FuncAnimation.
# # • Mostrar cómo la onda se desplaza hacia la izquierda o derecha.


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Configuración inicial de la figura y los ejes
# fig, ax = plt.subplots()
# x = np.linspace(0, 4 * np.pi, 1000)  # valores de x
# line, = ax.plot(x, np.sin(x))        # línea inicial

# # Establecer límites para los ejes
# ax.set_xlim(0, 4 * np.pi)
# ax.set_ylim(-1.5, 1.5)
# ax.set_title("Onda seno animada: sin(x + t)")
# ax.set_xlabel("x")
# ax.set_ylabel("sin(x + t)")
# ax.grid(True)

# # Función de actualización de la animación
# def update(frame):
#     t = frame / 10  # control de velocidad
#     y = np.sin(x + t)  # onda que cambia de fase
#     line.set_ydata(y)
#     return line,

# # Crear la animación
# ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# # Mostrar la animación
# plt.savefig("onda_seno.png", dpi=300)

# plt.show()
# -------------------------------------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Número de partículas
# num_particles = 100

# # Posiciones iniciales aleatorias
# x = np.random.rand(num_particles)
# y = np.random.rand(num_particles)

# # Crear la figura y el gráfico scatter
# fig, ax = plt.subplots()
# scat = ax.scatter(x, y)

# # Configurar los límites del plano
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_title("Movimiento aleatorio de partículas")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.grid(True)

# # Función para actualizar las posiciones
# def update(frame):
#     global x, y
#     # Movimiento aleatorio pequeño en cada dirección
#     dx = (np.random.rand(num_particles) - 0.5) * 0.05
#     dy = (np.random.rand(num_particles) - 0.5) * 0.05
#     x += dx
#     y += dy

#     # Mantener las partículas dentro del plano (rebote)
#     x = np.clip(x, 0, 1)
#     y = np.clip(y, 0, 1)

#     # Actualizar datos del scatter plot
#     scat.set_offsets(np.c_[x, y])
#     return scat,

# # Crear animación
# ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)


# plt.savefig("puntos aleatorios.png", dpi=300)

# # # Mostrar
# # plt.show()
# # ---------------------------------------------------------------------------

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Crear figura y ejes
# fig, ax = plt.subplots()
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# ax.set_aspect('equal')
# ax.set_title("Punto girando en un círculo")
# ax.grid(True)

# # Coordenadas del círculo de referencia
# t_vals = np.linspace(0, 2 * np.pi, 100)
# x_tray = np.cos(t_vals)
# y_tray = np.sin(t_vals)
# ax.plot(x_tray, y_tray, 'b-', linewidth=1)  # Dibujar el círculo de referencia

# # Inicializar punto
# punto, = ax.plot([], [], 'ro', markersize=8)

# def init():
#     punto.set_data([], [])
#     return punto,

# def update(frame):
#     t = frame * 0.1  # Avanzando en el tiempo
#     x = np.cos(t)
#     y = np.sin(t)
#     punto.set_data([x], [y])  # Asegurar que set_data recibe listas
#     return punto,

# ani = FuncAnimation(fig, update, frames=np.arange(0, 200, 1), init_func=init, interval=50, repeat=True)
# plt.savefig("circulo.png", dpi=300)
# plt.show()
# --------------------------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Cargar datos desde CSV (modifica el nombre del archivo según tus datos)
# df = pd.read_csv("01 renewable-share-energy.csv")

# # Filtrar datos para algunos países (puedes ajustar según tu interés)
# paises = ["Africa", "Japan", "Colombia"]
# df_filtrado = df[df["Entity"].isin(paises)].sort_values(["Entity", "Year"])

# # Configuración de la gráfica
# fig, ax = plt.subplots()
# ax.set_xlim(0, 100)  # Ajuste del eje x según valores máximos
# ax.set_ylim(0, len(paises))
# ax.set_title("Evolución de Energía Renovable")
# ax.set_xlabel("Renovables (% energía primaria)")
# ax.set_ylabel("Países")

# bars = ax.barh(paises, [0] * len(paises), color=["green", "blue", "red"])
# textos = [ax.text(0, i, "", va="center", fontsize=12) for i in range(len(paises))]

# # Función de actualización de la animación
# def update(frame):
#     año_actual = df_filtrado["Year"].unique()[frame]
#     datos_año = df_filtrado[df_filtrado["Year"] == año_actual]

#     for i, pais in enumerate(paises):
#         valor = datos_año[datos_año["Entity"] == pais]["Renewables (% equivalent primary energy)"].values
#         if len(valor) > 0:
#             bars[i].set_width(valor[0])  # Actualizar el ancho de la barra
#             textos[i].set_text(f"{pais}: {valor[0]:.2f}%")
    
#     ax.set_title(f"Energía Renovable en {año_actual}")

# # Crear la animación
# ani = FuncAnimation(fig, update, frames=len(df_filtrado["Year"].unique()), interval=500)

# plt.show()
# --------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
ax.set_title("Sistema Planetario Simple")
ax.grid(True)

# Posición de la estrella central
ax.plot(0, 0, 'yo', markersize=10, label="Estrella")

# Parámetros de los planetas (radio y velocidad angular)
planetas = [
    {"color": "red", "radio": 4, "velocidad": 0.05},
    {"color": "blue", "radio": 7, "velocidad": 0.03},
    {"color": "green", "radio": 10, "velocidad": 0.02}
]

# Inicializar los planetas y trayectorias
puntos = []
trayectorias = []
trayectoria_data = {i: {"x": [], "y": []} for i in range(len(planetas))}

for planeta in planetas:
    punto, = ax.plot([], [], 'o', color=planeta["color"], markersize=6)
    trayectoria, = ax.plot([], [], '-', color=planeta["color"], linewidth=1)
    puntos.append(punto)
    trayectorias.append(trayectoria)

ax.legend()

def init():
    for punto, trayectoria in zip(puntos, trayectorias):
        punto.set_data([], [])
        trayectoria.set_data([], [])
    return puntos + trayectorias

def update(frame):
    for i, planeta in enumerate(planetas):
        t = frame * planeta["velocidad"]
        x = planeta["radio"] * np.cos(t)
        y = planeta["radio"] * np.sin(t)
        puntos[i].set_data([x], [y])  # Asegurar que set_data recibe listas

        # Guardar trayectoria
        trayectoria_data[i]["x"].append(x)
        trayectoria_data[i]["y"].append(y)
        trayectorias[i].set_data(trayectoria_data[i]["x"], trayectoria_data[i]["y"])

    return puntos + trayectorias

# Crear la animación
ani = FuncAnimation(fig, update, frames=500, init_func=init, interval=50, repeat=True)

plt.show()