from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca( projection = '3d' )
x = np.random.sample(20)
y = np.random.sample(20)
ax.scatter(x, y, zs = 0 , zdir = 'y' ,color="r",  label = 'punkty na (x,z)' )
x = np.random.sample(5)
y = np.random.sample(5)
ax.plot(x, y, zs = 0 , zdir = 'z' , label = 'linia na (x,y)' )
ax.legend()
ax.set_xlim( 0 , 1 )
ax.set_ylim( 0 , 1 )
ax.set_zlim( 0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
ax.view_init( elev = 20. , azim =- 35 )
plt.show()