import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random


def funPrueba(x, y=0):
    return x**2 + y


def StraightFunction(x, m, b):
    return m * x + b


class MyPlot:

    def __init__(self, function=funPrueba, nprange=np.arange(-6, 6.1, 0.2)):
        self.functionType = None
        self.xRange = None
        self.yRange = None
        self.xFunction = None
        self.yFunction = None

        if type(function) == type((0, 0)):
            self.xFunction = function[0]
            self.yFunction = function[1]
            self.functionType = 1  #funcion tipo nube de puntos
            self.xRange = np.arange(self.xFunction[0], self.xFunction[-1], 0.2)
        if callable(function):
            self.function = function
            self.xRange = nprange
            self.yRange = nprange
            self.functionType = 0  #funcion tipo funcion continua
        else:
            pass  #raise Exception('Function debe ser o una funcion (x,y) -> z o una tupla (X,Y) tipo np.array')

        self.fig = plt.figure(figsize=(10, 9))

        self.ax = None
        self.line = None

    def plot3D(self):
        self.ax = plt.axes(projection='3d')
        x = y = self.xRange
        X, Y = np.meshgrid(x, y)
        ztemp = np.array(self.function(np.ravel(X), np.ravel(Y)))
        Z = ztemp.reshape(X.shape)

        surf = self.ax.plot_surface(X, Y, Z, cmap=plt.cm.cividis, zorder=2.2, alpha=0.5)

        self.ax.set_xlabel('x', labelpad=20)
        self.ax.set_ylabel('y', labelpad=20)
        self.ax.set_zlabel('z', labelpad=20)

        self.fig.colorbar(surf, shrink=0.5, aspect=8)

        point = None
        for _ in range(10):
            if point:
                point.remove()  # Eliminar el punto anterior

            # Updating the value of x, y, and z
            x = 0
            y = random.randint(-5, 5)
            z = 1

            # Plotting the new point
            point = self.ax.scatter(x, y, z, color='red', s=50, zorder=2.5, alpha=1.0)

            # Re-drawing the figure
            self.fig.canvas.draw()

            # To flush the GUI events
            self.fig.canvas.flush_events()
            plt.pause(0.25)

        plt.show()

    def visualizationTrainProcess2D(self):
        self.ax = plt.axes(xlabel='X', ylabel='Y', title='Gráfico')

        if self.functionType == 0:
            x = self.xRange
            y = np.array(self.function(x))
            plt.plot(x, y)

        if self.functionType == 1:
            plt.scatter(self.xFunction, self.yFunction)

    def updateLine2d(self, m, b):

        if self.line:
            self.line.remove()  # Eliminar la línea anterior

        # Updating the value of x and y
        yStraight = StraightFunction

        # Plotting the new straight
        self.line, = plt.plot(self.xRange, yStraight(self.xRange, m, b))

        # Re-drawing the figure
        self.fig.canvas.draw()

        # To flush the GUI events
        self.fig.canvas.flush_events()
        plt.pause(0.25)

    def keepOnScreen(self):
        plt.show()


if __name__ == '__main__':
    datos = (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(type(datos))
    grafica = MyPlot(datos)
    grafica.visualizationTrainProcess2D()
    for _ in range(10):
        grafica.updateLine2d(random.randrange(-5, 5), -2)
    grafica.keepOnScreen()
