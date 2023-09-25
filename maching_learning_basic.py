import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotter3D import MyPlot
import math


def update_w_b(datos1, datos2, w, b, alpha):
    dl_dw = 0.0  #se Inicializan las derivadas respecto a b y w
    dl_db = 0.0

    N = 0.0
    if len(datos1) == len(datos2):
        N = len(datos1)  #Se asigna el valor de N TODO: n = dato con menor len
    else:
        print('Error datos incompatibles')

    for i in range(N):
        #La función A optimizar es la sumatoria de una función por ende sus derivadas parciales también son sumatorios de una función
        dl_dw += -2 * datos1[i] * (datos2[i] - (w * datos1[i] + b))  #Derivada parcial de la función con respecto a A

        dl_db += -2 * (datos2[i] - (w * datos1[i] + b))  #Derivada parcial de la función con respecto a B

    #update w and b
    w = w - (1 / N) * dl_dw * alpha
    b = b - (1 / N) * dl_db * alpha

    return w, b


def avg_loss_MSE(datos1, datos2, w, b):
    N = len(datos1)
    total_error = 0.0
    for i in range(N):
        total_error += (datos2[i] - (w * datos1[i] + b))**2  #Función que se quiere optimizar
    return total_error / float(N)


def train(datos1, datos2, w, b, alpha, epoch):
    grafica = MyPlot((datos1, datos2))
    grafica.visualizationTrainProcess2D()

    for e in range(epoch):
        w, b = update_w_b(datos1, datos2, w, b, alpha)

        #log progress
        if e % (4**math.ceil(((5 * (e**2)) / (e**2 + 150 * e + 1)) - 0.3)) == 0 or e == epoch - 1:  #ignorar

            print("epoch:", e, "loss: ", avg_loss_MSE(datos1, datos2, w, b))
            grafica.updateLine2d(w, b)

    grafica.keepOnScreen()

    return w, b


def main():
    #importando tablas de datos
    #temperature_df = pd.read_csv("./res/Salary Data.csv")

    #cargando datos
    #x = np.array(temperature_df['YearsExperience'])
    #y = np.array(temperature_df['Salary'])

    #importando tablas de datos
    temperature_df = pd.read_csv("./res/celsius_a_fahrenheit.csv")

    #cargando datos
    x = np.array(temperature_df['Celsius'])
    y = np.array(temperature_df['Fahrenheit'])

    m, b = train(x, y, 0.0, 0.0, 0.0015, 15000)

    print(m, b)


main()