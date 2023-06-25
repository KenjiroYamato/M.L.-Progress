
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal
import time
import random
 
# Creating 3D figure
plt.ion()
fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
 
x = np.arange(-6, 6.1, 0.2)
y = np.arange(-6, 6.1, 0.2)

X, Y = np.meshgrid(x, y)
Z = np.sin(X)*np.cos(Y)

surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis, zorder=2.2, alpha=0.5)

# Set axes label
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

fig.colorbar(surf, shrink=0.5, aspect=8)


# 360 Degree view
#for angle in range(0, 360):
#    ax.view_init(angle, 30)
#    plt.draw()
#    plt.pause(.001)

for _ in range(4):
   
    # Updating the value of x and y
    x = 0
    y = random.randint(-5,5)
    z = 1

    # Plotting the new point
    ax.scatter(x, y, z, color='red', s=50, zorder=2.5, alpha=1.0)
    print(ax.collections)

    # Re-drawing the figure
    fig.canvas.draw()

    # To flush the GUI events
    fig.canvas.flush_events()
    time.sleep(1)

    # Clearing the previous point
    ax.collections[1].remove()
    
