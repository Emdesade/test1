import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#ZAD 1
fig = plt.figure()
ax = fig.gca( projection = '3d' )
z =np.linspace(0*np.pi,2)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y,z,  label = 'zadanie 1' )
ax.legend()
plt.show()