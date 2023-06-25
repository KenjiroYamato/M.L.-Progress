import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

class MyPlot:
    def __init__(self, function):
        self.function = function
        plt.ion()
        self.fig = plt.figure(figsize=(10, 10))
        self.ax = plt.axes(projection='3d')

    def plot(self):
        x = y = np.arange(-6, 6.1, 0.2)
        X, Y = np.meshgrid(x, y)
        ztemp = np.array(self.function(np.ravel(X),np.ravel(Y)))
        Z = ztemp.reshape(X.shape)

        surf = self.ax.plot_surface(X, Y, Z, cmap=plt.cm.cividis, zorder=2.2, alpha=0.5)

        self.ax.set_xlabel('x', labelpad=20)
        self.ax.set_ylabel('y', labelpad=20)
        self.ax.set_zlabel('z', labelpad=20)

        self.fig.colorbar(surf, shrink=0.5, aspect=8)

        for _ in range(10):
            # Updating the value of x and y
            x = 0
            y = random.randint(-5,5)
            z = 1

            # Plotting the new point
            self.ax.scatter(x, y, z, color='red', s=50, zorder=2.5, alpha=1.0)

            # Re-drawing the figure
            self.fig.canvas.draw()

            # To flush the GUI events
            self.fig.canvas.flush_events()
            plt.pause(0.25)

            # Clearing the previous point
            self.ax.collections[1].remove()

def funPrueba(x,y):
    return sum(x**2 + y)

if __name__ == '__main__':    
    grafica = MyPlot(funPrueba)
    grafica.plot()
