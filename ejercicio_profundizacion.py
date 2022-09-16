import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def fetch():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute('SELECT pulso FROM sensor')
    data = list(c.fetchall())
    print(data)
    conn.close()
    return data

def show(data):
    x = range(0, len(data))

    fig = plt.figure()
    fig.suptitle('Pulsos del futbol', fontsize=16)
    ax = fig.add_subplot()

    ax.plot(x, data, c='darkgreen', label='Pulsos')
    ax.legend()
    ax.grid()
    plt.show()


def estadistica(data):
    medio = None
    minimo = None
    maximo = None
    desvio = None

    medio = np.mean(data)
    minimo = np.min(data)
    maximo = np.max(data)
    desvio = np.std(data)

    print("Respecto de la lista, podemos recabar la siguiente informacion:")
    print("Valor medio: ", f"{medio:.2f}", "\nMínimo: ", minimo, "\nMáximo: ", maximo, "\nDesvío estandar: ", f"{desvio:.2f}")

def regiones(data):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    medio = np.mean(data)
    desvio = np.std(data)

    for i in range(len(data)):
        if data[i] <= (medio-desvio):
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (medio+desvio):
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])

    fig = plt.figure()
    fig.suptitle('Latidos futbolísticos!', fontsize=16, c='gray')
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)

    ax1.scatter(x1, y1, c='darkgreen')
    ax1.set_ylim(40, 150)
    ax1.grid()

    ax2.scatter(x2, y2, c='darkorange')
    ax2.set_ylim(40,150)
    ax2.grid()

    ax3.scatter(x3, y3, c='navy')
    ax3.set_ylim(40, 150)
    ax3.grid()
    # Los tres gráficos están configurados en sus límites inferior y superior para poder ver la distribución
    # de las 3 listas
    plt.show()



if __name__ == "__main__":
  # Leer la DB
  data = fetch()

  # Data analytics
  show(data)
  estadistica(data)
  regiones(data)
  print("Terminamos!")
