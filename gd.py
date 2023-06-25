import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotter3D import MyPlot

#importando tablas de datos
temperature_df = pd.read_csv("./res/celsius_a_fahrenheit.csv")

#cargando datos
x = temperature_df['Celsius']
y = temperature_df['Fahrenheit']

#Visualizacion
sns.scatterplot(x=x, y=y)

plt.show()